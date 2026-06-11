"""Tests for bundle and value parsing.

parse_value takes a raw token like '+', ':2', '1>0'.
parse_feature_bundle and parse_pattern_bundle use identify_feature
to split the feature name from the value.
"""

import pytest

from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.specs import PatternSpec
from src.fortis.models.values import AlphaOp, AlphaRef, ContourEdge
from src.fortis.parsing.bundles import (
    parse_feature_bundle,
    parse_pattern_bundle,
    parse_pattern_spec,
    parse_value,
)


class TestParseValue:
    """Tests for realized value parsing."""

    def test_unary_present(self, features):
        result = parse_value("+", "syllabic", features)
        assert result.is_ok()
        assert result.unwrap() == 1

    def test_binary_present(self, features):
        result = parse_value("+", "consonantal", features)
        assert result.is_ok()
        assert result.unwrap() == 1

    def test_binary_absent(self, features):
        result = parse_value("-", "consonantal", features)
        assert result.is_ok()
        assert result.unwrap() == 0

    def test_binary_numeric(self, features):
        result = parse_value("1", "consonantal", features)
        assert result.is_ok()
        assert result.unwrap() == 1

    def test_scalar_numeric_with_colon(self, features):
        result = parse_value(":2", "length", features)
        assert result.is_ok()
        assert result.unwrap() == 2

    def test_scalar_numeric_bare(self, features):
        result = parse_value("2", "length", features)
        assert result.is_ok()
        assert result.unwrap() == 2

    def test_contour_value(self, features):
        result = parse_value("1>0", "consonantal", features)
        assert result.is_ok()
        assert result.unwrap() == (1, 0)

    def test_unspecified(self, features):
        result = parse_value("∅", "consonantal", features)
        assert result.is_ok()
        assert result.unwrap() is None

    def test_alpha_in_realized_context(self, features):
        result = parse_value("α", "consonantal", features)
        assert result.is_err()

    def test_unknown_feature_raises(self, features):
        with pytest.raises(KeyError):
            parse_value("+", "nonexistent", features)


class TestParseFeatureBundle:
    """Tests for realized feature bundle parsing."""

    def test_simple_bundle(self, features):
        result = parse_feature_bundle("+syllabic, -consonantal", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["syllabic"] == 1
        assert bundle["consonantal"] == 0

    def test_scalar_in_bundle(self, features):
        result = parse_feature_bundle("stress:1", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["stress"] == 1

    def test_unknown_feature_error(self, features):
        result = parse_feature_bundle("+nonexistent", features)
        assert result.is_err()


class TestParsePatternSpec:
    """Tests for pattern spec parsing."""

    def test_simple_present(self, features):
        result = parse_pattern_spec("+nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.value == 1
        assert spec.negated is False

    def test_negated(self, features):
        result = parse_pattern_spec("!+nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.negated is True
        assert spec.value == 1

    def test_contour_position(self, features):
        result = parse_pattern_spec("tone:5@initial", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.contour_position == ContourEdge.initial

    def test_alpha_variable(self, features):
        result = parse_pattern_spec("αconsonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec.value, AlphaRef)
        assert spec.value.var == "α"
        assert spec.value.op == AlphaOp.same


class TestParsePatternBundle:
    """Tests for pattern bundle parsing."""

    def test_simple_pattern(self, features):
        result = parse_pattern_bundle("+syllabic, -consonantal", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "syllabic" in bundle
        assert bundle["syllabic"].value == 1
        assert bundle["consonantal"].value == 0

    def test_mixed_pattern(self, features):
        result = parse_pattern_bundle("+consonantal, stress:1", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "stress" in bundle