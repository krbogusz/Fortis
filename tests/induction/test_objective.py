"""Tests for the MDL bits objective (src/fortis/induction/objective.py)."""

from dataclasses import replace

import pytest

from src.fortis.analysis.accuracy import DistanceToTarget
from src.fortis.application.deriving import derive_all
from src.fortis.induction.intervals import synthetic_project
from src.fortis.induction.objective import (
    B_RULE,
    bits_model,
    cascade_rule_bits,
    cascade_score,
    residual_bits,
    rule_bits,
)
from src.fortis.loaders.rules import load_rule
from src.fortis.models.rules import RuleInventory


def _phones(form: str) -> tuple[str, ...]:
    """Base + combining marks per phone (the old codepoint split), for these synthetic forms."""
    import unicodedata

    out: list[str] = []
    for char in form:
        if char in ".-ˈˌ" or char.isspace():
            continue
        if out and unicodedata.category(char) in {"Mn", "Mc", "Lm", "Sk"}:
            out[-1] += char
        else:
            out.append(char)
    return tuple(out)


def _measure(target: str, derived: str) -> DistanceToTarget:
    return DistanceToTarget(
        gloss="w", ipa=target, derived=derived, target=target, distance=0,
        derived_phones=_phones(derived), target_phones=_phones(target),
    )


class TestBitsModel:
    def test_constants_are_positive(self, synth):
        model = bits_model(synth)
        assert model.b_site > 0
        assert model.b_feat > 0
        assert model.letter_bits > 0
        assert model.mean_features > 0

    def test_b_feat_scales_with_feature_count(self, synth):
        # More feature names ⇒ more bits to name one feature.
        model = bits_model(synth)
        assert model.b_feat == pytest.approx(
            __import__("math").log2(len(synth.features))
            + __import__("math").log2(
                sum(max(len(f.values), 1) for f in synth.features.values())
                / len(synth.features)
            )
        )


class TestResidualBits:
    def test_exact_word_costs_nothing(self, synth):
        assert residual_bits(_measure("avɑ", "avɑ"), synth) == 0.0

    def test_substitution_costs_a_site_plus_feature_delta(self, synth):
        model = bits_model(synth)
        # A one-phone near miss: t vs d differ only by voice → one site + a small delta.
        bits = residual_bits(_measure("t", "d"), synth, model, {})
        assert bits > model.b_site  # more than a bare site
        assert bits < model.b_site + model.b_feat * model.mean_features  # less than a full spell

    def test_deletion_costs_more_than_insertion(self, synth):
        model = bits_model(synth)
        cache: dict = {}
        # target has a phone the derived lacks (deletion): spell it.
        deletion = residual_bits(_measure("at", "a"), synth, model, cache)
        # derived has a spurious phone (insertion): site only.
        insertion = residual_bits(_measure("a", "at"), synth, model, cache)
        assert deletion > insertion
        assert insertion == pytest.approx(model.b_site)

    def test_unsegmentable_phone_falls_back_not_crashes(self, synth):
        # A symbol the project cannot segment must degrade to the mean-feature spell, not raise.
        model = bits_model(synth)
        bits = residual_bits(_measure("💥", "a"), synth, model, {})
        assert bits == pytest.approx(model.b_site + model.b_feat * model.mean_features)


class TestRuleBits:
    def test_worked_example_matches_plan(self, synth):
        # Plan §1.2 worked example: b → a / _ # ≈ 31 bits.
        rule = load_rule("r", {"definition": "b → a / _ #", "time": 0}, synth.features).unwrap()[0]
        assert rule_bits(rule, synth) == pytest.approx(31, abs=6)

    def test_longer_context_costs_more(self, synth):
        model = bits_model(synth)
        short = load_rule("r", {"definition": "b → a", "time": 0}, synth.features).unwrap()[0]
        longer = load_rule(
            "r", {"definition": "b → a / n _ t", "time": 0}, synth.features
        ).unwrap()[0]
        assert rule_bits(longer, synth, model) > rule_bits(short, synth, model)

    def test_header_is_the_floor(self, synth):
        # Even the emptiest rule pays the header.
        rule = load_rule("r", {"definition": "b → a", "time": 0}, synth.features).unwrap()[0]
        assert rule_bits(rule, synth) > B_RULE


class TestCascadeScore:
    def test_hand_beats_identity(self, synth, synth_derivations):
        hand = cascade_score(synth_derivations, synth)
        identity_project = replace(synth, rules=RuleInventory())
        identity = cascade_score(derive_all(identity_project), identity_project)
        # The hand cascade must fit far better, and win on total loss despite its rule cost.
        assert hand.fit_bits < identity.fit_bits
        assert hand.total < identity.total
        assert identity.rule_bits == 0.0
        assert hand.exact > identity.exact

    def test_hand_cascade_is_self_consistent_on_synthetic(self, synth):
        # The learnability floor (§6.1): on its own machine-generated lexicon the hand cascade
        # has zero residual and perfect accuracy.
        synth = synthetic_project(synth)
        score = cascade_score(derive_all(synth), synth)
        assert score.fit_bits == pytest.approx(0.0)
        assert score.exact == score.assessed
        assert score.mean_distance == pytest.approx(0.0)

    def test_cascade_rule_bits_sums_every_rule(self, synth):
        model = bits_model(synth)
        expected = sum(
            rule_bits(rule, synth, model)
            for rules in synth.rules.values()
            for rule in rules
        )
        assert cascade_rule_bits(synth, model) == pytest.approx(expected)
