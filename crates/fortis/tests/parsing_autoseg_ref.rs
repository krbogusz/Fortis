//! Port of `tests/parsing/test_autoseg_ref.py`: tier-autosegment reference parsing (`~n=value`
//! binds, `~n` recalls and spreads).

mod common;

use fortis::models::*;
use fortis::parsing::bundles::{parse_pattern_bundle, parse_result_bundle};

#[test]
fn bind_in_a_pattern() {
    let project = common::default_project();
    let tone = project.features.id("tone").unwrap();
    let bundle = parse_pattern_bundle("+syllabic, tone: ~1=high", &project.features).unwrap();
    let value = &bundle.iter().find(|s| s.feature == tone).unwrap().value;
    // 'high' is tone value 4.
    assert!(matches!(value, Value::One(Limb::Bind(b)) if b.r == 1 && b.value == 4), "found {value:?}");
}

#[test]
fn recall_in_a_result() {
    let project = common::default_project();
    let tone = project.features.id("tone").unwrap();
    let bundle = parse_result_bundle("tone: ~1", &project.features).unwrap();
    let value = &bundle.iter().find(|s| s.feature == tone).unwrap().value;
    assert_eq!(*value, Value::One(Limb::Recall(AutosegRecall { r: 1, optional: false })));
}

#[test]
fn recall_also_parses_in_a_pattern() {
    let project = common::default_project();
    let tone = project.features.id("tone").unwrap();
    let bundle = parse_pattern_bundle("+syllabic, tone: ~2", &project.features).unwrap();
    let value = &bundle.iter().find(|s| s.feature == tone).unwrap().value;
    assert_eq!(*value, Value::One(Limb::Recall(AutosegRecall { r: 2, optional: false })));
}

#[test]
fn non_numeric_reference_rejected() {
    let project = common::default_project();
    assert_eq!(
        parse_pattern_bundle("tone: ~x", &project.features).unwrap_err(),
        ["tier reference '~x' must be ~ followed by a reference number"]
    );
    assert_eq!(
        parse_pattern_bundle("tone: ~", &project.features).unwrap_err(),
        ["tier reference '~' must be ~ followed by a reference number"]
    );
}

#[test]
fn bind_with_an_invalid_inner_value_rejected() {
    let project = common::default_project();
    assert_eq!(
        parse_pattern_bundle("tone: ~1=nope", &project.features).unwrap_err(),
        ["Could not identify value for 'tone' from string 'nope'"]
    );
}
