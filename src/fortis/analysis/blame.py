"""Attribute each wrong word to the rule that broke it.

The grader says a word is wrong and by how much; this says *where* in the cascade
it went wrong. Three signals, from most to least trustworthy:

- **Segment-id provenance** (the rule-level culprit). Segments carry stable ids
  through the whole derivation, and each surface segment renders to exactly one phone
  (verified across the Latin lexicon). So a wrong surface phone maps to a segment id,
  and the *last* firing step that changed or introduced that id is the rule that set
  the wrong value. A wrong phone whose segment no rule ever touched is an **omission**
  (it should have changed and nothing did); a target phone with no surface segment at
  all is a **deletion** residual (produced-short, no single rule to name here).

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

from dataclasses import dataclass

from src.fortis.analysis.grading import align, compare, feature_compare, split_phones
from src.fortis.application.deriving import form_at_time
from src.fortis.application.rendering import render_segment, render_syllabified
from src.fortis.application.tiers import lower_tiers
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


def _phone_ids(form: Form) -> list[int]:
    """The stable segment id behind each rendered phone of *form*.

    One id per phone: every surface segment renders to exactly one phone, so the id
    list lines up with :func:`split_phones` of the rendered form.
    """
    return [segment.id for segment in form.segments]


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


def _residuals(derivation: Derivation, target: str, surface: str) -> tuple[Residual, ...]:
    """The wrong phones of *surface* vs *target*, each attributed via segment provenance."""
    surface_ids = _phone_ids(derivation.surface)
    surface_phones = split_phones(surface)
    # Provenance indexes surface_ids by a phone position, which is only valid when the
    # render maps one phone per segment. A tie-bar affricate (one segment → two phones)
    # or a leading stress mark (one phone → no segment) breaks that; rather than blame a
    # misaligned rule, attribution is dropped for the whole word (its residuals still
    # show *what* is wrong, just not *which rule*). A no-op on forms that map 1:1.
    attributable = len(surface_phones) == len(surface_ids)
    residuals: list[Residual] = []
    for op in align(split_phones(target), surface_phones):
        if op.kind == "match":
            continue
        culprit: tuple[str, int | None] | None = None
        if attributable and op.derived_index is not None and op.derived_index < len(surface_ids):
            culprit = _culprit_for_id(derivation, surface_ids[op.derived_index])
        residuals.append(
            Residual(
                expected=op.target,
                got=op.derived,
                culprit=culprit[0] if culprit else None,
                culprit_time=culprit[1] if culprit else None,
                attributed=attributable,
            )
        )
    return tuple(residuals)


def _stage_divergence(derivation: Derivation, project: Project) -> StageDivergence | None:
    """The earliest attested stage whose derived snapshot differs from the record."""
    for time in sorted(derivation.word.stages):
        attested = derivation.word.stages[time]
        form, boundaries = form_at_time(derivation, time)
        derived = _render(form, boundaries, project)
        if compare(derived, attested, project.settings.grading.transposition_cost) > 0:
            return StageDivergence(time=time, attested=attested, derived=derived)
    return None


def _trajectory(derivation: Derivation, project: Project) -> tuple[TrajectoryPoint, ...]:
    """Each firing step's rendered form, scored against the era's attested target.

    A snapshot is compared to the attested stage it is heading toward — the earliest
    ``Word.stages`` time ≥ the step's rule-time — or to ``Word.final`` once past the last
    stage (and for untimed steps). The input heads to the earliest stage; the surface is
    the final. With no attested stages, every point is compared to ``final``.
    """
    swap = project.settings.grading.transposition_cost
    stages = derivation.word.stages
    final = derivation.word.final
    stage_times = sorted(stages)

    def target_at(time: int | None) -> str:
        if time is not None:
            for stage_time in stage_times:  # the earliest attested stage at or after `time`
                if stage_time >= time:
                    return stages[stage_time]
        return final  # untimed step, or past the last attested stage

    input_boundaries = (
        derivation.steps[0].before_boundaries if derivation.steps else derivation.surface_boundaries
    )
    # (label, time, form, target): the input heads to the earliest stage; the surface is final
    # (so its distance still equals the grader's headline).
    rows: list[tuple[str, int | None, str, str]] = [
        (
            "input", None, _render(derivation.input, input_boundaries, project),
            stages[stage_times[0]] if stage_times else final,
        )
    ]
    for step in derivation.steps:
        rows.append((
            step.rule.name or step.rule.id, step.rule.time,
            _render(step.after, step.after_boundaries, project), target_at(step.rule.time),
        ))
    rows.append(
        ("surface", None, _render(derivation.surface, derivation.surface_boundaries, project), final)
    )

    trajectory: list[TrajectoryPoint] = []
    prev_distance: int | None = None
    prev_target: str | None = None
    for label, time, form, target in rows:
        distance = compare(form, target, swap)
        # A regression is only meaningful within one era — a rise against the *same* target.
        regressed = prev_distance is not None and target == prev_target and distance > prev_distance
        trajectory.append(
            TrajectoryPoint(
                label=label, time=time, form=form, target=target, distance=distance,
                feature_distance=feature_compare(form, target, project, swap), regressed=regressed,
            )
        )
        prev_distance, prev_target = distance, target
    return tuple(trajectory)


def blame_word(derivation: Derivation, project: Project) -> Blame | None:
    """Attribute one wrong word, or ``None`` if it has no target or is already exact."""
    target = derivation.word.final
    if target is None:
        return None
    surface = _render(derivation.surface, derivation.surface_boundaries, project)
    distance = compare(surface, target, project.settings.grading.transposition_cost)
    if distance == 0:
        return None
    return Blame(
        gloss=derivation.word.gloss,
        ipa=derivation.word.ipa,
        target=target,
        surface=surface,
        distance=distance,
        residuals=_residuals(derivation, target, surface),
        stage_divergence=_stage_divergence(derivation, project),
        trajectory=_trajectory(derivation, project),
    )


def blame_all(derivations: list[Derivation], project: Project) -> list[Blame]:
    """Attribute every wrong word, worst (largest distance) first."""
    blames = [b for d in derivations if (b := blame_word(d, project)) is not None]
    return sorted(blames, key=lambda b: (-b.distance, b.gloss.casefold()))


def blame_summary_line(blames: list[Blame]) -> str:
    """A one-line headline for stderr, naming the rule blamed for the most words."""
    if not blames:
        return "no wrong words to blame — every graded word is exact"
    counts: dict[str, int] = {}
    for blame in blames:
        for residual in blame.residuals:
            if residual.culprit is not None:
                counts[residual.culprit] = counts.get(residual.culprit, 0) + 1
    if not counts:
        return f"{len(blames)} wrong word(s); no rule-level culprit found — see blame.md"
    worst = max(counts, key=lambda r: counts[r])
    return (
        f"{len(blames)} wrong word(s); rule '{worst}' is behind {counts[worst]} wrong "
        f"phone(s) — see blame.md"
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
    """The full ``blame.md`` report: per wrong word, its residuals, stage, and path."""
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
        lines.append("Every graded word is exact — nothing to blame.")
        return "\n".join(lines).rstrip() + "\n"
    for blame in blames:
        lines += _blame_section(blame)
    return "\n".join(lines).rstrip() + "\n"


def _blame_section(blame: Blame) -> list[str]:
    name = blame.gloss or blame.ipa
    lines = [
        f"## {name} — `{blame.surface}` for `{blame.target}` (distance {blame.distance})",
        "",
        "Residuals: " + "; ".join(_residual_text(r) for r in blame.residuals),
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
