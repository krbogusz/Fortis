from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.elements import AlphaOp
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.values import ContourPosition, SingleValue, Value
from src.fortis.result import Err, Ok, Result

if TYPE_CHECKING:
    from src.fortis.models.bindings import Bindings


@dataclass
class PatternSpec:
    """A feature value in a pattern specification.

    Unlike FeatureValue (realized material), PatternSpec supports negation
    and is used in rule target, context, and exception positions.

    The feature name is the key in the enclosing PatternBundle dict, not a
    field on this class.

    Args:
        value: The pattern's value. When alpha_var is set, value is unresolved
            and the matcher supplies it at match time.
        negated: If the feature is negated.
        alpha_var: Greek letter variable name (e.g. "α", "β") if this spec
            binds or recalls an alpha variable; None for concrete values.
        alpha_op: The alpha operation (same/opposite/other) when alpha_var is set.
    """

    value: Value
    negated: bool = False
    contour_position: ContourPosition = "any"
    alpha_var: str | None = None
    alpha_op: AlphaOp | None = None

    @classmethod
    def from_string(
        cls, raw_spec_string: str, features: FeatureInventory
    ) -> Result[tuple[str, PatternSpec], str]:
        """Parse from a string like '+ nasal', '!+ nasal', 'height:2@initial', 'α high', '-α high'.

        Matches feature names longest-first (full names, then short names).
        Greek-letter tokens produce an alpha variable (alpha_var set, value
        left unresolved).

        Args:
            raw_spec_string: The raw token to parse.
            features: Feature inventory for name/value resolution.
        """
        # Clean input
        raw_spec_string = raw_spec_string.replace(" ", "")

        # Negation
        if "!" in raw_spec_string:
            negated = True
            raw_spec_string = raw_spec_string.replace("!", "", 1)
        else:
            negated = False

        # Contour position
        contour_position: ContourPosition = "any"
        if "@" in raw_spec_string:
            match cls.determine_contour_position(raw_spec_string.split("@")[1]):
                case Err() as err:
                    return err
                case Ok(contour_position_spec):
                    contour_position = contour_position_spec
            raw_spec_string = raw_spec_string.split("@")[0]

        # Identify feature name via greedy longest-first matching
        match features.identify_feature(raw_spec_string):
            case Ok(name):
                feature_name = name
            case Err() as err:
                return err

        # Stripping the feature name
        raw_value_string = raw_spec_string.replace(feature_name, "", 1)
        raw_value_string = raw_value_string.replace(features[feature_name].short, "", 1)
        raw_value_string = raw_value_string.replace(":", "")

        # Check for alpha variable in the value string
        alpha_var: str | None = None
        alpha_op: AlphaOp | None = None

        # Detect alpha prefixes like "α" (same), "-α" (opposite), "!α" (other)
        # These appear in the value portion after stripping the feature name
        # TODO: Phase 5 — full alpha resolution at match time

        # Plain feature name – could be unary, could be an error
        if not raw_value_string:
            if features[feature_name].kind == "unary":
                value: Value = 1
            else:
                return Err(f"Could not identify value for '{feature_name}' from '{raw_value_string}'")

        # No '>' means not a contour
        elif ">" in raw_value_string:
            value_list: list[SingleValue] = []
            raw_contour_string = raw_value_string.split(">")
            for raw_atom_value in raw_contour_string:
                value_result = cls.single_value_from_str(raw_atom_value, feature_name, features)
                if value_result.is_err():
                    return Err(value_result.unwrap_err())
                value_list.append(value_result.unwrap())
            value = tuple(value_list) if len(value_list) > 1 else value_list[0]

        # Single value
        else:
            # Check if the entire value string is a Greek letter (alpha variable)
            if raw_value_string in config.greek_alphabet:
                alpha_var = raw_value_string
                alpha_op = AlphaOp.same
                value = None  # Unresolved; matcher supplies at match time
            else:
                match cls.single_value_from_str(raw_value_string, feature_name, features):
                    case Err() as err:
                        return err
                    case Ok(single_value):
                        value = single_value

        pattern_spec = PatternSpec(value, negated, contour_position, alpha_var, alpha_op)
        match pattern_spec.validate():
            case Err() as err:
                return err
            case Ok():
                return Ok((feature_name, pattern_spec))

    def validate(self) -> Result[bool, str]:
        """Validate the pattern spec."""
        # A contour position list must be one contiguous window of length k
        if isinstance(self.contour_position, list) and isinstance(self.value, list):
            if len(self.contour_position) != len(self.value):
                return Err(
                    f"Contour of length {len(self.value)} needs exactly {len(self.value)} positions, "
                    f"got {len(self.contour_position)}"
                )
            if any(p <= 0 for p in self.contour_position):
                return Err(f"Contour positions must be positive (one-indexed): {self.contour_position}")
            if len(self.contour_position) > 1:
                if any(b != a + 1 for a, b in zip(self.contour_position, self.contour_position[1:], strict=False)):
                    return Err(f"Contour positions must be contiguous: {self.contour_position}")

        return Ok(True)

    def matches_against(self, segment_value: FeatureValue, bindings: Bindings | None = None) -> bool:
        """Whether this pattern spec's value matches a realized segment's value.

        For non-negated specs: the segment value must equal the pattern value.
        For negated specs: the segment value must *not* equal the pattern value.

        # TODO: Phase 5 — alpha variable resolution at match time
        """
        # Alpha variable: match any value (binding/recall happens in Phase 5)
        if self.alpha_var is not None:
            return not self.negated

        pattern_atoms: list[SingleValue] = self.value if isinstance(self.value, list) else [self.value]
        segment_atoms: list[SingleValue] = (
            segment_value.value if isinstance(segment_value.value, list) else [segment_value.value]
        )

        # Simple value comparison
        match = pattern_atoms == segment_atoms

        return (not match) if self.negated else match

    @staticmethod
    def determine_contour_position(contour_position: str) -> Result[ContourPosition, str]:
        """Parse the contour position from the part after '@'."""
        if "initial" in contour_position:
            return Ok("initial")
        if "final" in contour_position:
            return Ok("final")
        if "all" in contour_position:
            return Ok("all")
        if "any" in contour_position:
            return Ok("any")
        if ";" in contour_position:
            contour_list: list[int] = []
            for single_spec in contour_position.split(";"):
                parsed = safe_int(single_spec)
                if parsed is None or parsed == 0:
                    return Err(f"Could not identify contour specification from {contour_position}")
                contour_list.append(parsed)
            return Ok(contour_list)
        parsed = safe_int(contour_position)
        if parsed is not None and parsed != 0:
            return Ok(parsed)
        return Err(f"Could not identify contour specification from {contour_position}")

    @staticmethod
    def single_value_from_str(raw_value: str, feature: str, features: FeatureInventory) -> Result[SingleValue, str]:
        """Identify a single value (unary/binary/scalar/alpha).

        Args:
            raw_value: The value token after stripping the feature name.
            feature: Full feature name.
            features: Feature inventory for type/value resolution.
        """
        if raw_value in config.value_symbols.unspecified:
            return Ok(None)

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
                key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
                if key is not None:
                    return Ok(key)

        return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")