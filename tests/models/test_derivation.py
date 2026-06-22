"""Tests for DerivationStep and Derivation."""

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.specs import FeatureSpec


class TestDerivationStep:
    def test_construction(self):
        voice_1 = FeatureSpec(feature="voice", value=1)
        voice_0 = FeatureSpec(feature="voice", value=0)
        before = FeatureBundle(voice=voice_1)
        step = DerivationStep(before=before, rule="r1", change="voicing", after=FeatureBundle(voice=voice_0))
        assert step.rule == "r1"
        assert step.before["voice"].value == 1
        assert step.after["voice"].value == 0


class TestDerivation:
    def test_construction(self):
        d = Derivation(word="test", input=FeatureBundle(), steps=(), surface=FeatureBundle())
        assert d.word == "test"
        assert d.steps == ()

    def test_with_steps(self):
        voice_1 = FeatureSpec(feature="voice", value=1)
        voice_0 = FeatureSpec(feature="voice", value=0)
        step = DerivationStep(
            before=FeatureBundle(voice=voice_1),
            rule="r1",
            change="voicing",
            after=FeatureBundle(voice=voice_0),
        )
        d = Derivation(word="test", input=FeatureBundle(), steps=(step,), surface=FeatureBundle())
        assert len(d.steps) == 1