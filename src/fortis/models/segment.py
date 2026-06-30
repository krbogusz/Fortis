"""The segmental-tier element: a feature bundle with a stable identity."""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.models.bundles import FeatureBundle


@dataclass(frozen=True)
class Segment:
    """One position on the segmental tier: a bundle plus a stable ``id``.

    The id survives the splicing the applier does to the segment list, so an
    autosegmental association line can point at a segment that keeps its identity even
    as neighbours are inserted or deleted around it: a tier link pairs an autoseg id
    with one of these segment ids, and a deleted anchor's id simply leaves the live
    set, stranding its autoseg as floating.
    """

    bundle: FeatureBundle
    id: int
