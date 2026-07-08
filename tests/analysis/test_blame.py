"""Tests for rule blame (src/fortis/analysis/blame.py).

Uses the real Latin→French project — it has genuinely wrong words with attributable
residuals — rather than synthesising Derivations by hand.
"""

import csv
from pathlib import Path

import pytest

from src.fortis.analysis.accuracy import ingest_targets, measure_accuracy
from src.fortis.analysis.blame import (
    blame_all,
    blame_summary_line,
    blame_word,
    render_blame,
    render_blame_csv,
)
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project


@pytest.fixture(scope="module")
def latin():
    return load_project(Path("projects/latin_to_french")).unwrap()


@pytest.fixture(scope="module")
def derivs(latin):
    ds = derive_all(latin)
    ingest_targets(ds, latin)  # blame + the grader read the segmented attested forms
    return ds


@pytest.fixture(scope="module")
def blames(derivs, latin):
    return blame_all(derivs, latin)


class TestInvariants:
    def test_blame_distance_equals_grader_distance(self, blames, derivs, latin):
        # Key by ipa, the unique identifier — glosses can repeat across the lexicon.
        assessed = {g.ipa: g.distance for g in measure_accuracy(derivs, latin).distances}
        for blame in blames:
            assert blame.distance == assessed[blame.ipa]

    def test_trajectory_endpoint_is_the_surface(self, blames):
        # The final trajectory point is derivation.surface, so its distance is the measurement.
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
        # Any word carrying several attested stages plus a final (picked structurally rather
        # than by name, so it doesn't depend on a specific entry being in the lexicon).
        d = max(
            (dv for dv in derivs
             if dv.word.stages and dv.word.final is not None and blame_word(dv, latin)),
            key=lambda dv: (len(dv.word.stages), dv.word.ipa),
        )
        blame = blame_word(d, latin)
        assert blame is not None  # d was chosen for a non-empty blame
        stages, times = d.word.stages, sorted(d.word.stages)
        # The input heads to the earliest attested stage; the surface is the final.
        assert blame.trajectory[0].label == "input"
        assert blame.trajectory[0].target == stages[times[0]]
        assert blame.trajectory[-1].label == "surface"
        assert blame.trajectory[-1].target == d.word.final
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
            assert blame is not None  # d was chosen for a non-empty blame
            assert all(p.target == d.word.final for p in blame.trajectory)


class TestProvenance:
    def test_culprits_are_rules_that_fired_on_that_word(self, blames, derivs):
        # Provenance may only name a rule that actually fired on the word in question.
        by_ipa = {d.word.ipa: d for d in derivs}  # ipa is unique; glosses can repeat
        for blame in blames:
            fired = {step.rule.id for step in by_ipa[blame.ipa].steps}
            for residual in blame.residuals:
                if residual.culprit is not None:
                    assert residual.culprit in fired

    def test_summary_line_names_a_culprit(self, blames):
        line = blame_summary_line(blames)
        assert "wrong word(s)" in line


class TestStructure:
    def test_exact_word_is_not_blamed_by_default(self, derivs, latin):
        # By default an exactly-derived word (there are hundreds) gets no blame.
        blamed = {b.ipa for b in blame_all(derivs, latin)}  # ipa is unique; glosses can repeat
        exact = next(d for d in derivs if d.word.final and d.word.ipa not in blamed)
        assert blame_word(exact, latin) is None

    def test_include_exact_blames_every_assessed_word(self, derivs, latin):
        # include_exact adds the exact words (distance 0, no residual) to the wrong ones.
        wrong = blame_all(derivs, latin)
        every = blame_all(derivs, latin, include_exact=True)
        assert len(every) > len(wrong)
        exact = [b for b in every if b.distance == 0]
        assert exact and all(not b.residuals for b in exact)  # exact ⇒ no residual

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

    def test_csv_has_header_and_a_row_per_trajectory_point(self, derivs, latin):
        blames = blame_all(derivs, latin, include_exact=True)
        rows = list(csv.reader(render_blame_csv(blames).splitlines()))
        assert rows[0] == ["gloss", "step", "t", "form", "target", "d", "fd"]
        assert len(rows) == 1 + sum(len(b.trajectory) for b in blames)  # header + one row/point
        # Every data row carries a gloss and a step label.
        assert all(r[0] and r[1] for r in rows[1:])


