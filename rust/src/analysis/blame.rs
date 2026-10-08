//! Attribute each wrong word to the rule that broke it, and trace its distance trajectory.

use std::sync::Arc;

use indexmap::IndexMap;
use rayon::prelude::*;

use super::accuracy::{OpKind, align, comparable_bundles, edit_distance, feature_edit_distance, form_phones, phone_keys};
use crate::engine::rendering::Renderer;
use crate::engine::tiers::lower_tiers;
use crate::models::*;
use crate::py::{Cell, CsvWriter};

pub struct TrajectoryPoint {
    pub label: String,
    pub time: Option<i64>,
    pub form: String,
    pub target: String,
    pub distance: i64,
    pub feature_distance: i64,
    pub regressed: bool,
}

pub struct Blame {
    pub gloss: String,
    pub ipa: String,
    pub distance: i64,
    /// The rule id behind each wrong surface phone that a rule produced.
    pub culprits: Vec<String>,
    pub trajectory: Vec<TrajectoryPoint>,
}

/// The last firing rule that changed or introduced segment *id*.
fn culprit_for_id(d: &Derivation, id: u32) -> Option<String> {
    let mut culprit = None;
    for step in &d.steps {
        let Some(after) = step.after.segments.iter().find(|s| s.id == id) else { continue };
        match step.before.segments.iter().find(|s| s.id == id) {
            Some(before) if before.bundle == after.bundle => {}
            _ => culprit = Some(step.rule.id.clone()),
        }
    }
    culprit
}

fn culprits(d: &Derivation, target: &Form, r: &Renderer) -> Vec<String> {
    let mut phones = Vec::new();
    let mut ids = Vec::new();
    for (bundle, segment) in lower_tiers(&d.surface).iter().zip(&d.surface.segments) {
        if is_morpheme_boundary(bundle) {
            continue;
        }
        phones.push(r.segment(bundle, false));
        ids.push(segment.id);
    }
    let mut out = Vec::new();
    for op in align(&form_phones(target, r), &phones) {
        if op.kind == OpKind::Match {
            continue;
        }
        if let Some(i) = op.derived_index.filter(|i| *i < ids.len())
            && let Some(c) = culprit_for_id(d, ids[i]) {
                out.push(c);
            }
    }
    out
}

fn trajectory(d: &Derivation, project: &Project, r: &Renderer) -> Vec<TrajectoryPoint> {
    let swap = project.settings.accuracy.transposition_cost;
    let word = &d.word;
    let final_form = word.final_form().unwrap();
    let final_ipa = word.final_ipa().unwrap_or_default().to_string();
    let mut stage_times: Vec<i64> = word.stages().into_iter().map(|(t, _)| t).collect();
    stage_times.sort_unstable();
    let target_for = |t: i64| -> (String, &Form) {
        (word.stage_ipa(t).unwrap_or_default().to_string(), word.stage_form(t).unwrap_or(final_form))
    };
    let target_at = |time: Option<i64>| -> (String, &Form) {
        if let Some(time) = time
            && let Some(&t) = stage_times.iter().find(|&&t| t >= time) {
                return target_for(t);
            }
        (final_ipa.clone(), final_form)
    };
    let input_boundaries = d.steps.first().map_or(&d.surface_boundaries, |s| &s.before_boundaries);
    let input_target = match stage_times.first() {
        Some(&t) => target_for(t),
        None => (final_ipa.clone(), final_form),
    };
    let mut rows: Vec<(String, Option<i64>, &Arc<Form>, &Boundaries, (String, &Form))> =
        vec![("input".into(), None, &d.input, input_boundaries, input_target)];
    for step in &d.steps {
        let label = step.rule.name.clone().unwrap_or_else(|| step.rule.id.clone());
        rows.push((label, step.rule.time, &step.after, &step.after_boundaries, target_at(step.rule.time)));
    }
    rows.push(("surface".into(), None, &d.surface, &d.surface_boundaries, (final_ipa.clone(), final_form)));
    let mut out = Vec::new();
    let mut previous: Option<(i64, String)> = None;
    for (label, time, form, boundaries, (target_str, target_form)) in rows {
        let distance = edit_distance(&phone_keys(form), &phone_keys(target_form), swap);
        let feature_distance = feature_edit_distance(&comparable_bundles(form), &comparable_bundles(target_form), swap);
        let regressed = previous.as_ref().is_some_and(|(pd, pt)| *pt == target_str && distance > *pd);
        out.push(TrajectoryPoint {
            label,
            time,
            form: r.syllabified(&lower_tiers(form), boundaries, true),
            target: target_str.clone(),
            distance,
            feature_distance,
            regressed,
        });
        previous = Some((distance, target_str));
    }
    out
}

/// Every assessed word's blame (exact ones included), worst first.
pub fn blame_all(derivations: &[Derivation], project: &Project, r: &Renderer) -> Vec<Blame> {
    let swap = project.settings.accuracy.transposition_cost;
    let mut blames: Vec<Blame> = derivations
        .par_iter()
        .filter_map(|d| {
            let word = &d.word;
            let final_form = word.final_form()?;
            let distance = edit_distance(&phone_keys(final_form), &phone_keys(&d.surface), swap);
            Some(Blame {
                gloss: word.gloss.clone(),
                ipa: word.ipa().to_string(),
                distance,
                culprits: culprits(d, final_form, r),
                trajectory: trajectory(d, project, r),
            })
        })
        .collect();
    blames.sort_by_cached_key(|b| (-b.distance, crate::py::casefold(&b.gloss)));
    blames
}

pub fn blame_summary_line(blames: &[Blame]) -> String {
    let wrong: Vec<&Blame> = blames.iter().filter(|b| b.distance > 0).collect();
    if wrong.is_empty() {
        return "no wrong words to blame — every assessed word is exact".into();
    }
    let mut counts: IndexMap<&str, usize> = IndexMap::new();
    for b in &wrong {
        for c in &b.culprits {
            *counts.entry(c).or_insert(0) += 1;
        }
    }
    let mut worst: Option<(&str, usize)> = None;
    for (rule, count) in &counts {
        if worst.is_none_or(|(_, c)| *count > c) {
            worst = Some((rule, *count));
        }
    }
    match worst {
        None => format!("{} wrong word(s); no rule-level culprit found — see blame.csv", wrong.len()),
        Some((rule, count)) => {
            format!("{} wrong word(s); rule '{rule}' is behind {count} wrong phone(s) — see blame.csv", wrong.len())
        }
    }
}

pub fn render_blame_csv(blames: &[Blame]) -> String {
    let mut w = CsvWriter::new();
    w.row(["gloss", "step", "regression", "t", "form", "target", "d", "fd"]);
    for b in blames {
        let gloss = if b.gloss.is_empty() { &b.ipa } else { &b.gloss };
        for p in &b.trajectory {
            w.row([
                Cell::from(gloss),
                Cell::from(&p.label),
                Cell::from(if p.regressed { "true" } else { "" }),
                p.time.map_or(Cell::from(""), Cell::from),
                Cell::from(&p.form),
                Cell::from(&p.target),
                Cell::from(p.distance),
                Cell::from(p.feature_distance),
            ]);
        }
    }
    w.out
}
