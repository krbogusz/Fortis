"""Shared fixtures for Fortis tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from src.fortis.imports.features import FeatureDefinition, FeatureInventory, FeatureKind
from src.fortis.imports.inventories import Inventories
from src.fortis.models.tier import Tier

ROOT = Path(__file__).parent.parent
INVENTORIES_DIR = ROOT / "inventories"


# ---------------------------------------------------------------------------
# Synthetic (in-memory) inventory builders
# ---------------------------------------------------------------------------


def make_feature_inventory(
    feature_defs: dict[str, FeatureDefinition] | None = None,
) -> FeatureInventory:
    """Build a FeatureInventory from a dict of FeatureDefinitions.

    If None, builds a small default inventory with consonantal, syllabic,
    nasal, height (scalar), and tone (syllable-scalar).
    """
    if feature_defs is not None:
        return FeatureInventory(feature_defs)

    # Default synthetic inventory
    defs: dict[str, FeatureDefinition] = {}

    defs["consonantal"] = FeatureDefinition(
        name="consonantal",
        tier=Tier.segment,
        kind=FeatureKind.binary,
        short="cons",
        values={0: "absent", 1: "present"},
        children=None,
    )
    defs["syllabic"] = FeatureDefinition(
        name="syllabic",
        tier=Tier.segment,
        kind=FeatureKind.binary,
        short="syll",
        values={0: "absent", 1: "present"},
        children=None,
    )
    defs["nasal"] = FeatureDefinition(
        name="nasal",
        tier=Tier.segment,
        kind=FeatureKind.unary,
        short="nas",
        values={1: "present"},
        children=None,
    )
    defs["height"] = FeatureDefinition(
        name="height",
        tier=Tier.segment,
        kind=FeatureKind.scalar,
        short="hgt",
        values={1: "low", 2: "mid", 3: "high"},
        children=None,
    )
    defs["tone"] = FeatureDefinition(
        name="tone",
        tier=Tier.syllable,
        kind=FeatureKind.scalar,
        short="tn",
        values={1: "low", 2: "mid", 3: "high"},
        children=None,
    )
    return FeatureInventory(defs)


def load_feature_inventory_from_dict(raw: dict[str, Any]) -> FeatureInventory:
    """Build a FeatureInventory from a raw dict (mimics FeatureInventory.load without file I/O).

    Applies parent assignment and validation. Raises ValueError on errors.
    """
    error_list: list[str] = []
    feature_inventory: dict[str, FeatureDefinition] = {}

    for feature_name, feature_def_dict in raw.items():
        feature_name = feature_name.strip()
        if feature_name in feature_inventory:
            error_list.append(f"Feature name '{feature_name}' is already in use")
            continue
        result = FeatureDefinition.load(feature_name, feature_def_dict)
        if result.is_err():
            error_list.extend(result.unwrap_err())
            continue
        feature_inventory[feature_name] = result.unwrap()

    # Assign parents
    for feature_name, feature_def in feature_inventory.items():
        if not feature_def.children:
            continue
        for child_name in feature_def.children:
            if child_name not in feature_inventory:
                error_list.append(f"Feature '{feature_name}' references unknown child '{child_name}'")
                continue
            feature_inventory[child_name].parent = feature_name

    if error_list:
        raise ValueError("\n".join(error_list))

    inv = FeatureInventory(feature_inventory)
    check_result = inv.validate()
    if check_result.is_err():
        raise ValueError("\n".join(check_result.unwrap_err()))
    return inv


# ---------------------------------------------------------------------------
# Pytest fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def features() -> FeatureInventory:
    """A small synthetic feature inventory for unit tests."""
    return make_feature_inventory()


@pytest.fixture
def real_features() -> FeatureInventory:
    """The actual feature inventory from inventories/features.toml."""
    result = FeatureInventory.load(INVENTORIES_DIR / "features.toml")
    assert result.is_ok(), f"Failed to load features: {result.unwrap_err()}"
    return result.unwrap()


@pytest.fixture
def real_inventories() -> Inventories:
    """The full Inventories loaded from the inventories/ directory."""
    inv = Inventories.load()
    return inv
