from src.fortis.general.presentation import present_sequence
from src.fortis.inventories.inventories import Inventories
from src.fortis.transcription.parsing import string_to_sequence
from src.fortis.transcription.rendering import sequence_to_string


def main():
    """Main entry point for the project."""
    inventories = Inventories.load()
    print(f"Loaded {len(inventories.features)} features")
    print(f"Loaded {len(inventories.letters)} letters")

    print("ɣet͡sro")
    sequence = string_to_sequence("ɣet͡sro", inventories)
    print(present_sequence(sequence, inventories.features))
    print(sequence_to_string(sequence, inventories))


if __name__ == "__main__":
    main()
