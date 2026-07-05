"""Load a project's tunable parameters from ``settings.toml``.

The file is optional and sparse: a project supplies only the knobs it wants to
change. **Omitted keys fall to the built-in defaults on the settings dataclasses —
not to the default *project's* settings.toml** (like every other inventory,
``pick`` in ``load_project`` replaces the file wholesale rather than merging against
the default project). A missing or empty file therefore yields all defaults.

Validation is strict, to catch typos the way the rest of the loaders do: an unknown
section or key, a non-integer value (``bool`` included — it is an ``int`` subclass in
Python and must be rejected explicitly), or an out-of-range value is an error, not a
silent fallback.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.settings import DiagnosisSettings, GradingSettings, Settings
from src.fortis.result import Err, Ok, Result

# section -> {key: minimum allowed value}. Doubles as the schema (known sections/keys)
# and the range check. Kept in step with the dataclass fields in models/settings.py.
_SCHEMA: dict[str, dict[str, int]] = {
    "grading": {"transposition_cost": 0},
    "diagnosis": {"min_support": 1, "min_errors": 1, "report_top": 0, "focus_count": 0},
}
_TYPES = {"grading": GradingSettings, "diagnosis": DiagnosisSettings}


def _validate_section(name: str, table: Any) -> tuple[dict[str, int], list[str]]:
    """Validate one settings section, returning its accepted values and any errors."""
    errors: list[str] = []
    if not isinstance(table, dict):
        return {}, [f"[{name}] must be a table"]
    values: dict[str, int] = {}
    for key, value in table.items():
        if key not in _SCHEMA[name]:
            errors.append(f"[{name}] has unknown key '{key}'")
            continue
        # bool is an int subclass — reject it so `true` cannot masquerade as 1.
        if type(value) is not int:
            errors.append(f"[{name}] '{key}' must be an integer (got {value!r})")
            continue
        minimum = _SCHEMA[name][key]
        if value < minimum:
            errors.append(f"[{name}] '{key}' must be ≥ {minimum} (got {value})")
            continue
        values[key] = value
    return values, errors


def load_settings(path: Path) -> Result[Settings, list[str]]:
    """Load ``settings.toml`` into a :class:`Settings`, filling omissions with defaults.

    A missing file yields all defaults. Present keys override; unknown sections/keys,
    non-integer values, and out-of-range values are collected as errors.
    """
    if not path.is_file():
        return Ok(Settings())

    match load_toml_file(path, allow_empty=True):
        case Err(err):
            return Err([err])
        case Ok(data):
            pass

    errors: list[str] = []
    sections: dict[str, dict[str, int]] = {}
    for name, table in data.items():
        if name not in _SCHEMA:
            errors.append(f"unknown section '[{name}]'")
            continue
        values, section_errors = _validate_section(name, table)
        errors.extend(section_errors)
        sections[name] = values

    if errors:
        return Err(errors)

    return Ok(
        Settings(
            grading=_TYPES["grading"](**sections.get("grading", {})),
            diagnosis=_TYPES["diagnosis"](**sections.get("diagnosis", {})),
        )
    )
