from dataclasses import dataclass

from src.fortis.models.values import ContourEdge, ContourPosition, Value


@dataclass
class FeatureSpec:
    """A realized feature specification."""

    feature: str
    value: Value


@dataclass
class PatternSpec:
    """A value with a pattern specification.

    ``condition_label`` is set when the spec is a conditional feature
    ``[<n: F>]``: the paired result feature applies only when this condition
    holds. ``None`` for ordinary (unconditional) specs.
    """

    feature: str
    value: Value
    negated: bool = False
    contour_position: ContourPosition = ContourEdge.any
    condition_label: int | None = None


@dataclass
class ResultSpec:
    """A value with a result specification.

    ``condition_label`` is set when the spec is a conditional feature
    ``[<n: F>]``: this feature is applied only when the like-labelled
    condition holds. ``None`` for ordinary (unconditional) specs.
    """

    feature: str
    value: Value | None  # None means 'unlink'
    condition_label: int | None = None
