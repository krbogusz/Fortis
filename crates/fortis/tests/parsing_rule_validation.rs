//! Port of `tests/parsing/test_rule_validation.py`: structural rule validation (the §2.x
//! well-formedness checks).

mod common;

use std::path::Path;

use fortis::loaders::inventories::load_feature_inventory;
use fortis::models::*;
use fortis::parsing::notation::parse_definition;
use fortis::parsing::validation::validate_structural_description;

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

/// Parse a definition and run structural validation on the result. Like Python's `check`, it
/// passes no feature inventory to the validation.
fn check(definition: &str, features: &FeatureInventory) -> Result<(), Vec<String>> {
    validate_structural_description(&parse_definition(definition, features).unwrap(), None)
}

mod valid {
    use super::*;

    #[test]
    fn simple_rule() {
        assert_eq!(check("a -> b / c _ d", &features()), Ok(()));
    }

    #[test]
    fn alpha_bound_in_target() {
        assert_eq!(check("[αhigh] -> [αnasal] / c _", &features()), Ok(()));
    }

    #[test]
    fn alpha_bound_in_context() {
        assert_eq!(check("a -> [αnasal] / [αhigh] _", &features()), Ok(()));
    }

    #[test]
    fn reference_bind_and_recall() {
        assert_eq!(check("1=a -> b / @1 _", &features()), Ok(()));
    }

    #[test]
    fn conditional_label_once_each() {
        assert_eq!(check("[<1:+high>] -> [<1:+nasal>] / a _", &features()), Ok(()));
    }

    #[test]
    fn conditional_label_also_in_context() {
        assert_eq!(check("[<1:+high>] -> [<1:+nasal>] / [<1:+voice>] _", &features()), Ok(()));
    }

    #[test]
    fn conditional_label_context_only() {
        assert_eq!(check("[+syll] -> [<1:+nasal>] / [<1:+voice>] _", &features()), Ok(()));
    }

    #[test]
    fn conditional_label_multifeature_result() {
        assert_eq!(check("[<1:+high>] -> [<1:+nasal>, <1:+voice>] / a _", &features()), Ok(()));
    }

    #[test]
    fn collapse_to_letter() {
        assert_eq!(check("a a -> b / c _", &features()), Ok(()));
    }

    #[test]
    fn expand_to_letters() {
        assert_eq!(check("a -> b c / d _", &features()), Ok(()));
    }
}

mod invalid {
    use super::*;

    #[test]
    fn ambiguous_collapse_to_bundle() {
        assert_eq!(
            check("[+cons][-cons] -> [+nasal] / a _", &features()).unwrap_err(),
            [
                "Ambiguous rule: target has 2 element(s) but result has 1, and a result feature-bundle has no unambiguous target to merge with — a count mismatch is only allowed with letter-shorthand results"
            ]
        );
    }

    #[test]
    fn ambiguous_expand_to_bundles() {
        assert_eq!(
            check("[+syllabic] -> [+nasal][+high] / a _", &features()).unwrap_err(),
            [
                "Ambiguous rule: target has 1 element(s) but result has 2, and a result feature-bundle has no unambiguous target to merge with — a count mismatch is only allowed with letter-shorthand results"
            ]
        );
    }
}

mod batch2_valid {
    use super::*;

    #[test]
    fn null_target_with_context() {
        assert_eq!(check("∅ -> x / a _", &features()), Ok(()));
    }

    #[test]
    fn boundary_in_context() {
        assert_eq!(check("a -> b / # _", &features()), Ok(()));
    }

    #[test]
    fn matching_quantifiers() {
        assert_eq!(check("a{2} -> b{2} / c _", &features()), Ok(()));
    }

    #[test]
    fn quantified_target_collapses_to_letter() {
        assert_eq!(check("a{2} -> b / c _", &features()), Ok(()));
    }

    #[test]
    fn exception_without_context() {
        assert_eq!(check("a -> b // e _ f", &features()), Ok(()));
    }

    #[test]
    fn paired_disjunction() {
        assert_eq!(check("(a|b) -> (c|d) / f _", &features()), Ok(()));
    }

    #[test]
    fn disjunction_collapse_to_single_result() {
        assert_eq!(check("(a|b|c) -> d / f _", &features()), Ok(()));
    }

    #[test]
    fn negation_in_target() {
        assert_eq!(check("!a -> b / c _", &features()), Ok(()));
    }
}

mod batch2_invalid {
    use super::*;

    #[test]
    fn null_in_context() {
        assert_eq!(
            check("a -> b / ∅ _", &features()).unwrap_err(),
            ["∅ (null) is not valid in left context position"]
        );
    }

    #[test]
    fn boundary_sole_target() {
        assert_eq!(
            check("# -> x", &features()).unwrap_err(),
            ["A boundary may not be the only element in target position"]
        );
    }

    #[test]
    fn boundary_sole_result() {
        assert_eq!(
            check("x -> #", &features()).unwrap_err(),
            ["A boundary may not be the only element in result position"]
        );
    }

    #[test]
    fn null_entire_target_without_context() {
        assert_eq!(check("∅ -> x", &features()).unwrap_err(), ["∅ as the entire target requires a context"]);
    }

    #[test]
    fn merge_bundle_quantifier_mismatch() {
        assert_eq!(
            check("[+consonantal]{2} -> [+nasal] / c _", &features()).unwrap_err(),
            ["A merge-bundle result element must carry the same quantifier as its corresponding target element"]
        );
    }

    #[test]
    fn disjunction_unpaired() {
        assert_eq!(
            check("a -> (b|c) / d _", &features()).unwrap_err(),
            ["A disjunction in result position needs a corresponding target disjunction with the same number of branches"]
        );
    }

    #[test]
    fn disjunction_branch_count_mismatch() {
        assert_eq!(
            check("(a|b) -> (c|d|e) / f _", &features()).unwrap_err(),
            ["A disjunction in result position needs a corresponding target disjunction with the same number of branches"]
        );
    }

    #[test]
    fn more_than_one_disjunction_per_side() {
        assert_eq!(
            check("(a|b) (e|f) -> (c|d) (g|h)", &features()).unwrap_err(),
            [
                "at most one top-level disjunction per side (in the target)",
                "at most one top-level disjunction per side (in the result)",
            ]
        );
    }

    #[test]
    fn nested_disjunction_with_a_top_level_one_rejected() {
        assert_eq!(
            check("(a | (b|c)) -> (d|e)", &features()).unwrap_err(),
            ["a nested disjunction cannot coexist with a top-level disjunction (in the target)"]
        );
    }

    #[test]
    fn nested_only_disjunction_is_allowed() {
        assert_eq!(check("(a|b)? c -> ∅ / d _", &features()), Ok(()));
    }

    #[test]
    fn negation_in_result() {
        assert_eq!(
            check("a -> !b / c _", &features()).unwrap_err(),
            ["Negation '!' is not valid in result position"]
        );
    }

    #[test]
    fn negation_on_null() {
        assert_eq!(
            check("!∅ -> b / c _", &features()).unwrap_err(),
            ["Negation '!' may not be applied to ∅ or []"]
        );
    }

    #[test]
    fn negation_on_wildcard() {
        assert_eq!(
            check("![] -> b / c _", &features()).unwrap_err(),
            ["Negation '!' may not be applied to ∅ or []"]
        );
    }

    #[test]
    fn dangling_recall() {
        assert_eq!(check("@1 -> b / a _", &features()).unwrap_err(), ["Recall '@1' has no matching binding '1='"]);
    }

    #[test]
    fn binding_never_recalled() {
        assert_eq!(check("1=a -> b / c _", &features()).unwrap_err(), ["Binding '1=' is never recalled by '@1'"]);
    }

    #[test]
    fn binding_in_result() {
        assert_eq!(
            check("@1 -> 1=b / c _", &features()).unwrap_err(),
            ["Binding '1=' is not allowed in result position"]
        );
    }

    #[test]
    fn alpha_unbound_in_result() {
        assert_eq!(
            check("a -> [αnasal] / c _", &features()).unwrap_err(),
            ["Alpha variable 'α' is used but never bound in target or context"]
        );
    }

    #[test]
    fn conditional_label_condition_without_result() {
        assert_eq!(
            check("[<1:+high>] -> b / a _", &features()).unwrap_err(),
            ["Conditional label '1' is a condition but applies no result feature"]
        );
    }

    #[test]
    fn conditional_label_result_without_condition() {
        assert_eq!(
            check("a -> [<1:+nasal>] / b _", &features()).unwrap_err(),
            ["Conditional label '1' is applied in the result but has no condition in the target or context"]
        );
    }
}

mod tier_references {
    use super::*;

    #[test]
    fn spread_and_dock_validate() {
        let project = common::default_project();
        let spread = "[+syllabic, tone: none] -> [+syllabic, tone: ~1] / [+syllabic, tone: ~1=high] [-syllabic]* _";
        let dock = "⟨tone: ~1=high⟩ [+syllabic, tone: none] -> [+syllabic, tone: ~1]";
        assert_eq!(check(spread, &project.features), Ok(()));
        assert_eq!(check(dock, &project.features), Ok(()));
    }

    #[test]
    fn unbound_tier_recall() {
        let project = common::default_project();
        assert_eq!(
            check("[+syllabic, tone: none] -> [+syllabic, tone: ~2]", &project.features).unwrap_err(),
            ["Tier recall '~2' has no matching binding '~2='"]
        );
    }

    #[test]
    fn tier_binding_never_recalled() {
        let project = common::default_project();
        assert_eq!(
            check("[+syllabic, tone: ~1=high] -> [+syllabic]", &project.features).unwrap_err(),
            ["Tier binding '~1=' is never recalled by '~1'"]
        );
    }

    #[test]
    fn floating_in_result_rejected() {
        let project = common::default_project();
        assert_eq!(
            check("[+syllabic] -> ⟨tone: high⟩", &project.features).unwrap_err(),
            ["A floating autosegment '⟨...⟩' is not valid in result position"]
        );
    }
}
