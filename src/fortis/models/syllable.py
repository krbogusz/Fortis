from dataclasses import dataclass

from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.sequence import Sequence


@dataclass
class Syllable:
    """Syllable."""

    sequence: Sequence
    bundle: FeatureBundle
    onset: list[int]
    nucleus: list[int]
    coda: list[int]
