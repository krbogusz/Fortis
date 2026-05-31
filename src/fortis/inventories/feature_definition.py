from dataclasses import dataclass
from typing import Any

from src.fortis.models.feature_type import FeatureType
from src.fortis.models.tiers import Tier
from src.fortis.result import Err, Ok, Result


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
    type: FeatureType
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

        values_result = cls._load_values(feature_name, feature_def, type_result.unwrap_or(FeatureType.unary))
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
                    type=type_result.unwrap(),
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
    def _load_type(feature_name: str, feature_def: dict[str, Any]) -> Result[FeatureType, str]:
        """Parse and validate the 'type' field.

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
        """
        value = feature_def.get("type")
        if not value:
            return Err(f"Feature '{feature_name}' is missing required field 'type'")
        try:
            ftype = FeatureType(value.strip().lower())
        except ValueError:
            return Err(
                f"Feature '{feature_name}' has invalid type '{value}' "
                + f"(expected {', '.join(t.value for t in FeatureType)})"
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
    def _load_values(feature_name: str, feature_def: dict[str, Any], feature_type: FeatureType) -> Result[dict[int, str], str]:
        """Build the values map based on feature type (unary/binary/scalar).

        Args:
            feature_name: Feature name (for error messages).
            feature_def: Raw dictionary from the TOML file.
            feature_type: Resolved feature type (falls back to unary on earlier errors).
        """
        if feature_type == FeatureType.unary:
            return Ok({1: "present"})
        elif feature_type == FeatureType.binary:
            return Ok({0: "absent", 1: "present"})
        elif feature_type == FeatureType.scalar:
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
