from __future__ import annotations

from enum import StrEnum, auto


class Tier(StrEnum):
    """Phonological tiers (segment, syllable)."""

    segment = auto()
    syllable = auto()
