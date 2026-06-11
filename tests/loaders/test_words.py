"""Tests for the words loader."""

from src.fortis.loaders.words import load_word_inventory
from src.fortis.result import Err


class TestLoadWordInventory:
    def test_valid(self, tmp_path):
        toml_content = '"xenti" = "in front"\n"mexteːr" = "mother"\n'
        path = tmp_path / "words.toml"
        path.write_text(toml_content)
        result = load_word_inventory(path)
        assert result.is_ok()
        inv = result.unwrap()
        assert "xenti" in inv
        assert inv["xenti"].gloss == "in front"
        assert inv["mexteːr"].gloss == "mother"

    def test_empty_gloss(self, tmp_path):
        toml_content = '"test" = ""\n'
        path = tmp_path / "words.toml"
        path.write_text(toml_content)
        result = load_word_inventory(path)
        assert result.is_ok()
        inv = result.unwrap()
        assert inv["test"].gloss == ""

    def test_missing_file(self, tmp_path):
        path = tmp_path / "nonexistent.toml"
        result = load_word_inventory(path)
        assert result.is_err()

    def test_wrong_extension(self, tmp_path):
        path = tmp_path / "words.json"
        path.write_text("{}")
        result = load_word_inventory(path)
        assert result.is_err()