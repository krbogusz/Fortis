from __future__ import annotations

from dataclasses import dataclass, field

from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import (
    DiacriticInventory,
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    WordInventory,
)
from src.fortis.models.rules import RuleInventory
from src.fortis.models.settings import Settings
from src.fortis.models.tier_declaration import TierInventory


@dataclass
class Project:
    """The loaded project: every inventory bundled together."""

    features: FeatureInventory
    letters: LetterInventory  # ordered for longest-match tokenisation
    diacritics: DiacriticInventory
    sonorities: SonoritiesInventory
    syllable_parts: SyllablePartsInventory
    words: WordInventory
    rules: RuleInventory  # pre-sorted by (time, file order)
    time: int  # current time
    tiers: TierInventory = field(default_factory=TierInventory)  # autosegmental tiers; {} = none
    settings: Settings = field(default_factory=Settings)  # tunable analysis parameters
