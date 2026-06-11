"""Tests for Bindings model."""

from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle


class TestBindings:
    def test_default_empty(self):
        b = Bindings()
        assert b.alpha == {}
        assert b.reference == {}

    def test_with_alpha(self):
        b = Bindings(alpha={"α": 1})
        assert b.alpha["α"] == 1

    def test_with_reference(self):
        bundle = FeatureBundle(voice=1)
        b = Bindings(reference={0: bundle})
        assert b.reference[0]["voice"] == 1

    def test_mutation(self):
        b = Bindings()
        b.alpha["α"] = 1
        b.reference[0] = FeatureBundle(nasal=0)
        assert b.alpha["α"] == 1
        assert b.reference[0]["nasal"] == 0