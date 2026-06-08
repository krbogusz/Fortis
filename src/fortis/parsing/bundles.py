"""Bundle and value parsing — concrete and pattern material from strings."""

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.elements import AlphaOp
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.pattern_bundle import PatternBundle
from src.fortis.models.pattern_spec import PatternSpec
from src.fortis.models.values import ContourPosition, SingleValue, Value
from src.fortis.result import Err, Ok, Result

# ---------------------------------------------------------------------------
# FeatureValue parsing
# ---------------------------------------------------------------------------


def parse_feature_value(raw_string: str, feature: str, features: FeatureInventory) -> Result[FeatureValue, str]:
    """Parse a FeatureValue from a raw string, stripping the feature name.

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
        value_result = _single_feature_value(raw_value, feature, features)
        if value_result.is_err():
            return Err(value_result.unwrap_err())
        return Ok(FeatureValue(value_result.unwrap()))

    # '>' designates a contour
    contour: list[SingleValue] = []
    raw_contour = raw_value.split(">")
    for raw_contour_value in raw_contour:
        value_result = _single_feature_value(raw_contour_value, feature, features)
        if value_result.is_err():
            return Err(value_result.unwrap_err())
        contour.append(value_result.unwrap())

    return Ok(FeatureValue(contour))


def _single_feature_value(raw_value: str, feature: str, features: FeatureInventory) -> Result[SingleValue, str]:
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
            key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")


# ---------------------------------------------------------------------------
# FeatureBundle parsing
# ---------------------------------------------------------------------------


def parse_feature_bundle(raw_string: str, features: FeatureInventory) -> Result[FeatureBundle, list[str]]:
    """Parse a comma-separated feature bundle string (e.g. '+syll, -cons, height:2').

    Args:
        raw_string: Comma- or semicolon-separated feature specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    tokens = [t.strip() for t in string.split(",") if t.strip()]

    bundle = FeatureBundle()
    for token in tokens:
        # Identify feature name first, then parse value
        match features.identify_feature(token.replace(" ", "")):
            case Ok(feature_name):
                pass
            case Err() as err:
                error_list.append(err.unwrap_err())
                continue

        value_result = parse_feature_value(token, feature_name, features)
        if value_result.is_err():
            error_list.append(value_result.unwrap_err())
            continue
        bundle[feature_name] = value_result.unwrap()

    if error_list:
        return Err(error_list)

    return Ok(bundle)


# ---------------------------------------------------------------------------
# PatternSpec parsing
# ---------------------------------------------------------------------------


def parse_pattern_spec(raw_spec_string: str, features: FeatureInventory) -> Result[tuple[str, PatternSpec], str]:
    """Parse a PatternSpec from a string like '+ nasal', '!+ nasal', 'height:2@initial', 'α high'.

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
        match _determine_contour_position(raw_spec_string.split("@")[1]):
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
            value_result = _single_pattern_value(raw_atom_value, feature_name, features)
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
            match _single_pattern_value(raw_value_string, feature_name, features):
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


def _single_pattern_value(raw_value: str, feature: str, features: FeatureInventory) -> Result[SingleValue, str]:
    """Identify a single value (unary/binary/scalar) for pattern parsing.

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


def _determine_contour_position(contour_position: str) -> Result[ContourPosition, str]:
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


# ---------------------------------------------------------------------------
# PatternBundle parsing
# ---------------------------------------------------------------------------


def parse_pattern_bundle(raw_string: str, features: FeatureInventory) -> Result[PatternBundle, list[str]]:
    """Parse a comma-separated pattern bundle string.

    Args:
        raw_string: Comma- or semicolon-separated pattern specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    tokens = [t.strip() for t in string.split(",") if t.strip()]

    bundle = PatternBundle()
    for token in tokens:
        result = parse_pattern_spec(token, features)
        if result.is_err():
            error_list.append(result.unwrap_err())
            continue
        feature_name, spec = result.unwrap()
        bundle[feature_name] = spec

    if error_list:
        return Err(error_list)

    return Ok(bundle)