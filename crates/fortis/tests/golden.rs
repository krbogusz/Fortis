//! Golden-report tests. The binaries run on frozen copies of the five shipped projects
//! (`tests/golden/projects/`), and every file they write must equal the saved file under
//! `tests/golden/expected/`. The saved files are the Python program's output at the tag
//! `python-final`, so these tests carry its behavior forward.
//!
//! After a change meant to alter the reports, rewrite the saved files and review the diff:
//! `UPDATE_GOLDEN=1 cargo test --test golden`.
//!
//! The inducer's runs on `latin_to_french` and `pie_to_english` take minutes in a debug build,
//! so they are ignored by default: `cargo test --release --test golden -- --ignored`.

use std::fs;
use std::path::{Path, PathBuf};
use std::process::Command;

fn golden() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("tests").join("golden")
}

/// A fresh, empty scratch folder for one case.
fn scratch(case: &str) -> PathBuf {
    let dir = std::env::temp_dir().join(format!("fortis-golden-{}-{case}", std::process::id()));
    let _ = fs::remove_dir_all(&dir);
    fs::create_dir_all(&dir).unwrap();
    dir
}

/// Run a binary with the frozen projects as the repository root; return its stdout.
fn run(bin: &str, args: &[&str]) -> String {
    let out = Command::new(bin)
        .args(args)
        .current_dir(golden())
        .env("FORTIS_ROOT", golden())
        .env("NO_COLOR", "1")
        .output()
        .unwrap();
    assert!(out.status.success(), "{bin} {args:?} failed:\n{}", String::from_utf8_lossy(&out.stderr));
    String::from_utf8(out.stdout).unwrap()
}

/// Compare every file in *actual* with the saved files for *case*, or save them.
fn check(case: &str, actual: &Path) {
    let expected = golden().join("expected").join(case);
    if std::env::var_os("UPDATE_GOLDEN").is_some() {
        let _ = fs::remove_dir_all(&expected);
        fs::create_dir_all(&expected).unwrap();
        for entry in fs::read_dir(actual).unwrap() {
            let path = entry.unwrap().path();
            fs::copy(&path, expected.join(path.file_name().unwrap())).unwrap();
        }
        return;
    }
    let names = |dir: &Path| {
        let mut names: Vec<String> = fs::read_dir(dir)
            .unwrap_or_else(|e| panic!("no saved reports for {case} in {}: {e}", dir.display()))
            .map(|e| e.unwrap().file_name().to_string_lossy().into_owned())
            .collect();
        names.sort();
        names
    };
    assert_eq!(names(actual), names(&expected), "{case}: a different set of files");
    for name in names(&expected) {
        let want = fs::read_to_string(expected.join(&name)).unwrap();
        let got = fs::read_to_string(actual.join(&name)).unwrap();
        if want != got {
            let line = want.lines().zip(got.lines()).position(|(a, b)| a != b).unwrap_or(want.lines().count().min(got.lines().count()));
            panic!(
                "{case}/{name} differs at line {}:\n  saved: {}\n  now:   {}",
                line + 1,
                want.lines().nth(line).unwrap_or("<end of file>"),
                got.lines().nth(line).unwrap_or("<end of file>")
            );
        }
    }
}

fn full_run(project: &str) {
    let out = scratch(&format!("{project}-run"));
    let derivations = out.join("derivations.csv");
    run(env!("CARGO_BIN_EXE_fortis"), &["--project", &format!("projects/{project}"), "--autosegmental", "--output", derivations.to_str().unwrap()]);
    check(&format!("{project}/run"), &out);
    let _ = fs::remove_dir_all(&out);
}

/// `--single` on the first and last words of the lexicon, and on a word in no lexicon.
fn single_runs(project: &str, words: [&str; 3]) {
    for (i, word) in words.into_iter().enumerate() {
        let case = format!("{project}/single-{}", i + 1);
        let out = scratch(&case.replace('/', "-"));
        let derivations = out.join("derivations.csv");
        run(env!("CARGO_BIN_EXE_fortis"), &["--project", &format!("projects/{project}"), "--single", word, "--output", derivations.to_str().unwrap()]);
        check(&case, &out);
        let _ = fs::remove_dir_all(&out);
    }
}

fn scoreboard(project: &str) {
    let case = format!("{project}/scoreboard");
    let out = scratch(&case.replace('/', "-"));
    let report = out.join("scoreboard.md");
    let stdout = run(env!("CARGO_BIN_EXE_fortis-scoreboard"), &["--project", &format!("projects/{project}"), "--output", report.to_str().unwrap()]);
    fs::write(out.join("scoreboard.stdout"), stdout).unwrap();
    check(&case, &out);
    let _ = fs::remove_dir_all(&out);
}

fn induce(project: &str) {
    induce_with(project, "induce", &[]);
}

/// The inducer with extra options, saved as case `<project>/<name>`.
fn induce_with(project: &str, name: &str, options: &[&str]) {
    let case = format!("{project}/{name}");
    let out = scratch(&case.replace('/', "-"));
    let (rules, report) = (out.join("induced_rules.toml"), out.join("induction.md"));
    let project_dir = format!("projects/{project}");
    let mut args = vec!["--project", &project_dir, "--out", rules.to_str().unwrap(), "--report", report.to_str().unwrap()];
    args.extend_from_slice(options);
    let stdout = run(env!("CARGO_BIN_EXE_fortis-induce"), &args);
    fs::write(out.join("induce.stdout"), stdout).unwrap();
    check(&case, &out);
    let _ = fs::remove_dir_all(&out);
}

macro_rules! project_tests {
    ($run:ident, $single:ident, $scoreboard:ident, $induce:ident, $name:literal, $words:expr) => {
        #[test]
        fn $run() {
            full_run($name);
        }
        #[test]
        fn $single() {
            single_runs($name, $words);
        }
        #[test]
        fn $scoreboard() {
            scoreboard($name);
        }
        #[test]
        fn $induce() {
            induce($name);
        }
    };
}

project_tests!(default_run, default_single, default_scoreboard, default_induce, "default", ["voicing-assimilation", "contradictory-bundle", "akbaakba"]);
project_tests!(halle_vaux_wolfe_run, halle_vaux_wolfe_single, halle_vaux_wolfe_scoreboard, halle_vaux_wolfe_induce, "halle_vaux_wolfe", ["assim-velar", "irish-velar-dorsal", "ankaanka"]);
project_tests!(spe_run, spe_single, spe_scoreboard, spe_induce, "spe", ["intervocalic-voicing", "metaphony-raising", "ataata"]);

#[test]
fn latin_to_french_run() {
    full_run("latin_to_french");
}

#[test]
fn latin_to_french_single() {
    single_runs("latin_to_french", ["abbé", "œil", "ˌɑbˈbɑːt̪emˌɑbˈbɑːt̪em"]);
}

#[test]
fn latin_to_french_scoreboard() {
    scoreboard("latin_to_french");
}

#[test]
#[ignore = "minutes in a debug build; run with --release -- --ignored"]
fn latin_to_french_induce() {
    induce("latin_to_french");
}

#[test]
fn pie_to_english_run() {
    full_run("pie_to_english");
}

#[test]
fn pie_to_english_single() {
    single_runs("pie_to_english", ["mean", "womb", "ˈkomojnisˈkomojnis"]);
}

#[test]
fn pie_to_english_scoreboard() {
    scoreboard("pie_to_english");
}

#[test]
#[ignore = "minutes in a debug build; run with --release -- --ignored"]
fn pie_to_english_induce() {
    induce("pie_to_english");
}

// The inducer's options. The default project has three attested stages; only the two large
// projects induce rules, so refinement runs on `latin_to_french`, capped at two rules a stage.
#[test]
fn default_induce_ignore_stages() {
    induce_with("default", "induce-ignore-stages", &["--ignore-stages"]);
}

#[test]
fn default_induce_interval() {
    induce_with("default", "induce-interval", &["--interval", "100:200"]);
}

#[test]
fn default_induce_max_rules() {
    induce_with("default", "induce-max-rules", &["--max-rules", "1"]);
}

#[test]
#[ignore = "seconds in a release build, but long in a debug one; run with --release -- --ignored"]
fn latin_to_french_induce_refine() {
    induce_with("latin_to_french", "induce-refine", &["--max-rules", "2", "--refine"]);
}

#[test]
#[ignore = "seconds in a release build, but long in a debug one; run with --release -- --ignored"]
fn latin_to_french_induce_refine_localized() {
    induce_with("latin_to_french", "induce-refine-localized", &["--max-rules", "2", "--refine-localized"]);
}
