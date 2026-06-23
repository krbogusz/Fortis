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

    def test_bare_non_unary_realized_feature_rejected(self, features):
        """A bare binary feature in realized context is invalid (pattern-only)."""
        result = parse_feature_spec("nasal", features)
        assert result.is_err()
        assert "explicit value" in result.unwrap_err()

    def test_bare_unary_realized_feature_ok(self, features):
        """A bare unary feature resolves to present (1), not 'any'."""
        result = parse_feature_spec("manner", features)
        assert result.is_ok()
        assert result.unwrap().value == 1

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

    def test_negated_bare_feature(self, features):
        # '!nasal' = complement of the bare "present" feature (matches none).
        result = parse_pattern_spec("!nasal", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "nasal"
        assert spec.value == "any"
        assert spec.negated is True

    def test_negated_bare_unary_feature(self, features):
        result = parse_pattern_spec("!manner", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.value == 1
        assert spec.negated is True

    def test_alpha_other_is_value_level_not_spec_negation(self, features):
        # '!α' is the alpha-other value (AlphaOp.other), NOT spec negation.
        result = parse_pattern_spec("voice: !α", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.negated is False
        assert isinstance(spec.value, AlphaRef)
        assert spec.value.op == AlphaOp.other

    def test_alpha_other_limb_in_contour(self, features):
        result = parse_pattern_spec("tone: !α>2", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.negated is False
        assert spec.value[0] == AlphaRef("α", AlphaOp.other)
        assert spec.value[1] == 2

    def test_conditional_feature(self, features):
        result = parse_pattern_spec("<1: +high>", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "high"
        assert spec.value == 1
        assert spec.condition_label == 1

    def test_conditional_negated_condition(self, features):
        # '<n: !F>' — negation rides on the inner spec parse.
        result = parse_pattern_spec("<1: !high>", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.negated is True
        assert spec.condition_label == 1

    def test_conditional_alpha_condition(self, features):
        result = parse_pattern_spec("<2: αvoice>", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert isinstance(spec.value, AlphaRef)
        assert spec.value.op == AlphaOp.same
        assert spec.condition_label == 2

    def test_conditional_contour_inner(self, features):
        # The closing '>' must not be confused with a contour limb separator.
        result = parse_pattern_spec("<1: tone: 1>2>", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "tone"
        assert spec.value == (1, 2)
        assert spec.condition_label == 1

    def test_conditional_unconditional_has_no_label(self, features):
        spec = parse_pattern_spec("+high", features).unwrap()
        assert spec.condition_label is None

    def test_conditional_missing_closing_bracket(self, features):
        assert parse_pattern_spec("<1: +high", features).is_err()

    def test_conditional_non_integer_label(self, features):
        assert parse_pattern_spec("<x: +high>", features).is_err()

    def test_opposite_alpha_on_binary_ok(self, features):
        result = parse_pattern_spec("voice: -α", features)
        assert result.is_ok()
        assert result.unwrap().value == AlphaRef("α", AlphaOp.opposite)

    def test_opposite_alpha_on_scalar_rejected(self, features):
        # '-α' (opposite) is binary only — scalar/unary have no single value-opposite.
        result = parse_pattern_spec("tone: -α", features)
        assert result.is_err()
        assert "Alpha-opposite" in result.unwrap_err()

    def test_opposite_alpha_on_unary_rejected(self, features):
        # '-α' on a unary (privative) feature is rejected too — present has no opposite.
        result = parse_pattern_spec("manner: -α", features)
        assert result.is_err()
        assert "Alpha-opposite" in result.unwrap_err()

    def test_opposite_alpha_scalar_contour_limb_rejected(self, features):
        assert parse_pattern_spec("tone: 1>-α", features).is_err()

    def test_same_and_other_alpha_on_scalar_ok(self, features):
        # 'α' (same) and '!α' (other) remain valid on scalar features.
        assert parse_pattern_spec("tone: α", features).is_ok()
        assert parse_pattern_spec("tone: !α", features).is_ok()


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

    def test_comma_separates_features(self, features):
        result = parse_pattern_bundle("+nasal, +voice", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert set(bundle) == {"nasal", "voice"}

    def test_semicolon_does_not_separate_features(self, features):
        # ';' is reserved for contour-position index lists, not feature separation.
        result = parse_pattern_bundle("+nasal; +voice", features)
        assert result.is_err()

    def test_semicolon_contour_position_in_bundle(self, features):
        # A multi-limb contour with a ';'-list position survives bundle splitting.
        result = parse_pattern_bundle("+nasal, tone: 1>2@2;3", features)
        assert result.is_ok()
        bundle = result.unwrap()
        assert set(bundle) == {"nasal", "tone"}
        assert bundle["tone"].value == (1, 2)
        assert bundle["tone"].contour_position == (2, 3)


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
        assert "negation" in result.unwrap_err()

    def test_rejects_contour_position(self, features):
        result = parse_result_spec("tone:1@initial", features)
        assert result.is_err()

    def test_conditional_feature(self, features):
        result = parse_result_spec("<1: +high>", features)
        assert result.is_ok()
        spec = result.unwrap()
        assert spec.feature == "high"
        assert spec.value == 1
        assert spec.condition_label == 1

    def test_conditional_rejects_negated_condition(self, features):
        # A result conditional cannot be negated — the inner runs through
        # parse_result_spec, which forbids '!'.
        assert parse_result_spec("<1: !high>", features).is_err()

    def test_rejects_other_alpha(self, features):
        """Result spec should reject '!α' (other) notation with its own message."""
        result = parse_result_spec("!αconsonantal", features)
        assert result.is_err()
        assert "'other' alpha" in result.unwrap_err()

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

    def test_opposite_alpha_on_scalar_rejected(self, features):
        # '-α' (opposite) is binary only — also enforced result-side.
        result = parse_result_spec("tone: -α", features)
        assert result.is_err()
        assert "Alpha-opposite" in result.unwrap_err()

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