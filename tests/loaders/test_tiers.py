"""Tests for the tier-declaration loader (loaders/tiers.py)."""

from src.fortis.loaders.tiers import load_tier, load_tier_inventory


def test_valid_tier_loads(project):
    table = {"carries": ["tone"], "anchor": "+syllabic", "melody": True}
    tier = load_tier("tone", table, project.features).unwrap()
    assert tier.name == "tone" and tier.carries == ("tone",)
    assert tier.melody is True and tier.ocp is True and tier.stray_erase is True  # defaults


def test_unknown_carried_feature_rejected(project):
    table = {"carries": ["nope"], "anchor": "+syllabic", "melody": True}
    result = load_tier("x", table, project.features)
    assert result.is_err() and "unknown feature" in str(result.unwrap_err())


def test_missing_anchor_rejected(project):
    result = load_tier("tone", {"carries": ["tone"], "melody": True}, project.features)
    assert result.is_err()


def test_non_boolean_melody_rejected(project):
    table = {"carries": ["tone"], "anchor": "+syllabic", "melody": "yes"}
    assert load_tier("tone", table, project.features).is_err()


def test_a_feature_on_two_tiers_rejected(tmp_path, project):
    toml = tmp_path / "tiers.toml"
    toml.write_text(
        '[a]\ncarries = ["tone"]\nanchor = "+syllabic"\nmelody = true\n'
        '[b]\ncarries = ["tone"]\nanchor = "+syllabic"\nmelody = false\n'
    )
    result = load_tier_inventory(toml, project.features)
    assert result.is_err() and "carried by both" in str(result.unwrap_err())


def test_shipped_tiers_loaded_into_project(project):
    # load_project picks up the shipped inventories/tiers.toml.
    assert set(project.tiers.keys()) == {"tone", "stress"}
    assert project.tiers["tone"].melody is True
    assert project.tiers["stress"].melody is False


def test_stability_defaults_to_left(project):
    table = {"carries": ["tone"], "anchor": "+syllabic", "melody": True}
    assert load_tier("tone", table, project.features).unwrap().stability == "left"


def test_stability_right_loads(project):
    table = {"carries": ["tone"], "anchor": "+syllabic", "melody": True, "stability": "right"}
    assert load_tier("tone", table, project.features).unwrap().stability == "right"


def test_invalid_stability_rejected(project):
    table = {"carries": ["tone"], "anchor": "+syllabic", "melody": True, "stability": "up"}
    result = load_tier("tone", table, project.features)
    assert result.is_err() and "must be 'left' or 'right'" in str(result.unwrap_err())
