from dataclasses import dataclass

from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import (
    DiacriticInventory,
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    WordInventory,
)
from src.fortis.models.rules import RuleInventory


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
