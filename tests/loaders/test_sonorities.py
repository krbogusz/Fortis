"""Tests for the sonorities loader."""

from src.fortis.loaders.sonorities import (
    load_bundle,
    load_level,
    load_sonority,
    load_sonority_inventory,
    validate_sonority_inventory,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.result import Err


class TestLoadLevel:
    def test_valid(self):
        result = load_level("vowel", {"level": 7})
        assert result.is_ok()
        assert result.unwrap() == 7

    def test_missing(self):
        result = load_level("vowel", {})
        assert result.is_err()

    def test_zero(self):
        result = load_level("vowel", {"level": 0})
        assert result.is_err()

    def test_negative(self):
        result = load_level("vowel", {"level": -1})
        assert result.is_err()

    def test_non_integer(self):
        result = load_level("vowel", {"level": "high"})
        assert result.is_err()


class TestLoadBundle:
    def test_valid(self, features):
        result = load_bundle("vowel", {"bundle": "syllabic: +, consonantal: -"}, features)
        assert result.is_ok()
        assert result.unwrap() is not None

    def test_empty_string_returns_none(self, features):
        result = load_bundle("vowel", {"bundle": ""}, features)
        assert result.is_ok()
        assert result.unwrap() is None

    def test_missing(self, features):
        result = load_bundle("vowel", {}, features)
        assert result.is_err()


class TestLoadSonority:
    def test_valid(self, features):
        result = load_sonority("vowel", {"level": 7, "bundle": "syllabic: +, consonantal: -"}, features)
        assert result.is_ok()
        s = result.unwrap()
        assert s.label == "vowel"
        assert s.level == 7
        assert s.bundle is not None

    def test_missing_level(self, features):
        result = load_sonority("vowel", {"bundle": "syllabic: +"}, features)
        assert result.is_err()


class TestLoadSonorityInventory:
    def test_from_file(self, tmp_path, features):
        toml_content = 'vowel = { level = 7, bundle = "syllabic: +, consonantal: -" }\nstop = { level = 1, bundle = "sonorant: -" }\n'
        path = tmp_path / "sonorities.toml"
        path.write_text(toml_content)
        result = load_sonority_inventory(path, features)
        assert result.is_ok()
        inv = result.unwrap()
        assert "vowel" in inv
        assert inv["vowel"].level == 7

    def test_duplicate_levels(self, tmp_path, features):
        toml_content = 'vowel = { level = 7, bundle = "syllabic: +" }\nglide = { level = 7, bundle = "consonantal: -" }\n'
        path = tmp_path / "sonorities.toml"
        path.write_text(toml_content)
        result = load_sonority_inventory(path, features)
        assert result.is_err()