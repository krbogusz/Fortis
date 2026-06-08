"""Syllable model — placeholder for future syllable-structure representation.

This model is not yet integrated into the rule application pipeline.
It is reserved for representing parsed syllable structure with explicit
onset/nucleus/coda segmentation.
"""

from dataclasses import dataclass

from src.fortis.models.feature_bundle import FeatureBundle


@dataclass
class Syllable:
    """A syllable with onset, nucleus, and coda segment indices.

    Args:
        sequence: The full sequence of feature bundles.
        bundle: Syllable-level feature bundle.
        onset: Indices of onset segments in the sequence.
        nucleus: Indices of nucleus segments in the sequence.
        coda: Indices of coda segments in the sequence.
    """

    sequence: list[FeatureBundle]
    bundle: FeatureBundle
    onset: list[int]
    nucleus: list[int]
    coda: list[int]
