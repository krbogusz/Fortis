"""Tests for the target filter (src/fortis/analysis/filtering.py)."""

from pathlib import Path

import pytest

from src.fortis.analysis.filtering import filter_by_target, filter_note
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project


@pytest.fixture(scope="module")
def latin():
    return load_project(Path("projects/latin_to_french")).unwrap()


@pytest.fixture(scope="module")
def derivs(latin):
    return derive_all(latin)


class TestFilterByTarget:
    def test_selects_words_whose_target_matches(self, derivs, latin):
        result = filter_by_target(derivs, "ʁ", latin).unwrap()
        assert 0 < len(result.matched) < result.considered  # a proper subset
        assert all("ʁ" in d.word.final for d in result.matched)  # every match contains ʁ

    def test_feature_pattern_matches(self, derivs, latin):
        # /t̪/ before a high vowel — the notation a rule target uses.
        result = filter_by_target(derivs, "t̪ [aperture: high]", latin).unwrap()
        assert len(result.matched) > 0

    def test_considered_is_words_with_a_target(self, derivs, latin):
        result = filter_by_target(derivs, "ʁ", latin).unwrap()
        assert result.considered == sum(1 for d in derivs if d.word.final is not None)

    def test_zero_match_is_ok_not_error(self, derivs, latin):
        # /q/ is a valid symbol but no target has it — an empty result, not an error.
        result = filter_by_target(derivs, "q", latin).unwrap()
        assert result.matched == () and result.considered > 0

    def test_parse_error_is_err(self, derivs, latin):
        assert filter_by_target(derivs, "[bad", latin).is_err()

    def test_empty_pattern_is_err(self, derivs, latin):
        assert filter_by_target(derivs, "", latin).is_err()

    def test_unknown_symbol_is_err_not_silent_zero(self, derivs, latin):
        # The failure mode to avoid: a symbol that resolves to nothing must error,
        # not silently match zero words (which reads as "clean").
        assert filter_by_target(derivs, "×", latin).is_err()


class TestFilterNote:
    def test_note_reports_counts(self, derivs, latin):
        note = filter_note(filter_by_target(derivs, "ʁ", latin).unwrap())
        assert "filter `ʁ`" in note and "words" in note
