"""Tests for Bindings model."""

from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec


class TestBindings:
    def test_default_empty(self):
        b = Bindings()
        assert b.alpha == {}
        assert b.reference == {}

    def test_with_alpha(self):
        b = Bindings(alpha={"α": 1})
        assert b.alpha["α"] == 1

    def test_with_reference(self):
        voice = FeatureSpec(feature="voice", value=1)
        bundle = FeatureBundle(voice=voice)
        b = Bindings(reference={0: (bundle,)})
        assert b.reference[0][0]["voice"].value == 1

    def test_mutation(self):
        b = Bindings()
        b.alpha["α"] = 1
        nasal = FeatureSpec(feature="nasal", value=0)
        b.reference[0] = (FeatureBundle(nasal=nasal),)
        assert b.alpha["α"] == 1
        assert b.reference[0][0]["nasal"].value == 0
