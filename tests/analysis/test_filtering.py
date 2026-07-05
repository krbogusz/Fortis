"""Tests for the pattern filter (src/fortis/analysis/filtering.py)."""

from pathlib import Path

import pytest

from src.fortis.analysis.filtering import (
    filter_attested,
    filter_by_pattern,
    filter_summary_line,
    scope_summary_line,
)
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project


@pytest.fixture(scope="module")
def latin():
    return load_project(Path("projects/latin_to_french")).unwrap()


@pytest.fixture(scope="module")
def derivs(latin):
    return derive_all(latin)


class TestFilterByPattern:
    def test_matches_transient_forms_not_just_the_target(self, derivs, latin):
        # /d͡ʒ/ is an Old French affricate that arises mid-derivation and resolves to /ʒ/,
        # so words match on a DERIVED form even though their target has no d͡ʒ — the whole
        # point of matching every form, not just the target.
        result = filter_by_pattern(derivs, "d͡ʒ", latin).unwrap()
        assert len(result.matched) > 0
        assert all(m.locations for m in result.matched)
        assert any(all(loc.label != "target" for loc in m.locations) for m in result.matched)

    def test_locations_are_one_per_phase(self, derivs, latin):
        # A pattern persisting across several rules at one time collapses to one entry.
        result = filter_by_pattern(derivs, "d͡ʒ", latin).unwrap()
        for m in result.matched:
            labels = [loc.label for loc in m.locations]
            assert len(labels) == len(set(labels))

    def test_considered_is_every_word(self, derivs, latin):
        # Every word has a derivation, so all are considered (not only those with a target).
        assert filter_by_pattern(derivs, "ʁ", latin).unwrap().considered == len(derivs)

    def test_feature_pattern_matches(self, derivs, latin):
        result = filter_by_pattern(derivs, "t̪ [aperture: high]", latin).unwrap()
        assert len(result.matched) > 0

    def test_parse_error_is_err(self, derivs, latin):
        assert filter_by_pattern(derivs, "[bad", latin).is_err()

    def test_empty_pattern_is_err(self, derivs, latin):
        assert filter_by_pattern(derivs, "", latin).is_err()

    def test_unknown_symbol_is_err_not_silent_zero(self, derivs, latin):
        assert filter_by_pattern(derivs, "×", latin).is_err()


class TestFilterSummaryLine:
    def test_line_reports_counts(self, derivs, latin):
        line = filter_summary_line(filter_by_pattern(derivs, "ʁ", latin).unwrap())
        assert "filter `ʁ`" in line and "matched" in line


class TestFilterAttested:
    def test_matches_the_attested_target(self, derivs, latin):
        result = filter_attested(derivs, "ʁ", latin).unwrap()
        assert len(result.matched) > 0
        for d in result.matched:
            forms = ([d.word.final] if d.word.final else []) + list(d.word.stages.values())
            assert any("ʁ" in f for f in forms)

    def test_matches_a_stage_the_final_lacks(self, derivs, latin):
        # /s/ survives in early attested stages of some words but drops by the final —
        # scoping on all stages (not just the target) must include those words.
        result = filter_attested(derivs, "s", latin).unwrap()
        assert any(
            d.word.final and "s" not in d.word.final and any("s" in v for v in d.word.stages.values())
            for d in result.matched
        )

    def test_considered_is_words_with_an_attested_form(self, derivs, latin):
        result = filter_attested(derivs, "ʁ", latin).unwrap()
        expected = sum(1 for d in derivs if d.word.final is not None or d.word.stages)
        assert result.considered == expected

    def test_parse_error_is_err(self, derivs, latin):
        assert filter_attested(derivs, "[bad", latin).is_err()

    def test_summary_line(self, derivs, latin):
        line = scope_summary_line(filter_attested(derivs, "ʁ", latin).unwrap())
        assert "scope `ʁ`" in line and "match" in line
