//! The accuracy headline and its two CSV reports.

use super::accuracy::StageAccuracy;
use crate::py::{Cell, CsvWriter, fixed, percent};

pub fn accuracy_summary_line(stages: &[StageAccuracy]) -> String {
    let Some(final_stage) = stages.iter().find(|s| s.time.is_none()) else {
        return "no final target to measure against".into();
    };
    let r = &final_stage.report;
    if r.assessed() == 0 {
        return "no final target to measure against".into();
    }
    let intermediate: Vec<&str> = stages.iter().filter(|s| s.time.is_some()).map(|s| s.label.as_str()).collect();
    let stage_note = if intermediate.is_empty() {
        String::new()
    } else {
        format!(" · stages {} measured too", intermediate.join(", "))
    };
    let weighted = if r.frequencies_vary() {
        format!(", token-weighted {}", percent(r.weighted_accuracy(), 1))
    } else {
        String::new()
    };
    format!(
        "final: {}/{} exact ({}){weighted}, mean phone {}, mean feature {}{stage_note}",
        r.exact(),
        r.assessed(),
        percent(r.accuracy(), 1),
        fixed(r.mean_distance(), 3),
        fixed(r.mean_feature_distance(), 3)
    )
}

pub fn render_accuracy_csv(stages: &[StageAccuracy]) -> String {
    let weighted = stages.iter().find(|s| s.time.is_none()).is_some_and(|s| s.report.frequencies_vary());
    let mut header = vec!["stage", "assessed", "exact", "within 1", "mean phone dist", "mean feature dist"];
    if weighted {
        header.extend(["token-wt exact", "token-wt phone dist", "token-wt feature dist"]);
    }
    let mut w = CsvWriter::new();
    w.row(header);
    for stage in stages {
        let r = &stage.report;
        let mut row: Vec<Cell> = vec![
            Cell::from(&stage.label),
            Cell::from(r.assessed()),
            Cell::from(r.exact()),
            Cell::from(r.within_one()),
            Cell::from(fixed(r.mean_distance(), 3)),
            Cell::from(fixed(r.mean_feature_distance(), 3)),
        ];
        if weighted {
            row.push(Cell::from(fixed(r.weighted_accuracy(), 3)));
            row.push(Cell::from(fixed(r.weighted_mean_distance(), 3)));
            row.push(Cell::from(fixed(r.weighted_mean_feature_distance(), 3)));
        }
        w.row(row);
    }
    w.out
}

pub fn render_distance_to_target_csv(stages: &[StageAccuracy]) -> String {
    let mut w = CsvWriter::new();
    w.row(["stage", "gloss", "derived", "target", "d", "fd", "matches at", "closest at"]);
    for stage in stages {
        for g in &stage.report.distances {
            let gloss = if g.gloss.is_empty() { &g.ipa } else { &g.gloss };
            w.row([
                Cell::from(&stage.label),
                Cell::from(gloss),
                Cell::from(&g.derived),
                Cell::from(&g.target),
                Cell::from(g.distance),
                g.feature_distance.map_or(Cell::from(""), Cell::from),
                Cell::from(&g.matches_at),
                Cell::from(&g.closest_at),
            ]);
        }
    }
    w.out
}
