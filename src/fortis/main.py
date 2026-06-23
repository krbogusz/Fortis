"""Main entry point for the Fortis phonology engine.

Loads every inventory, then for each word: segments the IPA into feature
bundles, runs it through all rules in time order, and prints a step-by-step
derivation showing only the rules that changed the form, with syllable
structure (``.`` between syllables) on the surface.
"""

import sys

from src.fortis.application.deriving import derive
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project


def main() -> None:
    """Load inventories, derive every word, and print the traces."""
    result = load_project()
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()

    for ipa, word in project.words.items():
        segments = string_to_sequence(ipa, project)
        derivation = derive(
            word,
            segments,
            project.rules,
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
        )
        _print_derivation(derivation, project)
        print()


def _print_derivation(derivation: Derivation, project: Project) -> None:
    """Print one word's derivation: input, each firing rule, then the surface."""
    word = derivation.word
    gloss = f'  "{word.gloss}"' if word.gloss else ""
    print(f"{word.ipa}{gloss}")  # echo the input verbatim (no render round-trip)

    for step in derivation.steps:
        after = render_syllabified(step.after, step.after_boundaries, project)
        change = describe_change(step.before, step.after, project)
        print(f"  →  [{step.rule.id}]  {after}   ({change})")

    surface = render_syllabified(derivation.surface, derivation.surface_boundaries, project)
    print(f"Surface: {surface}")


if __name__ == "__main__":
    main()
