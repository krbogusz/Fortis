"""A word form: the segmental tier, plus (later) autosegmental tiers.

In Phase 0 ``tiers`` is always empty and a ``Form`` behaves exactly as the bare
``list[FeatureBundle]`` it replaces — it just carries each segment's stable identity
alongside the bundle. The autosegmental ``Tier``/``Autoseg`` types arrive in Phase 1.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.segment import Segment


@dataclass
class Form:
    """The segmental tier (``segments``) with optional autosegmental ``tiers``.

    ``segments`` is spliced in place by the applier; out-of-span ``Segment`` objects
    keep their identity across a rewrite. ``fresh_id`` mints ids unique within the form
    for newly inserted segments.
    """

    segments: list[Segment]
    tiers: dict[str, AutosegmentalTier] = field(default_factory=dict)
    _next_id: int = field(default=0, compare=False, repr=False)

    def __post_init__(self) -> None:
        """Seed the id counter past any ids the initial segments already carry."""
        used = max((segment.id for segment in self.segments), default=-1) + 1
        self._next_id = max(self._next_id, used)

    @classmethod
    def from_bundles(cls, bundles: list[FeatureBundle]) -> Form:
        """Wrap a plain bundle sequence, assigning sequential ids (the construction point)."""
        return cls([Segment(bundle, index) for index, bundle in enumerate(bundles)])

    def fresh_id(self) -> int:
        """A segment id not used elsewhere in this form."""
        new = self._next_id
        self._next_id += 1
        return new

    def bundles(self) -> list[FeatureBundle]:
        """The segmental tier as a plain bundle list (the matcher/syllabifier/applier view)."""
        return [segment.bundle for segment in self.segments]

    def copy(self) -> Form:
        """A shallow copy safe to splice without disturbing the original."""
        return Form(list(self.segments), dict(self.tiers), self._next_id)
