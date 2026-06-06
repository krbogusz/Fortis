from dataclasses import dataclass

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_value import FeatureValue
from src.fortis.result import Err, Ok, Result


@dataclass
class FeatureSpec:
    """A feature name paired with its value.

    Args:
        feature: Full feature name.
        value: The feature's value (int, contour list, or None).
        is_negated: If the feature is negated.
    """

    feature: str
    value: FeatureValue
    is_negated: bool = False

    def __repr__(self) -> str:
        """Repr for feature spec."""
        negation = "!" if self.is_negated else ""
        return f"{negation}{self.feature}: {self.value}"

    @classmethod
    def from_str(cls, raw_string: str, features: FeatureInventory) -> Result[FeatureSpec, str]:
        """Parse from a string like '+nasal', 'height:2', or 'glottal_aperture:spread'.

        Matches feature names longest-first (full names, then short names).

        Args:
            raw_string: The raw token to parse.
            features: Feature inventory for name/value resolution.
            bare_unary_means_present: If True (default), a bare feature name (no value marker)
                on a unary feature is interpreted as "+feature" (value 1).
        """
        raw_string = raw_string.replace(" ", "")

        # Build lookup indices sorted longest-first for greedy matching
        full_names = sorted(features.keys(), key=len, reverse=True)
        short_to_full: dict[str, str] = {}
        for name, ft_def in features.items():
            if ft_def.short != name:
                short_to_full[ft_def.short] = name
        short_names = sorted(short_to_full.keys(), key=len, reverse=True)

        # Identify feature name
        for name in full_names + short_names:
            if name in raw_string:
                feature = short_to_full.get(name, name)
                break
        else:
            return Err(f"Could not identify feature in '{raw_string}'")

        # Negation
        if "!" in raw_string:
            negated = True
            raw_string = raw_string.replace("!", "")
        else:
            negated = False

        # Feature value
        value_result = FeatureValue.from_str(raw_string, feature, features)
        if value_result.is_err():
            return Err(value_result.unwrap_err())
        return Ok(FeatureSpec(feature, value_result.unwrap(), negated))

    @classmethod
    def apply_negation(cls, self_is_negated: bool, other_is_negated: bool, matches: bool) -> bool:
        """Negation helper."""
        if self_is_negated and other_is_negated:
            return matches
        elif self_is_negated and not other_is_negated:
            return not matches
        elif not self_is_negated and other_is_negated:
            return not matches
        else:
            return matches

    def matches_pattern(self, other: FeatureSpec) -> bool:
        """Whether this realized segment satisfies *pattern*.

        Args:
            other: The feature spec to compare against.
            place: Which position(s) to check — applies to both single-vs-contour and
                contour-vs-contour matching.
        """
        match = self.value.matches_pattern(other.value)
        # Other situations
        return self.apply_negation(self.is_negated, other.is_negated, match)

    def form_contour(self, other: FeatureSpec) -> FeatureSpec:
        """Form a contour by appending *other*'s value onto *self*'s.

        Both specifications must refer to the same feature.

        Args:
            other: The feature spec to append.

        Returns:
            A new FeatureSpec whose value is a list combining both values.
        """
        if self.feature != other.feature:
            raise ValueError(f"The two merged features are not the same: '{self.feature}' vs '{other.feature}'")

        new_value = self.value.form_contour_with(other.value)

        return FeatureSpec(self.feature, new_value)
