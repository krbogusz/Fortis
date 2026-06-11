"""Tests for bundle types."""

from src.fortis.models.bundles import FeatureBundle, PatternBundle, ResultBundle
from src.fortis.models.specs import PatternSpec, ResultSpec
from src.fortis.models.values import ContourEdge


class TestFeatureBundle:
    def test_creation(self):
        bundle = FeatureBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        bundle = FeatureBundle()
        bundle["voice"] = 1
        assert bundle["voice"] == 1

    def test_update(self):
        bundle = FeatureBundle(voice=1, nasal=0)
        assert bundle["voice"] == 1
        assert bundle["nasal"] == 0

    def test_dict_operations(self):
        bundle = FeatureBundle(voice=1)
        assert "voice" in bundle
        assert len(bundle) == 1
        del bundle["voice"]
        assert len(bundle) == 0

    def test_iteration(self):
        bundle = FeatureBundle(voice=1, nasal=0)
        keys = list(bundle.keys())
        assert set(keys) == {"voice", "nasal"}

    def test_contour_value(self):
        bundle = FeatureBundle()
        bundle["tone"] = (1, 0, 1)
        assert bundle["tone"] == (1, 0, 1)


class TestPatternBundle:
    def test_creation(self):
        bundle = PatternBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        spec = PatternSpec(value=1)
        bundle = PatternBundle()
        bundle["voice"] = spec
        assert bundle["voice"] == spec
        assert bundle["voice"].value == 1

    def test_negated_spec(self):
        spec = PatternSpec(value=1, negated=True)
        bundle = PatternBundle(voice=spec)
        assert bundle["voice"].negated is True


class TestResultBundle:
    def test_creation(self):
        bundle = ResultBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        spec = ResultSpec(value=1)
        bundle = ResultBundle()
        bundle["voice"] = spec
        assert bundle["voice"].value == 1

    def test_unlink_value(self):
        spec = ResultSpec(value=None)
        bundle = ResultBundle(voice=spec)
        assert bundle["voice"].value is None