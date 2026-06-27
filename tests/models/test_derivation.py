"""Tests for DerivationStep and Derivation."""

from typing import cast

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.form import Form
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule
from src.fortis.models.specs import FeatureSpec


class TestDerivationStep:
    def test_construction(self):
        voice_1 = FeatureSpec(feature="voice", value=1)
        voice_0 = FeatureSpec(feature="voice", value=0)
        before = FeatureBundle(voice=voice_1)
        step = DerivationStep(
            before=Form.from_bundles([before]),
            rule=cast("Rule", "r1"),
            after=Form.from_bundles([FeatureBundle(voice=voice_0)]),
        )
        assert step.rule == "r1"
        assert step.before.bundles()[0]["voice"].value == 1
        assert step.after.bundles()[0]["voice"].value == 0


class TestDerivation:
    def test_construction(self):
        d = Derivation(
            word=cast("Word", "test"),
            input=Form.from_bundles([]),
            steps=(),
            surface=Form.from_bundles([]),
        )
        assert d.word == "test"
        assert d.steps == ()

    def test_with_steps(self):
        voice_1 = FeatureSpec(feature="voice", value=1)
        voice_0 = FeatureSpec(feature="voice", value=0)
        step = DerivationStep(
            before=Form.from_bundles([FeatureBundle(voice=voice_1)]),
            rule=cast("Rule", "r1"),
            after=Form.from_bundles([FeatureBundle(voice=voice_0)]),
        )
        d = Derivation(
            word=cast("Word", "test"),
            input=Form.from_bundles([]),
            steps=(step,),
            surface=Form.from_bundles([]),
        )
        assert len(d.steps) == 1
