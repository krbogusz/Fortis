"""Autosegmental tier representation: autosegments and their association links.

A tier holds its autosegments and a set of association lines to segment anchors. The
links are by *id* (an autoseg id paired with a ``Form.segments[].id``), so they survive
the applier's splicing of the segment list: a deleted anchor's id simply leaves the
live set, stranding its autoseg as floating — which is where tonal stability comes from.

Many-to-one association (one autoseg, several anchors) is spreading; one-to-many (several
autosegs, one anchor) is a contour tone; an autoseg with no link is floating. An empty
tier is inert, so a project that declares none behaves exactly as before.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src.fortis.models.bundles import FeatureBundle


@dataclass(frozen=True)
class Autoseg:
    """One autosegment: its featural content plus a stable identity.

    The content is a bundle (e.g. ``{tone: H}``). The id is what association links
    reference, so it must stay stable as the tier is edited.
    """

    bundle: FeatureBundle
    id: int


@dataclass
class AutosegmentalTier:
    """One tier's autosegments and the association lines to segment anchors.

    ``links`` pairs ``(autoseg_id, segment_id)``. An autoseg id absent from every link
    is floating; a segment id shared by several links carries a contour.

    ``float_hosts`` records a floating autoseg's *position* as adjacency to a segment —
    ``autoseg_id -> (segment_id, "before" | "after")`` — so a positioned floating tone (a
    lexical/grammatical melody, e.g. a suffixal H) docks where it sits rather than onto any
    toneless anchor. Keyed by id, so it survives the splice exactly like ``links``.
    """

    autosegs: list[Autoseg] = field(default_factory=list)
    links: set[tuple[int, int]] = field(default_factory=set)
    float_hosts: dict[int, tuple[int, str]] = field(default_factory=dict)
