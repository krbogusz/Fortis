"""Tests for the syllable parts loader."""

from src.fortis.loaders.syllable_parts import (
    VALID_PART_TYPES,
    load_definition,
    load_syllable_part,
    load_syllable_parts_inventory,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.result import Err


class TestValidPartTypes:
    def test_types(self):
        assert VALID_PART_TYPES == {"onset", "nucleus", "coda"}


class TestLoadDefinition:
    def test_present(self, features):
        result = load_definition("nucleus", -2000, {"definition": "+syll"}, features)
        assert result.is_ok()
        assert result.unwrap() is not None

    def test_absent_returns_none(self, features):
        result = load_definition("onset", -2000, {}, features)
        assert result.is_ok()
        assert result.unwrap() is None

    def test_empty_returns_none(self, features):
        result = load_definition("onset", -2000, {"definition": ""}, features)
        assert result.is_ok()
        assert result.unwrap() is None


class TestLoadSyllablePart:
    def test_valid_nucleus(self, features):
        result = load_syllable_part("nucleus", -2000, {"definition": "+syll"}, features)
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.part_type == "nucleus"
        assert sp.time == -2000
        assert sp.definition is not None

    def test_invalid_part_type(self, features):
        result = load_syllable_part("codu", -2000, {}, features)
        assert result.is_err()

    def test_without_definition(self, features):
        result = load_syllable_part("onset", -2000, {}, features)
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.definition is None


class TestLoadSyllablePartsInventory:
    def test_from_file(self, tmp_path, features):
        toml_content = '[-2000]\nnucleus = { definition = "+syll" }\n'
        path = tmp_path / "syllable_parts.toml"
        path.write_text(toml_content)
        result = load_syllable_parts_inventory(path, features)
        assert result.is_ok()
        inv = result.unwrap()
        assert -2000 in inv
        assert "nucleus" in inv[-2000]

    def test_non_integer_time(self, tmp_path, features):
        toml_content = '[abc]\nnucleus = { definition = "+syll" }\n'
        path = tmp_path / "syllable_parts.toml"
        path.write_text(toml_content)
        result = load_syllable_parts_inventory(path, features)
        assert result.is_err()