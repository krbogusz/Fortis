from collections import UserDict

from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.feature_spec import FeatureSpec, Place
from src.fortis.result import Err, Ok, Result


class FeatureBundle(UserDict[str, FeatureSpec]):
    """A collection of feature specifications, keyed by feature name."""

    def __repr__(self) -> str:
        """Represent a feature bundle."""
        parts: list[str] = []
        for name, spec in self.data.items():
            if spec.value is None:
                parts.append(f"{name}: ∅")
            elif isinstance(spec.value, list):
                vals = ">".join(_repr_value(v) for v in spec.value)
                parts.append(f"{name}: {vals}")
            else:
                parts.append(f"{name}: {_repr_value(spec.value)}")
        return "{" + ", ".join(parts) + "}"

    @classmethod
    def from_str(
        cls, raw_string: str, inventory: FeatureInventory, bare_unary_means_present: bool = False
    ) -> Result[FeatureBundle, list[str]]:
        """Parse a comma-separated feature bundle string (e.g. '+syll, -cons, height:2').

        Args:
            raw_string: Comma- or semicolon-separated feature specs.
            inventory: Feature inventory for name/value resolution.
            bare_unary_means_present: If True, a bare feature name on a unary
                feature is interpreted as present (value 1).
        """
        error_list = []
        string = raw_string.replace(" ", "").replace(";", ",")
        tokens = [t for t in string.split(",") if t]

        bundle = cls()
        for token in tokens:
            result = FeatureSpec.from_string(token, inventory, bare_unary_means_present)
            if result.is_err():
                error_list.append(result.unwrap_err())
                continue
            spec = result.unwrap()
            bundle[spec.feature] = spec

        if error_list:
            return Err(error_list)

        return Ok(bundle)

    def match_pattern(self, other: FeatureBundle, ignore_none: bool = False, place: Place = "any") -> bool:
        """Check if this bundle satisfies the pattern defined by *other*.

        *other* is the pattern (typically a rule condition or sonority definition);
        *self* is the target segment being tested.  Every feature in *other* must
        be present in *self* with a compatible value.  Features in *self* that
        *other* does not mention are unconstrained — the pattern doesn't care
        about them.

        Args:
            other: The pattern bundle to match against.
            ignore_none: Treat missing features and None values as wildcards.
            place: Positional control for contour matching, passed to FeatureSpec.matches.
        """
        for feature, spec in other.data.items():
            if feature not in self.data:
                # Feature not present in target — unspecified
                if ignore_none:
                    continue
                return False
            if not spec.matches(self.data[feature], ignore_none=ignore_none, place=place):
                return False
        return True

    def match_exact(self, other: FeatureBundle) -> bool:
        """Check if this bundle is exactly identical to *other*.

        Both bundles must have the same set of features and the same value for
        every feature. No wildcard or positional semantics — pure structural
        equality.
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


def _repr_value(value: int | None) -> str:
    """Format a value for __repr__ (inlined to avoid circular import with presentation.py)."""
    if value is None:
        return "∅"
    if value == 1:
        return "+"
    if value == 0:
        return "-"
    return str(value)
