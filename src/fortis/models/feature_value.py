from dataclasses import dataclass

from src.fortis.models.values import ContourValue, SingleValue, Value


@dataclass
class FeatureValue:
    """A value in a realized feature specification.

    Holds a single atomic value (int or None) or a contour (list of values).
    No position or negation — those belong in PatternSpec.
    """

    value: Value

    def __repr__(self) -> str:
        """Repr."""
        if self.value is None:
            return "∅"
        elif isinstance(self.value, list):
            return ">".join(str(v) if v is not None else "∅" for v in self.value)
        else:
            return str(self.value)

    def form_contour_with(self, other: FeatureValue) -> FeatureValue:
        """Form a contour by appending *other*'s value onto *self*'s."""
        self_values: list[SingleValue] = self.value if isinstance(self.value, list) else [self.value]
        other_values: list[SingleValue] = other.value if isinstance(other.value, list) else [other.value]
        contour: ContourValue = self_values + other_values
        return FeatureValue(contour)
