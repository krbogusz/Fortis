"""Tests for Feature and FeatureInventory."""

from src.fortis.models.features import Feature, FeatureInventory, FeatureKind
from src.fortis.models.tiers import Tier


class TestFeature:
    def test_binary_feature(self):
        f = Feature(name="voice", tier=Tier.segment, kind=FeatureKind.binary, short_name="vc", values={0: "absent", 1: "present"}, children=None)
        assert f.name == "voice"
        assert f.kind == FeatureKind.binary
        assert f.values[1] == "present"

    def test_unary_feature(self):
        f = Feature(name="manner", tier=Tier.segment, kind=FeatureKind.unary, short_name="man", values={1: "present"}, children=None)
        assert f.values == {1: "present"}

    def test_scalar_feature(self):
        f = Feature(name="tone", tier=Tier.syllable, kind=FeatureKind.scalar, short_name="t", values={1: "low", 2: "mid", 3: "high"}, children=None)
        assert f.values[2] == "mid"

    def test_default_parent(self):
        f = Feature(name="voice", tier=Tier.segment, kind=FeatureKind.binary, short_name="vc", values={0: "absent", 1: "present"}, children=None)
        assert f.parent is None

    def test_with_children(self):
        f = Feature(name="manner", tier=Tier.segment, kind=FeatureKind.unary, short_name="man", values={1: "present"}, children=("continuant", "sonorant"))
        assert f.children == ("continuant", "sonorant")


class TestFeatureInventory:
    def _make_inventory(self) -> FeatureInventory:
        inv = FeatureInventory()
        voice = Feature(name="voice", tier=Tier.segment, kind=FeatureKind.binary, short_name="vc", values={0: "absent", 1: "present"}, children=None)
        nasal = Feature(name="nasal", tier=Tier.segment, kind=FeatureKind.binary, short_name="nas", values={0: "absent", 1: "present"}, children=None)
        manner = Feature(name="manner", tier=Tier.segment, kind=FeatureKind.unary, short_name="man", values={1: "present"}, children=("continuant", "sonorant"))
        continuant = Feature(name="continuant", tier=Tier.segment, kind=FeatureKind.binary, short_name="cont", values={0: "absent", 1: "present"}, children=None, parent="manner")
        sonorant = Feature(name="sonorant", tier=Tier.segment, kind=FeatureKind.binary, short_name="son", values={0: "absent", 1: "present"}, children=None, parent="manner")

        inv["voice"] = voice
        inv["nasal"] = nasal
        inv["manner"] = manner
        inv["continuant"] = continuant
        inv["sonorant"] = sonorant
        return inv

    def test_is_node(self):
        inv = self._make_inventory()
        assert inv.is_node("manner") is True
        assert inv.is_node("voice") is False

    def test_children(self):
        inv = self._make_inventory()
        children = inv.children("manner")
        assert set(children) == {"continuant", "sonorant"}

    def test_children_of_leaf(self):
        inv = self._make_inventory()
        assert inv.children("voice") == ()

    def test_descendants(self):
        inv = self._make_inventory()
        descendants = inv.descendants("manner")
        assert set(descendants) == {"continuant", "sonorant"}

    def test_parent(self):
        inv = self._make_inventory()
        assert inv.parent("continuant") == "manner"
        assert inv.parent("voice") is None

    def test_names_by_length(self):
        inv = self._make_inventory()
        names = inv.names_by_length
        assert names == tuple(sorted(names, key=len, reverse=True))
        assert len(names) == 5

    def test_short_names_by_length(self):
        inv = self._make_inventory()
        shorts = inv.short_names_by_length
        assert shorts == tuple(sorted(shorts, key=len, reverse=True))

    def test_short_to_long_name(self):
        inv = self._make_inventory()
        mapping = inv.short_to_long_name
        assert mapping["vc"] == "voice"
        assert mapping["nas"] == "nasal"
        assert mapping["man"] == "manner"
        assert mapping["cont"] == "continuant"
        assert mapping["son"] == "sonorant"