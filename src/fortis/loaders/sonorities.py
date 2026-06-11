from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.general.utils import safe_int
from src.fortis.models.bundles import PatternBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import Sonority, SonorityInventory
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.result import Err, Ok, Result

# ---- Sonority ---------------------------------------------------------------------------------------------------------


def load_sonority(
    label: str, sonority_def: dict[str, Any], features: FeatureInventory
) -> Result[Sonority, list[str]]:
    """Load a Sonority from a raw TOML entry.

    Args:
        label: Sonority level label.
        sonority_def: Raw dictionary from the TOML file.
        features: Feature inventory for bundle parsing.
    """
    error_list: list[str] = []

    match load_level(label, sonority_def):
        case Err(err):
            error_list.append(err)
            level = 0  # Dummy value for the type checker
        case Ok(result):
            level = result

    match load_bundle(label, sonority_def, features):
        case Err(err):
            error_list.extend(err)
            bundle = None  # Dummy value for the type checker
        case Ok(result):
            bundle = result

    if error_list:
        return Err(error_list)
    return Ok(Sonority(label=label, level=level, bundle=bundle))


# ---- Per-field helpers ------------------------------------------------------------------------------------------------


def load_level(label: str, sonority_def: dict[str, Any]) -> Result[int, str]:
    """Parse and validate the 'level' field.

    Args:
        label: Sonority label (for error messages).
        sonority_def: Raw dictionary from the TOML file.
    """
    value = sonority_def.get("level")
    if value is None:
        return Err(f"Sonority '{label}' is missing the required 'level' field")
    level = safe_int(str(value).strip())
    if level is None or level <= 0:
        return Err(f"Sonority '{label}' has invalid level '{value}' (expected a positive integer)")
    return Ok(level)


def load_bundle(
    label: str, sonority_def: dict[str, Any], features: FeatureInventory
) -> Result[PatternBundle | None, list[str]]:
    """Parse the 'bundle' field; empty string yields None.

    Args:
        label: Sonority label (for error messages).
        sonority_def: Raw dictionary from the TOML file.
        features: Feature inventory for bundle parsing.
    """
    value = sonority_def.get("bundle")
    if value is None:
        return Err([f"Sonority '{label}' is missing the required 'bundle' field"])
    value = value.strip()
    if not value:
        return Ok(None)
    match parse_pattern_bundle(value, features):
        case Err(err):
            return Err(err)
        case Ok(result):
            return Ok(result)


# ---- Sonority Inventory -----------------------------------------------------------------------------------------------


def load_sonority_inventory(
    path: Path, features: FeatureInventory
) -> Result[SonorityInventory, list[str]]:
    """Load all sonority levels from a TOML file.

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

    inventory = SonorityInventory()
    for label, sonority_def in data.items():
        label = label.strip()
        if label in inventory:
            error_list.append(f"Sonority '{label}' is already defined")
            continue

        match load_sonority(label, sonority_def, features):
            case Err(err):
                error_list.extend(err)
                continue
            case Ok(result):
                sonority = result

        inventory[label] = sonority

    if error_list:
        return Err(error_list)

    match validate_sonority_inventory(inventory):
        case Err(err):
            return Err(err)
        case Ok():
            return Ok(inventory)


def validate_sonority_inventory(inventory: SonorityInventory) -> Result[None, list[str]]:
    """Check for cross-sonority consistency issues.

    Validates that sonority levels are unique.

    Args:
        inventory: The loaded sonority inventory.
    """
    error_list: list[str] = []

    seen_levels: dict[int, str] = {}
    for label, sonority in inventory.data.items():
        if sonority.level in seen_levels:
            error_list.append(
                f"Sonority '{label}' and '{seen_levels[sonority.level]}' share level {sonority.level}"
            )
        else:
            seen_levels[sonority.level] = label

    if error_list:
        return Err(error_list)
    return Ok(None)