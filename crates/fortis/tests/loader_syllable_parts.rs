//! The syllable parts loader, ported from `tests/loaders/test_syllable_parts.py`. Python's
//! `VALID_PART_TYPES` and `load_syllable_part` are private in Rust, so their cases run through
//! `load_syllable_parts_inventory`.

mod common;

use std::path::Path;

use fortis::loaders::inventories::{load_feature_inventory, load_syllable_parts_inventory};
use fortis::models::{FeatureInventory, SyllablePart, SyllablePartsInventory};

/// `MINIMAL_FEATURES_TOML` from `tests/conftest.py`.
const FEATURES_TOML: &str = r#"[consonantal]
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
    load_feature_inventory(&common::memory(&[("features.toml", FEATURES_TOML)]), Path::new("features.toml"))
        .expect("the minimal features load")
}

fn load(text: &str) -> Result<SyllablePartsInventory, Vec<String>> {
    load_syllable_parts_inventory(
        &common::memory(&[("syllable_parts.toml", text)]),
        Path::new("syllable_parts.toml"),
        &features(),
    )
}

/// Python's `load_syllable_part(part_type, time, {"definition": definition})`, as a one-part file.
fn load_part(part_type: &str, time: i64, definition: Option<&str>) -> Result<SyllablePart, Vec<String>> {
    let table = definition.map(|d| format!("{{ definition = \"{d}\" }}")).unwrap_or("{}".into());
    let inventory = load(&format!("[{time}]\n{part_type} = {table}\n"))?;
    Ok(inventory.by_time[&time][part_type].as_ref().clone())
}

mod valid_part_types {
    use super::*;

    #[test]
    fn types() {
        // Python compares VALID_PART_TYPES with {"onset", "nucleus", "coda"}: each loads, and the
        // error for any other type lists exactly those.
        let inventory = load("[0]\nonset = {}\nnucleus = {}\ncoda = {}\n").unwrap();
        assert_eq!(inventory.by_time[&0].keys().collect::<Vec<_>>(), ["onset", "nucleus", "coda"]);
        assert_eq!(
            load_part("rime", 0, None).unwrap_err(),
            ["Invalid syllable part type 'rime' (expected coda, nucleus, onset)"]
        );
    }
}

mod load_syllable_part {
    use super::*;

    #[test]
    fn valid_nucleus() {
        let sp = load_part("nucleus", -2000, Some("+syll")).unwrap();
        assert_eq!(sp.part_type, "nucleus");
        assert_eq!(sp.time, -2000);
        assert!(sp.definition.is_some());
        assert!(sp.pattern.is_none());
    }

    #[test]
    fn onset_parses_definition_as_sequence() {
        // An onset definition is an element sequence: a consonant + optional glide.
        let sp = load_part("onset", 0, Some("[+cons][-syllabic, -consonantal]?")).unwrap();
        assert!(sp.definition.is_none());
        assert_eq!(sp.pattern.unwrap().len(), 2); // two elements: the consonant and the optional glide
    }

    #[test]
    fn onset_bad_pattern_errors() {
        assert_eq!(
            load_part("onset", 0, Some("[+nope]")).unwrap_err(),
            ["No feature could be identified from '+nope' at position 0"]
        );
    }

    #[test]
    fn invalid_part_type() {
        assert_eq!(
            load_part("codu", -2000, None).unwrap_err(),
            ["Invalid syllable part type 'codu' (expected coda, nucleus, onset)"]
        );
    }

    #[test]
    fn without_definition() {
        let sp = load_part("onset", -2000, None).unwrap();
        assert!(sp.definition.is_none());
    }
}

mod load_syllable_parts_inventory {
    use super::*;

    #[test]
    fn from_file() {
        let inv = load("[-2000]\nnucleus = { definition = \"+syll\" }\n").unwrap();
        assert!(inv.by_time[&-2000].contains_key("nucleus"));
    }

    #[test]
    fn non_integer_time() {
        assert_eq!(
            load("[abc]\nnucleus = { definition = \"+syll\" }\n").unwrap_err(),
            ["Syllable part time 'abc' is not a valid integer"]
        );
    }
}
