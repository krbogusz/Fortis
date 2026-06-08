"""Tests for src.fortis.imports.syllable_parts — SyllablePartDefinition, SyllablePartsInventory."""

from __future__ import annotations

import pytest

from src.fortis.imports.features import FeatureInventory
from src.fortis.imports.syllable_parts import SyllablePartDefinition, SyllablePartsInventory
from tests.conftest import INVENTORIES_DIR, make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# SyllablePartDefinition.load
# ---------------------------------------------------------------------------


class TestSyllablePartDefinitionLoad:
    def test_nucleus_valid(self, features):
        raw = {"definition": "+syll"}
        result = SyllablePartDefinition.load("nucleus", -2000, raw, features)
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.part_type == "nucleus"
        assert sp.definition is not None

    def test_onset_valid(self, features):
        raw = {"required": "[+cons]+", "forbidden": "$[+cons, +nas]"}
        result = SyllablePartDefinition.load("onset", -2000, raw, features)
        assert result.is_ok()
        sp = result.unwrap()
        assert sp.part_type == "onset"
        assert sp.required is not None
        assert sp.forbidden is not None

    def test_coda_valid(self, features):
        raw = {"required": "[+cons]"}
        result = SyllablePartDefinition.load("coda", -2000, raw, features)
        assert result.is_ok()

    def test_invalid_part_type(self, features):
        raw = {"definition": "+syll"}
        result = SyllablePartDefinition.load("medial", -2000, raw, features)
        assert result.is_err()
        assert "Invalid" in result.unwrap_err()[0]

    def test_nucleus_with_required_field(self, features):
        raw = {"definition": "+syll", "required": "[+cons]"}
        result = SyllablePartDefinition.load("nucleus", -2000, raw, features)
        assert result.is_err()
        assert "required" in result.unwrap_err()[0].lower()

    def test_onset_with_definition_field(self, features):
        raw = {"definition": "+syll"}
        result = SyllablePartDefinition.load("onset", -2000, raw, features)
        assert result.is_err()
        assert "definition" in result.unwrap_err()[0].lower()

    def test_nucleus_missing_definition(self, features):
        raw = {}
        result = SyllablePartDefinition.load("nucleus", -2000, raw, features)
        assert result.is_err()
        assert "missing" in result.unwrap_err()[0].lower()

    def test_non_dict_part(self, features):
        result = SyllablePartDefinition.load("nucleus", -2000, "not a dict", features)
        assert result.is_err()


# ---------------------------------------------------------------------------
# SyllablePartsInventory — load from real file
# ---------------------------------------------------------------------------


class TestSyllablePartsInventoryLoadReal:
    def test_loads_without_error(self, real_features):
        result = SyllablePartsInventory.load(INVENTORIES_DIR / "syllable_parts.toml", real_features)
        assert result.is_ok()

    def test_get_nucleus(self, real_features):
        result = SyllablePartsInventory.load(INVENTORIES_DIR / "syllable_parts.toml", real_features)
        inv = result.unwrap()
        nucleus = inv.get_nucleus(-2000)
        assert nucleus is not None

    def test_get_onset(self, real_features):
        result = SyllablePartsInventory.load(INVENTORIES_DIR / "syllable_parts.toml", real_features)
        inv = result.unwrap()
        required, forbidden = inv.get_onset(-2000)
        # May be None if not defined, but should not error
        assert isinstance(required, str | type(None))
        assert isinstance(forbidden, str | type(None))

    def test_missing_time_returns_none(self, real_features):
        result = SyllablePartsInventory.load(INVENTORIES_DIR / "syllable_parts.toml", real_features)
        inv = result.unwrap()
        assert inv.get_nucleus(9999) is None
