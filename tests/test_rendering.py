"""Tests for rendering FeatureBundles back into IPA strings."""

import pytest

from src.fortis.inventories.inventories import Inventories
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.sequence import Sequence
from src.fortis.transcription.rendering import _find_diacritics, _render_segment, sequence_to_string
from src.fortis.transcription.parsing import string_to_sequence


@pytest.fixture
def inventories():
    """Load the real inventories."""
    return Inventories.load()


# ---------------------------------------------------------------------------
# Round-trip tests (parse → render should reproduce the original)
# ---------------------------------------------------------------------------


class TestRoundTrips:
    """Parsing an IPA string then rendering it should return the same string."""

    @pytest.mark.parametrize(
        "ipa",
        [
            # Plain letters
            "p", "b", "t", "d", "k", "ɡ", "m", "n", "s", "z",
            "i", "e", "a", "o", "u",
            # Affricates and complex symbols
            "t͡s", "d͡z", "t͡ʃ", "d͡ʒ",
            # Segment diacritics
            "tʰ", "dʱ", "n̩", "ⁿd", "bː", "bːː", "pʷ",
            # Multiple diacritics
            "tʰː", "pʷː", "ⁿdʱ",
            # Words
            "kʰat", "spʰin", "ɣet͡sro",
        ],
    )
    def test_round_trip(self, ipa: str, inventories: Inventories):
        sequence = string_to_sequence(ipa, inventories)
        assert sequence_to_string(sequence, inventories) == ipa


# ---------------------------------------------------------------------------
# Unit tests for _render_segment
# ---------------------------------------------------------------------------


class TestRenderSegment:
    def test_exact_match(self, inventories: Inventories):
        """A letter that exists in the inventory renders as itself."""
        t_bundle = inventories.letters["t"]
        segment = FeatureBundle(dict(t_bundle))
        assert _render_segment(segment, inventories) == "t"

    def test_closest_letter_for_empty(self, inventories: Inventories):
        """An empty segment picks the closest letter (fewest differences)."""
        # An empty bundle doesn't match any letter exactly, so the closest
        # letter by fewest remaining differences is returned
        segment = FeatureBundle()
        result = _render_segment(segment, inventories)
        assert result != ""  # should produce something
        assert "�" not in result  # replacement char only if no letters exist


# ---------------------------------------------------------------------------
# Unit tests for _find_diacritics
# ---------------------------------------------------------------------------


class TestFindDiacritics:
    def test_no_remaining_diffs(self, inventories: Inventories):
        """When there are no remaining diffs, no diacritics are added."""
        remaining: set[str] = set()
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        target = inventories.letters["t"]
        _find_diacritics(target, remaining, inventories.segment_diacritics(), before, combining, after)
        assert before == []
        assert combining == []
        assert after == []

    def test_single_diacritic_covers_all(self, inventories: Inventories):
        """One diacritic covers all remaining differences."""
        # Build segment: t + ʰ (aspiration)
        t_bundle = inventories.letters["t"]
        h_def = inventories.diacritics["ʰ"]
        segment = t_bundle.combine_with(h_def.bundle)
        remaining = set(segment.differing(t_bundle))
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, inventories.segment_diacritics(), before, combining, after)
        assert "ʰ" in after
        assert before == []
        assert combining == []

    def test_multiple_diacritics(self, inventories: Inventories):
        """Multiple diacritics needed for multiple differences."""
        # Build segment: b + ː + ʷ
        b_bundle = inventories.letters["b"]
        length_def = inventories.diacritics["ː"]
        labial_def = inventories.diacritics["ʷ"]
        segment = b_bundle.combine_with(length_def.bundle)
        segment = segment.combine_with(labial_def.bundle)
        remaining = set(segment.differing(b_bundle))
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, inventories.segment_diacritics(), before, combining, after)
        assert "ː" in after
        assert "ʷ" in after

    def test_before_diacritic(self, inventories: Inventories):
        """Before diacritics are placed in the before list."""
        # Build segment: d + ⁿ (prenasalization)
        d_bundle = inventories.letters["d"]
        nasal_def = inventories.diacritics["ⁿ"]
        segment = d_bundle.combine_with(nasal_def.bundle)
        remaining = set(segment.differing(d_bundle))
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, inventories.segment_diacritics(), before, combining, after)
        assert "ⁿ" in before

    def test_combining_diacritic(self, inventories: Inventories):
        """Combining diacritics are placed in the combining list."""
        # Build segment: n + ̩ (syllabic)
        n_bundle = inventories.letters["n"]
        syll_def = inventories.diacritics["̩"]
        segment = n_bundle.combine_with(syll_def.bundle)
        remaining = set(segment.differing(n_bundle))
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, inventories.segment_diacritics(), before, combining, after)
        assert "̩" in combining


# ---------------------------------------------------------------------------
# Unit tests for LetterInventory.validate (duplicate bundle detection)
# ---------------------------------------------------------------------------


class TestLetterInventoryValidate:
    def test_rejects_duplicate_bundles(self):
        """Two letters with identical feature bundles should fail validation."""
        from src.fortis.inventories.letters import LetterInventory

        bundle = FeatureBundle({"syllabic": FeatureSpec("syllabic", 1)})
        inv = LetterInventory({"a": FeatureBundle(dict(bundle)), "b": FeatureBundle(dict(bundle))})
        result = inv.validate()
        assert result.is_err()
        errors = result.unwrap_err()
        assert any("identical" in e for e in errors)

    def test_allows_distinct_bundles(self):
        """Letters with different feature bundles should pass validation."""
        from src.fortis.inventories.letters import LetterInventory

        inv = LetterInventory({
            "a": FeatureBundle({"syllabic": FeatureSpec("syllabic", 1)}),
            "b": FeatureBundle({"syllabic": FeatureSpec("syllabic", 0)}),
        })
        result = inv.validate()
        assert result.is_ok()

    def test_rejects_empty_bundle(self):
        """A letter with no features should fail validation."""
        from src.fortis.inventories.letters import LetterInventory

        inv = LetterInventory({"x": FeatureBundle()})
        result = inv.validate()
        assert result.is_err()

    def test_no_duplicate_bundles_in_real_inventory(self, inventories: Inventories):
        """The real inventory should have no duplicate bundles."""
        from src.fortis.inventories.letters import LetterInventory

        result = inventories.letters.validate()
        assert result.is_ok()