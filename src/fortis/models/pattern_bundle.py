from collections import UserDict

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.bindings import Bindings
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.pattern_spec import PatternSpec
from src.fortis.result import Err, Ok, Result


class PatternBundle(UserDict[str, PatternSpec]):
    """A collection of pattern feature specifications, keyed by feature name.

    Used in rule target, context, and exception positions. Supports negation,
    positional contour matching, and pattern comparison — unlike FeatureBundle
    which represents realized phonological material.
    """

    def __repr__(self) -> str:
        """Represent a pattern bundle."""
        parts: list[str] = []
        for _, spec in self.data.items():
            parts.append(f"{spec}")
        return "[" + ", ".join(parts) + "]"

    @classmethod
    def from_string(cls, raw_string: str, features: FeatureInventory) -> Result[PatternBundle, list[str]]:
        """Parse a comma-separated pattern bundle string.

        Supports negation (``!``) and contour positions (``@initial``, ``@2``,
        etc.) which are not valid in FeatureBundle.

        Args:
            raw_string: Comma- or semicolon-separated pattern specs.
            features: Feature inventory for name/value resolution.
        """
        error_list = []
        string = raw_string.replace(";", ",")
        tokens = [t.strip() for t in string.split(",") if t.strip()]

        bundle = cls()
        for token in tokens:
            result = PatternSpec.from_string(token, features)
            if result.is_err():
                error_list.append(result.unwrap_err())
                continue
            spec = result.unwrap()
            bundle[spec.feature] = spec

        if error_list:
            return Err(error_list)

        return Ok(bundle)

    def matches_against(self, segment: FeatureBundle, bindings: Bindings | None = None) -> bool:
        """Check if *self* (a pattern) matches *segment* (realized material).

        Every feature in the pattern must be present in the segment with a
        compatible value. Features in the segment that the pattern does not
        mention are unconstrained.

        For negated pattern specs, the match condition is inverted: the
        segment must *not* have the specified value for that feature.

        For pattern specs with contour positions, the realized segment's
        contour value is checked at the specified positions.

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
            segment_spec = segment[feature]
            if not pattern_spec.matches_against(segment_spec, bindings):
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
            if self.data[feature].value.value != other.data[feature].value.value:
                return False
        return True

    def differing(self, other: PatternBundle) -> list[str]:
        """Return the features that are different between this pattern and *other*."""
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

    def negated(self) -> PatternBundle:
        """Return a new pattern bundle with every spec's negation flag flipped."""
        return PatternBundle(
            {name: PatternSpec(spec.feature, spec.value, negated=not spec.negated) for name, spec in self.data.items()}
        )
