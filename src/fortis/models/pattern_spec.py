from dataclasses import dataclass

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.bindings import Bindings
from src.fortis.models.values import ContourPosition, SingleValue, Value
from src.fortis.result import Err, Ok, Result


@dataclass
class PatternSpec:
    """A feature name paired with its value.

    Unlike FeatureSpec (realized material), PatternSpec supports negation
    and is used in rule target, result, context, and exception positions.

    Args:
        feature: Full feature name.
        value: The pattern's value.
        is_negated: If the feature is negated.
    """

    feature: str
    value: Value
    negated: bool = False
    contour_position: ContourPosition = "any"

    @classmethod
    def from_string(
        cls, raw_spec_string: str, features: FeatureInventory, bindings: Bindings
    ) -> Result[PatternSpec, str]:
        """Parse from a string like '+ nasal', '!+ nasal', 'height:2@initial', '-α high'.

        Matches feature names longest-first (full names, then short names).

        Args:
            raw_spec_string: The raw token to parse.
            features: Feature inventory for name/value resolution.
            bindings: Environment variables.
        """
        # Clean input
        raw_spec_string = raw_spec_string.replace(" ", "")

        # Identify feature name via greedy longest-first matching
        match features.identify_feature(raw_spec_string):
            case Ok(name):
                feature_name = name
            case Err() as err:
                return err

        # Negation
        if "!" in raw_spec_string:
            negated = True
            raw_spec_string = raw_spec_string.replace("!", "", 1)
        else:
            negated = False

        # Contour position
        contour_position = "any"
        if "@" in raw_spec_string:
            match cls.determine_contour_position(raw_spec_string.split("@")[1]):
                case Err() as err:
                    return err
                case Ok(contour_position_spec):
                    contour_position = contour_position_spec
            raw_spec_string = raw_spec_string.split("@")[0]

        # Stripping the feature name
        raw_value_string = raw_spec_string.replace(feature_name, "", 1)
        raw_value_string = raw_value_string.replace(features[feature_name].short, "", 1)
        raw_value_string = raw_value_string.replace(":", "")

        # Plain feature name – could be unary, could be an error
        if not raw_value_string:
            if features[feature_name].kind == "unary":
                value = 1
            else:
                return Err(f"Could not identify value for '{feature_name}' from '{raw_value_string}'")

        # No '>' means not a contour
        elif ">" in raw_value_string:
            value = []
            raw_contour_string = raw_value_string.split(">")
            for raw_atom_value in raw_contour_string:
                # Alpha variable (Greek letter)
                if raw_atom_value in config.greek_alphabet:
                    if raw_atom_value in bindings.alpha:
                        value.append(bindings.alpha.unwrap())
                value_result = cls.single_value_from_str(raw_atom_value, feature_name, features)
                if value_result.is_err():
                    return Err(value_result.unwrap_err())
                value.append(value_result.unwrap())

        # '>' designates a contour
        else:
            match cls.single_value_from_str(raw_value_string, feature_name, features):
                case Err() as err:
                    return err
                case Ok(single_value):
                    value = single_value

        pattern_spec = PatternSpec(feature_name, value, negated, contour_position)
        match pattern_spec.validate():
            case Err() as err:
                return err
            case Ok():
                return Ok(pattern_spec)

    def validate(self) -> Result[bool, str]:
        """Validate the pattern spec."""
        # A contour position list must be one contiguous window of length k
        if isinstance(self.contour_position, list) and isinstance(self.value, list):
            if len(self.contour_position) != len(self.value):
                return Err(
                    f"Contour of length {len(self.value)} needs exactly {len(self.value)} positions, "
                    "got {len(self.contour_position)}"
                )
            if any(p <= 0 for p in self.contour_position):
                return Err(f"Contour positions must be positive (one-indexed): {self.contour_position}")
            if len(self.contour_position) > 1:
                if any(b != a + 1 for a, b in zip(self.contour_position, self.contour_position[1:], strict=False)):
                    return Err(f"Contour positions must be contiguous: {self.contour_position}")

        return Ok(True)

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
