"""Tests for the tier loader (loaders/tiers.py).

A tier IS a suprasegmental feature: its table is the feature definition (kind, values, short)
plus the association policy (anchor, melody, ocp, stray_erase, stability).
"""

from src.fortis.loaders.tiers import load_tier, load_tier_inventory


def _table(**overrides):
    table = {
        "kind": "scalar", "values": {1: "low", 2: "high"}, "anchor": "+syllabic", "melody": True,
    }
    table.update(overrides)
    return table


def test_valid_tier_loads_and_registers_its_feature(project):
    tier = load_tier("register", _table(), project.features).unwrap()
    assert tier.name == "register" and tier.carries == ("register",)  # the tier IS its feature
    assert tier.melody is True and tier.ocp is True and tier.stray_erase is True  # defaults
    assert "register" in project.features  # the feature was registered onto the inventory


def test_missing_kind_rejected(project):
    table = _table()
    del table["kind"]
    assert load_tier("register", table, project.features).is_err()


def test_missing_anchor_rejected(project):
    table = _table()
    del table["anchor"]
    assert load_tier("register", table, project.features).is_err()


def test_non_boolean_melody_rejected(project):
    assert load_tier("register", _table(melody="yes"), project.features).is_err()


def test_load_tier_inventory_from_file(tmp_path, project):
    toml = tmp_path / "tiers.toml"
    toml.write_text(
        '[register]\nkind = "scalar"\nvalues = { 1 = "low", 2 = "high" }\n'
        'anchor = "+syllabic"\nmelody = true\n'
    )
    tiers = load_tier_inventory(toml, project.features).unwrap()
    assert "register" in tiers and tiers["register"].carries == ("register",)
    assert "register" in project.features  # the feature was registered while loading the tier


def test_shipped_tiers_loaded_into_project(project):
    # load_project picks up the shipped inventories/tiers.toml.
    assert set(project.tiers.keys()) == {"tone", "stress"}
    assert project.tiers["tone"].melody is True
    assert project.tiers["stress"].melody is False
    assert project.features["tone"].tier.value == "syllable"  # registered as suprasegmental


def test_stability_defaults_to_left(project):
    assert load_tier("register", _table(), project.features).unwrap().stability == "left"


def test_stability_right_loads(project):
    tier = load_tier("register", _table(stability="right"), project.features).unwrap()
    assert tier.stability == "right"


def test_invalid_stability_rejected(project):
    result = load_tier("register", _table(stability="up"), project.features)
    assert result.is_err() and "must be 'left' or 'right'" in str(result.unwrap_err())
