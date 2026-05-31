from collections import UserList
from typing import Set

from src.fortis.models.feature_bundle import FeatureBundle


class Sequence(UserList[FeatureBundle]):
    """An ordered sequence of feature bundles (segments).

    Attributes:
        syllable_boundaries: Set of positions where syllable boundaries
            occur. Position i means "between segment i-1 and i".
            Position 0 = start of sequence, len(data) = end of sequence.
    """

    def __init__(
        self,
        data: list[FeatureBundle] | None = None,
        syllable_boundaries: Set[int] | None = None,
    ) -> None:
        super().__init__(data)
        self.syllable_boundaries: Set[int] = syllable_boundaries or set()