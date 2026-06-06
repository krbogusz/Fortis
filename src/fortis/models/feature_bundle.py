from collections import UserDict

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.result import Err, Ok, Result


class FeatureBundle(UserDict[str, FeatureSpec]):
    """A collection of feature specifications, keyed by feature name."""

    def __repr__(self) -> str:
        """Represent a feature bundle."""
        parts: list[str] = []
        for _, spec in self.data.items():
            parts.append(f"{spec}")
        return "[" + ", ".join(parts) + "]"

    @classmethod
    def from_string(cls, raw_string: str, features: FeatureInventory) -> Result[FeatureBundle, list[str]]:
        """Parse a comma-separated feature bundle string (e.g. '+syll, -cons, height:2').

        Args:
            raw_string: Comma- or semicolon-separated feature specs.
            features: Feature inventory for name/value resolution.
            bare_unary_means_present: If True (default), a bare feature name on a unary
                feature is interpreted as present (value 1).
        """
        error_list = []
        string = raw_string.replace(";", ",")
        tokens = [t.strip() for t in string.split(",") if t.strip()]

        bundle = cls()
        for token in tokens:
            result = FeatureSpec.from_str(token, features)
            if result.is_err():
                error_list.append(result.unwrap_err())
                continue
            spec = result.unwrap()
            bundle[spec.feature] = spec

        if error_list:
            return Err(error_list)

        return Ok(bundle)

    def matches_pattern(self, other: FeatureBundle) -> bool:
        """Check if this bundle satisfies the pattern defined by *other*.

        *other* is the pattern; *self* is the target segment being tested.
        Every feature in *other* must be present in *self* with a compatible value.
        Features in *self* that *other* does not mention are unconstrained.

        A feature that is **entirely absent** from the segment never satisfies
        a positive pattern requirement — absence means the segment definitively
        does not have that feature. A feature present with value ``None``
        (unspecified) also does not match a pattern requiring a specific value.

        Args:
            other: The pattern bundle to match against.
            contour_position: Positional control for contour matching, passed to FeatureSpec.matches.
        """
        for feature, feature_spec in other.data.items():
            if feature not in self.data:
                return False
            if not self.data[feature].matches_pattern(feature_spec):
                return False
        return True

    def matches_exactly(self, other: FeatureBundle) -> bool:
        """Check if this bundle is exactly identical to *other*.

        Both bundles must have the same set of features and the same value
        (int, list[int], None) for every feature.
        """
        if set(self.data.keys()) != set(other.data.keys()):
            return False
        for feature in self.data:
            if self.data[feature].value.value != other.data[feature].value.value:
                return False
        return True

    def differing(self, other: FeatureBundle) -> list[str]:
        """Return the features that are different between this bundle and *other*."""
        differing: list[str] = []
        for feature in self.data:
            if feature not in other.data:
                differing.append(feature)
                continue
            if self.data[feature].value.value != other.data[feature].value.value:
                differing.append(feature)
                continue
        for feature in other.data:
            if feature not in self.data and feature not in differing:
                differing.append(feature)
                continue
        return differing

    def negated(self) -> FeatureBundle:
        """Return a new bundle with every spec's negation flag flipped."""
        return FeatureBundle(
            {
                name: FeatureSpec(spec.feature, spec.value, is_negated=not spec.is_negated)
                for name, spec in self.data.items()
            }
        )

    def combine_with(self, other: FeatureBundle, form_contours: bool = False) -> FeatureBundle:
        """Combine this feature bundle with another.

        Args:
            other: The bundle to merge in.
            form_contours: If True, overlapping features form contours instead of overriding.
        """
        result = FeatureBundle(dict(self.data))
        for feature_name, feature_spec in other.items():
            if feature_name not in result:
                result[feature_name] = feature_spec
            elif form_contours:
                result[feature_name] = result[feature_name].form_contour(feature_spec)
            else:
                result[feature_name] = feature_spec

        return result
