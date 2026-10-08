//! Port of `tests/parsing/test_bundles.py`: bundle and value parsing.

mod common;

use std::path::Path;

use fortis::loaders::inventories::load_feature_inventory;
use fortis::models::*;
use fortis::parsing::bundles::*;

/// The `MINIMAL_FEATURES_TOML` fixture of `tests/conftest.py`.
const MINIMAL_FEATURES_TOML: &str = r#"[consonantal]
tier = "segment"
kind = "binary"
short = "cons"

[sonorant]
tier = "segment"
kind = "binary"
short = "son"

[syllabic]
tier = "segment"
kind = "binary"
short = "syll"

[nasal]
tier = "segment"
kind = "binary"
short = "nas"

[lateral]
tier = "segment"
kind = "binary"
short = "lat"

[continuant]
tier = "segment"
kind = "binary"
short = "cont"

[labial]
tier = "segment"
kind = "binary"
short = "lab"

[rounded]
tier = "segment"
kind = "binary"
short = "rd"

[front]
tier = "segment"
kind = "binary"
short = "frnt"

[high]
tier = "segment"
kind = "binary"
short = "hi"

[voice]
tier = "segment"
kind = "binary"
short = "vc"

[glop]
tier = "segment"
kind = "binary"
short = "gl"

[tense]
tier = "segment"
kind = "binary"
short = "tns"

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

/// The `features` fixture: the minimal inventory, loaded through the real loader.
fn features() -> FeatureInventory {
    let src = common::memory(&[("features.toml", MINIMAL_FEATURES_TOML)]);
    load_feature_inventory(&src, Path::new("features.toml")).unwrap()
}

fn id(f: &FeatureInventory, name: &str) -> FeatId {
    f.id(name).unwrap()
}

fn contour(limbs: &[Limb]) -> Value {
    Value::Contour(limbs.into())
}

fn alpha(op: AlphaOp, unary: bool) -> Limb {
    Limb::Alpha(AlphaRef { var: 'α', op, unary })
}

/// The alpha reference a single-limb value holds.
fn alpha_of(value: &Value) -> AlphaRef {
    match value {
        Value::One(Limb::Alpha(a)) => *a,
        other => panic!("expected an alpha reference, found {other:?}"),
    }
}

fn pattern_spec<'a>(bundle: &'a [PatternSpec], f: &FeatureInventory, name: &str) -> &'a PatternSpec {
    bundle.iter().find(|s| s.feature == id(f, name)).unwrap_or_else(|| panic!("no '{name}' in the bundle"))
}

fn names(bundle: &[PatternSpec], f: &FeatureInventory) -> Vec<String> {
    let mut names: Vec<String> = bundle.iter().map(|s| f.name(s.feature).to_string()).collect();
    names.sort();
    names
}

mod parse_value {
    use super::*;

    #[test]
    fn unary_present() {
        let f = features();
        let (feature, value) = parse_feature_spec("+syllabic", &f, None).unwrap();
        assert_eq!(f.name(feature), "syllabic");
        assert_eq!(value, Value::int(1));
    }

    #[test]
    fn binary_present() {
        let f = features();
        let (feature, value) = parse_feature_spec("+consonantal", &f, None).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, Value::int(1));
    }

    #[test]
    fn binary_absent() {
        let f = features();
        let (feature, value) = parse_feature_spec("-consonantal", &f, None).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, Value::int(0));
    }

    #[test]
    fn binary_numeric() {
        let f = features();
        let (feature, value) = parse_feature_spec("1", &f, Some(id(&f, "consonantal"))).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, Value::int(1));
    }

    #[test]
    fn scalar_numeric_with_colon() {
        let f = features();
        let (feature, value) = parse_feature_spec(":2", &f, Some(id(&f, "length"))).unwrap();
        assert_eq!(f.name(feature), "length");
        assert_eq!(value, Value::int(2));
    }

    #[test]
    fn scalar_numeric_bare() {
        let f = features();
        let (feature, value) = parse_feature_spec("2", &f, Some(id(&f, "length"))).unwrap();
        assert_eq!(f.name(feature), "length");
        assert_eq!(value, Value::int(2));
    }

    #[test]
    fn contour_value() {
        let f = features();
        let (feature, value) = parse_feature_spec("1>0", &f, Some(id(&f, "consonantal"))).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, contour(&[Limb::Int(1), Limb::Int(0)]));
    }

    #[test]
    fn unspecified() {
        let f = features();
        let (feature, value) = parse_feature_spec("∅", &f, Some(id(&f, "consonantal"))).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, Value::NONE);
    }

    #[test]
    fn alpha_in_realized_context() {
        let f = features();
        assert_eq!(
            parse_feature_spec("αconsonantal", &f, None).unwrap_err(),
            "Alpha value notation is not supported for realized features"
        );
    }

    // test_unknown_feature_returns_error is not ported: Rust takes the feature as a `FeatId`,
    // so an unknown feature name cannot be passed.

    #[test]
    fn unary_name_only() {
        let f = features();
        let (feature, value) = parse_feature_spec("manner", &f, None).unwrap();
        assert_eq!(f.name(feature), "manner");
        assert_eq!(value, Value::int(1));
    }

    #[test]
    fn bare_non_unary_realized_feature_rejected() {
        let f = features();
        assert_eq!(
            parse_feature_spec("nasal", &f, None).unwrap_err(),
            "Realized feature 'nasal' needs an explicit value; a bare feature name matches any value and is pattern-only"
        );
    }

    #[test]
    fn bare_unary_realized_feature_ok() {
        let f = features();
        let (_, value) = parse_feature_spec("manner", &f, None).unwrap();
        assert_eq!(value, Value::int(1));
    }

    #[test]
    fn binary_name_with_plus() {
        let f = features();
        let (feature, value) = parse_feature_spec("+consonantal", &f, None).unwrap();
        assert_eq!(f.name(feature), "consonantal");
        assert_eq!(value, Value::int(1));
    }
}

mod parse_feature_bundle {
    use super::*;

    #[test]
    fn single_feature() {
        let f = features();
        let bundle = parse_feature_bundle("+voice", &f).unwrap();
        assert_eq!(bundle.get(id(&f, "voice")), Some(&Value::int(1)));
    }

    #[test]
    fn scalar_in_bundle() {
        let f = features();
        let bundle = parse_feature_bundle("stress:1", &f).unwrap();
        assert_eq!(bundle.get(id(&f, "stress")), Some(&Value::int(1)));
    }

    #[test]
    fn unknown_feature_error() {
        // A short name counts only as a whole word: the 't' inside "nonexistent" is not tone's.
        let f = features();
        assert_eq!(
            parse_feature_bundle("+nonexistent", &f).unwrap_err(),
            ["Could not identify feature spec from string '+nonexistent'"]
        );
    }

    #[test]
    fn multi_feature_bundle() {
        let f = features();
        let bundle = parse_feature_bundle("+voice, -nasal", &f).unwrap();
        assert_eq!(bundle.get(id(&f, "voice")), Some(&Value::int(1)));
        assert_eq!(bundle.get(id(&f, "nasal")), Some(&Value::int(0)));
    }

    #[test]
    fn multi_feature_with_scalar() {
        let f = features();
        let bundle = parse_feature_bundle("+voice, stress:1", &f).unwrap();
        assert_eq!(bundle.get(id(&f, "voice")), Some(&Value::int(1)));
        assert_eq!(bundle.get(id(&f, "stress")), Some(&Value::int(1)));
    }

    #[test]
    fn duplicate_feature_is_an_error() {
        let f = features();
        assert_eq!(
            parse_feature_bundle("+voice, -voice", &f).unwrap_err(),
            ["feature 'voice' is specified more than once"]
        );
    }

    #[test]
    fn duplicate_feature_error_also_in_pattern_bundles() {
        // The Python test used 'aperture', which the minimal inventory lacks, so it failed on the
        // unknown feature instead. 'tone' is a scalar the inventory declares.
        let f = features();
        assert_eq!(
            parse_pattern_bundle("tone: high, tone: low", &f).unwrap_err(),
            ["feature 'tone' is specified more than once"]
        );
    }
}

mod parse_pattern_spec {
    use super::*;

    #[test]
    fn bare_scalar_label_in_a_conditional() {
        // The space in 'mid tone' separates the label from the feature, inside '<n: …>' too.
        let f = features();
        assert_eq!(
            parse_pattern_spec("<1: mid tone>", &f).unwrap_err(),
            "Scalar feature 'tone': a value label must follow a colon (write 'tone: mid', not a bare label)"
        );
        assert_eq!(parse_pattern_spec("<1: tone: mid>", &f).unwrap().condition_label, Some(1));
    }

    #[test]
    fn simple_present() {
        let f = features();
        let spec = parse_pattern_spec("+nasal", &f).unwrap();
        assert_eq!(f.name(spec.feature), "nasal");
        assert_eq!(spec.value, Value::int(1));
        assert!(!spec.negated);
    }

    #[test]
    fn absent() {
        let f = features();
        let spec = parse_pattern_spec("-nasal", &f).unwrap();
        assert_eq!(f.name(spec.feature), "nasal");
        assert_eq!(spec.value, Value::int(0));
    }

    #[test]
    fn contour_position() {
        let f = features();
        let spec = parse_pattern_spec("tone:5@initial", &f).unwrap();
        assert_eq!(f.name(spec.feature), "tone");
        assert_eq!(spec.contour_position, ContourPosition::Edge(ContourEdge::Initial));
    }

    #[test]
    fn alpha_variable() {
        let f = features();
        let spec = parse_pattern_spec("αconsonantal", &f).unwrap();
        let a = alpha_of(&spec.value);
        assert_eq!(a.var, 'α');
        assert_eq!(a.op, AlphaOp::Same);
    }

    #[test]
    fn negated_bare_feature() {
        let f = features();
        let spec = parse_pattern_spec("!nasal", &f).unwrap();
        assert_eq!(f.name(spec.feature), "nasal");
        assert_eq!(spec.value, Value::One(Limb::Any));
        assert!(spec.negated);
    }

    #[test]
    fn negated_bare_unary_feature() {
        let f = features();
        let spec = parse_pattern_spec("!manner", &f).unwrap();
        assert_eq!(spec.value, Value::int(1));
        assert!(spec.negated);
    }

    #[test]
    fn alpha_other_is_value_level_not_spec_negation() {
        let f = features();
        let spec = parse_pattern_spec("voice: !α", &f).unwrap();
        assert!(!spec.negated);
        assert_eq!(alpha_of(&spec.value).op, AlphaOp::Other);
    }

    #[test]
    fn alpha_other_limb_in_contour() {
        let f = features();
        let spec = parse_pattern_spec("tone: !α>2", &f).unwrap();
        assert!(!spec.negated);
        assert_eq!(spec.value, contour(&[alpha(AlphaOp::Other, false), Limb::Int(2)]));
    }

    #[test]
    fn conditional_feature() {
        let f = features();
        let spec = parse_pattern_spec("<1: +high>", &f).unwrap();
        assert_eq!(f.name(spec.feature), "high");
        assert_eq!(spec.value, Value::int(1));
        assert_eq!(spec.condition_label, Some(1));
    }

    #[test]
    fn conditional_negated_condition() {
        let f = features();
        let spec = parse_pattern_spec("<1: !high>", &f).unwrap();
        assert!(spec.negated);
        assert_eq!(spec.condition_label, Some(1));
    }

    #[test]
    fn conditional_alpha_condition() {
        let f = features();
        let spec = parse_pattern_spec("<2: αvoice>", &f).unwrap();
        assert_eq!(alpha_of(&spec.value).op, AlphaOp::Same);
        assert_eq!(spec.condition_label, Some(2));
    }

    #[test]
    fn conditional_contour_inner() {
        let f = features();
        let spec = parse_pattern_spec("<1: tone: 1>2>", &f).unwrap();
        assert_eq!(f.name(spec.feature), "tone");
        assert_eq!(spec.value, contour(&[Limb::Int(1), Limb::Int(2)]));
        assert_eq!(spec.condition_label, Some(1));
    }

    #[test]
    fn conditional_unconditional_has_no_label() {
        let f = features();
        assert_eq!(parse_pattern_spec("+high", &f).unwrap().condition_label, None);
    }

    #[test]
    fn conditional_missing_closing_bracket() {
        let f = features();
        assert_eq!(
            parse_pattern_spec("<1: +high", &f).unwrap_err(),
            "Malformed conditional feature (missing closing '>'): '<1:+high'"
        );
    }

    #[test]
    fn conditional_non_integer_label() {
        let f = features();
        assert_eq!(
            parse_pattern_spec("<x: +high>", &f).unwrap_err(),
            "Conditional feature label must be an integer: '<x:+high>'"
        );
    }

    #[test]
    fn opposite_alpha_on_binary_ok() {
        let f = features();
        assert_eq!(parse_pattern_spec("voice: -α", &f).unwrap().value, Value::One(alpha(AlphaOp::Opposite, false)));
    }

    #[test]
    fn opposite_alpha_on_scalar_rejected() {
        let f = features();
        assert_eq!(
            parse_pattern_spec("tone: -α", &f).unwrap_err(),
            "Alpha-opposite ('-α') is not valid for scalar feature 'tone' (binary/unary only)"
        );
    }

    #[test]
    fn opposite_alpha_on_unary_accepted() {
        let f = features();
        let a = alpha_of(&parse_pattern_spec("manner: -α", &f).unwrap().value);
        assert_eq!(a.op, AlphaOp::Opposite);
        assert!(a.unary);
    }

    #[test]
    fn opposite_alpha_scalar_contour_limb_rejected() {
        let f = features();
        assert_eq!(
            parse_pattern_spec("tone: 1>-α", &f).unwrap_err(),
            "Alpha-opposite ('-α') is not valid for scalar feature 'tone' (binary/unary only)"
        );
    }

    #[test]
    fn same_and_other_alpha_on_scalar_ok() {
        let f = features();
        assert!(parse_pattern_spec("tone: α", &f).is_ok());
        assert!(parse_pattern_spec("tone: !α", &f).is_ok());
    }
}

mod parse_pattern_bundle {
    use super::*;

    #[test]
    fn simple_pattern() {
        let f = features();
        let bundle = parse_pattern_bundle("+nasal", &f).unwrap();
        assert_eq!(pattern_spec(&bundle, &f, "nasal").value, Value::int(1));
    }

    #[test]
    fn mixed_pattern() {
        let f = features();
        let bundle = parse_pattern_bundle("+consonantal", &f).unwrap();
        assert_eq!(names(&bundle, &f), ["consonantal"]);
    }

    #[test]
    fn comma_separates_features() {
        let f = features();
        let bundle = parse_pattern_bundle("+nasal, +voice", &f).unwrap();
        assert_eq!(names(&bundle, &f), ["nasal", "voice"]);
    }

    #[test]
    fn semicolon_does_not_separate_features() {
        let f = features();
        assert_eq!(
            parse_pattern_bundle("+nasal; +voice", &f).unwrap_err(),
            ["Could not identify value for 'nasal' from string '+;+voice'"]
        );
    }

    #[test]
    fn semicolon_contour_position_in_bundle() {
        let f = features();
        let bundle = parse_pattern_bundle("+nasal, tone: 1>2@2;3", &f).unwrap();
        assert_eq!(names(&bundle, &f), ["nasal", "tone"]);
        let tone = pattern_spec(&bundle, &f, "tone");
        assert_eq!(tone.value, contour(&[Limb::Int(1), Limb::Int(2)]));
        assert_eq!(tone.contour_position, ContourPosition::List(vec![2, 3]));
    }
}

mod parse_result_spec {
    use super::*;

    #[test]
    fn simple_present() {
        let f = features();
        let spec = parse_result_spec("+nasal", &f).unwrap();
        assert_eq!(f.name(spec.feature), "nasal");
        assert_eq!(spec.value, Value::int(1));
    }

    #[test]
    fn absent() {
        let f = features();
        let spec = parse_result_spec("-consonantal", &f).unwrap();
        assert_eq!(f.name(spec.feature), "consonantal");
        assert_eq!(spec.value, Value::int(0));
    }

    #[test]
    fn rejects_negation() {
        let f = features();
        assert_eq!(parse_result_spec("!nasal", &f).unwrap_err(), "Result spec does not support negation");
    }

    #[test]
    fn rejects_contour_position() {
        let f = features();
        assert_eq!(
            parse_result_spec("tone:1@initial", &f).unwrap_err(),
            "Result spec does not support contour position"
        );
    }

    #[test]
    fn conditional_feature() {
        let f = features();
        let spec = parse_result_spec("<1: +high>", &f).unwrap();
        assert_eq!(f.name(spec.feature), "high");
        assert_eq!(spec.value, Value::int(1));
        assert_eq!(spec.condition_label, Some(1));
    }

    #[test]
    fn conditional_rejects_negated_condition() {
        let f = features();
        assert_eq!(parse_result_spec("<1: !high>", &f).unwrap_err(), "Result spec does not support negation");
    }

    #[test]
    fn rejects_other_alpha() {
        let f = features();
        assert_eq!(
            parse_result_spec("!αconsonantal", &f).unwrap_err(),
            "Result spec does not support 'other' alpha notation"
        );
    }

    #[test]
    fn alpha_same() {
        let f = features();
        let spec = parse_result_spec("αconsonantal", &f).unwrap();
        assert_eq!(alpha_of(&spec.value).op, AlphaOp::Same);
    }

    #[test]
    fn alpha_opposite() {
        let f = features();
        let spec = parse_result_spec("-αconsonantal", &f).unwrap();
        assert_eq!(alpha_of(&spec.value).op, AlphaOp::Opposite);
    }

    #[test]
    fn opposite_alpha_on_scalar_rejected() {
        let f = features();
        assert_eq!(
            parse_result_spec("tone: -α", &f).unwrap_err(),
            "Alpha-opposite ('-α') is not valid for scalar feature 'tone' (binary/unary only)"
        );
    }

    #[test]
    fn scalar_numeric() {
        let f = features();
        let spec = parse_result_spec("stress:1", &f).unwrap();
        assert_eq!(f.name(spec.feature), "stress");
        assert_eq!(spec.value, Value::int(1));
    }

    #[test]
    fn contour_value() {
        let f = features();
        let spec = parse_result_spec("consonantal:1>0", &f).unwrap();
        assert_eq!(f.name(spec.feature), "consonantal");
        assert_eq!(spec.value, contour(&[Limb::Int(1), Limb::Int(0)]));
    }

    #[test]
    fn unspecified_with_plain_name_non_unary() {
        let f = features();
        assert_eq!(
            parse_result_spec("consonantal", &f).unwrap_err(),
            "Could not identify value for 'consonantal' from string 'consonantal'"
        );
    }
}
