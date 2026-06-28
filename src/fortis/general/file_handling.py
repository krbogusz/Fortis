from __future__ import annotations

import csv
import tomllib
from pathlib import Path
from typing import Any

from src.fortis.result import Err, Ok, Result


def load_toml_file(path: Path, *, allow_empty: bool = False) -> Result[dict[str, Any], str]:
    """Load a TOML file into a dict. Return an Ok with the dict or Err with description.

    With ``allow_empty`` a file that parses to no tables is accepted as an empty dict —
    used for an optional file (e.g. ``tiers.toml``) where "no tables" means "nothing
    declared" rather than an error.
    """
    # Path checks
    if not path.is_file():
        return Err(f"There is no file at '{path}'")
    if not path.suffix.lower() == ".toml":
        return Err(f"File at '{path}' is not a TOML file")

    # File check
    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
    except Exception as e:
        return Err(f"Could not open '{path}': {e}")

    # Content check
    if not data:
        if allow_empty:
            return Ok({})
        return Err(f"File '{path}' is empty")
    if not isinstance(data, dict):
        return Err(f"File '{path}' is not a dict")

    return Ok(data)


def load_csv_file(path: Path) -> Result[list[dict[str, Any]], str]:
    """Load a CSV file into a list of dicts. Return an Ok with the rows or Err with description."""
    if not path.is_file():
        return Err(f"There is no file at '{path}'")
    if not path.suffix.lower() == ".csv":
        return Err(f"File at '{path}' is not a CSV file")

    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                return Err(f"File '{path}' has no header row")
            rows = [dict(row) for row in reader]
    except Exception as e:
        return Err(f"Could not read '{path}': {e}")

    if not rows:
        return Err(f"File '{path}' has no data rows")

    return Ok(rows)
