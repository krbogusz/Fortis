"""The segmental-tier element: a feature bundle with a stable identity."""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.models.bundles import FeatureBundle


@dataclass(frozen=True)
class Segment:
    """One position on the segmental tier: a bundle plus a stable ``id``.

    The id survives the splicing the applier does to the segment list, so a later
    autosegmental association line can point at a segment that keeps its identity even
    as neighbours are inserted or deleted around it. In Phase 0 nothing reads the id —
    it is inert scaffolding.
    """

    bundle: FeatureBundle
    id: int
