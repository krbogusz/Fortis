from collections import UserDict

from src.fortis.models.feature_value import FeatureValue


class FeatureBundle(UserDict[str, FeatureValue]):
    """A collection of realized feature values, keyed by feature name.

    Used for concrete phonological material — segments in the lexicon,
    diacritics, syllable parts, etc. No matching or negation methods;
    those belong on PatternBundle.
    """

    def __repr__(self) -> str:
        """Represent a feature bundle."""
        parts: list[str] = []
        for feature, value in self.data.items():
            parts.append(f"{feature}: {value}")
        return "[" + ", ".join(parts) + "]"

    def combine_with(self, other: FeatureBundle, form_contours: bool = False) -> FeatureBundle:
        """Combine this feature bundle with another.

        Args:
            other: The bundle to merge in.
            form_contours: If True, overlapping features form contours instead of overriding.
        """
        result = FeatureBundle(dict(self.data))
        for feature_name, value in other.items():
            if feature_name not in result:
                result[feature_name] = value
            elif form_contours:
                new_value = result[feature_name].form_contour_with(value)
                result[feature_name] = new_value
            else:
                result[feature_name] = value

        return result

    def matches_exactly(self, other: FeatureBundle) -> bool:
        """Check if this bundle is exactly identical to *other*.

        Both bundles must have the same set of features and the same value
        for every feature.
        """
        if set(self.data.keys()) != set(other.data.keys()):
            return False
        for feature in self.data:
            if self.data[feature].value != other.data[feature].value:
                return False
        return True

    def differing(self, other: FeatureBundle) -> list[str]:
        """Return the features that are different between this bundle and *other*."""
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
