//! `fortis-scoreboard`: the MDL loss of the identity and hand cascades, real and synthetic.

use std::path::PathBuf;
use std::process::ExitCode;

use clap::Parser;

use fortis::induction::compute_scoreboard;
use fortis::induction::report::{render_scoreboard, scoreboard_summary_line};
use fortis::loaders::{default_project_dir, load_project};

#[derive(Parser)]
#[command(name = "fortis-scoreboard", about = "Report L of the identity vs hand cascade, on real and synthetic data.")]
struct Args {
    /// A project directory.
    #[arg(long, value_name = "DIR")]
    project: Option<PathBuf>,
    /// Path for the report (default: <project>/induction_scoreboard.md).
    #[arg(long, value_name = "FILE")]
    output: Option<PathBuf>,
    /// Derive in a single thread.
    #[arg(long)]
    serial: bool,
    /// Worker-thread count.
    #[arg(long, value_name = "N")]
    workers: Option<usize>,
}

fn main() -> ExitCode {
    let args = Args::parse();
    let threads = if args.serial { Some(1) } else { args.workers };
    if let Some(n) = threads {
        rayon::ThreadPoolBuilder::new().num_threads(n.max(1)).build_global().ok();
    }
    let project = match load_project(args.project.as_deref(), None, None) {
        Ok(p) => p,
        Err(errors) => {
            for e in errors {
                eprintln!("error: {e}");
            }
            return ExitCode::from(1);
        }
    };
    let board = compute_scoreboard(&project);
    let where_ = match &args.project {
        Some(p) => format!("`{}`", p.display()),
        None => "the shipped `projects/default`".to_string(),
    };
    let output_dir = args.project.clone().unwrap_or_else(default_project_dir);
    let path = args.output.clone().unwrap_or_else(|| output_dir.join("induction_scoreboard.md"));
    std::fs::write(&path, render_scoreboard(&board, &where_)).expect("write the scoreboard");
    eprintln!("wrote {}", path.display());
    println!("{}", scoreboard_summary_line(&board));
    ExitCode::SUCCESS
}
