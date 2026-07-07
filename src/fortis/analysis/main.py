"""CLI for the accuracy analysis: derive a project and score it against its target forms.

Loads a project (the same way the engine CLI does), derives every word, measures the
derived forms' distance to target against the attested ``final`` and intermediate
``stages`` in ``words.toml``, and writes the analysis reports into a ``reports/``
subfolder of the project — ``accuracy.csv`` (per-stage accuracy summary) and
``distance_to_target.csv`` (per-word), then ``diagnosis.md`` (confusions + autopsy),
``timeline.md`` (errors by rule-time + per-stage), and ``blame.md`` (each wrong
word attributed to a rule). With
``--try 'RULE'`` it also writes ``whatif.md`` previewing a candidate rule. Run::

    python -m src.fortis.analysis.main --project projects/latin_to_french

``--scope 'PATTERN'`` writes ``scoped_output.md`` — the four analyses recomputed over
the words whose attested target, or any attested stage, matches a sequence pattern
(Fortis notation, e.g. ``k [aperture: high]``) — for debugging accuracy on a
sub-population, leaving the whole-lexicon reports intact.

The engine CLI (``python -m src.fortis.main``) writes the same reports as part of
a full run — and, with ``--filter``, an all-forms filtered synthesis; this standalone
entry point is for the accuracy analysis on its own.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from src.fortis.analysis.accuracy import accuracy_by_stage, ingest_targets
from src.fortis.analysis.blame import blame_all, blame_summary_line, render_blame
from src.fortis.analysis.diagnosis import (
    diagnose_stages,
    errors_summary_line,
    render_error_context_csv,
    render_errors_csv,
)
from src.fortis.analysis.filtering import filter_attested, scope_summary_line
from src.fortis.analysis.reporting import (
    accuracy_summary_line,
    render_accuracy_csv,
    render_distance_to_target_csv,
)
from src.fortis.analysis.synthesis import render_scoped
from src.fortis.analysis.whatif import render_whatif, try_rule, whatif_summary_line
from src.fortis.application.deriving import derive_all, derive_all_parallel
from src.fortis.config import config
from src.fortis.loaders.project import load_project
from src.fortis.result import Err, Ok

# Sentinel: no ``--output`` given ⇒ write to ``<project>/reports/accuracy.csv``.
_AUTO_OUTPUT = object()


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="fortis-accuracy",
        description=(
            "Derive a project and measure the derived forms' distance to target against the "
            "attested 'final' and 'stages' in words.toml: exact-match accuracy and mean "
            "phone/feature edit distance."
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
        help="lexicon file to measure (default: the project's words.toml)",
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
        help="path for the main report (default: <project>/reports/accuracy.csv); "
        "the other reports are written alongside it",
    )
    parser.add_argument(
        "--try",
        dest="candidate",
        metavar="RULE",
        help="preview a candidate rule (e.g. 'eː → ɛː / _ t') against the lexicon "
        "(writes whatif.md)",
    )
    parser.add_argument(
        "--at",
        dest="at",
        type=int,
        metavar="TIME",
        help="time to insert the --try rule at (default: untimed, after all timed rules)",
    )
    parser.add_argument(
        "--scope",
        dest="scope",
        metavar="PATTERN",
        help="write scoped_output.md — the analyses recomputed over words whose attested "
        "target or ANY attested stage matches a sequence pattern (e.g. 'k [aperture: high]')",
    )
    parser.add_argument(
        "--serial",
        dest="serial",
        action="store_true",
        help="derive in a single process, disabling the automatic multiprocessing "
        "(which otherwise fans a big lexicon across worker processes).",
    )
    parser.add_argument(
        "--workers",
        dest="workers",
        type=int,
        default=None,
        metavar="N",
        help="pin the worker-process count for the parallel derivation "
        "(default: auto, ~CPU count − 2). Ignored with --serial.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load a project, derive it, measure every stage and the final, and report."""
    args = _parse_args(argv)
    result = load_project(args.project, words_path=args.words, rules_path=args.rules)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()

    start = time.perf_counter()
    try:
        if args.serial:
            derivations = derive_all(project)
        else:
            derivations = derive_all_parallel(project, workers=args.workers)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    derive_done = time.perf_counter()

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    ingest_targets(derivations, project)  # segment attested forms once, in the main process
    stages = accuracy_by_stage(derivations, project)

    output_dir = args.project or config.paths.default
    # The main output is the per-stage accuracy summary; the per-word distance-to-target
    # table (and the other analyses) are written alongside it.
    path = output_dir / "reports" / "accuracy.csv" if args.output is _AUTO_OUTPUT else args.output
    path.parent.mkdir(parents=True, exist_ok=True)  # the reports/ subfolder (or --output's dir)
    path.write_text(render_accuracy_csv(stages), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    dtt_path = path.parent / "distance_to_target.csv"
    dtt_path.write_text(render_distance_to_target_csv(stages), encoding="utf-8")
    print(f"wrote {dtt_path}", file=sys.stderr)
    print(accuracy_summary_line(stages))
    accuracy_done = time.perf_counter()

    # Errors + Error context, per attested stage and the final: which segments came out
    # wrong, and the environments most associated with each.
    stage_diag = diagnose_stages(derivations, project)
    for name, render in (
        ("errors.csv", render_errors_csv),
        ("error_context.csv", render_error_context_csv),
    ):
        report_path = path.parent / name
        report_path.write_text(render(stage_diag), encoding="utf-8")
        print(f"wrote {report_path}", file=sys.stderr)
    print(errors_summary_line(stage_diag))

    # Attribute each wrong word to the rule that produced it.
    blames = blame_all(derivations, project)
    blame_path = path.parent / "blame.md"
    blame_path.write_text(render_blame(blames, where), encoding="utf-8")
    print(f"wrote {blame_path}", file=sys.stderr)
    print(blame_summary_line(blames))
    analysis_done = time.perf_counter()

    print(
        f"{len(derivations)} words · derive {derive_done - start:.2f}s, "
        f"accuracy {accuracy_done - derive_done:.2f}s, "
        f"analysis {analysis_done - accuracy_done:.2f}s",
        file=sys.stderr,
    )

    # --scope: a post-run pass. The standard reports above stay whole-lexicon; this bundles
    # the four analyses, recomputed over the words whose attested forms match, into one file.
    if args.scope is not None:
        match filter_attested(derivations, args.scope, project):
            case Err(errs):
                for error in errs:
                    print(f"error: --scope: {error}", file=sys.stderr)
                raise SystemExit(1)
            case Ok(scoped):
                scoped_where = (
                    f"{where} · scope `{args.scope}`: "
                    f"{len(scoped.matched)}/{scoped.considered} words"
                )
                scoped_path = path.parent / "scoped_output.md"
                scoped_path.write_text(
                    render_scoped(list(scoped.matched), project, scoped_where), encoding="utf-8"
                )
                print(f"wrote {scoped_path}", file=sys.stderr)
                print(scope_summary_line(scoped))

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
