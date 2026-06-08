"""Concrete segments and sequences."""

from dataclasses import dataclass

from src.fortis.models.values import Value


@dataclass(frozen=True)
class FeatureBundle:
    """Concrete feature data: feature -> value (simple or contour).

    Back this with an immutable/hashable map if you rely on ``Segment``
    hashability.
    """

    values: dict[str, Value]


@dataclass(frozen=True)
class Segment:
    """A segment is exactly its features; no source spelling is retained."""

    features: FeatureBundle


@dataclass(frozen=True)
class Sequence:
    """An ordered collection of segments."""

    segments: tuple[Segment, ...]
