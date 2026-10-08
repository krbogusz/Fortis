//! The `fortis` command end to end: a port of `tests/test_main.py`. The binary runs with the
//! frozen repository root (`tests/golden`), so the default project is the frozen copy. The
//! expected stderr and report texts are the Python program's output on the same input.

mod common;

use std::fs;
use std::io::Write;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::Arc;

use fortis::engine::deriving::Engine;
use fortis::engine::rendering::Renderer;
use fortis::engine::segmentation::string_to_sequence;
use fortis::loaders::lexicon::load_rule;
use fortis::models::*;
use fortis::reports;

fn golden() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("tests").join("golden")
}

/// A fresh, empty scratch folder for one case (pytest's `tmp_path`).
fn scratch(case: &str) -> PathBuf {
    let dir = std::env::temp_dir().join(format!("fortis-cli-{}-{case}", std::process::id()));
    let _ = fs::remove_dir_all(&dir);
    fs::create_dir_all(&dir).unwrap();
    dir
}

/// Run `fortis` from the frozen root, so `projects/default` resolves as it does from the
/// repository root in Python.
fn fortis(args: &[&str]) -> Output {
    Command::new(env!("CARGO_BIN_EXE_fortis"))
        .args(args)
        .current_dir(golden())
        .env("FORTIS_ROOT", golden())
        .env("NO_COLOR", "1")
        .output()
        .unwrap()
}

fn path(p: &Path) -> &str {
    p.to_str().unwrap()
}

/// Whether a word is a timing such as `0.08s`.
fn is_timing(word: &str) -> bool {
    word.strip_suffix('s').is_some_and(|n| n.contains('.') && n.chars().all(|c| c.is_ascii_digit() || c == '.'))
}

/// Each line with its timings replaced by `T`: they vary from run to run.
fn masked<S: AsRef<str>>(lines: &[S]) -> Vec<String> {
    lines
        .iter()
        .map(|line| line.as_ref().split(' ').map(|w| if is_timing(w) { "T" } else { w }).collect::<Vec<_>>().join(" "))
        .collect()
}

fn stderr_lines(out: &Output) -> Vec<String> {
    masked(&String::from_utf8(out.stderr.clone()).unwrap().lines().collect::<Vec<_>>())
}

fn read(path: &Path) -> String {
    fs::read_to_string(path).unwrap_or_else(|e| panic!("could not read '{}': {e}", path.display()))
}

fn csv_rows(text: &str) -> Vec<Vec<String>> {
    csv::ReaderBuilder::new()
        .has_headers(false)
        .flexible(true)
        .from_reader(text.as_bytes())
        .records()
        .map(|r| r.unwrap().iter().map(str::to_string).collect())
        .collect()
}

/// The first lexicon key of the default project, used as a seed IPA as the Python tests do.
fn first_ipa() -> String {
    common::default_project().words.keys().next().unwrap().clone()
}

/// A lexicon of one word, seeded with *ipa*, that carries the target `final` = `zzz`.
fn targeted_words(ipa: &str) -> String {
    format!(
        "[[words]]\nid = \"{ipa}\"\ngloss = \"x\"\n\
         forms = [{{ time = 0, ipa = \"{ipa}\" }}, {{ time = \"final\", ipa = \"zzz\" }}]\n"
    )
}

/// The summary of a run whose one word carries a target, with the default project's rules
/// all scoped to absent words.
const UNFIRED_RULES: [&str; 9] = [
    "  ⚠  28 rule(s) never fire — word-scoped to a word not in the lexicon:",
    "     voicing_assimilation, i_umlaut, final_devoicing, feature_override,",
    "     intervocalic_loss, epenthesis, degemination, tone_spread,",
    "     place_assimilation, tone_stability, tone_delinking, contour_tone,",
    "     stress, disjunction, gemination, exception, regressive_raising,",
    "     vowel_harmony, vowel_harmony_spread, morpheme_boundary_loss,",
    "     never_fires, contradictory_bundle, coda_lenition_early,",
    "     coda_lenition_late, lenition_voicing, lenition_spirantization,",
    "     lenition_loss, lenition_hiatus",
];

#[test]
fn main_derives_every_word() {
    // The shipped feature showcase, reports to the scratch folder.
    let dir = scratch("every-word");
    let out_path = dir.join("derivations.csv");
    let out = fortis(&["--output", path(&out_path)]);
    assert!(out.status.success());
    // The per-word cascade goes to derivations.csv; stdout is empty and the run summary,
    // with the accuracy headline, is on stderr.
    assert_eq!(String::from_utf8(out.stdout.clone()).unwrap(), "");
    let reports_line = format!("  10 reports → {}", dir.display());
    let expected = [
        "  ⚠  1 rule(s) never fire — word-scoped to a word not in the lexicon:",
        "     never_fires",
        "",
        "  Accuracy  21/21 exact (100.0%), mean phone 0.000, mean feature 0.000",
        "            also at stages 100, 200, 300 measured too",
        "  Errors    no errors — every assessed word is exact at the final",
        "  Blame     no wrong words to blame — every assessed word is exact",
        "  ⚠  ⚠ 1 word(s) fell back to sonority syllabification (onset/coda patterns admitted no split) — see warnings.md",
        "",
        "  25 words · 25/28 rules applied · 0.08s",
        "  init 0.01s · apply 0.01s · analysis 0.03s · write 0.03s",
        "",
        &reports_line,
        "  derivations · derivation_matrix · rule_firings · rule_dependencies ·",
        "  accuracy · distance_to_target · errors · error_context · blame · warnings",
    ];
    assert_eq!(stderr_lines(&out), masked(&expected));
    // A couple of the showcase derivations come through in the long-format trace.
    let trace = read(&out_path);
    let rows: Vec<&str> = trace.lines().collect();
    for row in [
        "voicing-assimilation,Voicing assimilation,,ak.ba,ag.ba,k→g", // k → g before b
        "final-devoicing,Final devoicing,,tag,tak,g→k",                // g → k word-finally
        "place-assimilation,Place assimilation,,an.ka,aŋ.ka,n→ŋ",      // node spread copies the velar's place
    ] {
        assert!(rows.contains(&row), "missing row {row}");
    }
}

#[test]
fn main_writes_derivation_matrix_csv() {
    // The rule × word matrix is written as derivation_matrix.csv, alongside the main report.
    let dir = scratch("matrix");
    assert!(fortis(&["--output", path(&dir.join("derivations.csv"))]).status.success());
    assert!(dir.join("derivation_matrix.csv").exists());
}

#[test]
fn lint_flag_passes_on_a_clean_project() {
    // A project with no unsatisfiable bundle: --lint exits 0 and writes no reports.
    let dir = scratch("lint-clean");
    fs::write(dir.join("words.toml"), "\"anpa\" = \"w\"\n").unwrap();
    fs::write(dir.join("rules.toml"), "[fine]\nwords = [\"w\"]\ndefinition = \"a -> e\"\n").unwrap();
    let out = fortis(&["--project", path(&dir), "--lint"]);
    assert_eq!(out.status.code(), Some(0));
    let expected = [
        "",
        "  Lint      0 unsatisfiable rule positions",
        "            every rule bundle can match at least one segment",
        "",
        "  0.01s",
    ];
    assert_eq!(stderr_lines(&out), masked(&expected));
    assert!(!dir.join("reports").exists());
}

#[test]
fn lint_flags_the_showcase_contradiction() {
    // The shipped showcase deliberately carries ONE unsatisfiable rule, its demo of this very
    // check, so --lint on projects/default exits 1 and names it.
    let out = fortis(&["--project", "projects/default", "--lint"]);
    assert_eq!(out.status.code(), Some(1));
    let expected = [
        "",
        "  ⚠  1 unsatisfiable rule position — a bundle that can never match a segment:",
        "     Contradictory bundle (showcase) · target  [front, oral: none]",
        "        front is required present, but its parent node oral is absent (`oral: none`)",
        "",
        "  0.01s",
    ];
    assert_eq!(stderr_lines(&out), masked(&expected));
}

#[test]
fn lint_flag_fails_on_an_unsatisfiable_bundle() {
    // A feature required present under a node required absent can never match: --lint exits 1.
    let dir = scratch("lint-impossible");
    fs::write(dir.join("words.toml"), "\"anpa\" = \"w\"\n").unwrap();
    fs::write(
        dir.join("rules.toml"),
        "[impossible]\nwords = [\"w\"]\n\
         definition = \"[+nasal] -> [oral: ~1] / _ [+consonantal, front, oral: none]\"\n",
    )
    .unwrap();
    let out = fortis(&["--project", path(&dir), "--lint"]);
    assert_eq!(out.status.code(), Some(1));
    let expected = [
        "",
        "  ⚠  1 unsatisfiable rule position — a bundle that can never match a segment:",
        "     impossible · right context  [+consonantal, front, oral: none]",
        "        front is required present, but its parent node oral is absent (`oral: none`)",
        "",
        "  0.03s",
    ];
    assert_eq!(stderr_lines(&out), masked(&expected));
}

#[test]
fn main_writes_rule_firings_csv() {
    // One row per rule: the words it matched (before → after) and its distinct changes.
    let dir = scratch("firings");
    assert!(fortis(&["--output", path(&dir.join("derivations.csv"))]).status.success());
    let rows = csv_rows(&read(&dir.join("rule_firings.csv")));
    assert_eq!(rows[0], ["rule", "t", "sporadic", "count", "changes", "matched"]);
    // Rules that changed at least one word.
    let fired: Vec<&Vec<String>> = rows[1..].iter().filter(|r| r[3].parse::<usize>().unwrap() > 0).collect();
    assert!(!fired.is_empty());
    for r in fired {
        assert!(!r[4].is_empty()); // changes (distinct segment deltas) are non-empty
        assert!(r[5].contains(" → ")); // matched holds `before → after` entries
        assert_eq!(r[5].split(", ").count(), r[3].parse::<usize>().unwrap()); // one entry per firing
    }
}

#[test]
fn main_writes_derivations_csv_long_format() {
    // The main report is derivations.csv: one row per word × rule, bookended by the synthetic
    // `input` (raw IPA → ingested form) and `output` (→ surface) rows.
    let dir = scratch("long-format");
    let out_path = dir.join("derivations.csv");
    assert!(fortis(&["--output", path(&out_path)]).status.success());
    let rows = csv_rows(&read(&out_path));
    assert_eq!(rows[0], ["word", "rule", "t", "before", "after", "change"]);
    let body = &rows[1..];
    assert_eq!(body[0][1], "input"); // the first row of the first word is its input
    // input's `before` is the raw IPA; `change` is empty on both synthetic rows.
    let inputs: Vec<&Vec<String>> = body.iter().filter(|r| r[1] == "input").collect();
    let outputs: Vec<&Vec<String>> = body.iter().filter(|r| r[1] == "output").collect();
    assert!(!inputs.is_empty() && inputs.len() == outputs.len()); // one of each per word
    assert!(inputs.iter().all(|r| !r[3].is_empty() && r[5].is_empty())); // before set, change empty
    // after set, before and change empty
    assert!(outputs.iter().all(|r| r[3].is_empty() && !r[4].is_empty() && r[5].is_empty()));
}

#[test]
fn main_writes_reports_into_subfolder() {
    // With --project (no --output), every report lands in <project>/reports/.
    let dir = scratch("subfolder");
    fs::write(dir.join("words.toml"), format!("\"{}\" = \"x\"\n", first_ipa())).unwrap();
    assert!(fortis(&["--project", path(&dir)]).status.success());
    assert!(dir.join("reports").join("derivations.csv").exists());
    assert!(dir.join("reports").join("derivation_matrix.csv").exists());
    assert!(!dir.join("derivations.csv").exists()); // not at the project root
}

#[test]
fn main_single_word_writes_single_reports() {
    // --single derives one word (found by IPA key) and writes single_*.csv, not the full run.
    let dir = scratch("single");
    let ipa = first_ipa();
    fs::write(dir.join("words.toml"), targeted_words(&ipa)).unwrap();
    let out = fortis(&["--project", path(&dir), "--single", &ipa]);
    assert!(out.status.success());
    let reports = dir.join("reports");
    assert!(reports.join("single_derivations.csv").exists());
    assert!(reports.join("single_accuracy.csv").exists()); // the word carries a target
    assert!(reports.join("single_blame.csv").exists());
    assert!(!reports.join("derivations.csv").exists()); // the whole-project run did not happen
    let reports_line = format!("  6 reports → {}", reports.display());
    let expected = [
        "",
        "  Single    voicing-assimilation ‘x’  →  vo.i.cing-as.si.mi.la.ti.on",
        "            in the lexicon",
        "  Accuracy  0/1 exact (0.0%), mean phone 19.000, mean feature 259.000",
        "",
        "  0.02s",
        "",
        &reports_line,
        "  single_derivations · single_accuracy · single_distance_to_target ·",
        "  single_errors · single_error_context · single_blame",
    ];
    assert_eq!(stderr_lines(&out), masked(&expected));
}

#[test]
fn main_single_word_by_gloss() {
    // A word absent from the lexicon key but matched by gloss still derives (from its IPA).
    let dir = scratch("single-gloss");
    fs::write(dir.join("words.toml"), format!("\"{}\" = \"hello\"\n", first_ipa())).unwrap();
    assert!(fortis(&["--project", path(&dir), "--single", "hello"]).status.success());
    assert!(dir.join("reports").join("single_derivations.csv").exists());
}

#[test]
fn main_single_word_not_in_lexicon_has_no_target_reports() {
    // A word not in the lexicon derives bare: only single_derivations.csv, no target reports.
    let dir = scratch("single-absent");
    let ipa = first_ipa();
    fs::write(dir.join("words.toml"), targeted_words(&ipa)).unwrap();
    // First a found run writes the target reports, then an absent word must clear them.
    assert!(fortis(&["--project", path(&dir), "--single", &ipa]).status.success());
    assert!(dir.join("reports").join("single_accuracy.csv").exists());
    assert!(fortis(&["--project", path(&dir), "--single", "ˈnot.a.word"]).status.success());
    let reports = dir.join("reports");
    assert!(reports.join("single_derivations.csv").exists());
    assert!(!reports.join("single_accuracy.csv").exists()); // stale target report cleared
}

#[test]
fn main_skips_accuracy_without_target() {
    // A lexicon with no attested forms (bare `word = "gloss"`) gets no accuracy report.
    let dir = scratch("no-target");
    fs::write(dir.join("words.toml"), format!("\"{}\" = \"x\"\n", first_ipa())).unwrap();
    assert!(fortis(&["--project", path(&dir)]).status.success());
    assert!(!dir.join("reports").join("accuracy.csv").exists());
}

#[test]
fn main_writes_accuracy_with_target() {
    // A minimal project (one word carrying a target `final`, everything else falling back to
    // the default inventory) triggers the accuracy CSVs, in reports/.
    let dir = scratch("target");
    fs::write(dir.join("words.toml"), targeted_words(&first_ipa())).unwrap();
    assert!(fortis(&["--project", path(&dir)]).status.success());
    let reports = dir.join("reports");
    assert_eq!(
        read(&reports.join("accuracy.csv")),
        "stage,assessed,exact,within 1,mean phone dist,mean feature dist\r\nfinal,1,0,0,19.000,259.000\r\n"
    );
    assert_eq!(
        read(&reports.join("distance_to_target.csv")),
        "stage,gloss,derived,target,d,fd,matches at,closest at\r\n\
         final,x,vo.i.cing-as.si.mi.la.ti.on,zzz,19,259,,final\r\n"
    );
    // No Markdown accuracy report is written.
    assert!(!reports.join("accuracy.md").exists());
    assert!(!reports.join("distances.md").exists());
}

#[test]
fn main_run_summary_splits_out_analysis() {
    // The end-of-run timing reports `analysis` (diagnosis + timeline + blame) apart from the
    // other phases, so each cost is visible.
    let dir = scratch("summary");
    fs::write(dir.join("words.toml"), targeted_words(&first_ipa())).unwrap();
    let out = fortis(&["--project", path(&dir)]);
    assert!(out.status.success());
    let reports_line = format!("  9 reports → {}", dir.join("reports").display());
    let mut expected: Vec<&str> = UNFIRED_RULES.to_vec();
    expected.extend([
        "",
        "  Accuracy  0/1 exact (0.0%), mean phone 19.000, mean feature 259.000",
        "  Errors    19 error site(s), 14 distinct; most common ∅→i (4×)",
        "            1 segment(s) too sparse to autopsy — omitted from error_context.csv: z @ final",
        "  Blame     1 wrong word(s); no rule-level culprit found",
        "",
        "  1 words · 0/28 rules applied · 0.02s",
        "  init 0.01s · apply 0.00s · analysis 0.00s · write 0.00s",
        "",
        &reports_line,
        "  derivations · derivation_matrix · rule_firings · rule_dependencies ·",
        "  accuracy · distance_to_target · errors · error_context · blame",
    ]);
    assert_eq!(stderr_lines(&out), masked(&expected));
}

// Python checks the two cases below on `_trace_lines`, the CLI's per-rule trace, which has no
// Rust counterpart. The reports that group a rule's steps the same way stand in for it:
// rule_firings.csv (one row per rule, each step as `before → after`) and the matrix header
// (`<time>: <name>` per rule). The expected texts are Python's `_build_rule_firings_csv` and
// `_build_matrix_csv` on the same derivation.

fn derive(word: &str, rules: &RuleInventory, project: &Project) -> Derivation {
    let seed_time = rules.by_time.keys().flatten().copied().min().unwrap_or(0);
    let seed = Attestation { ipa: word.to_string(), ..Default::default() };
    let word = Word { id: word.to_string(), forms: vec![(Some(seed_time), seed)], frequency: 1, ..Default::default() };
    let form = string_to_sequence(word.ipa(), project).unwrap();
    Engine::with_rules(project, rules).unwrap().derive(&word, form)
}

fn inventory(time: i64, rules: Vec<Rule>) -> RuleInventory {
    let mut inventory = RuleInventory::default();
    inventory.by_time.insert(Some(time), rules.into_iter().map(Arc::new).collect());
    inventory
}

#[test]
fn list_definition_substeps_share_one_heading() {
    // A list-definition rule's sub-steps (ids `name#1`, `#2`) render under a single heading,
    // one change each, not the rule name repeated per sub-step.
    let project = common::default_project();
    let spec: toml::Table = r#"
        time = -1000
        name = "Stress change to first syllable"
        definition = [
            "[+syll] → [stress: primary] / # [-syll]* _ []* [+syll, stress: primary]",
            "[+syll] → [stress: none] / [+syll] []* _",
        ]
    "#
    .parse()
    .unwrap();
    let rules = inventory(-1000, load_rule("stress_change", &spec, &project.features).unwrap());
    let derivation = derive("koˈta", &rules, &project);
    let r = Renderer::new(&project);
    // One row for the rule, both sub-steps' before → after shown, no `#1`/`#2` suffix.
    assert_eq!(
        reports::rule_firings_csv(std::slice::from_ref(&derivation), &rules, &r),
        "rule,t,sporadic,count,changes,matched\r\n\
         Stress change to first syllable,-1000,,2,\"o→ˈo, ˈa→a\",\"koˈta → ˈkoˈta, ˈkoˈta → ˈko.ta\"\r\n"
    );
    assert_eq!(
        reports::matrix_csv(&[derivation], &rules, &r),
        "ipa,gloss,-1000: Stress change to first syllable\r\nkoˈta,,ˈko.ta\r\n"
    );
}

#[test]
fn standalone_rule_keeps_its_own_heading() {
    // A plain (non-list) rule is its own heading, with its id shown when unnamed.
    let project = common::default_project();
    let spec: toml::Table = "time = 0\ndefinition = \"[+cons] → [-voice]\"\n".parse().unwrap();
    let rules = inventory(0, load_rule("devoicing", &spec, &project.features).unwrap());
    let derivation = derive("ˈba", &rules, &project);
    let r = Renderer::new(&project);
    // The unnamed rule falls back to its id (no suffix to strip).
    assert_eq!(
        reports::matrix_csv(std::slice::from_ref(&derivation), &rules, &r),
        "ipa,gloss,0: devoicing\r\nˈba,,ˈpa\r\n"
    );
    assert_eq!(
        reports::rule_firings_csv(&[derivation], &rules, &r),
        "rule,t,sporadic,count,changes,matched\r\ndevoicing,0,,1,b→p,ˈba → ˈpa\r\n"
    );
}

// `--segment` has no Python counterpart; its expected values come from the Python engine's
// string_to_sequence and syllabify at python-final on the same forms.

#[test]
fn segment_prints_segments_and_boundaries_per_line() {
    let dir = scratch("segment");
    let forms = dir.join("forms.txt");
    fs::write(&forms, "astra\na€b\n").unwrap();
    let out = fortis(&["--segment", path(&forms)]);
    assert!(out.status.success());
    assert_eq!(
        String::from_utf8(out.stdout).unwrap(),
        "{\"form\": \"astra\", \"segments\": [\"a\", \"s\", \"t\", \"r\", \"a\"], \"boundaries\": [0, 1, 5]}\n\
         {\"form\": \"a\\u20acb\", \"error\": \"Unknown character '\\u20ac' at position 1\"}\n"
    );
    let _ = fs::remove_dir_all(&dir);
}

#[test]
fn segment_time_selects_the_syllable_parts() {
    // The default project allows an s + stop + liquid onset only from time 500.
    let mut child = Command::new(env!("CARGO_BIN_EXE_fortis"))
        .args(["--segment", "-", "--time", "-2000"])
        .current_dir(golden())
        .env("FORTIS_ROOT", golden())
        .stdin(std::process::Stdio::piped())
        .stdout(std::process::Stdio::piped())
        .spawn()
        .unwrap();
    child.stdin.take().unwrap().write_all("astra\nekstra\n".as_bytes()).unwrap();
    let out = child.wait_with_output().unwrap();
    let lines: Vec<String> = String::from_utf8(out.stdout).unwrap().lines().map(str::to_string).collect();
    assert!(lines[0].ends_with("\"boundaries\": [0, 2, 5]}"), "{}", lines[0]);
    assert!(lines[1].ends_with("\"boundaries\": [0, 3, 6]}"), "{}", lines[1]);
}

#[test]
fn time_requires_segment() {
    let out = fortis(&["--time", "5"]);
    assert!(!out.status.success());
}
