"""Tests for inventory types."""

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import (
    Diacritic,
    DiacriticInventory,
    DiacriticKind,
    Letter,
    LetterInventory,
    SonoritiesInventory,
    Sonority,
    SyllablePart,
    SyllablePartsInventory,
    Word,
    WordInventory,
)
from src.fortis.models.tiers import Tier


class TestLetterInventory:
    def test_sorted_keys_longest_first(self):
        inv = LetterInventory()
        inv["ts"] = Letter(symbol="ts", bundle=FeatureBundle())
        inv["a"] = Letter(symbol="a", bundle=FeatureBundle())
        inv["str"] = Letter(symbol="str", bundle=FeatureBundle())
        assert inv.sorted_keys == ["str", "ts", "a"]

    def test_sorted_keys_empty(self):
        inv = LetterInventory()
        assert inv.sorted_keys == []


class TestDiacriticInventory:
    def _make_inventory(self) -> DiacriticInventory:
        inv = DiacriticInventory()
        inv["ʰ"] = Diacritic(
            symbol="ʰ",
            tier=Tier.segment,
            kind=DiacriticKind.after,
            bundle=FeatureBundle(),
            contour=False,
        )
        inv["ˈ"] = Diacritic(
            symbol="ˈ",
            tier=Tier.syllable,
            kind=DiacriticKind.before,
            bundle=FeatureBundle(),
            contour=False,
        )
        inv["̩"] = Diacritic(
            symbol="̩",
            tier=Tier.segment,
            kind=DiacriticKind.combining,
            bundle=FeatureBundle(),
            contour=False,
        )
        return inv

    def test_segment_keys(self):
        inv = self._make_inventory()
        keys = inv.segment_keys
        assert "ʰ" in keys
        assert "̩" in keys
        assert "ˈ" not in keys

    def test_syllable_keys(self):
        inv = self._make_inventory()
        keys = inv.syllable_keys
        assert "ˈ" in keys
        assert "ʰ" not in keys

    def test_before_keys(self):
        inv = self._make_inventory()
        keys = inv.before_keys
        assert "ˈ" in keys
        assert "ʰ" not in keys
        assert "̩" not in keys

    def test_attaching_keys(self):
        inv = self._make_inventory()
        keys = inv.attaching_keys
        assert "ʰ" in keys
        assert "̩" in keys
        assert "ˈ" not in keys

    def test_sorted_longest_first(self):
        inv = DiacriticInventory()
        inv["a"] = Diacritic(
            symbol="a",
            tier=Tier.segment,
            kind=DiacriticKind.after,
            bundle=FeatureBundle(),
            contour=False,
        )
        inv["abc"] = Diacritic(
            symbol="abc",
            tier=Tier.segment,
            kind=DiacriticKind.after,
            bundle=FeatureBundle(),
            contour=False,
        )
        inv["ab"] = Diacritic(
            symbol="ab",
            tier=Tier.segment,
            kind=DiacriticKind.after,
            bundle=FeatureBundle(),
            contour=False,
        )
        assert inv.segment_keys == ["abc", "ab", "a"]


class TestSonoritiesInventory:
    def test_basic_access(self):
        inv = SonoritiesInventory()
        inv["vowel"] = Sonority(label="vowel", level=7, bundle=None)
        assert inv["vowel"].level == 7
        assert inv["vowel"].bundle is None


class TestSyllablePartsInventory:
    def test_basic_access(self):
        inv = SyllablePartsInventory()
        part = SyllablePart(part_type="nucleus", time=-2000, definition=None)
        inv[-2000] = {"nucleus": part}
        assert inv[-2000]["nucleus"].part_type == "nucleus"


class TestWordInventory:
    def test_basic_access(self):
        inv = WordInventory()
        inv["xenti"] = Word.from_series(id="xenti", seed="xenti", gloss="in front")
        assert inv["xenti"].gloss == "in front"

    def test_default_gloss(self):
        inv = WordInventory()
        inv["test"] = Word.from_series(id="test", seed="test")
        assert inv["test"].gloss == ""
