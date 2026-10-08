//! Port of `tests/parsing/test_rules.py`: rule-definition parsing (`parse_definition`), the
//! split of a rule string into target, result, context and exception.

mod common;

use std::path::Path;

use fortis::loaders::inventories::load_feature_inventory;
use fortis::models::*;
use fortis::parsing::notation::parse_definition;

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

/// The symbols of a sequence made only of letter references.
fn letters(elements: &[Element]) -> Vec<&str> {
    elements
        .iter()
        .map(|e| match e {
            Element::LetterRef(symbol) => symbol.as_str(),
            other => panic!("expected a LetterRef, found {other:?}"),
        })
        .collect()
}

mod modified_letter {
    use super::*;

    #[test]
    fn result_side() {
        let f = features();
        let sd = parse_definition("ˈe -> a^[stress: none]", &f).unwrap();
        let [Element::ModifiedLetter(symbol, delta)] = &sd.result[..] else {
            panic!("expected one ModifiedLetter, found {:?}", sd.result);
        };
        assert_eq!(symbol, "a");
        assert_eq!(delta.get(id(&f, "stress")), Some(&Value::NONE));
    }

    #[test]
    fn target_side() {
        let f = features();
        let sd = parse_definition("e^[nasal: 1] -> i", &f).unwrap();
        let [Element::ModifiedLetter(symbol, delta)] = &sd.target[..] else {
            panic!("expected one ModifiedLetter, found {:?}", sd.target);
        };
        assert_eq!(symbol, "e");
        assert!(delta.contains(id(&f, "nasal")));
    }

    #[test]
    fn multi_letter_run_keeps_whole_symbol_for_resolve() {
        let f = features();
        let sd = parse_definition("au^[nasal: 1] -> e", &f).unwrap();
        let [Element::ModifiedLetter(symbol, _)] = &sd.target[..] else {
            panic!("expected one ModifiedLetter, found {:?}", sd.target);
        };
        assert_eq!(symbol, "au");
    }

    #[test]
    fn pattern_delta_is_rejected() {
        let f = features();
        assert_eq!(
            parse_definition("e^[!nasal] -> a", &f).unwrap_err(),
            ["Realized feature specifications don't support negation at position 2"]
        );
    }

    #[test]
    fn caret_requires_a_following_bundle() {
        let f = features();
        assert_eq!(parse_definition("e^ -> a", &f).unwrap_err(), ["expected BUNDLE, found ARROW at position 3"]);
    }
}

mod parse_definition {
    use super::*;

    #[test]
    fn full_rule() {
        let sd = parse_definition("a -> b / c _ d // e _ f", &features()).unwrap();
        assert_eq!(letters(&sd.target), ["a"]);
        assert_eq!(letters(&sd.result), ["b"]);
        assert_eq!(letters(&sd.left_context), ["c"]);
        assert_eq!(letters(&sd.right_context), ["d"]);
        assert_eq!(letters(&sd.left_exception), ["e"]);
        assert_eq!(letters(&sd.right_exception), ["f"]);
    }

    #[test]
    fn no_exception() {
        let sd = parse_definition("a -> b / c _ d", &features()).unwrap();
        assert_eq!(letters(&sd.target), ["a"]);
        assert_eq!(letters(&sd.result), ["b"]);
        assert_eq!(letters(&sd.left_context), ["c"]);
        assert_eq!(letters(&sd.right_context), ["d"]);
        assert!(sd.left_exception.is_empty());
        assert!(sd.right_exception.is_empty());
    }

    #[test]
    fn no_context() {
        let sd = parse_definition("a -> b", &features()).unwrap();
        assert_eq!(letters(&sd.target), ["a"]);
        assert_eq!(letters(&sd.result), ["b"]);
        assert!(sd.left_context.is_empty());
        assert!(sd.right_context.is_empty());
        assert!(sd.left_exception.is_empty());
        assert!(sd.right_exception.is_empty());
    }

    #[test]
    fn unicode_arrow() {
        let sd = parse_definition("a → b / c _ d", &features()).unwrap();
        assert_eq!(letters(&sd.target), ["a"]);
        assert_eq!(letters(&sd.result), ["b"]);
        assert_eq!(letters(&sd.left_context), ["c"]);
    }

    #[test]
    fn extra_whitespace_ignored() {
        let sd = parse_definition(" a  ->  b  /  c  _  d ", &features()).unwrap();
        assert_eq!(letters(&sd.target), ["a"]);
        assert_eq!(letters(&sd.result), ["b"]);
        assert_eq!(letters(&sd.left_context), ["c"]);
        assert_eq!(letters(&sd.right_context), ["d"]);
    }

    #[test]
    fn conditional_features_round_trip() {
        let f = features();
        let sd = parse_definition("[<1: +high>] → [<1: +voice>] / a _", &f).unwrap();
        let Element::BundleElem(target) = &sd.target[0] else {
            panic!("expected a BundleElem, found {:?}", sd.target[0]);
        };
        let Element::ResultElem(result) = &sd.result[0] else {
            panic!("expected a ResultElem, found {:?}", sd.result[0]);
        };
        let high = target.iter().find(|s| s.feature == id(&f, "high")).unwrap();
        let voice = result.iter().find(|s| s.feature == id(&f, "voice")).unwrap();
        assert_eq!(high.condition_label, Some(1));
        assert_eq!(voice.condition_label, Some(1));
    }
}
