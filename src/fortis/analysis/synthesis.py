"""Bundle the error analyses for a scoped subset into one ``scoped_output.md`` document.

``--scope`` (and the web Scope tab) restrict the accuracy analyses to the words whose
attested forms match a pattern. Rather than overwrite the whole-lexicon reports, that
subset is synthesised into a single file: the accuracy summary and the blame, recomputed
over the subset. (The per-stage errors and error context are CSV-only — ``errors.csv`` and
``error_context.csv`` — so they are not carried into this Markdown bundle.) Shared by the
grader CLI and the web helper so they render identically.
"""
from __future__ import annotations

from src.fortis.analysis.accuracy import StageAccuracy, accuracy_by_stage
from src.fortis.analysis.blame import blame_all, render_blame
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
    """The scoped subset's accuracy + blame, in one document.

    Each report is recomputed over *derivations* (the scoped subset) and demoted a level,
    under a single ``# Scoped`` heading. *where* should already carry the scope note
    (pattern + subset size), so it stamps into every section. The per-stage errors and
    error context stay CSV-only and are not included here.
    """
    stages = accuracy_by_stage(derivations, project)
    blames = blame_all(derivations, project)

    sections = [
        _accuracy_section(stages, where),
        render_blame(blames, where),
    ]
    # Demote each report's leading "# " to "## " so they nest under one "# Scoped".
    demoted = ["#" + section if section.startswith("# ") else section for section in sections]
    header = (
        f"# Scoped — {where}\n\n"
        "Accuracy and blame, recomputed over the scoped subset.\n\n"
    )
    return header + "\n".join(demoted)
