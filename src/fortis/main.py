"""Main entry point for the Fortis phonology engine.

Loads all inventories, processes every word through all phonological
rules, and prints a step-by-step derivation table showing which rules
applied and what changed at each stage.
"""

from src.fortis.application.parsing import split_rule_definition
from src.fortis.general.presentation import present_sequence
from src.fortis.imports.inventories import Inventories
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_value import FeatureValue
from src.fortis.transcription.parsing import string_to_sequence


def main() -> None:
    """Load inventories, run derivations for all words, and print results."""
    inventories = Inventories.load()
    print(f"Loaded {len(inventories.features)} features")
    print(f"Loaded {len(inventories.letters)} letters")
    print(f"Loaded {len(inventories.words)} words")
    print()

    value_1 = FeatureValue.from_str("nasal: none@all", "nasal", inventories.features).unwrap()
    print(value_1)
    spec_1 = FeatureSpec.from_str("nasal: none>1", inventories.features).unwrap()
    print("Spec 1: ", spec_1)
    spec_2 = FeatureSpec.from_str("nasal: none@any", inventories.features).unwrap()
    print("Spec 2: ", spec_2)
    print(f"'{spec_1}' matches '{spec_2}'?")
    print(spec_1.matches_pattern(spec_2))

    bundle_1 = FeatureBundle.from_string("!nasal", inventories.features).unwrap()
    bundle_2 = FeatureBundle.from_string("nasal: none>1", inventories.features).unwrap()
    print(f"'{bundle_1}' matches '{bundle_2}'?")
    print(bundle_1.matches_pattern(bundle_2))

    print(split_rule_definition("[+cons, +guttural, +coronal] → [cor: none]"))

    word_1 = "xenti"
    sequence_1 = string_to_sequence(word_1, inventories)
    print(present_sequence(sequence_1, inventories.features))


if __name__ == "__main__":
    main()
