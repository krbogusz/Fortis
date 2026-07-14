from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.features import FeatureInventory
from src.fortis.models.rules import ApplicationMode, Rule, RuleInventory, StructuralDescription
from src.fortis.parsing.notation import parse_definition
from src.fortis.parsing.rule_validation import validate_structural_description
from src.fortis.result import Err, Ok, Result, collect

# ---- Per-field helpers ----------------------------------------------------------------


def load_time(rule_id: str, rule_def: dict[str, Any]) -> Result[int | None, str]:
    """Parse the optional 'time' field.

    An untimed rule has time ``None`` and is applied *after* every timed rule (in file order),
    and is shown without a time prefix.

    Args:
        rule_id: Rule slug (for error messages).
        rule_def: Raw dictionary from the TOML file.
    """
    value = rule_def.get("time")
    if value is None:
        return Ok(None)  # untimed: applied after all timed rules
    if not isinstance(value, int):
        return Err(f"Rule '{rule_id}' has non-integer 'time' value: {value!r}")
    return Ok(value)


def _load_string_list(
    rule_id: str, rule_def: dict[str, Any], field: str
) -> Result[tuple[str, ...], str]:
    """Parse an optional scope field that is a string or a list of strings. Empty ⇒ unrestricted."""
    value = rule_def.get(field)
    if value is None:
        return Ok(())
    if isinstance(value, str):
        return Ok((value,))
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return Ok(tuple(value))
    return Err(f"Rule '{rule_id}' has a '{field}' that is not a string or list of strings")


def load_words(rule_id: str, rule_def: dict[str, Any]) -> Result[tuple[str, ...], str]:
    """Parse the optional 'words' field: which words the rule is restricted to.

    Accepts a single string or a list of strings, each matched against a word's id or
    gloss. Empty (the default) ⇒ the rule applies to every word.

    Args:
        rule_id: Rule slug (for error messages).
        rule_def: Raw dictionary from the TOML file.
    """
    return _load_string_list(rule_id, rule_def, "words")


def load_categories(rule_id: str, rule_def: dict[str, Any]) -> Result[tuple[str, ...], str]:
    """Parse the optional 'categories' field: which word CLASSES the rule is restricted to.

    The class-wide counterpart of ``words``. Each string is matched literally against the
    word's category in force at this rule's time; the engine has no vocabulary of categories
    and never parses one, so a project chooses its own scheme. Empty ⇒ every word.

    Args:
        rule_id: Rule slug (for error messages).
        rule_def: Raw dictionary from the TOML file.
    """
    return _load_string_list(rule_id, rule_def, "categories")


def load_application(rule_id: str, rule_def: dict[str, Any]) -> Result[ApplicationMode, str]:
    """Parse the optional 'application' field (defaults to simultaneous).

    Args:
        rule_id: Rule slug (for error messages).
        rule_def: Raw dictionary from the TOML file.
    """
    value = rule_def.get("application")
    if value is None:
        return Ok(ApplicationMode.simultaneous)
    if not isinstance(value, str):
        return Err(f"Rule '{rule_id}' has non-string 'application' value: {value!r}")
    try:
        return Ok(ApplicationMode(value.strip().lower()))
    except ValueError:
        return Err(
            f"Rule '{rule_id}' has invalid application '{value}' "
            f"(expected {', '.join(t.value for t in ApplicationMode)})"
        )


# ---- Per-rule loader ------------------------------------------------------------------


def _read_definitions(rule_id: str, rule_def: dict[str, Any]) -> Result[list[str], str]:
    """The rule's ``definition`` as a list of one or more definition strings.

    Accepts a single string (one structural description) or a non-empty list of
    strings (ordered sub-steps that share the table's time/name/description) — so a
    multi-part change like a loss plus its conditioned stress shift reads as one
    named rule.
    """
    raw = rule_def.get("definition")
    if raw is None:
        return Err(f"Rule '{rule_id}' is missing the required 'definition' field")
    if isinstance(raw, str):
        return Ok([raw])
    if isinstance(raw, list) and all(isinstance(item, str) for item in raw):
        if not raw:
            return Err(f"Rule '{rule_id}' has an empty 'definition' list")
        return Ok(raw)
    return Err(f"Rule '{rule_id}' has a 'definition' that is not a string or list of strings")


def load_rule(
    rule_id: str, rule_def: dict[str, Any], features: FeatureInventory
) -> Result[list[Rule], list[str]]:
    """Load the rule(s) from a raw TOML entry.

    Returns one ``Rule`` per definition: a string ``definition`` yields a single
    rule (id ``rule_id``); a list yields one sub-rule per entry, in order, sharing
    the table's time/name/description and id-suffixed ``rule_id#1``, ``#2``, ….

    Args:
        rule_id: Rule slug (the TOML table key).
        rule_def: Raw dictionary from the TOML file.
        features: Feature inventory for bundle parsing inside definitions.
    """
    error_list: list[str] = []

    time = collect(error_list, load_time(rule_id, rule_def), 0)
    definitions = collect(error_list, _read_definitions(rule_id, rule_def), [])
    application = collect(
        error_list, load_application(rule_id, rule_def), ApplicationMode.simultaneous
    )
    words = collect(error_list, load_words(rule_id, rule_def), ())
    categories = collect(error_list, load_categories(rule_id, rule_def), ())

    name = rule_def.get("name")
    if name is not None and not isinstance(name, str):
        error_list.append(f"Rule '{rule_id}' has non-string 'name' value")

    description = rule_def.get("description")
    if description is not None and not isinstance(description, str):
        error_list.append(f"Rule '{rule_id}' has non-string 'description' value")

    sds: list[StructuralDescription] = []
    for definition in definitions:
        match parse_definition(definition, features):
            case Ok(sd):
                match validate_structural_description(sd, features):
                    case Err(errs):
                        error_list.extend(errs)
                    case Ok():
                        pass
                sds.append(sd)
            case Err(errs):
                error_list.extend(errs)

    if error_list:
        return Err(error_list)

    multiple = len(definitions) > 1
    rules = [
        Rule(
            id=f"{rule_id}#{index}" if multiple else rule_id,
            time=time,
            raw_definition=definition,
            sd=sd,
            application=application,
            name=name,
            description=description,
            words=words,
            categories=categories,
        )
        for index, (definition, sd) in enumerate(zip(definitions, sds, strict=True), start=1)
    ]
    return Ok(rules)


# ---- Inventory loader -----------------------------------------------------------------


def load_rule_inventory(path: Path, features: FeatureInventory) -> Result[RuleInventory, list[str]]:
    """Load the rule inventory from a TOML or CSV file, dispatched by extension.

    Both formats carry the same schema (a rule's id, optional ``time``/``name``/
    ``description``/``application``/``words``, and a required ``definition``). A ``.csv``
    path is read as a rules table (:func:`load_rule_inventory_csv`); any other path is read
    as TOML (:func:`load_rule_inventory_toml`).

    Args:
        path: Path to the rules file (``.csv`` for CSV, else TOML).
        features: Feature inventory for bundle parsing inside definitions.
    """
    if path.suffix.lower() == ".csv":
        return load_rule_inventory_csv(path, features)
    return load_rule_inventory_toml(path, features)


def _assemble_inventory(
    ordered: list[tuple[str, dict[str, Any]]], features: FeatureInventory
) -> Result[RuleInventory, list[str]]:
    """Build a validated :class:`RuleInventory` from ``(rule_id, rule_def)`` pairs in file order.

    Shared by the TOML and CSV loaders: each pair goes through :func:`load_rule` (so both
    formats inherit identical per-rule validation), and the resulting rules are grouped by
    ``time`` preserving order.
    """
    error_list: list[str] = []
    rules_by_time: dict[int | None, list[Rule]] = {}
    for rule_id, rule_def in ordered:
        rule_id = rule_id.strip()
        match load_rule(rule_id, rule_def, features):
            case Err(errs):
                error_list.extend(f"rule '{rule_id}': {e}" for e in errs)
                continue
            case Ok(rules):
                for rule in rules:
                    rules_by_time.setdefault(rule.time, []).append(rule)

    if error_list:
        return Err(error_list)

    # Build inventory: each time key maps to a tuple of rules in file order
    inventory = RuleInventory()
    for time, rules in rules_by_time.items():
        inventory[time] = tuple(rules)

    return validate_rule_inventory(inventory).map(lambda _: inventory)


def load_rule_inventory_toml(
    path: Path, features: FeatureInventory
) -> Result[RuleInventory, list[str]]:
    """Load all rules from a TOML file.

    Rules are grouped by their ``time`` field — multiple rules at the same
    time are stored as a tuple in file order.

    Args:
        path: Path to the TOML file.
        features: Feature inventory for bundle parsing inside definitions.
    """
    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    return _assemble_inventory(list(data.items()), features)


# Columns the CSV loader understands; anything else is an error. ``definition`` is required,
# ``id`` names the rule; the rest are optional and mirror the TOML fields.
_RULE_COLUMNS = (
    "id", "time", "name", "description", "definition", "application", "words", "categories",
)
# List-valued cells (``definition`` sub-steps, ``words`` scope) are ';'-separated. '|' is
# reserved by alternation inside definitions (e.g. ``(j|w)``), so ';' is the safe delimiter.
_LIST_SEP = ";"


def load_rule_inventory_csv(
    path: Path, features: FeatureInventory
) -> Result[RuleInventory, list[str]]:
    """Load all rules from a CSV file — the same schema as the TOML form, one rule per row.

    A header row names the columns; they are read **by name**, so any order works. The
    canonical order mirrors a rule table top-to-bottom::

        id, time, name, description, definition, application, words, categories

    Columns in detail:

    - ``id`` — the rule slug (labels its derivation step); required and unique per row.
    - ``time`` — an optional integer stage time. Empty ⇒ untimed (applied after all timed
      rules, in file order), exactly as an omitted TOML ``time``.
    - ``name`` / ``description`` — optional prose; empty cells are treated as absent.
    - ``definition`` — required. A multi-part rule is written as ``;``-separated sub-steps in
      the one cell (they share the row's time/name/description and mint ``id#1``, ``id#2``, …),
      matching a TOML list ``definition``.
    - ``application`` — optional mode (``simultaneous`` default, ``iterative``, …).
    - ``words`` — optional ``;``-separated word-scope, each matched against a word's id or
      gloss. Empty ⇒ the rule applies to every word.
    - ``categories`` — optional ``;``-separated CLASS scope, each matched against the word's
      category in force at this rule's time. Empty ⇒ the rule applies to every word.

    Fields are read with the ``csv`` module, so a value containing a comma must be quoted.
    A gloss used as a word-scope cannot itself contain ``;`` (the list delimiter).

    Args:
        path: Path to the CSV file.
        features: Feature inventory for bundle parsing inside definitions.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        return Err([f"could not read '{path}': {error}"])

    reader = csv.DictReader(text.splitlines())
    if reader.fieldnames is None:
        return Err([f"'{path}' is empty (no header row)"])
    unknown = [name for name in reader.fieldnames if name not in _RULE_COLUMNS]
    if unknown:
        return Err([f"'{path}' has unknown column(s): {', '.join(unknown)}"])
    if "id" not in reader.fieldnames:
        return Err([f"'{path}' must have an 'id' column (the rule slug)"])
    if "definition" not in reader.fieldnames:
        return Err([f"'{path}' must have a 'definition' column"])

    error_list: list[str] = []
    ordered: list[tuple[str, dict[str, Any]]] = []
    for line, row in enumerate(reader, start=2):  # line 1 is the header
        rule_id = (row.get("id") or "").strip()
        if not rule_id:
            error_list.append(f"line {line}: empty rule id")
            continue

        rule_def: dict[str, Any] = {}

        time_cell = (row.get("time") or "").strip()
        if time_cell:
            try:
                rule_def["time"] = int(time_cell)
            except ValueError:
                rule_def["time"] = time_cell  # non-integer → load_time reports it uniformly

        # Omit an empty definition entirely so load_rule reports "missing" (not "empty list").
        definition_cell = (row.get("definition") or "").strip()
        if definition_cell:
            rule_def["definition"] = [
                part.strip() for part in definition_cell.split(_LIST_SEP) if part.strip()
            ]

        for field in ("name", "description", "application"):
            value = (row.get(field) or "").strip()
            if value:
                rule_def[field] = value

        for scope in ("words", "categories"):
            cell = (row.get(scope) or "").strip()
            if cell:
                rule_def[scope] = [s.strip() for s in cell.split(_LIST_SEP) if s.strip()]

        ordered.append((rule_id, rule_def))

    if error_list:
        return Err(error_list)

    return _assemble_inventory(ordered, features)


# ---- Validation ------------------------------------------------------------------------


def validate_rule_inventory(inventory: RuleInventory) -> Result[None, list[str]]:
    """Check cross-rule consistency: rule ids must be unique.

    Ids label derivation steps and are otherwise the rule's handle, so two rules
    sharing one is ambiguous. This is reachable now that a list ``definition``
    mints ``id#1``, ``id#2`` — which can collide with an explicit table of that
    name. (Per-rule structure is already validated during load.)

    Args:
        inventory: The loaded rule inventory.
    """
    seen: set[str] = set()
    duplicates: set[str] = set()
    for rules in inventory.values():
        for rule in rules:
            if rule.id in seen:
                duplicates.add(rule.id)
            seen.add(rule.id)
    if duplicates:
        return Err([f"duplicate rule id '{rule_id}'" for rule_id in sorted(duplicates)])
    return Ok(None)
