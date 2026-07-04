"""CLI for the grader: derive a project and score it against its target forms.

Loads a project (the same way the engine CLI does), derives every word, grades
the derived forms against the attested ``final`` and intermediate ``stages`` in
``words.toml``, prints a summary, and writes a ``distances.md`` report. Run::

    python -m src.fortis.analysis.main --project projects/latin_to_french

The engine CLI (``python -m src.fortis.main``) writes the same report as part of
a full run; this standalone entry point is for grading on its own.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.fortis.analysis.grading import grade_stages
from src.fortis.analysis.reporting import distance_summary_line, render_distance_summary
from src.fortis.application.deriving import derive_all
from src.fortis.config import config
from src.fortis.loaders.project import load_project

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

    stages = grade_stages(derivations, project)
    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    output_dir = args.project or config.paths.default
    path = output_dir / "distances.md" if args.output is _AUTO_OUTPUT else args.output
    path.write_text(render_distance_summary(stages, where), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    print(distance_summary_line(stages))


if __name__ == "__main__":
    main()
