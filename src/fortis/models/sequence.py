from collections import UserList

from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_inventory import FeatureInventory
from src.fortis.models.tiers import Tier
from src.fortis.models.values import present_value


class Sequence(UserList[FeatureBundle]):
    """An ordered sequence of feature bundles (segments)."""

    def present(self, inventory: FeatureInventory) -> str:
        """Format all bundles side-by-side with aligned features.

        Features that are present in any bundle get a row. Features absent
        from a specific bundle appear as empty rows within that bundle's column.
        A ``---`` row separates segment and syllable features.

        Args:
            inventory: Feature inventory for name/type/value lookups.
        """
        if not self.data:
            return ""

        # Build row template from inventory order
        rows: list[tuple[str, str | None]] = []  # (feature_name or "", separator_label or None)
        has_syllable = False
        for feature_name in inventory:
            ft_def = inventory[feature_name]
            if ft_def.tier == Tier.syllable and not has_syllable:
                rows.append(("", "---"))
                has_syllable = True
            if any(feature_name in bundle for bundle in self.data):
                rows.append((feature_name, None))

        # Format each feature value per bundle
        content: list[list[str]] = []  # content[row][col]
        is_separator: list[bool] = []
        for feature_name, separator in rows:
            is_separator.append(separator is not None)
            if separator:
                row = []
                for bundle in self.data:
                    has_syl = any(inventory[fn].tier == Tier.syllable for fn in bundle if fn in inventory)
                    row.append(separator if has_syl else "")
                content.append(row)
            else:
                ft_def = inventory[feature_name]
                short = ft_def.short
                row = []
                for bundle in self.data:
                    if feature_name not in bundle:
                        row.append("")
                    else:
                        spec = bundle[feature_name]
                        row.append(_format_feature(short, ft_def.type, spec.value))
                content.append(row)

        if not content:
            return ""

        # Calculate column widths
        col_widths = [max(len(content[r][c]) for r in range(len(content))) for c in range(len(self.data))]

        # For each column, find the first and last non-empty content row
        col_ranges: list[tuple[int, int]] = []
        for c in range(len(self.data)):
            non_empty = [r for r in range(len(content)) if content[r][c]]
            col_ranges.append((non_empty[0], non_empty[-1]))

        result_lines: list[str] = []
        for r in range(len(content)):
            cells = []
            for c in range(len(self.data)):
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


def _format_feature(short: str, feature_type: str, value: int | list[int | None] | None) -> str:
    """Format a single feature as a display string."""
    if feature_type == "unary":
        if isinstance(value, list):
            vals = ">".join(present_value(v) for v in value)
            return f"{short}: {vals}"
        return short
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
