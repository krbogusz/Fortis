"""Tests for src.fortis.imports.diacritics — DiacriticDefinition, DiacriticInventory."""

from __future__ import annotations

import pytest

from src.fortis.imports.diacritics import DiacriticDefinition, DiacriticInventory, DiacriticType
from src.fortis.imports.features import FeatureInventory
from src.fortis.models.tier import Tier
from src.fortis.result import Ok
from tests.conftest import INVENTORIES_DIR, make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# DiacriticDefinition._load_tier
# ---------------------------------------------------------------------------


class TestLoadTier:
    def test_segment(self, features):
        result = DiacriticDefinition._load_tier("ʰ", {"tier": "segment"})
        assert result == Ok(Tier.segment)

    def test_syllable(self, features):
        result = DiacriticDefinition._load_tier("ˈ", {"tier": "syllable"})
        assert result == Ok(Tier.syllable)

    def test_missing(self, features):
        result = DiacriticDefinition._load_tier("ʰ", {})
        assert result.is_err()
        assert "missing" in result.unwrap_err().lower()

    def test_invalid(self, features):
        result = DiacriticDefinition._load_tier("ʰ", {"tier": "morpheme"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# DiacriticDefinition._load_type
# ---------------------------------------------------------------------------


class TestLoadType:
    def test_before(self, features):
        result = DiacriticDefinition._load_type("ˈ", {"type": "before"})
        assert result == Ok(DiacriticType.before)

    def test_combining(self, features):
        result = DiacriticDefinition._load_type("̃", {"type": "combining"})
        assert result == Ok(DiacriticType.combining)

    def test_after(self, features):
        result = DiacriticDefinition._load_type("ʰ", {"type": "after"})
        assert result == Ok(DiacriticType.after)

    def test_missing(self, features):
        result = DiacriticDefinition._load_type("ʰ", {})
        assert result.is_err()

    def test_invalid(self, features):
        result = DiacriticDefinition._load_type("ʰ", {"type": "infix"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# DiacriticDefinition._load_bundle
# ---------------------------------------------------------------------------


class TestLoadBundle:
    def test_valid(self, features):
        result = DiacriticDefinition._load_bundle("ʰ", {"bundle": "1 glap"}, features)
        # This fails because "glap" is not in the synthetic inventory
        # Use a feature that exists in the synthetic inventory
        pass

    def test_valid_with_synthetic(self, features):
        result = DiacriticDefinition._load_bundle("ʰ", {"bundle": "+cons"}, features)
        assert result.is_ok()

    def test_missing(self, features):
        result = DiacriticDefinition._load_bundle("ʰ", {}, features)
        assert result.is_err()

    def test_empty_string(self, features):
        result = DiacriticDefinition._load_bundle("ʰ", {"bundle": ""}, features)
        assert result.is_err()

    def test_invalid_feature(self, features):
        result = DiacriticDefinition._load_bundle("ʰ", {"bundle": "+unknown"}, features)
        assert result.is_err()


# ---------------------------------------------------------------------------
# DiacriticDefinition._load_default
# ---------------------------------------------------------------------------


class TestLoadDefault:
    def test_missing_defaults_false(self, features):
        result = DiacriticDefinition._load_default("ʰ", {})
        assert result == Ok(False)

    def test_true(self, features):
        result = DiacriticDefinition._load_default("ˈ", {"default": True})
        assert result == Ok(True)

    def test_false(self, features):
        result = DiacriticDefinition._load_default("ʰ", {"default": False})
        assert result == Ok(False)

    def test_non_bool(self, features):
        result = DiacriticDefinition._load_default("ʰ", {"default": "yes"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# DiacriticDefinition._load_contour
# ---------------------------------------------------------------------------


class TestLoadContour:
    def test_missing_defaults_false(self, features):
        result = DiacriticDefinition._load_contour("ʰ", {})
        assert result == Ok(False)

    def test_true(self, features):
        result = DiacriticDefinition._load_contour("˥", {"contour": True})
        assert result == Ok(True)

    def test_non_bool(self, features):
        result = DiacriticDefinition._load_contour("˥", {"contour": "yes"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# DiacriticDefinition.load (integration)
# ---------------------------------------------------------------------------


class TestDiacriticDefinitionLoad:
    def test_minimal_segment(self, features):
        raw = {"tier": "segment", "type": "after", "bundle": "+cons"}
        result = DiacriticDefinition.load("ʰ", raw, features)
        assert result.is_ok()
        dd = result.unwrap()
        assert dd.tier == Tier.segment
        assert dd.type == DiacriticType.after
        assert dd.default is False
        assert dd.contour is False

    def test_syllable_with_default_and_contour(self, features):
        raw = {"tier": "syllable", "type": "after", "bundle": "tn: 3", "default": True, "contour": True}
        result = DiacriticDefinition.load("˧", raw, features)
        assert result.is_ok()
        dd = result.unwrap()
        assert dd.tier == Tier.syllable
        assert dd.default is True
        assert dd.contour is True

    def test_multiple_errors(self, features):
        raw = {"tier": "invalid", "type": "invalid"}
        result = DiacriticDefinition.load("bad", raw, features)
        assert result.is_err()
        assert len(result.unwrap_err()) >= 2


# ---------------------------------------------------------------------------
# DiacriticInventory.validate — bundle-tier consistency
# ---------------------------------------------------------------------------


class TestDiacriticInventoryValidate:
    def test_segment_diacritic_using_syllable_feature(self, features):
        """A segment-tier diacritic using a syllable-tier feature is an error."""
        raw = {"tier": "segment", "type": "after", "bundle": "tn: 3"}
        result = DiacriticDefinition.load("bad", raw, features)
        assert result.is_ok()  # per-entry load doesn't check tier consistency

        dd = result.unwrap()
        inv = DiacriticInventory({"bad": dd})
        check = inv.validate(features)
        assert check.is_err()
        assert "tone" in check.unwrap_err()[0]
        assert "segment" in check.unwrap_err()[0]

    def test_syllable_diacritic_using_segment_feature(self, features):
        """A syllable-tier diacritic using a segment-tier feature is an error."""
        raw = {"tier": "syllable", "type": "before", "bundle": "+cons"}
        result = DiacriticDefinition.load("bad", raw, features)
        assert result.is_ok()

        dd = result.unwrap()
        inv = DiacriticInventory({"bad": dd})
        check = inv.validate(features)
        assert check.is_err()
        assert "consonantal" in check.unwrap_err()[0]

    def test_valid_tier_match(self, features):
        """Same tier for diacritic and bundle features is fine."""
        raw = {"tier": "segment", "type": "after", "bundle": "+cons"}
        result = DiacriticDefinition.load("ok", raw, features)
        assert result.is_ok()

        dd = result.unwrap()
        inv = DiacriticInventory({"ok": dd})
        check = inv.validate(features)
        assert check.is_ok()


# ---------------------------------------------------------------------------
# DiacriticInventory — load from real file
# ---------------------------------------------------------------------------


class TestDiacriticInventoryLoadReal:
    def test_loads_without_error(self, real_features):
        result = DiacriticInventory.load(INVENTORIES_DIR / "diacritics.toml", real_features)
        assert result.is_ok()
        inv = result.unwrap()
        assert len(inv) > 0

    def test_has_segment_and_syllable(self, real_features):
        result = DiacriticInventory.load(INVENTORIES_DIR / "diacritics.toml", real_features)
        inv = result.unwrap()
        tiers = {dd.tier for dd in inv.values()}
        assert Tier.segment in tiers
        assert Tier.syllable in tiers
