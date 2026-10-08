//! Single-segment pattern matching and the sequence matcher (`engine/matching.rs`), ported from
//! `tests/application/test_matching.py`.

mod common;

use std::path::Path;
use std::sync::Arc;

use fortis::engine::matching::{
    FeatSet, MatchCtx, PatternCtx, SyllableView, cannot_match, matches_plain, pattern_matches, required_demands,
    target_recalls_context_binding, word_supply,
};
use fortis::engine::syllabifying::nuclei_by_position;
use fortis::loaders::inventories::load_feature_inventory;
use fortis::models::*;
use fortis::parsing::bundles::parse_pattern_bundle;
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

/// The TestAlpha cases name a feature `back` that the fixture lacks. Python keys bundles by
/// name, so it needs no declaration there; Rust needs a feature id.
const BACK_TOML: &str = r#"
[back]
tier = "segment"
kind = "binary"
short = "bk"
"#;

fn load_features(text: &str) -> FeatureInventory {
    let src = common::memory(&[("features.toml", text)]);
    load_feature_inventory(&src, Path::new("features.toml")).expect("the minimal features load")
}

/// The `features` fixture.
fn features() -> FeatureInventory {
    load_features(MINIMAL_FEATURES_TOML)
}

/// Python's `_fb`: a realized bundle from `feature=value` pairs. `a>b` is a contour, kept
/// unfolded like Python's tuple (so `tone=2>2` stays two limbs).
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

/// Python's `PatternSpec(feature, value)` with its defaults (`@any`, not negated, no label).
fn spec(f: &FeatureInventory, name: &str, value: Value) -> PatternSpec {
    PatternSpec {
        feature: f.id(name).unwrap(),
        value,
        negated: false,
        contour_position: ContourPosition::Edge(ContourEdge::Any),
        condition_label: None,
    }
}

fn alpha(op: AlphaOp) -> Limb {
    Limb::Alpha(AlphaRef { var: 'α', op, unary: false })
}

fn arcs(segs: &[FeatureBundle]) -> Vec<Arc<FeatureBundle>> {
    segs.iter().cloned().map(Arc::new).collect()
}

fn parse(f: &FeatureInventory, rule: &str) -> StructuralDescription {
    parse_definition(rule, f).unwrap()
}

/// Python's `_spans(find_matches(sd, segs, letters, boundaries, syllables))`. *view* pairs the
/// syllable view with its syllable-tier features.
fn spans_in(
    f: &FeatureInventory,
    sd: &StructuralDescription,
    segs: &[FeatureBundle],
    letters: &LetterInventory,
    boundaries: &[usize],
    view: Option<(&SyllableView, &FeatSet)>,
) -> Vec<(usize, usize)> {
    let segs = arcs(segs);
    let boundaries: Boundaries = boundaries.iter().copied().collect();
    let none = FeatSet::default();
    let cx = MatchCtx {
        segs: &segs,
        letters,
        boundaries: &boundaries,
        view: view.map(|(v, _)| v),
        features: f,
        syllable_features: view.map_or(&none, |(_, s)| s),
    };
    cx.find_matches(sd, target_recalls_context_binding(sd)).iter().map(|m| (m.start, m.end)).collect()
}

fn spans(f: &FeatureInventory, sd: &StructuralDescription, segs: &[FeatureBundle]) -> Vec<(usize, usize)> {
    spans_in(f, sd, segs, &LetterInventory::default(), &[], None)
}

/// Python's `cannot_match(sd, segs, LetterInventory())`.
fn cannot(sd: &StructuralDescription, segs: &[FeatureBundle]) -> bool {
    let demands = required_demands(sd, &LetterInventory::default(), &FeatSet::default());
    cannot_match(&demands, &word_supply(&arcs(segs)))
}

mod pattern_matches {
    use super::*;

    #[test]
    fn subsumption_match() {
        let f = features();
        assert!(matches_plain(&[spec(&f, "voice", Value::int(1))], &fb(&f, "voice=1 nasal=0")));
    }

    #[test]
    fn value_mismatch_fails() {
        let f = features();
        assert!(!matches_plain(&[spec(&f, "voice", Value::int(1))], &fb(&f, "voice=0")));
    }

    #[test]
    fn absent_feature_fails_positive() {
        let f = features();
        assert!(!matches_plain(&[spec(&f, "voice", Value::int(1))], &fb(&f, "nasal=0")));
    }

    #[test]
    fn absent_feature_passes_negated() {
        let f = features();
        let pat = [PatternSpec { negated: true, ..spec(&f, "voice", Value::int(1)) }];
        assert!(matches_plain(&pat, &fb(&f, "nasal=0")));
    }

    #[test]
    fn negated_blocks_matching_value() {
        let f = features();
        let pat = [PatternSpec { negated: true, ..spec(&f, "voice", Value::int(1)) }];
        assert!(!matches_plain(&pat, &fb(&f, "voice=1")));
    }

    #[test]
    fn none_matches_absent_feature() {
        let f = features();
        assert!(matches_plain(&[spec(&f, "nasal", Value::NONE)], &fb(&f, "voice=1")));
    }

    #[test]
    fn none_fails_specified_feature() {
        let f = features();
        assert!(!matches_plain(&[spec(&f, "nasal", Value::NONE)], &fb(&f, "nasal=0")));
    }

    #[test]
    fn negated_none_requires_presence() {
        let f = features();
        let pat = [PatternSpec { negated: true, ..spec(&f, "nasal", Value::NONE) }];
        assert!(!matches_plain(&pat, &fb(&f, "voice=1")));
        assert!(matches_plain(&pat, &fb(&f, "nasal=0")));
    }

    #[test]
    fn contour_matches_equal_length() {
        let f = features();
        let tone = Value::Contour(vec![Limb::Int(1), Limb::Int(2)].into());
        let pat = [PatternSpec { contour_position: ContourPosition::Edge(ContourEdge::All), ..spec(&f, "tone", tone) }];
        assert!(matches_plain(&pat, &fb(&f, "tone=1>2")));
    }

    #[test]
    fn contour_length_mismatch_fails() {
        let f = features();
        let tone = Value::Contour(vec![Limb::Int(1), Limb::Int(2)].into());
        let pat = [PatternSpec { contour_position: ContourPosition::Edge(ContourEdge::All), ..spec(&f, "tone", tone) }];
        assert!(!matches_plain(&pat, &fb(&f, "tone=1")));
    }
}

mod alpha {
    use super::*;

    fn features() -> FeatureInventory {
        load_features(&format!("{MINIMAL_FEATURES_TOML}{BACK_TOML}"))
    }

    #[test]
    fn alpha_binds_then_agrees() {
        let f = features();
        let mut bindings = Bindings::default();
        let same = Value::One(alpha(AlphaOp::Same));
        let pat = [spec(&f, "high", same.clone()), spec(&f, "back", same)];
        assert!(pattern_matches(&pat, &fb(&f, "high=1 back=1"), Some(&mut bindings), PatternCtx::default()));
        assert_eq!(map_get(&bindings.alpha, 'α'), Some(&Limb::Int(1)));
    }

    #[test]
    fn alpha_disagreement_fails() {
        let f = features();
        let mut bindings = Bindings::default();
        let same = Value::One(alpha(AlphaOp::Same));
        let pat = [spec(&f, "high", same.clone()), spec(&f, "back", same)];
        assert!(!pattern_matches(&pat, &fb(&f, "high=1 back=0"), Some(&mut bindings), PatternCtx::default()));
    }

    #[test]
    fn alpha_in_contour_limb() {
        let f = features();
        let mut bindings = Bindings::default();
        map_set(&mut bindings.alpha, 'α', Limb::Int(2));
        let tone = Value::Contour(vec![Limb::Int(2), alpha(AlphaOp::Same)].into());
        let pat = [PatternSpec { contour_position: ContourPosition::Edge(ContourEdge::All), ..spec(&f, "tone", tone) }];
        assert!(pattern_matches(&pat, &fb(&f, "tone=2>2"), Some(&mut bindings), PatternCtx::default()));
        assert!(!pattern_matches(&pat, &fb(&f, "tone=2>3"), Some(&mut bindings), PatternCtx::default()));
    }
}

mod contour_position {
    use super::*;

    fn m(f: &FeatureInventory, spec: &str, seg: &str) -> bool {
        let bundle = parse_pattern_bundle(spec, f).unwrap();
        pattern_matches(&bundle, &fb(f, seg), Some(&mut Bindings::default()), PatternCtx::default())
    }

    #[test]
    fn single_value_at_named_edges() {
        let f = features();
        assert!(m(&f, "tone: 5@final", "tone=1>5"));
        assert!(!m(&f, "tone: 5@final", "tone=5>1"));
        assert!(m(&f, "tone: 5@initial", "tone=5>1"));
        assert!(!m(&f, "tone: 5@initial", "tone=1>5"));
    }

    #[test]
    fn single_value_at_numeric_position() {
        let f = features();
        assert!(m(&f, "tone: 5@2", "tone=1>5"));
        assert!(!m(&f, "tone: 5@2", "tone=5>1"));
    }

    #[test]
    fn single_value_at_multiple_positions() {
        let f = features();
        assert!(m(&f, "tone: 5@2;3", "tone=1>5>5"));
        assert!(!m(&f, "tone: 5@2;3", "tone=1>5>1"));
    }

    #[test]
    fn single_value_all() {
        let f = features();
        assert!(m(&f, "tone: 5@all", "tone=5>5"));
        assert!(!m(&f, "tone: 5@all", "tone=5>1"));
    }

    #[test]
    fn single_value_any_matches_contour() {
        let f = features();
        assert!(m(&f, "+high", "high=0>1"));
        assert!(!m(&f, "+high", "high=0>0"));
        assert!(m(&f, "+high", "high=1"));
    }

    #[test]
    fn contour_initial_final_window() {
        let f = features();
        assert!(m(&f, "tone: 1>2@initial", "tone=1>2>3"));
        assert!(!m(&f, "tone: 1>2@initial", "tone=3>1>2"));
        assert!(m(&f, "tone: 1>2@final", "tone=3>1>2"));
    }

    #[test]
    fn contour_any_is_subsequence() {
        let f = features();
        assert!(m(&f, "tone: 1>2@any", "tone=3>1>2"));
        assert!(!m(&f, "tone: 1>2@any", "tone=1>3>2"));
    }

    #[test]
    fn contour_default_all_is_exact() {
        let f = features();
        assert!(m(&f, "tone: 1>2", "tone=1>2"));
        assert!(!m(&f, "tone: 1>2", "tone=1>2>3"));
    }

    #[test]
    fn negated_positional() {
        let f = features();
        assert!(m(&f, "tone: !5@final", "tone=1>3"));
        assert!(!m(&f, "tone: !5@final", "tone=1>5"));
        assert!(!m(&f, "!+high", "high=0>1"));
        assert!(m(&f, "!+high", "high=0>0"));
    }

    // Python raises NotImplementedError; Rust panics.
    #[test]
    #[should_panic(expected = "alpha in a multi-limb @any contour pattern is not supported")]
    fn alpha_in_multi_limb_any_is_refused() {
        let f = features();
        m(&f, "tone: α>2@any", "tone=1>2");
    }
}

mod tier_aware_matching {
    use super::*;

    #[test]
    fn syllable_tier_spec_reads_the_nucleus() {
        // [+cons, tone: 3] matches the consonant: +cons against the segment, tone: 3 against
        // its syllable's nucleus.
        let f = features();
        let tone = FeatSet::from_ids([f.id("tone").unwrap()]);
        let nucleus = parse_pattern_bundle("+syll", &f).unwrap();
        let boundaries: Boundaries = [0, 2].into();
        let cons = fb(&f, "consonantal=1");
        let segs = [cons.clone(), fb(&f, "syllabic=1 tone=3")];
        let view = SyllableView { nuclei: nuclei_by_position(&arcs(&segs), &boundaries, &nucleus), floating: vec![] };
        let sd = parse(&f, "[+cons, tone: 3] -> [+voice]");
        let no_letters = LetterInventory::default();
        assert_eq!(spans_in(&f, &sd, &segs, &no_letters, &[], Some((&view, &tone))), [(0, 1)]);
        let segs4 = [cons, fb(&f, "syllabic=1 tone=4")];
        let view4 = SyllableView { nuclei: nuclei_by_position(&arcs(&segs4), &boundaries, &nucleus), floating: vec![] };
        assert!(spans_in(&f, &sd, &segs4, &no_letters, &[], Some((&view4, &tone))).is_empty());
        // Without the view, tone is matched on the consonant itself.
        assert!(spans(&f, &sd, &segs).is_empty());
    }
}

mod sequence_matcher {
    use super::*;

    #[test]
    fn target_only_finds_every_locus() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice]");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(0, 1), (2, 3)]);
    }

    #[test]
    fn no_locus_when_target_absent() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice]");
        assert!(spans(&f, &sd, &[fb(&f, "voice=1"), fb(&f, "voice=1")]).is_empty());
    }

    #[test]
    fn left_context_required() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] / [+voice] _");
        let segs = [fb(&f, "voice=1"), fb(&f, "nasal=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(1, 2)]);
    }

    #[test]
    fn right_context_required() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] / _ [+voice]");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(0, 1)]);
    }

    #[test]
    fn word_boundary_left() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] / # _");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(0, 1)]);
    }

    #[test]
    fn word_boundary_right() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] / _ #");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(2, 3)]);
    }

    #[test]
    fn syllable_boundary_never_matches_when_unsyllabified() {
        let f = features();
        let sd = parse(&f, "[+cons] -> [+voice] / $ _");
        assert!(spans(&f, &sd, &[fb(&f, "consonantal=1"), fb(&f, "consonantal=1")]).is_empty());
    }

    #[test]
    fn syllable_boundary_left_onset() {
        let f = features();
        let sd = parse(&f, "[+cons] -> [+voice] / $ _");
        let segs = [fb(&f, "consonantal=1"), fb(&f, "consonantal=1"), fb(&f, "consonantal=1")];
        assert_eq!(spans_in(&f, &sd, &segs, &LetterInventory::default(), &[0, 2], None), [(0, 1), (2, 3)]);
    }

    #[test]
    fn syllable_boundary_right_coda() {
        let f = features();
        let sd = parse(&f, "[+cons] -> [+voice] / _ $");
        let segs = [fb(&f, "consonantal=1"), fb(&f, "consonantal=1"), fb(&f, "consonantal=1")];
        assert_eq!(spans_in(&f, &sd, &segs, &LetterInventory::default(), &[2], None), [(1, 2)]);
    }

    #[test]
    fn exception_blocks() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] // [+voice] _");
        let segs = [fb(&f, "voice=1"), fb(&f, "nasal=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(2, 3)]);
    }

    #[test]
    fn quantifier_greedy() {
        let f = features();
        let sd = parse(&f, "[+nasal]{2} -> [+voice]");
        let segs = [fb(&f, "nasal=1"), fb(&f, "nasal=1"), fb(&f, "voice=1")];
        assert_eq!(spans(&f, &sd, &segs), [(0, 2)]);
    }

    #[test]
    fn disjunction_matches_either_branch() {
        let f = features();
        let sd = parse(&f, "([+nasal]|[+lateral]) -> [+voice]");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "lateral=1")];
        assert_eq!(spans(&f, &sd, &segs), [(0, 1), (2, 3)]);
    }

    #[test]
    fn negation_matches_non_target() {
        let f = features();
        let sd = parse(&f, "![+nasal] -> [+voice]");
        assert_eq!(spans(&f, &sd, &[fb(&f, "nasal=1"), fb(&f, "voice=1")]), [(1, 2)]);
    }

    #[test]
    fn alpha_agreement_across_context() {
        let f = features();
        let sd = parse(&f, "[αhigh] -> [+voice] / [αhigh] _");
        assert_eq!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=1")]), [(1, 2)]);
        assert!(spans(&f, &sd, &[fb(&f, "high=0"), fb(&f, "high=1")]).is_empty());
    }

    #[test]
    fn letter_ref_resolves_against_inventory() {
        let f = features();
        let sd = parse(&f, "m -> [+voice]");
        let m = fb(&f, "nasal=1 labial=1");
        let mut letters = LetterInventory::default();
        letters.insert(Letter { symbol: "m".into(), bundle: Arc::new(m.clone()) });
        assert_eq!(spans_in(&f, &sd, &[fb(&f, "voice=1"), m], &letters, &[], None), [(1, 2)]);
    }

    #[test]
    fn reference_bind_and_recall() {
        let f = features();
        let sd = parse(&f, "1=[+nasal] -> [+voice] / @1 _");
        let same = fb(&f, "nasal=1 labial=1");
        assert_eq!(spans(&f, &sd, &[same.clone(), same.clone()]), [(1, 2)]);
        let other = fb(&f, "nasal=1 labial=0");
        assert!(spans(&f, &sd, &[other, same]).is_empty());
    }

    #[test]
    fn multisegment_reference_bind_and_recall() {
        let f = features();
        let sd = parse(&f, "1=([+cons][+syll]) @1 -> @1");
        let (c, v) = (fb(&f, "consonantal=1 voice=1"), fb(&f, "syllabic=1 high=1"));
        assert_eq!(spans(&f, &sd, &[c.clone(), v.clone(), c.clone(), v.clone()]), [(0, 4)]);
        assert!(spans(&f, &sd, &[c, v.clone(), fb(&f, "consonantal=1 voice=0"), v]).is_empty());
    }

    #[test]
    fn reference_bound_in_right_context_recalled_to_the_left() {
        let f = features();
        let sd = parse(&f, "[+cons] -> [+voice] / @1 _ 1=[+nasal]");
        let (same, other, c) = (fb(&f, "nasal=1 labial=1"), fb(&f, "nasal=1 labial=0"), fb(&f, "consonantal=1"));
        assert_eq!(spans(&f, &sd, &[same.clone(), c.clone(), same.clone()]), [(1, 2)]);
        assert!(spans(&f, &sd, &[other, c, same]).is_empty());
    }

    #[test]
    fn target_recalling_a_right_context_binding() {
        let f = features();
        let sd = parse(&f, "@1 -> x / _ 1=[+nasal]");
        let (same, other) = (fb(&f, "nasal=1 labial=1"), fb(&f, "nasal=1 labial=0"));
        assert_eq!(spans(&f, &sd, &[same.clone(), same.clone()]), [(0, 1)]);
        assert!(spans(&f, &sd, &[other, same.clone()]).is_empty());
        assert!(spans(&f, &sd, &[same]).is_empty());
    }

    #[test]
    fn reference_bound_in_right_exception_recalled_to_the_left() {
        let f = features();
        let sd = parse(&f, "[+cons] -> [+voice] // @1 _ 1=[+nasal]");
        let (same, other, c) = (fb(&f, "nasal=1 labial=1"), fb(&f, "nasal=1 labial=0"), fb(&f, "consonantal=1"));
        assert!(spans(&f, &sd, &[same.clone(), c.clone(), same.clone()]).is_empty());
        assert_eq!(spans(&f, &sd, &[other, c, same]), [(1, 2)]);
    }
}

mod binding_order {
    use super::*;

    #[test]
    fn alpha_opposite_is_order_independent_disagreement() {
        let f = features();
        let ctx_left = parse(&f, "[αhigh] -> [+voice] / [-αhigh] _");
        assert_eq!(spans(&f, &ctx_left, &[fb(&f, "high=0"), fb(&f, "high=1")]), [(1, 2)]);
        assert!(spans(&f, &ctx_left, &[fb(&f, "high=1"), fb(&f, "high=1")]).is_empty());
        let ctx_right = parse(&f, "[-αhigh] -> [+voice] / [αhigh] _");
        assert_eq!(spans(&f, &ctx_right, &[fb(&f, "high=0"), fb(&f, "high=1")]), [(1, 2)]);
        assert!(spans(&f, &ctx_right, &[fb(&f, "high=1"), fb(&f, "high=1")]).is_empty());
    }

    #[test]
    fn unary_opposite_is_present_absent_opposition() {
        let f = features();
        let sd = parse(&f, "[α manner] -> [+voice] / [-α manner] _");
        let (has, lacks) = (fb(&f, "manner=1"), fb(&f, "consonantal=1"));
        assert_eq!(spans(&f, &sd, &[has.clone(), lacks.clone()]), [(1, 2)]);
        assert!(spans(&f, &sd, &[has.clone(), has.clone()]).is_empty());
        assert_eq!(spans(&f, &sd, &[lacks, has]), [(1, 2)]);
    }

    #[test]
    fn alpha_other_is_deferred_until_bound() {
        let f = features();
        let sd = parse(&f, "[!αhigh] -> [+voice] / _ [αhigh]");
        assert_eq!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=0")]), [(0, 1)]);
        assert!(spans(&f, &sd, &[fb(&f, "high=0"), fb(&f, "high=0")]).is_empty());
    }

    #[test]
    fn pass1_is_alpha_blind_for_multi_occurrence_target() {
        let f = features();
        let sd = parse(&f, "[-αhigh][αhigh] -> [+voice] / [αhigh] _");
        assert_eq!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=0"), fb(&f, "high=1")]), [(1, 3)]);
        assert!(spans(&f, &sd, &[fb(&f, "high=0"), fb(&f, "high=1"), fb(&f, "high=1")]).is_empty());
    }

    #[test]
    fn negated_alpha_element_defers_to_pass_two() {
        let f = features();
        let sd = parse(&f, "![αhigh] -> [+voice] / [αhigh] _");
        assert_eq!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=0")]), [(1, 2)]);
        assert!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=1")]).is_empty());
    }

    #[test]
    fn negated_alpha_spec_defers_to_pass_two() {
        let f = features();
        let sd = parse(&f, "[!-αhigh] -> [+voice] / [αhigh] _");
        assert_eq!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=1")]), [(1, 2)]);
        assert!(spans(&f, &sd, &[fb(&f, "high=1"), fb(&f, "high=0")]).is_empty());
    }
}

mod sequence_edge_cases {
    use super::*;

    #[test]
    fn null_target_marks_insertion_points() {
        let f = features();
        let sd = parse(&f, "∅ -> [+voice] / [+nasal] _");
        let segs = [fb(&f, "nasal=1"), fb(&f, "voice=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(1, 1), (3, 3)]);
    }

    #[test]
    fn zero_rep_quantifier() {
        let f = features();
        let sd = parse(&f, "[+nasal]{0,2} [+voice] -> [+lateral]");
        assert_eq!(spans(&f, &sd, &[fb(&f, "voice=1")]), [(0, 1)]);
    }

    #[test]
    fn right_only_exception() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice] // _ [+lateral]");
        let segs = [fb(&f, "nasal=1"), fb(&f, "lateral=1"), fb(&f, "nasal=1")];
        assert_eq!(spans(&f, &sd, &segs), [(2, 3)]);
    }
}

/// `cannot_match` is a conservative pre-check: it must never prune a rule that could still match.
mod necessary_condition_pruning {
    use super::*;

    #[test]
    fn prunes_when_a_required_feature_is_absent() {
        let f = features();
        let sd = parse(&f, "[+nasal] -> [+voice]");
        assert!(cannot(&sd, &[fb(&f, "consonantal=1"), fb(&f, "voice=1")]));
        assert!(!cannot(&sd, &[fb(&f, "nasal=1"), fb(&f, "voice=1")]));
    }

    #[test]
    fn charges_a_recall_for_a_second_copy() {
        let f = features();
        let sd = parse(&f, "1=[+nasal] @1 -> [+voice] @1");
        let n = fb(&f, "nasal=1 labial=1");
        assert!(cannot(&sd, &[n.clone(), fb(&f, "consonantal=1")]));
        assert!(!cannot(&sd, &[n.clone(), n]));
    }

    #[test]
    fn never_prunes_a_disjunction_branch_away() {
        let f = features();
        let sd = parse(&f, "([+nasal]|[+cons]) -> [+voice]");
        let segs = [fb(&f, "consonantal=1 sonorant=0"), fb(&f, "voice=1")];
        assert!(!cannot(&sd, &segs));
        assert_eq!(spans(&f, &sd, &segs), [(0, 1)]);
    }

    #[test]
    fn never_prunes_an_optional_element_away() {
        let f = features();
        let sd = parse(&f, "[+nasal]? [+cons] -> [-voice]");
        assert!(!cannot(&sd, &[fb(&f, "consonantal=1 voice=1")]));
    }
}
