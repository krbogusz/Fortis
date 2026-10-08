//! Incremental candidate scoring: one interval's cached derivations, and a candidate scored by
//! applying it once to each word's running form (the append fast path).

use std::sync::Arc;

use rayon::prelude::*;

use super::objective::{BitsModel, PhoneCache, bits_model, residual_bits, rule_bits};
use crate::analysis::accuracy::{DistanceToTarget, distance_to_target};
use crate::engine::deriving::{Engine, PreparedRule};
use crate::engine::rendering::Renderer;
use crate::engine::matching::{Supply, word_supply};
use crate::engine::tiers::{cleanup_tiers, lower_tiers};
use crate::models::*;

/// The rules keyed by their list index, which is their order within an interval.
pub fn timed_inventory(rules: &[Rule]) -> RuleInventory {
    let mut inv = RuleInventory::default();
    for (i, rule) in rules.iter().enumerate() {
        inv.by_time.insert(Some(i as i64), vec![Arc::new(Rule { time: Some(i as i64), ..rule.clone() })]);
    }
    inv
}

#[derive(Clone, Copy, Debug)]
pub struct AppendScore {
    pub delta_l: f64,
    pub delta_fit: f64,
    pub rule_cost: f64,
    pub improved: usize,
    pub regressed: usize,
    pub moved: usize,
}

/// Whether two forms are equal as Python's dataclass equality sees them.
pub fn forms_equal(a: &Form, b: &Form) -> bool {
    if a.segments.len() != b.segments.len()
        || a.segments.iter().zip(&b.segments).any(|(x, y)| x.id != y.id || x.bundle != y.bundle)
    {
        return false;
    }
    if a.tiers.len() != b.tiers.len() {
        return false;
    }
    a.tiers.iter().all(|(name, t)| {
        b.tiers.get(name).is_some_and(|u| {
            t.links == u.links
                && t.float_hosts.len() == u.float_hosts.len()
                && t.float_hosts.iter().all(|(k, v)| u.float_hosts.get(k) == Some(v))
                && t.autosegs.len() == u.autosegs.len()
                && t.autosegs.iter().zip(&u.autosegs).all(|(x, y)| x.id == y.id && x.bundle == y.bundle)
        })
    })
}

pub struct IntervalState<'p> {
    pub project: &'p Project,
    pub rules: Vec<Rule>,
    pub model: BitsModel,
    phones: PhoneCache,
    renderer: Renderer<'p>,
    engine: Engine<'p>,
    pub baseline: Vec<Derivation>,
    /// Each baseline word's running form, lowered, with its supply: the append fast path's input.
    running: Vec<(Vec<Arc<FeatureBundle>>, Supply)>,
    pub baseline_distances: Vec<Option<DistanceToTarget>>,
    pub baseline_residuals: Vec<f64>,
    pub baseline_fit: f64,
}

impl<'p> IntervalState<'p> {
    pub fn new(project: &'p Project, rules: Vec<Rule>) -> IntervalState<'p> {
        let engine = Engine::with_rules(project, &RuleInventory::default()).expect("no rules to resolve");
        let mut state = IntervalState {
            project,
            rules,
            model: bits_model(project),
            phones: PhoneCache::new(),
            renderer: Renderer::new(project),
            engine,
            baseline: Vec::new(),
            running: Vec::new(),
            baseline_distances: Vec::new(),
            baseline_residuals: Vec::new(),
            baseline_fit: 0.0,
        };
        state.baseline = state.derive(&state.rules);
        state.refresh();
        state
    }

    fn derive(&self, rules: &[Rule]) -> Vec<Derivation> {
        let engine = Engine::with_rules(self.project, &timed_inventory(rules)).expect("candidate rules resolve");
        engine.derive_all().expect("interval words segment")
    }

    fn residual(&self, dtt: Option<&DistanceToTarget>) -> f64 {
        match dtt {
            None => 0.0,
            Some(d) => d.frequency as f64 * residual_bits(d, self.project, &self.model, &self.phones),
        }
    }

    fn refresh(&mut self) {
        self.running = self
            .baseline
            .par_iter()
            .map(|d| {
                let lowered = lower_tiers(d.steps.last().map_or(&d.input, |s| &s.after));
                let supply = word_supply(&lowered);
                (lowered, supply)
            })
            .collect();
        let distances: Vec<Option<DistanceToTarget>> =
            self.baseline.par_iter().map(|d| distance_to_target(d, self.project, &self.renderer)).collect();
        let residuals: Vec<f64> = distances.iter().map(|d| self.residual(d.as_ref())).collect();
        self.baseline_fit = crate::py::fsum(residuals.iter().copied());
        self.baseline_distances = distances;
        self.baseline_residuals = residuals;
    }

    fn resolved(&self, candidate: &Rule) -> PreparedRule {
        let placed = Rule { time: Some(self.rules.len() as i64), ..candidate.clone() };
        self.engine.prepare(&placed).expect("candidate rules resolve")
    }

    /// The derivation after applying *prep* once at the end of *base*'s cascade, or `None`
    /// when the rule does not change the word.
    fn append(&self, base: &Derivation, running: Option<&(Vec<Arc<FeatureBundle>>, Supply)>, prep: &PreparedRule) -> Option<Derivation> {
        let pre = base.steps.last().map_or(&base.input, |s| &s.after);
        let after = match running {
            Some((lowered, supply)) => self.engine.apply_with(prep, pre, lowered, supply)?,
            None => self.engine.apply_once(prep, pre)?,
        };
        if !Engine::fired(pre, &after) {
            return None;
        }
        let time = prep.rule.time;
        let after = self.engine.maintain_tiers(after, time);
        let step = DerivationStep {
            before: pre.clone(),
            rule: prep.rule.clone(),
            before_boundaries: self.engine.boundaries(&pre.bundles(), time),
            after_boundaries: self.engine.boundaries(&after.bundles(), time),
            after: Arc::new(after),
        };
        let mut surface = (*step.after).clone();
        cleanup_tiers(&mut surface, &self.project.tiers, true);
        let surface_boundaries = self.engine.boundaries(&surface.bundles(), time);
        let mut steps = base.steps.clone();
        steps.push(step);
        Some(Derivation {
            word: base.word.clone(),
            input: base.input.clone(),
            steps,
            surface: Arc::new(surface),
            surface_boundaries,
        })
    }

    pub fn score_append(&self, candidate: &Rule) -> AppendScore {
        let prep = self.resolved(candidate);
        let moved: Vec<(usize, f64)> = (0..self.baseline.len())
            .into_par_iter()
            .filter_map(|i| {
                let new = self.append(&self.baseline[i], Some(&self.running[i]), &prep)?;
                let dtt = distance_to_target(&new, self.project, &self.renderer);
                Some((i, self.residual(dtt.as_ref())))
            })
            .collect();
        let mut delta_fit = 0.0;
        let (mut improved, mut regressed) = (0, 0);
        for &(i, new_residual) in &moved {
            let old = self.baseline_residuals[i];
            delta_fit += new_residual - old;
            if new_residual < old {
                improved += 1;
            } else if new_residual > old {
                regressed += 1;
            }
        }
        let rule_cost = rule_bits(candidate, &self.model);
        AppendScore { delta_l: rule_cost + delta_fit, delta_fit, rule_cost, improved, regressed, moved: moved.len() }
    }

    pub fn score_at(&self, candidate: &Rule, index: usize) -> AppendScore {
        if index == self.rules.len() {
            return self.score_append(candidate);
        }
        let mut spliced = self.rules.clone();
        spliced.insert(index, candidate.clone());
        let derivations = self.derive(&spliced);
        let mut new_fit = 0.0;
        let (mut improved, mut regressed, mut moved) = (0, 0, 0);
        let residuals: Vec<f64> = derivations
            .par_iter()
            .map(|d| self.residual(distance_to_target(d, self.project, &self.renderer).as_ref()))
            .collect();
        for (i, d) in derivations.iter().enumerate() {
            let new_residual = residuals[i];
            new_fit += new_residual;
            if !forms_equal(&self.baseline[i].surface, &d.surface) {
                moved += 1;
            }
            let base = self.baseline_residuals[i];
            if new_residual < base {
                improved += 1;
            } else if new_residual > base {
                regressed += 1;
            }
        }
        let rule_cost = rule_bits(candidate, &self.model);
        AppendScore {
            delta_l: rule_cost + (new_fit - self.baseline_fit),
            delta_fit: new_fit - self.baseline_fit,
            rule_cost,
            improved,
            regressed,
            moved,
        }
    }

    pub fn accept_at(&mut self, candidate: &Rule, index: usize) {
        if index == self.rules.len() {
            let prep = self.resolved(candidate);
            self.rules.push(candidate.clone());
            let baseline = std::mem::take(&mut self.baseline);
            let running = std::mem::take(&mut self.running);
            self.baseline = baseline
                .into_par_iter()
                .zip(running)
                .map(|(b, r)| self.append(&b, Some(&r), &prep).unwrap_or(b))
                .collect();
        } else {
            self.rules.insert(index, candidate.clone());
            self.baseline = self.derive(&self.rules);
        }
        self.refresh();
    }

    pub fn exact(&self) -> usize {
        self.baseline_distances.iter().flatten().filter(|d| d.exact()).count()
    }

    pub fn assessed(&self) -> usize {
        self.baseline_distances.iter().flatten().count()
    }
}
