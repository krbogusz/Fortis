"""Main entry point for the Fortis phonology engine.

Loads every inventory, then for each word: segments the IPA into feature
bundles, runs it through all rules in time order, and prints a step-by-step
derivation showing only the rules that changed the form, with syllable
structure (``.`` between syllables) on the surface.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.diagram import (
    render_autosegmental,
    render_change,
)
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project

# Sentinel: ``--output`` given with no path ⇒ write to ``<project>/output.md``.
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
            "fall back to them (default: the shipped inventories/)"
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
        default=None,
        type=Path,
        metavar="FILE",
        help=(
            "write the run to a Markdown file instead of printing it — the firing-rule "
            "trace plus an association-change diagram for each tier operation "
            "(default path: <project>/output.md)"
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load inventories, derive every word, and print the traces.

    With no arguments, runs every shipped rule over every shipped word. ``--words`` and
    ``--rules`` override just the lexicon and the sound-change file; the feature system,
    letters, sonority, tiers, etc. stay the shipped defaults unless ``--project`` points to
    a project directory (whose own files override the defaults, the rest falling back).
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

    if args.output is not None:
        path = (
            (args.project or Path(".")) / "output.md"
            if args.output is _AUTO_OUTPUT
            else args.output
        )
        path.write_text(_build_report(derivations, project, args.project), encoding="utf-8")
        print(f"wrote {path}", file=sys.stderr)
        return

    for derivation in derivations:
        _print_derivation(derivation, project)
        print()


_SUBRULE_SUFFIX = re.compile(r"#\d+$")


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

    previous_base: str | None = None
    for step in derivation.steps:
        before = render_syllabified(lower_tiers(step.before), step.before_boundaries, project)
        after = render_syllabified(lower_tiers(step.after), step.after_boundaries, project)
        change = describe_change(lower_tiers(step.before), lower_tiers(step.after), project)
        base = _SUBRULE_SUFFIX.sub("", step.rule.id)
        if base != previous_base:
            label = step.rule.name or base
            head = f"{step.rule.time}: {label}" if step.rule.time is not None else label
            print(f"    {head}")
            previous_base = base
        print(f"        {before} → {after}   ({change})")

    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    print(f"    Surface: {surface}")
    print("")


def _build_report(derivations: list[Derivation], project: Project, project_dir: Path | None) -> str:
    """The whole run as one Markdown document (the ``--output`` target)."""
    where = f"`{project_dir}`" if project_dir is not None else "the shipped inventories"
    lines = [
        f"# Output — {where}",
        "",
        "Engine-generated run output (`--output`). For each word: the firing-rule trace and,",
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

    trace: list[str] = []
    previous_base: str | None = None
    for step in derivation.steps:
        before = render_syllabified(lower_tiers(step.before), step.before_boundaries, project)
        after = render_syllabified(lower_tiers(step.after), step.after_boundaries, project)
        change = describe_change(lower_tiers(step.before), lower_tiers(step.after), project)
        base = _SUBRULE_SUFFIX.sub("", step.rule.id)
        if base != previous_base:
            label = step.rule.name or base
            head = f"{step.rule.time}: {label}" if step.rule.time is not None else label
            trace.append(head)
            previous_base = base
        trace.append(f"    {before} → {after}   ({change})")
    if trace:
        lines += ["```", *trace, "```", ""]

    for step in derivation.steps:
        for diagram in render_change(step.before, step.after, project):  # unified: tier + place
            label = step.rule.name or _SUBRULE_SUFFIX.sub("", step.rule.id)
            lines += [f"{label} — association change", "", "```", diagram, "```", ""]
    return lines


if __name__ == "__main__":
    main()
