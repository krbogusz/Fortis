"""Load autosegmental tier declarations from ``tiers.toml``.

The file is optional: a project that declares no tiers runs the engine exactly as it
did before. Each top-level table is one tier — a suprasegmental feature that carries
itself — declaring that feature (kind/values/short), its anchor predicate, and its
association policy.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.loaders.features import load_feature
from src.fortis.models.features import FeatureInventory
from src.fortis.models.tier_declaration import TierDeclaration, TierInventory
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.result import Err, Ok, Result


def load_tier(
    name: str, tier_def: dict[str, Any], features: FeatureInventory
) -> Result[TierDeclaration, list[str]]:
    """Load one tier declaration from a raw TOML table.

    Args:
        name: The tier's name (the TOML table key).
        tier_def: Raw dictionary from the TOML file.
        features: Feature inventory — the tier registers itself on it, and parses ``anchor``.
    """
    error_list: list[str] = []

    # The tier IS a suprasegmental feature: build its definition (kind/values/short) and
    # register it on the inventory as a syllable-tier feature.
    match load_feature(name, {**tier_def, "tier": "syllable"}):
        case Err(err):
            error_list.extend(err)
        case Ok(feature):
            features[name] = feature

    anchor = None
    anchor_raw = tier_def.get("anchor")
    if not anchor_raw or not str(anchor_raw).strip():
        error_list.append(f"Tier '{name}' is missing the required 'anchor' field")
    else:
        match parse_pattern_bundle(str(anchor_raw).strip(), features):
            case Err(err):
                error_list.extend(f"Tier '{name}' anchor: {e}" for e in err)
            case Ok(result):
                anchor = result

    melody = tier_def.get("melody")
    if not isinstance(melody, bool):
        error_list.append(f"Tier '{name}' needs a boolean 'melody' field")
        melody = False

    ocp = tier_def.get("ocp", True)
    stray_erase = tier_def.get("stray_erase", True)
    for field_name, value in (("ocp", ocp), ("stray_erase", stray_erase)):
        if not isinstance(value, bool):
            error_list.append(f"Tier '{name}' field '{field_name}' must be a boolean")

    stability = tier_def.get("stability", "left")
    if stability not in ("left", "right"):
        error_list.append(f"Tier '{name}' field 'stability' must be 'left' or 'right'")

    if error_list:
        return Err(error_list)
    assert anchor is not None
    return Ok(
        TierDeclaration(
            name=name,
            carries=(name,),
            anchor=anchor,
            melody=melody,
            ocp=bool(ocp),
            stray_erase=bool(stray_erase),
            stability=str(stability),
        )
    )


def load_tier_inventory(path: Path, features: FeatureInventory) -> Result[TierInventory, list[str]]:
    """Load all tier declarations from a TOML file.

    Args:
        path: Path to ``tiers.toml``.
        features: Feature inventory for validation and anchor parsing.
    """
    match load_toml_file(path, allow_empty=True):  # an empty tiers.toml ⇒ no tiers, not an error
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    error_list: list[str] = []
    inventory = TierInventory()
    for name, tier_def in data.items():
        name = name.strip()
        if name in inventory:
            error_list.append(f"Tier '{name}' is already defined")
            continue
        match load_tier(name, tier_def, features):
            case Err(err):
                error_list.extend(err)
            case Ok(result):
                inventory[name] = result

    if error_list:
        return Err(error_list)

    match validate_tier_inventory(inventory):
        case Err(err):
            return Err(err)
        case Ok():
            return Ok(inventory)


def validate_tier_inventory(inventory: TierInventory) -> Result[None, list[str]]:
    """Cross-tier consistency: each feature is carried by at most one tier.

    Args:
        inventory: The loaded tier inventory.
    """
    error_list: list[str] = []
    owner: dict[str, str] = {}
    for name, tier in inventory.data.items():
        for feature in tier.carries:
            if feature in owner:
                error_list.append(
                    f"Feature '{feature}' is carried by both tier '{owner[feature]}' and '{name}'"
                )
            else:
                owner[feature] = name

    if error_list:
        return Err(error_list)
    return Ok(None)
