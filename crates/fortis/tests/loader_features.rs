//! Ports of `tests/loaders/test_features.py`. The crate makes public only `load_feature` and
//! `load_feature_inventory`, so the cases for the per-field helpers (`load_tier`, `load_kind`,
//! `load_short`, `load_values`, `load_children`) go through `load_feature`, with a valid `kind`
//! beside the field under test. The expected error texts are the Python loaders' output.

mod common;

use std::path::Path;

use fortis::loaders::inventories::{load_feature, load_feature_inventory};
use fortis::models::{Feature, FeatureInventory, FeatureKind, Tier};

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

/// `load_feature(name, def)` with *def* written as the body of a TOML inline table.
fn feature(name: &str, def: &str) -> Result<Feature, Vec<String>> {
    let doc: toml::Table = format!("def = {{ {def} }}").parse().unwrap();
    load_feature(name, doc["def"].as_table().unwrap())
}

fn get<'a>(features: &'a FeatureInventory, name: &str) -> &'a Feature {
    features.get(features.id(name).unwrap())
}

mod load_tier {
    use super::*;

    #[test]
    fn valid_segment() {
        let result = feature("voice", r#"tier = "segment", kind = "binary""#);
        assert_eq!(result.unwrap().tier, Tier::Segment);
    }

    #[test]
    fn valid_syllable() {
        let result = feature("voice", r#"tier = "syllable", kind = "binary""#);
        assert_eq!(result.unwrap().tier, Tier::Syllable);
    }

    #[test]
    fn missing_defaults_to_segment() {
        // No tier means segmental: features.toml is segment-only; suprasegmentals live in tiers.toml.
        let result = feature("voice", r#"kind = "binary""#);
        assert_eq!(result.unwrap().tier, Tier::Segment);
    }

    #[test]
    fn invalid() {
        let result = feature("voice", r#"tier = "prosodic", kind = "binary""#);
        assert_eq!(
            result.unwrap_err(),
            ["Feature 'voice' has an invalid tier 'prosodic' (expected segment, syllable)"]
        );
    }
}

mod load_kind {
    use super::*;

    #[test]
    fn valid_unary() {
        let result = feature("manner", r#"kind = "unary""#);
        assert_eq!(result.unwrap().kind, FeatureKind::Unary);
    }

    #[test]
    fn valid_binary() {
        let result = feature("manner", r#"kind = "binary""#);
        assert_eq!(result.unwrap().kind, FeatureKind::Binary);
    }

    #[test]
    fn valid_scalar() {
        // load_feature also reads the values of a scalar feature, so the case needs some.
        let result = feature("length", r#"kind = "scalar", values = { 1 = "short" }"#);
        assert_eq!(result.unwrap().kind, FeatureKind::Scalar);
    }

    #[test]
    fn missing() {
        let result = feature("manner", "");
        assert_eq!(result.unwrap_err(), ["Feature 'manner' is missing the required field 'kind'"]);
    }

    #[test]
    fn invalid() {
        let result = feature("manner", r#"kind = "trinary""#);
        assert_eq!(
            result.unwrap_err(),
            ["Feature 'manner' has an invalid kind 'trinary' (expected unary, binary, scalar)"]
        );
    }
}

mod load_short {
    use super::*;

    #[test]
    fn present() {
        let result = feature("consonantal", r#"kind = "binary", short = "cons""#);
        assert_eq!(result.unwrap().short_name, "cons");
    }

    #[test]
    fn missing_defaults_to_name() {
        let result = feature("consonantal", r#"kind = "binary""#);
        assert_eq!(result.unwrap().short_name, "consonantal");
    }

    #[test]
    fn whitespace_stripped() {
        let result = feature("consonantal", r#"kind = "binary", short = "  cons  ""#);
        assert_eq!(result.unwrap().short_name, "cons");
    }

    #[test]
    fn whitespace_in_name_rejected() {
        let result = feature("consonantal", r#"kind = "binary", short = "con son""#);
        assert_eq!(
            result.unwrap_err(),
            ["Feature 'consonantal' has a short name 'con son' that contains whitespace"]
        );
    }
}

mod load_values {
    use super::*;

    #[test]
    fn unary() {
        let result = feature("manner", r#"kind = "unary""#);
        assert_eq!(result.unwrap().values, [(1, "present".to_string())]);
    }

    #[test]
    fn binary() {
        let result = feature("voice", r#"kind = "binary""#);
        assert_eq!(result.unwrap().values, [(0, "absent".to_string()), (1, "present".to_string())]);
    }

    #[test]
    fn scalar_with_values() {
        let result = feature("tone", r#"kind = "scalar", values = { 1 = "low", 2 = "high" }"#);
        let tone = result.unwrap();
        assert_eq!(tone.label_of(1), Some("low"));
        assert_eq!(tone.label_of(2), Some("high"));
    }

    #[test]
    fn scalar_missing_values() {
        let result = feature("tone", r#"kind = "scalar""#);
        assert_eq!(result.unwrap_err(), ["Feature 'tone' is scalar, but does not have specified 'values'"]);
    }
}

mod load_children {
    use super::*;

    #[test]
    fn absent() {
        let result = feature("voice", r#"kind = "binary""#);
        assert_eq!(result.unwrap().children, None);
    }

    #[test]
    fn string() {
        let result = feature("manner", r#"kind = "unary", children = "continuant""#);
        assert_eq!(result.unwrap().children, Some(vec!["continuant".into()]));
    }

    #[test]
    fn list() {
        let result = feature("manner", r#"kind = "unary", children = ["continuant", "sonorant"]"#);
        assert_eq!(result.unwrap().children, Some(vec!["continuant".into(), "sonorant".into()]));
    }

    #[test]
    fn empty_string() {
        let result = feature("manner", r#"kind = "unary", children = """#);
        assert_eq!(result.unwrap().children, None);
    }

    #[test]
    fn empty_list() {
        let result = feature("manner", r#"kind = "unary", children = []"#);
        assert_eq!(result.unwrap().children, None);
    }
}

mod load_feature {
    use super::*;

    #[test]
    fn valid_binary() {
        let result = feature("voice", r#"tier = "segment", kind = "binary", short = "vc""#);
        let voice = result.unwrap();
        assert_eq!(voice.name, "voice");
        assert_eq!(voice.tier, Tier::Segment);
        assert_eq!(voice.kind, FeatureKind::Binary);
        assert_eq!(voice.short_name, "vc");
    }

    #[test]
    fn valid_unary_with_children() {
        let result = feature(
            "manner",
            r#"tier = "segment", kind = "unary", short = "man", children = ["continuant", "sonorant"]"#,
        );
        assert_eq!(result.unwrap().children, Some(vec!["continuant".into(), "sonorant".into()]));
    }

    #[test]
    fn no_tier_defaults_to_segment() {
        let result = feature("voice", r#"kind = "binary""#);
        assert_eq!(result.unwrap().tier, Tier::Segment);
    }

    #[test]
    fn missing_kind() {
        let result = feature("voice", "");
        assert_eq!(result.unwrap_err(), ["Feature 'voice' is missing the required field 'kind'"]);
    }

    #[test]
    fn multiple_errors_collected() {
        let result = feature("voice", r#"tier = "prosodic", kind = "bad""#);
        assert_eq!(
            result.unwrap_err(),
            [
                "Feature 'voice' has an invalid tier 'prosodic' (expected segment, syllable)",
                "Feature 'voice' has an invalid kind 'bad' (expected unary, binary, scalar)",
            ]
        );
    }
}

mod load_feature_inventory {
    use super::*;

    #[test]
    fn from_file() {
        let features = features();
        assert!(features.contains("consonantal"));
        assert!(features.contains("voice"));
        assert_eq!(get(&features, "consonantal").kind, FeatureKind::Binary);
        assert_eq!(get(&features, "stress").kind, FeatureKind::Scalar);
    }

    #[test]
    fn hierarchy() {
        let features = features();
        let manner = features.id("manner").unwrap();
        assert!(!features.children(manner).is_empty());
        assert!(features.children(features.id("voice").unwrap()).is_empty());
        assert!(features.children(manner).contains(&features.id("continuant").unwrap()));
    }

    #[test]
    fn scalar_values() {
        let features = features();
        assert_eq!(get(&features, "tone").label_of(1), Some("low"));
        assert_eq!(get(&features, "tone").label_of(5), Some("super_high"));
    }

    #[test]
    fn root_is_synthesized_as_the_segmental_apex() {
        // The minimal fixture declares no root; the loader builds one over the top-level
        // segmental features. Suprasegmentals (tone, stress) stay outside it.
        let features = features();
        assert!(features.contains("root"));
        assert_eq!(get(&features, "root").parent, None);
        assert_eq!(get(&features, "consonantal").parent.as_deref(), Some("root"));
        assert_eq!(get(&features, "manner").parent.as_deref(), Some("root"));
        assert_eq!(get(&features, "tone").parent, None);
    }

    #[test]
    fn two_segmental_tops_share_a_synthesized_root() {
        let text = r#"a = { tier = "segment", kind = "binary", short = "a" }
b = { tier = "segment", kind = "binary", short = "b" }
"#;
        let src = common::memory(&[("f.toml", text)]);
        let features = load_feature_inventory(&src, Path::new("f.toml")).unwrap();
        assert_eq!(get(&features, "a").parent.as_deref(), Some("root"));
        assert_eq!(get(&features, "b").parent.as_deref(), Some("root"));
    }
}
