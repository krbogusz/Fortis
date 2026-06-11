from dataclasses import dataclass

from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import (
    DiacriticInventory,
    LetterInventory,
    SonorityInventory,
    SyllablePartsInventory,
    WordInventory,
)
from src.fortis.models.rules import RuleInventory


@dataclass(frozen=True)
class Project:
    """The loaded project: every inventory bundled together."""

    features: FeatureInventory
    letters: LetterInventory  # ordered for longest-match tokenisation
    diacritics: DiacriticInventory
    sonority: SonorityInventory
    syllable_parts: SyllablePartsInventory
    words: WordInventory
    rules: RuleInventory  # pre-sorted by (time, file order); None until rules loader exists
