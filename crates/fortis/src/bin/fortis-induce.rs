//! `fortis-induce`: induce a sound-change cascade from a project's attested targets.

use std::path::PathBuf;
use std::process::ExitCode;
use std::time::Instant;

use clap::Parser;

use fortis::analysis::accuracy::{ingest_targets, measure_accuracy};
use fortis::engine::deriving::Engine;
use fortis::engine::rendering::Renderer;
use fortis::induction::refine::{induce_project, refine, refine_localized};
use fortis::induction::report::{induction_summary_line, render_induced_rules, render_induction};
use fortis::loaders::{default_project_dir, load_project};
use fortis::models::*;

#[derive(Parser)]
#[command(name = "fortis-induce", about = "Induce a sound-change cascade from a project's attested targets.")]
struct Args {
    /// A project directory.
    #[arg(long, value_name = "DIR")]
    project: Option<PathBuf>,
    /// Path for the induced rules (default: <project>/induced_rules.toml).
    #[arg(long, value_name = "FILE")]
    out: Option<PathBuf>,
    /// Path for the trace report (default: <project>/induction.md).
    #[arg(long, value_name = "FILE")]
    report: Option<PathBuf>,
    /// Induce a single input→final interval, ignoring intermediate stages.
    #[arg(long)]
    ignore_stages: bool,
    /// Induce only this interval (T1/T2 may be 'input'/'final' or a stage time).
    #[arg(long, value_name = "T1:T2")]
    interval: Option<String>,
    /// Override max_rules_per_interval.
    #[arg(long, value_name = "N")]
    max_rules: Option<i64>,
    /// Run Phase-B global refinement.
    #[arg(long)]
    refine: bool,
    /// Run Phase-B localized refinement.
    #[arg(long)]
    refine_localized: bool,
    /// Derive in a single thread.
    #[arg(long)]
    serial: bool,
    /// Worker-thread count.
    #[arg(long, value_name = "N")]
    workers: Option<usize>,
}

fn endpoint(token: &str) -> Option<i64> {
    match token {
        "input" | "final" | "" => None,
        t => Some(t.parse().expect("an interval endpoint is input, final or a stage time")),
    }
}

fn main() -> ExitCode {
    let args = Args::parse();
    let threads = if args.serial { Some(1) } else { args.workers };
    if let Some(n) = threads {
        rayon::ThreadPoolBuilder::new().num_threads(n.max(1)).build_global().ok();
    }
    let mut project = match load_project(args.project.as_deref(), None, None) {
        Ok(p) => p,
        Err(errors) => {
            for e in errors {
                eprintln!("error: {e}");
            }
            return ExitCode::from(1);
        }
    };
    if let Some(n) = args.max_rules {
        project.settings.induction.max_rules_per_interval = n;
    }
    let where_ = match &args.project {
        Some(p) => format!("`{}`", p.display()),
        None => "the shipped `projects/default`".to_string(),
    };
    let only = args.interval.as_deref().map(|spec| {
        let (a, b) = spec.split_once(':').unwrap_or((spec, ""));
        (endpoint(a), endpoint(b))
    });
    let start = Instant::now();
    let induction = induce_project(&project, args.ignore_stages, only);
    let mut inventory = induction.inventory.clone();
    let mut trace = None;
    if args.refine_localized {
        let (inv, t) = refine_localized(&project, &inventory);
        eprintln!("Phase B (localized): added {} rule(s)", t.added.len());
        inventory = inv;
        trace = Some(t);
    } else if args.refine {
        let (inv, t) = refine(&project, &inventory);
        eprintln!("Phase B: removed {}, added {} rule(s)", t.removed.len(), t.added.len());
        inventory = inv;
        trace = Some(t);
    }
    let elapsed = start.elapsed().as_secs_f64();
    let output_dir = args.project.clone().unwrap_or_else(default_project_dir);
    let out_path = args.out.clone().unwrap_or_else(|| output_dir.join("induced_rules.toml"));
    std::fs::write(&out_path, render_induced_rules(&inventory)).expect("write the induced rules");
    let report_path = args.report.clone().unwrap_or_else(|| output_dir.join("induction.md"));
    std::fs::write(&report_path, render_induction(&induction.intervals, &where_, trace.as_ref()))
        .expect("write the induction report");
    eprintln!("wrote {}", out_path.display());
    eprintln!("wrote {}", report_path.display());
    println!("{}", induction_summary_line(&induction.intervals));

    let runnable = Project { rules: inventory.clone(), ..project.clone() };
    let engine = Engine::new(&runnable).expect("induced rules resolve");
    let mut derivations = engine.derive_all().expect("words segment");
    ingest_targets(&mut derivations, &runnable);
    let report = measure_accuracy(&derivations, &runnable, &Renderer::new(&runnable));
    let rules: usize = inventory.by_time.values().map(Vec::len).sum();
    eprintln!(
        "composed cascade: {}/{} exact (mean phone dist {}) with {rules} induced rules · induced in {}s",
        report.exact(),
        report.assessed(),
        fortis::py::fixed(report.mean_distance(), 3),
        fortis::py::fixed(elapsed, 0)
    );
    ExitCode::SUCCESS
}
