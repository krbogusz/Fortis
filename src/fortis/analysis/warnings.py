"""Collect and render syllabification-fallback warnings.

When a project defines onset/coda patterns, a cluster the patterns cannot legally
divide falls back to the sonority Maximal Onset split (see
:func:`src.fortis.application.syllabifying.syllabification_fallbacks`) so the form
still syllabifies. That is a silent behaviour change worth surfacing: this module
reconstructs, per derived word, whether its **input** or **surface** form needed the
fallback, and renders a Markdown ``warnings.md`` report plus a one-line summary.

Scope: it inspects the input and surface forms only. A fallback on an intermediate
form used solely for a non-firing rule's matching is not separately reported (the
input/surface pair covers the cases that reach the trace).
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.application.rendering import render_segment, render_syllabified
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


def warnings_summary_line(warnings: list[SyllabificationWarning]) -> str:
    """A one-line headline for stderr."""
    if not warnings:
        return "no syllabification warnings"
    words = len({w.ipa for w in warnings})
    return (
        f"⚠ {words} word(s) fell back to sonority syllabification "
        f"(onset/coda patterns admitted no split) — see warnings.md"
    )


def render_warnings(warnings: list[SyllabificationWarning], where: str) -> str:
    """The full ``warnings.md`` report."""
    lines = [
        f"# Warnings — {where}",
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
        "| word | form | cluster(s) | syllabified as |",
        "| --- | --- | --- | --- |",
    ]
    for w in warnings:
        name = w.gloss or w.ipa
        clusters = ", ".join(f"`{c}`" for c in w.clusters)
        lines.append(f"| {name} | {w.stage} | {clusters} | `{w.syllabified}` |")
    return "\n".join(lines).rstrip() + "\n"
