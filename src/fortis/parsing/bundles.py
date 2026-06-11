"""Bundle and value parsing — concrete and pattern material from strings."""

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.loaders.features import FeatureInventory
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.specs import PatternSpec, ResultSpec
from src.fortis.models.values import (
    AlphaOp,
    AlphaRef,
    ContourEdge,
    ContourPosition,
    Limb,
    Value,
    Wildcard,
    make_value,
)
from src.fortis.result import Err, Ok, Result

# --------------------------------------------------------------------------------------------------
# General
# --------------------------------------------------------------------------------------------------


def identify_feature(raw_string: str, features: FeatureInventory) -> Result[tuple[str, str], str]:
    """Identify a feature from a string.

    Returns the name of the feature and the matched string.

    Covers a few ways of writing a feature:
        unary – 'nasal', 'nasal: +', '+nasal', 'nas', 'nas: +', '+nas',
        binary – 'syllabic: ±', '+syllabic', 'syll: ±', '+syll',
        scalar – 'height: 1', 'height: low', 'lo: lo'
    """
    raw_string = raw_string.replace(" ", "")

    for name in features.names_by_length:
        if name in raw_string:
            return Ok((name, name))
    for short_name in features.short_names_by_length:
        if short_name in raw_string:
            name = features.short_to_long_name[short_name]
            return Ok((name, short_name))

    return Err(f"No feature could be identified from '{raw_string}'")


def determine_contour_position(contour_position: str) -> Result[ContourPosition, str]:
    """Parse the contour position from the part after '@'."""
    if "initial" in contour_position:
        return Ok(ContourEdge.initial)
    if "final" in contour_position:
        return Ok(ContourEdge.final)
    if "all" in contour_position:
        return Ok(ContourEdge.all)
    if "any" in contour_position:
        return Ok(ContourEdge.any)
    if ";" in contour_position:
        contour_list: tuple = ()
        for single_spec in contour_position.split(";"):
            parsed = safe_int(single_spec)
            if parsed is None or parsed == 0:
                return Err(f"Could not identify contour specification from {contour_position}")
            contour_list += (parsed,)
        return Ok(contour_list)
    parsed = safe_int(contour_position)
    if parsed is not None and parsed != 0:
        return Ok(parsed)
    return Err(f"Could not identify contour specification from {contour_position}")


# --------------------------------------------------------------------------------------------------
# Realized
# --------------------------------------------------------------------------------------------------


def parse_single_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
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

    # Find if this is an alpha feature spec
    for letter in config.greek_alphabet:
        if letter in raw_value:
            return Err("Alpha value notation is not supported for realized features")

    # Contour position
    if "@" in raw_value:
        return Err("Result spec does not support contour position")

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
        if int_value is None:
            pass
        elif int_value in features[feature].values:
            return Ok(int_value)
        elif raw_value in features[feature].values.values():
            key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")


def parse_value(raw_string: str, feature: str, features: FeatureInventory) -> Result[Value, str]:
    """Parse a Value from a raw string.

    Args:
        raw_string: The raw token (e.g. '+', ':2', 'high').
        feature: Full feature name
        features: Feature inventory for type/value resolution.
    """
    # Cleaning the input
    raw_value = raw_string.replace(":", "").replace(" ", "")

    if ">" in raw_value:
        contour = ()
        raw_contour = raw_value.split(">")
        for raw_contour_value in raw_contour:
            match parse_single_value(raw_contour_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    contour = contour + (result,)
        return Ok(contour)

    # Plain feature name – could be unary, could be an error
    if not raw_value:
        if features[feature].kind == "unary":
            return Ok(1)
        else:
            return Err(f"Could not identify value for '{feature}' from string '{raw_string}'")

    match parse_single_value(raw_value, feature, features):
        case Err(err):
            return Err(err)
        case Ok(result):
            return Ok(result)


def parse_feature_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[FeatureBundle, list[str]]:
    """Parse a comma-separated feature bundle string  (e.g. '+syll, -cons, height:2').

    Args:
        raw_string: Comma- or semicolon-separated feature specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    raw_features = [t.strip() for t in string.split(",") if t.strip()]

    bundle = FeatureBundle()
    for raw_feature in raw_features:
        # Identify feature name first, then parse value
        match identify_feature(raw_feature, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                feature_name, matched_string = result

        raw_value = raw_string.replace(matched_string, "", 1)
        match parse_value(raw_value, feature_name, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                bundle[feature_name] = result

    if error_list:
        return Err(error_list)

    return Ok(bundle)


# --------------------------------------------------------------------------------------------------
# Pattern
# --------------------------------------------------------------------------------------------------


def parse_single_pattern_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Identify a single value (unary/binary/scalar) in pattern contexts.

    Args:
        raw_value: The value token after stripping the feature name.
        feature: Full feature name.
        features: Feature inventory for type/value resolution.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    # Find if this is an alpha feature spec
    for letter in config.greek_alphabet:
        if letter in raw_value:
            alpha_var = letter
            alpha_var_index = raw_value.index(alpha_var)
            if raw_value[alpha_var_index - 1] == "-":
                alpha_op = AlphaOp.opposite
            elif raw_value[alpha_var_index - 1] == "!":
                alpha_op = AlphaOp.other
            else:
                alpha_op = AlphaOp.same

            return Ok(AlphaRef(alpha_var, alpha_op))

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
        if int_value is None:
            pass
        elif int_value in features[feature].values:
            return Ok(int_value)
        elif raw_value in features[feature].values.values():
            key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")


def parse_pattern_spec(raw_spec: str, features: FeatureInventory) -> Result[PatternSpec, str]:
    """Parse a PatternSpec from a string.

    Accepts strings like '+ nasal', '!+ nasal', 'nasal', 'height:2@initial', 'α high',
    '+syll', '-α syll', '!α tone@final', 'tone: 2>α'.

    Not all accepted strings are valid at runtime, e.g. '-α syll', but that's a job for
    further down the pipeline.

    Args:
        raw_spec: The raw token to parse.
        features: Feature inventory for name/value resolution.
    """
    # Clean input
    raw_spec = raw_spec.replace(" ", "")

    # Identify feature name via greedy longest-first matching
    match identify_feature(raw_spec, features):
        case Ok(result):
            feature, matched_string = result
        case Err(err):
            return Err(err)

    # Stripping the feature name
    raw_value = raw_spec.replace(matched_string, "", 1)
    raw_value = raw_value.replace(":", "")

    # Negation
    negated = False
    if "!" in raw_value:
        for letter in config.greek_alphabet:
            if letter in raw_value:
                if f"!{letter}" in raw_value:
                    negated = False
                else:
                    negated = True
                    raw_value = raw_value.replace("!", "", 1)

    # Contour position
    contour_position: ContourPosition = ContourEdge.any
    if "@" in raw_value:
        match determine_contour_position(raw_value.split("@")[1]):
            case Err(err):
                return Err(err)
            case Ok(contour_position_spec):
                contour_position = contour_position_spec
        raw_value = raw_value.split("@")[0]

    # Plain feature name – could be unary, could be an error
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            value = Wildcard.wildcard

    # No '>' means not a contour
    elif ">" in raw_value:
        values: tuple = ()
        raw_contour_string = raw_value.split(">")
        for raw_atom_value in raw_contour_string:
            match parse_single_pattern_value(raw_atom_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    values += (result,)
        value = make_value(values)

    # Single value
    else:
        match parse_single_pattern_value(raw_value, feature, features):
            case Err(err):
                return Err(err)
            case Ok(single_value):
                value = single_value

    pattern_spec = PatternSpec(value, negated, contour_position)
    match validate_pattern_spec(pattern_spec):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(pattern_spec)


def validate_pattern_spec(pattern: PatternSpec) -> Result[None, list[str]]:
    """Valdidate the pattern spec - stub."""
    if pattern:
        return Ok(None)
    else:
        return Err(["No pattern"])


def parse_pattern_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[PatternBundle, list[str]]:
    """Parse a comma-separated pattern bundle string.

    Args:
        raw_string: Comma- or semicolon-separated feature specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    raw_features = [t.strip() for t in string.split(",") if t.strip()]

    bundle = PatternBundle()
    for raw_spec in raw_features:
        match identify_feature(raw_spec, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                feature_name, _ = result
        match parse_pattern_spec(raw_spec, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                bundle[feature_name] = result

    if error_list:
        return Err(error_list)

    return Ok(bundle)


# --------------------------------------------------------------------------------------------------
# Pattern
# --------------------------------------------------------------------------------------------------


def parse_single_result_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Identify a single value (unary/binary/scalar) in result contexts.

    Args:
        raw_value: The value token after stripping the feature name.
        feature: Full feature name.
        features: Feature inventory for type/value resolution.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    # Find if this is an alpha feature spec
    for letter in config.greek_alphabet:
        if letter in raw_value:
            alpha_var = letter
            alpha_var_index = raw_value.index(alpha_var)
            if raw_value[alpha_var_index - 1] == "-":
                alpha_op = AlphaOp.opposite
            elif raw_value[alpha_var_index - 1] == "!":
                return Err("Result spec does not support 'other' alpha notation")
            else:
                alpha_op = AlphaOp.same

            return Ok(AlphaRef(alpha_var, alpha_op))

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
        if int_value is None:
            pass
        elif int_value in features[feature].values:
            return Ok(int_value)
        elif raw_value in features[feature].values.values():
            key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")


def parse_result_spec(raw_spec: str, features: FeatureInventory) -> Result[ResultSpec, str]:
    """Parse a ResultSpec from a string.

    Args:
        raw_spec: The raw token to parse.
        features: Feature inventory for name/value resolution.
    """
    # Clean input
    raw_spec = raw_spec.replace(" ", "")

    # Identify feature name via greedy longest-first matching
    match identify_feature(raw_spec, features):
        case Ok(result):
            feature, matched_string = result
        case Err(err):
            return Err(err)

    # Stripping the feature name
    raw_value = raw_spec.replace(matched_string, "", 1)
    raw_value = raw_value.replace(":", "")

    # Negation
    if "!" in raw_value:
        return Err("Result spec does not support negation")

    # Contour position
    if "@" in raw_value:
        return Err("Result spec does not support contour position")

    # Plain feature name – could be unary, could be an error
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            return Err(f"Could not identify value for '{feature}' from string '{raw_spec}'")

    # No '>' means not a contour
    elif ">" in raw_value:
        values: tuple = ()
        raw_contour_string = raw_value.split(">")
        for raw_atom_value in raw_contour_string:
            match parse_single_result_value(raw_atom_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    values += (result,)
        value = make_value(values)

    # Single value
    else:
        match parse_single_result_value(raw_value, feature, features):
            case Err(err):
                return Err(err)
            case Ok(single_value):
                value = single_value

    result_spec = ResultSpec(value)
    match validate_result_spec(result_spec):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(result_spec)


def validate_result_spec(pattern: ResultSpec) -> Result[None, list[str]]:
    """Valdidate the result spec - stub."""
    if pattern:
        return Ok(None)
    else:
        return Err(["No pattern"])
