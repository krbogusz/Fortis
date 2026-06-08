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

        Alpha variable resolution:
        - If alpha_var is unbound in bindings, bind it to the segment value and succeed.
        - If alpha_var is already bound, compare per alpha_op (same/opposite/other).
        """
        # Alpha variable resolution
        if self.alpha_var is not None:
            if bindings is None:
                # No bindings context — alpha always matches (permissive)
                return not self.negated

            segment_atoms: list[SingleValue] = (
                segment_value.value if isinstance(segment_value.value, list) else [segment_value.value]
            )

            if self.alpha_var not in bindings.alpha:
                # First occurrence: bind the variable
                bound_value = segment_atoms[0] if len(segment_atoms) == 1 else tuple(segment_atoms)
                bindings.alpha[self.alpha_var] = bound_value
                return not self.negated

            # Subsequent occurrence: compare per alpha_op
            bound = bindings.alpha[self.alpha_var]
            bound_atoms: list[SingleValue] = [bound] if not isinstance(bound, tuple) else list(bound)

            match self.alpha_op:
                case AlphaOp.same:
                    match = segment_atoms == bound_atoms
                case AlphaOp.opposite:
                    # For binary features, opposite means different value
                    match = segment_atoms != bound_atoms
                case AlphaOp.other:
                    # "Other" means any different value
                    match = segment_atoms != bound_atoms
                case _:
                    match = segment_atoms == bound_atoms

            return (not match) if self.negated else match

        pattern_atoms: list[SingleValue] = self.value if isinstance(self.value, list) else [self.value]
        segment_atoms = (
            segment_value.value if isinstance(segment_value.value, list) else [segment_value.value]
        )

        # Simple value comparison
        match = pattern_atoms == segment_atoms

        return (not match) if self.negated else match