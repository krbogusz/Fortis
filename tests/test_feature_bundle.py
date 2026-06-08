"""Tests for FeatureBundle — parsing, matching, diffing, combining."""

from __future__ import annotations

import pytest

from src.fortis.parsing import parse_feature_bundle
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_value import FeatureValue
from tests.conftest import make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# parse_feature_bundle
# ---------------------------------------------------------------------------


class TestFromStr:
    def test_single_feature(self, features):
        result = parse_feature_bundle("+cons", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle

    def test_comma_separated(self, features):
        result = parse_feature_bundle("+cons, -syll", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "syllabic" in bundle

    def test_semicolon_separated(self, features):
        result = parse_feature_bundle("+cons; -syll", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "syllabic" in bundle

    def test_scalar_label(self, features):
        result = parse_feature_bundle("height: high", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["height"].value == 3

    def test_contour_value(self, features):
        result = parse_feature_bundle("tone: 1>3", features)
        assert result.is_ok()
        assert result.unwrap()["tone"].value == [1, 3]

    def test_bare_unary(self, features):
        result = parse_feature_bundle("nasal", features)
        assert result.is_ok()
        assert result.unwrap()["nasal"].value == 1

    def test_invalid_feature(self, features):
        result = parse_feature_bundle("+unknown", features)
        assert result.is_err()

    def test_mixed_valid_and_invalid(self, features):
        result = parse_feature_bundle("+cons, +unknown", features)
        assert result.is_err()

    def test_empty_string(self, features):
        result = parse_feature_bundle("", features)
        assert result.is_ok()
        assert len(result.unwrap()) == 0

    def test_whitespace_handling(self, features):
        result = parse_feature_bundle("  +cons  ,  -syll  ", features)
        assert result.is_ok()


# ---------------------------------------------------------------------------
# match_exact
# ---------------------------------------------------------------------------


class TestMatchExact:
    def test_identical(self, features):
        a = parse_feature_bundle("+cons, -syll", features).unwrap()
        b = parse_feature_bundle("+cons, -syll", features).unwrap()
        assert a.matches_exactly(b) is True

    def test_different_keys(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("+cons, -syll", features).unwrap()
        assert a.matches_exactly(b) is False

    def test_different_values(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("-cons", features).unwrap()
        assert a.matches_exactly(b) is False


# ---------------------------------------------------------------------------
# differing
# ---------------------------------------------------------------------------


class TestDiffering:
    def test_identical(self, features):
        a = parse_feature_bundle("+cons, -syll", features).unwrap()
        b = parse_feature_bundle("+cons, -syll", features).unwrap()
        assert a.differing(b) == []

    def test_value_diff(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("-cons", features).unwrap()
        assert "consonantal" in a.differing(b)

    def test_missing_feature(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("+cons, +nasal", features).unwrap()
        diff = a.differing(b)
        assert "nasal" in diff

    def test_extra_feature(self, features):
        a = parse_feature_bundle("+cons, +nasal", features).unwrap()
        b = parse_feature_bundle("+cons", features).unwrap()
        diff = a.differing(b)
        assert "nasal" in diff


# ---------------------------------------------------------------------------
# combine_with
# ---------------------------------------------------------------------------


class TestCombineWith:
    def test_merge_new_feature(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("+nasal", features).unwrap()
        result = a.combine_with(b)
        assert "consonantal" in result
        assert "nasal" in result

    def test_merge_overrides(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("-cons", features).unwrap()
        result = a.combine_with(b)
        assert result["consonantal"].value == 0

    def test_preserves_unmentioned(self, features):
        a = parse_feature_bundle("+cons, -syll", features).unwrap()
        b = parse_feature_bundle("+nasal", features).unwrap()
        result = a.combine_with(b)
        assert result["syllabic"].value == 0
        assert result["nasal"].value == 1

    def test_form_contours(self, features):
        a = parse_feature_bundle("tone: 1", features).unwrap()
        b = parse_feature_bundle("tone: 3", features).unwrap()
        result = a.combine_with(b, form_contours=True)
        assert result["tone"].value == [1, 3]

    def test_no_form_contours(self, features):
        a = parse_feature_bundle("tone: 1", features).unwrap()
        b = parse_feature_bundle("tone: 3", features).unwrap()
        result = a.combine_with(b, form_contours=False)
        assert result["tone"].value == 3  # overridden, not appended

    def test_original_unchanged(self, features):
        a = parse_feature_bundle("+cons", features).unwrap()
        b = parse_feature_bundle("-cons", features).unwrap()
        _ = a.combine_with(b)
        assert a["consonantal"].value == 1  # original bundle unchanged
