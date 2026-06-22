"""Main entry point for the Fortis phonology engine.

Loads all inventories, processes every word through all phonological
rules, and prints a step-by-step derivation table showing which rules
applied and what changed at each stage.
"""

from pprint import pprint

from src.fortis.loaders.project import load_project
from src.fortis.parsing.bundles import parse_pattern_spec
from src.fortis.parsing.notation import parse_definition


def main() -> None:
    """Load inventories, run derivations for all words, and print results."""
    project = load_project().unwrap()
    # pprint(project.rules)
    spec = "tone: 2>α"
    print(f"{spec} -> {parse_pattern_spec(spec, project.features)}")

    rule = "[+nasal] → [+voice, nasal: none] / [tone: 2>α] _ v // _ m"
    print(rule)
    pprint(parse_definition(rule, project.features))


if __name__ == "__main__":
    main()
