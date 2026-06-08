"""Tests for src.fortis.imports.words — WordInventory."""

from __future__ import annotations

from src.fortis.imports.words import WordInventory
from tests.conftest import INVENTORIES_DIR

# ---------------------------------------------------------------------------
# WordInventory.load
# ---------------------------------------------------------------------------


class TestWordInventoryLoad:
    def test_loads_without_error(self):
        result = WordInventory.load(INVENTORIES_DIR / "words.toml")
        assert result.is_ok()
        inv = result.unwrap()
        assert len(inv) > 0

    def test_keys_are_ipa(self):
        result = WordInventory.load(INVENTORIES_DIR / "words.toml")
        inv = result.unwrap()
        for key, word_def in inv.items():
            assert word_def.ipa == key

    def test_glosses_present(self):
        result = WordInventory.load(INVENTORIES_DIR / "words.toml")
        inv = result.unwrap()
        for word_def in inv.values():
            assert isinstance(word_def.gloss, str)

    def test_missing_file(self):
        result = WordInventory.load(INVENTORIES_DIR / "nonexistent.toml")
        assert result.is_err()
