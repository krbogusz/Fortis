"""Tests for src.fortis.imports.sonorities — SonorityDefinition, SonorityInventory."""

from __future__ import annotations

import pytest

from src.fortis.parsing import parse_feature_bundle

from src.fortis.imports.features import FeatureInventory
from src.fortis.imports.sonorities import SonorityDefinition, SonorityInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.result import Ok
from tests.conftest import INVENTORIES_DIR, make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# SonorityDefinition._load_level
# ---------------------------------------------------------------------------


class TestLoadLevel:
    def test_valid(self, features):
        result = SonorityDefinition._load_level("vowel", {"level": 7})
        assert result == Ok(7)

    def test_missing(self, features):
        result = SonorityDefinition._load_level("vowel", {})
        assert result.is_err()

    def test_non_numeric(self, features):
        result = SonorityDefinition._load_level("vowel", {"level": "high"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# SonorityDefinition._load_bundle
# ---------------------------------------------------------------------------


class TestLoadBundle:
    def test_valid(self, features):
        result = SonorityDefinition._load_bundle("vowel", {"feature_bundle": "+syll, -cons"}, features)
        assert result.is_ok()
        assert result.unwrap() is not None

    def test_empty_string_is_none(self, features):
        result = SonorityDefinition._load_bundle("x", {"feature_bundle": ""}, features)
        assert result == Ok(None)

    def test_missing(self, features):
        result = SonorityDefinition._load_bundle("x", {}, features)
        assert result.is_err()


# ---------------------------------------------------------------------------
# SonorityDefinition.load (integration)
# ---------------------------------------------------------------------------


class TestSonorityDefinitionLoad:
    def test_valid(self, features):
        raw = {"level": 5, "feature_bundle": "+syll, -cons"}
        result = SonorityDefinition.load("vowel", raw, features)
        assert result.is_ok()
        sd = result.unwrap()
        assert sd.label == "vowel"
        assert sd.level == 5
        assert sd.bundle is not None


# ---------------------------------------------------------------------------
# SonorityInventory.validate — duplicate levels
# ---------------------------------------------------------------------------


class TestSonorityInventoryValidate:
    def test_duplicate_levels(self, features):
        raw = {
            "v1": {"level": 5, "feature_bundle": "+syll"},
            "v2": {"level": 5, "feature_bundle": "+cons"},
        }
        # Build manually to test validate
        sd1_result = SonorityDefinition.load("v1", raw["v1"], features)
        sd2_result = SonorityDefinition.load("v2", raw["v2"], features)
        inv = SonorityInventory({"v1": sd1_result.unwrap(), "v2": sd2_result.unwrap()})
        result = inv.validate()
        assert result.is_err()

    def test_unique_levels_ok(self, features):
        raw = {
            "v1": {"level": 5, "feature_bundle": "+syll"},
            "v2": {"level": 3, "feature_bundle": "+cons"},
        }
        sd1_result = SonorityDefinition.load("v1", raw["v1"], features)
        sd2_result = SonorityDefinition.load("v2", raw["v2"], features)
        inv = SonorityInventory({"v1": sd1_result.unwrap(), "v2": sd2_result.unwrap()})
        result = inv.validate()
        assert result.is_ok()


# ---------------------------------------------------------------------------
# SonorityInventory.assign_sonority
# ---------------------------------------------------------------------------


class TestAssignSonority:
    def test_match(self, features):
        sd = SonorityDefinition.load("vowel", {"level": 5, "feature_bundle": "+syll"}, features).unwrap()
        inv = SonorityInventory({"vowel": sd})
        inv._sort_by_specificity()
        segment = parse_feature_bundle("+syll", features).unwrap()
        result = inv.assign_sonority(segment)
        assert result.label == "vowel"

    def test_no_match_raises(self, features):
        sd = SonorityDefinition.load("vowel", {"level": 5, "feature_bundle": "+syll"}, features).unwrap()
        inv = SonorityInventory({"vowel": sd})
        inv._sort_by_specificity()
        segment = parse_feature_bundle("+cons, -syll", features).unwrap()
        with pytest.raises(ValueError):
            inv.assign_sonority(segment)


# ---------------------------------------------------------------------------
# SonorityInventory — load from real file
# ---------------------------------------------------------------------------


class TestSonorityInventoryLoadReal:
    def test_loads_without_error(self, real_features):
        result = SonorityInventory.load(INVENTORIES_DIR / "sonorities.toml", real_features)
        assert result.is_ok()
        inv = result.unwrap()
        assert len(inv) > 0

    def test_levels_unique(self, real_features):
        result = SonorityInventory.load(INVENTORIES_DIR / "sonorities.toml", real_features)
        inv = result.unwrap()
        levels = [sd.level for sd in inv.values()]
        assert len(levels) == len(set(levels))
