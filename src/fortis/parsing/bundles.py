"""Bundle and value parsing — concrete and pattern material from strings."""

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.models.bundles import FeatureBundle, PatternBundle, ResultBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import (
    AlphaOp,
    AlphaRef,
    ContourEdge,
    ContourPosition,
    Limb,
    Value,
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
        contour_list: tuple[int, ...] = ()
        for single_spec in contour_position.split(";"):
            parsed = safe_int(single_spec)
            if parsed is None:
                return Err(f"Could not identify contour specification from '{contour_position}'")
            elif parsed < 1:
                return Err(f"Contour position cannot be smaller than 1: '{contour_position}'")
            contour_list += (parsed,)
        return Ok(contour_list)
    parsed = safe_int(contour_position)
    if parsed is None:
        return Err(f"Could not identify contour specification from '{contour_position}'")
    if parsed < 0:
        return Err(f"Contour position cannot be smaller than 1: '{contour_position}'")
    return Ok(parsed)


def parse_kind_value(raw_value: str, feature: str, features: FeatureInventory) -> Result[Limb, str]:
    """Dispatch value parsing by feature kind (unary / binary / scalar).

    Shared across all three contexts — only the kind-dispatch logic,
    no alpha or context-dependent checks.
    """
    if features[feature].kind == "unary":
        if raw_value in config.value_symbols.present:
            return Ok(1)
        if raw_value in ("0", "-"):
            return Err(f"Unary features don't support 'absent' values like '{raw_value}'")
    elif features[feature].kind == "binary":
        if raw_value in config.value_symbols.present:
            return Ok(1)
        elif raw_value in config.value_symbols.absent:
            return Ok(0)
    elif features[feature].kind == "scalar":
        int_value = safe_int(raw_value)
        if int_value is not None and int_value in features[feature].values:
            return Ok(int_value)
        if raw_value in features[feature].values.values():
            key = next((k for k, v in features[feature].values.items() if v == raw_value), None)
            if key is not None:
                return Ok(key)

    return Err(f"Could not identify value for '{feature}' from string '{raw_value}'")


# --------------------------------------------------------------------------------------------------
# Realized (feature) parsing
# --------------------------------------------------------------------------------------------------


def parse_feature_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[FeatureBundle, list[str]]:
    """Parse a comma-separated pattern bundle string.

    Args:
        raw_string: Comma- or semicolon-separated feature specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    raw_features = [t.strip() for t in string.split(",") if t.strip()]

    bundle = FeatureBundle()
    for raw_spec in raw_features:
        match parse_feature_spec(raw_spec, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                bundle[result.feature] = result

    if error_list:
        return Err(error_list)

    return Ok(bundle)


def parse_feature_spec(
    raw_spec: str, features: FeatureInventory, feature: str | None = None
) -> Result[FeatureSpec, str]:
    """Parse a FeatureSpec from a string.

    Args:
        raw_spec: The raw token to parse (may include feature name, or just value).
        features: Feature inventory for name/value resolution.
        feature: Optional feature name. When provided, raw_spec is treated as
            just the value part (feature identification is skipped).
    """
    # Clean input
    raw_spec = raw_spec.replace(" ", "")

    if feature is None:
        # Identify feature name via greedy longest-first matching
        match identify_feature(raw_spec, features):
            case Ok(result):
                feature, matched_string = result
            case Err(err):
                return Err(f"Could not identify feature spec from string '{raw_spec}'")

        # Strip the matched feature name
        raw_value = raw_spec.replace(matched_string, "", 1)
        raw_value = raw_value.replace(":", "")
    else:
        # Feature name provided — validate it exists in the inventory
        if feature not in features:
            return Err(f"Unknown feature '{feature}'")
        # raw_spec is the value part; strip leading colon if present
        raw_value = raw_spec
        if raw_value.startswith(":"):
            raw_value = raw_value[1:]

    # Plain feature name – unary defaults to present; non-unary defaults to "any"
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            value = "any"
        feature_spec = FeatureSpec(feature, value)
        match validate_feature_spec(feature_spec):
            case Err(err):
                return Err("\n".join(err))
            case Ok():
                return Ok(feature_spec)

    # Negation
    if "!" in raw_value:
        return Err("Realized feature specifications don't support negation")

    # Contour position
    if "@" in raw_value:
        return Err("Realized feature specifications don't support contour positions")

    # Contour
    if ">" in raw_value:
        contour_limbs: list[Limb] = []
        raw_contour_string = raw_value.split(">")
        for raw_limb_value in raw_contour_string:
            match parse_feature_value(raw_limb_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    contour_limbs.append(result)
        value = make_value(tuple(contour_limbs))

    # Single value
    else:
        match parse_feature_value(raw_value, feature, features):
            case Err(err):
                return Err(err)
            case Ok(single_value):
                value = single_value

    feature_spec = FeatureSpec(feature, value)
    match validate_feature_spec(feature_spec):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(feature_spec)


def validate_feature_spec(feature_spec: FeatureSpec) -> Result[None, list[str]]:
    """Validate the feature spec."""
    return Ok(None)


def parse_feature_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Parse a single value in realized (feature) context.

    Handles unspecified symbols and unary/binary/scalar kind dispatch.
    Rejects alpha references and contour positions.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    # Alpha references are not allowed in realized context
    for letter in config.greek_alphabet:
        if letter in raw_value:
            return Err("Alpha value notation is not supported for realized features")

    # Contour positions are not allowed in realized context
    if "@" in raw_value:
        return Err("Realized feature specifications don't support contour positions")

    return parse_kind_value(raw_value, feature, features)


# --------------------------------------------------------------------------------------------------
# Pattern parsing
# --------------------------------------------------------------------------------------------------


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
        match parse_pattern_spec(raw_spec, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                bundle[result.feature] = result

    if error_list:
        return Err(error_list)

    return Ok(bundle)


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

    # Plain feature name – unary defaults to present; others default to "any"
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            value = "any"
        pattern_spec = PatternSpec(feature, value, negated=False, contour_position=ContourEdge.any)
        match validate_pattern_spec(pattern_spec):
            case Err(err):
                return Err("\n".join(err))
            case Ok():
                return Ok(pattern_spec)

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
    contour_position_assigned = False
    contour_position: ContourPosition = ContourEdge.any
    if "@" in raw_value:
        match determine_contour_position(raw_value.split("@")[1]):
            case Err(err):
                return Err(err)
            case Ok(result):
                contour_position = result
                contour_position_assigned = True
        raw_value = raw_value.split("@")[0]

    # No '>' means not a contour
    if ">" in raw_value:
        if not contour_position_assigned:
            contour_position = ContourEdge.all
        contour_limbs: list[Limb] = []
        raw_contour_string = raw_value.split(">")
        for raw_atom_value in raw_contour_string:
            match parse_pattern_value(raw_atom_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    contour_limbs.append(result)
        value = make_value(tuple(contour_limbs))

    # Single value
    else:
        match parse_pattern_value(raw_value, feature, features):
            case Err(err):
                return Err(err)
            case Ok(single_value):
                value = single_value

    pattern_spec = PatternSpec(feature, value, negated, contour_position)
    match validate_pattern_spec(pattern_spec):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(pattern_spec)


def validate_pattern_spec(pattern_spec: PatternSpec) -> Result[None, list[str]]:
    """Validate the pattern spec — stub."""
    error_list = []
    if isinstance(pattern_spec.value, tuple):
        if isinstance(pattern_spec.contour_position, int):
            error_list.append(
                f"Contour position for a contour must be a list or an edge: '{pattern_spec}'"
            )
        if isinstance(pattern_spec.contour_position, tuple):
            if len(pattern_spec.value) != len(pattern_spec.contour_position):
                error_list.append(
                    f"Contour position and a contour must be the same length: '{pattern_spec}'"
                )
            for index, position in enumerate(pattern_spec.contour_position):
                if index > 0:
                    if position - pattern_spec.contour_position[index - 1] != 1:
                        error_list.append(f"Contour positions must be contiguous: '{pattern_spec}'")
    if error_list:
        return Err(error_list)
    return Ok(None)


def parse_pattern_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Parse a single value in pattern context.

    Handles unspecified symbols, full alpha support (same/opposite/other),
    and unary/binary/scalar kind dispatch.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    # Alpha references — pattern context supports same/opposite/other
    for letter in config.greek_alphabet:
        if letter in raw_value:
            alpha_var = letter
            alpha_var_index = raw_value.index(alpha_var)
            if alpha_var_index > 0 and raw_value[alpha_var_index - 1] == "-":
                alpha_op = AlphaOp.opposite
            elif alpha_var_index > 0 and raw_value[alpha_var_index - 1] == "!":
                alpha_op = AlphaOp.other
            else:
                alpha_op = AlphaOp.same
            return Ok(AlphaRef(alpha_var, alpha_op))

    return parse_kind_value(raw_value, feature, features)


# --------------------------------------------------------------------------------------------------
# Result parsing
# --------------------------------------------------------------------------------------------------


def parse_result_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[ResultBundle, list[str]]:
    """Parse a comma- or semicolon-separated result bundle string.

    Args:
        raw_string: Comma- or semicolon-separated feature specs.
        features: Feature inventory for name/value resolution.
    """
    error_list = []
    string = raw_string.replace(";", ",")
    raw_features = [t.strip() for t in string.split(",") if t.strip()]

    bundle = ResultBundle()
    for raw_spec in raw_features:
        match parse_result_spec(raw_spec, features):
            case Err(err):
                error_list.append(err)
                continue
            case Ok(result):
                bundle[result.feature] = result

    if error_list:
        return Err(error_list)

    return Ok(bundle)


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

    # Plain feature name – unary defaults to present; others require a value
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            return Err(f"Could not identify value for '{feature}' from string '{raw_spec}'")

    # Contour
    elif ">" in raw_value:
        values: list[Limb] = []
        raw_contour_string = raw_value.split(">")
        for raw_limb_value in raw_contour_string:
            match parse_result_value(raw_limb_value, feature, features):
                case Err(err):
                    return Err(err)
                case Ok(result):
                    values.append(result)
        value = make_value(tuple(values))

    # Single value
    else:
        match parse_result_value(raw_value, feature, features):
            case Err(err):
                return Err(err)
            case Ok(single_value):
                value = single_value

    result_spec = ResultSpec(feature, value)
    match validate_result_spec(result_spec):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(result_spec)


def validate_result_spec(pattern: ResultSpec) -> Result[None, list[str]]:
    """Validate the result spec — stub."""
    _ = pattern  # TODO: implement real validation
    return Ok(None)


def parse_result_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Parse a single value in result context.

    Handles unspecified symbols, alpha same/opposite only (no 'other'),
    and unary/binary/scalar kind dispatch.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    # Alpha references — result context supports same/opposite only
    for letter in config.greek_alphabet:
        if letter in raw_value:
            alpha_var = letter
            alpha_var_index = raw_value.index(alpha_var)
            if alpha_var_index > 0 and raw_value[alpha_var_index - 1] == "-":
                alpha_op = AlphaOp.opposite
            elif alpha_var_index > 0 and raw_value[alpha_var_index - 1] == "!":
                return Err("Result spec does not support 'other' alpha notation")
            else:
                alpha_op = AlphaOp.same
            return Ok(AlphaRef(alpha_var, alpha_op))

    return parse_kind_value(raw_value, feature, features)
