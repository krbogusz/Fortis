from __future__ import annotations

import csv
from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.inventories import Attestation, Word, WordInventory
from src.fortis.result import Err, Ok, Result

# The literal spelling of the untimed slot in both formats. It is not a year: an untimed rule
# runs after every timed one, so the form after it cannot be given a date. See
# :func:`~src.fortis.models.inventories.time_order`.
FINAL = "final"

_WORD_KEYS = ("id", "gloss", "frequency", "forms")
_CSV_COLUMNS = ("id", "time", "ipa", "category", "gloss", "frequency")


def load_word_inventory(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML or CSV lexicon file, dispatched by extension.

    Both formats carry the same model: a word is an ``id``, a ``gloss``, a ``frequency``, and a
    series of **attested forms through time**, each an IPA transcription with an optional
    grammatical ``category``. The EARLIEST form is the derivation seed (the input); every later
    one is a target the derived form is scored against at that time. The time ``"final"`` means
    "after every rule, including the untimed ones" — the surface.

    A ``.csv`` path is read as a lexicon table (:func:`load_word_inventory_csv`); any other path
    is read as TOML (:func:`load_word_inventory_toml`).

    Args:
        path: Path to the lexicon file (``.csv`` for CSV, else TOML).
    """
    if path.suffix.lower() == ".csv":
        return load_word_inventory_csv(path)
    return load_word_inventory_toml(path)


def load_word_inventory_toml(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a TOML file — an array of ``[[words]]`` tables.

    ::

        [[words]]
        id = "bear-v"
        gloss = "to bear"
        frequency = 1200
        forms = [
          { time = -2000,   ipa = "ˈbʱereti", category = "verb.pres.3sg" },
          { time = 200,     ipa = "ˈbirið̠i", category = "verb.pres.3sg.strong" },
          { time = "final", ipa = "beəz" },
        ]

    ``id`` is the key and must be unique — it is deliberately not the gloss, because identity and
    human label are different concerns (``lay`` is both a verb and a noun, and a word with no
    modern reflex has nothing to gloss it with). ``category`` is an opaque, project-defined
    string; the engine never parses it, and only compares it against a rule's ``categories``.

    Args:
        path: Path to the TOML file.
    """
    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    error_list: list[str] = []
    inventory = WordInventory()

    entries = data.get("words", [])
    if not isinstance(entries, list):
        return Err([f"'{path}': 'words' must be an array of [[words]] tables"])
    for index, table in enumerate(entries):
        if not isinstance(table, dict):
            error_list.append(f"words[{index}] is not a table")
            continue
        word = _parse_word_table(index, table, error_list)
        if word is None:
            continue
        if word.id in inventory:
            error_list.append(f"Word '{word.id}' is already defined")
            continue
        inventory[word.id] = word

    # The CONCISE form, for a word that is only a seed — no targets, no category::
    #
    #     "ata" = "intervocalic voicing"
    #
    # The key is both the id and the seed IPA (which is what they are for such a word), and the
    # value is the gloss. It exists because a lexicon used only to *watch* a rule fire — every
    # hand-written showcase project, and most of the test lexicons — has nothing else to say, and
    # spelling out a [[words]] table with a one-entry `forms` list for each would be noise.
    for key, value in data.items():
        if key == "words":
            continue
        if not isinstance(value, str):
            error_list.append(
                f"Word '{key}' must be a gloss string (the concise form); a word with targets "
                "goes in a [[words]] table"
            )
            continue
        if key.strip() in inventory:
            error_list.append(f"Word '{key.strip()}' is already defined")
            continue
        inventory[key.strip()] = Word(
            id=key.strip(), forms={0: Attestation(ipa=key.strip())}, gloss=value.strip()
        )

    if error_list:
        return Err(error_list)
    return validate_word_inventory(inventory).map(lambda _: inventory)


def load_word_inventory_csv(path: Path) -> Result[WordInventory, list[str]]:
    """Load words from a CSV file — **one row per attested form**, not per word.

    ::

        id,time,ipa,category,gloss,frequency
        bear-v,-2000,ˈbʱereti,verb.pres.3sg,to bear,1200
        bear-v,200,ˈbirið̠i,verb.pres.3sg.strong,,
        bear-v,final,beəz,,,

    Rows sharing an ``id`` are one word; they need not be adjacent, and their order does not
    matter (times are sorted). ``gloss`` and ``frequency`` belong to the word rather than to any
    one time, so they are taken from whichever of its rows supplies them — conventionally the
    first — and it is an error for two rows to disagree.

    This is the long ("tidy") shape rather than one-column-per-checkpoint, because a category
    varies with time and a wide table has nowhere to put it. It also means a lexicon of any depth
    has a fixed set of columns.

    ``time`` is an integer, or ``final`` for the surface after every rule.

    Args:
        path: Path to the CSV file.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        return Err([f"could not read '{path}': {error}"])

    reader = csv.DictReader(text.splitlines())
    if reader.fieldnames is None:
        return Err([f"'{path}' is empty (no header row)"])
    missing = [c for c in ("id", "time", "ipa") if c not in reader.fieldnames]
    if missing:
        return Err([f"'{path}' is missing required column(s): {', '.join(missing)}"])
    unknown = [c for c in reader.fieldnames if c not in _CSV_COLUMNS]
    if unknown:
        return Err([f"'{path}' has unknown column(s): {', '.join(unknown)}"])

    error_list: list[str] = []
    inventory = WordInventory()
    for line, row in enumerate(reader, start=2):
        word_id = (row.get("id") or "").strip()
        if not word_id:
            error_list.append(f"line {line}: row has an empty 'id'")
            continue

        time = _parse_time((row.get("time") or "").strip(), f"line {line}", error_list)
        if time is _INVALID:
            continue

        ipa = (row.get("ipa") or "").strip()
        if not ipa:
            error_list.append(f"line {line}: word '{word_id}' has an empty 'ipa'")
            continue

        word = inventory.get(word_id)
        if word is None:
            word = inventory[word_id] = Word(id=word_id)
        if time in word.forms:
            error_list.append(f"line {line}: word '{word_id}' already has a form at {time}")
            continue
        word.forms[time] = Attestation(ipa=ipa, category=(row.get("category") or "").strip())

        gloss = (row.get("gloss") or "").strip()
        if gloss:
            if word.gloss and word.gloss != gloss:
                error_list.append(f"line {line}: word '{word_id}' has two different glosses")
            word.gloss = gloss

        raw = (row.get("frequency") or "").strip()
        if raw:
            try:
                frequency = int(raw)
            except ValueError:
                frequency = 0  # forces the positive-integer check below to fail
            if frequency <= 0:
                error_list.append(
                    f"line {line}: word '{word_id}' has a 'frequency' that is not a "
                    "positive integer"
                )
                continue
            if word.frequency != 1 and word.frequency != frequency:
                error_list.append(f"line {line}: word '{word_id}' has two different frequencies")
            word.frequency = frequency

    if error_list:
        return Err(error_list)
    return validate_word_inventory(inventory).map(lambda _: inventory)


class _Invalid:
    """Sentinel: a time cell that failed to parse (distinct from the valid time ``None``)."""


_INVALID = _Invalid()


def _parse_time(raw: str, where: str, error_list: list[str]) -> int | None | _Invalid:
    """``"final"`` → ``None`` (the untimed slot); an integer string → that int."""
    if raw == FINAL:
        return None
    try:
        return int(raw)
    except ValueError:
        error_list.append(f"{where}: time {raw!r} is neither an integer nor '{FINAL}'")
        return _INVALID


def _parse_word_table(index: int, table: dict, error_list: list[str]) -> Word | None:
    """Parse one ``[[words]]`` table. Appends to *error_list* and returns None on any error."""
    word_id = table.get("id")
    if not isinstance(word_id, str) or not word_id.strip():
        error_list.append(f"words[{index}] has no 'id'")
        return None
    word_id = word_id.strip()
    where = f"Word '{word_id}'"

    unknown = [k for k in table if k not in _WORD_KEYS]
    if unknown:
        # Almost always a concise entry written BELOW a [[words]] table. TOML binds a bare
        # key/value to the table above it, so `"atta" = "eight"` after [[words]] silently becomes
        # a key OF that word rather than a word of its own. Say so — the bare "unknown key" that
        # this used to report sends you looking in the wrong place entirely.
        strings = [k for k in unknown if isinstance(table[k], str)]
        hint = (
            f" — a concise entry ({strings[0]!r}) must go ABOVE every [[words]] table, or TOML "
            "reads it as a key of the word above it"
            if strings else ""
        )
        error_list.append(f"{where} has unknown key(s): {', '.join(sorted(unknown))}{hint}")
        return None

    gloss = table.get("gloss", "")
    if not isinstance(gloss, str):
        error_list.append(f"{where} has a gloss that is not a string")
        return None

    # bool is an int subclass — reject it so `frequency = true` cannot become 1.
    frequency = table.get("frequency", 1)
    if type(frequency) is not int or frequency <= 0:
        error_list.append(f"{where} has a 'frequency' that is not a positive integer")
        return None

    raw_forms = table.get("forms")
    if not isinstance(raw_forms, list) or not raw_forms:
        error_list.append(f"{where} has no 'forms' (a word needs at least its seed)")
        return None

    forms: dict[int | None, Attestation] = {}
    for entry in raw_forms:
        if not isinstance(entry, dict):
            error_list.append(f"{where} has a form that is not a table")
            return None
        raw_time = entry.get("time")
        if isinstance(raw_time, str):
            time = _parse_time(raw_time, where, error_list)
            if time is _INVALID:
                return None
        elif type(raw_time) is int:
            time = raw_time
        else:
            error_list.append(f"{where} has a form with no integer (or '{FINAL}') 'time'")
            return None

        ipa = entry.get("ipa")
        if not isinstance(ipa, str) or not ipa.strip():
            error_list.append(f"{where} has a form at {raw_time} with no 'ipa'")
            return None
        category = entry.get("category", "")
        if not isinstance(category, str):
            error_list.append(f"{where} has a form at {raw_time} whose category is not a string")
            return None
        if time in forms:
            error_list.append(f"{where} has two forms at {raw_time}")
            return None
        forms[time] = Attestation(ipa=ipa.strip(), category=category.strip())

    return Word(id=word_id, forms=forms, gloss=gloss.strip(), frequency=frequency)


def validate_word_inventory(inventory: WordInventory) -> Result[None, list[str]]:
    """Check for cross-word consistency issues.

    Args:
        inventory: The loaded word inventory.
    """
    # Currently no cross-word validation needed
    return Ok(None)
