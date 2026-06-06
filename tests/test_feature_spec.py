"""Tests for src.fortis.models.feature_spec — FeatureSpec parsing, matching, and contour."""

from __future__ import annotations

import pytest

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_value import FeatureValue
from tests.conftest import make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# from_string
# ---------------------------------------------------------------------------


class TestFromString:
    def test_plus_binary(self, features):
        result = FeatureSpec.from_str("+consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value.value == 1

    def test_minus_binary(self, features):
        result = FeatureSpec.from_str("-consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value.value == 0

    def test_short_name(self, features):
        result = FeatureSpec.from_str("+cons", features)
        assert result.is_ok()
        assert result.unwrap().feature == "consonantal"

    def test_scalar_int(self, features):
        result = FeatureSpec.from_str("height:3", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "height"
        assert spec.value.value == 3

    def test_scalar_label(self, features):
        result = FeatureSpec.from_str("height:high", features)
        assert result.is_ok()
        assert result.unwrap().value.value == 3

    def test_short_name_scalar(self, features):
        result = FeatureSpec.from_str("hgt:2", features)
        assert result.is_ok()
        assert result.unwrap().feature == "height"

    def test_bare_unary(self, features):
        result = FeatureSpec.from_str("nasal", features)
        assert result.is_ok()
        assert result.unwrap().value.value == 1

    def test_unknown_feature(self, features):
        result = FeatureSpec.from_str("+unknown", features)
        assert result.is_err()

    def test_contour_value(self, features):
        result = FeatureSpec.from_str("tone:1>3", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "tone"
        assert spec.value.value == [1, 3]

    def test_unspecified_value(self, features):
        result = FeatureSpec.from_str("consonantal:none", features)
        assert result.is_ok()
        assert result.unwrap().value.value is None


# ---------------------------------------------------------------------------
# from_string — negation
# ---------------------------------------------------------------------------


class TestFromStringNegation:
    def test_negated_binary(self, features):
        result = FeatureSpec.from_str("!+cons", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value.value == 1
        assert spec.is_negated is True

    def test_negated_binary_minus(self, features):
        result = FeatureSpec.from_str("!-cons", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value.value == 0
        assert spec.is_negated is True

    def test_negated_bare_unary(self, features):
        result = FeatureSpec.from_str("!nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "nasal"
        assert spec.value.value == 1
        assert spec.is_negated is True

    def test_negated_scalar(self, features):
        result = FeatureSpec.from_str("!height:2", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "height"
        assert spec.value.value == 2
        assert spec.is_negated is True

    def test_negated_unspecified(self, features):
        result = FeatureSpec.from_str("!consonantal:none", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.value.value is None
        assert spec.is_negated is True

    def test_non_negated_has_negated_false(self, features):
        result = FeatureSpec.from_str("+cons", features)
        assert result.is_ok()
        assert result.unwrap().is_negated is False


# ---------------------------------------------------------------------------
# matches_pattern — single vs single
# ---------------------------------------------------------------------------


class TestMatchesSingleSingle:
    def test_equal(self, features):
        a = FeatureSpec("consonantal", FeatureValue(1))
        b = FeatureSpec("consonantal", FeatureValue(1))
        assert a.matches_pattern(b) is True

    def test_not_equal(self, features):
        a = FeatureSpec("consonantal", FeatureValue(1))
        b = FeatureSpec("consonantal", FeatureValue(0))
        assert a.matches_pattern(b) is False

    def test_both_none(self, features):
        a = FeatureSpec("consonantal", FeatureValue(None))
        b = FeatureSpec("consonantal", FeatureValue(None))
        assert a.matches_pattern(b) is True


# ---------------------------------------------------------------------------
# matches_pattern — negation
# ---------------------------------------------------------------------------


class TestMatchesNegation:
    def test_negated_pattern_matching_value_does_not_match(self, features):
        """Segment with +cons does not match negated pattern !+cons."""
        segment = FeatureSpec("consonantal", FeatureValue(1))
        pattern = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        assert segment.matches_pattern(pattern) is False

    def test_negated_pattern_non_matching_value_matches(self, features):
        """Segment with -cons matches negated pattern !+cons."""
        segment = FeatureSpec("consonantal", FeatureValue(0))
        pattern = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        assert segment.matches_pattern(pattern) is True

    def test_plain_pattern_vs_negated_segment(self, features):
        """Plain pattern +cons does not match a negated segment."""
        segment = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        pattern = FeatureSpec("consonantal", FeatureValue(1))
        assert segment.matches_pattern(pattern) is False

    def test_both_negated_matching_values(self, features):
        """!+cons matches !+cons (double negation cancels)."""
        a = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        b = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        assert a.matches_pattern(b) is True

    def test_both_negated_non_matching_values(self, features):
        """!+cons does not match !-cons (double negation, but values differ)."""
        a = FeatureSpec("consonantal", FeatureValue(1), is_negated=True)
        b = FeatureSpec("consonantal", FeatureValue(0), is_negated=True)
        assert a.matches_pattern(b) is False

    def test_negated_contour_vs_contour(self, features):
        """Negated pattern inverts contour-vs-contour match."""
        segment = FeatureSpec("tone", FeatureValue([1, 3]))
        pattern = FeatureSpec("tone", FeatureValue([1, 3]), is_negated=True)
        assert segment.matches_pattern(pattern) is False

    def test_negated_single_vs_contour(self, features):
        """Negated single value inverts match against contour — value absent."""
        segment = FeatureSpec("tone", FeatureValue([1, 3]))
        pattern = FeatureSpec("tone", FeatureValue(5), is_negated=True)
        assert segment.matches_pattern(pattern) is True  # 5 not in [1,3], inverted → True

    def test_negated_single_vs_contour_matching(self, features):
        """Negated single value inverts match against contour — value present."""
        segment = FeatureSpec("tone", FeatureValue([1, 3]))
        pattern = FeatureSpec("tone", FeatureValue(1), is_negated=True)
        assert segment.matches_pattern(pattern) is False  # 1 in [1,3], inverted → False

    def test_negated_scalar(self, features):
        """Negation works with scalar values — different value."""
        segment = FeatureSpec("height", FeatureValue(3))
        pattern = FeatureSpec("height", FeatureValue(2), is_negated=True)
        assert segment.matches_pattern(pattern) is True

    def test_negated_scalar_matching(self, features):
        """Negation works with scalar values — same value."""
        segment = FeatureSpec("height", FeatureValue(2))
        pattern = FeatureSpec("height", FeatureValue(2), is_negated=True)
        assert segment.matches_pattern(pattern) is False


# ---------------------------------------------------------------------------
# matches_pattern — single vs contour (target=contour, pattern=single)
# ---------------------------------------------------------------------------


class TestMatchesSingleContour:
    def test_any_existential(self, features):
        pattern = FeatureSpec("tone", FeatureValue(1, "any"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is True

    def test_any_not_present(self, features):
        pattern = FeatureSpec("tone", FeatureValue(5, "any"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is False

    def test_initial_match(self, features):
        pattern = FeatureSpec("tone", FeatureValue(1, "initial"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is True

    def test_initial_no_match(self, features):
        pattern = FeatureSpec("tone", FeatureValue(3, "initial"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is False

    def test_final_match(self, features):
        pattern = FeatureSpec("tone", FeatureValue(3, "final"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is True

    def test_final_no_match(self, features):
        pattern = FeatureSpec("tone", FeatureValue(1, "final"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is False

    def test_all_match(self, features):
        pattern = FeatureSpec("tone", FeatureValue(3, "all"))
        target = FeatureSpec("tone", FeatureValue([3, 3]))
        assert target.matches_pattern(pattern) is True

    def test_all_not_uniform(self, features):
        pattern = FeatureSpec("tone", FeatureValue(3, "all"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is False

    def test_index_match(self, features):
        """Position 2 (one-indexed) = second slot; 3 at that slot in [1,3,5]."""
        pattern = FeatureSpec("tone", FeatureValue(3, 2))
        target = FeatureSpec("tone", FeatureValue([1, 3, 5]))
        assert target.matches_pattern(pattern) is True

    def test_index_out_of_range(self, features):
        pattern = FeatureSpec("tone", FeatureValue(3, 5))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is False

    def test_index_list_match(self, features):
        """Positions [1, 2] (one-indexed) = first and second slots."""
        pattern = FeatureSpec("tone", FeatureValue(1, [1, 2]))
        target = FeatureSpec("tone", FeatureValue([1, 1, 3]))
        assert target.matches_pattern(pattern) is True

    def test_index_list_partial_fail(self, features):
        pattern = FeatureSpec("tone", FeatureValue(1, [1, 2]))
        target = FeatureSpec("tone", FeatureValue([1, 3, 1]))
        assert target.matches_pattern(pattern) is False


# ---------------------------------------------------------------------------
# matches_pattern — contour vs contour
# ---------------------------------------------------------------------------


class TestMatchesContourContour:
    def test_any_existential(self, features):
        """Contour pattern [1, 3] fits at offset 0 in target [1, 3, 5]."""
        pattern = FeatureSpec("tone", FeatureValue([1, 3], "any"))
        target = FeatureSpec("tone", FeatureValue([1, 3, 5]))
        assert target.matches_pattern(pattern) is True

    def test_all_same_length(self, features):
        pattern = FeatureSpec("tone", FeatureValue([1, 3], "all"))
        target = FeatureSpec("tone", FeatureValue([1, 3]))
        assert target.matches_pattern(pattern) is True

    def test_all_different_length(self, features):
        pattern = FeatureSpec("tone", FeatureValue([1, 3], "all"))
        target = FeatureSpec("tone", FeatureValue([1, 3, 5]))
        assert target.matches_pattern(pattern) is False

    def test_initial(self, features):
        """Contour [1, 3] at initial position matches target [1, 3, 5]."""
        pattern = FeatureSpec("tone", FeatureValue([1, 3], "initial"))
        target = FeatureSpec("tone", FeatureValue([1, 3, 5]))
        assert target.matches_pattern(pattern) is True

    def test_final(self, features):
        """Contour [3, 5] at final position matches target [1, 3, 5]."""
        pattern = FeatureSpec("tone", FeatureValue([3, 5], "final"))
        target = FeatureSpec("tone", FeatureValue([1, 3, 5]))
        assert target.matches_pattern(pattern) is True


# ---------------------------------------------------------------------------
# form_contour
# ---------------------------------------------------------------------------


class TestFormContour:
    def test_int_plus_int(self, features):
        a = FeatureSpec("tone", FeatureValue(1))
        b = FeatureSpec("tone", FeatureValue(3))
        result = a.form_contour(b)
        assert result.value.value == [1, 3]

    def test_int_plus_contour(self, features):
        a = FeatureSpec("tone", FeatureValue(1))
        b = FeatureSpec("tone", FeatureValue([2, 3]))
        result = a.form_contour(b)
        assert result.value.value == [1, 2, 3]

    def test_contour_plus_int(self, features):
        a = FeatureSpec("tone", FeatureValue([1, 2]))
        b = FeatureSpec("tone", FeatureValue(3))
        result = a.form_contour(b)
        assert result.value.value == [1, 2, 3]

    def test_contour_plus_contour(self, features):
        a = FeatureSpec("tone", FeatureValue([1, 2]))
        b = FeatureSpec("tone", FeatureValue([3, 5]))
        result = a.form_contour(b)
        assert result.value.value == [1, 2, 3, 5]

    def test_different_features_raises(self, features):
        a = FeatureSpec("tone", FeatureValue(1))
        b = FeatureSpec("height", FeatureValue(3))
        with pytest.raises(ValueError, match="not the same"):
            a.form_contour(b)
