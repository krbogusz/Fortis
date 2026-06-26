"""The declaration of an autosegmental tier (loaded from ``tiers.toml``)."""
from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass

from src.fortis.models.bundles import PatternBundle


@dataclass(frozen=True)
class TierDeclaration:
    """A declared autosegmental tier: the features it carries, its anchor, and its policy.

    ``carries`` are the feature names that live on this tier rather than in the segment
    bundle. ``anchor`` is the tone-bearing-unit predicate (e.g. ``+syllabic``). ``melody``
    marks a lexical melody that universal association maps onto anchors (tone), as opposed
    to a rule-placed tier (stress). ``ocp`` merges adjacent identical autosegments;
    ``stray_erase`` deletes a floating autosegment at the surface unless it docks.
    ``stability`` (``"left"`` or ``"right"``) is the direction a melody autosegment stranded
    by deletion carries to — the neighbour it re-docks onto.
    """

    name: str
    carries: tuple[str, ...]
    anchor: PatternBundle
    melody: bool
    ocp: bool = True
    stray_erase: bool = True
    stability: str = "left"


class TierInventory(UserDict[str, TierDeclaration]):
    """Declared autosegmental tiers, keyed by name. Empty ⇒ no tiers run (the gate)."""
