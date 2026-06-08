"""Tests for src.fortis.imports.letters — LetterDefinition, LetterInventory."""

from __future__ import annotations

import pytest

from src.fortis.application.parsing import parse_feature_bundle

from src.fortis.imports.features import FeatureInventory
from src.fortis.imports.letters import LetterDefinition, LetterInventory
from src.fortis.models.feature_bundle import FeatureBundle
from tests.conftest import INVENTORIES_DIR, make_feature_inventory


@pytest.fixture
def features() -> FeatureInventory:
    return make_feature_inventory()


# ---------------------------------------------------------------------------
# LetterDefinition.load
# ---------------------------------------------------------------------------


class TestLetterDefinitionLoad:
    def test_valid_row(self, features):
        row = {"symbol": "p", "consonantal": "+", "syllabic": "-"}
        result = LetterDefinition.load(row, features)
        assert result.is_ok()
        ld = result.unwrap()
        assert ld.symbol == "p"
        assert "consonantal" in ld.bundle
        assert "syllabic" in ld.bundle

    def test_missing_symbol(self, features):
        row = {"consonantal": "+"}
        result = LetterDefinition.load(row, features)
        assert result.is_err()

    def test_empty_symbol(self, features):
        row = {"symbol": "  ", "consonantal": "+"}
        result = LetterDefinition.load(row, features)
        assert result.is_err()

    def test_unknown_feature_column(self, features):
        row = {"symbol": "x", "consonantal": "+", "foobar": "1"}
        result = LetterDefinition.load(row, features)
        assert result.is_err()
        assert "foobar" in result.unwrap_err()[0]

    def test_empty_cell_is_unspecified(self, features):
        row = {"symbol": "x", "consonantal": "+", "nasal": ""}
        result = LetterDefinition.load(row, features)
        assert result.is_ok()
        ld = result.unwrap()
        assert "nasal" not in ld.bundle  # empty cell = unspecified = omitted

    def test_scalar_value(self, features):
        row = {"symbol": "a", "height": "3"}
        result = LetterDefinition.load(row, features)
        assert result.is_ok()
        assert result.unwrap().bundle["height"].value == 3

    def test_contour_value(self, features):
        row = {"symbol": "x", "height": "1>3"}
        result = LetterDefinition.load(row, features)
        assert result.is_ok()
        assert result.unwrap().bundle["height"].value == [1, 3]


# ---------------------------------------------------------------------------
# LetterInventory — load from real file
# ---------------------------------------------------------------------------


class TestLetterInventoryLoadReal:
    def test_loads_without_error(self, real_features):
        result = LetterInventory.load(INVENTORIES_DIR / "letters.csv", real_features)
        assert result.is_ok()
        inv = result.unwrap()
        assert len(inv) > 0

    def test_has_known_symbols(self, real_features):
        result = LetterInventory.load(INVENTORIES_DIR / "letters.csv", real_features)
        inv = result.unwrap()
        # The real inventory should have at least some common symbols
        # (exact content depends on the CSV, but it should load)
        assert len(inv) >= 50


# ---------------------------------------------------------------------------
# LetterInventory.validate
# ---------------------------------------------------------------------------


class TestLetterInventoryValidate:
    def test_empty_bundle_is_error(self, features):
        """A letter with an empty bundle (no features) should be caught."""
        ld = LetterDefinition(symbol="x", bundle=FeatureBundle())
        inv = LetterInventory({"x": ld})
        result = inv.validate()
        assert result.is_err()

    def test_duplicate_bundles_is_error(self, features):
        """Two letters with identical bundles should be caught."""
        bundle = parse_feature_bundle("+cons, -syll", features).unwrap()
        ld1 = LetterDefinition(symbol="p", bundle=bundle)
        ld2 = LetterDefinition(symbol="b", bundle=bundle)
        inv = LetterInventory({"p": ld1, "b": ld2})
        result = inv.validate()
        assert result.is_err()

    def test_distinct_bundles_ok(self, features):
        """Two letters with different bundles should pass."""
        b1 = parse_feature_bundle("+cons, -syll", features).unwrap()
        b2 = parse_feature_bundle("-cons, +syll", features).unwrap()
        ld1 = LetterDefinition(symbol="p", bundle=b1)
        ld2 = LetterDefinition(symbol="a", bundle=b2)
        inv = LetterInventory({"p": ld1, "a": ld2})
        result = inv.validate()
        assert result.is_ok()
