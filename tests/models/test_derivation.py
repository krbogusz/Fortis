"""Tests for DerivationStep and Derivation."""

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep


class TestDerivationStep:
    def test_construction(self):
        before = FeatureBundle(voice=1)
        step = DerivationStep(before=before, rule="r1", change="voicing", after=FeatureBundle(voice=0))
        assert step.rule == "r1"
        assert step.before["voice"] == 1
        assert step.after["voice"] == 0


class TestDerivation:
    def test_construction(self):
        d = Derivation(word="test", input=FeatureBundle(), steps=(), surface=FeatureBundle())
        assert d.word == "test"
        assert d.steps == ()

    def test_with_steps(self):
        step = DerivationStep(
            before=FeatureBundle(voice=1),
            rule="r1",
            change="voicing",
            after=FeatureBundle(voice=0),
        )
        d = Derivation(word="test", input=FeatureBundle(), steps=(step,), surface=FeatureBundle())
        assert len(d.steps) == 1