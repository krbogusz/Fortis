//! Composition of the per-interval cascades into one real-time cascade, and Phase-B refinement.

use std::sync::Arc;

use super::boost::{InducedInterval, induce_interval};
use super::intervals::{Interval, build_interval, build_intervals, mini_project, series_word, stage_times};
use super::objective::{CascadeScore, cascade_score};
use crate::analysis::accuracy::ingest_word;
use crate::engine::deriving::Engine;
use crate::engine::rendering::Renderer;
use crate::engine::segmentation::string_to_sequence;
use crate::engine::tiers::lower_tiers;
use crate::models::*;

const OPEN_SPAN: i64 = 1000;

fn spaced_times(lo: i64, hi: i64, count: usize) -> Vec<i64> {
    let step = (hi - lo) as f64 / (count + 1) as f64;
    (0..count).map(|i| (lo as f64 + step * (i + 1) as f64).round_ties_even() as i64).collect()
}

fn safe_label(label: &str) -> String {
    let mut out = String::new();
    let mut in_run = false;
    for c in label.chars() {
        if c.is_ascii_alphanumeric() || c == '-' {
            out.push(c);
            in_run = false;
        } else if !in_run {
            out.push('_');
            in_run = true;
        }
    }
    out
}

pub fn ingest_interval(interval: &mut Interval) {
    let project = interval.project.clone();
    for word in interval.project.words.values_mut() {
        ingest_word(word, &project);
    }
}

pub struct InductionResult {
    pub intervals: Vec<InducedInterval>,
    pub inventory: RuleInventory,
}

pub fn induce_project(project: &Project, ignore_stages: bool, only: Option<(Option<i64>, Option<i64>)>) -> InductionResult {
    let mut intervals = match only {
        Some((a, b)) => vec![build_interval(project, a, b)],
        None if ignore_stages || stage_times(project).is_empty() => vec![build_interval(project, None, None)],
        None => build_intervals(project),
    };
    let mut induced = Vec::new();
    for interval in &mut intervals {
        ingest_interval(interval);
        induced.push(induce_interval(interval));
    }
    let inventory = compose(&induced, project);
    InductionResult { intervals: induced, inventory }
}

pub fn compose(intervals: &[InducedInterval], project: &Project) -> RuleInventory {
    let times_all = stage_times(project);
    let mut composed: std::collections::BTreeMap<i64, Vec<Arc<Rule>>> = std::collections::BTreeMap::new();
    for interval in intervals {
        if interval.rules.is_empty() {
            continue;
        }
        let (lo, hi) = if times_all.is_empty() {
            (0, interval.rules.len() as i64 + 1)
        } else {
            let (s, e) = interval.label.split_once('→').unwrap();
            let lo = if s == "input" { times_all[0] - OPEN_SPAN } else { s.parse().unwrap() };
            let hi = if e == "final" { times_all[times_all.len() - 1] + OPEN_SPAN } else { e.parse().unwrap() };
            (lo, hi)
        };
        let times = spaced_times(lo, hi, interval.rules.len());
        let safe = safe_label(&interval.label);
        for (n, (rule, time)) in interval.rules.iter().zip(times).enumerate() {
            let number = n + 1;
            let placed = Rule {
                id: format!("ind_{safe}_{number}"),
                time: Some(time),
                name: Some(format!("{} (induced)", rule.raw_definition)),
                description: Some(format!("induced in interval {}, step {number}", interval.label)),
                ..rule.clone()
            };
            composed.entry(time).or_default().push(Arc::new(placed));
        }
    }
    let mut inv = RuleInventory::default();
    for (time, rules) in composed {
        inv.by_time.insert(Some(time), rules);
    }
    inv
}

// ---- Phase B ----------------------------------------------------------------------------------

pub struct RefineTrace {
    pub removed: Vec<String>,
    pub added: Vec<String>,
    pub start_score: CascadeScore,
    pub final_score: CascadeScore,
}

fn flat(inv: &RuleInventory) -> Vec<Rule> {
    inv.in_order().into_iter().map(|r| (*r).clone()).collect()
}

fn inventory(rules: &[Rule]) -> RuleInventory {
    let mut inv = RuleInventory::default();
    for rule in rules {
        inv.by_time.entry(rule.time).or_default().push(Arc::new(rule.clone()));
    }
    inv
}

fn runnable(project: &Project, inv: RuleInventory) -> Project {
    Project { rules: inv, ..project.clone() }
}

fn derive(project: &Project) -> Vec<Derivation> {
    Engine::new(project).expect("rules resolve").derive_all().expect("words segment")
}

/// The whole-lexicon loss of a cascade.
fn score(project: &Project, inv: &RuleInventory) -> CascadeScore {
    let p = runnable(project, inv.clone());
    let mut derivations = derive(&p);
    cascade_score(&mut derivations, &p, &Renderer::new(&p))
}

fn global_shrink(project: &Project, rules: Vec<Rule>) -> (Vec<Rule>, Vec<String>) {
    let base = score(project, &inventory(&rules)).total();
    let deltas: Vec<f64> = (0..rules.len())
        .map(|i| {
            let mut trial = rules.clone();
            trial.remove(i);
            base - score(project, &inventory(&trial)).total()
        })
        .collect();
    let helpful: Vec<usize> = (0..rules.len()).filter(|&i| deltas[i] > 1e-6).collect();
    if helpful.is_empty() {
        return (rules, Vec::new());
    }
    let kept: Vec<Rule> = rules.iter().enumerate().filter(|(i, _)| !helpful.contains(i)).map(|(_, r)| r.clone()).collect();
    if !kept.is_empty() && score(project, &inventory(&kept)).total() < base - 1e-6 {
        let log = helpful.iter().map(|&i| format!("removed `{}`", rules[i].raw_definition)).collect();
        return (kept, log);
    }
    let mut best = helpful[0];
    for &i in &helpful {
        if deltas[i] > deltas[best] {
            best = i;
        }
    }
    let log = vec![format!(
        "removed `{}` (L {} → {})",
        rules[best].raw_definition,
        crate::py::fixed(base, 0),
        crate::py::fixed(base - deltas[best], 0)
    )];
    let mut rules = rules;
    rules.remove(best);
    (rules, log)
}

fn residual_interval(project: &Project, inv: &RuleInventory, start: Option<i64>, end: Option<i64>, localized: bool) -> Interval {
    let p = runnable(project, inv.clone());
    let derivations = derive(&p);
    let r = Renderer::new(project);
    let mut words = WordInventory::new();
    for d in &derivations {
        let target = match end {
            None => d.word.final_ipa(),
            Some(t) => d.word.stage_ipa(t),
        };
        let Some(target) = target else { continue };
        let (form, boundaries) = match end {
            None => (d.surface.clone(), d.surface_boundaries.clone()),
            Some(t) => Engine::form_at_time(d, t),
        };
        let source = r.syllabified(&lower_tiers(&form), &boundaries, true);
        if words.contains_key(&source) {
            continue;
        }
        if localized && string_to_sequence(&source, project).is_err() {
            continue;
        }
        words.insert(source.clone(), series_word(&source, &d.word.gloss, target, d.word.frequency));
    }
    let mut interval = Interval { start, end, project: mini_project(project, words) };
    ingest_interval(&mut interval);
    interval
}

pub fn refine(project: &Project, inv: &RuleInventory) -> (RuleInventory, RefineTrace) {
    let start = score(project, inv);
    let mut rules = flat(inv);
    let (mut removed, mut added) = (Vec::new(), Vec::new());
    for _ in 0..2 {
        let (kept, log) = global_shrink(project, rules);
        rules = kept;
        let shrank = !log.is_empty();
        removed.extend(log);
        let residual = residual_interval(project, &inventory(&rules), None, None, false);
        let induced = induce_interval(&residual);
        if induced.rules.is_empty() {
            if !shrank {
                break;
            }
            continue;
        }
        let latest = rules.iter().filter_map(|r| r.time).max().unwrap_or(0);
        for (offset, rule) in induced.rules.iter().enumerate() {
            let offset = offset + 1;
            rules.push(Rule {
                id: format!("ind_refine_{}", added.len() + offset),
                time: Some(latest + offset as i64),
                name: Some(format!("{} (refined)", rule.raw_definition)),
                description: Some("Phase-B final-residual correction".into()),
                ..rule.clone()
            });
            added.push(rule.raw_definition.clone());
        }
    }
    let final_inv = inventory(&rules);
    let final_score = score(project, &final_inv);
    (final_inv, RefineTrace { removed, added, start_score: start, final_score })
}

pub fn refine_localized(project: &Project, inv: &RuleInventory) -> (RuleInventory, RefineTrace) {
    let start = score(project, inv);
    let mut rules = flat(inv);
    let mut added: Vec<String> = Vec::new();
    let times = stage_times(project);
    let mut checkpoints: Vec<Option<i64>> = vec![None];
    checkpoints.extend(times.iter().copied().map(Some));
    checkpoints.push(None);
    for _ in 0..2 {
        let mut changed = false;
        for w in checkpoints.windows(2) {
            let (s, e) = (w[0], w[1]);
            let interval = residual_interval(project, &inventory(&rules), s, e, true);
            if interval.project.words.is_empty() {
                continue;
            }
            let induced = induce_interval(&interval);
            if induced.rules.is_empty() {
                continue;
            }
            changed = true;
            let lo = s.unwrap_or_else(|| times[0] - OPEN_SPAN);
            let hi = e.unwrap_or_else(|| times[times.len() - 1] + OPEN_SPAN);
            let after = rules.iter().filter_map(|r| r.time).filter(|t| lo < *t && *t < hi).max().unwrap_or(lo);
            let new_times = spaced_times(after, hi, induced.rules.len());
            for (offset, (rule, time)) in induced.rules.iter().zip(new_times).enumerate() {
                let offset = offset + 1;
                let label = |t: Option<i64>| t.map_or("None".to_string(), |t| t.to_string());
                rules.push(Rule {
                    id: format!("ind_loc_{}", added.len() + offset),
                    time: Some(time),
                    name: Some(format!("{} (localized)", rule.raw_definition)),
                    description: Some(format!("Phase-B localized refinement of interval {}→{}", label(s), label(e))),
                    ..rule.clone()
                });
                added.push(rule.raw_definition.clone());
            }
            rules.sort_by_key(|r| time_order(r.time));
        }
        if !changed {
            break;
        }
    }
    let final_inv = inventory(&rules);
    let final_score = score(project, &final_inv);
    (final_inv, RefineTrace { removed: Vec::new(), added, start_score: start, final_score })
}
