from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.models.feature_inventory import FeatureInventory
from src.fortis.result import Err, Ok, Result


def present_value(value: int | None) -> str:
    """Format a single feature value as a display string."""
    if value is None:
        return "∅"
    if value == 1:
        return "+"
    if value == 0:
        return "-"
    return str(value)


def value_from_str(
    raw_string: str, feature: str, inventory: FeatureInventory, bare_unary_means_present: bool = False
) -> Result[int | list[int | None] | None, str]:
    """Identify a value (single or contour) from a raw string, stripping the feature name first.

    Args:
        raw_string: The raw token (e.g. '+nasal', 'height:2').
        feature: Full feature name to strip from the string.
        inventory: Feature inventory for type/value resolution.
        bare_unary_means_present: If True, a bare name on a unary feature yields 1.
    """
    raw_value = raw_string.replace(":", "").replace(" ", "")
    raw_value = raw_value.replace(feature, "")
    raw_value = raw_value.replace(inventory[feature].short, "")
    if not raw_value:
        if bare_unary_means_present and inventory[feature].type == "unary":
            return Ok(1)
        else:
            return Err(f"Could not identify value for '{feature}' from string '{raw_string}'")
    if ">" not in raw_value:
        value_result = single_value_from_str(raw_value, feature, inventory)
        if value_result.is_err():
            return Err(value_result.unwrap_err())
        return Ok(value_result.unwrap())
    else:
        contour = []
        raw_contour = raw_value.split(">")
        for raw_contour_value in raw_contour:
            value_result = single_value_from_str(raw_contour_value, feature, inventory)
            if value_result.is_err():
                return Err(value_result.unwrap_err())
            contour.append(value_result.unwrap())
        return Ok(contour)


def single_value_from_str(raw_value: str, feature: str, inventory: FeatureInventory) -> Result[int | None, str]:
    """Identify a single value (unary/binary/scalar).

    Args:
        raw_value: The value token after stripping the feature name.
        feature: Full feature name.
        inventory: Feature inventory for type/value resolution.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    if inventory[feature].type == "unary":
        if raw_value in config.value_symbols.present:
            return Ok(1)
    elif inventory[feature].type == "binary":
        if raw_value in config.value_symbols.present:
            return Ok(1)
        elif raw_value in config.value_symbols.absent:
            return Ok(0)
    elif inventory[feature].type == "scalar":
        int_value = safe_int(raw_value)
        if int_value is not None and int_value in inventory[feature].values:
            return Ok(int_value)
        elif raw_value in inventory[feature].values.values():
            # First key whose value matches (None if none match)
            key = next((k for k, v in inventory[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")
