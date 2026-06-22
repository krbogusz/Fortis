"""Tests for spec types."""

from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import ContourEdge


class TestFeatureSpec:
    def test_with_value(self):
        spec = FeatureSpec(feature="voice", value=1)
        assert spec.feature == "voice"
        assert spec.value == 1

    def test_with_none_value(self):
        spec = FeatureSpec(feature="nasal", value=None)
        assert spec.feature == "nasal"
        assert spec.value is None

    def test_with_contour_value(self):
        spec = FeatureSpec(feature="tone", value=(1, 0, 1))
        assert spec.feature == "tone"
        assert spec.value == (1, 0, 1)


class TestPatternSpec:
    def test_defaults(self):
        spec = PatternSpec(feature="nasal", value=1)
        assert spec.feature == "nasal"
        assert spec.value == 1
        assert spec.negated is False
        assert spec.contour_position == ContourEdge.any

    def test_explicit_values(self):
        spec = PatternSpec(feature="consonantal", value=0, negated=True, contour_position=ContourEdge.initial)
        assert spec.feature == "consonantal"
        assert spec.value == 0
        assert spec.negated is True
        assert spec.contour_position == ContourEdge.initial

    def test_contour_value(self):
        spec = PatternSpec(feature="tone", value=(1, 0))
        assert spec.value == (1, 0)

    def test_none_value(self):
        spec = PatternSpec(feature="voice", value=None)
        assert spec.value is None


class TestResultSpec:
    def test_with_value(self):
        spec = ResultSpec(feature="voice", value=1)
        assert spec.feature == "voice"
        assert spec.value == 1

    def test_none_value_means_unlink(self):
        spec = ResultSpec(feature="voice", value=None)
        assert spec.value is None