"""Tests for the append-scoring fast path (src/fortis/induction/evaluate.py).

The load-bearing test is :meth:`TestFastPathEquivalence` — that ``append_derivation`` produces
a assessed surface **byte-identical** to a real ``derive`` with the candidate genuinely appended,
including on the stress-tier-bearing Latin forms whose ``_maintain_tiers``/re-dock the fast path
must reproduce. If that holds, every ΔL the search reads is exact.
"""
from dataclasses import replace

import pytest

from src.fortis.analysis.accuracy import distance_to_target, form_phones
from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.induction.evaluate import IntervalState, timed_inventory
from src.fortis.induction.intervals import build_interval
from src.fortis.loaders.rules import load_rule


def _rule(project, definition: str):
    return load_rule("c", {"definition": definition, "time": 0}, project.features).unwrap()[0]


def _surface(derivation, project) -> str:
    return render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )


# Candidates that fire heavily on the -100 Latin forms, including a final-vowel deletion that
# strands stress (exercising the suprasegmental re-dock the fast path must mirror) and a bundle
# rule that changes a feature in place.
_CANDIDATES = [
    "t̪ → d̪",  # broad voicing
    "k → ∅",  # deletion
    "[+syllabic] → ∅ / _ #",  # final vowel loss — strands stress
    "s → ∅ / _ t̪",  # cluster simplification
    "[-syllabic, +voice] → [-voice]",  # feature rule via bundle
    "ˈɑ → ˈɛ",  # stressed vowel change
]
_BASE_LISTS = ["empty", "three"]


@pytest.fixture(scope="module")
def interval(synth):
    """The stress-heavy -100→750 interval mini-project."""
    return build_interval(synth, -100, 750)


class TestFastPathEquivalence:
    @pytest.mark.parametrize("base_name", _BASE_LISTS)
    @pytest.mark.parametrize("definition", _CANDIDATES)
    def test_append_matches_full_derive(self, synth, interval, base_name, definition):
        mini = interval.project
        base_rules = (
            []
            if base_name == "empty"
            else [_rule(synth, "m → n̪"), _rule(synth, "u → o"), _rule(synth, "rr → r")]
        )
        state = IntervalState(mini, base_rules)
        candidate = _rule(synth, definition)
        resolved = state._resolved(candidate)

        # Fast path: apply just the candidate to each cached derivation.
        fast = [state.append_derivation(base, resolved) for base in state.baseline]
        # Ground truth: derive the mini-lexicon with the candidate genuinely appended.
        real = derive_all(replace(mini, rules=timed_inventory(base_rules + [candidate])))

        for fast_d, real_d in zip(fast, real, strict=True):
            # The assessed segment sequence is identical (what the accuracy analysis compares).
            assert form_phones(fast_d.surface, synth) == form_phones(real_d.surface, synth)
            fast_g, real_g = distance_to_target(fast_d, synth), distance_to_target(real_d, synth)
            assert fast_g is not None and real_g is not None
            assert (fast_g.distance, fast_g.feature_distance) == (
                real_g.distance,
                real_g.feature_distance,
            )

    def test_a_firing_candidate_actually_moves_words(self, synth, interval):
        # Guard: the equivalence above would be vacuous if nothing ever fired.
        state = IntervalState(interval.project, [])
        resolved = state._resolved(_rule(synth, "[+syllabic] → ∅ / _ #"))
        moved = sum(
            1
            for base in state.baseline
            if state.append_derivation(base, resolved) is not base
        )
        assert moved > 0


class TestScoreAppend:
    def test_nonfiring_candidate_is_zero_delta(self, synth, interval):
        state = IntervalState(interval.project, [])
        # A rule whose target never occurs in the -100 forms: no word moves, no fit change.
        score = state.score_append(_rule(synth, "q → x"))
        assert score.moved == 0
        assert score.delta_fit == pytest.approx(0.0, abs=1e-9)
        # It still costs its own bits, so ΔL is strictly positive (MDL rejects it).
        assert score.delta_l > 0

    def test_score_matches_a_recomputed_fit_delta(self, synth, interval):
        # score_append's delta_fit must equal the fit change from a full re-derive.
        state = IntervalState(interval.project, [])
        from src.fortis.induction.objective import cascade_score

        candidate = _rule(synth, "t̪ → d̪")
        score = state.score_append(candidate)

        baseline = cascade_score(state.baseline, state.project)
        appended_project = replace(state.project, rules=timed_inventory([candidate]))
        appended = cascade_score(derive_all(appended_project), appended_project)
        expected_delta_fit = appended.fit_bits - baseline.fit_bits
        assert score.delta_fit == pytest.approx(expected_delta_fit, abs=1e-6)

    def test_accept_updates_baseline(self, synth, interval):
        state = IntervalState(interval.project, [])
        before = state.baseline_fit
        candidate = _rule(synth, "t̪ → d̪")
        score = state.score_append(candidate)
        state.accept(candidate)
        assert len(state.rules) == 1
        assert state.baseline_fit == pytest.approx(before + score.delta_fit, abs=1e-6)


class TestPlacement:
    """Placement search: correct by construction.

    It reduces to the append fast path at the append index, and every non-append placement is a
    real spliced re-derive — so it inherits the fast path's byte-identical proof.
    """

    def test_score_at_append_equals_score_append(self, synth, interval):
        state = IntervalState(interval.project, [_rule(synth, "eː → e"), _rule(synth, "o → u")])
        candidate = _rule(synth, "k → t")
        at_append = state.score_at(candidate, len(state.rules))
        appended = state.score_append(candidate)
        assert at_append.delta_l == pytest.approx(appended.delta_l, abs=1e-9)

    def test_accept_at_matches_a_fresh_spliced_derive(self, synth, interval):
        base = [_rule(synth, "eː → e"), _rule(synth, "o → u"), _rule(synth, "k → t")]
        state = IntervalState(interval.project, base)
        candidate = _rule(synth, "s → ∅ / _ #")
        state.accept_at(candidate, 1)  # insert before index 1
        spliced = base[:1] + [candidate] + base[1:]
        fresh = derive_all(replace(state.project, rules=timed_inventory(spliced)))
        for cached, reference in zip(state.baseline, fresh, strict=True):
            assert cached.surface == reference.surface

    def test_score_at_interior_reports_a_real_delta(self, synth, interval):
        # A candidate spliced at the start re-derives the whole cascade; its Δfit must equal
        # the fit change a fresh derive of that spliced cascade gives.
        from src.fortis.induction.objective import cascade_score

        base = [_rule(synth, "eː → e"), _rule(synth, "o → u")]
        state = IntervalState(interval.project, base)
        candidate = _rule(synth, "t̪ → d̪")
        score = state.score_at(candidate, 0)
        spliced = [candidate, *base]
        spliced_project = replace(state.project, rules=timed_inventory(spliced))
        expected = cascade_score(derive_all(spliced_project), spliced_project)
        assert score.delta_fit == pytest.approx(expected.fit_bits - state.baseline_fit, abs=1e-6)
