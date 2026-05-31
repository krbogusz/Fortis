from dataclasses import dataclass
from typing import Literal

from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.values import value_from_str
from src.fortis.result import Err, Ok, Result

type Place = Literal["any", "initial", "final", "all"] | int | list[int]
"""Which position(s) in a contour to check during matching."""


@dataclass
class FeatureSpec:
    """A feature name paired with its value.

    Args:
        feature: Full feature name.
        value: The feature's value (int, contour list, or None).
        negated: If True, this spec matches when the feature does NOT satisfy
            the value (feature-level negation, e.g. ``!nasal``).
    """

    feature: str
    value: int | list[int | None] | None
    negated: bool = False

    @classmethod
    def from_string(
        cls, raw_string: str, inventory: FeatureInventory, bare_unary_means_present: bool = False
    ) -> Result[FeatureSpec, str]:
        """Parse from a string like '+nasal', 'height:2', or 'glottal_aperture:spread'.

        Matches feature names longest-first (full names, then short names).

        Args:
            raw_string: The raw token to parse.
            inventory: Feature inventory for name/value resolution.
            bare_unary_means_present: If True, a bare feature name (no value marker)
                on a unary feature is interpreted as "+feature" (value 1).
        """
        # Build lookup indices sorted longest-first for greedy matching
        full_names = sorted(inventory.keys(), key=len, reverse=True)
        short_to_full: dict[str, str] = {}
        for name, ft_def in inventory.items():
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

        value_result = value_from_str(raw_string, feature, inventory, bare_unary_means_present)
        if value_result.is_err():
            return Err(value_result.unwrap_err())
        return Ok(FeatureSpec(feature, value_result.unwrap()))

    def matches(self, other: FeatureSpec, ignore_none: bool = False, place: Place = "any") -> bool:
        """Check if this spec matches *other*.

        Args:
            other: The feature spec to compare against.
            ignore_none: Treat None (unspecified) values as wildcards that match anything.
            place: Which position(s) to check — applies to both single-vs-contour and
                contour-vs-contour matching.
        """
        # Top-level None handling
        if self.value is None and other.value is None:
            return True
        if self.value is None:
            return ignore_none
        if other.value is None:
            return ignore_none
        # Int vs int
        if isinstance(self.value, int) and isinstance(other.value, int):
            return self.value == other.value
        # Single vs contour (direction doesn't matter)
        if isinstance(self.value, int) and isinstance(other.value, list):
            return self._single_matches_contour(self.value, other.value, place, ignore_none)
        if isinstance(self.value, list) and isinstance(other.value, int):
            return self._single_matches_contour(other.value, self.value, place, ignore_none)
        # Contour vs contour
        if isinstance(self.value, list) and isinstance(other.value, list):
            return self._contour_matches_contour(self.value, other.value, place, ignore_none)
        raise TypeError(f"Wrong matching types: {type(self.value)} vs {type(other.value)}")

    @staticmethod
    def _single_matches_contour(pattern: int, contour: list[int | None], place: Place, ignore_none: bool) -> bool:
        """Check if a single value appears at the position(s) specified by *place*."""

        def matches_at(v: int | None) -> bool:
            if v is None and ignore_none:
                return True
            return v == pattern

        # "any" — existential: match at any position
        if place == "any":
            for v in contour:
                if matches_at(v):
                    return True
            return False

        # "initial" — first position only
        if place == "initial":
            return matches_at(contour[0])

        # "final" — last position only
        if place == "final":
            return matches_at(contour[-1])

        # "all" — must match at every position
        if place == "all":
            for v in contour:
                if not matches_at(v):
                    return False
            return True

        # single integer index
        if isinstance(place, int):
            if place < 0 or place >= len(contour):
                return False
            return matches_at(contour[place])

        # list of integer indices — must match at every listed position
        if isinstance(place, list):
            for idx in place:
                if idx < 0 or idx >= len(contour):
                    return False
                if not matches_at(contour[idx]):
                    return False
            return True

        return False

    @staticmethod
    def _contour_matches_contour(
        pattern: list[int | None], target: list[int | None], place: Place, ignore_none: bool
    ) -> bool:
        """Element-wise contour comparison with positional control."""

        def matches_at(i: int) -> bool:
            """Check that pattern[i] and target[i] agree (or None wildcards)."""
            if pattern[i] is None and ignore_none:
                return True
            if target[i] is None and ignore_none:
                return True
            return pattern[i] == target[i]

        # "any" — existential: at least one position matches
        if place == "any":
            for i in range(min(len(pattern), len(target))):
                if matches_at(i):
                    return True
            return False

        # "all" — every position must match, and contours must be same length
        if place == "all":
            if len(pattern) != len(target):
                return False
            for i in range(len(pattern)):
                if not matches_at(i):
                    return False
            return True

        # "initial" — first positions must match
        if place == "initial":
            if not pattern or not target:
                return False
            return matches_at(0)

        # "final" — last positions must match
        if place == "final":
            if not pattern or not target:
                return False
            return matches_at(-1)

        # single integer index — that position in both must match
        if isinstance(place, int):
            if place < 0 or place >= len(pattern) or place >= len(target):
                return False
            return matches_at(place)

        # list of integer indices — every listed position in both must match
        if isinstance(place, list):
            for idx in place:
                if idx < 0 or idx >= len(pattern) or idx >= len(target):
                    return False
                if not matches_at(idx):
                    return False
            return True

        return False

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

        if isinstance(self.value, list):
            self_values = self.value
        else:
            self_values = [self.value]

        if isinstance(other.value, list):
            other_values = other.value
        else:
            other_values = [other.value]

        return FeatureSpec(self.feature, self_values + other_values)
