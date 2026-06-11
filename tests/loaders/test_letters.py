"""Tests for the letters loader."""

from src.fortis.loaders.letters import load_letter, load_letter_inventory
from src.fortis.models.features import FeatureInventory
from src.fortis.result import Err


class TestLoadLetter:
    def test_valid_letter(self, features):
        row = {"symbol": "m", "consonantal": "+", "sonorant": "+", "nasal": "+", "lateral": "-"}
        result = load_letter(row, features)
        assert result.is_ok()
        letter = result.unwrap()
        assert letter.symbol == "m"
        assert "consonantal" in letter.bundle

    def test_missing_symbol(self, features):
        row = {"consonantal": "+"}
        result = load_letter(row, features)
        assert result.is_err()

    def test_empty_cell_skipped(self, features):
        row = {"symbol": "m", "consonantal": "+", "voice": ""}
        result = load_letter(row, features)
        assert result.is_ok()
        letter = result.unwrap()
        assert "consonantal" in letter.bundle
        assert "voice" not in letter.bundle

    def test_unknown_feature(self, features):
        row = {"symbol": "m", "nonexistent": "+"}
        result = load_letter(row, features)
        assert result.is_err()


class TestLoadLetterInventory:
    def test_from_file(self, tmp_path, features):
        csv_content = "symbol,consonantal,sonorant,nasal\nm,+,+,+\nn,-,+,-\n"
        path = tmp_path / "letters.csv"
        path.write_text(csv_content)
        result = load_letter_inventory(path, features)
        assert result.is_ok()
        inv = result.unwrap()
        assert "m" in inv
        assert "n" in inv

    def test_duplicate_symbol(self, tmp_path, features):
        csv_content = "symbol,consonantal\nm,+\nm,+\n"
        path = tmp_path / "letters.csv"
        path.write_text(csv_content)
        result = load_letter_inventory(path, features)
        assert result.is_err()

    def test_missing_file(self, tmp_path, features):
        path = tmp_path / "nonexistent.csv"
        result = load_letter_inventory(path, features)
        assert result.is_err()