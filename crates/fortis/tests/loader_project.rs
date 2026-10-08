//! Project assembly, ported from `tests/loaders/test_project.py`.
//!
//! The default project has 'voicing assimilation' (gloss) / 'voicing-assimilation' (id) / 'akba'
//! (seed ipa); a `words` scope may name any of the three.

mod common;

use std::fs;
use std::path::Path;

use fortis::loaders::files::Memory;
use fortis::loaders::{load_project_from, unfired_scoped_rules};
use fortis::models::Project;

/// The frozen default project's files at their disk paths, plus a `rules.toml` holding *rules*.
fn source(rules: &str) -> Memory {
    let mut source = common::memory(&[("rules.toml", rules)]);
    for entry in fs::read_dir(common::projects().join("default")).unwrap() {
        let path = entry.unwrap().path();
        source.0.insert(path.clone(), fs::read_to_string(&path).unwrap());
    }
    source
}

/// Python's `load_project(_PIE, rules_path=rules)`.
fn load_project(rules: &str) -> Project {
    let defaults = common::projects().join("default");
    load_project_from(&source(rules), &defaults, Some(&defaults), None, Some(Path::new("rules.toml"))).unwrap()
}

#[test]
fn word_scope_unknown_word_is_flagged() {
    // A `words` entry matching no word (by ipa or gloss) is a likely typo, so it is flagged,
    // not an error: the project still loads, and the rule is reported as never-firing.
    let project = load_project("[r]\nwords = [\"snu\"]\ndefinition = \"a → e\"\n");
    assert!(unfired_scoped_rules(&project.rules, &project.words).contains(&("r".to_string(), "snu".to_string())));
}

#[test]
fn word_scope_known_word_is_not_flagged() {
    // Matching by gloss, id or seed ipa is fine: nothing flagged.
    let project = load_project(
        "[r]\nwords = [\"voicing assimilation\", \"voicing-assimilation\", \"akba\"]\ndefinition = \"a → e\"\n",
    );
    assert_eq!(unfired_scoped_rules(&project.rules, &project.words), Vec::<(String, String)>::new());
}
