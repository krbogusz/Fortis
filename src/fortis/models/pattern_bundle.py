from __future__ import annotations

from collections import UserDict
from typing import TYPE_CHECKING

from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.pattern_spec import PatternSpec

if TYPE_CHECKING:
    from src.fortis.models.bindings import Bindings


class PatternBundle(UserDict[str, PatternSpec]):
    """A collection of pattern feature specifications, keyed by feature name.

    Used in rule target, context, and exception positions. Supports negation,
    positional contour matching, and pattern comparison — unlike FeatureBundle
    which represents realized phonological material.
    """

    def __repr__(self) -> str:
        """Represent a pattern bundle."""
        parts: list[str] = []
        for feature, spec in self.data.items():
            parts.append(f"{feature}: {spec}")
        return "[" + ", ".join(parts) + "]"

    def matches_against(self, segment: FeatureBundle, bindings: Bindings | None = None) -> bool:
        """Check if *self* (a pattern) matches *segment* (realized material).

        Every feature in the pattern must be present in the segment with a
        compatible value. Features in the segment that the pattern does not
        mention are unconstrained.

        For negated pattern specs, the match condition is inverted: the
        segment must *not* have the specified value for that feature.

        Args:
            segment: The realized segment to test against.
            bindings: Optional bindings dict for alpha variable resolution.
        """
        for feature, pattern_spec in self.data.items():
            if feature not in segment:
                # Absent feature: positive pattern fails, negated pattern passes
                if pattern_spec.negated:
                    continue
                return False
            segment_value = segment[feature]
            if not pattern_spec.matches_against(segment_value, bindings):
                return False
        return True

    def matches_exactly(self, other: PatternBundle) -> bool:
        """Check if this pattern is exactly identical to *other*.

        Both bundles must have the same set of features and the same value
        for every feature.
        """
        if set(self.data.keys()) != set(other.data.keys()):
            return False
        for feature in self.data:
            if self.data[feature].value != other.data[feature].value:
                return False
        return True

    def differing(self, other: PatternBundle) -> list[str]:
        """Return the features that are different between this pattern and *other*."""
        differing: list[str] = []
        for feature in self.data:
            if feature not in other.data:
                differing.append(feature)
                continue
            if self.data[feature].value != other.data[feature].value:
                differing.append(feature)
                continue
        for feature in other.data:
            if feature not in self.data and feature not in differing:
                differing.append(feature)
                continue
        return differing

    def negated(self) -> PatternBundle:
        """Return a new pattern bundle with every spec's negation flag flipped."""
        return PatternBundle(
            {name: PatternSpec(spec.value, negated=not spec.negated) for name, spec in self.data.items()}
        )