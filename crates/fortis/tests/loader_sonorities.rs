//! Ports of `tests/loaders/test_sonorities.py`. The crate makes public only
//! `load_sonorities_inventory`, which reads TOML or CSV by the file extension. The cases for the
//! per-field helpers (`load_level`, `load_bundle`) and for `load_sonority` go through it, with
//! one TOML entry. The expected error texts are the Python loaders' output.

mod common;

use std::path::Path;

use fortis::loaders::inventories::{load_feature_inventory, load_sonorities_inventory};
use fortis::models::{FeatureInventory, PatternBundle, Sonority};

/// The `features` fixture of `tests/conftest.py` (`MINIMAL_FEATURES_TOML`), its plain features as
/// inline tables.
const MINIMAL_FEATURES_TOML: &str = r#"
consonantal = { tier = "segment", kind = "binary", short = "cons" }
sonorant = { tier = "segment", kind = "binary", short = "son" }
syllabic = { tier = "segment", kind = "binary", short = "syll" }
nasal = { tier = "segment", kind = "binary", short = "nas" }
lateral = { tier = "segment", kind = "binary", short = "lat" }
continuant = { tier = "segment", kind = "binary", short = "cont" }
labial = { tier = "segment", kind = "binary", short = "lab" }
rounded = { tier = "segment", kind = "binary", short = "rd" }
front = { tier = "segment", kind = "binary", short = "frnt" }
high = { tier = "segment", kind = "binary", short = "hi" }
voice = { tier = "segment", kind = "binary", short = "vc" }
glop = { tier = "segment", kind = "binary", short = "gl" }
tense = { tier = "segment", kind = "binary", short = "tns" }

[stress]
tier = "syllable"
kind = "scalar"
short = "str"
values = { 1 = "primary", 2 = "secondary" }

[tone]
tier = "syllable"
kind = "scalar"
short = "t"
values = { 1 = "low", 2 = "mid", 3 = "high", 4 = "extra_high", 5 = "super_high" }

[length]
tier = "segment"
kind = "scalar"
short = "ln"
values = { 1 = "short", 2 = "long", 3 = "overlong" }

[manner]
tier = "segment"
kind = "unary"
short = "man"
children = ["continuant", "sonorant", "nasal", "lateral"]
"#;

fn features() -> FeatureInventory {
    let src = common::memory(&[("features.toml", MINIMAL_FEATURES_TOML)]);
    load_feature_inventory(&src, Path::new("features.toml")).expect("the minimal features load")
}

/// `load_sonorities_inventory` on *text* saved as *name*; the extension picks the format.
fn load(name: &str, text: &str) -> Result<Vec<Sonority>, Vec<String>> {
    load_sonorities_inventory(&common::memory(&[(name, text)]), Path::new(name), &features())
}

/// `inv[label]`.
fn get<'a>(inv: &'a [Sonority], label: &str) -> &'a Sonority {
    inv.iter().find(|s| s.label == label).unwrap()
}

mod load_level {
    // An empty bundle is the catch-all level, so these entries isolate the level field.
    use super::*;

    #[test]
    fn valid() {
        let inv = load("sonorities.toml", r#"vowel = { level = 7, bundle = "" }"#).unwrap();
        assert_eq!(get(&inv, "vowel").level, 7);
    }

    #[test]
    fn missing() {
        let result = load("sonorities.toml", r#"vowel = { bundle = "" }"#);
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' is missing the required 'level' field"]);
    }

    #[test]
    fn zero() {
        let result = load("sonorities.toml", r#"vowel = { level = 0, bundle = "" }"#);
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' has invalid level '0' (expected a positive integer)"]);
    }

    #[test]
    fn negative() {
        let result = load("sonorities.toml", r#"vowel = { level = -1, bundle = "" }"#);
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' has invalid level '-1' (expected a positive integer)"]);
    }

    #[test]
    fn non_integer() {
        let result = load("sonorities.toml", r#"vowel = { level = "high", bundle = "" }"#);
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' has invalid level 'high' (expected a positive integer)"]);
    }
}

mod load_bundle {
    use super::*;

    #[test]
    fn valid() {
        let inv = load("sonorities.toml", r#"vowel = { level = 7, bundle = "syllabic: +, consonantal: -" }"#).unwrap();
        assert!(get(&inv, "vowel").bundle.is_some());
    }

    #[test]
    fn empty_string_returns_none() {
        let inv = load("sonorities.toml", r#"vowel = { level = 7, bundle = "" }"#).unwrap();
        assert!(get(&inv, "vowel").bundle.is_none());
    }

    #[test]
    fn missing() {
        let result = load("sonorities.toml", "vowel = { level = 7 }");
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' is missing the required 'bundle' field"]);
    }
}

mod load_sonority {
    use super::*;

    #[test]
    fn valid() {
        let inv = load("sonorities.toml", r#"vowel = { level = 7, bundle = "syllabic: +, consonantal: -" }"#).unwrap();
        let s = get(&inv, "vowel");
        assert_eq!(s.label, "vowel");
        assert_eq!(s.level, 7);
        assert!(s.bundle.is_some());
    }

    #[test]
    fn missing_level() {
        let result = load("sonorities.toml", r#"vowel = { bundle = "syllabic: +" }"#);
        assert_eq!(result.unwrap_err(), ["Sonority 'vowel' is missing the required 'level' field"]);
    }
}

mod load_sonorities_inventory {
    use super::*;

    #[test]
    fn from_file() {
        let text = r#"vowel = { level = 7, bundle = "syllabic: +, consonantal: -" }
stop = { level = 1, bundle = "sonorant: -" }
"#;
        let inv = load("sonorities.toml", text).unwrap();
        assert!(inv.iter().any(|s| s.label == "vowel"));
        assert_eq!(get(&inv, "vowel").level, 7);
    }

    #[test]
    fn duplicate_levels() {
        let text = r#"vowel = { level = 7, bundle = "syllabic: +" }
glide = { level = 7, bundle = "consonantal: -" }
"#;
        let result = load("sonorities.toml", text);
        assert_eq!(result.unwrap_err(), ["Sonority 'glide' and 'vowel' share level 7"]);
    }
}

mod load_sonorities_inventory_csv {
    use super::*;

    #[test]
    fn from_file_preserves_order() {
        // Row order is first-match order: vowel outranks the rest.
        let text = "name,level,bundle\n\
                    vowel,7,\"syllabic: +, consonantal: -\"\n\
                    nasal,3,\"sonorant: +, nasal: +\"\n\
                    stop,1,sonorant: -\n";
        let inv = load("sonorities.csv", text).unwrap();
        let labels: Vec<&str> = inv.iter().map(|s| s.label.as_str()).collect();
        assert_eq!(labels, ["vowel", "nasal", "stop"]);
        assert_eq!(get(&inv, "vowel").level, 7);
    }

    #[test]
    fn empty_bundle_is_catch_all() {
        let inv = load("sonorities.csv", "name,level,bundle\nother,1,\n").unwrap();
        assert!(get(&inv, "other").bundle.is_none());
    }

    #[test]
    fn duplicate_level_is_an_error() {
        let result = load("sonorities.csv", "name,level,bundle\na,1,sonorant: -\nb,1,sonorant: +\n");
        assert_eq!(result.unwrap_err(), ["Sonority 'b' and 'a' share level 1"]);
    }

    #[test]
    fn bad_level_is_an_error() {
        let result = load("sonorities.csv", "name,level,bundle\na,high,sonorant: -\n");
        assert_eq!(result.unwrap_err(), ["Sonority 'a' has invalid level 'high' (expected a positive integer)"]);
    }

    #[test]
    fn missing_required_column() {
        let result = load("sonorities.csv", "name,bundle\na,sonorant: -\n");
        assert_eq!(result.unwrap_err(), ["'sonorities.csv' must have a 'level' column"]);
    }

    #[test]
    fn unknown_column_is_an_error() {
        let result = load("sonorities.csv", "name,level,bundle,colour\na,1,sonorant: -,blue\n");
        assert_eq!(result.unwrap_err(), ["'sonorities.csv' has unknown column(s): colour"]);
    }
}

mod sonority_csv_toml_equivalence {
    use super::*;

    fn flat(inv: &[Sonority]) -> Vec<(String, i64, Option<PatternBundle>)> {
        inv.iter().map(|s| (s.label.clone(), s.level, s.bundle.clone())).collect()
    }

    #[test]
    fn round_trip_is_identical() {
        let toml_text = r#"vowel = { level = 7, bundle = "syllabic: +, consonantal: -" }
nasal = { level = 3, bundle = "sonorant: +, nasal: +" }
stop = { level = 1, bundle = "sonorant: -" }
"#;
        let csv_text = "name,level,bundle\n\
                        vowel,7,\"syllabic: +, consonantal: -\"\n\
                        nasal,3,\"sonorant: +, nasal: +\"\n\
                        stop,1,sonorant: -\n";
        let from_toml = load("sonorities.toml", toml_text).unwrap();
        let from_csv = load("sonorities.csv", csv_text).unwrap();
        assert_eq!(flat(&from_toml), flat(&from_csv));
    }
}
