"""Tests for src.fortis.transcription — parsing and rendering (round-trip)."""

from __future__ import annotations

import pytest

from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.transcription.parsing import string_to_sequence
from src.fortis.transcription.rendering import render_segment, sequence_to_string

# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


class TestParsing:
    def test_single_letter(self, real_inventories):
        segments = string_to_sequence("p", real_inventories)
        assert len(segments) == 1

    def test_multiple_letters(self, real_inventories):
        segments = string_to_sequence("pan", real_inventories)
        assert len(segments) == 3

    def test_reserved_symbol_skipped(self, real_inventories):
        """The dot (syllable boundary) is a reserved symbol and gets skipped."""
        segments = string_to_sequence("pa.na", real_inventories)
        assert len(segments) == 4  # p, a, n, a

    def test_unknown_character_raises(self, real_inventories):
        with pytest.raises(ValueError, match="Unknown"):
            string_to_sequence("ZZZZ", real_inventories)

    def test_before_diacritic(self, real_inventories):
        """A before-diacritic (e.g. stress) should modify the following segment."""
        segments = string_to_sequence("ˈpa", real_inventories)
        # Stress is syllable-tier, so it should be in the first nucleus segment
        # At minimum, we should get 2 segments
        assert len(segments) >= 2

    def test_combining_diacritic(self, real_inventories):
        """A combining diacritic should modify the last segment."""
        # Use the syllabic combining diacritic which exists in the inventory
        segments = string_to_sequence("pm̩", real_inventories)
        assert len(segments) >= 2


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


class TestRendering:
    def test_exact_letter_match(self, real_inventories):
        """A segment that exactly matches a letter should render as that letter."""
        # Use a letter that exists in the inventory
        letter_symbol = real_inventories.letters.sorted_keys[0]
        segment = real_inventories.letters[letter_symbol].bundle
        result = render_segment(segment, real_inventories)
        assert result == letter_symbol

    def test_unknown_segment_returns_letter_or_replacement(self, real_inventories):
        """A segment that doesn't exactly match a letter still gets the closest letter + diacritics."""
        empty = FeatureBundle()
        result = render_segment(empty, real_inventories)
        # Empty bundle may match some letter or return replacement char — just check it doesn't crash
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Round-trip: parse → render
# ---------------------------------------------------------------------------


class TestRoundTrip:
    def test_simple_word(self, real_inventories):
        """Parsing then rendering a simple word should recover the original."""
        original = "xenti"
        segments = string_to_sequence(original, real_inventories)
        rendered = sequence_to_string(segments, real_inventories)
        assert rendered == original

    def test_multi_char_symbol(self, real_inventories):
        """Multi-character symbols should round-trip correctly."""
        # Try a word from the real inventory
        for ipa in list(real_inventories.words.keys())[:5]:
            segments = string_to_sequence(ipa, real_inventories)
            rendered = sequence_to_string(segments, real_inventories)
            assert rendered == ipa, f"Round-trip failed for '{ipa}' → '{rendered}'"
