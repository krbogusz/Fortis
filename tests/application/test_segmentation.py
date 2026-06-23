"""Tests for IPA segmentation (application/segmentation.py).

These run against the real project inventories (the ``project`` fixture).
"""

import pytest

from src.fortis.application.combining import matches_exactly
from src.fortis.application.rendering import sequence_to_string
from src.fortis.application.segmentation import string_to_sequence


def _feature_equal(a, b) -> bool:
    """Whether two segment sequences carry the same features, segment for segment."""
    return len(a) == len(b) and all(matches_exactly(x, y) for x, y in zip(a, b, strict=True))


class TestStringToSequence:
    def test_known_word_segments(self, project):
        # xenti is five segments: x e n t i.
        assert len(string_to_sequence("xenti", project)) == 5

    def test_diacritics_attach_to_their_base(self, project):
        # ɣʷeroː is four segments — the labialisation and length are diacritics on
        # their bases, not separate segments.
        assert len(string_to_sequence("ɣʷeroː", project)) == 4

    def test_unknown_character_raises(self, project):
        with pytest.raises(ValueError):
            string_to_sequence("xen§ti", project)  # a section sign is not in any inventory

    def test_syllable_tier_diacritic_attaches_to_nucleus(self, project):
        # A syllable-tier tone mark written after the coda must land on the syllable's
        # nucleus, not an earlier segment. ("̄" is tone 3.) Guards the last_nucleus_index
        # path, which no plain lexicon word exercises.
        seq = string_to_sequence("tan" + "̄", project)
        assert [("tone" in s) for s in seq] == [False, True, False]  # tone on the a, not t/n

    def test_word_initial_nucleus_tier_diacritic(self, project):
        # The nucleus is segment 0 here; the tone must land on it (not index -1).
        seq = string_to_sequence("an" + "̄", project)
        assert seq[0]["tone"].value == 3

    def test_stress_attaches_to_a_diacritic_made_nucleus(self, project):
        # ˈl̩ : the syllabic diacritic makes l a nucleus *after* the letter is read;
        # the pending stress must still attach to it (not get stranded / skipped).
        seq = string_to_sequence("ˈl̩", project)
        assert "stress" in seq[0]

    def test_stress_not_stolen_by_a_later_plain_vowel(self, project):
        # ˈl̩a : stress belongs to the syllabic l̩, not the following plain vowel a.
        seq = string_to_sequence("ˈl̩a", project)
        assert "stress" in seq[0] and "stress" not in seq[1]


class TestRoundTrip:
    def test_feature_level_round_trip_for_all_words(self, project):
        # Render-then-resegment recovers the same segments for every lexicon word.
        # (String equality can differ only by diacritic ordering, e.g. gʲʱ vs gʱʲ —
        # the same feature bundle written two ways — so the feature level is the
        # invariant that must hold.)
        for word in project.words:
            seq = string_to_sequence(word, project)
            reseg = string_to_sequence(sequence_to_string(seq, project), project)
            assert _feature_equal(seq, reseg), word
