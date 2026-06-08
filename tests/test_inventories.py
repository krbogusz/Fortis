"""Tests for src.fortis.imports.inventories — Inventories container and integration."""

from __future__ import annotations

from src.fortis.models.tier import Tier

# ---------------------------------------------------------------------------
# Inventories.load — integration
# ---------------------------------------------------------------------------


class TestInventoriesLoad:
    def test_loads_without_error(self, real_inventories):
        assert real_inventories.features is not None
        assert real_inventories.letters is not None
        assert real_inventories.diacritics is not None
        assert real_inventories.sonorities is not None
        assert real_inventories.syllable_parts is not None
        assert real_inventories.words is not None

    def test_has_features(self, real_inventories):
        assert len(real_inventories.features) > 0

    def test_has_letters(self, real_inventories):
        assert len(real_inventories.letters) > 0

    def test_has_diacritics(self, real_inventories):
        assert len(real_inventories.diacritics) > 0


# ---------------------------------------------------------------------------
# Filter methods
# ---------------------------------------------------------------------------


class TestInventoriesFilters:
    def test_segment_features(self, real_inventories):
        seg = real_inventories.segment_features()
        assert len(seg) > 0
        for fd in seg.values():
            assert fd.tier == Tier.segment

    def test_syllable_features(self, real_inventories):
        syl = real_inventories.syllable_features()
        assert len(syl) > 0
        for fd in syl.values():
            assert fd.tier == Tier.syllable

    def test_segment_diacritics(self, real_inventories):
        seg = real_inventories.diacritics.segment_dict
        assert len(seg) > 0
        for dd in seg.values():
            assert dd.tier == Tier.segment

    def test_syllable_diacritics(self, real_inventories):
        syl = real_inventories.diacritics.syllable_dict
        assert len(syl) > 0
        for dd in syl.values():
            assert dd.tier == Tier.syllable


# ---------------------------------------------------------------------------
# Pre-computed key lists
# ---------------------------------------------------------------------------


class TestInventoriesKeyLists:
    def test_letter_keys_sorted_longest_first(self, real_inventories):
        keys = real_inventories.letters.sorted_keys
        for i in range(len(keys) - 1):
            assert len(keys[i]) >= len(keys[i + 1])

    def test_before_diacritic_keys_sorted(self, real_inventories):
        keys = real_inventories.diacritics.before_keys
        for i in range(len(keys) - 1):
            assert len(keys[i]) >= len(keys[i + 1])

    def test_segment_diacritic_keys_sorted(self, real_inventories):
        keys = real_inventories.diacritics.segment_keys
        for i in range(len(keys) - 1):
            assert len(keys[i]) >= len(keys[i + 1])

    def test_attaching_diacritic_keys_sorted(self, real_inventories):
        keys = real_inventories.diacritics.attaching_keys
        for i in range(len(keys) - 1):
            assert len(keys[i]) >= len(keys[i + 1])


# ---------------------------------------------------------------------------
# Time
# ---------------------------------------------------------------------------


class TestInventoriesTime:
    def test_earliest_time(self, real_inventories):
        assert isinstance(real_inventories.time, int)

    def test_time_set_to_earliest(self, real_inventories):
        assert real_inventories.time == real_inventories.earliest_time
