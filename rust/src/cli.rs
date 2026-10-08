//! The analysis phase of a run, and the single-word mode.

use std::path::{Path, PathBuf};
use std::process::ExitCode;
use std::time::Instant;

use crate::analysis::accuracy::{accuracy_by_stage, ingest_targets};
use crate::analysis::blame::{blame_all, blame_summary_line, render_blame_csv};
use crate::analysis::dependencies::base_id;
use crate::analysis::diagnosis::*;
use crate::analysis::reporting::*;
use crate::analysis::warnings::*;
use crate::engine::deriving::Engine;
use crate::engine::rendering::Renderer;
use crate::engine::segmentation::string_to_sequence;
use crate::engine::tiers::lower_tiers;
use crate::models::*;

/// What the analysis phase hands to the run summary.
pub struct AnalysisSummary {
    pub has_targets: bool,
    pub words: usize,
    pub applied_rules: usize,
    /// `(label, headline, sub-lines)` rows: Accuracy, Errors, Blame.
    pub rows: Vec<(String, String, Vec<String>)>,
    pub warning_line: Option<String>,
}

fn write(path: PathBuf, text: &str, saved: &mut Vec<PathBuf>) {
    std::fs::write(&path, text).unwrap_or_else(|e| panic!("could not write '{}': {e}", path.display()));
    saved.push(path);
}

fn has_target(word: &Word) -> bool {
    word.final_ipa().is_some() || !word.stages().is_empty()
}

/// Accuracy, errors, blame and warnings for a full run, written next to the core reports.
pub fn run_analysis(
    derivations: &mut [Derivation],
    project: &Project,
    r: &Renderer,
    reports_dir: &Path,
    where_: &str,
    saved: &mut Vec<PathBuf>,
) -> AnalysisSummary {
    let has_targets = project.words.values().any(has_target);
    let mut rows = Vec::new();
    if has_targets {
        ingest_targets(derivations, project);
        let stages = accuracy_by_stage(derivations, project, r);
        write(reports_dir.join("accuracy.csv"), &render_accuracy_csv(&stages), saved);
        write(reports_dir.join("distance_to_target.csv"), &render_distance_to_target_csv(&stages), saved);
        let acc = accuracy_summary_line(&stages);
        let acc = acc.strip_prefix("final: ").unwrap_or(&acc);
        let (head, tail) = acc.split_once(" · stages ").unwrap_or((acc, ""));
        let subs = if tail.is_empty() { Vec::new() } else { vec![format!("also at stages {tail}")] };
        rows.push(("Accuracy".to_string(), head.to_string(), subs));

        let diagnosis = diagnose_stages(&stages, project);
        write(reports_dir.join("errors.csv"), &render_errors_csv(&diagnosis), saved);
        write(reports_dir.join("error_context.csv"), &render_error_context_csv(&diagnosis), saved);
        let mut subs = Vec::new();
        let omitted = error_context_omissions(&diagnosis);
        if !omitted.is_empty() {
            let shown: Vec<String> = omitted.iter().take(10).map(|(l, s)| format!("{s} @ {l}")).collect();
            let more = if omitted.len() > 10 { format!(", +{} more", omitted.len() - 10) } else { String::new() };
            subs.push(format!(
                "{} segment(s) too sparse to autopsy — omitted from error_context.csv: {}{more}",
                omitted.len(),
                shown.join(", ")
            ));
        }
        let line = errors_summary_line(&diagnosis);
        let line = line.strip_prefix("final: ").unwrap_or(&line);
        rows.push(("Errors".into(), line.split(" — see").next().unwrap().to_string(), subs));

        let blames = blame_all(derivations, project, r);
        write(reports_dir.join("blame.csv"), &render_blame_csv(&blames), saved);
        rows.push(("Blame".into(), blame_summary_line(&blames).split(" — see").next().unwrap().to_string(), Vec::new()));
    }

    let syllab = syllabification_warnings(derivations, project, r);
    let rendering = rendering_warnings(derivations, project, r);
    let warn_path = reports_dir.join("warnings.md");
    let mut warning_line = None;
    if !syllab.is_empty() || !rendering.is_empty() {
        write(warn_path, &render_warnings(&syllab, where_, &rendering), saved);
        warning_line = Some(warnings_summary_line(&syllab, &rendering));
    } else if warn_path.exists() {
        std::fs::remove_file(&warn_path).ok();
    }

    let mut fired = std::collections::HashSet::new();
    for d in derivations.iter() {
        for s in &d.steps {
            fired.insert(base_id(&s.rule.id).to_string());
        }
    }
    AnalysisSummary { has_targets, words: derivations.len(), applied_rules: fired.len(), rows, warning_line }
}

/// Derive one word (found by id, seed IPA or gloss, else derived bare) and write `single_*.csv`.
pub fn run_single(project: &Project, engine: &Engine, word_str: &str, reports_dir: &Path, start: Instant) -> ExitCode {
    let found = project.words.values().find(|w| [w.id.as_str(), w.ipa(), w.gloss.as_str()].contains(&word_str));
    let word = match found {
        Some(w) => w.clone(),
        None => Word {
            id: word_str.to_string(),
            forms: vec![(Some(0), Attestation { ipa: word_str.to_string(), ..Default::default() })],
            frequency: 1,
            ..Default::default()
        },
    };
    let form = match string_to_sequence(word.ipa(), project) {
        Ok(f) => f,
        Err(e) => {
            eprintln!("error: {e}");
            return ExitCode::from(1);
        }
    };
    let mut derivations = vec![engine.derive(&word, form)];
    std::fs::create_dir_all(reports_dir).ok();
    let r = Renderer::new(project);
    let mut saved = Vec::new();
    write(reports_dir.join("single_derivations.csv"), &crate::reports::derivations_csv(&derivations, &r), &mut saved);
    let names = ["single_accuracy.csv", "single_distance_to_target.csv", "single_errors.csv", "single_error_context.csv", "single_blame.csv"];
    let mut acc_line = None;
    if has_target(&word) {
        ingest_targets(&mut derivations, project);
        let stages = accuracy_by_stage(&derivations, project, &r);
        write(reports_dir.join(names[0]), &render_accuracy_csv(&stages), &mut saved);
        write(reports_dir.join(names[1]), &render_distance_to_target_csv(&stages), &mut saved);
        let diagnosis = diagnose_stages(&stages, project);
        write(reports_dir.join(names[2]), &render_errors_csv(&diagnosis), &mut saved);
        write(reports_dir.join(names[3]), &render_error_context_csv(&diagnosis), &mut saved);
        let blames = blame_all(&derivations, project, &r);
        write(reports_dir.join(names[4]), &render_blame_csv(&blames), &mut saved);
        let line = accuracy_summary_line(&stages);
        acc_line = Some(line.strip_prefix("final: ").unwrap_or(&line).to_string());
    } else {
        for name in names {
            let path = reports_dir.join(name);
            if path.exists() {
                std::fs::remove_file(path).ok();
            }
        }
    }
    let d = &derivations[0];
    let surface = r.syllabified(&lower_tiers(&d.surface), &d.surface_boundaries, true);
    let gloss = if word.gloss.is_empty() { String::new() } else { format!(" ‘{}’", word.gloss) };
    eprintln!();
    eprintln!("  {:<8}  {}{gloss}  →  {surface}", "Single", word.ipa());
    let tag = if found.is_some() { "in the lexicon" } else { "not in the lexicon — derived without a target" };
    eprintln!("  {}  {tag}", " ".repeat(8));
    if let Some(line) = acc_line {
        eprintln!("  Accuracy  {line}");
    }
    eprintln!();
    eprintln!("  {:.2}s", start.elapsed().as_secs_f64());
    eprintln!();
    eprintln!("  {} reports → {}", saved.len(), reports_dir.display());
    let stems: Vec<String> =
        saved.iter().map(|p| p.file_stem().map(|s| s.to_string_lossy().into_owned()).unwrap_or_default()).collect();
    eprintln!("{}", crate::py::fill(&stems.join(" · "), 76, "  ", "  "));
    ExitCode::SUCCESS
}
