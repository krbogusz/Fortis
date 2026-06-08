"""Tests for src.fortis.application.merge — apply_bundle with delinking."""

from src.fortis.application.merge import apply_bundle
from src.fortis.imports.features import FeatureDefinition, FeatureInventory, FeatureKind
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_value import FeatureValue
from src.fortis.models.tier import Tier


def _make_inventory_with_hierarchy() -> FeatureInventory:
    """Build a feature inventory with parent→children geometry."""
    features: dict[str, FeatureDefinition] = {
        "place": FeatureDefinition(
            name="place",
            tier=Tier.segment,
            kind=FeatureKind.scalar,
            short="pl",
            values={1: "labial", 2: "coronal", 3: "dorsal"},
            children=["labial", "coronal", "dorsal"],
        ),
        "labial": FeatureDefinition(
            name="labial",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="lab",
            values={0: "absent", 1: "present"},
            children=None,
        ),
        "coronal": FeatureDefinition(
            name="coronal",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="cor",
            values={0: "absent", 1: "present"},
            children=None,
        ),
        "dorsal": FeatureDefinition(
            name="dorsal",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="dor",
            values={0: "absent", 1: "present"},
            children=None,
        ),
        "consonantal": FeatureDefinition(
            name="consonantal",
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short="cons",
            values={0: "absent", 1: "present"},
            children=None,
        ),
    }
    # Assign parents
    for child in ("labial", "coronal", "dorsal"):
        features[child] = FeatureDefinition(
            name=child,
            tier=Tier.segment,
            kind=FeatureKind.binary,
            short=child[:3],
            values={0: "absent", 1: "present"},
            children=None,
            parent="place",
        )
    return FeatureInventory(features)


class TestApplyBundle:
    """Tests for apply_bundle with geometry-aware delinking."""

    def test_simple_override(self):
        """A delta with a concrete value overrides the base."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({"consonantal": FeatureValue(1)})
        delta = FeatureBundle({"consonantal": FeatureValue(0)})
        result = apply_bundle(base, delta, features)
        assert result["consonantal"].value == 0

    def test_new_feature_added(self):
        """A delta with a new feature adds it to the base."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({"consonantal": FeatureValue(1)})
        delta = FeatureBundle({"labial": FeatureValue(1)})
        result = apply_bundle(base, delta, features)
        assert result["consonantal"].value == 1
        assert result["labial"].value == 1

    def test_delink_none_removes_feature(self):
        """Setting a feature to None (unspecified) removes it."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({"consonantal": FeatureValue(1), "labial": FeatureValue(1)})
        delta = FeatureBundle({"labial": FeatureValue(None)})
        result = apply_bundle(base, delta, features)
        assert "labial" not in result
        assert result["consonantal"].value == 1

    def test_delink_parent_removes_descendants(self):
        """Setting a parent node to None removes it AND all its children."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({
            "place": FeatureValue(3),      # dorsal
            "dorsal": FeatureValue(1),      # present
            "consonantal": FeatureValue(1),
        })
        delta = FeatureBundle({"place": FeatureValue(None)})
        result = apply_bundle(base, delta, features)
        assert "place" not in result
        assert "dorsal" not in result
        assert result["consonantal"].value == 1

    def test_delink_child_does_not_remove_parent(self):
        """Setting a child to None removes only that child, not the parent."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({
            "place": FeatureValue(3),      # dorsal
            "dorsal": FeatureValue(1),
            "consonantal": FeatureValue(1),
        })
        delta = FeatureBundle({"dorsal": FeatureValue(None)})
        result = apply_bundle(base, delta, features)
        assert "dorsal" not in result
        assert "place" in result
        assert result["place"].value == 3

    def test_form_contours(self):
        """form_contours=True appends overlapping values."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({"consonantal": FeatureValue(1)})
        delta = FeatureBundle({"consonantal": FeatureValue(0)})
        result = apply_bundle(base, delta, features, form_contours=True)
        assert result["consonantal"].value == [1, 0]

    def test_delta_empty_no_change(self):
        """An empty delta leaves the base unchanged."""
        features = _make_inventory_with_hierarchy()
        base = FeatureBundle({"consonantal": FeatureValue(1)})
        delta = FeatureBundle()
        result = apply_bundle(base, delta, features)
        assert result["consonantal"].value == 1