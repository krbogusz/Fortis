"""Main entry point for the Fortis phonology engine.

Loads all inventories, processes every word through all phonological
rules, and prints a step-by-step derivation table showing which rules
applied and what changed at each stage.
"""

from src.fortis.imports.inventories import Inventories
from src.fortis.operations.rule_parsing import split_rule_definition


def main() -> None:
    """Load inventories, run derivations for all words, and print results."""
    inventories = Inventories.load()
    print(f"Loaded {len(inventories.features)} features")
    print(f"Loaded {len(inventories.letters)} letters")
    print(f"Loaded {len(inventories.words)} words")
    print()
    print(split_rule_definition("[+cons, +guttural, +coronal] → [cor: none]"))


if __name__ == "__main__":
    main()
