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
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project


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
        "--inventories",
        type=Path,
        metavar="DIR",
        help="directory of inventory files (default: the shipped inventories/)",
    )
    parser.add_argument(
        "--words",
        type=Path,
        metavar="FILE",
        help="lexicon file to run (default: <inventories>/words.toml)",
    )
    parser.add_argument(
        "--rules",
        type=Path,
        metavar="FILE",
        help="sound-change file to apply (default: <inventories>/rules.toml)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load inventories, derive every word, and print the traces.

    With no arguments, runs every shipped rule over every shipped word. ``--words`` and
    ``--rules`` override just the lexicon and the sound-change file; the feature system,
    letters, sonority, tiers, etc. stay the shipped defaults unless ``--inventories`` points
    the whole set elsewhere.
    """
    args = _parse_args(argv)
    result = load_project(args.inventories, words_path=args.words, rules_path=args.rules)
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

    for ipa, word in project.words.items():
        segments = string_to_sequence(ipa, project)
        derivation = derive(
            word,
            segments,
            rules,
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
            project.tiers,
        )
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
            print(f"    {step.rule.time}: {step.rule.name or base}")
            previous_base = base
        print(f"        {before} → {after}   ({change})")

    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    print(f"    Surface: {surface}")
    print("")


if __name__ == "__main__":
    main()
