"""Tests for rule blame (src/fortis/analysis/blame.py).

Uses the real Latin→French project — it has genuinely wrong words with attributable
residuals — rather than synthesising Derivations by hand.
"""

from pathlib import Path

import pytest

from src.fortis.analysis.blame import blame_all, blame_summary_line, blame_word, render_blame
from src.fortis.analysis.grading import grade, split_phones
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project


@pytest.fixture(scope="module")
def latin():
    return load_project(Path("projects/latin_to_french")).unwrap()


@pytest.fixture(scope="module")
def derivs(latin):
    return derive_all(latin)


@pytest.fixture(scope="module")
def blames(derivs, latin):
    return blame_all(derivs, latin)


class TestInvariants:
    def test_blame_distance_equals_grader_distance(self, blames, derivs, latin):
        graded = {g.gloss: g.distance for g in grade(derivs, latin).grades}
        for blame in blames:
            assert blame.distance == graded[blame.gloss]

    def test_trajectory_endpoint_is_the_surface(self, blames):
        # The final trajectory point is derivation.surface, so its distance is the grade.
        for blame in blames:
            assert blame.trajectory[-1].label == "surface"
            assert blame.trajectory[-1].distance == blame.distance

    def test_only_wrong_words_are_blamed(self, blames):
        assert blames  # Latin has wrong words
        for blame in blames:
            assert blame.distance > 0
            assert blame.residuals  # a wrong word has at least one residual


class TestTrajectoryTargets:
    def test_targets_track_the_attested_stage(self, derivs, latin):
        # connaître carries stages -200,-100,750,1000,1200,1400 + final.
        d = next(dv for dv in derivs if dv.word.gloss == "connaître")
        blame = blame_word(d, latin)
        stages, times = d.word.stages, sorted(d.word.stages)
        # The input heads to the earliest attested stage; the surface is the final.
        assert blame.trajectory[0].label == "input"
        assert blame.trajectory[0].target == stages[times[0]]
        assert blame.trajectory[-1].label == "surface" and blame.trajectory[-1].target == d.word.final
        # A timed step targets the earliest stage at or after its rule-time (else final).
        for point in blame.trajectory:
            if point.time is None:
                continue
            expected = next((stages[t] for t in times if t >= point.time), d.word.final)
            assert point.target == expected
        # d and fd are both computed (the final form segments).
        assert blame.trajectory[-1].feature_distance is not None

    def test_no_stages_targets_everything_to_final(self, derivs, latin):
        # A wrong word without attested stages compares every point to the final.
        d = next((dv for dv in derivs if not dv.word.stages and blame_word(dv, latin)), None)
        if d is not None:  # the latin lexicon may or may not have such a word
            blame = blame_word(d, latin)
            assert all(p.target == d.word.final for p in blame.trajectory)


class TestProvenance:
    def test_culprits_are_rules_that_fired_on_that_word(self, blames, derivs):
        # Provenance may only name a rule that actually fired on the word in question.
        by_gloss = {d.word.gloss: d for d in derivs}
        for blame in blames:
            fired = {step.rule.id for step in by_gloss[blame.gloss].steps}
            for residual in blame.residuals:
                if residual.culprit is not None:
                    assert residual.culprit in fired

    def test_summary_line_names_a_culprit(self, blames):
        line = blame_summary_line(blames)
        assert "wrong word(s)" in line


class TestStructure:
    def test_exact_word_is_not_blamed(self, derivs, latin):
        # Find an exactly-derived word (there are hundreds) — it gets no blame.
        blamed = {b.gloss for b in blame_all(derivs, latin)}
        exact = next(d for d in derivs if d.word.final and d.word.gloss not in blamed)
        assert blame_word(exact, latin) is None

    def test_word_without_target_is_not_blamed(self, derivs, latin):
        target_less = next((d for d in derivs if d.word.final is None), None)
        if target_less is not None:
            assert blame_word(target_less, latin) is None

    def test_render_has_sections_and_caveat(self, blames):
        md = render_blame(blames, "`proj`")
        assert "# Blame" in md
        assert "notation artifact" in md  # the stage caveat
        assert "Residuals:" in md

    def test_render_empty_is_short(self):
        md = render_blame([], "`proj`")
        assert "nothing to blame" in md.lower()
        assert "Residuals:" not in md


class TestUnattributable:
    """When a surface phone doesn't map 1:1 to a segment (a tie-bar affricate is one
    segment but two phones), attribution is dropped rather than blaming a misaligned
    rule. (Stress marks no longer trigger this — they're dropped before comparison.)"""

    def test_split_phones_splits_a_tie_bar_affricate(self):
        # The invariant the guard protects against: 'd͡ʒ' is one segment, two phones.
        assert split_phones("d͡ʒa") == ["d͡", "ʒ", "a"]

    def test_residuals_degrade_when_phones_exceed_segments(self):
        from src.fortis.analysis.blame import _residuals
        from src.fortis.models.bundles import FeatureBundle
        from src.fortis.models.derivation import Derivation
        from src.fortis.models.form import Form
        from src.fortis.models.inventories import Word
        from src.fortis.models.segment import Segment

        # A surface of two segments that renders to three phones (the affricate splits).
        surface_form = Form(segments=[Segment(FeatureBundle(), 0), Segment(FeatureBundle(), 1)])
        derivation = Derivation(word=Word(ipa="x", gloss="x"), input=surface_form,
                                steps=(), surface=surface_form)
        residuals = _residuals(derivation, target="ka", surface="d͡ʒa")

        assert residuals
        assert all(not r.attributed for r in residuals)  # attribution dropped, not guessed
        assert all(r.culprit is None for r in residuals)
        assert all(r.kind != "omission" for r in residuals)  # not mislabelled
