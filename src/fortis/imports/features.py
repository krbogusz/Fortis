from collections import UserDict
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path
from typing import Any

from src.fortis.general.file_handling import load_toml_file
from src.fortis.models.tier import Tier
from src.fortis.result import Err, Ok, Result


class FeatureKind(StrEnum):
    """Whether a feature is unary, binary, or scalar."""

    unary = auto()
    binary = auto()
    scalar = auto()


@dataclass
class FeatureDefinition:
    """A feature's tier, type, short name, values, and hierarchical relations.

    Args:
        tier: Phonological tier this feature belongs to.
        type: Whether the feature is unary, binary, or scalar.
        short: Short/abbreviated name for compact notation.
        values: Mapping of integer codes to human-readable labels.
        children: Sub-features in the feature hierarchy, if any.
        parent: Name of the parent feature, assigned after loading.
    """

    name: str
    tier: Tier
    kind: FeatureKind
    short: str
    values: dict[int, str]
    children: list[str] | None
    parent: str | None = None

    # —— Main loading method ——————————————————————————————————————————————————————————————————————
    @classmethod
    def load(cls, feature_name: str, feature_def: dict[str, Any]) -> Result[FeatureDefinition, list[str]]:
        """Build a FeatureDefinition from a raw TOML entry.

        Args:
            feature_name: Full name of the feature.
            feature_def: Raw dictionary from the TOML file.
        """
        error_list = []

        tier_result = cls._load_tier(feature_name, feature_def)
        if tier_result.is_err():
            error_list.append(tier_result.unwrap_err())

        type_result = cls._load_type(feature_name, feature_def)
        if type_result.is_err():
            error_list.append(type_result.unwrap_err())

        short_result = cls._load_short(feature_name, feature_def)
        if short_result.is_err():
            error_list.append(short_result.unwrap_err())

        values_result = cls._load_values(feature_name, feature_def, type_result.unwrap_or(FeatureKind.unary))
        if values_result.is_err():
            error_list.append(values_result.unwrap_err())

        children_result = cls._load_children(feature_name, feature_def)
        if children_result.is_err():
            error_list.append(children_result.unwrap_err())

        if error_list:
            return Err(error_list)
        else:
            return Ok(
                FeatureDefinition(
                    name=feature_name,
                    tier=tier_result.unwrap(),
                    kind=type_result.unwrap(),
                    short=short_result.unwrap(),
                    values=values_result.unwrap(),
                    children=children_result.unwrap(),
                )
            )

    # —— Loading helpers ——————————————————————————————————————————————————————————————————————————
    @staticmethod
    def _load_tier(feature_name: str, feature_def: dict[str, Any]) -> Result[Tier, str]:
        """Parse and validate the 'tier' field.

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
        """
        value = feature_def.get("tier")
        if not value:
            return Err(f"Feature '{feature_name}' is missing required field 'tier'")
        try:
            tier = Tier(value.strip().lower())
        except ValueError:
            return Err(
                f"Feature '{feature_name}' has invalid tier '{value}' "
                + f"(expected {', '.join(t.value for t in Tier)})"
            )
        return Ok(tier)

    @staticmethod
    def _load_type(feature_name: str, feature_def: dict[str, Any]) -> Result[FeatureKind, str]:
        """Parse and validate the 'type' field.

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
        """
        value = feature_def.get("type")
        if not value:
            return Err(f"Feature '{feature_name}' is missing required field 'type'")
        try:
            ftype = FeatureKind(value.strip().lower())
        except ValueError:
            return Err(
                f"Feature '{feature_name}' has invalid type '{value}' "
                + f"(expected {', '.join(t.value for t in FeatureKind)})"
            )
        return Ok(ftype)

    @staticmethod
    def _load_short(feature_name: str, feature_def: dict[str, Any]) -> Result[str, str]:
        """Parse the 'short' field; defaults to the feature name itself.

        Args:
            feature_name: Feature name (used as default short name).
            feature_def: Raw dictionary from the TOML file.
        """
        if "short" not in feature_def:
            return Ok(feature_name)
        value = feature_def["short"]
        if not isinstance(value, str):
            return Err(f"Feature '{feature_name}' field 'short' is not a string")
        if not value.strip():
            return Err(f"Feature '{feature_name}' has an empty 'short' field")
        stripped = value.strip()
        if " " in stripped or "\t" in stripped:
            return Err(f"Feature '{feature_name}' short name '{stripped}' contains whitespace")
        return Ok(stripped)

    @staticmethod
    def _load_values(
        feature_name: str, feature_def: dict[str, Any], feature_type: FeatureKind
    ) -> Result[dict[int, str], str]:
        """Build the values map based on feature type (unary/binary/scalar).

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
            feature_type: Resolved feature type (falls back to unary on earlier errors).
        """
        if feature_type == FeatureKind.unary:
            return Ok({1: "present"})
        elif feature_type == FeatureKind.binary:
            return Ok({0: "absent", 1: "present"})
        elif feature_type == FeatureKind.scalar:
            raw_values = feature_def.get("values")
            if not raw_values:
                return Err(f"Feature '{feature_name}' is scalar, but does not have specified 'values'")
            if not isinstance(raw_values, dict):
                return Err(f"Feature '{feature_name}' has 'values' field that is not a dictionary")
            sanitized_values: dict[int, str] = {}
            for value, label in raw_values.items():
                # TOML inline table keys are always strings; accept string representations of integers
                if isinstance(value, str):
                    try:
                        value = int(value)
                    except ValueError:
                        return Err(f"Feature '{feature_name}' value '{value}' is not an integer")
                if not isinstance(value, int):
                    return Err(f"Feature '{feature_name}' value '{value}' is not an integer")
                if not isinstance(label, str):
                    return Err(f"Feature '{feature_name}' value '{value}' has a label that is not a string")
                if not label.strip():
                    return Err(f"Feature '{feature_name}' value '{value}' has an empty label")
                sanitized_values[value] = label.strip().lower()
            return Ok(sanitized_values)
        else:
            return Err(f"Feature '{feature_name}' has an unknown feature type '{feature_type}'")

    @staticmethod
    def _load_children(feature_name: str, feature_def: dict[str, Any]) -> Result[list[str] | None, str]:
        """Parse the optional 'children' field.

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
        """
        if "children" not in feature_def:
            return Ok(None)
        raw_children = feature_def["children"]
        if isinstance(raw_children, str):
            if not raw_children.strip():
                return Err(f"Feature '{feature_name}' has an empty 'children' field")
            return Ok([raw_children.strip()])
        if isinstance(raw_children, list):
            if not raw_children:
                return Err(f"Feature '{feature_name}' has an empty 'children' field")
            sanitized: list[str] = []
            for child in raw_children:
                if not isinstance(child, str):
                    return Err(f"Feature '{feature_name}' has a non-string child '{child}'")
                if not child.strip():
                    return Err(f"Feature '{feature_name}' has an empty child name")
                sanitized.append(child.strip())
            return Ok(sanitized)
        return Err(f"Feature '{feature_name}' field 'children' is neither a string nor a list")


class FeatureInventory(UserDict[str, FeatureDefinition]):
    """Feature definitions keyed by name, loaded from TOML with cross-feature validation."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initiate the inventory."""
        super().__init__(*args, **kwargs)
        self._build_name_indices()

    def _build_name_indices(self) -> None:
        """Pre-compute sorted name lists and short→full mapping for greedy longest-first matching."""
        self._full_names: list[str] = sorted(self.keys(), key=len, reverse=True)
        self._short_to_full: dict[str, str] = {}
        for name, ft_def in self.items():
            if ft_def.short != name:
                self._short_to_full[ft_def.short] = name
        self._short_names: list[str] = sorted(self._short_to_full.keys(), key=len, reverse=True)

    def identify_feature(self, raw_string: str) -> Result[str, str]:
        """Identify a feature name in *raw_string* by greedy longest-first matching.

        Scans for full feature names first, then short names, picking the
        longest match. Returns the full (canonical) feature name.

        Args:
            raw_string: A raw token that may contain a feature name (e.g. '+nasal', 'height:2').
        """
        for name in self._full_names + self._short_names:
            if name in raw_string:
                return Ok(self._short_to_full.get(name, name))
        return Err(f"Could not identify feature in '{raw_string}'")

    @classmethod
    def load(cls, path: Path) -> Result[FeatureInventory, list[str]]:
        """Load from a TOML file, assign parents, and run cross-feature checks.

        Args:
            path: Path to the TOML file.
        """
        error_list = []

        data_result = load_toml_file(path)
        if data_result.is_err():
            return Err([data_result.unwrap_err()])
        data = data_result.unwrap()

        feature_inventory = {}
        for feature_name, feature_def_dict in data.items():
            feature_name = feature_name.strip()
            if " " in feature_name or "\t" in feature_name:
                error_list.append(f"Feature name '{feature_name}' contains whitespace")
                continue
            if feature_name in feature_inventory:
                error_list.append(f"Feature name '{feature_name}' is already in use")
                continue

            feature_def_result = FeatureDefinition.load(feature_name, feature_def_dict)
            if feature_def_result.is_err():
                error_list.extend(feature_def_result.unwrap_err())
                continue

            feature_inventory[feature_name] = feature_def_result.unwrap()

        for feature_name, feature_def in feature_inventory.items():
            if not feature_def.children:
                continue
            for child_name in feature_def.children:
                if child_name not in feature_inventory:
                    error_list.append(f"Feature '{feature_name}' references unknown child '{child_name}'")
                    continue
                feature_inventory[child_name].parent = feature_name

        if error_list:
            return Err(error_list)

        inventory = cls(feature_inventory)
        check_result = inventory.validate()
        if check_result.is_err():
            return Err(check_result.unwrap_err())

        return Ok(inventory)

    def validate(self) -> Result[None, list[str]]:
        """Validate unique names/shorts, tier consistency, and no circular parent chains."""
        error_list = []

        seen_names: dict[str, str] = {}
        seen_shorts: dict[str, str] = {}

        for feature_name, ft_def in self.data.items():
            # Unique long names
            if feature_name in seen_names:
                error_list.append(
                    f"Feature name '{feature_name}' is already used by feature '{seen_names[feature_name]}'"
                )
            seen_names[feature_name] = feature_name

            # Unique short names — a feature's own long name matching its short is fine
            if ft_def.short in seen_shorts:
                other = seen_shorts[ft_def.short]
                if other != feature_name:
                    error_list.append(
                        f"Feature '{feature_name}' has short name '{ft_def.short}' already used by feature '{other}'"
                    )
            if ft_def.short != feature_name:
                seen_shorts[ft_def.short] = feature_name

        # Children on the same tier as parent
        for feature_name, ft_def in self.data.items():
            if not ft_def.children:
                continue
            for child_name in ft_def.children:
                if child_name not in self.data:
                    continue  # already caught in load
                child_def = self.data[child_name]
                if child_def.tier != ft_def.tier:
                    error_list.append(
                        f"Feature '{child_name}' (tier: {child_def.tier.value}) "
                        f"cannot be a child of '{feature_name}' (tier: {ft_def.tier.value})"
                    )

        # No circular parent chains
        for feature_name in self.data:
            visited: set[str] = set()
            current = feature_name
            while current is not None:
                if current in visited:
                    error_list.append(f"Feature '{feature_name}' has a circular parent chain")
                    break
                visited.add(current)
                current = self.data[current].parent

        if error_list:
            return Err(error_list)

        return Ok(None)
