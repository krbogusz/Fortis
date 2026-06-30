"""Bundle and value parsing — concrete and pattern material from strings."""
from __future__ import annotations

from collections import UserDict
from collections.abc import Callable
from typing import Protocol

from src.fortis.config import config
from src.fortis.general.utils import safe_int
from src.fortis.models.bundles import FeatureBundle, PatternBundle, ResultBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import (
    AlphaOp,
    AlphaRef,
    AutosegBind,
    AutosegRecall,
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
    # Search only the part before any ':value'. The feature name lives there (possibly
    # wrapped in a sign or alpha marker, with the value adjacent, e.g. `+nasal`,
    # `syllabic-`, `1glap`, `α fr`), so substring matching still finds it — but a value
    # *label* after the colon may itself be a feature name (`tone: high`), and matching
    # the whole string would mistake that label for the feature.
    lhs = raw_string.split(":", 1)[0]
    for name in features.names_by_length:
        if name in lhs:
            return Ok((name, name))
    for short_name in features.short_names_by_length:
        if short_name in lhs:
            return Ok((features.short_to_long_name[short_name], short_name))

    return Err(f"No feature could be identified from '{raw_string}'")


def _scalar_label_requires_colon(
    feature: str, raw_value: str, had_colon: bool, features: FeatureInventory
) -> str | None:
    """A scalar feature's value *label* is only legible after a colon.

    A bare label (`high`, `low`) collides with feature names of the same spelling
    (the vowel-height features), so for a scalar feature a label must be introduced by
    a colon — ``tone: high``, not ``high tone``. Numbers (``tone3``) and alpha markers
    (``α tone``) are unambiguous and need no colon. Returns an error message when the
    rule is violated, else ``None``. Unary and binary features are unaffected.
    """
    if had_colon or features[feature].kind != "scalar":
        return None
    labels = set(features[feature].values.values())
    if any(limb in labels for limb in raw_value.split(">")):
        return (
            f"Scalar feature '{feature}': a value label must follow a colon "
            f"(write '{feature}: {raw_value}', not a bare label)"
        )
    return None


def split_conditional(raw_spec: str) -> Result[tuple[int, str], str]:
    """Split a conditional-feature wrapper ``<n: F>`` into ``(label, inner)``.

    ``raw_spec`` is assumed to start with ``<`` (whitespace already stripped).
    The label is the integer before the first colon; the inner spec string is
    returned for the caller to parse normally. Because only the first colon is
    consumed and only one trailing ``>`` is stripped, a contour inner such as
    ``<1: tone: 1>2>`` splits correctly into ``(1, 'tone:1>2')``.

    Args:
        raw_spec: A whitespace-free spec string beginning with ``<``.
    """
    if not raw_spec.endswith(">"):
        return Err(f"Malformed conditional feature (missing closing '>'): '{raw_spec}'")
    label_str, sep, inner = raw_spec[1:-1].partition(":")
    if not sep:
        return Err(f"Conditional feature is missing its ':' label separator: '{raw_spec}'")
    label = safe_int(label_str)
    if label is None:
        return Err(f"Conditional feature label must be an integer: '{raw_spec}'")
    if not inner:
        return Err(f"Conditional feature has no inner spec: '{raw_spec}'")
    return Ok((label, inner))


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
    if parsed < 1:
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


class _HasFeature(Protocol):
    feature: str


def _parse_bundle[S: _HasFeature, B: UserDict](
    raw_string: str,
    features: FeatureInventory,
    factory: Callable[[], B],
    parse_spec: Callable[[str, FeatureInventory], Result[S, str]],
) -> Result[B, list[str]]:
    """Shared core for the three bundle parsers: comma-split, parse each spec, collect errors.

    ``;`` is reserved for contour-position index lists and does not separate features. *factory*
    fixes the bundle type and *parse_spec* the spec type (realized / pattern / result).
    """
    error_list: list[str] = []
    bundle = factory()
    for raw_spec in (t.strip() for t in raw_string.split(",") if t.strip()):
        match parse_spec(raw_spec, features):
            case Err(err):
                error_list.append(err)
            case Ok(result):
                bundle[result.feature] = result
    if error_list:
        return Err(error_list)
    return Ok(bundle)


def parse_feature_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[FeatureBundle, list[str]]:
    """Parse a comma-separated realized feature bundle string."""
    return _parse_bundle(raw_string, features, FeatureBundle, parse_feature_spec)


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
        had_colon = ":" in raw_spec
    else:
        # Feature name provided — validate it exists in the inventory
        if feature not in features:
            return Err(f"Unknown feature '{feature}'")
        # raw_spec is the value part; strip leading colon if present
        raw_value = raw_spec
        if raw_value.startswith(":"):
            raw_value = raw_value[1:]
        had_colon = True  # feature already identified — no ambiguity to resolve

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

    label_error = _scalar_label_requires_colon(feature, raw_value, had_colon, features)
    if label_error is not None:
        return Err(label_error)

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
    """Validate a realized (lexicon) feature spec.

    Parsing already rejects negation, alpha, and contour positions in realized
    context. The one remaining reachable-but-invalid state is the bare-feature
    form ``value == "any"`` (Wildcard.present), which is pattern-only — a
    concrete segment must carry an explicit value. Bare unary features are
    unaffected: they resolve to present (1), never "any".
    """
    if feature_spec.value == "any":
        return Err(
            [
                f"Realized feature '{feature_spec.feature}' needs an explicit value; "
                "a bare feature name matches any value and is pattern-only"
            ]
        )
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
    """Parse a comma-separated pattern bundle string."""
    return _parse_bundle(raw_string, features, PatternBundle, parse_pattern_spec)


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

    # Conditional feature '<n: F>' — parse the inner spec normally, tag the label.
    if raw_spec.startswith("<"):
        match split_conditional(raw_spec):
            case Err(err):
                return Err(err)
            case Ok((label, inner)):
                match parse_pattern_spec(inner, features):
                    case Err(err):
                        return Err(err)
                    case Ok(spec):
                        spec.condition_label = label
                        return Ok(spec)

    # Identify feature name via greedy longest-first matching
    match identify_feature(raw_spec, features):
        case Ok(result):
            feature, matched_string = result
        case Err(err):
            return Err(err)

    # Stripping the feature name
    raw_value = raw_spec.replace(matched_string, "", 1)
    raw_value = raw_value.replace(":", "")
    had_colon = ":" in raw_spec

    # Negation — a leading '!' negates the whole spec, UNLESS it immediately
    # precedes a Greek letter, where it is the value-level alpha-other marker
    # ('!α', resolved by parse_pattern_value to AlphaOp.other).
    negated = False
    if raw_value.startswith("!") and not (
        len(raw_value) > 1 and raw_value[1] in config.greek_alphabet
    ):
        negated = True
        raw_value = raw_value[1:]

    # Plain feature name – unary defaults to present; others default to "any"
    if not raw_value:
        if features[feature].kind == "unary":
            value: Value = 1
        else:
            value = "any"
        pattern_spec = PatternSpec(feature, value, negated, contour_position=ContourEdge.any)
        match validate_pattern_spec(pattern_spec, features):
            case Err(err):
                return Err("\n".join(err))
            case Ok():
                return Ok(pattern_spec)

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

    label_error = _scalar_label_requires_colon(feature, raw_value, had_colon, features)
    if label_error is not None:
        return Err(label_error)

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
    match validate_pattern_spec(pattern_spec, features):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(pattern_spec)


def opposite_alpha_on_scalar(
    feature: str, value: Value | None, features: FeatureInventory
) -> str | None:
    """Return an error message if ``value`` uses alpha-opposite on a scalar feature.

    Alpha-opposite (``-α``) means "the other pole", so it is defined for features
    with two poles: **binary** (0 ↔ 1) and **unary** (present 1 ↔ absent none). A
    **scalar** feature has many values and no single opposite, so ``-α`` is invalid
    on it — for a single value or any contour limb. Returns ``None`` when fine.
    """
    if features[feature].kind != "scalar":
        return None
    limbs = value if isinstance(value, tuple) else (value,)
    if any(isinstance(limb, AlphaRef) and limb.op == AlphaOp.opposite for limb in limbs):
        return (
            f"Alpha-opposite ('-α') is not valid for scalar feature '{feature}' "
            "(binary/unary only)"
        )
    return None


def validate_pattern_spec(
    pattern_spec: PatternSpec, features: FeatureInventory
) -> Result[None, list[str]]:
    """Validate an assembled pattern spec.

    Enforces the contour-position invariants that parsing cannot check
    incrementally: a multi-limb contour's positional modifier must be an index
    list (not a single index or bare edge), whose length matches the contour's
    limb count and whose indices are contiguous. Also rejects alpha-opposite
    (``-α``) on scalar features (binary/unary only).
    """
    error_list = []
    message = opposite_alpha_on_scalar(pattern_spec.feature, pattern_spec.value, features)
    if message is not None:
        error_list.append(message)
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


def parse_autoseg_ref(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[AutosegBind | AutosegRecall, str]:
    """Parse a tier-autosegment reference: ``~n=value`` binds, ``~n`` recalls (spread).

    ``~n=value`` binds the autosegment carrying *value* under reference *n*; ``~n`` recalls
    a bound autosegment, so the applier associates the **same** one (spreading it) rather
    than minting a copy. The bind's inner value is parsed in pattern context.
    """
    ref_str, sep, value_str = raw_value[1:].partition("=")
    if not ref_str.isdigit():
        return Err(f"tier reference '{raw_value}' must be ~ followed by a reference number")
    ref = int(ref_str)
    if not sep:
        return Ok(AutosegRecall(ref))
    match parse_kind_value(value_str, feature, features):
        case Err(error):
            return Err(error)
        case Ok(value):
            return Ok(AutosegBind(ref, value))


def parse_pattern_value(
    raw_value: str, feature: str, features: FeatureInventory
) -> Result[Limb, str]:
    """Parse a single value in pattern context.

    Handles unspecified symbols, full alpha support (same/opposite/other),
    and unary/binary/scalar kind dispatch.
    """
    if raw_value in config.value_symbols.unspecified:
        return Ok(None)

    if raw_value.startswith("~"):
        return parse_autoseg_ref(raw_value, feature, features)

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
            return Ok(AlphaRef(alpha_var, alpha_op, unary=features[feature].kind == "unary"))

    return parse_kind_value(raw_value, feature, features)


# --------------------------------------------------------------------------------------------------
# Result parsing
# --------------------------------------------------------------------------------------------------


def parse_result_bundle(
    raw_string: str, features: FeatureInventory
) -> Result[ResultBundle, list[str]]:
    """Parse a comma-separated result bundle string."""
    return _parse_bundle(raw_string, features, ResultBundle, parse_result_spec)


def parse_result_spec(raw_spec: str, features: FeatureInventory) -> Result[ResultSpec, str]:
    """Parse a ResultSpec from a string.

    Args:
        raw_spec: The raw token to parse.
        features: Feature inventory for name/value resolution.
    """
    # Clean input
    raw_spec = raw_spec.replace(" ", "")

    # Conditional feature '<n: F>' — parse the inner spec normally, tag the label.
    if raw_spec.startswith("<"):
        match split_conditional(raw_spec):
            case Err(err):
                return Err(err)
            case Ok((label, inner)):
                match parse_result_spec(inner, features):
                    case Err(err):
                        return Err(err)
                    case Ok(spec):
                        spec.condition_label = label
                        return Ok(spec)

    # Identify feature name via greedy longest-first matching
    match identify_feature(raw_spec, features):
        case Ok(result):
            feature, matched_string = result
        case Err(err):
            return Err(err)

    # Stripping the feature name
    raw_value = raw_spec.replace(matched_string, "", 1)
    raw_value = raw_value.replace(":", "")
    had_colon = ":" in raw_spec

    # Negation — a leading '!' is spec negation, rejected here. A '!' that
    # precedes a Greek letter is the value-level alpha-other marker ('!α');
    # it falls through to parse_result_value, which rejects it with its own
    # ('other' alpha) message.
    if raw_value.startswith("!") and not (
        len(raw_value) > 1 and raw_value[1] in config.greek_alphabet
    ):
        return Err("Result spec does not support negation")

    # Contour position
    if "@" in raw_value:
        return Err("Result spec does not support contour position")

    label_error = _scalar_label_requires_colon(feature, raw_value, had_colon, features)
    if label_error is not None:
        return Err(label_error)

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
    match validate_result_spec(result_spec, features):
        case Err(err):
            return Err("\n".join(err))
        case Ok():
            return Ok(result_spec)


def validate_result_spec(
    result_spec: ResultSpec, features: FeatureInventory
) -> Result[None, list[str]]:
    """Validate an assembled result spec.

    Parsing already rejects negation, alpha-other, and contour positions in
    result position. The remaining spec-level invariant is that alpha-opposite
    (``-α``) is binary/unary only — a scalar feature has no single opposite.
    Cross-position rules (conditional-label pairing with the target, alpha
    binding) are checked in the rule-level validation layer (``rule_validation.py``).
    """
    error_list: list[str] = []
    message = opposite_alpha_on_scalar(result_spec.feature, result_spec.value, features)
    if message is not None:
        error_list.append(message)
    if error_list:
        return Err(error_list)
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

    if raw_value.startswith("~"):
        return parse_autoseg_ref(raw_value, feature, features)

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
            return Ok(AlphaRef(alpha_var, alpha_op, unary=features[feature].kind == "unary"))

    return parse_kind_value(raw_value, feature, features)
