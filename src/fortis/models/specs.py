from dataclasses import dataclass

from src.fortis.models.values import ContourEdge, ContourPosition, Value


@dataclass
class FeatureSpec:
    """A realized feature specification."""

    feature: str
    value: Value


@dataclass
class PatternSpec:
    """A value with a pattern specification."""

    feature: str
    value: Value
    negated: bool = False
    contour_position: ContourPosition = ContourEdge.any


@dataclass
class ResultSpec:
    """A value with a result specification."""

    feature: str
    value: Value | None  # None means 'unlink'
