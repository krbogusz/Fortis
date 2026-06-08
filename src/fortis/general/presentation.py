"""Presentation functions for Fortis model objects.

All display/formatting logic lives here so that model classes stay
focused on data and matching.  Every function takes the model object
as its first argument, keeping presentation separate from identity.
"""

from src.fortis.general.utils import is_combining
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.tier import Tier
from src.fortis.models.values import Value

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


def format_feature(short: str, feature_type: str, value: Value) -> str:
    """Format a single feature as a display string.

    Args:
        short: Short/abbreviated feature name.
        feature_type: ``"unary"``, ``"binary"``, or ``"scalar"``.
        value: The feature value (int, contour, None, or alpha variable).
    """
    if isinstance(value, str):
        # Alpha variable — display the Greek letter
        return f"{short}: {value}"
    if feature_type == "unary":
        if isinstance(value, list):
            vals = ">".join(present_value(v) for v in value)
            return f"{short}: {vals}"
        return f"{short}"
    if feature_type == "binary":
        if isinstance(value, list):
            vals = ">".join(present_value(v) for v in value)
            return f"{short}: {vals}"
        return f"{short}: {present_value(value)}"
    # scalar
    if isinstance(value, list):
        vals = ">".join(present_value(v) for v in value)
        return f"{short}: {vals}"
    return f"{short}: {value if value is not None else '∅'}"


# ---------------------------------------------------------------------------
# FeatureBundle presentation
# ---------------------------------------------------------------------------


def present_bundle(bundle: FeatureBundle, features: FeatureInventory) -> str:
    """Format a feature bundle as a boxed display string.

    Binary/unary features show as ``+name`` or ``-name`` (using short names).
    Scalar features show as ``name: label``.
    Contour values show as ``name: label>label>...``.

    Args:
        bundle: The feature bundle to present.
        features: Feature inventory for name/type/value lookups.
    """
    return "\n".join(present_bundle_lines(bundle, features))


def present_bundle_lines(bundle: FeatureBundle, features: FeatureInventory) -> list[str]:
    """Return the boxed lines for a feature bundle (for side-by-side display).

    Args:
        bundle: The feature bundle to present.
        features: Feature inventory for name/type/value lookups.
    """
    lines: list[str] = []
    has_syllable = False
    for feature_name in features:
        if feature_name not in bundle:
            continue
        spec = bundle[feature_name]
        if spec.value.value is None:
            continue
        ft_def = features[feature_name]
        if ft_def.tier == Tier.syllable and not has_syllable:
            lines.append("---")
            has_syllable = True
        short = ft_def.short
        lines.append(format_feature(short, ft_def.kind, spec.value.value))

    if not lines:
        return ["⎡⎤"]

    width = max(len(line) for line in lines)
    result = [f"⎡{lines[0]:<{width}}⎤"]
    if len(lines) > 1:
        result.extend(f"⎢{line:<{width}}⎥" for line in lines[1:-1])
        result.append(f"⎣{lines[-1]:<{width}}⎦")

    return result


# ---------------------------------------------------------------------------
# Sequence presentation
# ---------------------------------------------------------------------------


def present_sequence(sequence: list[FeatureBundle], features: FeatureInventory) -> str:
    """Format all bundles in a sequence side-by-side with aligned features.

    Features that are present in any bundle get a row. Features absent
    from a specific bundle appear as empty rows within that bundle's column.
    A ``---`` row separates segment and syllable features.

    Args:
        sequence: The sequence of feature bundles to present.
        features: Feature inventory for name/type/value lookups.
    """
    if not sequence:
        return ""

    # Build row template from inventory order
    rows: list[tuple[str, str | None]] = []  # (feature_name or "", separator_label or None)
    has_syllable = False
    for feature_name in features:
        ft_def = features[feature_name]
        if ft_def.tier == Tier.syllable and not has_syllable:
            rows.append(("", "---"))
            has_syllable = True
        if any(feature_name in bundle and bundle[feature_name].value.value is not None for bundle in sequence):
            rows.append((feature_name, None))

    # Format each feature value per bundle
    content: list[list[str]] = []  # content[row][col]
    is_separator: list[bool] = []
    for feature_name, separator in rows:
        is_separator.append(separator is not None)
        if separator:
            row = []
            for bundle in sequence:
                has_syl = any(features[fn].tier == Tier.syllable for fn in bundle if fn in features)
                row.append(separator if has_syl else "")
            content.append(row)
        else:
            ft_def = features[feature_name]
            short = ft_def.short
            row = []
            for bundle in sequence:
                if feature_name not in bundle:
                    row.append("")
                else:
                    spec = bundle[feature_name]
                    if spec.value.value is None:
                        row.append("")
                    else:
                        row.append(format_feature(short, ft_def.kind, spec.value.value))
            content.append(row)

    if not content:
        return ""

    # Calculate column widths
    col_widths = [max(len(content[r][c]) for r in range(len(content))) for c in range(len(sequence))]

    # For each column, find the first and last non-empty content row
    col_ranges: list[tuple[int, int]] = []
    for c in range(len(sequence)):
        non_empty = [r for r in range(len(content)) if content[r][c]]
        col_ranges.append((non_empty[0], non_empty[-1]))

    result_lines: list[str] = []
    for r in range(len(content)):
        cells = []
        for c in range(len(sequence)):
            val = content[r][c]
            padded = f"{val:<{col_widths[c]}}"
            first_row, last_row = col_ranges[c]
            if r < first_row or r > last_row:
                cells.append(" " * (col_widths[c] + 2))
            elif r == first_row:
                cells.append(f"⎡{padded}⎤")
            elif r == last_row:
                cells.append(f"⎣{padded}⎦")
            else:
                cells.append(f"⎢{padded}⎥")
        result_lines.append(" ".join(cells))

    return "\n".join(result_lines)
