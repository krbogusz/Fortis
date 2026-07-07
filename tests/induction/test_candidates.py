"""Tests for candidate generation (src/fortis/induction/candidates.py)."""

from src.fortis.induction.candidates import propose
from src.fortis.induction.correspond import ContextPredictor, Correspondence


def _predictor(side: str, element: str, phi: float = 0.9) -> ContextPredictor:
    return ContextPredictor(
        side=side, element=element, phi=phi, fscore=0.0,
        change_here=5, stay_here=0, change_away=0, stay_away=5,
    )


class TestPropose:
    def test_substitution_emits_unconditioned_and_conditioned(self, synth):
        corr = Correspondence(
            expected="u", got="o", count=8, delta=2,
            predictors=(_predictor("right", "t"), _predictor("left", "[+nasal]")),
        )
        definitions = {c.definition for c in propose(corr, synth)}
        assert "o → u" in definitions  # tier 1, unconditioned
        assert "o → u / _ t" in definitions  # tier 2, right predictor
        assert "o → u / [+nasal] _" in definitions  # tier 2, left predictor
        assert "o → u / [+nasal] _ t" in definitions  # tier 3, pair

    def test_every_candidate_parses(self, synth):
        corr = Correspondence(
            expected="u", got="o", count=8, delta=2,
            predictors=(_predictor("right", "t"), _predictor("right", "#")),
        )
        for candidate in propose(corr, synth):
            assert len(candidate.rules) == 1  # v1 lattice is single-rule
            assert candidate.rules[0].sd is not None

    def test_deletion_requires_a_context(self, synth):
        # A spurious derived phone → a deletion rule, never unconditioned (policy §2.2).
        corr = Correspondence(
            expected=None, got="o", count=8, delta=None,
            predictors=(_predictor("right", "#"),),
        )
        definitions = {c.definition for c in propose(corr, synth)}
        assert "o → ∅" not in definitions
        assert "o → ∅ / _ #" in definitions

    def test_unsegmentable_literal_yields_no_candidates(self, synth):
        # A stray tie-bar fragment doesn't segment as a lone literal, so can't be a rule literal.
        corr = Correspondence(expected="s", got="t͡", count=5, delta=1, predictors=())
        assert propose(corr, synth) == []

    def test_cap_is_respected(self, synth):
        many = tuple(_predictor("right", f"[aperture: {v}]") for v in ("low", "mid", "high"))
        corr = Correspondence(expected="u", got="o", count=8, delta=2, predictors=many)
        candidates = propose(corr, synth)
        assert len(candidates) <= synth.settings.induction.contexts_per_confusion
