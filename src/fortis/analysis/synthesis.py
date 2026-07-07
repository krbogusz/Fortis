"""Bundle the error analyses for a scoped subset into one ``scoped_output.md`` document.

``--scope`` (and the web Scope tab) restrict the accuracy analyses to the words whose
attested forms match a pattern. Rather than overwrite the whole-lexicon reports, that
subset is synthesised into a single file: the accuracy summary, the errors (per-stage
confusions), the error context (per-stage autopsy), and the blame — the same four reports,
recomputed over the subset. Shared by the grader CLI and the web helper so they render identically.
"""
from __future__ import annotations

from src.fortis.analysis.accuracy import StageAccuracy, accuracy_by_stage
from src.fortis.analysis.blame import blame_all, render_blame
from src.fortis.analysis.diagnosis import (
    diagnose_stages,
    render_error_context_md,
    render_errors_md,
)
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project


def _accuracy_section(stages: list[StageAccuracy], where: str) -> str:
    """A compact Markdown accuracy table (per-stage) for the scoped bundle.

    The standalone accuracy analysis is CSV-only; this small inline table exists just so
    the scoped_output.md synthesis carries an accuracy overview beside the other reports.
    """
    lines = [
        f"# Accuracy — {where}",
        "",
        "| stage | assessed | exact | ≤1 phone | mean phone | mean feature |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for s in stages:
        r = s.report
        lines.append(
            f"| {s.label} | {r.assessed} | {r.exact} | {r.within_one} "
            f"| {r.mean_distance:.3f} | {r.mean_feature_distance:.3f} |"
        )
    return "\n".join(lines) + "\n"


def render_scoped(derivations: list[Derivation], project: Project, where: str) -> str:
    """The scoped subset's accuracy + errors + error context + blame, in one document.

    Each of the four reports is recomputed over *derivations* (the scoped subset) and
    demoted a level, under a single ``# Scoped`` heading. *where* should already carry
    the scope note (pattern + subset size), so it stamps into every section.
    """
    stages = accuracy_by_stage(derivations, project)
    blames = blame_all(derivations, project)
    stage_diagnoses = diagnose_stages(derivations, project)

    sections = [
        _accuracy_section(stages, where),
        render_errors_md(stage_diagnoses, where),
        render_error_context_md(stage_diagnoses, project, where),
        render_blame(blames, where),
    ]
    # Demote each report's leading "# " to "## " so they nest under one "# Scoped".
    demoted = ["#" + section if section.startswith("# ") else section for section in sections]
    header = (
        f"# Scoped — {where}\n\n"
        "Accuracy, errors, error context, and blame, recomputed over the scoped subset.\n\n"
    )
    return header + "\n".join(demoted)
