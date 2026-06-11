"""Main entry point for the Fortis phonology engine.

Loads all inventories, processes every word through all phonological
rules, and prints a step-by-step derivation table showing which rules
applied and what changed at each stage.
"""

from src.fortis.loaders.project import load_project
from src.fortis.parsing.bundles import parse_pattern_spec


def main() -> None:
    """Load inventories, run derivations for all words, and print results."""
    project = load_project().unwrap()
    print(f"nasal -> {parse_pattern_spec('nasal', project.features)}")


if __name__ == "__main__":
    main()
