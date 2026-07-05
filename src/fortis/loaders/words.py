from __future__ import annotations

from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.result import Err, Ok, Result


_RESERVED_KEYS = ("gloss", "final", "frequency")


def load_word_inventory(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML file.

    Keys are IPA transcription strings. A value is either:

    - a **string** — the gloss (the concise form): ``"ˌɑbˈɑnte" = "avant"``; or
    - a **table** with an optional ``gloss``, an optional ``final`` (the attested
      surface form), an optional ``frequency`` (a positive-integer token weight for
      frequency-weighted grading, default 1), and any number of integer-keyed
      *stage* forms (the attested form at that time), e.g.::

          "ˈɑmɑt̪" = {gloss = "aime – loves", final = "ɛm", frequency = 240,
                     100 = "ˈɑ.mɑt̪", 600 = "ˈãj̃.məθ", 1400 = "ˈɛ̃.mə"}

      ``final`` and the stage forms are target annotations for grading; only the
      IPA key feeds derivation.

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
    for ipa, value in data.items():
        ipa = ipa.strip()
        if not ipa:
            error_list.append("Word has an empty IPA key")
            continue
        if ipa in inventory:
            error_list.append(f"Word '{ipa}' is already defined")
            continue
        if isinstance(value, str):
            inventory[ipa] = Word(ipa=ipa, gloss=value.strip())
        elif isinstance(value, dict):
            word = _parse_word_table(ipa, value, error_list)
            if word is not None:
                inventory[ipa] = word
        else:
            error_list.append(
                f"Word '{ipa}' must be a gloss string or a table, not {type(value).__name__}"
            )

    if error_list:
        return Err(error_list)

    return validate_word_inventory(inventory).map(lambda _: inventory)


def _parse_word_table(ipa: str, table: dict, error_list: list[str]) -> Word | None:
    """Parse the table form of a word: ``gloss``/``final`` + integer stage keys.

    Appends to ``error_list`` and returns ``None`` on any error.
    """
    gloss = table.get("gloss", "")
    if not isinstance(gloss, str):
        error_list.append(f"Word '{ipa}' has a gloss that is not a string")
        return None

    final = table.get("final")
    if final is not None and not isinstance(final, str):
        error_list.append(f"Word '{ipa}' has a 'final' that is not a string")
        return None

    # bool is an int subclass — reject it so `frequency = true` cannot become 1.
    frequency = table.get("frequency", 1)
    if type(frequency) is not int or frequency <= 0:
        error_list.append(f"Word '{ipa}' has a 'frequency' that is not a positive integer")
        return None

    stages: dict[int, str] = {}
    ok = True
    for key, form in table.items():
        if key in _RESERVED_KEYS:
            continue
        try:
            time = int(key)
        except ValueError:
            error_list.append(
                f"Word '{ipa}' has key '{key}' that is neither 'gloss'/'final' nor a stage time"
            )
            ok = False
            continue
        if not isinstance(form, str):
            error_list.append(f"Word '{ipa}' stage {key} has a form that is not a string")
            ok = False
            continue
        stages[time] = form.strip()

    if not ok:
        return None
    return Word(
        ipa=ipa,
        gloss=gloss.strip(),
        final=final.strip() if isinstance(final, str) else None,
        stages=stages,
        frequency=frequency,
    )


def validate_word_inventory(inventory: WordInventory) -> Result[None, list[str]]:
    """Check for cross-word consistency issues.

    Args:
        inventory: The loaded word inventory.
    """
    # Currently no cross-word validation needed
    return Ok(None)
