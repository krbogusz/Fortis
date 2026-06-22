"""Presentation functions for Fortis model objects.

All display/formatting logic lives here so that model classes stay
focused on data and matching.  Every function takes the model object
as its first argument, keeping presentation separate from identity.
"""

from src.fortis.general.utils import is_combining
from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import AlphaOp, AlphaRef, ContourEdge

# ---------------------------------------------------------------------------
# Primitive formatters
# ---------------------------------------------------------------------------


def present_symbol(symbol: str) -> str:
    """Return a str with the ◌ if the first character is combining, otherwise return character."""
    if len(symbol) == 1 and is_combining(symbol):
        return "◌" + symbol
    else:
        return symbol


def present_value(value: int | None | str) -> str:
    """Format a single feature value as a display string.

    Maps: ``None`` → ``"∅"``, ``1`` → ``"+"``, ``0`` → ``"-"``,
    alpha variables (str) pass through as-is, otherwise ``str(value)``.
    """
    if isinstance(value, str):
        return value
    if value is None:
        return "∅"
    if value == 1:
        return "+"
    if value == 0:
        return "-"
    return str(value)


def present_alpha_ref(alpha: AlphaRef) -> str:
    """Format an alpha reference as a display string."""
    prefix = ""
    match alpha.op:
        case AlphaOp.same:
            prefix = ""
        case AlphaOp.opposite:
            prefix = "-"
        case AlphaOp.other:
            prefix = "!"
    return f"{prefix}{alpha.var}"


def present_contour_position(pos: int | tuple[int, ...] | ContourEdge) -> str:
    """Format a contour position as a display string."""
    if isinstance(pos, ContourEdge):
        return f"@{pos.value}"
    if isinstance(pos, tuple):
        return "@" + ";".join(str(p) for p in pos)
    return f"@{pos}"


def present_spec(spec: FeatureSpec | PatternSpec | ResultSpec) -> str:
    """Present a spec as a clean string."""
    # Format the value part
    value_str: str
    if isinstance(spec.value, AlphaRef):
        value_str = present_alpha_ref(spec.value)
    elif isinstance(spec.value, tuple):
        value_str = ">".join(
            present_alpha_ref(v) if isinstance(v, AlphaRef) else present_value(v)
            for v in spec.value
        )
    else:
        value_str = present_value(spec.value)

    # Build the full string based on spec type
    if isinstance(spec, FeatureSpec):
        if spec.value is None:
            return f"{spec.feature}:∅"
        if spec.value == 1 and value_str == "+":
            return f"+{spec.feature}"
        return f"{spec.feature}:{value_str}"

    if isinstance(spec, PatternSpec):
        prefix = "!" if spec.negated else ""
        suffix = ""
        if spec.contour_position != ContourEdge.any:
            suffix = present_contour_position(spec.contour_position)
        if spec.value == 1 and value_str == "+" and not spec.negated:
            return f"+{spec.feature}{suffix}"
        if spec.value == 0 and value_str == "-" and not spec.negated:
            return f"-{spec.feature}{suffix}"
        return f"{prefix}{spec.feature}:{value_str}{suffix}"

    if isinstance(spec, ResultSpec):
        if spec.value is None:
            return f"{spec.feature}:∅"
        if spec.value == 1 and value_str == "+":
            return f"+{spec.feature}"
        return f"{spec.feature}:{value_str}"

    return str(spec)
