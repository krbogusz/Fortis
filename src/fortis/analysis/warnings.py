"""Collect and render the warnings — silent behaviour changes worth surfacing.

Two kinds, both cases of the engine quietly doing something other than what the rules
appear to say:

* **Syllabification fallback.** When a project defines onset/coda patterns, a cluster the
  patterns cannot legally divide falls back to the sonority Maximal Onset split (see
  :func:`src.fortis.application.syllabifying.syllabification_fallbacks`) so the form still
  syllabifies. Reported per word, at its input and surface forms.

* **Unspellable segments.** A segment whose features no letter can express renders as ``�``.

  It used to render as the nearest letter, with the leftover features silently dropped, and
  that made the one failure the engine cannot otherwise show you invisible: the symbol in the
  trace was not the segment being held — and it was a *plausible* symbol. A bundle one feature
  away from ``ɑ`` printed as an ordinary ``ɑ``, while no rule written ``ɑ → …`` would ever
  match it, because rendering is lossy and many-to-one but a letter PATTERN matches by exact
  identity. The rule fired on some words and passed silently over identical-looking others.

  The usual cause is a merge that changed a segment's quality and left a feature of the old
  quality behind — a merge keeps every feature it does not mention, so un-rounding *o with
  ``rounded: none`` and forgetting ``labial: none`` yields an ``ɑ`` that is still labial. The
  report names the near-miss letter AND the rule that produced the segment, which together
  turn the mystery into a one-line fix.

Scope: syllabification inspects the input and surface forms only. A fallback on an
intermediate form used solely for a non-firing rule's matching is not separately reported
(the input/surface pair covers the cases that reach the trace). Unspellable segments are
checked at every step of every derivation, so a segment that appears mid-cascade and is
gone by the surface is still caught.
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.application.rendering import (
    render_nearest,
    render_residue,
    render_segment,
    render_syllabified,
)
from src.fortis.application.syllabifying import syllabification_fallbacks, syllabify
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation
from src.fortis.models.form import Form
from src.fortis.models.project import Project


@dataclass(frozen=True)
class SyllabificationWarning:
    """One word whose syllabification fell back to sonority under the defined patterns."""

    ipa: str
    gloss: str
    stage: str  # "input" or "surface" — which form needed the fallback
    form: str  # the exact (unsyllabified) form this warning fired on
    clusters: tuple[str, ...]  # the offending cluster(s), rendered
    syllabified: str  # the resulting (fallback) syllabification


def _cluster_text(bundles: list[FeatureBundle], start: int, end: int, project: Project) -> str:
    """Render the raw segments of a fallen-back cluster (no syllable dots)."""
    return "".join(render_segment(b, project) for b in bundles[start:end])


def _stage_warning(
    ipa: str, gloss: str, stage: str, form: Form, time: int | None, project: Project
) -> SyllabificationWarning | None:
    """A warning for *form* at *time*, or ``None`` if its patterns syllabified it cleanly."""
    bundles = lower_tiers(form)
    spans = syllabification_fallbacks(
        bundles, project.sonorities, project.syllable_parts, time, project.letters
    )
    if not spans:
        return None
    boundaries = syllabify(
        bundles, project.sonorities, project.syllable_parts, time, project.letters
    )
    return SyllabificationWarning(
        ipa=ipa,
        gloss=gloss,
        stage=stage,
        form=render_syllabified(bundles, boundaries, project, dots=False),
        clusters=tuple(_cluster_text(bundles, s, e, project) for s, e in spans),
        syllabified=render_syllabified(bundles, boundaries, project),
    )


def syllabification_warnings(
    derivations: list[Derivation], project: Project
) -> list[SyllabificationWarning]:
    """Every word whose input or surface form needed the sonority fallback.

    Reported once per (word, stage): a word is checked at its input form (the
    derivation's start time) and its surface form (the latest rule time). A word clean
    at both is omitted. With no sonority scale or syllable parts there is nothing to
    fall back from, so the result is empty.
    """
    if project.sonorities is None or project.syllable_parts is None:
        return []
    latest = max((t for t in project.rules if t is not None), default=0)
    warnings: list[SyllabificationWarning] = []
    seen: set[tuple[str, tuple[str, ...], str]] = set()
    for derivation in derivations:
        word = derivation.word
        for stage, form, time in (
            ("input", derivation.input, project.time),
            ("surface", derivation.surface, latest),
        ):
            warning = _stage_warning(word.ipa, word.gloss, stage, form, time, project)
            if warning is None:
                continue
            # Collapse the common case where input and surface fall back identically.
            key = (warning.ipa, warning.clusters, warning.syllabified)
            if key in seen:
                continue
            seen.add(key)
            warnings.append(warning)
    return warnings


@dataclass(frozen=True)
class RenderingWarning:
    """A segment the letter inventory cannot spell — rendered as the nearest letter instead.

    Such a segment now renders as ``�``. ``nearest`` is the letter it is a near-miss for — the
    letter it would silently have been mistaken for, and the one whose rules will not match it.
    ``dropped`` are the features that letter cannot express. ``rule`` is the rule that produced
    the segment (or ``"input"``), which is nearly always where the fix belongs.
    """

    nearest: str  # the near-miss letter — e.g. "ɑ"
    dropped: tuple[str, ...]  # features it carries that the letter cannot — e.g. ("labial",)
    rule: str  # the rule that produced it, or "input"
    words: tuple[str, ...]  # example glosses
    count: int  # how many (word, step) sites


def rendering_warnings(
    derivations: list[Derivation], project: Project, *, examples: int = 3
) -> list[RenderingWarning]:
    """Every segment in every derivation whose rendered symbol drops features.

    Grouped by (near-miss letter, dropped features) — one row per distinct DEFECT, not one per
    site, because a single leaky merge marks thousands of segments. The rule reported is the
    FIRST one to produce the defect, which is the one to fix: every later rule that touches the
    segment re-emits it (changing its stress is enough to make the bundle look new), so blaming
    each of them turns one leaky merge into a dozen innocent suspects. Ordered by count.
    """
    # (nearest, dropped) -> [count, example glosses, first rule seen]
    found: dict[tuple[str, tuple[str, ...]], list] = {}

    def note(bundle: FeatureBundle, rule: str, gloss: str) -> None:
        residue = render_residue(bundle, project)
        if not residue:
            return
        key = (render_nearest(bundle, project), tuple(sorted(residue)))
        entry = found.setdefault(key, [0, [], rule])
        entry[0] += 1
        if gloss not in entry[1] and len(entry[1]) < examples:
            entry[1].append(gloss)

    for derivation in derivations:
        gloss = derivation.word.gloss or derivation.word.ipa
        # The input, before any rule has run: a defect here is in the lexicon or the letters.
        for segment in lower_tiers(derivation.input):
            note(segment, "input", gloss)
        # Then each firing rule — but blame only the rule that INTRODUCED the defect, not the
        # ones that inherit it. A defect is new to a step when no segment the step started with
        # already carried that same residue; otherwise the rule merely touched a segment that
        # was already broken. Comparing the segments themselves is not enough: changing ANY
        # feature (even lengthening the vowel, or restressing the syllable it sits in) makes the
        # bundle look new, so every later rule got blamed too and one leaky merge turned into a
        # dozen innocent suspects. It is the RESIDUE whose first appearance we want.
        for step in derivation.steps:
            already = {render_residue(s, project) for s in lower_tiers(step.before)}
            for segment in lower_tiers(step.after):
                if render_residue(segment, project) not in already:
                    note(segment, step.rule.name, gloss)

    return sorted(
        (
            RenderingWarning(
                nearest=nearest, dropped=dropped, rule=rule, words=tuple(words), count=count
            )
            for (nearest, dropped), (count, words, rule) in found.items()
        ),
        key=lambda w: (-w.count, w.nearest, w.rule),
    )


def warnings_summary_line(
    warnings: list[SyllabificationWarning], rendering: list[RenderingWarning] | None = None
) -> str:
    """A one-line headline for stderr."""
    parts = []
    if warnings:
        words = len({w.ipa for w in warnings})
        parts.append(
            f"⚠ {words} word(s) fell back to sonority syllabification "
            f"(onset/coda patterns admitted no split)"
        )
    if rendering:
        sites = sum(w.count for w in rendering)
        worst = rendering[0]
        parts.append(
            f"⚠ {len(rendering)} unspellable segment(s), {sites} site(s) — no letter can "
            f"express them, so they render as �; worst: "
            f"nearest '{worst.nearest}' loses {'/'.join(worst.dropped)} from '{worst.rule}'"
        )
    if not parts:
        return "no warnings"
    return " · ".join(parts) + " — see warnings.md"


def render_warnings(
    warnings: list[SyllabificationWarning],
    where: str,
    rendering: list[RenderingWarning] | None = None,
) -> str:
    """The full ``warnings.md`` report."""
    lines = [f"# Warnings — {where}", ""]

    if rendering:
        lines += [
            "## Unspellable segments",
            "",
            "These segments carry features **no letter can express**, so they render as `�`.",
            "",
            "They used to render as the nearest letter, with the leftover features silently",
            "dropped — which made the one failure the engine cannot otherwise show you invisible.",
            "A bundle one feature away from `ɑ` printed as a perfectly ordinary `ɑ`, and yet **no",
            "rule written `ɑ → …` would ever match it**, because rendering is lossy and",
            "many-to-one while a letter PATTERN matches by exact identity. The rule fired on some",
            "words and passed silently over identical-looking others, with no error anywhere.",
            "",
            "The **mistaken for** column is the letter each one is a near-miss of — the letter it",
            "used to print as, and the letter whose rules will not match it.",
            "",
            "The usual cause is in the **rule named below**: a merge changed a segment's quality",
            "and left a feature of the old quality behind. A merge keeps every feature it does not",
            "mention, so un-rounding `o` with `rounded: none` and forgetting `labial: none` leaves",
            "an `ɑ` that is still labial. Clear the whole set of features that go with the quality",
            "you are changing (`rounded` **and** `labial`; `front` **and** `back`) — or, if the",
            "segment is real, add a letter or diacritic that can spell it.",
            "",
            "| renders as | mistaken for | features it carries that the letter cannot "
            "| produced by | sites | examples |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for r in rendering:
            dropped = ", ".join(f"`{f}`" for f in r.dropped)
            words = ", ".join(r.words)
            lines.append(
                f"| `�` | `{r.nearest}` | {dropped} | `{r.rule}` | {r.count} | {words} |"
            )
        lines.append("")

    lines += [
        "## Syllabification fallback",
        "",
        "Syllabification fell back to the **sonority Maximal Onset** division for the words",
        "below: the project's onset/coda patterns admitted no legal split for the listed",
        "cluster, so the sonority-based division was used instead (rather than leaving the",
        "word unsyllabified). Loosen the onset/coda patterns to cover these clusters, or",
        "accept the sonority fallback.",
        "",
    ]
    if not warnings:
        lines.append("No syllabification fell back — every word matched the onset/coda patterns.")
        return "\n".join(lines).rstrip() + "\n"
    lines += [
        "| word | gloss | form | cluster | syllabified as |",
        "| --- | --- | --- | --- | --- |",
    ]
    for w in warnings:
        clusters = ", ".join(f"`{c}`" for c in w.clusters)
        lines.append(f"| `{w.ipa}` | {w.gloss} | `{w.form}` | {clusters} | `{w.syllabified}` |")
    return "\n".join(lines).rstrip() + "\n"
