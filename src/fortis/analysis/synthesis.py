"""Bundle the error analyses for a scoped subset into one ``scoped_output.md`` document.

``--scope`` (and the web Scope tab) restrict the accuracy analyses to the words whose
attested forms match a pattern. Rather than overwrite the whole-lexicon reports, that
subset is synthesised into a single file: the grading summary, the diagnosis snapshot,
the timeline, and the blame — the same four reports, recomputed over the subset. Shared
by the grader CLI and the web helper so they render identically.
"""
from __future__ import annotations

from src.fortis.analysis.blame import blame_all, render_blame
from src.fortis.analysis.diagnosis import (
    diagnose_stages,
    errors_by_time,
    render_diagnosis,
    render_timeline,
)
from src.fortis.analysis.grading import grade_stages
from src.fortis.analysis.reporting import render_distance_summary
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project


def render_scoped(derivations: list[Derivation], project: Project, where: str) -> str:
    """The scoped subset's grading + diagnosis + timeline + blame, in one document.

    Each of the four reports is recomputed over *derivations* (the scoped subset) and
    demoted a level, under a single ``# Scoped`` heading. *where* should already carry
    the scope note (pattern + subset size), so it stamps into every section.
    """
    stages = grade_stages(derivations, project)
    grades = next(s for s in stages if s.time is None).report.grades
    blames = blame_all(derivations, project)
    buckets = errors_by_time(blames)
    stage_diagnoses = diagnose_stages(derivations, project)

    sections = [
        render_distance_summary(stages, where),
        render_diagnosis(grades, project, where),
        render_timeline(buckets, stage_diagnoses, project, where),
        render_blame(blames, where),
    ]
    # Demote each report's leading "# " to "## " so they nest under one "# Scoped".
    demoted = ["#" + section if section.startswith("# ") else section for section in sections]
    header = (
        f"# Scoped — {where}\n\n"
        "Grading, diagnosis, timeline, and blame, recomputed over the scoped subset.\n\n"
    )
    return header + "\n".join(demoted)
