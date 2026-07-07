"""Tests for the greedy boosting loop (src/fortis/induction/boost.py).

The integration test is synthetic single-interval recovery (plan §6.1): on a clean,
self-consistent interval the loop must drive the loss down monotonically with
recognizable, valid rules — the M1 milestone measure.
"""
from dataclasses import replace

import pytest

from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.induction.boost import induce_interval
from src.fortis.induction.intervals import Interval, build_interval, synthetic_project
from src.fortis.loaders.rules import load_rule
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.models.rules import RuleInventory


@pytest.fixture(scope="module")
def induced_750_1000(synth):
    """Induce the synthetic 750→1000 interval once (a fast, substitution-heavy interval).

    Runs with the escape ladder, shrink, and placement search off to keep the test fast —
    those are exercised by their own focused tests; this fixture validates the core loop.
    """
    synth = synthetic_project(synth)
    return induce_interval(
        build_interval(synth, 750, 1000), escape=False, shrink=False, placement=False
    )


class TestSyntheticRecovery:
    def test_loss_falls_and_accuracy_rises(self, induced_750_1000):
        result = induced_750_1000
        assert result.rules, "the loop should induce at least one rule"
        assert result.final_fit < result.start_fit
        assert result.final_exact > result.start_exact

    def test_every_step_strictly_lowers_loss(self, induced_750_1000):
        # The acceptance criterion is ΔL < 0 — no accepted rule may raise the loss.
        for step in induced_750_1000.steps:
            assert step.delta_l < 0
            assert step.fit_after <= step.fit_before

    def test_rule_count_is_frugal(self, induced_750_1000):
        # MDL keeps the induced cascade far smaller than the hand rules for the interval
        # (M1 bar: well under 2× the ~119 hand rules at these times).
        assert len(induced_750_1000.rules) <= 40

    def test_induced_rules_are_valid_notation(self, induced_750_1000, synth):
        # Every induced rule is a real Rule that re-loads from its own notation (round-trip).
        from src.fortis.loaders.rules import load_rule
        from src.fortis.result import Ok

        for rule in induced_750_1000.rules:
            match load_rule("r", {"definition": rule.raw_definition, "time": 0}, synth.features):
                case Ok(reloaded):
                    assert reloaded[0].sd is not None
                case _:
                    pytest.fail(f"induced rule did not re-parse: {rule.raw_definition!r}")

    def test_stop_reason_is_recorded(self, induced_750_1000):
        assert induced_750_1000.stopped in {"converged", "fit_zero", "max_rules"}


class TestExpressibleRecovery:
    """The decisive gate: when the target IS expressible in the v1 lattice, fit must reach 0.

    Generates a mini-lexicon by applying a handful of v1-expressible rules (unconditioned
    substitutions + a conditioned deletion) to real source forms, hides them, and induces. If
    the loop reaches ``fit_bits`` 0 here, it converges whenever expressivity suffices — so a
    non-zero residual on a *real* interval is a genuine expressivity/ordering limit, not the
    loop giving up early (and not the ``min_improved_words`` guard rejecting real gains).
    """

    def test_reaches_zero_fit_on_expressible_targets(self, synth):
        oracle = ["k → t", "o → u", "m → n"]
        rules = [
            load_rule("o", {"definition": d, "time": i}, synth.features).unwrap()[0]
            for i, d in enumerate(oracle)
        ]
        sources = [w.stages[-100] for w in synth.words.values() if -100 in w.stages][:120]
        generator = replace(
            synth,
            words=WordInventory({s: Word(ipa=s) for s in sources}),
            rules=RuleInventory({r.time: (r,) for r in rules}),
        )
        mini = {}
        for derivation in derive_all(generator):
            target = render_syllabified(
                lower_tiers(derivation.surface), derivation.surface_boundaries, synth
            )
            mini[derivation.word.ipa] = Word(ipa=derivation.word.ipa, final=target)
        interval = Interval(
            start=-100, end=750,
            project=replace(synth, words=WordInventory(mini), rules=RuleInventory()),
        )
        result = induce_interval(interval, escape=False)
        assert result.final_fit == pytest.approx(0.0)
        assert result.final_exact == result.assessed
        assert result.stopped == "fit_zero"


class TestShrink:
    """The shrink pass retires a redundant rule but never trades away exact accuracy."""

    def test_shrink_removes_a_dominated_duplicate(self, synth):
        # o→u then o→u again: the second is pure dead weight — shrink must drop exactly one.
        from src.fortis.induction.boost import _shrink
        from src.fortis.induction.objective import bits_model

        synth = synthetic_project(synth)
        interval = build_interval(synth, 750, 1000)
        rule = load_rule("o", {"definition": "o → u", "time": 0}, synth.features).unwrap()[0]
        dup = load_rule("o", {"definition": "o → u", "time": 1}, synth.features).unwrap()[0]
        kept, log = _shrink(interval.project, [rule, dup], bits_model(interval.project))
        assert len(kept) == 1
        assert len(log) == 1

    def test_shrink_keeps_a_load_bearing_rule(self, synth):
        # Two independent load-bearing rules (the 750→1000 interval's k→t and m→n): neither is
        # covered by the other, so shrink must keep both.
        from src.fortis.induction.boost import _shrink
        from src.fortis.induction.objective import bits_model

        synth = synthetic_project(synth)
        interval = build_interval(synth, 750, 1000)
        rule = load_rule("k", {"definition": "k → t", "time": 0}, synth.features).unwrap()[0]
        keep = load_rule("m", {"definition": "m → n", "time": 1}, synth.features).unwrap()[0]
        kept, _log = _shrink(interval.project, [rule, keep], bits_model(interval.project))
        assert len(kept) == 2


class TestDegenerateInterval:
    def test_interval_with_no_residual_induces_nothing(self, synth):
        # An interval whose source already equals its target (synthetic input→input) has zero
        # residual, so the loop induces nothing and stops immediately.
        synth = synthetic_project(synth)
        interval = build_interval(synth, 750, 1000)
        # Point every target at its own source: nothing to learn.
        for word in interval.project.words.values():
            word.final = word.ipa
        result = induce_interval(interval)
        assert result.rules == []
        assert result.stopped == "fit_zero"
