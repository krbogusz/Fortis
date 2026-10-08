//! Where a rule set goes wrong: the phone confusions at each stage, and for each erring target
//! phone the attested environments most associated with the error (phi coefficient).

use std::collections::HashMap;

use indexmap::IndexMap;

use super::accuracy::{DistanceToTarget, OpKind, StageAccuracy, align};
use crate::engine::segmentation::string_to_sequence;
use crate::engine::tiers::lower_tiers;
use crate::models::*;
use crate::py::{CsvWriter, fixed, signed_fixed};

const BOUNDARY: &str = "#";

pub struct Confusion {
    pub expected: Option<String>,
    pub got: Option<String>,
    pub count: usize,
    pub examples: Vec<String>,
}

impl Confusion {
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

/// Every non-match alignment op across the assessed words, most frequent first.
pub fn confusions(distances: &[DistanceToTarget]) -> Vec<Confusion> {
    let mut counts: IndexMap<(Option<String>, Option<String>), (usize, Vec<String>)> = IndexMap::new();
    for dtt in distances {
        if dtt.exact() {
            continue;
        }
        let label = if dtt.gloss.is_empty() {
            format!("{}/{}", dtt.derived, dtt.target)
        } else {
            format!("{}: {}/{}", dtt.gloss, dtt.derived, dtt.target)
        };
        for op in align(&dtt.target_phones, &dtt.derived_phones) {
            if op.kind == OpKind::Match {
                continue;
            }
            let entry = counts.entry((op.target, op.derived)).or_default();
            entry.0 += 1;
            if !entry.1.contains(&label) && entry.1.len() < 3 {
                entry.1.push(label.clone());
            }
        }
    }
    let shown = |s: &Option<String>| s.clone().unwrap_or_else(|| "None".into());
    let mut ordered: Vec<Confusion> = counts
        .into_iter()
        .map(|((expected, got), (count, examples))| Confusion { expected, got, count, examples })
        .collect();
    ordered.sort_by(|a, b| {
        b.count
            .cmp(&a.count)
            .then_with(|| shown(&a.expected).cmp(&shown(&b.expected)))
            .then_with(|| shown(&a.got).cmp(&shown(&b.got)))
    });
    ordered
}

pub struct ContextAssociation {
    pub predictor: String,
    pub phi: f64,
    pub fscore: f64,
    pub err_here: i64,
    pub ok_here: i64,
    pub err_away: i64,
    pub ok_away: i64,
}

pub struct FocusAutopsy {
    pub phone: String,
    /// How often the phone came out wrong, and how often it occurred.
    pub errors: i64,
    pub total: i64,
    /// The support a predictor needed to be listed.
    pub support_floor: i64,
    pub associations: Vec<ContextAssociation>,
}

pub fn phi_coefficient(err_here: i64, ok_here: i64, err_away: i64, ok_away: i64) -> f64 {
    let numerator = (err_here * ok_away - ok_here * err_away) as f64;
    let margins = (err_here + ok_here) as i128
        * (err_away + ok_away) as i128
        * (err_here + err_away) as i128
        * (ok_here + ok_away) as i128;
    if margins == 0 { 0.0 } else { numerator / (margins as f64).sqrt() }
}

fn f_score(err_here: i64, ok_here: i64, err_away: i64) -> f64 {
    let precision_denom = err_here + ok_here;
    let recall_denom = err_here + err_away;
    if err_here == 0 || precision_denom == 0 || recall_denom == 0 {
        return 0.0;
    }
    let precision = err_here as f64 / precision_denom as f64;
    let recall = err_here as f64 / recall_denom as f64;
    2.0 * precision * recall / (precision + recall)
}

/// Python's `str()` of a realized feature value.
fn value_str(value: &Value) -> String {
    let limb = |l: &Limb| match l {
        Limb::Int(n) => n.to_string(),
        Limb::None => "None".into(),
        Limb::Any => "any".into(),
        other => format!("{other:?}"),
    };
    match value {
        Value::One(l) => limb(l),
        Value::Contour(limbs) => format!("({})", limbs.iter().map(limb).collect::<Vec<_>>().join(", ")),
    }
}

/// Feature predictors for one phone, segmented on its own (cached).
struct FeatureMaps<'p> {
    project: &'p Project,
    cache: HashMap<String, Option<Vec<(String, String)>>>,
}

impl FeatureMaps<'_> {
    fn of(&mut self, phone: &str) -> Option<&Vec<(String, String)>> {
        if !self.cache.contains_key(phone) {
            let map = string_to_sequence(phone, self.project).ok().and_then(|form| {
                lower_tiers(&form).first().map(|b| {
                    b.items
                        .iter()
                        .filter(|(_, v)| !v.is_none())
                        .map(|(f, v)| (self.project.features.name(*f).to_string(), value_str(v)))
                        .collect()
                })
            });
            self.cache.insert(phone.to_string(), map);
        }
        self.cache[phone].as_ref()
    }
}

fn error_contexts(distances: &[DistanceToTarget], focus: &str, project: &Project, maps: &mut FeatureMaps) -> FocusAutopsy {
    let mut errors = 0i64;
    let mut total = 0i64;
    let mut err_with: HashMap<String, i64> = HashMap::new();
    let mut ok_with: HashMap<String, i64> = HashMap::new();
    for dtt in distances {
        let target = &dtt.target_phones;
        for op in align(target, &dtt.derived_phones) {
            if op.target.as_deref() != Some(focus) {
                continue;
            }
            let Some(i) = op.target_index else { continue };
            total += 1;
            let is_error = op.kind != OpKind::Match;
            errors += i64::from(is_error);
            let left = if i > 0 { target[i - 1].as_str() } else { BOUNDARY };
            let right = if i + 1 < target.len() { target[i + 1].as_str() } else { BOUNDARY };
            let mut predictors: Vec<String> = vec![format!("left={left}"), format!("right={right}")];
            for (side, phone) in [("left", left), ("right", right)] {
                if phone == BOUNDARY {
                    continue;
                }
                if let Some(features) = maps.of(phone) {
                    for (f, v) in features {
                        predictors.push(format!("{side}:{f}={v}"));
                    }
                }
            }
            predictors.sort_unstable();
            predictors.dedup();
            let counter = if is_error { &mut err_with } else { &mut ok_with };
            for p in predictors {
                *counter.entry(p).or_insert(0) += 1;
            }
        }
    }
    let diag = &project.settings.diagnosis;
    let floor = diag.min_support.max(((diag.min_support_percent * total) as f64 / 100.0).ceil() as i64);
    let mut associations = Vec::new();
    if errors >= diag.min_errors {
        let mut keys: Vec<&String> = err_with.keys().chain(ok_with.keys()).collect();
        keys.sort_unstable();
        keys.dedup();
        for predictor in keys {
            let err_here = err_with.get(predictor).copied().unwrap_or(0);
            let ok_here = ok_with.get(predictor).copied().unwrap_or(0);
            if err_here + ok_here < floor {
                continue;
            }
            let err_away = errors - err_here;
            let ok_away = (total - errors) - ok_here;
            associations.push(ContextAssociation {
                predictor: predictor.clone(),
                phi: phi_coefficient(err_here, ok_here, err_away, ok_away),
                fscore: f_score(err_here, ok_here, err_away),
                err_here,
                ok_here,
                err_away,
                ok_away,
            });
        }
    }
    associations.sort_by(|a, b| {
        b.phi
            .partial_cmp(&a.phi)
            .unwrap()
            .then_with(|| b.err_here.cmp(&a.err_here))
            .then_with(|| a.predictor.cmp(&b.predictor))
    });
    FocusAutopsy { phone: focus.to_string(), errors, total, support_floor: floor, associations }
}

pub struct StageDiagnosis {
    pub label: String,
    pub time: Option<i64>,
    pub confusions: Vec<Confusion>,
    pub autopsy: Vec<FocusAutopsy>,
}

pub fn diagnose_stages(stages: &[StageAccuracy], project: &Project) -> Vec<StageDiagnosis> {
    let mut maps = FeatureMaps { project, cache: HashMap::new() };
    stages
        .iter()
        .map(|stage| {
            let distances = &stage.report.distances;
            let confusions = confusions(distances);
            let mut focus: Vec<&str> = Vec::new();
            for c in &confusions {
                if let Some(e) = &c.expected
                    && !focus.contains(&e.as_str()) {
                        focus.push(e);
                    }
            }
            let autopsy = focus.iter().map(|p| error_contexts(distances, p, project, &mut maps)).collect();
            StageDiagnosis { label: stage.label.clone(), time: stage.time, confusions, autopsy }
        })
        .collect()
}

pub fn errors_summary_line(stages: &[StageDiagnosis]) -> String {
    let Some(final_stage) = stages.iter().find(|s| s.time.is_none()).filter(|s| !s.confusions.is_empty()) else {
        return "no errors — every assessed word is exact at the final".into();
    };
    let sites: usize = final_stage.confusions.iter().map(|c| c.count).sum();
    let top = &final_stage.confusions[0];
    format!(
        "final: {sites} error site(s), {} distinct; most common {}→{} ({}×) — see errors.csv",
        final_stage.confusions.len(),
        top.expected.as_deref().unwrap_or("∅"),
        top.got.as_deref().unwrap_or("∅"),
        top.count
    )
}

pub fn render_errors_csv(stages: &[StageDiagnosis]) -> String {
    let mut w = CsvWriter::new();
    w.row(["stage", "expected", "got", "count", "kind", "examples (gloss: derived vs. attested)"]);
    for stage in stages {
        for c in &stage.confusions {
            w.row([
                stage.label.clone(),
                c.expected.clone().unwrap_or_else(|| "∅".into()),
                c.got.clone().unwrap_or_else(|| "∅".into()),
                c.count.to_string(),
                c.kind().to_string(),
                c.examples.join("; "),
            ]);
        }
    }
    w.out
}

pub fn render_error_context_csv(stages: &[StageDiagnosis]) -> String {
    let mut w = CsvWriter::new();
    w.row(["stage", "segment", "environment", "assoc. (φ)", "F₁", "err/ok · with", "err/ok · without"]);
    for stage in stages {
        for autopsy in &stage.autopsy {
            for a in &autopsy.associations {
                if a.phi <= 0.0 {
                    continue;
                }
                w.row([
                    stage.label.clone(),
                    autopsy.phone.clone(),
                    a.predictor.clone(),
                    signed_fixed(a.phi, 2),
                    fixed(a.fscore, 2),
                    format!("{}/{}", a.err_here, a.ok_here),
                    format!("{}/{}", a.err_away, a.ok_away),
                ]);
            }
        }
    }
    w.out
}

/// The `(stage, segment)` autopsies with no positively associated predictor.
pub fn error_context_omissions(stages: &[StageDiagnosis]) -> Vec<(String, String)> {
    stages
        .iter()
        .flat_map(|s| {
            s.autopsy
                .iter()
                .filter(|a| !a.associations.iter().any(|x| x.phi > 0.0))
                .map(|a| (s.label.clone(), a.phone.clone()))
                .collect::<Vec<_>>()
        })
        .collect()
}
