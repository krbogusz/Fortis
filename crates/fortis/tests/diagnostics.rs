//! The diagnostics tools: a port of `tests/analysis/test_diagnostics.py`. Covers the match-set
//! query and the unsatisfiable-bundle check. The expected values are the Python program's.

mod common;

use std::fs;
use std::path::PathBuf;
use std::sync::Arc;

use fortis::analysis::diagnostics::{Unsatisfiable, match_set, unsatisfiable_rules};
use fortis::loaders::files::Disk;
use fortis::loaders::lexicon::load_rule;
use fortis::loaders::load_project_from;
use fortis::models::*;

/// A fresh, empty scratch folder for one case (pytest's `tmp_path`).
fn scratch(case: &str) -> PathBuf {
    let dir = std::env::temp_dir().join(format!("fortis-diagnostics-{}-{case}", std::process::id()));
    let _ = fs::remove_dir_all(&dir);
    fs::create_dir_all(&dir).unwrap();
    dir
}

/// A frozen project directory loaded over the frozen default, as `load_project(dir)` does.
fn load(dir: &std::path::Path) -> Project {
    load_project_from(&Disk, &common::projects().join("default"), Some(dir), None, None).unwrap()
}

/// `(rule, time, role, label, reason)` per finding, for comparing whole findings.
fn fields(findings: &[Unsatisfiable]) -> Vec<(&str, Option<i64>, &str, &str, &str)> {
    findings.iter().map(|f| (f.rule.as_str(), f.time, f.role, f.label.as_str(), f.reason.as_str())).collect()
}

#[test]
fn match_set_returns_the_engines_denotation_of_a_bundle() {
    // The whole point: the answer is the engine's own match, so a bundle's real reach is visible.
    let proj = common::default_project();
    let (matched, total) = match_set("+nasal", &proj).unwrap();
    assert_eq!(total, proj.letters.len());
    // In inventory order (not sorted), so it reads like the letters file; no plain oral stop.
    let expected = [
        "m", "ɱ", "n", "ɳ", "ɲ", "ŋ", "ɴ", "ŋ͡ʘ", "ŋ͡ǀ", "ŋ͡ǃ", "ŋ͡𝼊", "ŋ͡ǂ", "ŋ͡ǁ",
        "ɴ͡ʘ", "ɴ͡ǀ", "ɴ͡ǃ", "ɴ͡𝼊", "ɴ͡ǂ", "ɴ͡ǁ",
    ];
    assert_eq!(matched, expected);
}

#[test]
fn coronal_front_overlap_is_surfaced_not_hidden() {
    // The canonical feature-system surprise: [+front] is the coronal place node too, so a bundle
    // meaning "front glide/sonorant" also catches every coronal. The tool must show that.
    let proj = common::default_project();
    let (matched, _) = match_set("+front, +sonorant, -syllabic", &proj).unwrap();
    // The coronals n, l, r and the palatal glide j, together.
    let expected = [
        "n", "ɳ", "ɲ", "ɹ", "ɻ", "j", "ɥ", "ɾ", "ɽ", "r", "ɽr", "l", "ɫ", "ɭ", "ʎ", "ɺ", "ŋ͡ǀ", "ŋ͡ǃ", "ŋ͡𝼊", "ŋ͡ǂ",
        "ŋ͡ǁ", "ɴ͡ǀ", "ɴ͡ǃ", "ɴ͡𝼊", "ɴ͡ǂ", "ɴ͡ǁ",
    ];
    assert_eq!(matched, expected);
}

#[test]
fn brackets_are_optional() {
    let proj = common::default_project();
    let (bracketed, _) = match_set("[+nasal]", &proj).unwrap();
    assert_eq!(bracketed, match_set("+nasal", &proj).unwrap().0);
}

#[test]
fn empty_input_is_a_friendly_error() {
    let err = match_set("   ", &common::default_project()).unwrap_err();
    assert_eq!(err, "Enter a feature bundle, e.g. +front, +sonorant, -syllabic");
}

#[test]
fn unknown_feature_surfaces_the_parse_error_as_a_string() {
    let err = match_set("+bogus", &common::default_project()).unwrap_err();
    assert_eq!(err, "No feature could be identified from '+bogus'");
}

#[test]
fn rule_only_specs_are_rejected_with_a_clear_message() {
    // References, agreement variables, and conditionals silently match all-or-nothing without a
    // rule's bindings, so they are rejected up front rather than returning a misleading set.
    let proj = common::default_project();
    for (query, offender) in [("oral: ~1", "oral"), ("αvoice", "voice"), ("<1: aperture: high>", "aperture")] {
        let err = match_set(query, &proj).unwrap_err();
        assert_eq!(
            err,
            format!(
                "References (~n), agreement variables (α), and conditionals (<n: …>) only mean something inside a \
                 rule — remove: {offender}"
            )
        );
    }
}

// --- unsatisfiable-bundle check -------------------------------------------------------------

/// The lint's reason for a rule whose target is the bundle *raw*, or `None` when it can match.
/// Python tests its private `_contradiction`; the Rust one is private too, so a project whose
/// one rule carries the bundle takes it to the public `unsatisfiable_rules`.
fn contradicts(raw: &str) -> Option<String> {
    let mut proj = common::default_project();
    let def: toml::Table = format!("definition = \"[{raw}] -> [+voice]\"\n").parse().unwrap();
    let rules = load_rule("probe", &def, &proj.features).unwrap();
    proj.rules = RuleInventory::default();
    proj.rules.by_time.insert(None, rules.into_iter().map(Arc::new).collect());
    let findings = unsatisfiable_rules(&proj);
    assert!(findings.len() <= 1);
    findings.into_iter().next().map(|f| f.reason)
}

#[test]
fn child_present_under_absent_ancestor_is_unsatisfiable() {
    // front → lingual → oral: requiring front present while removing an ancestor node can never
    // match, at any depth of the geometry chain.
    let reason = |child: &str, node: &str| {
        Some(format!("{child} is required present, but its parent node {node} is absent (`{node}: none`)"))
    };
    assert_eq!(contradicts("front, oral: none"), reason("front", "oral")); // front under lingual under oral
    assert_eq!(contradicts("labial, oral: none"), reason("labial", "oral"));
    assert_eq!(contradicts("front, lingual: none"), reason("front", "lingual")); // immediate parent
    assert_eq!(contradicts("+voice, glottal: none"), reason("voice", "glottal")); // voice under glottal
}

#[test]
fn independent_node_absence_is_satisfiable() {
    // nasal hangs off root, not oral, so removing oral does not contradict a present nasal.
    assert_eq!(contradicts("+nasal, oral: none"), None);
    assert_eq!(contradicts("front, lingual"), None); // both present: consistent
    assert_eq!(contradicts("aperture: high"), None);
}

#[test]
fn real_projects_have_no_unsatisfiable_rules() {
    for name in ["halle_vaux_wolfe", "spe", "latin_to_french"] {
        let proj = load(&common::projects().join(name));
        assert_eq!(fields(&unsatisfiable_rules(&proj)), [], "{name}");
    }
}

#[test]
fn default_project_carries_exactly_the_showcase_contradiction() {
    // The shipped showcase deliberately includes one unsatisfiable rule: the demo of this check.
    let findings = unsatisfiable_rules(&common::default_project());
    assert_eq!(
        fields(&findings),
        [(
            "Contradictory bundle (showcase)",
            None,
            "target",
            "[front, oral: none]",
            "front is required present, but its parent node oral is absent (`oral: none`)"
        )]
    );
}

#[test]
fn unsatisfiable_rule_is_reported_with_rule_and_reason() {
    let dir = scratch("reported");
    fs::write(dir.join("words.toml"), "\"anpa\" = \"w\"\n").unwrap();
    fs::write(
        dir.join("rules.toml"),
        "[bad]\nwords = [\"w\"]\n\
         definition = \"[+nasal] -> [oral: ~1] / _ [+consonantal, front, oral: none]\"\n",
    )
    .unwrap();
    let findings = unsatisfiable_rules(&load(&dir));
    assert_eq!(
        fields(&findings),
        [(
            "bad",
            None,
            "right context",
            "[+consonantal, front, oral: none]",
            "front is required present, but its parent node oral is absent (`oral: none`)"
        )]
    );
}
