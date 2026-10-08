//! The greedy MDL boosting loop for one interval, with the escape ladder, the placement search,
//! and the shrink pass.

use std::collections::HashSet;

use rayon::prelude::*;

use super::candidates::{Candidate, class_candidates, propose};
use super::correspond::correspondences;
use super::evaluate::{AppendScore, IntervalState};
use super::intervals::Interval;
use super::objective::{BitsModel, bits_model, rule_bits};
use crate::models::*;
use crate::py::fsum;

const EPSILON: f64 = 1e-6;

pub struct InductionStep {
    pub definition: String,
    pub delta_l: f64,
    pub delta_fit: f64,
    pub rule_cost: f64,
    pub moved: usize,
    pub exact_before: usize,
    pub exact_after: usize,
    pub placement: usize,
}

pub struct InducedInterval {
    pub label: String,
    pub rules: Vec<Rule>,
    pub steps: Vec<InductionStep>,
    pub stopped: &'static str,
    pub start_fit: f64,
    pub final_fit: f64,
    pub start_exact: usize,
    pub final_exact: usize,
    pub assessed: usize,
    pub shrink_log: Vec<String>,
}

fn gather(state: &IntervalState, project: &Project, cap: usize) -> Vec<Candidate> {
    let distances: Vec<&crate::analysis::accuracy::DistanceToTarget> = state.baseline_distances.iter().flatten().collect();
    let corrs = correspondences(&distances, project, cap);
    let mut out = Vec::new();
    let mut seen = HashSet::new();
    for c in &corrs {
        for candidate in propose(c, project) {
            if seen.insert(candidate.definition.clone()) {
                out.push(candidate);
            }
        }
    }
    for candidate in class_candidates(&corrs, project) {
        if seen.insert(candidate.definition.clone()) {
            out.push(candidate);
        }
    }
    out
}

fn qualifying(state: &IntervalState, candidates: Vec<Candidate>, min_improved: usize) -> Vec<(Candidate, AppendScore)> {
    let single: Vec<Candidate> = candidates.into_iter().filter(|c| c.rules.len() == 1).collect();
    let scores: Vec<AppendScore> = single.par_iter().map(|c| state.score_append(&c.rules[0])).collect();
    let mut scored: Vec<(Candidate, AppendScore)> = single
        .into_iter()
        .zip(scores)
        .filter(|(_, s)| s.delta_l < -EPSILON && s.improved >= min_improved)
        .collect();
    scored.sort_by(|a, b| a.1.delta_l.partial_cmp(&b.1.delta_l).unwrap());
    scored
}

fn placement_positions(n: usize) -> Vec<usize> {
    let mut positions = vec![0];
    if n >= 2 && n / 2 != 0 {
        positions.push(n / 2);
    }
    positions.retain(|&p| p != n);
    positions
}

fn best_candidate(state: &IntervalState, project: &Project) -> Option<(Candidate, usize, AppendScore)> {
    let settings = &project.settings.induction;
    let min_improved = settings.min_improved_words as usize;
    let mut finalists = Vec::new();
    for depth in [1, 2, 4] {
        let candidates = gather(state, project, settings.top_confusions as usize * depth);
        finalists = qualifying(state, candidates, min_improved);
        if !finalists.is_empty() {
            break;
        }
    }
    if finalists.is_empty() {
        return None;
    }
    let append_index = state.rules.len();
    let (first, first_score) = finalists[0].clone();
    let mut best = (first, append_index, first_score);
    let trials: Vec<(usize, usize)> = (0..finalists.len().min(settings.placement_candidates as usize))
        .flat_map(|f| placement_positions(append_index).into_iter().map(move |i| (f, i)))
        .collect();
    let scores: Vec<AppendScore> =
        trials.par_iter().map(|&(f, i)| state.score_at(&finalists[f].0.rules[0], i)).collect();
    for (&(f, index), score) in trials.iter().zip(scores) {
        if score.delta_l < best.2.delta_l - EPSILON && score.improved >= min_improved {
            best = (finalists[f].0.clone(), index, score);
        }
    }
    Some(best)
}

fn loss_and_exact(project: &Project, rules: &[Rule], model: &BitsModel) -> (f64, usize) {
    let state = IntervalState::new(project, rules.to_vec());
    let loss = state.baseline_fit + fsum(rules.iter().map(|r| rule_bits(r, model)).collect::<Vec<_>>());
    (loss, state.exact())
}

fn shrink(project: &Project, mut rules: Vec<Rule>, model: &BitsModel) -> (Vec<Rule>, Vec<String>) {
    let mut log = Vec::new();
    while rules.len() > 1 {
        let (base_loss, _) = loss_and_exact(project, &rules, model);
        let mut best_index = None;
        let mut best_loss = base_loss - EPSILON;
        let losses: Vec<f64> = (0..rules.len())
            .into_par_iter()
            .map(|index| {
                let mut trial = rules.clone();
                trial.remove(index);
                loss_and_exact(project, &trial, model).0
            })
            .collect();
        for (index, &loss) in losses.iter().enumerate() {
            if loss < best_loss {
                best_index = Some(index);
                best_loss = loss;
            }
        }
        let Some(index) = best_index else { break };
        log.push(format!(
            "removed `{}` (L {} → {})",
            rules[index].raw_definition,
            crate::py::fixed(base_loss, 0),
            crate::py::fixed(best_loss, 0)
        ));
        rules.remove(index);
    }
    (rules, log)
}

/// Induce one interval's cascade by greedy MDL boosting.
pub fn induce_interval(interval: &Interval) -> InducedInterval {
    let project = &interval.project;
    let settings = &project.settings.induction;
    let mut state = IntervalState::new(project, Vec::new());
    let start_fit = state.baseline_fit;
    let start_exact = state.exact();
    let assessed = state.assessed();
    let mut steps = Vec::new();
    let mut stopped = "max_rules";
    for _ in 0..settings.max_rules_per_interval {
        if state.baseline_fit <= EPSILON {
            stopped = "fit_zero";
            break;
        }
        let exact_before = state.exact();
        let Some((candidate, index, score)) = best_candidate(&state, project) else {
            stopped = "converged";
            break;
        };
        state.accept_at(&candidate.rules[0], index);
        steps.push(InductionStep {
            definition: candidate.definition,
            delta_l: score.delta_l,
            delta_fit: score.delta_fit,
            rule_cost: score.rule_cost,
            moved: score.moved,
            exact_before,
            exact_after: state.exact(),
            placement: index,
        });
    }
    let mut shrink_log = Vec::new();
    if state.rules.len() > 1 {
        let (kept, log) = shrink(project, state.rules.clone(), &bits_model(project));
        shrink_log = log;
        state = IntervalState::new(project, kept);
    }
    InducedInterval {
        label: interval.label(),
        rules: state.rules.clone(),
        steps,
        stopped,
        start_fit,
        final_fit: state.baseline_fit,
        start_exact,
        final_exact: state.exact(),
        assessed,
        shrink_log,
    }
}
