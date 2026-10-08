//! Syllabification-fallback and rendering warnings: a port of
//! `tests/analysis/test_warnings.py`.
//!
//! Each project is a scratch folder that supplies only the files a case needs, loaded over the
//! frozen default project; everything else (features, letters, the sonority scale) falls back to
//! the default per file. The expected texts are the Python program's.

mod common;

use std::fs;
use std::path::PathBuf;

use fortis::analysis::warnings::*;
use fortis::engine::deriving::Engine;
use fortis::engine::rendering::Renderer;
use fortis::engine::tiers::lower_tiers;
use fortis::loaders::files::Disk;
use fortis::loaders::load_project_from;
use fortis::models::*;

// onset and coda each exactly one consonant → any interior cluster must be exactly two.
const STRICT_PARTS: &str = "[0]\n\
    nucleus = { definition = \"+syll\" }\n\
    onset   = { definition = \"[-syll]\" }\n\
    coda    = { definition = \"[-syll]\" }\n";

/// The head of every warnings report, and the fallback section's text before its table.
const HEAD: [&str; 10] = [
    "# Warnings — the test project",
    "",
    "## Syllabification fallback",
    "",
    "Syllabification fell back to the **sonority Maximal Onset** division for the words",
    "below: the project's onset/coda patterns admitted no legal split for the listed",
    "cluster, so the sonority-based division was used instead (rather than leaving the",
    "word unsyllabified). Loosen the onset/coda patterns to cover these clusters, or",
    "accept the sonority fallback.",
    "",
];

const NO_FALLBACK: &str = "No syllabification fell back — every word matched the onset/coda patterns.";

/// The unspellable-segments section, which sits between the title and the fallback section.
const UNSPELLABLE: [&str; 24] = [
    "## Unspellable segments",
    "",
    "These segments carry features **no letter can express**, so they render as `�`.",
    "",
    "They used to render as the nearest letter, with the leftover features silently",
    "dropped — which made the one failure the engine cannot otherwise show you invisible.",
    "A bundle one feature away from `ɑ` printed as a perfectly ordinary `ɑ`, and yet **no",
    "rule written `ɑ → …` would ever match it**, because rendering is lossy and",
    "many-to-one while a letter PATTERN matches by exact identity. The rule fired on some",
    "words and passed silently over identical-looking others, with no error anywhere.",
    "",
    "The **mistaken for** column is the letter each one is a near-miss of — the letter it",
    "used to print as, and the letter whose rules will not match it.",
    "",
    "The usual cause is in the **rule named below**: a merge changed a segment's quality",
    "and left a feature of the old quality behind. A merge keeps every feature it does not",
    "mention, so un-rounding `o` with `rounded: none` and forgetting `labial: none` leaves",
    "an `ɑ` that is still labial. Clear the whole set of features that go with the quality",
    "you are changing (`rounded` **and** `labial`; `front` **and** `back`) — or, if the",
    "segment is real, add a letter or diacritic that can spell it.",
    "",
    "| renders as | mistaken for | features it carries that the letter cannot | produced by | sites | examples |",
    "| --- | --- | --- | --- | --- | --- |",
    "| `�` | `ɤ` | `labial` | `un-round o` | 1 | oh |",
];

/// *lines* as a text, each ending in a newline.
fn text(lines: &[&str]) -> String {
    lines.iter().map(|l| format!("{l}\n")).collect()
}

/// A fresh, empty scratch folder for one case (pytest's `tmp_path`).
fn scratch(case: &str) -> PathBuf {
    let dir = std::env::temp_dir().join(format!("fortis-warnings-{}-{case}", std::process::id()));
    let _ = fs::remove_dir_all(&dir);
    fs::create_dir_all(&dir).unwrap();
    dir
}

/// A project of *files* (name, text) over the frozen default, as `load_project(tmp_path)`.
fn project(case: &str, files: &[(&str, &str)]) -> Project {
    let dir = scratch(case);
    for (name, text) in files {
        fs::write(dir.join(name), text).unwrap();
    }
    load_project_from(&Disk, &common::projects().join("default"), Some(&dir), None, None).unwrap()
}

fn derive_all(project: &Project) -> Vec<Derivation> {
    Engine::new(project).unwrap().derive_all().unwrap()
}

#[test]
fn unpatternable_cluster_warns() {
    let words = "\"apta\" = \"ok\"\n\"astra\" = \"three\"\n";
    let project = project("cluster", &[("syllable_parts.toml", STRICT_PARTS), ("words.toml", words)]);
    let r = Renderer::new(&project);
    let warnings = syllabification_warnings(&derive_all(&project), &project, &r);
    // pt splits legally (one coda + one onset); str is three consonants, so no 1+1 split and
    // the sonority fallback is used.
    assert_eq!(warnings.iter().map(|w| w.ipa.as_str()).collect::<Vec<_>>(), ["astra"]);
    let astra = &warnings[0];
    assert_eq!(astra.form, "astra"); // the exact (unsyllabified) form the warning fired on
    assert_eq!(astra.clusters, ["str"]);
    assert_eq!(astra.syllabified, "as.tra");
}

#[test]
fn render_and_summary() {
    let words = "\"astra\" = \"three\"\n";
    let project = project("render", &[("syllable_parts.toml", STRICT_PARTS), ("words.toml", words)]);
    let r = Renderer::new(&project);
    let warnings = syllabification_warnings(&derive_all(&project), &project, &r);
    // The table row names the gloss, the cluster and the syllabified form.
    let mut expected = HEAD.to_vec();
    expected.extend([
        "| word | gloss | form | cluster | syllabified as |",
        "| --- | --- | --- | --- | --- |",
        "| `astra` | three | `astra` | `str` | `as.tra` |",
    ]);
    assert_eq!(render_warnings(&warnings, "the test project", &[]), text(&expected));
    assert_eq!(
        warnings_summary_line(&warnings, &[]),
        "⚠ 1 word(s) fell back to sonority syllabification (onset/coda patterns admitted no split) — see warnings.md"
    );
}

#[test]
fn no_patterns_never_warns() {
    // With only a nucleus and no onset/coda patterns, sonority is always used: there is no
    // pattern to fail, so nothing "falls back".
    let parts = "[0]\nnucleus = { definition = \"+syll\" }\n";
    let project = project("no-patterns", &[("syllable_parts.toml", parts), ("words.toml", "\"astra\" = \"three\"\n")]);
    let r = Renderer::new(&project);
    assert!(syllabification_warnings(&derive_all(&project), &project, &r).is_empty());
    assert_eq!(warnings_summary_line(&[], &[]), "no warnings");
}

#[test]
fn render_empty() {
    let mut expected = HEAD.to_vec();
    expected.push(NO_FALLBACK);
    assert_eq!(render_warnings(&[], "the test project", &[]), text(&expected));
}

// ── Unspellable segments ────────────────────────────────────────────────────────────────
//
// The engine's one otherwise-invisible failure: a rule whose merge changes a segment's quality
// but leaves a feature of the old quality behind. A merge keeps every feature it does not
// mention, so the result is a segment that is ALMOST a letter, and the renderer used to spell
// it as that letter, dropping the difference. It then looked identical to the real letter in
// every report while matching no rule written against it, because letter patterns match by
// exact identity. Now it renders as � and warns, naming the near-miss letter and the culprit.

/// A project whose one rule un-rounds /o/, completely or otherwise.
///
/// /o/ is [+rounded, +labial]; the letter ɤ is exactly /o/ without BOTH. So clearing only
/// `rounded` lands one feature short of a real letter, and clearing both lands on it.
fn leaky_project(case: &str, definition: &str) -> Project {
    let rules = format!("[unround]\ntime = 0\nname = \"un-round o\"\ndefinition = \"{definition}\"\n");
    project(case, &[("rules.toml", &rules), ("words.toml", "\"o\" = \"oh\"\n")])
}

#[test]
fn leaky_merge_renders_replacement_and_warns() {
    // Clearing `rounded` but not `labial` leaves a segment that is the letter ɤ plus a stray
    // `labial`: it is NOT ɤ, and must not be spelt as one.
    let project = leaky_project("leaky", "[+syll, +rounded] → [rounded: none]");
    let derivations = derive_all(&project);
    let r = Renderer::new(&project);
    let warnings = rendering_warnings(&derivations, &project, &r);
    assert_eq!(warnings.len(), 1);
    let warning = &warnings[0];
    assert_eq!(warning.dropped, ["labial"]); // the feature no letter can express
    assert_eq!(warning.nearest, "ɤ"); // what it will be MISTAKEN for
    assert_eq!(warning.rule, "un-round o"); // and who to blame
    // The surface says so out loud rather than lying with a plausible ɤ.
    assert_eq!(r.sequence(&lower_tiers(&derivations[0].surface)), "�");
}

#[test]
fn complete_merge_leaves_no_residue() {
    // The same rule, clearing `labial` too: now the result really IS the letter ɤ.
    let project = leaky_project("complete", "[+syll, +rounded] → [rounded: none, labial: none]");
    let derivations = derive_all(&project);
    let r = Renderer::new(&project);
    assert!(rendering_warnings(&derivations, &project, &r).is_empty());
    assert_eq!(r.sequence(&lower_tiers(&derivations[0].surface)), "ɤ");
}

#[test]
fn rendering_warning_reaches_the_report_and_summary() {
    let project = leaky_project("report", "[+syll, +rounded] → [rounded: none]");
    let r = Renderer::new(&project);
    let warnings = rendering_warnings(&derive_all(&project), &project, &r);
    let mut expected = vec![HEAD[0], HEAD[1]];
    expected.extend(UNSPELLABLE);
    expected.push("");
    expected.extend(&HEAD[2..]);
    expected.push(NO_FALLBACK);
    assert_eq!(render_warnings(&[], "the test project", &warnings), text(&expected));
    assert_eq!(
        warnings_summary_line(&[], &warnings),
        "⚠ 1 unspellable segment(s), 1 site(s) — no letter can express them, so they render as �; \
         worst: nearest 'ɤ' loses labial from 'un-round o' — see warnings.md"
    );
}

#[test]
fn blame_is_the_rule_that_produced_it_not_the_ones_that_carried_it() {
    // A second rule that merely lengthens the already-broken segment must not be blamed for it:
    // the fix belongs in the merge that leaked the feature, not in every later rule that touches
    // the segment (changing any feature makes the bundle look "new").
    let rules = "[unround]\ntime = 0\nname = \"un-round o\"\n\
                 definition = \"[+syll, +rounded] → [rounded: none]\"\n\
                 \n\
                 [lengthen]\ntime = 100\nname = \"lengthen it\"\n\
                 definition = \"[+syll] → [length: long]\"\n";
    let project = project("blame", &[("rules.toml", rules), ("words.toml", "\"o\" = \"oh\"\n")]);
    let r = Renderer::new(&project);
    let warnings = rendering_warnings(&derive_all(&project), &project, &r);
    assert_eq!(warnings.iter().map(|w| w.rule.as_str()).collect::<Vec<_>>(), ["un-round o"]); // not "lengthen it"
}
