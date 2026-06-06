"""Tests for src.fortis.models.feature_value — FeatureValue parsing, matching, contours, and repr."""

from __future__ import annotations

import pytest

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_value import FeatureValue
from src.fortis.result import Ok
from tests.conftest import make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# single_from_str (static method)
# ---------------------------------------------------------------------------


class TestSingleValueBinary:
    def test_plus(self, features):
        assert FeatureValue.single_from_str("+", "consonantal", features) == Ok(1)

    def test_one(self, features):
        assert FeatureValue.single_from_str("1", "consonantal", features) == Ok(1)

    def test_present(self, features):
        assert FeatureValue.single_from_str("present", "consonantal", features) == Ok(1)

    def test_minus(self, features):
        assert FeatureValue.single_from_str("-", "consonantal", features) == Ok(0)

    def test_zero(self, features):
        assert FeatureValue.single_from_str("0", "consonantal", features) == Ok(0)

    def test_absent(self, features):
        assert FeatureValue.single_from_str("absent", "consonantal", features) == Ok(0)

    def test_invalid(self, features):
        result = FeatureValue.single_from_str("maybe", "consonantal", features)
        assert result.is_err()


class TestSingleValueUnary:
    def test_plus(self, features):
        assert FeatureValue.single_from_str("+", "nasal", features) == Ok(1)

    def test_minus_rejected(self, features):
        result = FeatureValue.single_from_str("-", "nasal", features)
        assert result.is_err()

    def test_invalid(self, features):
        result = FeatureValue.single_from_str("maybe", "nasal", features)
        assert result.is_err()


class TestSingleValueScalar:
    def test_integer_key(self, features):
        assert FeatureValue.single_from_str("3", "height", features) == Ok(3)

    def test_label(self, features):
        assert FeatureValue.single_from_str("high", "height", features) == Ok(3)

    def test_another_label(self, features):
        assert FeatureValue.single_from_str("low", "height", features) == Ok(1)

    def test_invalid_label(self, features):
        result = FeatureValue.single_from_str("ultrahigh", "height", features)
        assert result.is_err()


class TestSingleValueUnspecified:
    def test_none_symbol(self, features):
        assert FeatureValue.single_from_str("none", "consonantal", features) == Ok(None)

    def test_null_symbol(self, features):
        assert FeatureValue.single_from_str("null", "consonantal", features) == Ok(None)

    def test_unspecified_symbol(self, features):
        assert FeatureValue.single_from_str("unspecified", "consonantal", features) == Ok(None)

    def test_empty_set_symbol(self, features):
        assert FeatureValue.single_from_str("∅", "consonantal", features) == Ok(None)


# ---------------------------------------------------------------------------
# from_str — basic value parsing
# ---------------------------------------------------------------------------


class TestFromStrBasic:
    def test_simple_plus(self, features):
        result = FeatureValue.from_str("+consonantal", "consonantal", features)
        assert result == Ok(FeatureValue(1))

    def test_simple_minus(self, features):
        result = FeatureValue.from_str("-consonantal", "consonantal", features)
        assert result == Ok(FeatureValue(0))

    def test_scalar_by_label(self, features):
        result = FeatureValue.from_str("height:high", "height", features)
        assert result == Ok(FeatureValue(3))

    def test_scalar_by_int(self, features):
        result = FeatureValue.from_str("height:3", "height", features)
        assert result == Ok(FeatureValue(3))

    def test_unspecified(self, features):
        result = FeatureValue.from_str("consonantal:none", "consonantal", features)
        assert result == Ok(FeatureValue(None))

    def test_contour(self, features):
        result = FeatureValue.from_str("tone:1>3", "tone", features)
        assert result == Ok(FeatureValue([1, 3]))

    def test_three_step_contour(self, features):
        result = FeatureValue.from_str("tone:1>2>3", "tone", features)
        assert result == Ok(FeatureValue([1, 2, 3]))

    def test_contour_with_unspecified(self, features):
        result = FeatureValue.from_str("nasal:none>1", "nasal", features)
        assert result == Ok(FeatureValue([None, 1]))

    def test_contour_with_unspecified_binary(self, features):
        result = FeatureValue.from_str("consonantal:none>1", "consonantal", features)
        assert result == Ok(FeatureValue([None, 1]))

    def test_bare_unary_means_present(self, features):
        result = FeatureValue.from_str("nasal", "nasal", features)
        assert result == Ok(FeatureValue(1))

    def test_bare_binary_is_error(self, features):
        result = FeatureValue.from_str("consonantal", "consonantal", features)
        assert result.is_err()

    def test_short_name_stripping(self, features):
        """from_str should resolve values using both full and short feature names."""
        result = FeatureValue.from_str("+cons", "consonantal", features)
        assert result == Ok(FeatureValue(1))

    def test_scalar_short_name(self, features):
        result = FeatureValue.from_str("hgt:2", "height", features)
        assert result == Ok(FeatureValue(2))


# ---------------------------------------------------------------------------
# from_str — contour position parsing (@-syntax)
# ---------------------------------------------------------------------------


class TestFromStrContourPosition:
    def test_position_initial(self, features):
        result = FeatureValue.from_str("tone:1>3@initial", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == [1, 3]
        assert fv.position == "initial"

    def test_position_final(self, features):
        result = FeatureValue.from_str("tone:1>3@final", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == [1, 3]
        assert fv.position == "final"

    def test_position_all(self, features):
        result = FeatureValue.from_str("tone:3@all", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == 3
        assert fv.position == "all"

    def test_position_any(self, features):
        result = FeatureValue.from_str("tone:1>3@any", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == [1, 3]
        assert fv.position == "any"

    def test_position_integer(self, features):
        result = FeatureValue.from_str("tone:3@2", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == 3
        assert fv.position == 2

    def test_position_list(self, features):
        result = FeatureValue.from_str("tone:1>3@1;2", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == [1, 3]
        assert fv.position == [1, 2]

    def test_position_default_is_any(self, features):
        """When no @-position is given, position defaults to 'any'."""
        result = FeatureValue.from_str("tone:1>3", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.position == "any"

    def test_position_zero_is_error(self, features):
        result = FeatureValue.from_str("tone:3@0", "tone", features)
        assert result.is_err()

    def test_position_negative_is_accepted(self, features):
        """Negative positions mean 'count from end' (e.g. -1 = last slot)."""
        result = FeatureValue.from_str("tone:3@-1", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == 3
        assert fv.position == -1

    def test_position_invalid_string_is_error(self, features):
        result = FeatureValue.from_str("tone:3@xyz", "tone", features)
        assert result.is_err()

    def test_position_list_non_contiguous_is_error(self, features):
        result = FeatureValue.from_str("tone:1>3>5@1;3", "tone", features)
        assert result.is_err()

    def test_position_list_length_mismatch_is_error(self, features):
        """Position list must have the same length as the contour."""
        result = FeatureValue.from_str("tone:1>3@1;2;3", "tone", features)
        assert result.is_err()

    def test_position_list_with_zero_is_error(self, features):
        result = FeatureValue.from_str("tone:1>3@0;1", "tone", features)
        assert result.is_err()

    def test_contour_position_on_scalar(self, features):
        """Position can be set on a single (scalar) value, not just contours."""
        result = FeatureValue.from_str("tone:3@final", "tone", features)
        assert result.is_ok()
        fv = result.unwrap()
        assert fv.value == 3
        assert fv.position == "final"


# ---------------------------------------------------------------------------
# determine_contour_position (static method)
# ---------------------------------------------------------------------------


class TestDetermineContourPosition:
    def test_initial(self):
        assert FeatureValue.determine_contour_position("initial") == Ok("initial")

    def test_final(self):
        assert FeatureValue.determine_contour_position("final") == Ok("final")

    def test_all(self):
        assert FeatureValue.determine_contour_position("all") == Ok("all")

    def test_any(self):
        assert FeatureValue.determine_contour_position("any") == Ok("any")

    def test_positive_integer(self):
        assert FeatureValue.determine_contour_position("3") == Ok(3)

    def test_positive_integer_1(self):
        assert FeatureValue.determine_contour_position("1") == Ok(1)

    def test_zero_is_error(self):
        assert FeatureValue.determine_contour_position("0").is_err()

    def test_negative_integer(self):
        """Negative positions are valid (count from end)."""
        assert FeatureValue.determine_contour_position("-1") == Ok(-1)

    def test_negative_integer_minus_three(self):
        assert FeatureValue.determine_contour_position("-3") == Ok(-3)

    def test_semicolon_list(self):
        assert FeatureValue.determine_contour_position("1;2;3") == Ok([1, 2, 3])

    def test_semicolon_list_with_zero_is_error(self):
        assert FeatureValue.determine_contour_position("0;1").is_err()

    def test_invalid_string_is_error(self):
        assert FeatureValue.determine_contour_position("xyz").is_err()


# ---------------------------------------------------------------------------
# matches_pattern
# ---------------------------------------------------------------------------


class TestMatchesPattern:
    # --- scalar vs scalar ---

    def test_scalar_equal(self):
        assert FeatureValue(1).matches_pattern(FeatureValue(1)) is True

    def test_scalar_unequal(self):
        assert FeatureValue(1).matches_pattern(FeatureValue(0)) is False

    def test_scalar_none_matches_none(self):
        assert FeatureValue(None).matches_pattern(FeatureValue(None)) is True

    def test_scalar_does_not_match_none(self):
        assert FeatureValue(1).matches_pattern(FeatureValue(None)) is False

    def test_none_does_not_match_scalar(self):
        assert FeatureValue(None).matches_pattern(FeatureValue(1)) is False

    # --- single vs contour (position=any) ---

    def test_single_in_contour(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(3, "any")) is True

    def test_single_not_in_contour(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(7, "any")) is False

    def test_single_at_start(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(1, "any")) is True

    def test_single_at_end(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(5, "any")) is True

    # --- single vs contour (position=initial) ---

    def test_initial_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(1, "initial")) is True

    def test_initial_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(3, "initial")) is False

    # --- single vs contour (position=final) ---

    def test_final_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(5, "final")) is True

    def test_final_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(1, "final")) is False

    # --- single vs contour (position=all) ---

    def test_all_uniform(self):
        assert FeatureValue([3, 3, 3]).matches_pattern(FeatureValue(3, "all")) is True

    def test_all_not_uniform(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(3, "all")) is False

    def test_all_single_element_contour(self):
        assert FeatureValue([5]).matches_pattern(FeatureValue(5, "all")) is True

    # --- single vs contour (position=int) ---

    def test_position_match(self):
        """One-indexed position 2 = second slot."""
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(3, 2)) is True

    def test_position_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(1, 2)) is False

    def test_position_out_of_range(self):
        assert FeatureValue([1, 3]).matches_pattern(FeatureValue(3, 5)) is False

    # --- single vs contour (position=list) ---

    def test_position_list_all_match(self):
        assert FeatureValue([1, 1, 3]).matches_pattern(FeatureValue(1, [1, 2])) is True

    def test_position_list_partial_fail(self):
        assert FeatureValue([1, 3, 1]).matches_pattern(FeatureValue(1, [1, 2])) is False

    # --- contour vs contour ---

    def test_contour_any_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([1, 3], "any")) is True

    def test_contour_any_no_match(self):
        assert FeatureValue([1, 5, 7]).matches_pattern(FeatureValue([3, 4], "any")) is False

    def test_contour_all_same_length(self):
        assert FeatureValue([1, 3]).matches_pattern(FeatureValue([1, 3], "all")) is True

    def test_contour_all_different_length(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([1, 3], "all")) is False

    def test_contour_initial(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([1, 3], "initial")) is True

    def test_contour_initial_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([3, 5], "initial")) is False

    def test_contour_final(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([3, 5], "final")) is True

    def test_contour_final_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue([1, 3], "final")) is False

    # --- contour with None values ---

    def test_none_in_contour_matches(self):
        assert FeatureValue([None, 1]).matches_pattern(FeatureValue([None, 1], "all")) is True

    def test_none_mismatch(self):
        assert FeatureValue([1, 1]).matches_pattern(FeatureValue([None, 1], "all")) is False

    # --- scalar target (length 1) vs pattern ---

    def test_scalar_target_any_match(self):
        assert FeatureValue(1).matches_pattern(FeatureValue(1, "any")) is True

    def test_scalar_target_any_no_match(self):
        assert FeatureValue(1).matches_pattern(FeatureValue(0, "any")) is False

    def test_scalar_target_contour_too_long(self):
        """A contour pattern longer than the scalar target cannot fit."""
        assert FeatureValue(1).matches_pattern(FeatureValue([1, 3], "any")) is False

    # --- negative position (direct construction, count-from-end) ---

    def test_negative_position_from_end(self):
        """Direct construction with position=-1 means last slot."""
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(5, -1)) is True

    def test_negative_position_from_end_no_match(self):
        assert FeatureValue([1, 3, 5]).matches_pattern(FeatureValue(1, -1)) is False


# ---------------------------------------------------------------------------
# matches_exactly
# ---------------------------------------------------------------------------


class TestMatchesExactly:
    def test_equal_scalars(self):
        assert FeatureValue(1).matches_exactly(FeatureValue(1)) is True

    def test_unequal_scalars(self):
        assert FeatureValue(1).matches_exactly(FeatureValue(0)) is False

    def test_none_equals_none(self):
        assert FeatureValue(None).matches_exactly(FeatureValue(None)) is True

    def test_scalar_vs_none(self):
        assert FeatureValue(1).matches_exactly(FeatureValue(None)) is False

    def test_none_vs_scalar(self):
        assert FeatureValue(None).matches_exactly(FeatureValue(1)) is False

    def test_equal_contours(self):
        assert FeatureValue([1, 3]).matches_exactly(FeatureValue([1, 3])) is True

    def test_unequal_contours(self):
        assert FeatureValue([1, 3]).matches_exactly(FeatureValue([1, 5])) is False

    def test_scalar_vs_length_one_contour(self):
        """A scalar 1 matches a contour [1] (normalised to same list)."""
        assert FeatureValue(1).matches_exactly(FeatureValue([1])) is True

    def test_length_one_contour_vs_scalar(self):
        assert FeatureValue([1]).matches_exactly(FeatureValue(1)) is True

    def test_different_length_contours(self):
        assert FeatureValue([1, 3]).matches_exactly(FeatureValue([1, 3, 5])) is False

    def test_contour_with_none(self):
        assert FeatureValue([None, 1]).matches_exactly(FeatureValue([None, 1])) is True

    def test_position_ignored(self):
        """matches_exactly compares values, not positions."""
        assert FeatureValue(1, "initial").matches_exactly(FeatureValue(1, "final")) is True


# ---------------------------------------------------------------------------
# form_contour_with
# ---------------------------------------------------------------------------


class TestFormContourWith:
    def test_scalar_plus_scalar(self):
        result = FeatureValue(1).form_contour_with(FeatureValue(3))
        assert result.value == [1, 3]
        assert result.position == "any"  # position resets to default

    def test_scalar_plus_contour(self):
        result = FeatureValue(1).form_contour_with(FeatureValue([2, 3]))
        assert result.value == [1, 2, 3]

    def test_contour_plus_scalar(self):
        result = FeatureValue([1, 2]).form_contour_with(FeatureValue(3))
        assert result.value == [1, 2, 3]

    def test_contour_plus_contour(self):
        result = FeatureValue([1, 2]).form_contour_with(FeatureValue([3, 5]))
        assert result.value == [1, 2, 3, 5]

    def test_with_none_values(self):
        result = FeatureValue(None).form_contour_with(FeatureValue(1))
        assert result.value == [None, 1]


# ---------------------------------------------------------------------------
# __repr__
# ---------------------------------------------------------------------------


class TestRepr:
    def test_positive_scalar(self):
        assert repr(FeatureValue(1)) == "1"

    def test_zero_scalar(self):
        assert repr(FeatureValue(0)) == "0"

    def test_none(self):
        assert repr(FeatureValue(None)) == "∅"

    def test_contour(self):
        assert repr(FeatureValue([1, 3])) == "1>3"

    def test_contour_with_none(self):
        assert repr(FeatureValue([None, 1])) == "∅>1"

    def test_position_initial(self):
        assert repr(FeatureValue(3, "initial")) == "3@initial"

    def test_position_final(self):
        assert repr(FeatureValue(3, "final")) == "3@final"

    def test_position_all(self):
        assert repr(FeatureValue(3, "all")) == "3@all"

    def test_position_any_is_hidden(self):
        """Position 'any' is the default and should not appear in repr."""
        assert repr(FeatureValue(3, "any")) == "3"

    def test_position_integer(self):
        assert repr(FeatureValue(3, 2)) == "3@2"

    def test_position_list(self):
        assert repr(FeatureValue(3, [1, 2])) == "3@1;2"

    def test_contour_with_position(self):
        assert repr(FeatureValue([1, 3], "initial")) == "1>3@initial"
