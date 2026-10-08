//! The two-part MDL objective in bits: fit bits (the corrections from derived to attested) plus
//! rule bits (the cost of writing each rule).

use std::collections::HashMap;
use std::sync::Arc;

use crate::analysis::accuracy::{AccuracyReport, DistanceToTarget, OpKind, accuracy_by_stage, align, comparable_bundles, feature_diff, segment_form, try_segment};
use crate::engine::rendering::Renderer;
use crate::models::*;
use crate::py::fsum;

pub const B_RULE: f64 = 10.0;
pub const B_TAG: f64 = 3.0;

#[derive(Clone, Copy, Debug)]
pub struct BitsModel {
    pub b_site: f64,
    pub b_feat: f64,
    pub letter_bits: f64,
    pub mean_features: f64,
}

fn specified_count(b: &FeatureBundle) -> usize {
    b.items.iter().filter(|(_, v)| !v.is_none()).count()
}

fn mean_attested_length(project: &Project) -> f64 {
    let mut lengths: Vec<usize> = Vec::new();
    for word in project.words.values() {
        let mut strings: Vec<&str> = word.final_ipa().into_iter().collect();
        strings.extend(word.stages().into_iter().map(|(_, s)| s));
        for s in strings {
            if let Some(form) = try_segment(s, project) {
                lengths.push(comparable_bundles(&form).len());
            }
        }
    }
    if lengths.is_empty() { 1.0 } else { lengths.iter().sum::<usize>() as f64 / lengths.len() as f64 }
}

pub fn bits_model(project: &Project) -> BitsModel {
    let num_features = project.features.len().max(1) as f64;
    let counts: Vec<usize> = project.features.iter().map(|(_, f)| f.values.len().max(1)).collect();
    let mean_values = if counts.is_empty() { 1.0 } else { counts.iter().sum::<usize>() as f64 / counts.len() as f64 };
    let num_letters = project.letters.len().max(1) as f64;
    let letter_counts: Vec<usize> = project.letters.letters.iter().map(|l| specified_count(&l.bundle)).collect();
    let mean_features = if letter_counts.is_empty() {
        1.0
    } else {
        letter_counts.iter().sum::<usize>() as f64 / letter_counts.len() as f64
    };
    BitsModel {
        b_site: 3f64.log2() + (mean_attested_length(project) + 1.0).log2(),
        b_feat: num_features.log2() + mean_values.max(1.0).log2(),
        letter_bits: num_letters.log2(),
        mean_features,
    }
}

/// A phone → the single bundle it segments to, memoised (shared across threads).
#[derive(Default)]
pub struct PhoneCache(std::sync::Mutex<HashMap<String, Option<Arc<FeatureBundle>>>>);

impl PhoneCache {
    pub fn new() -> Self {
        Self::default()
    }
}

fn phone_bundle(phone: &str, project: &Project, cache: &PhoneCache) -> Option<Arc<FeatureBundle>> {
    if let Some(hit) = cache.0.lock().unwrap().get(phone) {
        return hit.clone();
    }
    let bundle = segment_form(phone, project).filter(|b| b.len() == 1).map(|mut b| b.remove(0));
    cache.0.lock().unwrap().insert(phone.to_string(), bundle.clone());
    bundle
}

/// Bits to encode the corrections turning the derived form into the target.
pub fn residual_bits(dtt: &DistanceToTarget, project: &Project, model: &BitsModel, cache: &PhoneCache) -> f64 {
    let mut total = 0.0;
    for op in align(&dtt.target_phones, &dtt.derived_phones) {
        match op.kind {
            OpKind::Match => {}
            OpKind::Sub => {
                let a = phone_bundle(op.target.as_deref().unwrap(), project, cache);
                let b = phone_bundle(op.derived.as_deref().unwrap(), project, cache);
                let delta = match (a, b) {
                    (Some(a), Some(b)) => feature_diff(&a, &b) as f64,
                    _ => model.mean_features,
                };
                total += model.b_site + model.b_feat * delta;
            }
            OpKind::Delete => {
                let count = match phone_bundle(op.target.as_deref().unwrap(), project, cache) {
                    Some(b) => specified_count(&b) as f64,
                    None => model.mean_features,
                };
                total += model.b_site + model.b_feat * count;
            }
            OpKind::Insert => total += model.b_site,
        }
    }
    total
}

fn content_bits(el: &Element, model: &BitsModel) -> f64 {
    match el {
        Element::LetterRef(_) | Element::LetterBundle(_) => model.letter_bits,
        Element::ModifiedLetter(_, delta) => model.letter_bits + model.b_feat * delta.len() as f64,
        Element::BundleElem(b) | Element::FloatingAutoseg(b) => model.b_feat * b.len() as f64,
        Element::ResultElem(b) => model.b_feat * b.len() as f64,
        Element::Group(inner) => fsum(inner.iter().map(|e| element_bits(e, model))),
        Element::Disjunction(branches) => fsum(branches.iter().flatten().map(|e| element_bits(e, model))),
        Element::Negated(inner) | Element::Quantified(inner, _) | Element::Bound(_, inner) => content_bits(inner, model),
        _ => 0.0,
    }
}

pub fn element_bits(el: &Element, model: &BitsModel) -> f64 {
    B_TAG + content_bits(el, model)
}

pub fn rule_bits(rule: &Rule, model: &BitsModel) -> f64 {
    let sd = &rule.sd;
    let sides = [&sd.target, &sd.result, &sd.left_context, &sd.right_context, &sd.left_exception, &sd.right_exception];
    B_RULE + fsum(sides.iter().flat_map(|s| s.iter()).map(|e| element_bits(e, model)))
}

#[derive(Clone, Copy, Debug)]
pub struct CascadeScore {
    pub fit_bits: f64,
    pub rule_bits: f64,
    pub exact: usize,
    pub assessed: usize,
    pub mean_distance: f64,
}

impl CascadeScore {
    pub fn total(&self) -> f64 {
        self.fit_bits + self.rule_bits
    }
}

pub fn fit_bits_of_report(report: &AccuracyReport, project: &Project, model: &BitsModel, cache: &PhoneCache, weight: f64) -> f64 {
    weight * fsum(report.distances.iter().map(|d| d.frequency as f64 * residual_bits(d, project, model, cache)).collect::<Vec<_>>())
}

/// The whole-cascade loss over every checkpoint, plus the final checkpoint's accuracy.
pub fn cascade_score(derivations: &[Derivation], project: &Project, r: &Renderer) -> CascadeScore {
    let model = bits_model(project);
    let cache = PhoneCache::new();
    let final_weight = project.settings.induction.final_weight;
    let stages = accuracy_by_stage(derivations, project, r);
    let mut fit = 0.0;
    let mut final_report = None;
    for stage in &stages {
        let weight = if stage.time.is_none() { final_weight } else { 1.0 };
        fit += fit_bits_of_report(&stage.report, project, &model, &cache, weight);
        if stage.time.is_none() {
            final_report = Some(&stage.report);
        }
    }
    let report = final_report.unwrap();
    CascadeScore {
        fit_bits: fit,
        rule_bits: fsum(project.rules.in_file_order().map(|r| rule_bits(r, &model)).collect::<Vec<_>>()),
        exact: report.exact(),
        assessed: report.assessed(),
        mean_distance: report.mean_distance(),
    }
}
