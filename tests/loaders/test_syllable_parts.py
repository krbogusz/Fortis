"""Tests for the syllable parts loader."""

from src.fortis.loaders.syllable_parts import (
    VALID_PART_TYPES,
    load_syllable_part,
    load_syllable_parts_inventory,
)


class TestValidPartTypes:
    def test_types(self):
        assert VALID_PART_TYPES == {"onset", "nucleus", "coda"}


class TestLoadSyllablePart:
    def test_valid_nucleus(self, features):
        result = load_syllable_part("nucleus", -2000, {"definition": "+syll"}, features)
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.part_type == "nucleus"
        assert sp.time == -2000
        assert sp.definition is not None
        assert sp.pattern is None

    def test_onset_parses_definition_as_sequence(self, features):
        # An onset definition is an element sequence: a consonant + optional glide.
        result = load_syllable_part(
            "onset", 0, {"definition": "[+cons][-syllabic, -consonantal]?"}, features
        )
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.definition is None
        assert sp.pattern is not None
        assert len(sp.pattern) == 2  # two elements: the consonant and the optional glide

    def test_onset_bad_pattern_errors(self, features):
        result = load_syllable_part("onset", 0, {"definition": "[+nope]"}, features)
        assert result.is_err()

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
