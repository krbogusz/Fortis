//! The `fortis` command: load a project, derive every word, and write the reports.

use std::io::{BufRead, Write};
use std::path::{Path, PathBuf};
use std::process::ExitCode;
use std::time::Instant;

use clap::Parser;

use fortis::analysis::dependencies::{build_dependency_graph, render_dependency_html};
use fortis::analysis::diagnostics::unsatisfiable_rules;
use fortis::engine::deriving::Engine;
use fortis::engine::rendering::Renderer;
use fortis::engine::segmentation::string_to_sequence;
use fortis::engine::syllabifying::syllabify;
use fortis::loaders::{default_project_dir, load_project, unfired_scoped_rules};
use fortis::models::*;
use fortis::py;
use fortis::reports;

#[derive(Parser)]
#[command(
    name = "fortis",
    about = "Run a phonological derivation: segment each word, apply the rules in time order, and write the reports."
)]
struct Args {
    /// A project directory; its files override the shipped defaults.
    #[arg(long, value_name = "DIR")]
    project: Option<PathBuf>,
    /// Lexicon file to run (default: the project's words.toml).
    #[arg(long, value_name = "FILE")]
    words: Option<PathBuf>,
    /// Sound-change file to apply (default: the project's rules.toml).
    #[arg(long, value_name = "FILE")]
    rules: Option<PathBuf>,
    /// Path for derivations.csv; the other reports are written alongside it.
    #[arg(long, value_name = "FILE", num_args = 0..=1)]
    output: Option<Option<PathBuf>>,
    /// Derive a single word, looked up by id, seed IPA or gloss, and write single_*.csv.
    #[arg(long, value_name = "WORD")]
    single: Option<String>,
    /// Also write reports/autosegmental.md.
    #[arg(long)]
    autosegmental: bool,
    /// Check the rules for unsatisfiable bundles, then exit.
    #[arg(long)]
    lint: bool,
    /// Segment and syllabify each line of FILE ('-' for standard input) against the project's
    /// inventory, and print one JSON object per line: the segments and the syllable boundaries,
    /// or the reason the form cannot be segmented.
    #[arg(long, value_name = "FILE")]
    segment: Option<PathBuf>,
    /// With --segment: syllabify with the syllable parts in force at time T (default: the
    /// latest).
    #[arg(long, value_name = "T", allow_negative_numbers = true, requires = "segment")]
    time: Option<i64>,
    /// Derive in a single thread.
    #[arg(long)]
    serial: bool,
    /// Pin the worker-thread count.
    #[arg(long, value_name = "N")]
    workers: Option<usize>,
}

fn color() -> bool {
    use std::io::IsTerminal;
    std::io::stderr().is_terminal() && std::env::var_os("NO_COLOR").is_none()
}

fn sgr(text: &str, codes: &str) -> String {
    if color() { format!("\x1b[{codes}m{text}\x1b[0m") } else { text.to_string() }
}

fn label(text: &str) -> String {
    sgr(text, "1;36")
}

fn key(text: &str) -> String {
    sgr(text, "1")
}

fn dim(text: &str) -> String {
    sgr(text, "2")
}

fn write(path: &Path, text: &str, saved: &mut Vec<PathBuf>) {
    std::fs::write(path, text).unwrap_or_else(|e| panic!("could not write '{}': {e}", path.display()));
    saved.push(path.to_path_buf());
}

fn main() -> ExitCode {
    let args = Args::parse();
    if let Some(n) = args.workers.filter(|_| !args.serial) {
        rayon::ThreadPoolBuilder::new().num_threads(n.max(1)).build_global().ok();
    } else if args.serial {
        rayon::ThreadPoolBuilder::new().num_threads(1).build_global().ok();
    }
    let start = Instant::now();
    let project = match load_project(args.project.as_deref(), args.words.as_deref(), args.rules.as_deref()) {
        Ok(p) => p,
        Err(errors) => {
            for e in errors {
                eprintln!("error: {e}");
            }
            return ExitCode::from(1);
        }
    };
    if let Some(file) = &args.segment {
        return run_segment(&project, file, args.time);
    }
    let engine = match Engine::new(&project) {
        Ok(e) => e,
        Err(e) => {
            eprintln!("error: {e}");
            return ExitCode::from(1);
        }
    };
    let init_done = start.elapsed().as_secs_f64();

    if args.lint {
        return run_lint(&project, start);
    }

    let output_dir = args.project.clone().unwrap_or_else(default_project_dir);
    let path = match &args.output {
        Some(Some(p)) => p.clone(),
        _ => output_dir.join("reports").join("derivations.csv"),
    };
    let reports_dir = path.parent().map(Path::to_path_buf).unwrap_or_default();

    if let Some(word) = &args.single {
        return fortis::cli::run_single(&project, &engine, word, &reports_dir, start);
    }

    let mut derivations = match engine.derive_all() {
        Ok(d) => d,
        Err(e) => {
            eprintln!("error: {e}");
            return ExitCode::from(1);
        }
    };
    let derive_done = start.elapsed().as_secs_f64();

    std::fs::create_dir_all(&reports_dir).ok();
    let renderer = Renderer::new(&project);
    let mut saved = Vec::new();
    write(&path, &reports::derivations_csv(&derivations, &renderer), &mut saved);
    write(&reports_dir.join("derivation_matrix.csv"), &reports::matrix_csv(&derivations, &engine.rules, &renderer), &mut saved);
    write(&reports_dir.join("rule_firings.csv"), &reports::rule_firings_csv(&derivations, &engine.rules, &renderer), &mut saved);
    let graph = build_dependency_graph(&derivations, &engine.rules, &renderer);
    write(&reports_dir.join("rule_dependencies.html"), &render_dependency_html(&graph), &mut saved);
    if args.autosegmental {
        let text = fortis::diagram::autosegmental_md(&derivations, &project, &renderer);
        write(&reports_dir.join("autosegmental.md"), &text, &mut saved);
    }
    let write_done = start.elapsed().as_secs_f64();

    let where_ = match &args.project {
        Some(p) => format!("`{}`", p.display()),
        None => "the shipped `projects/default`".to_string(),
    };
    let analysis = fortis::cli::run_analysis(&mut derivations, &project, &renderer, &reports_dir, &where_, &mut saved);
    let accuracy_done = start.elapsed().as_secs_f64();

    print_scoped_warnings(&unfired_scoped_rules(&project.rules, &project.words));

    let done = start.elapsed().as_secs_f64();
    let mut phases = vec![("init", init_done), ("apply", derive_done - init_done)];
    if analysis.has_targets {
        phases.push(("analysis", accuracy_done - write_done));
    }
    phases.push(("write", (write_done - derive_done) + (done - accuracy_done)));
    print_summary(&analysis, &engine.rules, &saved, &phases, done, &reports_dir);
    ExitCode::SUCCESS
}

fn print_scoped_warnings(unfired: &[(String, String)]) {
    if unfired.is_empty() {
        return;
    }
    let mut rules: Vec<&str> = Vec::new();
    for (rule, _) in unfired {
        if !rules.contains(&rule.as_str()) {
            rules.push(rule);
        }
    }
    eprintln!(
        "  {}  {} rule(s) never fire — word-scoped to a word not in the lexicon:",
        sgr("⚠", "33"),
        key(&rules.len().to_string())
    );
    eprintln!("{}", dim(&py::fill(&rules.join(", "), 76, "     ", "     ")));
}

fn print_summary(
    analysis: &fortis::cli::AnalysisSummary,
    rules: &RuleInventory,
    saved: &[PathBuf],
    phases: &[(&str, f64)],
    total: f64,
    reports_dir: &Path,
) {
    let pad = analysis.rows.iter().map(|(l, _, _)| l.len()).max().unwrap_or(0);
    if !analysis.rows.is_empty() {
        eprintln!();
    }
    for (l, headline, subs) in &analysis.rows {
        eprintln!("  {}  {headline}", label(&format!("{l:<pad$}")));
        for sub in subs {
            eprintln!("  {}  {}", " ".repeat(pad), dim(sub));
        }
    }
    if let Some(line) = &analysis.warning_line {
        eprintln!("  {}  {line}", sgr("⚠", "33"));
    }
    let breakdown: Vec<String> = phases.iter().map(|(n, s)| format!("{n} {s:.2}s")).collect();
    eprintln!();
    eprintln!(
        "  {} words · {} rules applied · {}",
        key(&analysis.words.to_string()),
        key(&format!("{}/{}", analysis.applied_rules, reports::rule_columns(rules).len())),
        key(&format!("{total:.2}s"))
    );
    eprintln!("  {}", dim(&breakdown.join(" · ")));
    eprintln!();
    eprintln!("  {} reports {}", key(&saved.len().to_string()), dim(&format!("→ {}", reports_dir.display())));
    let stems: Vec<String> =
        saved.iter().map(|p| p.file_stem().map(|s| s.to_string_lossy().into_owned()).unwrap_or_default()).collect();
    eprintln!("{}", dim(&py::fill(&stems.join(" · "), 76, "  ", "  ")));
}

/// `--segment`: answer one form per line, flushing each answer, so a caller can keep the command
/// open and ask about forms one at a time.
fn run_segment(project: &Project, file: &Path, time: Option<i64>) -> ExitCode {
    let input: Box<dyn BufRead> = if file == Path::new("-") {
        Box::new(std::io::stdin().lock())
    } else {
        match std::fs::File::open(file) {
            Ok(f) => Box::new(std::io::BufReader::new(f)),
            Err(e) => {
                eprintln!("error: could not read '{}': {e}", file.display());
                return ExitCode::from(1);
            }
        }
    };
    let renderer = Renderer::new(project);
    let mut out = std::io::stdout().lock();
    for line in input.lines() {
        let line = match line {
            Ok(l) => l,
            Err(e) => {
                eprintln!("error: could not read '{}': {e}", file.display());
                return ExitCode::from(1);
            }
        };
        let form = line.trim();
        let mut fields = vec![("form".to_string(), py::Json::Str(form.to_string()))];
        match string_to_sequence(form, project) {
            Ok(sequence) => {
                let bundles = sequence.bundles();
                let segments = bundles.iter().map(|b| py::Json::Str(renderer.segment(b, false))).collect();
                let boundaries = syllabify(&bundles, project, time).into_iter().map(|b| py::Json::Int(b as i64)).collect();
                fields.push(("segments".into(), py::Json::List(segments)));
                fields.push(("boundaries".into(), py::Json::List(boundaries)));
            }
            Err(e) => fields.push(("error".into(), py::Json::Str(e))),
        }
        if writeln!(out, "{}", py::Json::Obj(fields).dumps()).and_then(|_| out.flush()).is_err() {
            return ExitCode::from(1); // the reader went away
        }
    }
    ExitCode::SUCCESS
}

fn run_lint(project: &Project, start: Instant) -> ExitCode {
    let findings = unsatisfiable_rules(project);
    eprintln!();
    if findings.is_empty() {
        eprintln!("  {}  {} unsatisfiable rule positions", label(&format!("{:<8}", "Lint")), key("0"));
        eprintln!("  {}  {}", " ".repeat(8), dim("every rule bundle can match at least one segment"));
        eprintln!();
        eprintln!("  {}", key(&format!("{:.2}s", start.elapsed().as_secs_f64())));
        return ExitCode::SUCCESS;
    }
    let plural = if findings.len() == 1 { "" } else { "s" };
    eprintln!(
        "  {}  {} unsatisfiable rule position{plural} — a bundle that can never match a segment:",
        sgr("⚠", "33"),
        key(&findings.len().to_string())
    );
    for f in &findings {
        let head = match f.time {
            Some(t) => format!("{} @{t}", f.rule),
            None => f.rule.clone(),
        };
        eprintln!("     {} · {}  {}", label(&head), f.role, key(&f.label));
        eprintln!("        {}", dim(&f.reason));
    }
    eprintln!();
    eprintln!("  {}", key(&format!("{:.2}s", start.elapsed().as_secs_f64())));
    ExitCode::from(1)
}
