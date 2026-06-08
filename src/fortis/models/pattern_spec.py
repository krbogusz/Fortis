from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.fortis.models.elements import AlphaOp
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.values import ContourPosition, SingleValue, Value
from src.fortis.result import Ok, Result

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
        contour_position: The contour position (any, initial, final, all, or specific).
        alpha_var: Greek letter variable name (e.g. "α", "β") if this spec
            binds or recalls an alpha variable; None for concrete values.
        alpha_op: The alpha operation (same/opposite/other) when alpha_var is set.
    """

    value: Value
    negated: bool = False
    contour_position: ContourPosition = "any"
    alpha_var: str | None = None
    alpha_op: AlphaOp | None = None

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