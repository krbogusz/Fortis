//! The top-level project loader (integration), ported from `tests/loaders/test_inventories.py`.

mod common;

use std::fs;
use std::path::Path;

use fortis::loaders::files::Memory;
use fortis::loaders::load_project_from;
use fortis::models::Project;

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
"#;

const LETTERS_CSV: &str = "symbol,consonantal,sonorant\nm,+,+\n";

const DIACRITICS_TOML: &str = "\"\u{329}\" = { tier = \"segment\", kind = \"combining\", bundle = \"+syll\" }\n";

const SONORITIES_TOML: &str =
    "vowel = { level = 7, bundle = \"+syllabic\" }\nstop = { level = 1, bundle = \"-sonorant\" }\n";

const SYLLABLE_PARTS_TOML: &str = "[-2000]\nnucleus = { definition = \"+syll\" }\n";

const WORDS_TOML: &str = "\"xenti\" = \"in front\"\n";

const RULES_TOML: &str = "[test_rule]\ntime = -2000\ndefinition = \"m → n\"\n";

/// The frozen default project's files at their disk paths (the fall-back), plus the project's
/// *files* under `project/`.
fn source(files: &[(&str, &str)]) -> Memory {
    let mut source = common::memory(&[]);
    for entry in fs::read_dir(common::projects().join("default")).unwrap() {
        let path = entry.unwrap().path();
        source.0.insert(path.clone(), fs::read_to_string(&path).unwrap());
    }
    for (name, text) in files {
        source.0.insert(Path::new("project").join(name), text.to_string());
    }
    source
}

fn load_project(files: &[(&str, &str)]) -> Result<Project, Vec<String>> {
    let defaults = common::projects().join("default");
    load_project_from(&source(files), &defaults, Some(Path::new("project")), None, None)
}

mod load_project {
    use super::*;

    #[test]
    fn full_load() {
        let project = load_project(&[
            ("features.toml", FEATURES_TOML),
            ("letters.csv", LETTERS_CSV),
            ("diacritics.toml", DIACRITICS_TOML),
            ("sonorities.toml", SONORITIES_TOML),
            ("syllable_parts.toml", SYLLABLE_PARTS_TOML),
            ("words.toml", WORDS_TOML),
            ("rules.toml", RULES_TOML),
            // This fixture's minimal feature set has no tone/stress, so it declares its own (empty)
            // tiers rather than inheriting the shipped tone/stress tiers via fall-back.
            ("tiers.toml", "# no autosegmental tiers\n"),
        ])
        .unwrap();
        assert!(project.features.contains("consonantal"));
        assert!(project.letters.contains("m"));
        assert!(project.diacritics.contains("\u{329}"));
        assert!(project.sonorities.iter().any(|s| s.label == "vowel"));
        assert!(project.syllable_parts.by_time.contains_key(&-2000));
        assert!(project.words.contains_key("xenti"));
    }

    #[test]
    fn missing_files_fall_back_to_defaults() {
        // A project that omits files (here, all but the lexicon) uses the shipped
        // defaults, so re-using the default feature system needs no features.toml.
        let project = load_project(&[("words.toml", WORDS_TOML)]).unwrap();
        assert!(project.features.contains("consonantal")); // the default feature system, via fallback
        assert!(project.words.contains_key("xenti")); // the project's own lexicon
    }

    #[test]
    fn invalid_features() {
        let result = load_project(&[
            ("features.toml", "[bad]\nkind = 'invalid'\n"),
            ("letters.csv", LETTERS_CSV),
            ("diacritics.toml", DIACRITICS_TOML),
            ("sonorities.toml", SONORITIES_TOML),
            ("syllable_parts.toml", SYLLABLE_PARTS_TOML),
            ("words.toml", WORDS_TOML),
        ]);
        assert_eq!(
            result.unwrap_err(),
            ["Feature 'bad' has an invalid kind 'invalid' (expected unary, binary, scalar)"]
        );
    }
}
