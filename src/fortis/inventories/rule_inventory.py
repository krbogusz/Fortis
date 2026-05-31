"""RuleInventory — load phonological rules from TOML.

Each TOML entry has the key format ``[<time>.<id>]`` where *time* is
an integer (lower = applied earlier) and *id* is a unique identifier.
The value is a table with ``name``, ``description`` (optional), and
``definition`` (the SPE notation string).

Because TOML treats ``[1200.final_devoicing]`` as a nested table
(``{1200: {final_devoicing: {...}}}``), the loader flattens nested dicts
to collect all leaf rule entries.

Example::

    [1200.final_devoicing]
    name = "Final devoicing"
    description = "Devoices the final consonant in a sequence"
    definition = "[+cons, -syll] → [-vc] / _#"
"""

from __future__ import annotations

from collections import UserDict
from pathlib import Path

from src.fortis.general.file_handling import load_toml_file
from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.result import Err, Ok, Result
from src.fortis.rules.elements import Application
from src.fortis.rules.parsing import parse_rule_definition
from src.fortis.rules.rule import Rule


class RuleInventory(UserDict[str, Rule]):
    """Phonological rules keyed by ID, loaded from TOML and sorted by time.

    The ``sorted_rules`` property returns rules in ascending time order
    (lower time = applied earlier).
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the rule inventory and cache for sorted rules."""
        super().__init__(*args, **kwargs)
        self._sorted: list[Rule] | None = None

    @property
    def sorted_rules(self) -> list[Rule]:
        """Rules sorted by ascending time (lower number = applied earlier).

        The list is cached; invalidate by setting ``_sorted = None`` after
        mutating the dict.
        """
        if self._sorted is None:
            self._sorted = sorted(self.data.values(), key=lambda r: r.time)
        return self._sorted

    @classmethod
    def load(cls, path: Path, inventory: FeatureInventory) -> Result[RuleInventory, list[str]]:
        """Load all rules from a TOML file.

        Args:
            path: Path to the TOML file.
            inventory: Feature inventory for bundle parsing.
        """
        error_list: list[str] = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        # Flatten nested TOML tables.  [1200.final_devoicing] in TOML
        # becomes {"1200": {"final_devoicing": {...}}} — we need to walk
        # through and collect all leaf rule entries.
        entries = _flatten_toml(dict(data))

        rules: dict[str, Rule] = {}
        seen_times: set[int] = set()

        for full_key, rule_value in entries:
            # Parse the flattened key: "<time>.<id>.<...>"
            time, rule_id = _parse_key(full_key)
            if time is None:
                error_list.append(f"Rule key '{full_key}' must be in the format '<time>.<id>' with an integer time")
                continue

            if rule_id in rules:
                error_list.append(f"Rule ID '{rule_id}' is already defined")
                continue

            if time in seen_times:
                error_list.append(f"Rule '{rule_id}' has the same time ({time}) as another rule")

            # Parse the rule entry
            if not isinstance(rule_value, dict):
                error_list.append(f"Rule '{full_key}' must be a table, got {type(rule_value).__name__}")
                continue

            rule_dict: dict[str, object] = rule_value
            name_raw = rule_dict.get("name", "")
            name: str = str(name_raw) if name_raw else ""
            if not name:
                error_list.append(f"Rule '{full_key}' is missing required field 'name'")
                name = full_key

            description_raw = rule_dict.get("description", "")
            description: str = str(description_raw) if description_raw else ""

            definition_raw = rule_dict.get("definition", "")
            definition: str = str(definition_raw) if definition_raw else ""
            if not definition:
                error_list.append(f"Rule '{full_key}' is missing required field 'definition'")
                continue

            # Parse optional application mode (default: simultaneous)
            application_raw = rule_dict.get("application", "simultaneous")
            application: Application = Application(str(application_raw).strip().lower())

            rule_result = parse_rule_definition(
                definition=definition,
                inventory=inventory,
                rule_id=rule_id,
                name=name,
                description=description,
                time=time,
                application=application,
            )
            if rule_result.is_err():
                error_list.extend(rule_result.unwrap_err())
                continue

            rule = rule_result.unwrap()
            rules[rule_id] = rule
            seen_times.add(time)

        if error_list:
            return Err(error_list)

        return Ok(cls(rules))

    def validate(self) -> Result[None, list[str]]:
        """Check for cross-rule consistency issues.

        Currently a no-op; reserved for future checks.
        """
        return Ok(None)


def _flatten_toml(data: dict[str, object], prefix: str = "") -> list[tuple[str, object]]:
    """Flatten nested TOML tables into (full_key, leaf_value) pairs.

    TOML parses ``[1200.final_devoicing]`` as
    ``{"1200": {"final_devoicing": {...}}}``.  This function walks through
    the nested structure and collects all leaf values with their full
    dotted key path.

    Returns a list of (full_dotted_key, value) pairs.  Values are either
    dicts (rule entries with a "definition" key) or non-dict values (which
    will cause an error later).
    """
    entries: list[tuple[str, object]] = []
    for key, value in data.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            # Check if this is a leaf rule dict (has "definition" key)
            # or a nested table that needs further flattening
            if "definition" in value:
                entries.append((full_key, value))
            else:
                entries.extend(_flatten_toml(value, full_key))
        else:
            # Non-dict value at this level — not a rule entry, will cause error later
            entries.append((full_key, value))
    return entries


def _parse_key(key: str) -> tuple[int | None, str]:
    """Parse a flattened TOML key in the format '<time>.<id>'.

    Returns (time, id).  If time is not a valid integer,
    returns (None, key) so the caller can report an error.
    """
    dot_pos = key.find(".")
    if dot_pos == -1:
        return None, key

    time_str = key[:dot_pos]
    rule_id = key[dot_pos + 1 :]

    try:
        time_val = int(time_str)
    except ValueError:
        return None, key

    return time_val, rule_id
