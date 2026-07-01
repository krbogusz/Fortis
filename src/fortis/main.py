"""Main entry point for the Fortis phonology engine.

Loads every inventory, then for each word: segments the IPA into feature
bundles, runs it through all rules in time order, and prints a step-by-step
derivation showing only the rules that changed the form, with syllable
structure (``.`` between syllables) on the surface. Every run also writes a
Markdown report (``<project>/output.md`` by default; ``--output`` overrides
the path) and a CSV report alongside it (one row per word, one column per
rule, holding the word's resulting form wherever that rule fired).
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from collections.abc import Sequence
from pathlib import Path

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.diagram import (
    render_autosegmental,
    render_change,
)
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.config import config
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory

# Sentinel: no ``--output`` path given (the default) ⇒ write to ``<project>/output.md``.
_AUTO_OUTPUT = object()


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="fortis",
        description=(
            "Run a phonological derivation: segment each word, apply the rules in time order, "
            "and print a step-by-step trace. With no arguments, runs every shipped rule over "
            "every shipped word."
        ),
    )
    parser.add_argument(
        "--project",
        type=Path,
        metavar="DIR",
        help=(
            "a project directory; its files override the shipped defaults and any it omits "
            "fall back to them (default: the shipped projects/default/)"
        ),
    )
    parser.add_argument(
        "--words",
        type=Path,
        metavar="FILE",
        help="lexicon file to run (default: the project's words.toml)",
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
        help=(
            "path for the Markdown report — the firing-rule trace plus an "
            "association-change diagram for each tier operation. Always written, "
            "alongside the printed trace and a same-named .csv report (one row per "
            "word, one column per rule) (default path: <project>/output.md)"
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load inventories, derive every word, print the traces, and write the reports.

    With no arguments, runs every shipped rule over every shipped word. ``--words`` and
    ``--rules`` override just the lexicon and the sound-change file; the feature system,
    letters, sonority, tiers, etc. stay the shipped defaults unless ``--project`` points to
    a project directory (whose own files override the defaults, the rest falling back).
    Every run writes ``output.md`` (the trace, ``--output`` overrides the path) and
    ``output.csv`` (one row per word, one column per rule) into the same directory.
    """
    args = _parse_args(argv)
    result = load_project(args.project, words_path=args.words, rules_path=args.rules)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()
    # Resolve the letter+diacritic runs a rule writes (e.g. ʁʷ, au) into segments.
    try:
        rules = resolve_rule_letters(project.rules, project)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    derivations = [
        derive(
            word,
            string_to_sequence(ipa, project),
            rules,
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
            project.tiers,
        )
        for ipa, word in project.words.items()
    ]

    output_dir = args.project or config.paths.default
    path = output_dir / "output.md" if args.output is _AUTO_OUTPUT else args.output
    path.write_text(_build_report(derivations, project, args.project), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)

    csv_path = path.with_suffix(".csv")
    csv_path.write_text(_build_csv_report(derivations, rules, project), encoding="utf-8")
    print(f"wrote {csv_path}", file=sys.stderr)

    for derivation in derivations:
        _print_derivation(derivation, project)
        print()


_SUBRULE_SUFFIX = re.compile(r"#\d+$")


def _trace_lines(steps: Sequence[DerivationStep], project: Project) -> list[str]:
    """The firing-rule trace, shared by the CLI and Markdown renders.

    A ``<time>: <name>`` head per rule group — consecutive sub-rules of one list-``definition``
    rule (``name#1``/``#2``) share a head — then an indented ``<before> → <after>   (<change>)``
    line per step. The CLI render prefixes each line with four more spaces.
    """
    lines: list[str] = []
    previous_base: str | None = None
    for step in steps:
        before = render_syllabified(lower_tiers(step.before), step.before_boundaries, project)
        after = render_syllabified(lower_tiers(step.after), step.after_boundaries, project)
        change = describe_change(lower_tiers(step.before), lower_tiers(step.after), project)
        base = _SUBRULE_SUFFIX.sub("", step.rule.id)
        if base != previous_base:
            label = step.rule.name or base
            lines.append(f"{step.rule.time}: {label}" if step.rule.time is not None else label)
            previous_base = base
        lines.append(f"    {before} → {after}   ({change})")
    return lines


def _print_derivation(derivation: Derivation, project: Project) -> None:
    """Print one word's derivation: headword, each firing rule, then the surface.

    Each firing rule is shown as ``<time>: <rule name>``, with the before → after
    forms and a change summary on the indented line below. Consecutive steps from
    one list-``definition`` rule (sub-rules sharing a ``name#1``/``#2`` id) are
    grouped under a single heading, one change line per sub-step.
    """
    word = derivation.word
    gloss = f' – "{word.gloss}"' if word.gloss else ""
    print("")
    print(f"{word.ipa}{gloss}")  # echo the input verbatim (no render round-trip)

    for line in _trace_lines(derivation.steps, project):
        print(f"    {line}")

    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    print(f"    Surface: {surface}")
    print("")


def _build_report(derivations: list[Derivation], project: Project, project_dir: Path | None) -> str:
    """The whole run as one Markdown document (the ``output.md`` report)."""
    where = f"`{project_dir}`" if project_dir is not None else "the shipped `projects/default`"
    lines = [
        f"# Output — {where}",
        "",
        "Engine-generated run output. For each word: the firing-rule trace and,",
        "for tier operations, the association-change diagram — `│` kept · `╎` added ·",
        "`╪` delinked.",
        "",
    ]
    for derivation in derivations:
        lines += _render_derivation_md(derivation, project)
    return "\n".join(lines).rstrip() + "\n"


def _render_derivation_md(derivation: Derivation, project: Project) -> list[str]:
    """One word's derivation as Markdown: surface, firing-rule trace, and change diagrams."""
    word = derivation.word
    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    lines = [f"## {word.gloss or word.ipa}", "", f"`{word.ipa}` → `{surface}`", ""]
    if any(tier.autosegs for tier in derivation.input.tiers.values()):
        melody = render_autosegmental(derivation.input, project)
        lines += ["Input melody", "", "```", melody, "```", ""]

    trace = _trace_lines(derivation.steps, project)
    if trace:
        lines += ["```", *trace, "```", ""]

    for step in derivation.steps:
        base = step.rule.name or _SUBRULE_SUFFIX.sub("", step.rule.id)
        for sublabel, diagram in render_change(step.before, step.after, step.rule, project):
            label = f"{base} · {sublabel}" if sublabel else base
            lines += [f"{label} — association change", "", "```", diagram, "```", ""]
    return lines


def _rule_columns(rules: RuleInventory) -> list[tuple[str, str]]:
    """Ordered ``(base_id, label)`` pairs, one per rule, in firing order.

    A list-``definition`` rule's sub-rules (``name#1``, ``name#2``, ...) share one
    column, matching how the Markdown report groups them under one heading.
    """
    columns: dict[str, str] = {}
    for time in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[time]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in columns:
                columns[base] = rule.name or base
    return list(columns.items())


def _build_csv_report(derivations: list[Derivation], rules: RuleInventory, project: Project) -> str:
    """One row per word, one column per rule.

    A cell holds the word's resulting form right after that rule fired (its last
    step, if it fired more than once), or stays empty if the rule never fired on
    that word.
    """
    columns = _rule_columns(rules)
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["ipa", "gloss", *(label for _base, label in columns)])
    for derivation in derivations:
        word = derivation.word
        after_by_base: dict[str, str] = {}
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            after_by_base[base] = render_syllabified(
                lower_tiers(step.after), step.after_boundaries, project
            )
        writer.writerow(
            [word.ipa, word.gloss or "", *(after_by_base.get(base, "") for base, _label in columns)]
        )
    return buffer.getvalue()


if __name__ == "__main__":
    main()
