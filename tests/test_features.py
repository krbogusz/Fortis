"""Tests for src.fortis.imports.features — FeatureDefinition, FeatureInventory."""

from __future__ import annotations

import pytest

from src.fortis.imports.features import FeatureDefinition, FeatureKind
from src.fortis.models.tier import Tier
from src.fortis.result import Ok
from tests.conftest import load_feature_inventory_from_dict

# ---------------------------------------------------------------------------
# FeatureDefinition._load_tier
# ---------------------------------------------------------------------------


class TestLoadTier:
    def test_segment(self):
        result = FeatureDefinition._load_tier("test", {"tier": "segment"})
        assert result == Ok(Tier.segment)

    def test_syllable(self):
        result = FeatureDefinition._load_tier("test", {"tier": "syllable"})
        assert result == Ok(Tier.syllable)

    def test_missing(self):
        result = FeatureDefinition._load_tier("test", {})
        assert result.is_err()
        assert "missing" in result.unwrap_err().lower()

    def test_invalid(self):
        result = FeatureDefinition._load_tier("test", {"tier": "morpheme"})
        assert result.is_err()
        assert "invalid" in result.unwrap_err().lower()

    def test_whitespace_stripped(self):
        result = FeatureDefinition._load_tier("test", {"tier": "  segment  "})
        assert result == Ok(Tier.segment)


# ---------------------------------------------------------------------------
# FeatureDefinition._load_type
# ---------------------------------------------------------------------------


class TestLoadType:
    def test_unary(self):
        result = FeatureDefinition._load_type("test", {"type": "unary"})
        assert result == Ok(FeatureKind.unary)

    def test_binary(self):
        result = FeatureDefinition._load_type("test", {"type": "binary"})
        assert result == Ok(FeatureKind.binary)

    def test_scalar(self):
        result = FeatureDefinition._load_type("test", {"type": "scalar"})
        assert result == Ok(FeatureKind.scalar)

    def test_missing(self):
        result = FeatureDefinition._load_type("test", {})
        assert result.is_err()

    def test_invalid(self):
        result = FeatureDefinition._load_type("test", {"type": "ternary"})
        assert result.is_err()


# ---------------------------------------------------------------------------
# FeatureDefinition._load_short
# ---------------------------------------------------------------------------


class TestLoadShort:
    def test_default_is_name(self):
        result = FeatureDefinition._load_short("nasal", {})
        assert result == Ok("nasal")

    def test_explicit(self):
        result = FeatureDefinition._load_short("nasal", {"short": "nas"})
        assert result == Ok("nas")

    def test_whitespace_stripped(self):
        result = FeatureDefinition._load_short("nasal", {"short": "  nas  "})
        assert result == Ok("nas")

    def test_empty_rejected(self):
        result = FeatureDefinition._load_short("nasal", {"short": ""})
        assert result.is_err()


# ---------------------------------------------------------------------------
# FeatureDefinition._load_values
# ---------------------------------------------------------------------------


class TestLoadValues:
    def test_unary_auto(self):
        result = FeatureDefinition._load_values("test", {}, FeatureKind.unary)
        assert result == Ok({1: "present"})

    def test_binary_auto(self):
        result = FeatureDefinition._load_values("test", {}, FeatureKind.binary)
        assert result == Ok({0: "absent", 1: "present"})

    def test_scalar_requires_values(self):
        result = FeatureDefinition._load_values("test", {}, FeatureKind.scalar)
        assert result.is_err()

    def test_scalar_valid(self):
        raw = {"values": {1: "low", 2: "mid", 3: "high"}}
        result = FeatureDefinition._load_values("test", raw, FeatureKind.scalar)
        assert result.is_ok()

    def test_scalar_non_int_key(self):
        raw = {"values": {"high": 3}}
        result = FeatureDefinition._load_values("test", raw, FeatureKind.scalar)
        assert result.is_err()

    def test_scalar_empty_label(self):
        raw = {"values": {1: ""}}
        result = FeatureDefinition._load_values("test", raw, FeatureKind.scalar)
        assert result.is_err()


# ---------------------------------------------------------------------------
# FeatureDefinition._load_children
# ---------------------------------------------------------------------------


class TestLoadChildren:
    def test_none(self):
        result = FeatureDefinition._load_children("test", {})
        assert result == Ok(None)

    def test_single_string(self):
        result = FeatureDefinition._load_children("test", {"children": "lateral"})
        assert result == Ok(["lateral"])

    def test_list(self):
        result = FeatureDefinition._load_children("test", {"children": ["a", "b"]})
        assert result == Ok(["a", "b"])

    def test_empty_in_list(self):
        result = FeatureDefinition._load_children("test", {"children": ["a", ""]})
        assert result.is_err()


# ---------------------------------------------------------------------------
# FeatureDefinition.load (integration)
# ---------------------------------------------------------------------------


class TestFeatureDefinitionLoad:
    def test_binary_minimal(self):
        result = FeatureDefinition.load("consonantal", {"tier": "segment", "type": "binary"})
        assert result.is_ok()
        fd = result.unwrap()
        assert fd.tier == Tier.segment
        assert fd.kind == FeatureKind.binary

    def test_scalar_with_values(self):
        raw = {"tier": "segment", "type": "scalar", "values": {1: "low", 2: "high"}}
        result = FeatureDefinition.load("height", raw)
        assert result.is_ok()

    def test_multiple_errors(self):
        result = FeatureDefinition.load("bad", {"tier": "invalid", "type": "invalid"})
        assert result.is_err()
        assert len(result.unwrap_err()) >= 2


# ---------------------------------------------------------------------------
# FeatureInventory — load from dict (parent assignment, validation)
# ---------------------------------------------------------------------------


class TestFeatureInventoryFromDict:
    def test_parents_assigned(self):
        raw = {
            "manner": {"tier": "segment", "type": "unary", "children": ["continuant"]},
            "continuant": {"tier": "segment", "type": "binary"},
        }
        inv = load_feature_inventory_from_dict(raw)
        assert inv["continuant"].parent == "manner"

    def test_unknown_child(self):
        raw = {
            "manner": {"tier": "segment", "type": "unary", "children": ["nonexistent"]},
        }
        with pytest.raises(ValueError, match="unknown child"):
            load_feature_inventory_from_dict(raw)

    def test_duplicate_short_names(self):
        raw = {
            "alpha": {"tier": "segment", "type": "binary", "short": "a"},
            "beta": {"tier": "segment", "type": "binary", "short": "a"},
        }
        with pytest.raises(ValueError, match="short name"):
            load_feature_inventory_from_dict(raw)

    def test_short_matches_own_name_is_ok(self):
        raw = {
            "alpha": {"tier": "segment", "type": "binary", "short": "alpha"},
        }
        inv = load_feature_inventory_from_dict(raw)
        assert "alpha" in inv

    def test_children_different_tier(self):
        raw = {
            "parent": {"tier": "segment", "type": "unary", "children": ["child"]},
            "child": {"tier": "syllable", "type": "unary"},
        }
        with pytest.raises(ValueError, match="tier"):
            load_feature_inventory_from_dict(raw)

    def test_circular_parents(self):
        raw = {
            "a": {"tier": "segment", "type": "unary", "children": ["b"]},
            "b": {"tier": "segment", "type": "unary", "children": ["a"]},
        }
        with pytest.raises(ValueError, match="circular"):
            load_feature_inventory_from_dict(raw)


# ---------------------------------------------------------------------------
# FeatureInventory — load from real file
# ---------------------------------------------------------------------------


class TestFeatureInventoryLoadReal:
    def test_loads_without_error(self, real_features):
        assert "consonantal" in real_features
        assert "tone" in real_features

    def test_parent_pointers(self, real_features):
        """In the real inventory, continuant should have manner as parent."""
        if "continuant" in real_features:
            assert real_features["continuant"].parent == "manner"

    def test_has_both_tiers(self, real_features):
        tiers = {fd.tier for fd in real_features.values()}
        assert Tier.segment in tiers
        assert Tier.syllable in tiers
