from __future__ import annotations

import csv
from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.result import Err, Ok, Result

_RESERVED_KEYS = ("gloss", "final", "frequency")


def load_word_inventory(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML or CSV lexicon file, dispatched by extension.

    Both formats carry the same schema — an IPA key with an optional ``gloss``, ``final``
    (attested surface), ``frequency`` (positive-integer token weight, default 1), and any
    number of integer-keyed *stage* forms (the attested form at that time). ``final`` and the
    stages are target annotations for accuracy; only the IPA key feeds derivation.

    A ``.csv`` path is read as a lexicon table (see :func:`load_word_inventory_csv`); any other
    path is read as TOML (:func:`load_word_inventory_toml`).

    Args:
        path: Path to the lexicon file (``.csv`` for CSV, else TOML).
    """
    if path.suffix.lower() == ".csv":
        return load_word_inventory_csv(path)
    return load_word_inventory_toml(path)


def load_word_inventory_toml(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML file.

    Keys are IPA transcription strings. A value is either:

    - a **string** — the gloss (the concise form): ``"ˌɑbˈɑnte" = "avant"``; or
    - a **table** with an optional ``gloss``, an optional ``final`` (the attested
      surface form), an optional ``frequency`` (a positive-integer token weight for
      frequency-weighted accuracy, default 1), and any number of integer-keyed
      *stage* forms (the attested form at that time), e.g.::

          "ˈɑmɑt̪" = {gloss = "aime – loves", final = "ɛm", frequency = 240,
                     100 = "ˈɑ.mɑt̪", 600 = "ˈãj̃.məθ", 1400 = "ˈɛ̃.mə"}

      ``final`` and the stage forms are target annotations for accuracy; only the
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


def load_word_inventory_csv(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a CSV file — the same schema as the TOML form, one word per row.

    A header row names the columns; the columns are read **by name**, so any order works.
    The **canonical order follows the derivation timeline** — the input, then the target
    annotations from earliest to latest::

        word, gloss, <intermediate stage times, ascending>, final

    e.g. ``word, gloss, -200, -100, 750, 1000, 1200, 1400, final``.

    Columns in detail:

    - ``word`` — the IPA transcription (the derivation input); required, the row's key.
    - ``gloss`` — an optional gloss/translation.
    - ``final`` — the optional attested final surface form (the last checkpoint).
    - an optional ``frequency`` — a positive-integer token weight (default 1).
    - every other column whose name is an **integer** is a *stage* time; its cell is the
      attested form at that stage.

    ``final`` and the stages are target annotations for accuracy; only ``word`` feeds
    derivation. An empty cell means "not present" (no gloss, no final, no form at that
    stage). Fields are read with the ``csv`` module, so a value containing a comma must be
    quoted (``"amère, bitter"``).

    Args:
        path: Path to the CSV file.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        return Err([f"could not read '{path}': {error}"])

    error_list: list[str] = []
    reader = csv.DictReader(text.splitlines())
    if reader.fieldnames is None:
        return Err([f"'{path}' is empty (no header row)"])
    if "word" not in reader.fieldnames:
        return Err([f"'{path}' must have a 'word' column (the IPA key)"])

    stage_columns: dict[str, int] = {}
    for column in reader.fieldnames:
        if column in _RESERVED_KEYS or column == "word":
            continue
        try:
            stage_columns[column] = int(column)
        except ValueError:
            error_list.append(
                f"column '{column}' is neither 'word'/'gloss'/'final'/'frequency' nor a stage time"
            )
    if error_list:
        return Err(error_list)

    inventory = WordInventory()
    for row in reader:
        ipa = (row.get("word") or "").strip()
        if not ipa:
            error_list.append("Word has an empty IPA key")
            continue
        if ipa in inventory:
            error_list.append(f"Word '{ipa}' is already defined")
            continue

        final = (row.get("final") or "").strip() or None
        raw_frequency = (row.get("frequency") or "").strip()
        frequency = 1
        if raw_frequency:
            try:
                frequency = int(raw_frequency)
            except ValueError:
                frequency = 0  # forces the positive-integer check below to fail
            if frequency <= 0:
                error_list.append(f"Word '{ipa}' has a 'frequency' that is not a positive integer")
                continue

        stages = {
            time: form.strip()
            for column, time in stage_columns.items()
            if (form := (row.get(column) or "").strip())
        }
        inventory[ipa] = Word(
            ipa=ipa, gloss=(row.get("gloss") or "").strip(),
            final=final, stages=stages, frequency=frequency,
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
