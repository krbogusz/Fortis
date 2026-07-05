"""CLI for the grader: derive a project and score it against its target forms.

Loads a project (the same way the engine CLI does), derives every word, grades
the derived forms against the attested ``final`` and intermediate ``stages`` in
``words.toml``, and writes the analysis reports — ``distances.md`` (grading),
``diagnosis.md`` (confusions + autopsy), ``timeline.md`` (errors by rule-time +
per-stage), and ``blame.md`` (each wrong word attributed to a rule). With
``--try 'RULE'`` it also writes ``whatif.md`` previewing a candidate rule. Run::

    python -m src.fortis.analysis.main --project projects/latin_to_french

``--filter 'PATTERN'`` restricts every report to the words whose attested target
matches a sequence pattern (Fortis rule notation, e.g. ``k [aperture: high]``).

The engine CLI (``python -m src.fortis.main``) writes the same reports as part of
a full run; this standalone entry point is for grading on its own.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.fortis.analysis.blame import blame_all, blame_summary_line, render_blame
from src.fortis.analysis.diagnosis import (
    diagnose_stages,
    diagnosis_summary_line,
    errors_by_time,
    render_diagnosis,
    render_timeline,
    timeline_summary_line,
)
from src.fortis.analysis.filtering import filter_by_target, filter_note
from src.fortis.analysis.grading import grade_stages
from src.fortis.analysis.reporting import distance_summary_line, render_distance_summary
from src.fortis.analysis.whatif import render_whatif, try_rule, whatif_summary_line
from src.fortis.application.deriving import derive_all
from src.fortis.config import config
from src.fortis.loaders.project import load_project
from src.fortis.result import Err, Ok

# Sentinel: no ``--output`` given ⇒ write to ``<project>/distances.md``.
_AUTO_OUTPUT = object()


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="fortis-grade",
        description=(
            "Derive a project and grade the derived forms against the attested 'final' and "
            "'stages' in words.toml: exact-match accuracy and mean phone/feature edit distance."
        ),
    )
    parser.add_argument(
        "--project",
        type=Path,
        metavar="DIR",
        help="a project directory (default: the shipped projects/default/)",
    )
    parser.add_argument(
        "--words",
        type=Path,
        metavar="FILE",
        help="lexicon file to grade (default: the project's words.toml)",
    )
    parser.add_argument(
        "--rules",
        type=Path,
        metavar="FILE",
        help="sound-change file to apply (default: the project's rules.toml)",
    )
    parser.add_argument(
        "--output",
        nargs="?",
        const=_AUTO_OUTPUT,
        default=_AUTO_OUTPUT,
        type=Path,
        metavar="FILE",
        help="path for the Markdown report (default: <project>/distances.md)",
    )
    parser.add_argument(
        "--try",
        dest="candidate",
        metavar="RULE",
        help="preview a candidate rule (e.g. 'eː → ɛː / _ t') against the lexicon (writes whatif.md)",
    )
    parser.add_argument(
        "--at",
        dest="at",
        type=int,
        metavar="TIME",
        help="time to insert the --try rule at (default: untimed, after all timed rules)",
    )
    parser.add_argument(
        "--filter",
        dest="filter",
        metavar="PATTERN",
        help="restrict the reports to words whose attested target matches a sequence "
        "pattern (Fortis notation, e.g. 'k [aperture: high]')",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load a project, derive it, grade every stage and the final, and report."""
    args = _parse_args(argv)
    result = load_project(args.project, words_path=args.words, rules_path=args.rules)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()

    try:
        derivations = derive_all(project)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    # --filter restricts every report to the words whose target matches a pattern.
    if args.filter is not None:
        match filter_by_target(derivations, args.filter, project):
            case Err(errs):
                for error in errs:
                    print(f"error: --filter: {error}", file=sys.stderr)
                raise SystemExit(1)
            case Ok(selection):
                derivations = list(selection.matched)
                where += f" · {filter_note(selection)}"
                print(filter_note(selection), file=sys.stderr)  # announce, incl. a 0-match filter

    stages = grade_stages(derivations, project)

    output_dir = args.project or config.paths.default
    path = output_dir / "distances.md" if args.output is _AUTO_OUTPUT else args.output
    path.write_text(render_distance_summary(stages, where), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    print(distance_summary_line(stages))

    # Diagnose where the final derivation goes wrong (the snapshot), from the same graded forms.
    final = next(s for s in stages if s.time is None)
    grades = final.report.grades
    diagnosis_path = path.parent / "diagnosis.md"
    diagnosis_path.write_text(render_diagnosis(grades, project, where), encoding="utf-8")
    print(f"wrote {diagnosis_path}", file=sys.stderr)
    print(diagnosis_summary_line(grades))

    # Blame and the temporal views share the per-word blames — computed once here.
    blames = blame_all(derivations, project)
    buckets = errors_by_time(blames)
    stage_diag = diagnose_stages(derivations, project)
    timeline_path = path.parent / "timeline.md"
    timeline_path.write_text(render_timeline(buckets, stage_diag, project, where), encoding="utf-8")
    print(f"wrote {timeline_path}", file=sys.stderr)
    print(timeline_summary_line(buckets))

    # Attribute each wrong word to the rule that produced it.
    blame_path = path.parent / "blame.md"
    blame_path.write_text(render_blame(blames, where), encoding="utf-8")
    print(f"wrote {blame_path}", file=sys.stderr)
    print(blame_summary_line(blames))

    if args.candidate is not None:
        result = try_rule(project, args.candidate, args.at)
        if result.is_err():
            for error in result.unwrap_err():
                print(f"error: --try rule: {error}", file=sys.stderr)
            raise SystemExit(1)
        whatif = result.unwrap()
        whatif_path = path.parent / "whatif.md"
        whatif_path.write_text(render_whatif(whatif, where), encoding="utf-8")
        print(f"wrote {whatif_path}", file=sys.stderr)
        print(whatif_summary_line(whatif))


if __name__ == "__main__":
    main()
