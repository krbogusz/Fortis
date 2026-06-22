from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.general.utils import safe_int
from src.fortis.models.bundles import PatternBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import SyllablePart, SyllablePartsInventory
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.result import Err, Ok, Result

VALID_PART_TYPES = {"onset", "nucleus", "coda"}

# ---- SyllablePart -----------------------------------------------------------------------------------------------------


def load_syllable_part(
    part_type: str, time: int, part_dict: dict[str, Any], features: FeatureInventory
) -> Result[SyllablePart, list[str]]:
    """Load a SyllablePart from a raw TOML sub-table.

    Args:
        part_type: Syllable part type ("onset", "nucleus", or "coda").
        time: Application time for this constraint.
        part_dict: Raw dictionary from the TOML sub-table.
        features: Feature inventory for bundle parsing.
    """
    error_list: list[str] = []

    if part_type not in VALID_PART_TYPES:
        return Err([f"Invalid syllable part type '{part_type}' (expected {', '.join(sorted(VALID_PART_TYPES))})"])

    bundles: dict[str, PatternBundle | None] = {}
    for field in ("definition", "required", "forbidden"):
        match load_pattern_field(field, part_dict, features):
            case Err(err):
                error_list.extend(err)
            case Ok(result):
                bundles[field] = result

    if error_list:
        return Err(error_list)
    return Ok(
        SyllablePart(
            part_type=part_type,
            time=time,
            definition=bundles.get("definition"),
            required=bundles.get("required"),
            forbidden=bundles.get("forbidden"),
        )
    )


# ---- Per-field helpers ------------------------------------------------------------------------------------------------


def load_pattern_field(
    field: str, part_dict: dict[str, Any], features: FeatureInventory
) -> Result[PatternBundle | None, list[str]]:
    """Parse a pattern-bundle field by name; absent or empty yields None.

    Args:
        field: The TOML key to read ("definition", "required", or "forbidden").
        part_dict: Raw dictionary from the TOML sub-table.
        features: Feature inventory for bundle parsing.
    """
    value = part_dict.get(field)
    if value is None:
        return Ok(None)
    value = str(value).strip()
    if not value:
        return Ok(None)
    return parse_pattern_bundle(value, features)


# ---- SyllableParts Inventory ------------------------------------------------------------------------------------------


def load_syllable_parts_inventory(
    path: Path, features: FeatureInventory
) -> Result[SyllablePartsInventory, list[str]]:
    """Load syllable part constraints from a TOML file.

    The TOML file has top-level keys that are integer strings representing
    application times. Each time has sub-keys for part types
    (``onset``, ``nucleus``, ``coda``).

    Args:
        path: Path to the TOML file.
        features: Feature inventory for bundle parsing.
    """
    error_list: list[str] = []

    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    inventory = SyllablePartsInventory()
    for raw_time, time_dict in data.items():
        time = safe_int(raw_time.strip())
        if time is None:
            error_list.append(f"Syllable part time '{raw_time}' is not a valid integer")
            continue

        for part_type, part_dict in time_dict.items():
            part_type = part_type.strip()

            if time in inventory and part_type in inventory[time]:
                error_list.append(
                    f"Syllable part '{part_type}' at time {time} is already defined"
                )
                continue

            match load_syllable_part(part_type, time, part_dict, features):
                case Err(err):
                    error_list.extend(err)
                    continue
                case Ok(result):
                    syllable_part = result

            if time not in inventory:
                inventory[time] = {}
            inventory[time][part_type] = syllable_part

    if error_list:
        return Err(error_list)

    match validate_syllable_parts_inventory(inventory):
        case Err(err):
            return Err(err)
        case Ok():
            return Ok(inventory)


def validate_syllable_parts_inventory(inventory: SyllablePartsInventory) -> Result[None, list[str]]:
    """Check for cross-part consistency issues.

    Args:
        inventory: The loaded syllable parts inventory.
    """
    error_list: list[str] = []

    for time, parts in inventory.data.items():
        for part_type, part in parts.items():
            if part.part_type not in VALID_PART_TYPES:
                error_list.append(
                    f"Invalid syllable part type '{part.part_type}' at time {time}"
                )

    if error_list:
        return Err(error_list)
    return Ok(None)
