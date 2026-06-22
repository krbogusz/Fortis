"""Tests for bundle types."""

from src.fortis.models.bundles import FeatureBundle, PatternBundle, ResultBundle
from src.fortis.models.specs import FeatureSpec, PatternSpec, ResultSpec
from src.fortis.models.values import ContourEdge


class TestFeatureBundle:
    def test_creation(self):
        bundle = FeatureBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        bundle = FeatureBundle()
        spec = FeatureSpec(feature="voice", value=1)
        bundle["voice"] = spec
        assert bundle["voice"] == spec
        assert bundle["voice"].value == 1

    def test_update(self):
        voice = FeatureSpec(feature="voice", value=1)
        nasal = FeatureSpec(feature="nasal", value=0)
        bundle = FeatureBundle(voice=voice, nasal=nasal)
        assert bundle["voice"].value == 1
        assert bundle["nasal"].value == 0

    def test_dict_operations(self):
        voice = FeatureSpec(feature="voice", value=1)
        bundle = FeatureBundle(voice=voice)
        assert "voice" in bundle
        assert len(bundle) == 1
        del bundle["voice"]
        assert len(bundle) == 0

    def test_iteration(self):
        voice = FeatureSpec(feature="voice", value=1)
        nasal = FeatureSpec(feature="nasal", value=0)
        bundle = FeatureBundle(voice=voice, nasal=nasal)
        keys = list(bundle.keys())
        assert set(keys) == {"voice", "nasal"}

    def test_contour_value(self):
        tone = FeatureSpec(feature="tone", value=(1, 0, 1))
        bundle = FeatureBundle()
        bundle["tone"] = tone
        assert bundle["tone"].value == (1, 0, 1)


class TestPatternBundle:
    def test_creation(self):
        bundle = PatternBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        spec = PatternSpec(feature="voice", value=1)
        bundle = PatternBundle()
        bundle["voice"] = spec
        assert bundle["voice"] == spec
        assert bundle["voice"].value == 1

    def test_negated_spec(self):
        spec = PatternSpec(feature="voice", value=1, negated=True)
        bundle = PatternBundle(voice=spec)
        assert bundle["voice"].negated is True


class TestResultBundle:
    def test_creation(self):
        bundle = ResultBundle()
        assert len(bundle) == 0

    def test_set_and_get(self):
        spec = ResultSpec(feature="voice", value=1)
        bundle = ResultBundle()
        bundle["voice"] = spec
        assert bundle["voice"].value == 1

    def test_unlink_value(self):
        spec = ResultSpec(feature="voice", value=None)
        bundle = ResultBundle(voice=spec)
        assert bundle["voice"].value is None