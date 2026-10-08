//! Regression tests for bugs found in the bug hunt, each reproducing a fixed defect: a port of
//! `tests/test_regressions.py`. The expected error messages are the Python program's.

mod common;

use std::path::Path;
use std::sync::Arc;

use fortis::engine::applying::apply_match;
use fortis::engine::combining::merge;
use fortis::engine::matching::{FeatSet, Match, MatchCtx, target_recalls_context_binding};
use fortis::engine::segmentation::string_to_sequence;
use fortis::loaders::inventories::{load_feature, load_feature_inventory};
use fortis::models::*;
use fortis::parsing::bundles::{determine_contour_position, parse_feature_spec, parse_pattern_spec};
use fortis::parsing::notation::parse_definition;

/// A segment carrying *specs*, each a `(feature name, value)` pair.
fn fb(features: &FeatureInventory, specs: &[(&str, i64)]) -> Arc<FeatureBundle> {
    Arc::new(FeatureBundle { items: specs.iter().map(|(f, v)| (features.id(f).unwrap(), Value::int(*v))).collect() })
}

/// Python's `find_matches(sd, segments, letters)`: no syllable boundaries and no syllable view.
fn find_matches(sd: &StructuralDescription, segs: &[Arc<FeatureBundle>], project: &Project) -> Vec<Match> {
    let boundaries = Boundaries::new();
    let none = FeatSet::default();
    let cx = MatchCtx {
        segs,
        letters: &project.letters,
        boundaries: &boundaries,
        view: None,
        features: &project.features,
        syllable_features: &none,
    };
    cx.find_matches(sd, target_recalls_context_binding(sd))
}

#[test]
fn bare_feature_matches_any_value() {
    // `[cons]` means "consonantal present with any value": it must match both +cons and -cons
    // segments, not silently match nothing.
    let project = common::default_project();
    let f = &project.features;
    let sd = parse_definition("[cons] -> [+voice]", f).unwrap();
    let segs = [fb(f, &[("consonantal", 1)]), fb(f, &[("consonantal", 0)])];
    let spans: Vec<(usize, usize)> = find_matches(&sd, &segs, &project).iter().map(|m| (m.start, m.end)).collect();
    assert_eq!(spans, [(0, 1), (1, 2)]);
}

#[test]
fn value_label_matching_a_feature_name() {
    // `tone: high` must resolve to feature `tone`, not the feature `high` that the value label
    // `high` happens to spell.
    let project = common::default_project();
    let (feature, _) = parse_feature_spec("tone: high", &project.features, None).unwrap();
    assert_eq!(project.features.name(feature), "tone");
}

#[test]
fn scalar_value_label_requires_a_colon() {
    // A scalar feature's value LABEL must follow a colon (`tone: mid`): a bare label collides
    // with a feature name of the same spelling. Numbers and alpha markers are unambiguous and
    // need no colon; unary and binary features are unaffected.
    let project = common::default_project();
    let f = &project.features;
    assert!(parse_pattern_spec("tone: mid", f).is_ok()); // label + colon -> ok
    assert_eq!(
        parse_pattern_spec("mid tone", f).unwrap_err(), // bare label -> err
        "Scalar feature 'tone': a value label must follow a colon (write 'tone: mid', not a bare label)"
    );
    assert!(parse_pattern_spec("tone: 3", f).is_ok()); // number + colon -> ok
    assert!(parse_pattern_spec("tone3", f).is_ok()); // number, no colon -> ok
    assert!(parse_pattern_spec("α tone", f).is_ok()); // alpha on a scalar, no colon -> ok
    assert!(parse_pattern_spec("+nasal", f).is_ok()); // unary, no colon -> ok
    // Same rule holds in the realized (lexicon) context:
    assert!(parse_feature_spec("tone: high", f, None).is_ok());
    assert_eq!(
        parse_feature_spec("high tone", f, None).unwrap_err(),
        "Scalar feature 'tone': a value label must follow a colon (write 'tone: high', not a bare label)"
    );
}

#[test]
fn blank_short_field_defaults_to_feature_name() {
    // A whitespace-only `short` defaults to the feature name (was: silently ""). Python tests
    // its `load_short` helper; Rust reads the short name inside `load_feature`.
    let def: toml::Table = "kind = \"binary\"\nshort = \"   \"\n".parse().unwrap();
    assert_eq!(load_feature("nasal", &def).unwrap().short_name, "nasal");
}

#[test]
fn leading_diacritic_raises_cleanly() {
    // A diacritic with no preceding segment or nucleus is a clean error, not a panic or a
    // silent misattachment to the wrong segment.
    let project = common::default_project();
    assert_eq!(
        string_to_sequence("ʰa", &project).unwrap_err(), // segment-tier diacritic, no base
        "Diacritic 'ʰ' at position 0 has no preceding segment to attach to"
    );
    assert_eq!(
        string_to_sequence("t˥a", &project).unwrap_err(), // tone before any nucleus
        "Suprasegmental diacritic '˥' at position 1 has no preceding nucleus to attach to"
    );
}

#[test]
fn contour_position_zero_rejected() {
    // Contour positions are 1-based; the single-index path must reject 0.
    assert_eq!(determine_contour_position("0").unwrap_err(), "Contour position cannot be smaller than 1: '0'");
}

#[test]
fn variable_count_with_a_multi_segment_bound() {
    // A bound multi-segment group consumes more than one segment; the variable quantifier's
    // repetition count must subtract its real width, not assume width 1.
    let project = common::default_project();
    let f = &project.features;
    let sd = parse_definition("1=([+cons][+cons]) [-syll]* -> @1 a*", f).unwrap();
    let segs = [
        fb(f, &[("consonantal", 1)]),
        fb(f, &[("consonantal", 1)]),
        fb(f, &[("consonantal", 1), ("syllabic", 0)]),
        fb(f, &[("consonantal", 1), ("syllabic", 0)]),
    ];
    let m = find_matches(&sd, &segs, &project).into_iter().find(|m| (m.start, m.end) == (0, 4)).unwrap();
    let out = apply_match(&sd, &m, &segs, &project.letters, f);
    assert_eq!(out.len(), 4); // @1 replays 2 + a* repeats 2; was 5 (count inflated by 1)
    let a = (*project.letters.get("a").unwrap().bundle).clone();
    let expected = vec![((*segs[0]).clone(), None), ((*segs[1]).clone(), None), (a.clone(), None), (a, None)];
    assert_eq!(out, expected);
}

#[test]
fn upward_geometry_skips_a_non_unary_ancestor() {
    // Setting a daughter pulls in unary class nodes, but a scalar or binary ancestor carries a
    // value that cannot be inferred, so it must NOT be fabricated.
    let source = common::memory(&[(
        "features.toml",
        "place = { tier = \"segment\", kind = \"scalar\", short = \"pl\", \
         values = { 1 = \"labial\" }, children = [\"anterior\"] }\n\
         anterior = { tier = \"segment\", kind = \"binary\", short = \"ant\" }\n",
    )]);
    let inv = load_feature_inventory(&source, Path::new("features.toml")).unwrap();
    let out = merge(&FeatureBundle::new(), &fb(&inv, &[("anterior", 1)]), &inv, false);
    assert!(out.contains(inv.id("anterior").unwrap()) && !out.contains(inv.id("place").unwrap()));
}
