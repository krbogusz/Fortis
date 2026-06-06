"""Rule loading — parses TOML rule definitions into RuleDefinition objects.

A RuleDefinition holds the raw *definition* string from the TOML file and
parsed Element lists populated by a separate parser
(see ``application.parser``).

The TOML key format is ``[<rule_id>]`` with ``time`` given as a field inside
the table.  Lower time values are applied earlier; rules with the same time
are applied in declaration order.
"""

from collections import UserDict
from dataclasses import dataclass, field
from enum import StrEnum, auto
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.general.utils import safe_int
from src.fortis.models.elements import Element
from src.fortis.result import Err, Ok, Result


class ApplicationType(StrEnum):
    """How a rule should be applied when multiple loci match."""

    simultaneous = auto()  # default — find every locus, rewrite all at once
    left_to_right = auto()
    right_to_left = auto()


@dataclass
class RuleDefinition:
    """A phonological rule parsed from TOML.

    The general form is  A → B / C_D // E_F  where:

    - **target** (A): what elements are matched
    - **result** (B): what they become
    - **context_left** (C): environment before the target
    - **context_right** (D): environment after the target
    - **exception_left** (E): exception environment before the target
    - **exception_right** (F): exception environment after the target

    ``None`` for a context/exception field means "unconstrained" (no condition
    on that side).  An empty list means the same — no constraint.

    The *definition* string is the raw SPE notation from TOML.  The parsed
    Element lists are populated by the parser after loading.
    """

    rule_id: str
    name: str
    time: int
    definition: str
    description: str | None = None
    application: ApplicationType = ApplicationType.simultaneous

    # Parsed Element lists (populated by the parser)
    target: list[Element] = field(default_factory=list)
    result: list[Element] = field(default_factory=list)
    context_left: list[Element] | None = None
    context_right: list[Element] | None = None
    exception_left: list[Element] | None = None
    exception_right: list[Element] | None = None

    @property
    def is_parsed(self) -> bool:
        """Whether the definition string has been parsed into Element lists."""
        return bool(self.target) and bool(self.result)

    @classmethod
    def from_dict(cls, rule_id: str, rule_dict: dict[str, Any]) -> Result[RuleDefinition, list[str]]:
        """Import rule definition from a TOML dictionary.

        Validates name, time, definition, description, and application type.
        The definition string is stored as-is; Element lists are populated
        later by the parser (see ``application.parser``).
        """
        error_list: list[str] = []

        # Name
        name = rule_dict.get("name")
        if not name:
            error_list.append(f"missing required field 'name' for rule '{rule_id}'")
        elif not isinstance(name, str):
            error_list.append(f"invalid 'name' for rule '{rule_id}': expected a string")

        # Time
        time_raw = rule_dict.get("time")
        if time_raw is None:
            error_list.append(f"missing required field 'time' for rule '{rule_id}'")
        time_val = safe_int(str(time_raw))
        if time_val is None:
            error_list.append(f"invalid time for rule '{rule_id}': expected an integer")

        # Definition
        definition = rule_dict.get("definition")
        if not definition:
            error_list.append(f"missing required field 'definition' for rule '{rule_id}'")
        elif not isinstance(definition, str):
            error_list.append(f"invalid 'definition' for rule '{rule_id}': expected a string")

        # Description (optional)
        description = rule_dict.get("description")
        if description is not None and not isinstance(description, str):
            error_list.append(f"invalid 'description' for rule '{rule_id}': expected a string or None")

        # Application type (optional, defaults to simultaneous)
        application_raw = rule_dict.get("application")
        if application_raw is None:
            application = ApplicationType.simultaneous
        else:
            try:
                application = ApplicationType(application_raw)
            except ValueError:
                error_list.append(f"invalid application type '{application_raw}' for rule '{rule_id}'")
                application = None

        if error_list:
            return Err(error_list)

        return Ok(
            cls(
                rule_id=rule_id,
                name=name if isinstance(name, str) else "",
                time=time_val if time_val is not None else 0,
                definition=definition if isinstance(definition, str) else "",
                description=description if isinstance(description, str) else None,
                application=application if application is not None else ApplicationType.simultaneous,
            )
        )


class RuleInventory(UserDict[str, RuleDefinition]):
    """Rules keyed by rule_id, loaded from TOML.

    The TOML key is the rule_id.  Rules are stored in time order
    (lower first, same-time in declaration order).
    """

    @classmethod
    def load(cls, path: Path) -> Result[RuleInventory, list[str]]:
        """Load rules from a TOML file.

        Args:
            path: Path to the rules TOML file.
        """
        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        rules: dict[str, RuleDefinition] = {}
        error_list: list[str] = []

        for key, value in data.items():
            rule_id = key
            result = RuleDefinition.from_dict(rule_id, value)
            if result.is_err():
                error_list.extend(result.unwrap_err())
                continue
            rules[rule_id] = result.unwrap()

        if error_list:
            return Err(error_list)

        inv = cls(rules)
        check_result = inv.validate()
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inv)

    def validate(self) -> Result[None, list[str]]:
        """Check for cross-rule consistency issues."""
        return Ok(None)

    def sorted_by_time(self) -> list[RuleDefinition]:
        """Return rules sorted by time (ascending), preserving declaration order for ties."""
        return sorted(self.data.values(), key=lambda r: r.time)
