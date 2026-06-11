"""Tests for spec types."""

from src.fortis.models.specs import PatternSpec, ResultSpec
from src.fortis.models.values import ContourEdge


class TestPatternSpec:
    def test_defaults(self):
        spec = PatternSpec(value=1)
        assert spec.value == 1
        assert spec.negated is False
        assert spec.contour_position == ContourEdge.any

    def test_explicit_values(self):
        spec = PatternSpec(value=0, negated=True, contour_position=ContourEdge.initial)
        assert spec.value == 0
        assert spec.negated is True
        assert spec.contour_position == ContourEdge.initial

    def test_contour_value(self):
        spec = PatternSpec(value=(1, 0))
        assert spec.value == (1, 0)

    def test_none_value(self):
        spec = PatternSpec(value=None)
        assert spec.value is None


class TestResultSpec:
    def test_with_value(self):
        spec = ResultSpec(value=1)
        assert spec.value == 1

    def test_none_value_means_unlink(self):
        spec = ResultSpec(value=None)
        assert spec.value is None