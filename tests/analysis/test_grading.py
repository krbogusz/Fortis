"""Tests for the accuracy analysis (src/fortis/analysis/accuracy.py)."""

from src.fortis.analysis import main as grade_cli
from src.fortis.analysis.accuracy import (
    AccuracyReport,
    DistanceToTarget,
    StageAccuracy,
    accuracy_by_stage,
    distance_to_target,
    edit_distance,
    feature_diff,
    feature_edit_distance,
    ingest_targets,
    measure_accuracy,
)
from src.fortis.analysis.reporting import (
    accuracy_summary_line,
    render_accuracy_csv,
    render_distance_to_target_csv,
)
from src.fortis.application.deriving import derive_all, form_at_time
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec


def _bundle(**features) -> FeatureBundle:
    bundle = FeatureBundle()
    for feature, value in features.items():
        bundle[feature] = FeatureSpec(feature=feature, value=value)
    return bundle


class TestEditDistance:
    def test_identical(self):
        assert edit_distance(["a", "b", "c"], ["a", "b", "c"]) == 0

    def test_substitution(self):
        assert edit_distance(["a", "b"], ["a", "c"]) == 1

    def test_insertion_and_deletion(self):
        assert edit_distance(["a", "c"], ["a", "b", "c"]) == 1
        assert edit_distance(["a", "b", "c"], ["a", "c"]) == 1

    def test_empty_operands(self):
        assert edit_distance([], []) == 0
        assert edit_distance([], ["a", "b"]) == 2
        assert edit_distance(["a", "b"], []) == 2

    def test_adjacent_transposition_is_one_edit(self):
        # a swap costs 1, not the 2 substitutions plain Levenshtein would charge
        assert edit_distance(["a", "b"], ["b", "a"]) == 1
        assert edit_distance(["k", "ʁ", "e"], ["k", "e", "ʁ"]) == 1

    def test_transposition_within_a_longer_word(self):
        assert edit_distance(["p", "a", "r", "t"], ["p", "r", "a", "t"]) == 1

    def test_transposition_cost_is_tunable(self):
        assert edit_distance(["a", "b"], ["b", "a"], transposition_cost=2) == 2


class TestFeatureDiff:
    def test_identical(self):
        assert feature_diff(_bundle(cons=1, voice=1), _bundle(cons=1, voice=1)) == 0

    def test_differing_value_counts_once(self):
        assert feature_diff(_bundle(cons=1, voice=1), _bundle(cons=1, voice=0)) == 1

    def test_present_vs_absent_counts_once(self):
        assert feature_diff(_bundle(cons=1), _bundle(cons=1, nasal=1)) == 1

    def test_none_value_is_treated_as_absent(self):
        assert feature_diff(_bundle(cons=1, nasal=None), _bundle(cons=1)) == 0

    def test_multiple_differences(self):
        assert feature_diff(_bundle(cons=1, voice=1), _bundle(cons=0, voice=0, nasal=1)) == 3


class TestFeatureEditDistance:
    def test_identical_sequences(self):
        seq = [_bundle(cons=1, voice=1), _bundle(cons=0)]
        assert feature_edit_distance(seq, seq) == 0

    def test_substitution_costs_feature_diff(self):
        a = [_bundle(cons=1, voice=1)]
        b = [_bundle(cons=1, voice=0)]
        assert feature_edit_distance(a, b) == 1

    def test_indel_costs_segment_feature_count(self):
        seg = _bundle(cons=1, voice=1, nasal=1)  # 3 features
        assert feature_edit_distance([seg], []) == 3
        assert feature_edit_distance([], [seg]) == 3

    def test_substitution_preferred_over_indel_for_similar_segments(self):
        # deleting + inserting the differing segment would cost size+size; a
        # one-feature substitution must win.
        a = [_bundle(cons=1, voice=1), _bundle(cons=0, back=1)]
        b = [_bundle(cons=1, voice=0), _bundle(cons=0, back=1)]
        assert feature_edit_distance(a, b) == 1

    def test_finer_than_phone_distance(self):
        # a near-miss (one feature) scores below a gross miss, where a phone
        # distance would flatten both to 1.
        base = _bundle(cons=1, voice=1, nasal=0)
        near = _bundle(cons=1, voice=1, nasal=1)  # 1 feature off
        far = _bundle(cons=0, voice=0, nasal=1)  # 3 features off
        assert feature_edit_distance([base], [near]) < feature_edit_distance([base], [far])

    def test_metathesis_of_identical_segments_costs_one(self):
        # swapping two adjacent, featurally-identical segments is one edit — not
        # the 2 × feature_diff two substitutions would charge.
        x = _bundle(cons=1, voice=1, back=1)
        y = _bundle(cons=0, voice=1, back=0)
        assert feature_diff(x, y) == 2
        assert feature_edit_distance([x, y], [y, x]) == 1  # not 4

    def test_transposition_cost_is_tunable(self):
        x = _bundle(cons=1, back=1)
        y = _bundle(cons=0, back=0)
        assert feature_edit_distance([x, y], [y, x], transposition_cost=3) == 3

    def test_no_transposition_discount_when_swapped_pair_also_differs(self):
        # only an exact reorder gets the discount; a swap that also changes a
        # feature falls back to substitutions.
        x = _bundle(cons=1, voice=1)
        y = _bundle(cons=0, voice=1)
        y2 = _bundle(cons=0, voice=0)  # like y but a feature off
        # [x, y] -> [y2, x]: not a clean metathesis (y2 != y)
        plain = feature_edit_distance([x, y], [y2, x])
        assert plain > 1


class TestGradeAggregates:
    def _report(self, distances, skipped=0, feature_distances=None):
        feature_distances = feature_distances or [None] * len(distances)
        distances = tuple(
            DistanceToTarget(
                gloss=f"w{i}", ipa=f"i{i}", derived="x", target="x",
                distance=d, feature_distance=fd,
            )
            for i, (d, fd) in enumerate(zip(distances, feature_distances, strict=True))
        )
        return AccuracyReport(distances=distances, skipped=skipped)

    def test_counts(self):
        report = self._report([0, 0, 1, 2], skipped=3)
        assert report.assessed == 4
        assert report.exact == 2
        assert report.within_one == 3  # distances 0, 0, 1
        assert report.total_distance == 3
        assert report.skipped == 3

    def test_ratios(self):
        report = self._report([0, 0, 1, 2])
        assert report.accuracy == 0.5
        assert report.mean_distance == 0.75

    def test_empty_report_is_safe(self):
        report = self._report([])
        assert report.assessed == 0
        assert report.accuracy == 0.0
        assert report.mean_distance == 0.0
        assert report.mean_feature_distance == 0.0

    def test_feature_aggregates_skip_unsegmentable(self):
        # two words with feature distances, one unsegmentable (None).
        report = self._report([0, 1, 2], feature_distances=[0, 3, None])
        assert report.feature_assessed == 2
        assert report.unsegmentable == 1
        assert report.total_feature_distance == 3
        assert report.mean_feature_distance == 1.5  # (0 + 3) / 2, None excluded

    def test_grade_exact_property(self):
        assert DistanceToTarget("w", "i", "x", "x", 0).exact
        assert not DistanceToTarget("w", "i", "x", "y", 1).exact


class TestWeightedAggregates:
    def _report(self, pairs):  # pairs of (distance, frequency)
        distances = tuple(
            DistanceToTarget(gloss=f"w{i}", ipa=f"i{i}", derived="x", target="x", distance=d,
                  feature_distance=d, frequency=f)
            for i, (d, f) in enumerate(pairs)
        )
        return AccuracyReport(distances=distances)

    def test_no_variation_is_a_noop(self):
        report = self._report([(0, 1), (1, 1)])  # all default frequency
        assert not report.frequencies_vary
        assert report.weighted_accuracy == report.accuracy  # 0.5 == 0.5

    def test_weighting_shifts_accuracy_toward_frequent_words(self):
        # A frequent word is wrong, a rare word is exact: unweighted looks 50%,
        # but by token weight the frequent error dominates.
        report = self._report([(1, 99), (0, 1)])
        assert report.frequencies_vary
        assert report.accuracy == 0.5  # one of two words exact
        assert report.weight == 100
        assert report.weighted_accuracy == 0.01  # only the freq-1 exact word counts
        assert report.weighted_mean_distance == 0.99  # (99*1 + 1*0) / 100

    def test_weighting_rewards_frequent_correct_words(self):
        # The mirror: the frequent word is exact, the rare one wrong.
        report = self._report([(0, 99), (1, 1)])
        assert report.weighted_accuracy == 0.99
        assert report.weighted_mean_distance == 0.01

    def test_weighted_feature_distance_skips_unsegmentable(self):
        distances = (
            DistanceToTarget("a", "a", "x", "x", 0, feature_distance=0, frequency=10),
            # unsegmentable
            DistanceToTarget("b", "b", "y", "z", 2, feature_distance=None, frequency=5),
            DistanceToTarget("c", "c", "y", "z", 1, feature_distance=4, frequency=2),
        )
        report = AccuracyReport(distances=distances)
        assert report.weighted_mean_feature_distance == (10 * 0 + 2 * 4) / (10 + 2)


class TestGradeDerivationIntegration:
    """End-to-end plumbing against the real engine, using the default project.

    The default lexicon carries no target forms, so we inject a ``final`` on the
    derived surface itself — verifying the render → phone-split → distance path
    without hard-coding any phonology.
    """

    def _surface(self, derivation, project):
        return render_syllabified(
            lower_tiers(derivation.surface), derivation.surface_boundaries, project
        )

    def test_exact_match_when_target_equals_surface(self, project):
        derivation = derive_all(project)[0]
        derivation.word.final = self._surface(derivation, project)
        ingest_targets([derivation], project)
        result = distance_to_target(derivation, project)
        assert result is not None
        assert result.exact and result.distance == 0
        assert result.feature_distance == 0  # feature 0 coincides with phone 0

    def test_one_phone_difference(self, project):
        derivation = derive_all(project)[0]
        derivation.word.final = self._surface(derivation, project) + "k"
        ingest_targets([derivation], project)
        result = distance_to_target(derivation, project)
        assert result is not None and result.distance == 1

    def test_missing_target_is_skipped(self, project):
        derivation = derive_all(project)[0]
        derivation.word.final = None
        assert distance_to_target(derivation, project) is None

    def test_grade_counts_skipped_and_graded(self, project):
        derivations = derive_all(project)
        for derivation in derivations:
            derivation.word.final = None
        derivations[0].word.final = self._surface(derivations[0], project)
        ingest_targets(derivations, project)
        report = measure_accuracy(derivations, project)
        assert report.assessed == 1
        assert report.skipped == len(derivations) - 1
        assert report.exact == 1


class TestFormAtTime:
    def test_before_all_rules_is_the_input(self, project):
        derivation = next(d for d in derive_all(project) if d.steps)
        form, _ = form_at_time(derivation, -(10**9))
        assert form is derivation.input  # nothing fired that early

    def test_after_all_timed_rules_is_the_last_timed_after(self, project):
        derivation = next(d for d in derive_all(project) if d.steps)
        timed = [s for s in derivation.steps if s.rule.time is not None]
        if timed:  # the showcase has timed rules; guard defensively
            form, _ = form_at_time(derivation, 10**9)
            assert form is timed[-1].after


class TestGradeStages:
    def _surface(self, derivation, project):
        return render_syllabified(
            lower_tiers(derivation.surface), derivation.surface_boundaries, project
        )

    def test_stage_snapshot_is_graded_and_final_trails(self, project):
        derivations = derive_all(project)
        d = derivations[0]
        time = 10**9
        form, bounds = form_at_time(d, time)
        snapshot = render_syllabified(lower_tiers(form), bounds, project)
        d.word.stages = {time: snapshot}  # target == the snapshot ⇒ exact
        d.word.final = None
        ingest_targets(derivations, project)
        stages = accuracy_by_stage(derivations, project)
        assert stages[-1].label == "final"  # final always trails
        stage = next(s for s in stages if s.label == str(time))
        row = next(g for g in stage.report.distances if g.ipa == d.word.ipa)
        assert row.exact

    def test_only_words_with_that_stage_are_graded(self, project):
        derivations = derive_all(project)
        derivations[0].word.stages = {500: self._surface(derivations[0], project)}
        for d in derivations[1:]:
            d.word.stages = {}
        ingest_targets(derivations, project)
        stage = next(s for s in accuracy_by_stage(derivations, project) if s.label == "500")
        assert stage.report.assessed == 1


class TestRendering:
    def _stages(self):
        exact = DistanceToTarget("alpha", "a", "x", "x", 0, 0)
        miss = DistanceToTarget("beta", "b", "y", "z", 1, 3)
        return [
            StageAccuracy("300", 300, AccuracyReport((exact, miss))),
            StageAccuracy("final", None, AccuracyReport((exact,), skipped=1)),
        ]

    def test_summary_line_reports_final(self):
        line = accuracy_summary_line(self._stages())
        assert "final:" in line and "1/1 exact" in line

    def test_overall_csv_one_row_per_stage(self):
        import csv

        rows = list(csv.reader(render_accuracy_csv(self._stages()).splitlines()))
        assert rows[0] == [
            "stage", "assessed", "exact", "within 1", "mean phone dist", "mean feature dist",
        ]
        # 300: two assessed (one exact, one a distance-1 miss), mean phone 0.5, mean feature 1.5.
        assert rows[1] == ["300", "2", "1", "2", "0.500", "1.500"]
        assert rows[2][0] == "final" and rows[2][1] == "1" and rows[2][2] == "1"

    def test_stages_csv_keeps_every_assessed_word(self):
        import csv

        rows = list(csv.reader(render_distance_to_target_csv(self._stages()).splitlines()))
        assert rows[0] == ["stage", "gloss", "derived", "target", "d", "fd"]
        body = rows[1:]
        # Every assessed word at every stage — exact matches included.
        assert ["300", "alpha", "x", "x", "0", "0"] in body
        assert ["300", "beta", "y", "z", "1", "3"] in body
        assert ["final", "alpha", "x", "x", "0", "0"] in body


class TestGradeCli:
    def test_writes_report_and_prints_summary(self, capsys, tmp_path):
        output = tmp_path / "accuracy.csv"
        # The default showcase carries target forms, so the run writes the accuracy
        # summary CSV and prints a headline reporting exact matches.
        grade_cli.main(["--output", str(output)])
        assert output.exists()
        assert output.read_text(encoding="utf-8").startswith("stage,assessed,exact,within 1")
        assert (tmp_path / "distance_to_target.csv").exists()
        out = capsys.readouterr().out
        assert "exact" in out

    def test_summary_reports_analysis_timing(self, capsys, tmp_path):
        grade_cli.main(["--output", str(tmp_path / "accuracy.csv")])
        err = capsys.readouterr().err
        assert "derive" in err and "accuracy" in err and "analysis" in err

    def test_scope_writes_scoped_output_leaving_standard_whole(self, tmp_path):
        output = tmp_path / "accuracy.csv"
        grade_cli.main(["--output", str(output), "--scope", "[+syllabic]"])  # any vowel
        scoped = tmp_path / "scoped_output.md"
        assert scoped.exists()
        assert "# Scoped" in scoped.read_text(encoding="utf-8")
        # the standard report stays whole-lexicon — no scope note
        assert "scope" not in output.read_text(encoding="utf-8")

    def test_bad_scope_pattern_exits(self, tmp_path):
        import pytest

        with pytest.raises(SystemExit):
            grade_cli.main(["--output", str(tmp_path / "accuracy.csv"), "--scope", "[bad"])
