"""Tests for alpha variable resolution in pattern matching."""

from src.fortis.parsing import parse_pattern_bundle
from src.fortis.imports.features import FeatureDefinition, FeatureInventory, FeatureKind
from src.fortis.models.bindings import Bindings
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.tier import Tier


def _make_inventory() -> FeatureInventory:
    """Build a small feature inventory for alpha tests."""
    features: dict[str, FeatureDefinition] = {
        "consonantal": FeatureDefinition(
            name="consonantal",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="cons",
            values={0: "absent", 1: "present"},
            children=None,
        ),
        "syllabic": FeatureDefinition(
            name="syllabic",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="syll",
            values={0: "absent", 1: "present"},
            children=None,
        ),
        "nasal": FeatureDefinition(
            name="nasal",
            tier=Tier.segment,
            kind=FeatureKind.unary,
            short="nas",
            values={1: "present"},
            children=None,
        ),
        "height": FeatureDefinition(
            name="height",
            tier=Tier.segment,
            kind=FeatureKind.scalar,
            short="hgt",
            values={1: "low", 2: "mid", 3: "high"},
            children=None,
        ),
    }
    return FeatureInventory(features)


class TestAlphaBinding:
    """Alpha variables bind on first occurrence and check on subsequent."""

    def test_alpha_binds_on_first(self):
        """First occurrence of α binds to the segment's value."""
        features = _make_inventory()
        pattern = parse_pattern_bundle("+cons, α height", features).unwrap()
        segment = FeatureBundle({"consonantal": FeatureValue(1), "height": FeatureValue(3)})
        bindings = Bindings()
        assert pattern.matches_against(segment, bindings) is True
        assert "α" in bindings.alpha
        assert bindings.alpha["α"] == 3

    def test_alpha_same_succeeds(self):
        """Second occurrence of α with same value matches."""
        features = _make_inventory()
        pattern = parse_pattern_bundle("α height", features).unwrap()
        segment = FeatureBundle({"height": FeatureValue(3)})
        bindings = Bindings(alpha={"α": 3})
        assert pattern.matches_against(segment, bindings) is True

    def test_alpha_same_fails(self):
        """Second occurrence of α with different value does not match."""
        features = _make_inventory()
        pattern = parse_pattern_bundle("α height", features).unwrap()
        segment = FeatureBundle({"height": FeatureValue(2)})
        bindings = Bindings(alpha={"α": 3})
        assert pattern.matches_against(segment, bindings) is False

    def test_alpha_harmony(self):
        """A harmony-style rule: [α height]...[α height] binds on first, checks on second."""
        features = _make_inventory()
        first_pattern = parse_pattern_bundle("α height", features).unwrap()
        second_pattern = parse_pattern_bundle("α height", features).unwrap()

        bindings = Bindings()
        # First segment has height=3
        seg1 = FeatureBundle({"height": FeatureValue(3)})
        assert first_pattern.matches_against(seg1, bindings) is True
        assert bindings.alpha["α"] == 3

        # Second segment also has height=3 — should match
        seg2 = FeatureBundle({"height": FeatureValue(3)})
        assert second_pattern.matches_against(seg2, bindings) is True

        # Third segment has height=2 — should not match
        seg3 = FeatureBundle({"height": FeatureValue(2)})
        assert second_pattern.matches_against(seg3, bindings) is False

    def test_alpha_no_bindings_matches_any(self):
        """Without bindings, alpha matches any value (permissive)."""
        features = _make_inventory()
        pattern = parse_pattern_bundle("α height", features).unwrap()
        segment = FeatureBundle({"height": FeatureValue(3)})
        # No bindings provided — alpha always matches
        assert pattern.matches_against(segment) is True

    def test_concrete_value_still_works(self):
        """Non-alpha patterns still compare values correctly."""
        features = _make_inventory()
        pattern = parse_pattern_bundle("+cons", features).unwrap()
        segment_match = FeatureBundle({"consonantal": FeatureValue(1)})
        segment_no_match = FeatureBundle({"consonantal": FeatureValue(0)})
        assert pattern.matches_against(segment_match) is True
        assert pattern.matches_against(segment_no_match) is False