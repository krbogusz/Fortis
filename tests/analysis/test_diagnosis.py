"""Tests for the diagnosis layer (src/fortis/analysis/diagnosis.py)."""

from src.fortis.analysis.accuracy import AlignOp, DistanceToTarget, align
from src.fortis.analysis.diagnosis import (
    Confusion,
    StageDiagnosis,
    confusions,
    diagnose,
    diagnose_stages,
    error_contexts,
    errors_summary_line,
    f_score,
    phi_coefficient,
    render_error_context_csv,
    render_errors_csv,
)
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project


def _phones(form: str) -> tuple[str, ...]:
    """Split a form into one-char-per-phone for the diagnosis tests.

    Their forms are single-codepoint segments, so this stands in for the inventory
    ``form_phones`` — dropping structural marks.
    """
    return tuple(char for char in form if char not in ".-ˈˌ")


def _measure(derived: str, target: str, gloss: str = "") -> DistanceToTarget:
    """A DistanceToTarget for the diagnosis tests — phones the error tally aligns on."""
    from src.fortis.analysis.accuracy import edit_distance

    dp, tp = _phones(derived), _phones(target)
    return DistanceToTarget(
        gloss=gloss, ipa=derived, derived=derived, target=target,
        distance=edit_distance(dp, tp), derived_phones=dp, target_phones=tp,
    )


class TestAlign:
    def test_all_match(self):
        ops = align(["k", "a"], ["k", "a"])
        assert [o.kind for o in ops] == ["match", "match"]
        assert [o.target_index for o in ops] == [0, 1]

    def test_substitution_on_the_diagonal(self):
        # kata → kada: the t/d mismatch is one substitution, not delete+insert.
        ops = align(["k", "a", "t", "a"], ["k", "a", "d", "a"])
        assert [o.kind for o in ops] == ["match", "match", "sub", "match"]
        sub = ops[2]
        assert (sub.target, sub.derived, sub.target_index) == ("t", "d", 2)

    def test_deletion_carries_target_index_and_no_derived(self):
        # pata → ata: p is deleted; the deletion knows its target position, no derived one.
        ops = align(["p", "a", "t", "a"], ["a", "t", "a"])
        assert ops[0] == AlignOp("delete", "p", None, 0, None)

    def test_insertion_has_no_target_index(self):
        # ata → pata: p is inserted; it knows its derived position, no target one.
        ops = align(["a", "t", "a"], ["p", "a", "t", "a"])
        assert ops[0] == AlignOp("insert", None, "p", None, 0)

    def test_metathesis_reads_as_two_substitutions(self):
        # no transposition discount here (unlike edit_distance): ab → ba is two subs.
        ops = align(["a", "b"], ["b", "a"])
        assert [o.kind for o in ops] == ["sub", "sub"]


class TestConfusions:
    def test_tally_and_examples(self):
        # two t→d and one p→b across three inexact words.
        distances = (
            _measure("kada", "kata", "one"),
            _measure("mada", "mata", "two"),
            _measure("taba", "tapa", "three"),
        )
        table = confusions(distances)
        # each example label is "gloss: derived/attested"
        assert table[0] == Confusion("t", "d", 2, ("one: kada/kata", "two: mada/mata"))
        assert Confusion("p", "b", 1, ("three: taba/tapa",)) in table

    def test_exact_words_contribute_nothing(self):
        assert confusions((_measure("kata", "kata"),)) == []

    def test_deletion_and_insertion_kinds(self):
        deletion = confusions((_measure("ata", "pata"),))[0]
        assert deletion.expected == "p" and deletion.got is None and deletion.kind == "deletion"
        insertion = confusions((_measure("pata", "ata"),))[0]
        assert insertion.expected is None and insertion.got == "p" and insertion.kind == "insertion"

    def test_examples_capped_at_three(self):
        # five distinct words all showing d→t; examples (the "derived • target" labels) cap at 3
        distances = tuple(_measure(f"d{v}", f"t{v}", f"w{i}") for i, v in enumerate("aeiou"))
        assert len(confusions(distances)[0].examples) == 3

    def test_limit(self):
        distances = (_measure("da", "ta"), _measure("ba", "pa"), _measure("ga", "ka"))
        assert len(confusions(distances, limit=2)) == 2


class TestPhiCoefficient:
    def test_perfect_positive_association(self):
        # every predictor-present case is an error, every predictor-absent case correct.
        assert phi_coefficient(err_here=2, ok_here=0, err_away=0, ok_away=1) == 1.0

    def test_no_association_is_zero(self):
        assert phi_coefficient(1, 1, 1, 1) == 0.0

    def test_perfect_negative_association(self):
        assert phi_coefficient(err_here=0, ok_here=2, err_away=2, ok_away=0) == -1.0

    def test_zero_margin_is_zero_not_error(self):
        # a predictor present everywhere (no absent cases): coefficient undefined ⇒ 0.
        assert phi_coefficient(5, 5, 0, 0) == 0.0


class TestFScore:
    def test_perfect(self):
        # predictor present ⟺ error: precision = recall = 1 → F1 = 1.
        assert f_score(err_here=4, ok_here=0, err_away=0) == 1.0

    def test_harmonic_mean(self):
        # precision 4/(4+4)=0.5, recall 4/(4+4)=0.5 → F1 = 0.5.
        assert f_score(err_here=4, ok_here=4, err_away=4) == 0.5

    def test_zero_when_predictor_covers_no_error(self):
        assert f_score(err_here=0, ok_here=5, err_away=3) == 0.0

    def test_high_f_at_low_phi_is_possible(self):
        # Predictor present in 90% of sites, same 10% error rate present vs absent:
        # phi is exactly 0 (independence), but F1 stays healthy on recall alone —
        # the reason ranking is by phi, not F.
        assert f_score(err_here=9, ok_here=81, err_away=1) > 0.15
        assert phi_coefficient(9, 81, 1, 9) == 0.0


class TestErrorContexts:
    """A conditioned autopsy fixture with counts known by hand.

    Focus /t/ occurs five times: three after /a/ (all wrong: t→d) and twice after
    /i/ (both right). So among /t/, left=a perfectly predicts the error — phi 1.0,
    support 3 — while left=i perfectly predicts correctness.
    """

    def _grades(self):
        return (
            _measure("ada", "ata", "a1"),
            _measure("ada", "ata", "a2"),
            _measure("ada", "ata", "a3"),
            _measure("ita", "ita", "i1"),
            _measure("ita", "ita", "i2"),
        )

    def test_counts(self, project):
        autopsy = error_contexts(self._grades(), "t", project)
        assert (autopsy.phone, autopsy.errors, autopsy.total) == ("t", 3, 5)

    def test_left_a_perfectly_predicts_error(self, project):
        autopsy = error_contexts(self._grades(), "t", project)
        left_a = next(a for a in autopsy.associations if a.predictor == "left=a")
        assert left_a.phi == 1.0
        assert left_a.fscore == 1.0  # every /t/-after-/a/ is an error, and covers all errors
        assert (left_a.err_here, left_a.ok_here) == (3, 0)
        assert (left_a.err_away, left_a.ok_away) == (0, 2)
        assert left_a.support == 3

    def test_associations_sorted_most_error_associated_first(self, project):
        autopsy = error_contexts(self._grades(), "t", project)
        phis = [a.phi for a in autopsy.associations]
        assert phis == sorted(phis, reverse=True)

    def test_support_floor_drops_thin_predictors(self, project):
        # 'right=#' would mark the two /a/-final... but here focus /t/ never sits word-final;
        # a predictor present in fewer than the floor of positions must be absent.
        autopsy = error_contexts(self._grades(), "t", project)
        for a in autopsy.associations:
            assert a.support >= 3

    def test_insertions_never_enter_the_autopsy(self, project):
        # a spurious inserted /t/ has no target position (its target has no /t/ at all),
        # so it is not a /t/ trial.
        distances = (*self._grades(), _measure("taa", "aa", "ins"))
        autopsy = error_contexts(distances, "t", project)
        assert autopsy.total == 5  # unchanged by the insertion

    def test_too_few_errors_yields_no_associations(self, project):
        autopsy = error_contexts((_measure("ita", "ita"),), "t", project)
        assert autopsy.errors == 0 and autopsy.associations == ()

    def test_support_floor_scales_with_occurrences(self, project):
        # 50 occurrences of /t/: with the default 10%, the floor is max(3, ceil(5.0)) = 5,
        # so a predictor present in only 4 positions is dropped even though it clears the
        # absolute floor of 3 — the bar rises with the word base.
        distances = tuple(_measure("ada", "ata", f"a{i}") for i in range(46)) + tuple(
            _measure("ida", "ita", f"i{i}") for i in range(4)
        )
        autopsy = error_contexts(distances, "t", project)
        assert autopsy.total == 50
        assert autopsy.support_floor == 5
        predictors = {a.predictor for a in autopsy.associations}
        assert "left=a" in predictors  # support 46, kept
        assert "left=i" not in predictors  # support 4, below the scaled floor of 5


class TestDiagnose:
    def test_focuses_on_the_top_confusions_expected_phones(self, project):
        distances = (
            _measure("ada", "ata", "a1"),
            _measure("ada", "ata", "a2"),
            _measure("aba", "apa", "p1"),
        )
        autopsies = diagnose(distances, project, top=5)
        phones = [a.phone for a in autopsies]
        assert phones[0] == "t"  # the most frequent confusion's expected phone leads
        assert "p" in phones


class TestDiagnoseStages:
    def test_shape_ends_with_final(self):
        project = load_project().unwrap()  # fresh default, insulated from mutations
        stages = diagnose_stages(derive_all(project), project)
        assert stages, "expected at least the final stage"
        assert stages[-1].label == "final" and stages[-1].time is None
        assert all(isinstance(s, StageDiagnosis) for s in stages)


class TestRendering:
    def _grades(self):
        return (
            _measure("ada", "ata", "one"),
            _measure("ada", "ata", "two"),
            _measure("aba", "apa", "three"),
        )

    def _stages(self, project):
        # A one-stage-plus-final shape: reuse diagnose_stages' machinery via a hand-built
        # StageDiagnosis so the CSV renderers can be tested without a full project run.
        cf = tuple(confusions(self._grades()))
        autopsy = tuple(
            error_contexts(self._grades(), c.expected, project) for c in cf if c.expected
        )
        return [StageDiagnosis("300", 300, cf, autopsy), StageDiagnosis("final", None, cf, autopsy)]

    def test_errors_csv_header_and_rows(self, project):
        import csv

        rows = list(csv.reader(render_errors_csv(self._stages(project)).splitlines()))
        assert rows[0] == [
            "stage", "expected", "got", "count", "kind",
            "examples (gloss: derived vs. attested)",
        ]
        body = rows[1:]
        # The t→d substitution appears for each stage label (300 and final).
        td = [r for r in body if r[1] == "t" and r[2] == "d"]
        assert {r[0] for r in td} == {"300", "final"}
        assert td[0][3] == "2" and td[0][4] == "substitution"

    def test_errors_csv_marks_absent_side_with_null(self, project):
        stages = [StageDiagnosis("final", None, (Confusion("x", None, 1, ("w: ax/a",)),), ())]
        rows = list(__import__("csv").reader(render_errors_csv(stages).splitlines()))
        assert rows[1][:5] == ["final", "x", "∅", "1", "deletion"]

    def test_error_context_csv_header_and_shape(self, project):
        import csv

        rows = list(csv.reader(render_error_context_csv(self._stages(project)).splitlines()))
        assert rows[0] == [
            "stage", "segment", "environment", "assoc. (φ)", "F₁",
            "err/ok · with", "err/ok · without",
        ]
        # Every data row names a stage and a focus segment, and only positive-phi predictors.
        for r in rows[1:]:
            assert r[0] in {"300", "final"} and r[1]
            assert float(r[3]) > 0

    def test_summary_line_names_the_top_confusion(self, project):
        line = errors_summary_line(self._stages(project))
        assert "t→d" in line and "error site" in line

    def test_summary_line_when_all_exact(self):
        stages = [StageDiagnosis("final", None, (), ())]
        assert "no errors" in errors_summary_line(stages).lower()
