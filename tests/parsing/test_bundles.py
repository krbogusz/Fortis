"""Tests for bundle and value parsing."""

from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import AlphaOp, AlphaRef, ContourEdge
from src.fortis.parsing.bundles import (
    parse_feature_bundle,
    parse_feature_spec,
    parse_pattern_bundle,
    parse_pattern_spec,
    parse_result_spec,
)


class TestParseValue:
    """Tests for realized value parsing."""

    def test_unary_present(self, features):
        result = parse_feature_spec("+syllabic", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec, FeatureSpec)
        assert spec.feature == "syllabic"
        assert spec.value == 1

    def test_binary_present(self, features):
        result = parse_feature_spec("+consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == 1

    def test_binary_absent(self, features):
        result = parse_feature_spec("-consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == 0

    def test_binary_numeric(self, features):
        result = parse_feature_spec("1", features, feature="consonantal")
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == 1

    def test_scalar_numeric_with_colon(self, features):
        result = parse_feature_spec(":2", features, feature="length")
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "length"
        assert spec.value == 2

    def test_scalar_numeric_bare(self, features):
        result = parse_feature_spec("2", features, feature="length")
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "length"
        assert spec.value == 2

    def test_contour_value(self, features):
        result = parse_feature_spec("1>0", features, feature="consonantal")
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == (1, 0)

    def test_unspecified(self, features):
        result = parse_feature_spec("∅", features, feature="consonantal")
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value is None

    def test_alpha_in_realized_context(self, features):
        result = parse_feature_spec("αconsonantal", features)
        assert result.is_err()

    def test_unknown_feature_returns_error(self, features):
        result = parse_feature_spec("+", features, feature="nonexistent")
        assert result.is_err()

    def test_unary_name_only(self, features):
        """A plain unary feature name with no value should default to 1."""
        result = parse_feature_spec("manner", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "manner"
        assert spec.value == 1

    def test_binary_name_defaults_to_any(self, features):
        """A plain binary feature name with no value should default to 'any'."""
        result = parse_feature_spec("nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "nasal"
        assert spec.value == "any"

    def test_binary_name_with_plus(self, features):
        result = parse_feature_spec("+consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == 1


class TestParseFeatureBundle:
    """Tests for realized feature bundle parsing."""

    def test_single_feature(self, features):
        result = parse_feature_bundle("+voice", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "voice" in bundle
        assert bundle["voice"].value == 1

    def test_scalar_in_bundle(self, features):
        result = parse_feature_bundle("stress:1", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "stress" in bundle
        assert bundle["stress"].value == 1

    def test_unknown_feature_error(self, features):
        result = parse_feature_bundle("+nonexistent", features)
        assert result.is_err()

    def test_multi_feature_bundle(self, features):
        """Multi-feature bundles should parse correctly (was previously buggy)."""
        result = parse_feature_bundle("+voice, -nasal", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "voice" in bundle
        assert "nasal" in bundle
        assert bundle["voice"].value == 1
        assert bundle["nasal"].value == 0

    def test_multi_feature_with_scalar(self, features):
        result = parse_feature_bundle("+voice, stress:1", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert bundle["voice"].value == 1
        assert bundle["stress"].value == 1


class TestParsePatternSpec:
    """Tests for pattern spec parsing."""

    def test_simple_present(self, features):
        result = parse_pattern_spec("+nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec, PatternSpec)
        assert spec.feature == "nasal"
        assert spec.value == 1
        assert spec.negated is False

    def test_absent(self, features):
        result = parse_pattern_spec("-nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "nasal"
        assert spec.value == 0

    def test_contour_position(self, features):
        result = parse_pattern_spec("tone:5@initial", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "tone"
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
        result = parse_pattern_bundle("+nasal", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "nasal" in bundle
        assert bundle["nasal"].value == 1

    def test_mixed_pattern(self, features):
        result = parse_pattern_bundle("+consonantal", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle


class TestParseResultSpec:
    """Tests for result spec parsing."""

    def test_simple_present(self, features):
        result = parse_result_spec("+nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec, ResultSpec)
        assert spec.feature == "nasal"
        assert spec.value == 1

    def test_absent(self, features):
        result = parse_result_spec("-consonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == 0

    def test_rejects_negation(self, features):
        result = parse_result_spec("!nasal", features)
        assert result.is_err()

    def test_rejects_contour_position(self, features):
        result = parse_result_spec("tone:1@initial", features)
        assert result.is_err()

    def test_rejects_other_alpha(self, features):
        """Result spec should reject '!α' (other) notation."""
        result = parse_result_spec("!αconsonantal", features)
        assert result.is_err()

    def test_alpha_same(self, features):
        result = parse_result_spec("αconsonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec.value, AlphaRef)
        assert spec.value.op == AlphaOp.same

    def test_alpha_opposite(self, features):
        result = parse_result_spec("-αconsonantal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec.value, AlphaRef)
        assert spec.value.op == AlphaOp.opposite

    def test_scalar_numeric(self, features):
        result = parse_result_spec("stress:1", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "stress"
        assert spec.value == 1

    def test_contour_value(self, features):
        result = parse_result_spec("consonantal:1>0", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "consonantal"
        assert spec.value == (1, 0)

    def test_unspecified_with_plain_name_non_unary(self, features):
        """Non-unary feature with no value should error in result context."""
        result = parse_result_spec("consonantal", features)
        assert result.is_err()