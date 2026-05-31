import pytest

from src.fortis.inventories.feature_definition import FeatureDefinition
from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_type import FeatureType
from src.fortis.models.tiers import Tier


@pytest.fixture
def inventory():
    """A small feature inventory for testing FeatureBundle."""
    return FeatureInventory(
        {
            "consonantal": FeatureDefinition(
                name="consonantal",
                tier=Tier.segment,
                type=FeatureType.binary,
                short="cons",
                values={0: "absent", 1: "present"},
                children=None,
            ),
            "nasal": FeatureDefinition(
                name="nasal",
                tier=Tier.segment,
                type=FeatureType.unary,
                short="nas",
                values={1: "present"},
                children=None,
            ),
            "height": FeatureDefinition(
                name="height",
                tier=Tier.segment,
                type=FeatureType.scalar,
                short="ht",
                values={1: "low", 2: "mid", 3: "high"},
                children=None,
            ),
            "glottal_aperture": FeatureDefinition(
                name="glottal_aperture",
                tier=Tier.segment,
                type=FeatureType.scalar,
                short="ga",
                values={-1: "constricted", 0: "neutral", 1: "spread"},
                children=None,
            ),
        }
    )


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Basic parsing
# ——————————————————————————————————————————————————————————————————————-———————


class TestFeatureBundleParsing:
    def test_single_binary_plus(self, inventory):
        result = FeatureBundle.from_str("+consonantal", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert bundle["consonantal"].value == 1

    def test_single_binary_minus(self, inventory):
        result = FeatureBundle.from_str("-consonantal", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert bundle["consonantal"].value == 0

    def test_single_scalar(self, inventory):
        result = FeatureBundle.from_str("height:2", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "height" in bundle
        assert bundle["height"].value == 2

    def test_single_short_name(self, inventory):
        result = FeatureBundle.from_str("+cons", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert bundle["consonantal"].value == 1


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Comma-separated features
# ——————————————————————————————————————————————————————————————————————————————————————


class TestCommaSeparated:
    def test_two_features(self, inventory):
        result = FeatureBundle.from_str("+consonantal, nasal:1", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "nasal" in bundle

    def test_mixed_types(self, inventory):
        result = FeatureBundle.from_str("+consonantal, height:2", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert len(bundle) == 2
        assert bundle["consonantal"].value == 1
        assert bundle["height"].value == 2

    def test_three_features(self, inventory):
        result = FeatureBundle.from_str("+consonantal, height:3, ga:1", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert len(bundle) == 3
        assert bundle["consonantal"].value == 1
        assert bundle["height"].value == 3
        assert bundle["glottal_aperture"].value == 1


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Semicolon-separated features
# ——————————————————————————————————————————————————————————————————————-———————


class TestSemicolonSeparated:
    def test_semicolons_converted(self, inventory):
        result = FeatureBundle.from_str("+consonantal; height:2", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert len(bundle) == 2
        assert bundle["consonantal"].value == 1
        assert bundle["height"].value == 2

    def test_mixed_commas_and_semicolons(self, inventory):
        result = FeatureBundle.from_str("+consonantal; height:2, ga:1", inventory)
        assert result.is_ok()
        assert len(result.unwrap()) == 3


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Whitespace handling
# ——————————————————————————————————————————————————————————————————————————————————————


class TestWhitespace:
    def test_spaces_stripped(self, inventory):
        result = FeatureBundle.from_str("  + consonantal , height : 2 ", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert "consonantal" in bundle
        assert "height" in bundle

    def test_no_spaces(self, inventory):
        result = FeatureBundle.from_str("+consonantal,height:2", inventory)
        assert result.is_ok()
        assert len(result.unwrap()) == 2


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Contour values
# ————————————————————————————————————————————————————————————————————————————————-——


class TestBundleContours:
    def test_contour_in_bundle(self, inventory):
        result = FeatureBundle.from_str("+consonantal, height:1>2>3", inventory)
        assert result.is_ok()
        assert result.unwrap()["height"].value == [1, 2, 3]

    def test_only_contour(self, inventory):
        result = FeatureBundle.from_str("height:low>mid>high", inventory)
        assert result.is_ok()
        assert result.unwrap()["height"].value == [1, 2, 3]


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle: Invalid tokens are skipped
# ——————————————————————————————————————————————————————————————————————-———————


class TestBundleInvalidTokens:
    def test_invalid_feature_returns_err(self, inventory):
        result = FeatureBundle.from_str("+consonantal, +xyz, height:2", inventory)
        assert result.is_err()

    def test_invalid_value_returns_err(self, inventory):
        result = FeatureBundle.from_str("+consonantal, height:99", inventory)
        assert result.is_err()

    def test_empty_string(self, inventory):
        result = FeatureBundle.from_str("", inventory)
        assert result.is_ok()
        assert len(result.unwrap()) == 0

    def test_trailing_comma(self, inventory):
        result = FeatureBundle.from_str("+consonantal,", inventory)
        assert result.is_ok()
        bundle = result.unwrap()
        assert len(bundle) == 1
        assert "consonantal" in bundle


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle.match_pattern
# ——————————————————————————————————————————————————————————————————————————————————————


class TestBundleMatchPattern:
    def _bundle(self, **specs: int | list[int | None] | None) -> FeatureBundle:
        return FeatureBundle({f: FeatureSpec(f, v) for f, v in specs.items()})

    def test_all_features_match(self):
        pattern = self._bundle(cons=1, nasal=1)
        target = self._bundle(cons=1, nasal=1)
        assert target.match_pattern(pattern) is True

    def test_one_feature_mismatch(self):
        pattern = self._bundle(cons=1, nasal=1)
        target = self._bundle(cons=1, nasal=0)
        assert target.match_pattern(pattern) is False

    def test_extra_features_in_target_ok(self):
        pattern = self._bundle(cons=1)
        target = self._bundle(cons=1, nasal=0, ht=2)
        assert target.match_pattern(pattern) is True

    def test_missing_feature_in_target_no_match(self):
        pattern = self._bundle(cons=1, nasal=1)
        target = self._bundle(cons=1)
        assert target.match_pattern(pattern) is False

    def test_missing_feature_in_target_ignore_none(self):
        pattern = self._bundle(cons=1, nasal=1)
        target = self._bundle(cons=1)
        assert target.match_pattern(pattern, ignore_none=True) is True

    def test_empty_pattern_matches_anything(self):
        pattern = self._bundle()
        target = self._bundle(cons=1, nasal=0)
        assert target.match_pattern(pattern) is True

    def test_contour_match(self):
        pattern = self._bundle(ht=[1, 2])
        target = self._bundle(ht=[1, 2, 3])
        assert target.match_pattern(pattern, place="any") is True

    def test_contour_mismatch(self):
        pattern = self._bundle(ht=[1, 2])
        target = self._bundle(ht=[0, 3, 4])
        assert target.match_pattern(pattern, place="any") is False


# ——————————————————————————————————————————————————————————————————————————————————————
# FeatureBundle.match_exact
# ——————————————————————————————————————————————————————————————————————————————————————


class TestBundleMatchExact:
    def _bundle(self, **specs: int | list[int | None] | None) -> FeatureBundle:
        return FeatureBundle({f: FeatureSpec(f, v) for f, v in specs.items()})

    def test_identical_bundles_match(self):
        a = self._bundle(cons=1, nasal=0, ht=2)
        b = self._bundle(cons=1, nasal=0, ht=2)
        assert a.match_exact(b) is True

    def test_different_values_no_match(self):
        a = self._bundle(cons=1, nasal=0)
        b = self._bundle(cons=1, nasal=1)
        assert a.match_exact(b) is False

    def test_extra_feature_no_match(self):
        a = self._bundle(cons=1)
        b = self._bundle(cons=1, nasal=0)
        assert a.match_exact(b) is False

    def test_missing_feature_no_match(self):
        a = self._bundle(cons=1, nasal=0)
        b = self._bundle(cons=1)
        assert a.match_exact(b) is False

    def test_empty_bundles_match(self):
        a = self._bundle()
        b = self._bundle()
        assert a.match_exact(b) is True

    def test_contour_exact_match(self):
        a = self._bundle(ht=[1, 2])
        b = self._bundle(ht=[1, 2])
        assert a.match_exact(b) is True

    def test_contour_different_lengths_no_match(self):
        a = self._bundle(ht=[1, 2])
        b = self._bundle(ht=[1, 2, 3])
        assert a.match_exact(b) is False

    def test_contour_different_values_no_match(self):
        a = self._bundle(ht=[1, 2])
        b = self._bundle(ht=[1, 3])
        assert a.match_exact(b) is False
