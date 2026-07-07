"""Render the accuracy analysis: a one-line headline and the two CSV reports.

The accuracy analysis scores each derived form against its attested target via a
distance to target (phone and feature edit distance), per attested stage and the
final. It is reported as two CSV files — a per-stage summary
(:func:`render_accuracy_csv`) and a per-word long table
(:func:`render_distance_to_target_csv`) — plus a stderr headline
(:func:`accuracy_summary_line`). Shared by the derivation CLI and the standalone
grader. See :func:`src.fortis.analysis.accuracy.accuracy_by_stage` for the data.
"""
from __future__ import annotations

import csv
import io

from src.fortis.analysis.accuracy import StageAccuracy


def accuracy_summary_line(stages: list[StageAccuracy]) -> str:
    """A one-line headline built from the ``final`` stage (the reliable metric)."""
    final = next((s for s in stages if s.time is None), None)
    if final is None or final.report.assessed == 0:
        return "no final target to measure against"
    r = final.report
    intermediate = [s.label for s in stages if s.time is not None]
    stage_note = f" · stages {', '.join(intermediate)} measured too" if intermediate else ""
    weighted = (
        f", token-weighted {r.weighted_accuracy:.1%}" if r.frequencies_vary else ""
    )
    return (
        f"final: {r.exact}/{r.assessed} exact ({r.accuracy:.1%}){weighted}, "
        f"mean phone {r.mean_distance:.3f}, mean feature {r.mean_feature_distance:.3f}"
        f"{stage_note}"
    )


def render_accuracy_csv(stages: list[StageAccuracy]) -> str:
    """The per-stage accuracy summary as CSV — one row per attested stage plus the final.

    Columns: ``stage, assessed, exact, within 1, mean phone dist, mean feature dist``
    (``assessed`` = words carrying a target to measure against).
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(
        ["stage", "assessed", "exact", "within 1", "mean phone dist", "mean feature dist"]
    )
    for stage in stages:
        r = stage.report
        writer.writerow([
            stage.label, r.assessed, r.exact, r.within_one,
            f"{r.mean_distance:.3f}", f"{r.mean_feature_distance:.3f}",
        ])
    return buffer.getvalue()


def render_distance_to_target_csv(stages: list[StageAccuracy]) -> str:
    """Every assessed word at every stage as CSV — the long-format distance-to-target detail.

    Columns: ``stage, gloss, derived, target, d, fd`` (``d`` = phone distance,
    ``fd`` = feature distance, empty when the form could not be segmented). Keeps every
    assessed word (exact matches included), so the file is a complete table for analysis.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["stage", "gloss", "derived", "target", "d", "fd"])
    for stage in stages:
        for g in stage.report.distances:
            fd = "" if g.feature_distance is None else g.feature_distance
            writer.writerow([stage.label, g.gloss or g.ipa, g.derived, g.target, g.distance, fd])
    return buffer.getvalue()
