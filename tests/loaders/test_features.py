"""Tests for the features loader."""

from src.fortis.loaders.features import (
    load_children,
    load_feature,
    load_feature_inventory,
    load_kind,
    load_short,
    load_tier,
    load_values,
)
from src.fortis.models.features import FeatureKind
from src.fortis.models.tiers import Tier


class TestLoadTier:
    def test_valid_segment(self):
        result = load_tier("voice", {"tier": "segment"})
        assert result.is_ok()
        assert result.unwrap() == Tier.segment

    def test_valid_syllable(self):
        result = load_tier("voice", {"tier": "syllable"})
        assert result.is_ok()
        assert result.unwrap() == Tier.syllable

    def test_missing_defaults_to_segment(self):
        # No tier ⇒ segmental: features.toml is segment-only; suprasegmentals live in tiers.toml.
        result = load_tier("voice", {})
        assert result.unwrap() == Tier.segment

    def test_invalid(self):
        result = load_tier("voice", {"tier": "prosodic"})
        assert result.is_err()


class TestLoadKind:
    def test_valid_unary(self):
        result = load_kind("manner", {"kind": "unary"})
        assert result.is_ok()
        assert result.unwrap() == FeatureKind.unary

    def test_valid_binary(self):
        result = load_kind("manner", {"kind": "binary"})
        assert result.is_ok()
        assert result.unwrap() == FeatureKind.binary

    def test_valid_scalar(self):
        result = load_kind("length", {"kind": "scalar"})
        assert result.is_ok()
        assert result.unwrap() == FeatureKind.scalar

    def test_missing(self):
        result = load_kind("manner", {})
        assert result.is_err()

    def test_invalid(self):
        result = load_kind("manner", {"kind": "trinary"})
        assert result.is_err()


class TestLoadShort:
    def test_present(self):
        result = load_short("consonantal", {"short": "cons"})
        assert result.is_ok()
        assert result.unwrap() == "cons"

    def test_missing_defaults_to_name(self):
        result = load_short("consonantal", {})
        assert result.is_ok()
        assert result.unwrap() == "consonantal"

    def test_whitespace_stripped(self):
        result = load_short("consonantal", {"short": "  cons  "})
        assert result.is_ok()
        assert result.unwrap() == "cons"

    def test_whitespace_in_name_rejected(self):
        result = load_short("consonantal", {"short": "con son"})
        assert result.is_err()


class TestLoadValues:
    def test_unary(self):
        result = load_values("manner", {"kind": "unary"}, FeatureKind.unary)
        assert result.is_ok()
        assert result.unwrap() == {1: "present"}

    def test_binary(self):
        result = load_values("voice", {"kind": "binary"}, FeatureKind.binary)
        assert result.is_ok()
        assert result.unwrap() == {0: "absent", 1: "present"}

    def test_scalar_with_values(self):
        result = load_values(
            "tone", {"kind": "scalar", "values": {"1": "low", "2": "high"}}, FeatureKind.scalar
        )
        assert result.is_ok()
        values = result.unwrap()
        assert values[1] == "low"
        assert values[2] == "high"

    def test_scalar_missing_values(self):
        result = load_values("tone", {"kind": "scalar"}, FeatureKind.scalar)
        assert result.is_err()


class TestLoadChildren:
    def test_absent(self):
        result = load_children("voice", {})
        assert result.is_ok()
        assert result.unwrap() is None

    def test_string(self):
        result = load_children("manner", {"children": "continuant"})
        assert result.is_ok()
        assert result.unwrap() == ("continuant",)

    def test_list(self):
        result = load_children("manner", {"children": ["continuant", "sonorant"]})
        assert result.is_ok()
        assert result.unwrap() == ("continuant", "sonorant")

    def test_empty_string(self):
        result = load_children("manner", {"children": ""})
        assert result.is_ok()
        assert result.unwrap() is None

    def test_empty_list(self):
        result = load_children("manner", {"children": []})
        assert result.is_ok()
        assert result.unwrap() is None


class TestLoadFeature:
    def test_valid_binary(self):
        result = load_feature("voice", {"tier": "segment", "kind": "binary", "short": "vc"})
        assert result.is_ok()
        feature = result.unwrap()
        assert feature.name == "voice"
        assert feature.tier == Tier.segment
        assert feature.kind == FeatureKind.binary
        assert feature.short_name == "vc"

    def test_valid_unary_with_children(self):
        result = load_feature(
            "manner",
            {
                "tier": "segment",
                "kind": "unary",
                "short": "man",
                "children": ["continuant", "sonorant"],
            },
        )
        assert result.is_ok()
        feature = result.unwrap()
        assert feature.children == ("continuant", "sonorant")

    def test_no_tier_defaults_to_segment(self):
        result = load_feature("voice", {"kind": "binary"})
        assert result.unwrap().tier == Tier.segment  # tier optional; defaults to segmental

    def test_missing_kind(self):
        result = load_feature("voice", {})
        assert result.is_err()

    def test_multiple_errors_collected(self):
        result = load_feature("voice", {"tier": "prosodic", "kind": "bad"})  # invalid tier + kind
        assert result.is_err()
        errors = result.unwrap_err()
        assert len(errors) >= 2  # both errors collected, not just the first


class TestLoadFeatureInventory:
    def test_from_file(self, features):
        assert "consonantal" in features
        assert "voice" in features
        assert features["consonantal"].kind == FeatureKind.binary
        assert features["stress"].kind == FeatureKind.scalar

    def test_hierarchy(self, features):
        assert features.is_node("manner")
        assert not features.is_node("voice")
        assert "continuant" in features.children("manner")

    def test_scalar_values(self, features):
        assert features["tone"].values[1] == "low"
        assert features["tone"].values[5] == "super_high"

    def test_root_is_synthesized_as_the_segmental_apex(self, features):
        # The MINIMAL fixture declares no root; the loader builds one over the top-level
        # segmental features. Suprasegmentals (tone, stress) stay outside it.
        assert "root" in features  # synthesized, not declared
        assert features.parent("root") is None  # the apex
        assert features.parent("consonantal") == "root"
        assert features.parent("manner") == "root"
        assert features.parent("tone") is None  # suprasegmental — not under the root

    def test_two_segmental_tops_share_a_synthesized_root(self, tmp_path):
        # No declared root: the loader parents both top-level segmental features to one.
        path = tmp_path / "f.toml"
        path.write_text(
            'a = { tier = "segment", kind = "binary", short = "a" }\n'
            'b = { tier = "segment", kind = "binary", short = "b" }\n'
        )
        result = load_feature_inventory(path)
        assert result.is_ok()
        features = result.unwrap()
        assert features.parent("a") == "root" and features.parent("b") == "root"
