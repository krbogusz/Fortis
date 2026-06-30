from __future__ import annotations

from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.result import Err, Ok, Result


def load_word_inventory(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML file.

    Keys are IPA transcription strings; values are gloss strings.

    Args:
        path: Path to the TOML file.
    """
    error_list: list[str] = []

    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    inventory = WordInventory()
    for ipa, gloss in data.items():
        ipa = ipa.strip()
        if not ipa:
            error_list.append("Word has an empty IPA key")
            continue
        if ipa in inventory:
            error_list.append(f"Word '{ipa}' is already defined")
            continue
        if not isinstance(gloss, str):
            error_list.append(f"Word '{ipa}' has a gloss that is not a string")
            continue
        inventory[ipa] = Word(ipa=ipa, gloss=gloss.strip())

    if error_list:
        return Err(error_list)

    return validate_word_inventory(inventory).map(lambda _: inventory)


def validate_word_inventory(inventory: WordInventory) -> Result[None, list[str]]:
    """Check for cross-word consistency issues.

    Args:
        inventory: The loaded word inventory.
    """
    # Currently no cross-word validation needed
    return Ok(None)
