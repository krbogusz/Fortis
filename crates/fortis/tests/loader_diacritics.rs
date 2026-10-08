//! Ports of `tests/loaders/test_diacritics.py`. The crate makes public only
//! `load_diacritic_inventory`, which reads TOML or CSV by the file extension. The cases for the
//! per-field helpers (`load_tier`, `load_kind`, `load_bool_field`, `load_bundle`) and for
//! `load_diacritic` go through it, with one TOML entry whose other fields are valid. The
//! expected error texts are the Python loaders' output.
//!
//! The combining mark U+0329 is written `\u0329` in TOML keys and `\u{329}` in Rust strings,
//! so that it stays visible in the source.

mod common;

use std::path::Path;

use fortis::loaders::inventories::{load_diacritic_inventory, load_feature_inventory};
use fortis::models::{DiacriticInventory, DiacriticKind, FeatureBundle, FeatureInventory, Tier};

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

/// `load_diacritic_inventory` on *text* saved as *name*; the extension picks the format.
fn load(name: &str, text: &str) -> Result<DiacriticInventory, Vec<String>> {
    load_diacritic_inventory(&common::memory(&[(name, text)]), Path::new(name), &features())
}

mod load_tier {
    use super::*;

    #[test]
    fn valid_segment() {
        let inv = load("diacritics.toml", r#""ʰ" = { tier = "segment", kind = "after", bundle = "+voice" }"#).unwrap();
        assert_eq!(inv.get("ʰ").unwrap().tier, Tier::Segment);
    }

    #[test]
    fn valid_syllable() {
        let text = r#""ˈ" = { tier = "syllable", kind = "before", bundle = "stress: primary" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert_eq!(inv.get("ˈ").unwrap().tier, Tier::Syllable);
    }

    #[test]
    fn missing() {
        let result = load("diacritics.toml", r#""ʰ" = { kind = "after", bundle = "+voice" }"#);
        assert_eq!(result.unwrap_err(), ["Diacritic 'ʰ' is missing the required 'tier' field"]);
    }

    #[test]
    fn invalid() {
        let result = load("diacritics.toml", r#""ʰ" = { tier = "prosodic", kind = "after", bundle = "+voice" }"#);
        assert_eq!(result.unwrap_err(), ["Diacritic 'ʰ' has invalid tier 'prosodic' (expected segment, syllable)"]);
    }
}

mod load_kind {
    use super::*;

    #[test]
    fn valid_before() {
        let text = r#""ˈ" = { tier = "syllable", kind = "before", bundle = "stress: primary" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert_eq!(inv.get("ˈ").unwrap().kind, DiacriticKind::Before);
    }

    #[test]
    fn valid_combining() {
        let text = r#""\u0329" = { tier = "segment", kind = "combining", bundle = "+syll" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert_eq!(inv.get("\u{329}").unwrap().kind, DiacriticKind::Combining);
    }

    #[test]
    fn valid_after() {
        let inv = load("diacritics.toml", r#""ʰ" = { tier = "segment", kind = "after", bundle = "+voice" }"#).unwrap();
        assert_eq!(inv.get("ʰ").unwrap().kind, DiacriticKind::After);
    }

    #[test]
    fn missing() {
        let result = load("diacritics.toml", r#""ʰ" = { tier = "segment", bundle = "+voice" }"#);
        assert_eq!(result.unwrap_err(), ["Diacritic 'ʰ' is missing the required 'kind' field"]);
    }
}

mod load_bool_field {
    // The Python cases for `true` and `false` read a field named `default`, which no diacritic
    // has; load_diacritic reads only its three flags, so these cases use `marks_boundary`.
    use super::*;

    #[test]
    fn r#true() {
        let text = r#""ˈ" = { tier = "syllable", kind = "before", bundle = "stress: primary", marks_boundary = true }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert!(inv.get("ˈ").unwrap().marks_boundary);
    }

    #[test]
    fn false_explicit() {
        let text =
            r#""ˈ" = { tier = "syllable", kind = "before", bundle = "stress: primary", marks_boundary = false }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert!(!inv.get("ˈ").unwrap().marks_boundary);
    }

    #[test]
    fn absent_defaults_to_false() {
        let text = r#""˥" = { tier = "syllable", kind = "after", bundle = "tone: 5" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert!(!inv.get("˥").unwrap().contour);
    }

    #[test]
    fn non_bool() {
        let text = r#""˥" = { tier = "syllable", kind = "after", bundle = "tone: 5", contour = "yes" }"#;
        let result = load("diacritics.toml", text);
        assert_eq!(result.unwrap_err(), ["Diacritic '˥' 'contour' must be 'true' or 'false'"]);
    }
}

mod load_bundle {
    use super::*;

    #[test]
    fn valid() {
        let result = load("diacritics.toml", r#""ʰ" = { tier = "segment", kind = "after", bundle = "+voice" }"#);
        assert!(result.is_ok());
    }

    #[test]
    fn missing() {
        let result = load("diacritics.toml", r#""ʰ" = { tier = "segment", kind = "after" }"#);
        assert_eq!(result.unwrap_err(), ["Diacritic 'ʰ' is missing the required 'bundle' field"]);
    }

    #[test]
    fn empty() {
        let result = load("diacritics.toml", r#""ʰ" = { tier = "segment", kind = "after", bundle = "" }"#);
        assert_eq!(result.unwrap_err(), ["Diacritic 'ʰ' is missing the required 'bundle' field"]);
    }
}

mod load_diacritic {
    use super::*;

    #[test]
    fn valid() {
        let text = r#""\u0329" = { tier = "segment", kind = "combining", bundle = "+syllabic" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        let d = inv.get("\u{329}").unwrap();
        assert_eq!(d.symbol, "\u{329}");
        assert_eq!(d.tier, Tier::Segment);
        assert_eq!(d.kind, DiacriticKind::Combining);
        assert!(!d.read_only);
    }

    #[test]
    fn missing_required_fields() {
        let result = load("diacritics.toml", r#""\u0329" = {}"#);
        assert_eq!(
            result.unwrap_err(),
            [
                "Diacritic '◌\u{329}' is missing the required 'tier' field",
                "Diacritic '◌\u{329}' is missing the required 'kind' field",
                "Diacritic '◌\u{329}' is missing the required 'bundle' field",
            ]
        );
    }
}

mod load_diacritic_inventory {
    use super::*;

    #[test]
    fn from_file() {
        let text = r#""\u0329" = { tier = "segment", kind = "combining", bundle = "+syll" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert!(inv.contains("\u{329}"));
    }

    #[test]
    fn dotted_circle_placeholder_is_stripped() {
        // A diacritic may be written on the dotted-circle carrier for legibility;
        // the carrier is dropped so it defines the bare combining mark.
        let text = r#""◌\u0329" = { tier = "segment", kind = "combining", bundle = "+syll" }"#;
        let inv = load("diacritics.toml", text).unwrap();
        assert!(inv.contains("\u{329}"));
        assert!(!inv.contains("◌\u{329}"));
        assert!(!inv.diacritics.iter().any(|d| d.symbol.contains('◌')));
    }

    #[test]
    fn duplicate_symbol() {
        // TOML forbids a repeated key, so the duplicate is the same mark with and without its
        // dotted-circle carrier. The Python test loaded a single entry and never reached this.
        let text = "\"◌\u{329}\" = { tier = \"segment\", kind = \"combining\", bundle = \"+syll\" }\n\
                    \"\u{329}\" = { tier = \"segment\", kind = \"combining\", bundle = \"-syll\" }\n";
        assert_eq!(load("diacritics.toml", text).unwrap_err(), ["Diacritic '◌\u{329}' is already defined"]);
    }
}

mod load_diacritic_inventory_csv {
    use super::*;

    #[test]
    fn from_file() {
        // The bundle has commas, so it is quoted.
        let text = "diacritic,tier,kind,bundle,marks_boundary,read_only,contour\n\
                    ʰ,segment,after,+voice,,,\n\
                    ʷ,segment,after,\"+labial, +rounded\",,,\n";
        let inv = load("diacritics.csv", text).unwrap();
        assert!(inv.contains("ʰ") && inv.contains("ʷ"));
    }

    #[test]
    fn duplicate_symbol() {
        let text = "diacritic,tier,kind,bundle\n◌\u{329},segment,combining,+syll\n\u{329},segment,combining,-syll\n";
        assert_eq!(load("diacritics.csv", text).unwrap_err(), ["Diacritic '◌\u{329}' is already defined"]);
    }

    #[test]
    fn dotted_circle_carrier_stripped() {
        let inv = load("diacritics.csv", "diacritic,tier,kind,bundle\n◌\u{329},segment,combining,+syll\n").unwrap();
        assert!(inv.contains("\u{329}") && !inv.contains("◌\u{329}"));
    }

    #[test]
    fn boolean_flags() {
        // An empty cell is false.
        let text = "diacritic,tier,kind,bundle,marks_boundary\nˈ,segment,before,+syll,true\nx,segment,after,+voice,\n";
        let inv = load("diacritics.csv", text).unwrap();
        assert!(inv.get("ˈ").unwrap().marks_boundary);
        assert!(!inv.get("x").unwrap().marks_boundary);
    }

    #[test]
    fn bad_boolean_is_an_error() {
        let result = load("diacritics.csv", "diacritic,tier,kind,bundle,read_only\nx,segment,after,+voice,maybe\n");
        assert_eq!(result.unwrap_err(), ["Diacritic 'x' 'read_only' must be 'true' or 'false'"]);
    }

    #[test]
    fn missing_required_column() {
        let result = load("diacritics.csv", "diacritic,kind,bundle\nx,after,+voice\n");
        assert_eq!(result.unwrap_err(), ["'diacritics.csv' must have a 'tier' column"]);
    }

    #[test]
    fn unknown_column_is_an_error() {
        let result = load("diacritics.csv", "diacritic,tier,kind,bundle,colour\nx,segment,after,+voice,blue\n");
        assert_eq!(result.unwrap_err(), ["'diacritics.csv' has unknown column(s): colour"]);
    }

    #[test]
    fn column_order_is_free() {
        let inv = load("diacritics.csv", "bundle,diacritic,kind,tier\n+syll,ʰ,after,segment\n").unwrap();
        assert_eq!(inv.get("ʰ").unwrap().kind, DiacriticKind::After);
    }
}

mod diacritic_csv_toml_equivalence {
    use super::*;

    type Flat = (String, Tier, DiacriticKind, FeatureBundle, bool, bool, bool);

    fn flat(inv: &DiacriticInventory) -> Vec<Flat> {
        inv.diacritics
            .iter()
            .map(|d| (d.symbol.clone(), d.tier, d.kind, d.bundle.clone(), d.contour, d.read_only, d.marks_boundary))
            .collect()
    }

    #[test]
    fn round_trip_is_identical() {
        let toml_text = r#""ʰ" = { tier = "segment", kind = "after", bundle = "+voice" }
"ʷ" = { tier = "segment", kind = "after", bundle = "+labial, +rounded" }
"\u0329" = { tier = "segment", kind = "combining", bundle = "+syll", read_only = true }
"#;
        let csv_text = "diacritic,tier,kind,bundle,marks_boundary,read_only,contour\n\
                        ʰ,segment,after,+voice,,,\n\
                        ʷ,segment,after,\"+labial, +rounded\",,,\n\
                        \u{329},segment,combining,+syll,,true,\n";
        let from_toml = load("diacritics.toml", toml_text).unwrap();
        let from_csv = load("diacritics.csv", csv_text).unwrap();
        assert_eq!(flat(&from_toml), flat(&from_csv));
    }
}
