from __future__ import annotations

from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.features import Feature, FeatureInventory, FeatureKind
from src.fortis.models.tiers import Tier
from src.fortis.result import Err, Ok, Result

# ---- Feature ------------------------------------------------------------------------------------


def load_feature(feature: str, feature_def: dict[str, Any]) -> Result[Feature, list[str]]:
    """Load a Feature from a raw TOML entry.

    Args:
        feature: Full name of the feature.
        feature_def: Raw dictionary from the TOML file.
    """
    error_list: list[str] = []

    match load_tier(feature, feature_def):
        case Err(err):
            error_list.append(err)
            tier = Tier.segment  # Dummy value for the type checker
        case Ok(result):
            tier = result

    match load_kind(feature, feature_def):
        case Err(err):
            error_list.append(err)
            kind = FeatureKind.unary  # Dummy value for the type checker
        case Ok(result):
            kind = result

    match load_short(feature, feature_def):
        case Err(err):
            error_list.append(err)
            short_name = feature  # Dummy value for the type checker
        case Ok(result):
            short_name = result

    match load_values(feature, feature_def, kind):
        case Err(err):
            error_list.append(err)
            values = {}  # Dummy value for the type checker
        case Ok(result):
            values = result

    match load_children(feature, feature_def):
        case Err(err):
            error_list.append(err)
            children = ()  # Dummy value for the type checker
        case Ok(result):
            children = result

    if error_list:
        return Err(error_list)

    return Ok(
        Feature(
            name=feature,
            tier=tier,
            kind=kind,
            short_name=short_name,
            values=values,
            children=children,
        )
    )


def load_tier(feature: str, feature_def: dict[str, Any]) -> Result[Tier, str]:
    """Parse and validate the 'tier' field.

    Args:
        feature: Feature name (for error messages).
        feature_def: Raw dictionary from the TOML file.
    """
    tier = feature_def.get("tier")
    if not tier:
        return Ok(Tier.segment)  # default: segmental (suprasegmentals live in tiers.toml)
    try:
        tier = Tier(tier.strip().lower())
    except ValueError:
        expected = ", ".join(t.value for t in Tier)
        return Err(f"Feature '{feature}' has an invalid tier '{tier}' (expected {expected})")
    return Ok(tier)


def load_kind(feature: str, feature_def: dict[str, Any]) -> Result[FeatureKind, str]:
    """Parse and validate the 'kind' field.

    Args:
        feature: Feature name (for error messages).
        feature_def: Raw dictionary from the TOML file.
    """
    kind = feature_def.get("kind")
    if not kind:
        return Err(f"Feature '{feature}' is missing the required field 'type'")
    try:
        kind = FeatureKind(kind.strip().lower())
    except ValueError:
        expected = ", ".join(t.value for t in FeatureKind)
        return Err(f"Feature '{feature}' has an invalid kind '{kind}' (expected {expected})")
    return Ok(kind)


def load_short(feature: str, feature_def: dict[str, Any]) -> Result[str, str]:
    """Parse the 'short' field; defaults to the feature name itself.

    Args:
        feature: Feature name (used as default short name).
        feature_def: Raw dictionary from the TOML file.
    """
    if "short" not in feature_def:
        return Ok(feature)
    value = feature_def["short"]
    if not isinstance(value, str):
        return Err(f"Feature '{feature}' field 'short' is not a string")
    if not value.strip():
        return Ok(feature)  # a blank `short` field defaults to the feature name
    stripped = value.strip()
    if " " in stripped or "\t" in stripped:
        return Err(f"Feature '{feature}' has a short name '{stripped}' that contains whitespace")
    return Ok(stripped)


def load_values(
    feature: str, feature_def: dict[str, Any], kind: FeatureKind
) -> Result[dict[int, str], str]:
    """Build the values map based on feature kind (unary/binary/scalar).

    Args:
        feature: Feature name (for error messages).
        feature_def: Raw dictionary from the TOML file.
        kind: Resolved feature kind (falls back to unary on earlier errors).
    """
    if kind == FeatureKind.unary:
        return Ok({1: "present"})
    elif kind == FeatureKind.binary:
        return Ok({0: "absent", 1: "present"})
    elif kind == FeatureKind.scalar:
        raw_values = feature_def.get("values")
        if not raw_values:
            return Err(f"Feature '{feature}' is scalar, but does not have specified 'values'")
        if not isinstance(raw_values, dict):
            return Err(f"Feature '{feature}' has 'values' field that is not a dictionary")
        sanitized_values: dict[int, str] = {}
        for value, label in raw_values.items():
            # TOML inline table keys are always strings; accept string representations of integers
            if isinstance(value, str):
                try:
                    value = int(value)
                except ValueError:
                    return Err(f"Feature '{feature}' value '{value}' is not an integer")
            if not isinstance(value, int):
                return Err(f"Feature '{feature}' value '{value}' is not an integer")
            if not isinstance(label, str):
                return Err(f"Feature '{feature}' value '{value}' has a label that is not a string")
            if not label.strip():
                return Err(f"Feature '{feature}' value '{value}' has an empty label")
            sanitized_values[value] = label.strip().lower()
        return Ok(sanitized_values)
    else:
        return Err(f"Feature '{feature}' has an unknown feature type '{kind}'")


def load_children(feature: str, feature_def: dict[str, Any]) -> Result[tuple[str, ...] | None, str]:
    """Parse the optional 'children' field.

    Args:
        feature: Feature name (for error messages).
        feature_def: Raw dictionary from the TOML file.
    """
    if "children" not in feature_def:
        return Ok(None)
    raw_children = feature_def["children"]
    if isinstance(raw_children, str):
        if not raw_children.strip():
            return Ok(None)
        return Ok((raw_children.strip(),))
    if isinstance(raw_children, list):
        if not raw_children:
            return Ok(None)
        sanitized: tuple[str, ...] = ()
        for child in raw_children:
            if not isinstance(child, str):
                return Err(f"Feature '{feature}' has a non-string child '{child}'")
            if not child.strip():
                return Err(f"Feature '{feature}' has an empty child name")
            sanitized = sanitized + (child.strip(),)
        return Ok(sanitized)
    return Err(f"Feature '{feature}' field 'children' is neither a string nor a list")


# ---- Feature Inventory --------------------------------------------------------------------------


def load_feature_inventory(path: Path) -> Result[FeatureInventory, list[str]]:
    """Load from a TOML file, assign parents, and run cross-feature checks.

    Args:
        path: Path to the TOML file.
    """
    error_list = []

    match load_toml_file(path):
        case Err(err):
            return Err([err])
        case Ok(result):
            data = result

    feature_inventory = FeatureInventory()
    for feature, feature_def in data.items():
        feature = feature.strip()
        if " " in feature or "\t" in feature:
            error_list.append(f"Feature name '{feature}' contains whitespace")
            continue
        if feature in feature_inventory:
            error_list.append(f"Feature name '{feature}' is already in use")
            continue

        match load_feature(feature, feature_def):
            case Err(err):
                error_list.extend(err)
                continue
            case Ok(result):
                feature_inventory[feature] = result

    for feature, feature_def in feature_inventory.items():
        if not feature_def.children:
            continue
        for child_name in feature_def.children:
            if child_name not in feature_inventory:
                error_list.append(f"Feature '{feature}' references unknown child '{child_name}'")
                continue
            feature_inventory[child_name].parent = feature

    if error_list:
        return Err(error_list)

    _synthesize_root(feature_inventory)

    match validate_feature_inventory(feature_inventory):
        case Err(err):
            return Err(err)
        case Ok(result):
            return Ok(feature_inventory)


def _synthesize_root(inventory: FeatureInventory) -> None:
    """Parent every top-level segmental feature to a single ``root`` node, building it if absent.

    So an inventory needn't declare a root: whatever segmental features are left unparented
    become children of an auto-built ``root`` — the segment's apex. An explicitly declared
    ``root`` is honoured and simply absorbs any segmental features still unparented.
    """
    tops = [
        name
        for name, feature in inventory.data.items()
        if feature.tier == Tier.segment and feature.parent is None and name != "root"
    ]
    if not tops:
        return
    if "root" in inventory.data:
        root = inventory.data["root"]
        root.children = tuple(root.children or ()) + tuple(tops)
    else:
        inventory["root"] = Feature(
            name="root",
            tier=Tier.segment,
            kind=FeatureKind.unary,
            short_name="root",
            values={},
            children=tuple(tops),
        )
    for name in tops:
        inventory.data[name].parent = "root"


def validate_feature_inventory(feature_inventory: FeatureInventory) -> Result[None, list[str]]:
    """Validate unique names/shorts, tier consistency, and no circular parent chains."""
    error_list = []

    seen_names: dict[str, str] = {}
    seen_shorts: dict[str, str] = {}

    for feature, ft_def in feature_inventory.data.items():
        # Unique long names
        if feature in seen_names:
            error_list.append(
                f"Feature name '{feature}' is already used by feature '{seen_names[feature]}'"
            )
        seen_names[feature] = feature

        # Unique short names — a feature's own long name matching its short is fine
        if ft_def.short_name in seen_shorts:
            other = seen_shorts[ft_def.short_name]
            if other != feature:
                short = ft_def.short_name
                error_list.append(
                    f"Feature '{feature}' has short name '{short}' already used by '{other}'"
                )
        if ft_def.short_name != feature:
            seen_shorts[ft_def.short_name] = feature

    # Children on the same tier as parent
    for feature, ft_def in feature_inventory.data.items():
        if not ft_def.children:
            continue
        for child_name in ft_def.children:
            if child_name not in feature_inventory.data:
                continue  # already caught in load
            child_def = feature_inventory.data[child_name]
            if child_def.tier != ft_def.tier:
                error_list.append(
                    f"Feature '{child_name}' (tier: {child_def.tier.value}) "
                    f"cannot be a child of '{feature}' (tier: {ft_def.tier.value})"
                )

    # No circular parent chains
    for feature in feature_inventory.data:
        visited: set[str] = set()
        current = feature
        while current is not None:
            if current in visited:
                error_list.append(f"Feature '{feature}' has a circular parent chain")
                break
            visited.add(current)
            current = feature_inventory.data[current].parent

    if error_list:
        return Err(error_list)

    return Ok(None)
