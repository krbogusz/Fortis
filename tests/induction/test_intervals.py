"""Tests for stage bucketing, mini-projects, and the synthetic benchmark (intervals.py)."""

from dataclasses import replace

from src.fortis.induction.intervals import (
    build_interval,
    build_intervals,
    stage_times,
    synthetic_project,
    synthetic_words,
)
from src.fortis.models.inventories import Word, WordInventory


class TestStageBucketing:
    def test_stage_times_are_the_sorted_attested_times(self, synth):
        assert stage_times(synth) == [-200, -100, 750, 1000, 1200, 1400]

    def test_one_more_interval_than_stage_times(self, synth):
        intervals = build_intervals(synth)
        assert len(intervals) == len(stage_times(synth)) + 1

    def test_endpoints_chain_input_to_final(self, synth):
        intervals = build_intervals(synth)
        assert intervals[0].start is None  # input
        assert intervals[-1].end is None  # final
        assert intervals[0].label.startswith("input")
        assert intervals[-1].label.endswith("final")
        # consecutive intervals share their boundary
        for earlier, later in zip(intervals, intervals[1:], strict=False):
            assert earlier.end == later.start


class TestTeacherForcing:
    def test_source_is_the_attested_earlier_form(self, synth):
        # For the -100→750 interval, each mini-word's input IS the attested -100 form
        # and its target IS the attested 750 form.
        interval = build_interval(synth, -100, 750)
        sample = next(iter(interval.project.words.values()))
        # find the parent word carrying this -100 form
        parent = next(w for w in synth.words.values() if w.stages.get(-100) == sample.ipa)
        assert sample.ipa == parent.stages[-100]
        assert sample.final == parent.stages[750]

    def test_only_words_attesting_both_endpoints_enter(self, synth):
        interval = build_interval(synth, 1200, 1400)
        both = sum(1 for w in synth.words.values() if 1200 in w.stages and 1400 in w.stages)
        # size ≤ the eligible count (collisions may collapse a few onto one key)
        assert interval.size <= both
        assert interval.size + interval.collisions == both

    def test_mini_project_shares_everything_but_words_and_rules(self, synth):
        interval = build_interval(synth, -100, 750)
        mini = interval.project
        assert mini.features is synth.features
        assert mini.letters is synth.letters
        assert mini.tiers is synth.tiers
        assert mini.settings is synth.settings
        assert len(mini.rules) == 0  # induced list starts empty


class TestSegmentationGate:
    def test_unsegmentable_source_is_excluded_and_counted(self, synth):
        # Inject a word whose -100 stage uses a symbol the project cannot segment.
        poisoned = dict(synth.words)
        poisoned["💥boom"] = Word.from_series(
            id="💥boom", seed="💥boom", seed_time=-1000,
            final="a", stages={-100: "💥", 750: "a"},
        )
        project = replace(synth, words=WordInventory(poisoned))
        interval = build_interval(project, -100, 750)
        assert "💥" in interval.excluded
        assert "💥" not in interval.project.words


class TestSynthetic:
    def test_synthetic_keeps_inputs_and_supervision_shape(self, synth):
        words = synthetic_words(synth)
        assert set(words.keys()) == set(synth.words.keys())
        for key, word in words.items():
            # same input, same stage times attested, a machine-generated final present
            assert word.ipa == synth.words[key].ipa
            assert set(word.stages) == set(synth.words[key].stages)
            assert word.final is not None

    def test_synthetic_project_reuses_rules(self, synth):
        synth = synthetic_project(synth)
        assert synth.rules is synth.rules
        assert len(synth.words) == len(synth.words)
