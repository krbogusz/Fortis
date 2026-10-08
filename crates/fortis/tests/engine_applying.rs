//! Rewriting a matched span per the rule's result (`engine/applying.rs`), ported from
//! `tests/application/test_applying.py`.

mod common;

use std::path::Path;
use std::sync::Arc;

use fortis::engine::applying::apply_match;
use fortis::engine::matching::{FeatSet, Match, MatchCtx, target_recalls_context_binding};
use fortis::loaders::inventories::load_feature_inventory;
use fortis::models::*;
use fortis::parsing::notation::parse_definition;

/// `MINIMAL_FEATURES_TOML` from `tests/conftest.py`.
const MINIMAL_FEATURES_TOML: &str = r#"
[consonantal]
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

/// The `features` fixture.
fn features() -> FeatureInventory {
    let src = common::memory(&[("features.toml", MINIMAL_FEATURES_TOML)]);
    load_feature_inventory(&src, Path::new("features.toml")).expect("the minimal features load")
}

/// Python's `_fb`: a realized bundle from `feature=value` pairs. `a>b` is a contour, kept
/// unfolded like Python's tuple.
fn fb(f: &FeatureInventory, spec: &str) -> FeatureBundle {
    let mut bundle = FeatureBundle::new();
    for pair in spec.split_whitespace() {
        let (name, value) = pair.split_once('=').unwrap();
        let limbs: Vec<Limb> = value.split('>').map(|n| Limb::Int(n.parse().unwrap())).collect();
        let value = if limbs.len() == 1 { Value::One(limbs[0]) } else { Value::Contour(limbs.into()) };
        bundle.set(f.id(name).unwrap(), value);
    }
    bundle
}

/// The `letters` fixture: a small letter inventory for replacement results.
fn letters(f: &FeatureInventory) -> LetterInventory {
    let mut inventory = LetterInventory::default();
    for (symbol, spec) in [
        ("a", "syllabic=1 high=0"),
        ("u", "syllabic=1 high=1 rounded=1"),
        ("e", "syllabic=1 high=0 front=1"),
        ("x", "consonantal=1 voice=0"),
    ] {
        inventory.insert(Letter { symbol: symbol.into(), bundle: Arc::new(fb(f, spec)) });
    }
    inventory
}

fn arcs(segs: &[FeatureBundle]) -> Vec<Arc<FeatureBundle>> {
    segs.iter().cloned().map(Arc::new).collect()
}

fn parse(f: &FeatureInventory, rule: &str) -> StructuralDescription {
    parse_definition(rule, f).unwrap()
}

/// Python's `find_matches(sd, segs, letters)`: no syllable boundaries, no syllable view.
fn find(
    f: &FeatureInventory,
    letters: &LetterInventory,
    sd: &StructuralDescription,
    segs: &[Arc<FeatureBundle>],
) -> Vec<Match> {
    let boundaries = Boundaries::new();
    let none = FeatSet::default();
    let cx = MatchCtx { segs, letters, boundaries: &boundaries, view: None, features: f, syllable_features: &none };
    cx.find_matches(sd, target_recalls_context_binding(sd))
}

/// Python's `_apply`: parse *rule*, match it against *segs*, and apply it at the first locus.
/// Returns the replacement bundles without their source positions.
fn apply(f: &FeatureInventory, rule: &str, segs: &[FeatureBundle]) -> Vec<FeatureBundle> {
    let letters = letters(f);
    let sd = parse(f, rule);
    let segs = arcs(segs);
    let matches = find(f, &letters, &sd, &segs);
    assert!(!matches.is_empty(), "rule {rule:?} found no locus");
    apply_match(&sd, &matches[0], &segs, &letters, f).into_iter().map(|(bundle, _)| bundle).collect()
}

mod merge_path {
    use super::*;

    #[test]
    fn bundle_merge_preserves_other_features() {
        let f = features();
        let out = apply(&f, "[+nasal] -> [-voice]", &[fb(&f, "nasal=1 voice=1")]);
        assert_eq!(out, [fb(&f, "nasal=1 voice=0")]);
    }

    #[test]
    fn unlink_delinks_node_and_descendants() {
        // `manner` dominates continuant, sonorant, nasal and lateral.
        let f = features();
        let out = apply(&f, "[+nasal] -> [manner: none]", &[fb(&f, "nasal=1 manner=1 voice=1 continuant=0")]);
        assert_eq!(out, [fb(&f, "voice=1")]);
    }

    #[test]
    fn alpha_recall_in_result() {
        let f = features();
        let out = apply(&f, "[+high] -> [αfront] / [αfront] _", &[fb(&f, "front=1"), fb(&f, "high=1")]);
        assert_eq!(out, [fb(&f, "front=1 high=1")]);
    }

    #[test]
    fn opposite_alpha_in_result_dissimilates() {
        let f = features();
        let out = apply(&f, "[+high] -> [-αvoice] / [αvoice] _", &[fb(&f, "voice=1"), fb(&f, "high=1")]);
        assert_eq!(out, [fb(&f, "voice=0 high=1")]);
    }

    #[test]
    fn alpha_recall_into_a_contour_limb() {
        let f = features();
        let out = apply(&f, "[+syll] -> [length: α>3] / [αlength] _", &[fb(&f, "length=2"), fb(&f, "syllabic=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 length=2>3")]);
    }

    #[test]
    fn mixed_null_and_bundle() {
        let f = features();
        let out = apply(&f, "[+cons][+syll] -> ∅[-syll]", &[fb(&f, "consonantal=1"), fb(&f, "syllabic=1")]);
        assert_eq!(out, [fb(&f, "syllabic=0")]);
    }

    #[test]
    fn letter_in_merge_path_replaces_its_pair() {
        let f = features();
        let out = apply(&f, "[+cons][+syll] -> x[-syll]", &[fb(&f, "consonantal=1 voice=1"), fb(&f, "syllabic=1")]);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=0"), fb(&f, "syllabic=0")]);
    }

    #[test]
    fn negated_class_target_merges() {
        let f = features();
        let out = apply(&f, "![+nasal] -> [+voice]", &[fb(&f, "consonantal=1")]);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=1")]);
    }

    #[test]
    fn bound_single_segment_target_merges() {
        let f = features();
        let out = apply(&f, "1=[+cons] -> [+voice]", &[fb(&f, "consonantal=1")]);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=1")]);
    }

    #[test]
    fn mid_span_null_insertion() {
        let f = features();
        let segs = [fb(&f, "consonantal=1"), fb(&f, "syllabic=1")];
        let out = apply(&f, "[+cons] ∅ [+syll] -> [+voice][+nasal][-syll]", &segs);
        // The inserted [+nasal] implies its parent node manner (geometry completion).
        assert_eq!(out, [fb(&f, "consonantal=1 voice=1"), fb(&f, "nasal=1 manner=1"), fb(&f, "syllabic=0")]);
    }

    #[test]
    fn three_pair_merge_keeps_correspondence() {
        let f = features();
        let segs = [fb(&f, "nasal=1"), fb(&f, "lateral=1"), fb(&f, "continuant=1")];
        let out = apply(&f, "[+nasal][+lateral][+cont] -> [-voice][+high][-high]", &segs);
        assert_eq!(out, [fb(&f, "nasal=1 voice=0"), fb(&f, "lateral=1 high=1"), fb(&f, "continuant=1 high=0")]);
    }
}

mod replacement_path {
    use super::*;

    #[test]
    fn letter_replaces_wholesale() {
        let f = features();
        let out = apply(&f, "x -> a", &[fb(&f, "consonantal=1 voice=0")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=0")]);
    }

    #[test]
    fn collapse_two_into_one() {
        let f = features();
        let out = apply(&f, "a u -> e", &[fb(&f, "syllabic=1 high=0"), fb(&f, "syllabic=1 high=1 rounded=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=0 front=1")]);
    }

    #[test]
    fn expand_one_into_two() {
        let f = features();
        let out = apply(&f, "e -> a u", &[fb(&f, "syllabic=1 high=0 front=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=0"), fb(&f, "syllabic=1 high=1 rounded=1")]);
    }

    #[test]
    fn deletion() {
        let f = features();
        assert!(apply(&f, "[+cons] -> ∅", &[fb(&f, "consonantal=1")]).is_empty());
    }

    #[test]
    fn insertion() {
        let f = features();
        let out = apply(&f, "∅ -> [+voice] / [+nasal] _", &[fb(&f, "nasal=1")]);
        assert_eq!(out, [fb(&f, "voice=1")]);
    }

    #[test]
    fn recall_in_result() {
        let f = features();
        let out = apply(&f, "1=[+cons] -> @1", &[fb(&f, "consonantal=1 voice=1")]);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=1")]);
    }

    #[test]
    fn case_b_target_recall_rewrites_the_matched_segment() {
        // @1 recalls a right-context binding; the first nasal is rewritten, the second stays.
        let f = features();
        let n = fb(&f, "nasal=1 labial=1");
        let out = apply(&f, "@1 -> [-voice] / _ 1=[+nasal]", &[n.clone(), n]);
        assert_eq!(out, [fb(&f, "nasal=1 labial=1 voice=0")]);
    }
}

mod complex_merge_targets {
    use super::*;

    #[test]
    fn fixed_quantified_merge() {
        let f = features();
        let segs = [fb(&f, "consonantal=1 voice=1"), fb(&f, "consonantal=1 voice=1")];
        let out = apply(&f, "[+cons]{2} -> [-voice]{2}", &segs);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=0"), fb(&f, "consonantal=1 voice=0")]);
    }

    #[test]
    fn grouped_merge() {
        let f = features();
        let segs = [fb(&f, "consonantal=1 voice=1"), fb(&f, "syllabic=1")];
        let out = apply(&f, "([+cons][+syll]) -> ([-voice][+nasal])", &segs);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=0"), fb(&f, "syllabic=1 nasal=1 manner=1")]);
    }

    #[test]
    fn variable_quantifier_merge_takes_count_from_span() {
        let f = features();
        let segs = vec![fb(&f, "consonantal=1 syllabic=0 voice=1"); 3];
        let out = apply(&f, "[-syll]* -> [-voice]*", &segs);
        assert_eq!(out, vec![fb(&f, "consonantal=1 syllabic=0 voice=0"); 3]);
    }

    #[test]
    fn bounded_variable_quantifier_merge() {
        let f = features();
        let segs = [fb(&f, "consonantal=1 voice=1"), fb(&f, "consonantal=1 voice=1")];
        let out = apply(&f, "[+cons]{1,2} -> [-voice]{1,2}", &segs);
        assert_eq!(out, [fb(&f, "consonantal=1 voice=0"), fb(&f, "consonantal=1 voice=0")]);
    }

    // Python raises NotImplementedError; Rust panics.
    #[test]
    #[should_panic(expected = "more than one variable-width element on the merge path")]
    fn two_variable_quantifiers_still_refused() {
        let f = features();
        let letters = letters(&f);
        let sd = parse(&f, "[-syll]* [-syll]* -> [-voice]* [-voice]*");
        let segs = arcs(&[fb(&f, "consonantal=1 voice=1"), fb(&f, "consonantal=1 voice=1")]);
        let m = find(&f, &letters, &sd, &segs).remove(0);
        apply_match(&sd, &m, &segs, &letters, &f);
    }

    #[test]
    fn variable_quantifier_replacement_mirrors_the_target() {
        let f = features();
        let a = fb(&f, "syllabic=1 high=0");
        let segs = vec![fb(&f, "consonantal=1 syllabic=0"); 3];
        assert_eq!(apply(&f, "[-syll]* -> a*", &segs), [a.clone(), a.clone(), a.clone()]);
        assert_eq!(apply(&f, "[-syll]* -> a*", &segs[..1]), [a]);
    }

    // Python raises NotImplementedError; Rust panics.
    #[test]
    #[should_panic(expected = "result element Quantified")]
    fn variable_result_without_a_variable_target_is_refused() {
        let f = features();
        let letters = letters(&f);
        let sd = parse(&f, "[+cons] -> a*");
        let segs = arcs(&[fb(&f, "consonantal=1")]);
        let m = find(&f, &letters, &sd, &segs).remove(0);
        apply_match(&sd, &m, &segs, &letters, &f);
    }

    #[test]
    fn multisegment_recall_replays_the_whole_span() {
        let f = features();
        let (c, v) = (fb(&f, "consonantal=1 voice=1"), fb(&f, "syllabic=1"));
        let out = apply(&f, "1=([+cons][+syll]) -> @1 @1", &[c.clone(), v.clone()]);
        assert_eq!(out, [c.clone(), v.clone(), c, v]);
    }
}

mod conditional_features {
    use super::*;

    #[test]
    fn condition_gates_result_without_filtering() {
        let f = features();
        let rule = "[+syll, <1: +high>] -> [<1: +voice>]";
        assert_eq!(apply(&f, rule, &[fb(&f, "syllabic=1 high=1")]), [fb(&f, "syllabic=1 high=1 voice=1")]);
        // -high still matches (a condition does not filter), but voice is not applied.
        assert_eq!(apply(&f, rule, &[fb(&f, "syllabic=1 high=0")]), [fb(&f, "syllabic=1 high=0")]);
    }

    #[test]
    fn negated_condition() {
        let f = features();
        let rule = "[+syll, <1: !+high>] -> [<1: +voice>]";
        assert_eq!(apply(&f, rule, &[fb(&f, "syllabic=1 high=0")]), [fb(&f, "syllabic=1 high=0 voice=1")]);
        assert_eq!(apply(&f, rule, &[fb(&f, "syllabic=1 high=1")]), [fb(&f, "syllabic=1 high=1")]);
    }

    #[test]
    fn context_shared_label_requires_both() {
        let f = features();
        let rule = "[+syll, <1: +high>] -> [<1: +voice>] / [<1: +nasal>] _";
        let out = apply(&f, rule, &[fb(&f, "nasal=1"), fb(&f, "syllabic=1 high=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=1 voice=1")]);
        let out = apply(&f, rule, &[fb(&f, "nasal=0"), fb(&f, "syllabic=1 high=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=1")]);
    }

    #[test]
    fn alpha_condition_is_recall_only() {
        let f = features();
        let rule = "[+syll, <1: αhigh>] -> [<1: +voice>] / [αhigh] _";
        let out = apply(&f, rule, &[fb(&f, "high=1"), fb(&f, "syllabic=1 high=1")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=1 voice=1")]);
        let out = apply(&f, rule, &[fb(&f, "high=1"), fb(&f, "syllabic=1 high=0")]);
        assert_eq!(out, [fb(&f, "syllabic=1 high=0")]);
    }

    #[test]
    fn conditions_isolated_per_locus() {
        let f = features();
        let sd = parse(&f, "[+syll, <1: +high>] -> [<1: +voice>]");
        let segs = arcs(&[fb(&f, "syllabic=1 high=0"), fb(&f, "syllabic=1 high=1")]);
        let matches = find(&f, &letters(&f), &sd, &segs);
        let held: Vec<Option<bool>> = matches.iter().map(|m| map_get(&m.bindings.conditions, 1).copied()).collect();
        assert_eq!(held, [Some(false), Some(true)]);
    }

    // A hand-built match with no conditions recorded; real rules cannot reach this guard.
    // Python raises NotImplementedError; Rust panics.
    #[test]
    #[should_panic(expected = "has no condition recorded from matching")]
    fn missing_condition_label_raises() {
        let f = features();
        let sd = parse(&f, "[+syll, <1: +high>] -> [<1: +voice>]");
        let bogus = Match { start: 0, end: 1, bindings: Bindings::default(), target_choices: vec![] };
        apply_match(&sd, &bogus, &arcs(&[fb(&f, "syllabic=1 high=1")]), &letters(&f), &f);
    }
}

mod disjunction {
    use super::*;

    #[test]
    fn branch_selection_is_positional() {
        let f = features();
        let rule = "([+high] | [+front]) -> ([+nasal] | [+voice])";
        assert_eq!(apply(&f, rule, &[fb(&f, "high=1")]), [fb(&f, "high=1 nasal=1 manner=1")]);
        assert_eq!(apply(&f, rule, &[fb(&f, "front=1")]), [fb(&f, "front=1 voice=1")]);
    }

    #[test]
    fn collapse_to_single_result() {
        let f = features();
        let rule = "([+high] | [+front]) -> [+nasal]";
        assert_eq!(apply(&f, rule, &[fb(&f, "high=1")]), [fb(&f, "high=1 nasal=1 manner=1")]);
        assert_eq!(apply(&f, rule, &[fb(&f, "front=1")]), [fb(&f, "front=1 nasal=1 manner=1")]);
    }

    #[test]
    fn scalar_chain_shift_flips_the_value() {
        let f = features();
        let rule = "([length: 3] | [length: 2]) -> ([length: 2] | [length: 1])";
        assert_eq!(apply(&f, rule, &[fb(&f, "length=3 syllabic=1")]), [fb(&f, "length=2 syllabic=1")]);
        assert_eq!(apply(&f, rule, &[fb(&f, "length=2 syllabic=1")]), [fb(&f, "length=1 syllabic=1")]);
    }
}
