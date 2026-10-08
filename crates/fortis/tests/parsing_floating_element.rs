//! Port of `tests/parsing/test_floating_element.py`: parsing the floating-autosegment notation
//! `⟨...⟩`.

mod common;

use fortis::models::*;
use fortis::parsing::notation::parse_definition;
use fortis::parsing::validation::validate_structural_description;

/// The value of the `tone` spec in the floating autosegment that opens the target.
fn floating_tone(sd: &StructuralDescription, features: &FeatureInventory) -> Value {
    let Element::FloatingAutoseg(pattern) = &sd.target[0] else {
        panic!("expected a FloatingAutoseg, found {:?}", sd.target[0]);
    };
    let tone = features.id("tone").unwrap();
    pattern.iter().find(|s| s.feature == tone).unwrap().value.clone()
}

#[test]
fn floating_element_parses_as_floating_autoseg() {
    let project = common::default_project();
    let sd = parse_definition(
        "⟨tone: ~1=high⟩ [+syllabic, tone: none] -> [+syllabic, tone: ~1]",
        &project.features,
    )
    .unwrap();
    let value = floating_tone(&sd, &project.features);
    assert!(matches!(value, Value::One(Limb::Bind(b)) if b.r == 1), "found {value:?}");
}

#[test]
fn plain_floating_tone_parses() {
    let project = common::default_project();
    let sd = parse_definition("⟨tone: high⟩ [+syllabic] -> [+syllabic]", &project.features).unwrap();
    assert_eq!(floating_tone(&sd, &project.features), Value::int(4));
}

#[test]
fn unterminated_floating_bracket_rejected() {
    let project = common::default_project();
    assert_eq!(
        parse_definition("⟨tone: high [+syll] -> [+syll]", &project.features).unwrap_err(),
        ["unterminated floating autosegment at position 0"]
    );
}

#[test]
fn dock_rule_validates() {
    let project = common::default_project();
    let sd = parse_definition(
        "⟨tone: ~1=high⟩ [+syllabic, tone: none] -> [+syllabic, tone: ~1]",
        &project.features,
    )
    .unwrap();
    // Python validates without a feature inventory here.
    assert_eq!(validate_structural_description(&sd, None), Ok(()));
}
