//! Ports of `tests/loaders/test_letters.py`. The crate makes public only `load_letter_inventory`,
//! so the cases for `load_letter` go through it, with the row written as a one-row CSV. The
//! expected error texts are the Python loaders' output.

mod common;

use std::path::Path;

use fortis::loaders::inventories::{load_feature_inventory, load_letter_inventory};
use fortis::models::{FeatureInventory, LetterInventory};

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

/// `load_letter_inventory` on *text* as `letters.csv`.
fn load(text: &str, features: &FeatureInventory) -> Result<LetterInventory, Vec<String>> {
    load_letter_inventory(&common::memory(&[("letters.csv", text)]), Path::new("letters.csv"), features)
}

mod load_letter {
    use super::*;

    #[test]
    fn valid_letter() {
        // The inventory checks the geometry, which load_letter does not: manner parents
        // sonorant, nasal and lateral in the fixture, so the row sets it too.
        let features = features();
        let inv = load("symbol,consonantal,manner,sonorant,nasal,lateral\nm,+,+,+,+,-\n", &features).unwrap();
        let letter = inv.get("m").unwrap();
        assert_eq!(letter.symbol, "m");
        assert!(letter.bundle.contains(features.id("consonantal").unwrap()));
    }

    #[test]
    fn missing_symbol() {
        let result = load("consonantal\n+\n", &features());
        assert_eq!(result.unwrap_err(), ["A letter is missing the required 'symbol' field"]);
    }

    #[test]
    fn empty_cell_skipped() {
        let features = features();
        let inv = load("symbol,consonantal,voice\nm,+,\n", &features).unwrap();
        let letter = inv.get("m").unwrap();
        assert!(letter.bundle.contains(features.id("consonantal").unwrap()));
        assert!(!letter.bundle.contains(features.id("voice").unwrap()));
    }

    #[test]
    fn unknown_feature() {
        let result = load("symbol,nonexistent\nm,+\n", &features());
        assert_eq!(
            result.unwrap_err(),
            [
                "CSV column 'nonexistent' is not a known feature",
                "Letter 'm' has a feature 'nonexistent' that is unknown",
            ]
        );
    }
}

mod load_letter_inventory {
    use super::*;

    #[test]
    fn from_file() {
        // manner parents sonorant/nasal in the fixture geometry, so it must be set too
        let inv = load("symbol,consonantal,manner,sonorant,nasal\nm,+,+,+,+\nn,-,+,+,-\n", &features()).unwrap();
        assert!(inv.contains("m"));
        assert!(inv.contains("n"));
    }

    #[test]
    fn duplicate_symbol() {
        let result = load("symbol,consonantal\nm,+\nm,+\n", &features());
        assert_eq!(result.unwrap_err(), ["Duplicate symbol 'm'"]);
    }

    #[test]
    fn missing_file() {
        let result = load_letter_inventory(&common::memory(&[]), Path::new("nonexistent.csv"), &features());
        assert_eq!(result.unwrap_err(), ["There is no file at 'nonexistent.csv'"]);
    }
}

mod geometry_validation {
    // A letter's bundle is a full segment description: every set feature needs its
    // declared parent set too. (Diacritics are deltas and are deliberately exempt.)
    use super::*;

    #[test]
    fn child_without_parent_rejected() {
        // `front` is declared under `lingual`: setting the child alone describes
        // a segment the geometry cannot represent.
        let project = common::default_project();
        let result = load("symbol,syllabic,consonantal,front\nx,+,-,+\n", &project.features);
        assert_eq!(result.unwrap_err(), ["Letter 'x' sets 'front' but not its parent 'lingual'"]);
    }

    #[test]
    fn full_chain_accepted() {
        let project = common::default_project();
        let result = load("symbol,syllabic,consonantal,oral,lingual,front\nx,+,-,+,+,+\n", &project.features);
        assert!(result.is_ok());
    }

    #[test]
    fn padded_symbol_rejected() {
        let project = common::default_project();
        let result = load("symbol,syllabic,consonantal\nm ,+,-\n", &project.features);
        assert_eq!(result.unwrap_err(), ["Letter 'm' has leading/trailing whitespace in its symbol cell"]);
    }
}
