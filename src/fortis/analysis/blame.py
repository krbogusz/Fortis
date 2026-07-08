"""Attribute each wrong word to the rule that broke it.

The grader says a word is wrong and by how much; this says *where* in the cascade
it went wrong. Three signals, from most to least trustworthy:

- **Segment-id provenance** (the rule-level culprit). Segments carry stable ids
  through the whole derivation, and blame works on *inventory segments* (one phone per
  segment by construction — an affricate ``d͡ʒ`` is one), so a wrong surface phone maps
  straight to its segment id, and the *last* firing step that changed or introduced that
  id is the rule that set the wrong value. A wrong phone whose segment no rule ever touched
  is an **omission** (it should have changed and nothing did); a target phone with no
  surface segment at all is a **deletion** residual (produced-short, no single rule here).

- **Stage divergence** (ground truth, where the lexicon has it). For a word carrying
  attested ``stages``, the earliest stage whose derived snapshot differs from the
  attested form localizes the first divergence to a period — independent of the
  derivation's own trace. Shown alongside the provenance culprit as corroboration.

- **Distance trajectory** (context only). The rendered form after each firing step and
  its phone distance to the target. Distance to the *final* target is not monotone
  mid-cascade — a rule may correctly move a form further from its eventual shape — so a
  rise is flagged but never used to *name* the culprit; it is there to read the path.

The trajectory's final point is ``derivation.surface`` (after ``derive``'s closing
tier cleanup), not the last step's ``after`` — so its distance equals the grader's.
"""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass

from src.fortis.analysis.accuracy import (
    align,
    comparable_bundles,
    edit_distance,
    feature_edit_distance,
    form_phones,
)
from src.fortis.application.deriving import form_at_time
from src.fortis.application.rendering import render_segment, render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import is_morpheme_boundary
from src.fortis.models.derivation import Derivation
from src.fortis.models.form import Form
from src.fortis.models.project import Project


@dataclass(frozen=True)
class Residual:
    """One wrong phone at the surface and the rule that produced it.

    ``expected``/``got`` are the target and surface phones (``None`` on the absent
    side: ``got is None`` for a target phone never produced, ``expected is None`` for a
    spurious inserted one). ``culprit``/``culprit_time`` name the last firing rule that
    set or introduced the phone's segment; both ``None`` means the segment was never
    touched (an omission) or has no surface segment (a deletion residual).

    ``attributed`` is ``False`` when provenance could not run for the word — the rendered
    surface did not map one phone per segment (a tie-bar affricate splits into two
    phones, a leading stress mark adds one with no segment), so an index-based culprit
    would be misaligned. Then ``culprit`` is left ``None`` and the residual is reported
    without a rule rather than blaming the wrong one.
    """

    expected: str | None
    got: str | None
    culprit: str | None
    culprit_time: int | None
    attributed: bool = True

    @property
    def kind(self) -> str:
        """The correspondence kind: ``insertion``, ``deletion``, or ``substitution``."""
        if self.expected is None:
            return "insertion"
        if self.got is None:
            return "deletion"
        if not self.attributed:
            return "substitution"  # wrong phone; which rule is unavailable, not an omission
        return "omission" if self.culprit is None else "substitution"


@dataclass(frozen=True)
class StageDivergence:
    """The earliest attested stage whose derived snapshot diverges from the record."""

    time: int
    attested: str
    derived: str


@dataclass(frozen=True)
class TrajectoryPoint:
    """The rendered form after one firing step, scored against the era's attested target.

    ``target`` is the attested form this point is measured against — the stage the
    derivation is heading toward here (the earliest ``Word.stages`` time ≥ the point's
    rule-time), or ``Word.final`` once past the last stage — so an intermediate snapshot
    is compared to the temporally-appropriate attested form, not the final one. ``distance``
    and ``feature_distance`` are the phone and feature edit distances to that ``target``.
    """

    label: str
    time: int | None
    form: str
    target: str
    distance: int
    feature_distance: int | None
    regressed: bool  # distance rose against the SAME target (a lead, never the culprit)


@dataclass(frozen=True)
class Blame:
    """Why one word came out wrong: its residual phones, stage divergence, and path."""

    gloss: str
    ipa: str
    target: str
    surface: str
    distance: int
    residuals: tuple[Residual, ...]
    stage_divergence: StageDivergence | None
    trajectory: tuple[TrajectoryPoint, ...]


def _render(form: Form, boundaries, project: Project) -> str:
    """Render a form to its surface string (the same path the grader compares)."""
    return render_syllabified(lower_tiers(form), boundaries, project)


def _surface_phones_and_ids(form: Form, project: Project) -> tuple[list[str], list[int]]:
    """The surface's phones and the segment id behind each — one per non-boundary segment.

    ``lower_tiers`` yields one bundle per segment in order (aligned with ``form.segments``), so
    rendering each and taking the matching id gives a *structural* one-phone-per-segment
    correspondence: a wrong phone maps straight to its segment id, no length check needed. This
    is why blame works on inventory segments rather than the codepoint split — an affricate
    ``d͡ʒ`` is one segment/one phone, so the id alignment can't come apart on it.
    """
    phones: list[str] = []
    ids: list[int] = []
    for bundle, segment in zip(lower_tiers(form), form.segments, strict=True):
        if is_morpheme_boundary(bundle):
            continue  # a morpheme boundary is structural, not a phone (and has no rule to blame)
        phones.append(render_segment(bundle, project))
        ids.append(segment.id)
    return phones, ids


def _culprit_for_id(derivation: Derivation, seg_id: int) -> tuple[str, int | None] | None:
    """The last firing rule that changed or introduced the segment *seg_id*.

    Returns ``(rule_id, time)`` or ``None`` if no step ever touched the segment (it
    kept its input value throughout — an omission).
    """
    culprit: tuple[str, int | None] | None = None
    for step in derivation.steps:
        before = {seg.id: seg.bundle for seg in step.before.segments}
        after = {seg.id: seg.bundle for seg in step.after.segments}
        if seg_id in after and (seg_id not in before or before[seg_id] != after[seg_id]):
            culprit = (step.rule.id, step.rule.time)
    return culprit


def _residuals(derivation: Derivation, target_form: Form, project: Project) -> tuple[Residual, ...]:
    """The wrong phones of the surface vs the attested target, each attributed via segment id.

    Both sides are inventory segments (:func:`form_phones`), so the surface phone ↔ segment-id
    correspondence is exact and attribution is always available (no degrade path): each wrong
    surface phone maps to its segment id, thence to the last rule that set it. A target phone
    with no surface counterpart is a deletion — nothing produced it, so there is no rule to name.
    """
    surface_phones, surface_ids = _surface_phones_and_ids(derivation.surface, project)
    residuals: list[Residual] = []
    for op in align(form_phones(target_form, project), surface_phones):
        if op.kind == "match":
            continue
        culprit: tuple[str, int | None] | None = None
        if op.derived_index is not None and op.derived_index < len(surface_ids):
            culprit = _culprit_for_id(derivation, surface_ids[op.derived_index])
        residuals.append(
            Residual(
                expected=op.target,
                got=op.derived,
                culprit=culprit[0] if culprit else None,
                culprit_time=culprit[1] if culprit else None,
                attributed=True,
            )
        )
    return tuple(residuals)


def _stage_divergence(derivation: Derivation, project: Project) -> StageDivergence | None:
    """The earliest attested stage whose derived snapshot differs from the record."""
    swap = project.settings.accuracy.transposition_cost
    for time in sorted(derivation.word.stages):
        target_form = derivation.word.stage_forms.get(time)
        if target_form is None:  # attested stage the inventory could not segment — skip (warned)
            continue
        form, boundaries = form_at_time(derivation, time)
        if edit_distance(form_phones(target_form, project), form_phones(form, project), swap) > 0:
            return StageDivergence(
                time=time,
                attested=derivation.word.stages[time],
                derived=_render(form, boundaries, project),
            )
    return None


def _trajectory(derivation: Derivation, project: Project) -> tuple[TrajectoryPoint, ...]:
    """Each firing step's rendered form, scored against the era's attested target.

    A snapshot is compared to the attested stage it is heading toward — the earliest
    ``Word.stages`` time ≥ the step's rule-time — or to ``Word.final`` once past the last
    stage (and for untimed steps). The input heads to the earliest stage; the surface is
    the final. With no attested stages, every point is compared to ``final``.
    """
    swap = project.settings.accuracy.transposition_cost
    word = derivation.word
    final_form = word.final_form
    assert final_form is not None  # blame_word guards that word.final_form is set before calling
    stage_times = sorted(word.stages)

    def target_at(time: int | None) -> tuple[str, Form]:
        # The attested (string, ingested form) an era heads toward — the earliest stage ≥ time,
        # else the final. An unsegmentable stage form falls back to the final so the point still
        # scores against a real target.
        if time is not None:
            for stage_time in stage_times:
                if stage_time >= time:
                    return word.stages[stage_time], word.stage_forms.get(stage_time) or final_form
        return word.final or "", final_form

    input_boundaries = (
        derivation.steps[0].before_boundaries if derivation.steps else derivation.surface_boundaries
    )
    # (label, time, form, boundaries, target string, target form): input heads to the earliest
    # stage; the surface is the final (so its distance equals the grader's headline).
    input_target = (
        (word.stages[stage_times[0]], word.stage_forms.get(stage_times[0]) or final_form)
        if stage_times
        else (word.final or "", final_form)
    )  # the input heads to the earliest attested stage (any time), else the final
    rows: list[tuple[str, int | None, Form, frozenset[int], str, Form]] = [
        ("input", None, derivation.input, input_boundaries, *input_target)
    ]
    for step in derivation.steps:
        rows.append(
            (
                step.rule.name or step.rule.id,
                step.rule.time,
                step.after,
                step.after_boundaries,
                *target_at(step.rule.time),
            )
        )
    rows.append(
        (
            "surface",
            None,
            derivation.surface,
            derivation.surface_boundaries,
            word.final or "",
            final_form,
        )
    )

    trajectory: list[TrajectoryPoint] = []
    prev_distance: int | None = None
    prev_target: str | None = None
    for label, time, form, boundaries, target_str, target_form in rows:
        distance = edit_distance(
            form_phones(form, project), form_phones(target_form, project), swap
        )
        feature_distance = feature_edit_distance(
            comparable_bundles(form), comparable_bundles(target_form), swap
        )
        # A regression is only meaningful within one era — a rise against the *same* target.
        regressed = (
            prev_distance is not None and target_str == prev_target and distance > prev_distance
        )
        trajectory.append(
            TrajectoryPoint(
                label=label,
                time=time,
                form=_render(form, boundaries, project),
                target=target_str,
                distance=distance,
                feature_distance=feature_distance,
                regressed=regressed,
            )
        )
        prev_distance, prev_target = distance, target_str
    return tuple(trajectory)


def blame_word(
    derivation: Derivation, project: Project, include_exact: bool = False
) -> Blame | None:
    """Attribute one assessed word, or ``None`` if it has no target or is unsegmentable.

    Uses the ingested ``final_form`` (segment-based, so an affricate is one unit and the phone
    distance equals the grader's). Assumes :func:`src.fortis.analysis.accuracy.ingest_targets`
    has run; a word whose ``final`` the inventory could not segment is skipped (warned there).
    An exact word (distance 0) returns ``None`` by default; pass ``include_exact=True`` to get a
    residual-free ``Blame`` for it too, so a caller can list every assessed word, not only wrong
    ones.
    """
    word = derivation.word
    if word.final is None or word.final_form is None:
        return None
    swap = project.settings.accuracy.transposition_cost
    surface = _render(derivation.surface, derivation.surface_boundaries, project)
    distance = edit_distance(
        form_phones(word.final_form, project), form_phones(derivation.surface, project), swap
    )
    if distance == 0 and not include_exact:
        return None
    return Blame(
        gloss=word.gloss,
        ipa=word.ipa,
        target=word.final,
        surface=surface,
        distance=distance,
        residuals=_residuals(derivation, word.final_form, project),
        stage_divergence=_stage_divergence(derivation, project),
        trajectory=_trajectory(derivation, project),
    )


def blame_all(
    derivations: list[Derivation], project: Project, include_exact: bool = False
) -> list[Blame]:
    """Attribute every wrong word (or every assessed word when *include_exact*), worst first."""
    blames = [b for d in derivations if (b := blame_word(d, project, include_exact)) is not None]
    return sorted(blames, key=lambda b: (-b.distance, b.gloss.casefold()))


def blame_summary_line(blames: list[Blame]) -> str:
    """A one-line headline for stderr, naming the rule blamed for the most wrong words.

    Counts only the wrong words (distance > 0), so it reads the same whether *blames* holds
    just the wrong words or every assessed word (exact ones carry distance 0).
    """
    wrong = [b for b in blames if b.distance > 0]
    if not wrong:
        return "no wrong words to blame — every assessed word is exact"
    counts: dict[str, int] = {}
    for blame in wrong:
        for residual in blame.residuals:
            if residual.culprit is not None:
                counts[residual.culprit] = counts.get(residual.culprit, 0) + 1
    if not counts:
        return f"{len(wrong)} wrong word(s); no rule-level culprit found — see blame.csv"
    worst = max(counts, key=lambda r: counts[r])
    return (
        f"{len(wrong)} wrong word(s); rule '{worst}' is behind {counts[worst]} wrong "
        f"phone(s) — see blame.csv"
    )


def _residual_text(residual: Residual) -> str:
    """One residual as ``expected→got (rule)`` with ∅ for an absent side."""
    expected = residual.expected if residual.expected is not None else "∅"
    got = residual.got if residual.got is not None else "∅"
    if residual.culprit is not None:
        time = "" if residual.culprit_time is None else f", t={residual.culprit_time}"
        return f"`{expected}`→`{got}` ({residual.culprit}{time})"
    if not residual.attributed:
        return f"`{expected}`→`{got}` (unattributed)"
    return f"`{expected}`→`{got}` ({residual.kind})"


def render_blame(blames: list[Blame], where: str) -> str:
    """Blame as Markdown — per word, its residuals, stage, and path (for the --scope bundle).

    The standalone blame output is ``blame.csv`` (:func:`render_blame_csv`); this Markdown
    rendering is what the ``--scope`` synthesis carries into ``scoped_output.md``.
    """
    lines = [
        f"# Blame — {where}",
        "",
        "Each wrong word attributed to the rule that produced the wrong phone. The",
        "**culprit** of a residual is the last firing rule that set or introduced that",
        "phone's segment (via stable segment ids); *omission* means no rule ever touched",
        "it, *deletion* that the target phone was never produced — this is the headline",
        "signal. Where the lexicon has an attested intermediate **stage**, the first",
        "diverging stage is shown too, but trust it only where the attested stage forms",
        "are notationally comparable to the engine's output: if they use reconstructive",
        "notation the engine never emits (stress placement, length, θ/ə…), an early",
        "‘divergence’ is a notation artifact, not a real error. The **trajectory** is",
        "context — each step's form against the attested form of the era it is heading",
        "toward (the **target** column), with phone (**d**) and feature (**fd**) distances;",
        "a rise against the same target (⤴) is a lead, not the culprit.",
        "",
    ]
    if not blames:
        lines.append("Every assessed word is exact — nothing to blame.")
        return "\n".join(lines).rstrip() + "\n"
    for blame in blames:
        lines += _blame_section(blame)
    return "\n".join(lines).rstrip() + "\n"


def _blame_section(blame: Blame) -> list[str]:
    name = blame.gloss or blame.ipa
    residuals = "; ".join(_residual_text(r) for r in blame.residuals) or "none — exact at the final"
    lines = [
        f"## {name} — `{blame.surface}` for `{blame.target}` (distance {blame.distance})",
        "",
        "Residuals: " + residuals,
        "",
    ]
    if blame.stage_divergence is not None:
        sd = blame.stage_divergence
        lines += [
            f"First diverges at stage t={sd.time}: attested `{sd.attested}`, "
            f"derived `{sd.derived}`.",
            "",
        ]
    lines += ["| step | t | form | target | d | fd |", "| --- | ---: | --- | --- | ---: | ---: |"]
    for point in blame.trajectory:
        time = "" if point.time is None else str(point.time)
        mark = " ⤴" if point.regressed else ""
        fd = "—" if point.feature_distance is None else str(point.feature_distance)
        lines.append(
            f"| {point.label}{mark} | {time} | `{point.form}` | `{point.target}` "
            f"| {point.distance} | {fd} |"
        )
    lines.append("")
    return lines


def render_blame_csv(blames: list[Blame]) -> str:
    """The per-word distance trajectory as CSV — one row per word × trajectory point.

    Columns: ``gloss, step, regression, t, form, target, d, fd``. *step* is the trajectory label
    (``input``, a firing rule's name, or ``surface``); *regression* is ``true`` where this step's
    distance rose against the same target (a lead, never the culprit) and blank otherwise; *t* its
    rule-time (blank for the untimed ends); *form*/*target* the rendered form and the attested form
    of the era it heads toward; *d*/*fd* the phone and feature distances. Every assessed word
    appears — a wrong word as its full path, an exact word (when blamed with ``include_exact``) as
    a short, ``d=0`` trajectory.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["gloss", "step", "regression", "t", "form", "target", "d", "fd"])
    for blame in blames:
        gloss = blame.gloss or blame.ipa
        for point in blame.trajectory:
            writer.writerow([
                gloss,
                point.label,
                "true" if point.regressed else "",
                "" if point.time is None else point.time,
                point.form,
                point.target,
                point.distance,
                "" if point.feature_distance is None else point.feature_distance,
            ])
    return buffer.getvalue()
