//! The tier loader, ported from `tests/loaders/test_tiers.py`.
//!
//! A tier IS a suprasegmental feature: its table is the feature definition (kind, values, short)
//! plus the association policy (anchor, melody, ocp, stray_erase, stability). Python's
//! `load_tier` is private in Rust, so its cases run through `load_tier_inventory`.

mod common;

use std::path::Path;

use fortis::loaders::inventories::load_tier_inventory;
use fortis::models::{FeatureInventory, Tier, TierDeclaration};
use toml::{Table, Value};

/// `_table()`: the register tier before any override.
fn table() -> Table {
    "kind = \"scalar\"\nvalues = { 1 = \"low\", 2 = \"high\" }\nanchor = \"+syllabic\"\nmelody = true".parse().unwrap()
}

/// Python's `load_tier("register", table, features)`, as a `tiers.toml` with that one table.
fn load_tier(table: Table, features: &mut FeatureInventory) -> Result<TierDeclaration, Vec<String>> {
    let mut file = Table::new();
    file.insert("register".into(), Value::Table(table));
    let source = common::memory(&[("tiers.toml", &file.to_string())]);
    let tiers = load_tier_inventory(&source, Path::new("tiers.toml"), features)?;
    Ok(tiers["register"].clone())
}

fn carried_names(tier: &TierDeclaration, features: &FeatureInventory) -> Vec<String> {
    tier.carries.iter().map(|f| features.name(*f).to_string()).collect()
}

#[test]
fn valid_tier_loads_and_registers_its_feature() {
    let mut features = common::default_project().features;
    let tier = load_tier(table(), &mut features).unwrap();
    assert!(tier.name == "register" && carried_names(&tier, &features) == ["register"]); // the tier IS its feature
    assert!(tier.melody && tier.ocp && tier.stray_erase); // defaults
    assert!(features.contains("register")); // the feature was registered onto the inventory
}

#[test]
fn missing_kind_rejected() {
    let mut table = table();
    table.remove("kind");
    let result = load_tier(table, &mut common::default_project().features);
    assert_eq!(result.unwrap_err(), ["Feature 'register' is missing the required field 'kind'"]);
}

#[test]
fn missing_anchor_rejected() {
    let mut table = table();
    table.remove("anchor");
    let result = load_tier(table, &mut common::default_project().features);
    assert_eq!(result.unwrap_err(), ["Tier 'register' is missing the required 'anchor' field"]);
}

#[test]
fn non_boolean_melody_rejected() {
    let mut table = table();
    table.insert("melody".into(), "yes".into());
    let result = load_tier(table, &mut common::default_project().features);
    assert_eq!(result.unwrap_err(), ["Tier 'register' needs a boolean 'melody' field"]);
}

#[test]
fn load_tier_inventory_from_file() {
    let mut features = common::default_project().features;
    let text = "[register]\nkind = \"scalar\"\nvalues = { 1 = \"low\", 2 = \"high\" }\n\
                anchor = \"+syllabic\"\nmelody = true\n";
    let tiers =
        load_tier_inventory(&common::memory(&[("tiers.toml", text)]), Path::new("tiers.toml"), &mut features).unwrap();
    assert!(tiers.contains_key("register") && carried_names(&tiers["register"], &features) == ["register"]);
    assert!(features.contains("register")); // the feature was registered while loading the tier
}

#[test]
fn shipped_tiers_loaded_into_project() {
    // load_project picks up the shipped projects/default/tiers.toml.
    let project = common::default_project();
    let mut names: Vec<&str> = project.tiers.keys().map(String::as_str).collect();
    names.sort();
    assert_eq!(names, ["stress", "tone"]);
    assert!(project.tiers["tone"].melody);
    assert!(!project.tiers["stress"].melody);
    let tone = project.features.id("tone").unwrap();
    assert_eq!(project.features.get(tone).tier, Tier::Syllable); // registered as suprasegmental
}

#[test]
fn stability_defaults_to_left() {
    assert_eq!(load_tier(table(), &mut common::default_project().features).unwrap().stability, "left");
}

#[test]
fn stability_right_loads() {
    let mut table = table();
    table.insert("stability".into(), "right".into());
    let tier = load_tier(table, &mut common::default_project().features).unwrap();
    assert_eq!(tier.stability, "right");
}

#[test]
fn invalid_stability_rejected() {
    let mut table = table();
    table.insert("stability".into(), "up".into());
    let result = load_tier(table, &mut common::default_project().features);
    assert_eq!(result.unwrap_err(), ["Tier 'register' field 'stability' must be 'left' or 'right'"]);
}
