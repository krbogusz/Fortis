"""Tests for src.fortis.models.feature_bundle — parsing, matching, diffing, combining."""

from __future__ import annotations

import pytest

from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_value import FeatureValue
from tests.conftest import make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# from_str
# ---------------------------------------------------------------------------


class TestFromStr:
    def test_single_feature(self, features):
        result = FeatureBundle.from_string("+cons", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle

    def test_comma_separated(self, features):
        result = FeatureBundle.from_string("+cons, -syll", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "syllabic" in bundle

    def test_semicolon_separated(self, features):
        result = FeatureBundle.from_string("+cons; -syll", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "syllabic" in bundle

    def test_scalar_label(self, features):
        result = FeatureBundle.from_string("height: high", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["height"].value.value == 3

    def test_contour_value(self, features):
        result = FeatureBundle.from_string("tone: 1>3", features)
        assert result.is_ok()
        assert result.unwrap()["tone"].value.value == [1, 3]

    def test_bare_unary(self, features):
        result = FeatureBundle.from_string("nasal", features)
        assert result.is_ok()
        assert result.unwrap()["nasal"].value.value == 1

    def test_invalid_feature(self, features):
        result = FeatureBundle.from_string("+unknown", features)
        assert result.is_err()

    def test_mixed_valid_and_invalid(self, features):
        result = FeatureBundle.from_string("+cons, +unknown", features)
        assert result.is_err()

    def test_empty_string(self, features):
        result = FeatureBundle.from_string("", features)
        assert result.is_ok()
        assert len(result.unwrap()) == 0

    def test_whitespace_handling(self, features):
        result = FeatureBundle.from_string("  +cons  ,  -syll  ", features)
        assert result.is_ok()

    def test_negated_feature(self, features):
        result = FeatureBundle.from_string("!+cons", features)
        assert result.is_ok()
        spec = result.unwrap()["consonantal"]
        assert spec.is_negated is True
        assert spec.value.value == 1

    def test_mixed_negated_and_plain(self, features):
        result = FeatureBundle.from_string("!+cons, -syll", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["consonantal"].is_negated is True
        assert bundle["syllabic"].is_negated is False


# ---------------------------------------------------------------------------
# match_pattern
# ---------------------------------------------------------------------------


class TestMatchPattern:
    def test_subset_matches(self, features):
        segment = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        pattern = FeatureBundle.from_string("+cons", features).unwrap()
        assert segment.matches_pattern(pattern) is True

    def test_missing_feature_fails(self, features):
        segment = FeatureBundle.from_string("+cons", features).unwrap()
        pattern = FeatureBundle.from_string("+cons, +nasal", features).unwrap()
        assert segment.matches_pattern(pattern) is False

    def test_value_mismatch_fails(self, features):
        segment = FeatureBundle.from_string("+cons, +syll", features).unwrap()
        pattern = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        assert segment.matches_pattern(pattern) is False

    def test_empty_pattern_matches_anything(self, features):
        segment = FeatureBundle.from_string("+cons", features).unwrap()
        pattern = FeatureBundle()
        assert segment.matches_pattern(pattern) is True

    def test_absent_feature_never_satisfies(self, features):
        """A feature entirely absent from the segment never satisfies a positive pattern."""
        segment = FeatureBundle.from_string("+cons", features).unwrap()
        pattern = FeatureBundle.from_string("+nasal", features).unwrap()
        assert segment.matches_pattern(pattern) is False

    def test_none_value_does_not_match(self, features):
        """A None value in the segment does not satisfy a pattern requiring a specific value."""
        segment = FeatureBundle({"consonantal": FeatureSpec("consonantal", FeatureValue(None))})
        pattern = FeatureBundle.from_string("+cons", features).unwrap()
        assert segment.matches_pattern(pattern) is False


# ---------------------------------------------------------------------------
# match_pattern — negation
# ---------------------------------------------------------------------------


class TestMatchPatternNegation:
    def test_negated_pattern_matches_different_value(self, features):
        """Segment with -cons matches pattern !+cons."""
        segment = FeatureBundle.from_string("-cons", features).unwrap()
        pattern = FeatureBundle.from_string("!+cons", features).unwrap()
        assert segment.matches_pattern(pattern) is True

    def test_negated_pattern_does_not_match_same_value(self, features):
        """Segment with +cons does not match pattern !+cons."""
        segment = FeatureBundle.from_string("+cons", features).unwrap()
        pattern = FeatureBundle.from_string("!+cons", features).unwrap()
        assert segment.matches_pattern(pattern) is False

    def test_negated_pattern_with_other_features(self, features):
        """Negated feature in pattern with other non-negated features."""
        segment = FeatureBundle.from_string("-cons, +syll", features).unwrap()
        pattern = FeatureBundle.from_string("!+cons, +syll", features).unwrap()
        assert segment.matches_pattern(pattern) is True

    def test_negated_pattern_fails_on_other_feature(self, features):
        """Negated feature matches but other feature in pattern doesn't."""
        segment = FeatureBundle.from_string("-cons, -syll", features).unwrap()
        pattern = FeatureBundle.from_string("!+cons, +syll", features).unwrap()
        assert segment.matches_pattern(pattern) is False


# ---------------------------------------------------------------------------
# negated
# ---------------------------------------------------------------------------


class TestNegated:
    def test_flips_all_flags(self, features):
        bundle = FeatureBundle.from_string("!+cons, -syll", features).unwrap()
        result = bundle.negated()
        assert result["consonantal"].is_negated is False
        assert result["syllabic"].is_negated is True

    def test_double_negation_restores(self, features):
        bundle = FeatureBundle.from_string("!+cons, -syll", features).unwrap()
        assert bundle.negated().negated() == bundle

    def test_preserves_values(self, features):
        bundle = FeatureBundle.from_string("!+cons, height:2", features).unwrap()
        result = bundle.negated()
        assert result["consonantal"].value.value == 1
        assert result["height"].value.value == 2

    def test_does_not_mutate_original(self, features):
        bundle = FeatureBundle.from_string("+cons", features).unwrap()
        result = bundle.negated()
        assert bundle["consonantal"].is_negated is False
        assert result["consonantal"].is_negated is True


# ---------------------------------------------------------------------------
# match_exact
# ---------------------------------------------------------------------------


class TestMatchExact:
    def test_identical(self, features):
        a = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        b = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        assert a.matches_exactly(b) is True

    def test_different_keys(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        assert a.matches_exactly(b) is False

    def test_different_values(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("-cons", features).unwrap()
        assert a.matches_exactly(b) is False


# ---------------------------------------------------------------------------
# differing
# ---------------------------------------------------------------------------


class TestDiffering:
    def test_identical(self, features):
        a = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        b = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        assert a.differing(b) == []

    def test_value_diff(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("-cons", features).unwrap()
        assert "consonantal" in a.differing(b)

    def test_missing_feature(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("+cons, +nasal", features).unwrap()
        diff = a.differing(b)
        assert "nasal" in diff

    def test_extra_feature(self, features):
        a = FeatureBundle.from_string("+cons, +nasal", features).unwrap()
        b = FeatureBundle.from_string("+cons", features).unwrap()
        diff = a.differing(b)
        assert "nasal" in diff


# ---------------------------------------------------------------------------
# combine_with
# ---------------------------------------------------------------------------


class TestCombineWith:
    def test_merge_new_feature(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("+nasal", features).unwrap()
        result = a.combine_with(b)
        assert "consonantal" in result
        assert "nasal" in result

    def test_merge_overrides(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("-cons", features).unwrap()
        result = a.combine_with(b)
        assert result["consonantal"].value.value == 0

    def test_preserves_unmentioned(self, features):
        a = FeatureBundle.from_string("+cons, -syll", features).unwrap()
        b = FeatureBundle.from_string("+nasal", features).unwrap()
        result = a.combine_with(b)
        assert result["syllabic"].value.value == 0
        assert result["nasal"].value.value == 1

    def test_form_contours(self, features):
        a = FeatureBundle.from_string("tone: 1", features).unwrap()
        b = FeatureBundle.from_string("tone: 3", features).unwrap()
        result = a.combine_with(b, form_contours=True)
        assert result["tone"].value.value == [1, 3]

    def test_no_form_contours(self, features):
        a = FeatureBundle.from_string("tone: 1", features).unwrap()
        b = FeatureBundle.from_string("tone: 3", features).unwrap()
        result = a.combine_with(b, form_contours=False)
        assert result["tone"].value.value == 3  # overridden, not appended

    def test_original_unchanged(self, features):
        a = FeatureBundle.from_string("+cons", features).unwrap()
        b = FeatureBundle.from_string("-cons", features).unwrap()
        _ = a.combine_with(b)
        assert a["consonantal"].value.value == 1  # original bundle unchanged
