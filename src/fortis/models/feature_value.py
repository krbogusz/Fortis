from dataclasses import dataclass
from typing import Literal

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.result import Err, Ok, Result

type SingleValue = int | None
type ContourValue = list[SingleValue]
type Value = SingleValue | ContourValue

type Position = Literal["any", "initial", "final", "all"] | int | list[int]


@dataclass
class FeatureValue:
    """Value specification."""

    value: Value
    position: Position = "any"

    def __repr__(self) -> str:
        """Repr."""
        if self.value is None:
            value_repr = "∅"
        elif isinstance(self.value, list):
            value_repr = ">".join(str(v) if v is not None else "∅" for v in self.value)
        else:
            value_repr = str(self.value)

        if self.position == "any":
            position_repr = ""
        elif self.position in ["initial", "final", "all"]:
            position_repr = f"@{self.position}"
        elif isinstance(self.position, list):
            position_repr = "@" + ";".join(str(v) for v in self.position)
        else:
            position_repr = f"@{self.position}"

        return value_repr + position_repr

    @classmethod
    def from_str(cls, raw_string: str, feature: str, features: FeatureInventory) -> Result[FeatureValue, str]:
        """Identify a value (single or contour) from a raw string, stripping the feature name first.

        Args:
            raw_string: The raw token (e.g. '+nasal', 'height:2').
            feature: Full feature name to strip from the string.
            features: Feature inventory for type/value resolution.
        """
        # Let's determine the contour specification first
        contour_spec = "any"
        if "@" in raw_string:
            contour_spec_result = cls.determine_contour_position(raw_string.split("@")[1])
            if contour_spec_result.is_err():
                return Err(contour_spec_result.unwrap_err())
            contour_spec = contour_spec_result.unwrap()
            raw_string = raw_string.split("@")[0]

        # Stripping the feature name
        raw_value = raw_string.replace(feature, "")
        raw_value = raw_value.replace(features[feature].short, "")
        raw_value = raw_value.replace(":", "").replace(" ", "")

        # Plain feature name – could be unary, could be an error
        if not raw_value:
            if features[feature].type == "unary":
                return Ok(FeatureValue(1, contour_spec))
            else:
                return Err(f"Could not identify value for '{feature}' from string '{raw_string}'")

        # No '>' means not a contour
        if ">" not in raw_value:
            value_result = cls.single_from_str(raw_value, feature, features)
            if value_result.is_err():
                return Err(value_result.unwrap_err())
            return Ok(FeatureValue(value_result.unwrap(), contour_spec))

        # '>' designates a contour
        contour = []
        raw_contour = raw_value.split(">")
        for raw_contour_value in raw_contour:
            value_result = cls.single_from_str(raw_contour_value, feature, features)
            if value_result.is_err():
                return Err(value_result.unwrap_err())
            contour.append(value_result.unwrap())

        # A contour position list must be one contiguous window of length k
        if isinstance(contour_spec, list):
            if len(contour_spec) != len(contour):
                return Err(
                    f"Contour of length {len(contour)} needs exactly {len(contour)} positions, got {len(contour_spec)}"
                )
            if any(p <= 0 for p in contour_spec):
                return Err(f"Contour positions must be positive (one-indexed): {contour_spec}")
            if len(contour_spec) > 1 and any(b != a + 1 for a, b in zip(contour_spec, contour_spec[1:], strict=False)):
                return Err(f"Contour positions must be contiguous: {contour_spec}")

        return Ok(FeatureValue(contour, contour_spec))

    @staticmethod
    def single_from_str(raw_value: str, feature: str, features: FeatureInventory) -> Result[int | None, str]:
        """Identify a single value (unary/binary/scalar).

        Args:
            raw_value: The value token after stripping the feature name.
            feature: Full feature name.
            features: Feature inventory for type/value resolution.
        """
        if raw_value in config.value_symbols.unspecified:
            return Ok(None)

        if features[feature].type == "unary":
            if raw_value in config.value_symbols.present:
                return Ok(1)
        elif features[feature].type == "binary":
            if raw_value in config.value_symbols.present:
                return Ok(1)
            elif raw_value in config.value_symbols.absent:
                return Ok(0)
        elif features[feature].type == "scalar":
            int_value = safe_int(raw_value)
            if int_value is not None and int_value in features[feature].values:
                return Ok(int_value)
            elif raw_value in features[feature].values.values():
                # First key whose value matches (None if none match)
                key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
                if key is not None:
                    return Ok(key)

        return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")

    @staticmethod
    def determine_contour_position(contour_spec: str) -> Result[Position, str]:
        """Parse the contour position from the part after '@'."""
        if "initial" in contour_spec:
            return Ok("initial")
        if "final" in contour_spec:
            return Ok("final")
        if "all" in contour_spec:
            return Ok("all")
        if "any" in contour_spec:
            return Ok("any")
        if ";" in contour_spec:
            contour_list: list[int] = []
            for single_spec in contour_spec.split(";"):
                parsed = safe_int(single_spec)
                if parsed is None or parsed == 0:
                    return Err(f"Could not identify contour specification from {contour_spec}")
                contour_list.append(parsed)
            return Ok(contour_list)
        parsed = safe_int(contour_spec)
        if parsed is not None and parsed != 0:
            return Ok(parsed)
        return Err(f"Could not identify contour specification from {contour_spec}")

    def matches_pattern(self, pattern: FeatureValue) -> bool:
        """Whether this realized segment value satisfies *pattern*.

        ``self`` is the realized value (its ``position`` is ignored). The
        pattern's value is a window of length ``k`` (a scalar is length one);
        ``pattern.position`` selects the offset(s) at which it must sit within
        this segment's value.

        Args:
            pattern: The specification to test this segment against.
        """
        window = pattern.value if isinstance(pattern.value, list) else [pattern.value]
        target = self.value if isinstance(self.value, list) else [self.value]
        k, length = len(window), len(target)

        def fits(offset: int) -> bool:
            if offset < 0 or offset + k > length:
                return False
            return all(w == target[offset + i] for i, w in enumerate(window))

        match pattern.position:
            case "any":
                return any(fits(o) for o in range(length - k + 1))
            case "all":
                if k == 1:
                    return length >= 1 and all(slot == window[0] for slot in target)
                return length == k and fits(0)
            case "initial":
                return fits(0)
            case "final":
                return fits(length - k)
            case int() as n:
                return fits(n - 1 if n > 0 else length + n)
            case list() as positions:
                if k > 1:  # one contiguous window; validated at parse time
                    start = positions[0]
                    return fits(start - 1 if start > 0 else length + start)
                return all(fits(n - 1 if n > 0 else length + n) for n in positions)
        return False  # unreachable once position is validated

    def matches_exactly(self, other: FeatureValue) -> bool:
        """Whether this value equals *other*'s value, position aside.

        Compares realized content only — same length, same atoms, with a
        scalar treated as a length-one contour. For full structural identity
        (value *and* position) use ``==`` instead.
        """
        own = self.value if isinstance(self.value, list) else [self.value]
        their = other.value if isinstance(other.value, list) else [other.value]
        return own == their

    def form_contour_with(self, other: FeatureValue) -> FeatureValue:
        """Form a contour by appending *other*'s value onto *self*'s."""
        if isinstance(self.value, list):
            self_values = self.value
        else:
            self_values = [self.value]

        if isinstance(other.value, list):
            other_values = other.value
        else:
            other_values = [other.value]

        return FeatureValue(self_values + other_values)
