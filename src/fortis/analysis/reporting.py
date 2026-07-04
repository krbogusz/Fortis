"""Render a distance summary from staged grades to Markdown.

Presentation for :func:`src.fortis.analysis.grading.grade_stages`: a summary
table with one row per attested stage plus the final, then a per-stage list of
the words that differ. Shared by the derivation CLI and the standalone grader.
"""
from __future__ import annotations

from src.fortis.analysis.grading import Grade, StageGrades

_CAVEAT = (
    "> **Reading the stage rows.** Each intermediate stage is graded by matching the "
    "engine's *rule-time* to the target's *stage-time* — the derived snapshot after all "
    "rules dated ≤ T, against the attested form at stage T. If those two timescales are "
    "not calibrated (e.g. rule times assigned for ordering, target periods from another "
    "scheme), the intermediate rows read low for an alignment reason, not a phonological "
    "one — only the `final` row is independent of that alignment. Where a word carries "
    "both a last-stage form and `final`, those two rows measure the same thing."
)


def distance_summary_line(stages: list[StageGrades]) -> str:
    """A one-line headline built from the ``final`` stage (the reliable metric)."""
    final = next((s for s in stages if s.time is None), None)
    if final is None or final.report.graded == 0:
        return "no final target to grade against"
    r = final.report
    intermediate = [s.label for s in stages if s.time is not None]
    stage_note = f" · stages {', '.join(intermediate)} graded too" if intermediate else ""
    return (
        f"final: {r.exact}/{r.graded} exact ({r.accuracy:.1%}), "
        f"mean phone {r.mean_distance:.3f}, mean feature {r.mean_feature_distance:.3f}"
        f"{stage_note}"
    )


def render_distance_summary(stages: list[StageGrades], where: str) -> str:
    """The whole distance summary as one Markdown document."""
    lines = [
        f"# Distances — {where}",
        "",
        "Engine output vs. attested forms. `d` is the phone edit distance (exact = 0);",
        "`fd` is the feature edit distance (features that differ, so a near-miss scores",
        "far below a gross one). Both drop syllable dots and count an adjacent-segment",
        "swap as one edit.",
        "",
        _CAVEAT,
        "",
        "## Summary",
        "",
        "| stage | graded | exact | ≤1 phone | mean phone | mean feature |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for stage in stages:
        lines.append(_summary_row(stage))
    lines.append("")  # blank line separates the table from the first detail heading
    for stage in stages:
        lines += _detail_section(stage)
    return "\n".join(lines).rstrip() + "\n"


def _summary_row(stage: StageGrades) -> str:
    r = stage.report
    return (
        f"| {stage.label} | {r.graded} | {r.exact} | {r.within_one} "
        f"| {r.mean_distance:.3f} | {r.mean_feature_distance:.3f} |"
    )


def _detail_section(stage: StageGrades) -> list[str]:
    """One stage's per-word detail: the words that differ (exact matches omitted)."""
    report = stage.report
    misses = [g for g in sorted(report.grades, key=lambda g: g.gloss.casefold()) if not g.exact]
    header = [f"## {stage.label}", ""]
    if report.graded == 0:
        return [*header, "No words graded for this stage.", ""]
    if not misses:
        return [*header, f"All {report.graded} graded words exact.", ""]
    return [
        *header,
        f"{len(misses)} of {report.graded} graded words differ (exact matches omitted).",
        "",
        "| gloss | derived | target | d | fd |",
        "| --- | --- | --- | ---: | ---: |",
        *(_detail_row(g) for g in misses),
        "",
    ]


def _detail_row(grade: Grade) -> str:
    feature = "—" if grade.feature_distance is None else str(grade.feature_distance)
    return f"| {grade.gloss or grade.ipa} | `{grade.derived}` | `{grade.target}` | {grade.distance} | {feature} |"
