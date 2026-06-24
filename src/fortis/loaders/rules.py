from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.features import FeatureInventory
from src.fortis.models.rules import ApplicationMode, Rule, RuleInventory, StructuralDescription
from src.fortis.parsing.notation import parse_definition
from src.fortis.parsing.rule_validation import validate_structural_description
from src.fortis.result import Err, Ok, Result

# ---- Per-field helpers ----------------------------------------------------------------


def load_time(rule_id: str, rule_def: dict[str, Any]) -> Result[int, str]:
    """Parse and validate the required 'time' field.

    Args:
        rule_id: Rule slug (for error messages).
        rule_def: Raw dictionary from the TOML file.
    """
    value = rule_def.get("time")
    if value is None:
        return Err(f"Rule '{rule_id}' is missing the required 'time' field")
    if not isinstance(value, int):
        return Err(f"Rule '{rule_id}' has non-integer 'time' value: {value!r}")
    return Ok(value)


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

    match load_time(rule_id, rule_def):
        case Err(err):
            error_list.append(err)
            time = 0  # dummy
        case Ok(result):
            time = result

    definitions: list[str] = []
    match _read_definitions(rule_id, rule_def):
        case Err(err):
            error_list.append(err)
        case Ok(result):
            definitions = result

    match load_application(rule_id, rule_def):
        case Err(err):
            error_list.append(err)
            application = ApplicationMode.simultaneous
        case Ok(result):
            application = result

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
                match validate_structural_description(sd):
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
        )
        for index, (definition, sd) in enumerate(zip(definitions, sds, strict=True), start=1)
    ]
    return Ok(rules)


# ---- Inventory loader -----------------------------------------------------------------


def load_rule_inventory(path: Path, features: FeatureInventory) -> Result[RuleInventory, list[str]]:
    """Load all rules from a TOML file.

    Rules are grouped by their ``time`` field — multiple rules at the same
    time are stored as a tuple in file order.

    Args:
        path: Path to the TOML file.
        features: Feature inventory for bundle parsing inside definitions.
    """
    error_list: list[str] = []

    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    # Collect rules, preserving file order
    rules_by_time: dict[int, list[Rule]] = {}
    for rule_id, rule_def in data.items():
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

    match validate_rule_inventory(inventory):
        case Err(err):
            return Err(err)
        case Ok():
            return Ok(inventory)


# ---- Validation ------------------------------------------------------------------------


def validate_rule_inventory(inventory: RuleInventory) -> Result[None, list[str]]:
    """Check for cross-rule consistency issues.

    Args:
        inventory: The loaded rule inventory.
    """
    # No cross-rule validation needed yet — individual rules are already
    # validated during load. Kept as a stub for future checks.
    return Ok(None)
