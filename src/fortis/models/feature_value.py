from dataclasses import dataclass

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.values import ContourValue, SingleValue, Value
from src.fortis.result import Err, Ok, Result


@dataclass
class FeatureValue:
    """A value in a realized feature specification.

    Holds a single atomic value (int or None) or a contour (list of values).
    No position or negation — those belong in PatternValue.
    """

    value: Value

    def __repr__(self) -> str:
        """Repr."""
        if self.value is None:
            return "∅"
        elif isinstance(self.value, list):
            return ">".join(str(v) if v is not None else "∅" for v in self.value)
        else:
            return str(self.value)

    @classmethod
    def from_str(cls, raw_string: str, feature: str, features: FeatureInventory) -> Result[FeatureValue, str]:
        """Identify a value (single or contour) from a raw string, stripping the feature name first.

        Args:
            raw_string: The raw token (e.g. '+nasal', 'height:2').
            feature: Full feature name to strip from the string.
            features: Feature inventory for type/value resolution.
        """
        # Stripping the feature name
        raw_value = raw_string.replace(feature, "")
        raw_value = raw_value.replace(features[feature].short, "")
        raw_value = raw_value.replace(":", "").replace(" ", "")

        # Plain feature name – could be unary, could be an error
        if not raw_value:
            if features[feature].kind == "unary":
                return Ok(FeatureValue(1))
            else:
                return Err(f"Could not identify value for '{feature}' from string '{raw_string}'")

        # No '>' means not a contour
        if ">" not in raw_value:
            value_result = cls.single_from_str(raw_value, feature, features)
            if value_result.is_err():
                return Err(value_result.unwrap_err())
            return Ok(FeatureValue(value_result.unwrap()))

        # '>' designates a contour
        contour: list[SingleValue] = []
        raw_contour = raw_value.split(">")
        for raw_contour_value in raw_contour:
            value_result = cls.single_from_str(raw_contour_value, feature, features)
            if value_result.is_err():
                return Err(value_result.unwrap_err())
            contour.append(value_result.unwrap())

        return Ok(FeatureValue(contour))

    @staticmethod
    def single_from_str(raw_value: str, feature: str, features: FeatureInventory) -> Result[SingleValue, str]:
        """Identify a single value (unary/binary/scalar).

        Alpha variables (Greek letters) are not valid in realized material
        and produce a specific error.

        Args:
            raw_value: The value token after stripping the feature name.
            feature: Full feature name.
            features: Feature inventory for type/value resolution.
        """
        if raw_value in config.value_symbols.unspecified:
            return Ok(None)

        # Alpha variables are not valid in realized material
        if raw_value in config.greek_alphabet:
            return Err(f"Alpha variable '{raw_value}' is not valid in realized material for '{feature}'")

        if features[feature].kind == "unary":
            if raw_value in config.value_symbols.present:
                return Ok(1)
        elif features[feature].kind == "binary":
            if raw_value in config.value_symbols.present:
                return Ok(1)
            elif raw_value in config.value_symbols.absent:
                return Ok(0)
        elif features[feature].kind == "scalar":
            int_value = safe_int(raw_value)
            if int_value is not None and int_value in features[feature].values:
                return Ok(int_value)
            elif raw_value in features[feature].values.values():
                # First key whose value matches (None if none match)
                key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
                if key is not None:
                    return Ok(key)

        return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")

    def form_contour_with(self, other: FeatureValue) -> FeatureValue:
        """Form a contour by appending *other*'s value onto *self*'s."""
        self_values: list[SingleValue] = self.value if isinstance(self.value, list) else [self.value]
        other_values: list[SingleValue] = other.value if isinstance(other.value, list) else [other.value]
        contour: ContourValue = self_values + other_values
        return FeatureValue(contour)
