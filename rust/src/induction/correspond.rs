//! Residual correspondences read from the derived side, each with its phi-ranked conditioning
//! environments; and the notation renderer for feature predictors.

use std::collections::HashMap;

use indexmap::IndexMap;

use crate::analysis::accuracy::{DistanceToTarget, OpKind, align, segment_form};
use crate::models::*;

const BOUNDARY: &str = "#";

/// A realized value as Python's `str()` would key it: only integers are renderable.
pub type FeatureMap = Vec<(String, Value)>;

pub struct FeatureMaps<'p> {
    project: &'p Project,
    cache: HashMap<String, Option<FeatureMap>>,
}

impl<'p> FeatureMaps<'p> {
    pub fn new(project: &'p Project) -> Self {
        FeatureMaps { project, cache: HashMap::new() }
    }

    /// The specified features of one phone, or `None` if it does not segment to one segment.
    pub fn of(&mut self, phone: &str) -> Option<FeatureMap> {
        if let Some(hit) = self.cache.get(phone) {
            return hit.clone();
        }
        let map = segment_form(phone, self.project).filter(|b| b.len() == 1).map(|b| {
            b[0].items
                .iter()
                .filter(|(_, v)| !v.is_none())
                .map(|(f, v)| (self.project.features.name(*f).to_string(), v.clone()))
                .collect()
        });
        self.cache.insert(phone.to_string(), map.clone());
        map
    }
}

/// One feature/value pair as a notation token, or `None` if it has no single-token spelling.
pub fn render_feature(feature: &str, value: &Value, features: &FeatureInventory) -> Option<String> {
    let id = features.id(feature)?;
    let Value::One(Limb::Int(n)) = value else { return None };
    match features.kind(id) {
        FeatureKind::Unary => (*n == 1).then(|| feature.to_string()),
        FeatureKind::Binary => Some(if *n == 1 { format!("+{feature}") } else { format!("-{feature}") }),
        FeatureKind::Scalar => features.get(id).label_of(*n).map(|l| format!("{feature}: {l}")),
    }
}

pub fn render_feature_map(pairs: &[(String, Value)], features: &FeatureInventory) -> Option<String> {
    let tokens: Vec<String> = pairs.iter().filter_map(|(f, v)| render_feature(f, v, features)).collect();
    if tokens.is_empty() { None } else { Some(format!("[{}]", tokens.join(", "))) }
}

#[derive(Clone, Debug)]
pub struct ContextPredictor {
    pub side: &'static str,
    pub element: String,
    pub phi: f64,
    pub change_here: i64,
}

#[derive(Clone, Debug)]
pub struct Correspondence {
    pub expected: Option<String>,
    pub got: Option<String>,
    pub count: usize,
    pub predictors: Vec<ContextPredictor>,
    pub feature_delta: Vec<(String, Value)>,
    pub got_features: Vec<(String, Value)>,
}

impl Correspondence {
    pub fn kind(&self) -> &'static str {
        if self.expected.is_none() {
            "insertion"
        } else if self.got.is_none() {
            "deletion"
        } else {
            "substitution"
        }
    }
}

fn neighbours(phones: &[String], i: usize) -> (&str, &str) {
    let left = if i > 0 { phones[i - 1].as_str() } else { BOUNDARY };
    let right = if i + 1 < phones.len() { phones[i + 1].as_str() } else { BOUNDARY };
    (left, right)
}

fn predictors_at(left: &str, right: &str, maps: &mut FeatureMaps, features: &FeatureInventory) -> Vec<(&'static str, String)> {
    let mut out = Vec::new();
    for (side, phone) in [("left", left), ("right", right)] {
        if phone == BOUNDARY {
            out.push((side, BOUNDARY.to_string()));
            continue;
        }
        let Some(map) = maps.of(phone) else { continue };
        out.push((side, phone.to_string()));
        for (f, v) in &map {
            if let Some(token) = render_feature(f, v, features) {
                out.push((side, format!("[{token}]")));
            }
        }
    }
    out.sort();
    out.dedup();
    out
}

type Tally = HashMap<(&'static str, String), i64>;

fn rank(change_with: &Tally, stay_with: &Tally, changes: i64, stays: i64, project: &Project) -> Vec<ContextPredictor> {
    let total = changes + stays;
    let s = &project.settings.diagnosis;
    let floor = s.min_support.max(((s.min_support_percent * total) as f64 / 100.0).ceil() as i64);
    let mut keys: Vec<&(&'static str, String)> = change_with.keys().chain(stay_with.keys()).collect();
    keys.sort();
    keys.dedup();
    let mut ranked = Vec::new();
    for key in keys {
        let change_here = change_with.get(key).copied().unwrap_or(0);
        let stay_here = stay_with.get(key).copied().unwrap_or(0);
        if change_here + stay_here < floor {
            continue;
        }
        let phi = crate::analysis::diagnosis::phi_coefficient(change_here, stay_here, changes - change_here, stays - stay_here);
        if phi <= 0.0 {
            continue;
        }
        ranked.push(ContextPredictor { side: key.0, element: key.1.clone(), phi, change_here });
    }
    ranked.sort_by(|a, b| {
        b.phi
            .partial_cmp(&a.phi)
            .unwrap()
            .then_with(|| b.change_here.cmp(&a.change_here))
            .then_with(|| a.side.cmp(b.side))
            .then_with(|| a.element.cmp(&b.element))
    });
    ranked
}

type Graded<'a> = Vec<&'a DistanceToTarget>;

/// Should-change vs should-stay sites anchored on the derived phone *got*.
fn anchored_predictors(words: &Graded, got: &str, is_change: impl Fn(&crate::analysis::accuracy::AlignOp) -> bool, maps: &mut FeatureMaps, project: &Project) -> Vec<ContextPredictor> {
    let mut change_with = Tally::new();
    let mut stay_with = Tally::new();
    let (mut changes, mut stays) = (0, 0);
    for dtt in words {
        for op in align(&dtt.target_phones, &dtt.derived_phones) {
            if op.derived.as_deref() != Some(got) {
                continue;
            }
            let Some(i) = op.derived_index else { continue };
            let bucket = if is_change(&op) {
                changes += 1;
                &mut change_with
            } else if op.kind == OpKind::Match {
                stays += 1;
                &mut stay_with
            } else {
                continue;
            };
            let (left, right) = neighbours(&dtt.derived_phones, i);
            for p in predictors_at(left, right, maps, &project.features) {
                *bucket.entry(p).or_insert(0) += 1;
            }
        }
    }
    rank(&change_with, &stay_with, changes, stays, project)
}

fn deletion_predictors(words: &Graded, expected: &str) -> Vec<ContextPredictor> {
    let mut left_counts: IndexMap<String, i64> = IndexMap::new();
    let mut right_counts: IndexMap<String, i64> = IndexMap::new();
    let mut sites = 0i64;
    for dtt in words {
        let derived = &dtt.derived_phones;
        let mut pos = 0usize;
        for op in align(&dtt.target_phones, derived) {
            if op.kind == OpKind::Delete && op.target.as_deref() == Some(expected) {
                sites += 1;
                let left = if pos > 0 { derived[pos - 1].clone() } else { BOUNDARY.to_string() };
                let right = if pos < derived.len() { derived[pos].clone() } else { BOUNDARY.to_string() };
                *left_counts.entry(left).or_insert(0) += 1;
                *right_counts.entry(right).or_insert(0) += 1;
            }
            if let Some(j) = op.derived_index {
                pos = j + 1;
            }
        }
    }
    let mut out = Vec::new();
    for (side, counts) in [("left", left_counts), ("right", right_counts)] {
        let mut entries: Vec<(String, i64)> = counts.into_iter().collect();
        entries.sort_by(|a, b| b.1.cmp(&a.1));
        for (element, count) in entries {
            let phi = if sites != 0 { count as f64 / sites as f64 } else { 0.0 };
            out.push(ContextPredictor { side, element, phi, change_here: count });
        }
    }
    out
}

/// The top *cap* residual correspondences, each with its derived-side predictors.
pub fn correspondences(distances: &[&DistanceToTarget], project: &Project, cap: usize) -> Vec<Correspondence> {
    let distance_cap = project.settings.induction.alignment_distance_cap;
    let words: Graded = distances.iter().copied().filter(|d| !d.exact() && d.distance <= distance_cap).collect();
    let mut counts: IndexMap<(Option<String>, Option<String>), usize> = IndexMap::new();
    for dtt in &words {
        for op in align(&dtt.target_phones, &dtt.derived_phones) {
            if op.kind != OpKind::Match {
                *counts.entry((op.target, op.derived)).or_insert(0) += 1;
            }
        }
    }
    let shown = |s: &Option<String>| s.clone().unwrap_or_else(|| "None".into());
    let mut ordered: Vec<((Option<String>, Option<String>), usize)> = counts.into_iter().collect();
    ordered.sort_by(|a, b| {
        b.1.cmp(&a.1).then_with(|| shown(&a.0.0).cmp(&shown(&b.0.0))).then_with(|| shown(&a.0.1).cmp(&shown(&b.0.1)))
    });
    let mut maps = FeatureMaps::new(project);
    let mut out = Vec::new();
    for ((expected, got), count) in ordered.into_iter().take(cap) {
        let mut feature_delta = Vec::new();
        let mut got_features = Vec::new();
        let predictors = match (&expected, &got) {
            (Some(e), None) => deletion_predictors(&words, e),
            (None, Some(g)) => anchored_predictors(&words, g, |op| op.kind == OpKind::Insert, &mut maps, project),
            (Some(e), Some(g)) => {
                let e2 = e.clone();
                let p = anchored_predictors(
                    &words,
                    g,
                    move |op| op.target.as_deref() == Some(e2.as_str()) && op.kind != OpKind::Match,
                    &mut maps,
                    project,
                );
                if let (Some(a), Some(b)) = (maps.of(e), maps.of(g)) {
                    let mut pairs: Vec<(String, Value)> = a
                        .iter()
                        .filter(|(f, v)| b.iter().find(|(g, _)| g == f).map(|(_, w)| w) != Some(v))
                        .cloned()
                        .collect();
                    pairs.sort_by(|x, y| x.0.cmp(&y.0));
                    feature_delta = pairs;
                }
                if let Some(mut m) = maps.of(g) {
                    m.sort_by(|x, y| x.0.cmp(&y.0));
                    got_features = m;
                }
                p
            }
            (None, None) => Vec::new(),
        };
        out.push(Correspondence { expected, got, count, predictors, feature_delta, got_features });
    }
    out
}
