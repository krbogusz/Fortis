//! Distance from each derived form to its attested target: a phone distance over inventory
//! segments and a feature-weighted distance over the same bundles, per stage and at the final.

use std::sync::Arc;

use rayon::prelude::*;

use crate::engine::deriving::Engine;
use crate::engine::rendering::Renderer;
use crate::engine::segmentation::string_to_sequence;
use crate::engine::tiers::lower_tiers;
use crate::models::*;

/// Damerau–Levenshtein (optimal string alignment) with unit costs and a set swap cost.
pub fn edit_distance<T: PartialEq>(a: &[T], b: &[T], transposition_cost: i64) -> i64 {
    let (n, m) = (a.len(), b.len());
    let mut d = vec![vec![0i64; m + 1]; n + 1];
    for (i, row) in d.iter_mut().enumerate() {
        row[0] = i as i64;
    }
    for j in 0..=m {
        d[0][j] = j as i64;
    }
    for i in 1..=n {
        for j in 1..=m {
            let sub = d[i - 1][j - 1] + i64::from(a[i - 1] != b[j - 1]);
            d[i][j] = (d[i - 1][j] + 1).min(d[i][j - 1] + 1).min(sub);
            if i > 1 && j > 1 && a[i - 1] == b[j - 2] && a[i - 2] == b[j - 1] {
                d[i][j] = d[i][j].min(d[i - 2][j - 2] + transposition_cost);
            }
        }
    }
    d[n][m]
}

/// The form's segments, suprasegmentals folded in, morpheme boundaries dropped.
pub fn comparable_bundles(form: &Form) -> Vec<Arc<FeatureBundle>> {
    lower_tiers(form).into_iter().filter(|b| !is_morpheme_boundary(b)).collect()
}

pub fn form_phones(form: &Form, r: &Renderer) -> Vec<String> {
    comparable_bundles(form).iter().map(|b| r.segment(b, false)).collect()
}

pub fn phone_keys(form: &Form) -> Vec<BundleKey> {
    comparable_bundles(form).iter().map(|b| b.key()).collect()
}

/// Segment a rendered string with dots, boundaries, stress marks and spaces stripped.
pub fn segment_form(text: &str, project: &Project) -> Option<Vec<Arc<FeatureBundle>>> {
    let cleaned: String =
        text.chars().filter(|c| !matches!(c, '.' | '-' | 'ˈ' | 'ˌ') && !crate::py::is_space(*c)).collect();
    string_to_sequence(&cleaned, project).ok().map(|f| lower_tiers(&f))
}

pub fn try_segment(text: &str, project: &Project) -> Option<Form> {
    string_to_sequence(text, project).ok()
}

/// Segment every target of each derivation's word against the inventory, in place.
pub fn ingest_targets(derivations: &mut [Derivation], project: &Project) {
    for d in derivations {
        ingest_word(&mut d.word, project);
    }
}

pub fn ingest_word(word: &mut Word, project: &Project) {
    let seed = word.seed_time();
    let who = if word.gloss.is_empty() { word.ipa().to_string() } else { word.gloss.clone() };
    for (time, attestation) in &mut word.forms {
        if *time == seed {
            continue;
        }
        attestation.form = try_segment(&attestation.ipa, project);
        if attestation.form.is_none() {
            let where_ = time.map_or("final".to_string(), |t| format!("stage {t}"));
            eprintln!(
                "warning: attested {where_} form {} for {} uses a symbol not in the inventory — skipped from the accuracy and error analyses",
                crate::py::repr_str(&attestation.ipa),
                crate::py::repr_str(&who)
            );
        }
    }
}

#[derive(Clone, Copy, PartialEq, Eq, Debug)]
pub enum OpKind {
    Match,
    Sub,
    Delete,
    Insert,
}

/// One step of a target→derived alignment.
#[derive(Clone, Debug)]
pub struct AlignOp {
    pub kind: OpKind,
    pub target: Option<String>,
    pub derived: Option<String>,
    pub target_index: Option<usize>,
    pub derived_index: Option<usize>,
}

/// Levenshtein alignment with a deterministic traceback: diagonal, then deletion, then insertion.
pub fn align(target: &[String], derived: &[String]) -> Vec<AlignOp> {
    let (n, m) = (target.len(), derived.len());
    let mut d = vec![vec![0usize; m + 1]; n + 1];
    for (i, row) in d.iter_mut().enumerate() {
        row[0] = i;
    }
    for j in 0..=m {
        d[0][j] = j;
    }
    for i in 1..=n {
        for j in 1..=m {
            let sub = d[i - 1][j - 1] + usize::from(target[i - 1] != derived[j - 1]);
            d[i][j] = sub.min(d[i - 1][j] + 1).min(d[i][j - 1] + 1);
        }
    }
    let mut ops = Vec::new();
    let (mut i, mut j) = (n, m);
    while i > 0 || j > 0 {
        if i > 0 && j > 0 && d[i][j] == d[i - 1][j - 1] + usize::from(target[i - 1] != derived[j - 1]) {
            let kind = if target[i - 1] == derived[j - 1] { OpKind::Match } else { OpKind::Sub };
            ops.push(AlignOp {
                kind,
                target: Some(target[i - 1].clone()),
                derived: Some(derived[j - 1].clone()),
                target_index: Some(i - 1),
                derived_index: Some(j - 1),
            });
            i -= 1;
            j -= 1;
        } else if i > 0 && d[i][j] == d[i - 1][j] + 1 {
            ops.push(AlignOp {
                kind: OpKind::Delete,
                target: Some(target[i - 1].clone()),
                derived: None,
                target_index: Some(i - 1),
                derived_index: None,
            });
            i -= 1;
        } else {
            ops.push(AlignOp {
                kind: OpKind::Insert,
                target: None,
                derived: Some(derived[j - 1].clone()),
                target_index: None,
                derived_index: Some(j - 1),
            });
            j -= 1;
        }
    }
    ops.reverse();
    ops
}

/// Number of features on which two segments disagree (present vs absent counts).
pub fn feature_diff(a: &FeatureBundle, b: &FeatureBundle) -> i64 {
    fn specified(bundle: &FeatureBundle, f: FeatId) -> Option<&Value> {
        bundle.get(f).filter(|v| !v.is_none())
    }
    let mut count = 0;
    for (f, v) in &a.items {
        if v.is_none() {
            continue;
        }
        if specified(b, *f) != Some(v) {
            count += 1;
        }
    }
    for (f, v) in &b.items {
        if v.is_none() {
            continue;
        }
        if specified(a, *f).is_none() {
            count += 1;
        }
    }
    count
}

fn sorted_specified(b: &FeatureBundle) -> Vec<(FeatId, &Value)> {
    let mut items: Vec<(FeatId, &Value)> = b.items.iter().filter(|(_, v)| !v.is_none()).map(|(f, v)| (*f, v)).collect();
    items.sort_unstable_by_key(|(f, _)| *f);
    items
}

/// [`feature_diff`] over two pre-sorted specified-feature lists, by merging them.
fn merged_diff(a: &[(FeatId, &Value)], b: &[(FeatId, &Value)]) -> i64 {
    let (mut i, mut j, mut count) = (0, 0, 0);
    while i < a.len() && j < b.len() {
        match a[i].0.cmp(&b[j].0) {
            std::cmp::Ordering::Less => {
                count += 1;
                i += 1;
            }
            std::cmp::Ordering::Greater => {
                count += 1;
                j += 1;
            }
            std::cmp::Ordering::Equal => {
                count += i64::from(a[i].1 != b[j].1);
                i += 1;
                j += 1;
            }
        }
    }
    count + (a.len() - i) as i64 + (b.len() - j) as i64
}

/// Feature-weighted Damerau–Levenshtein: a substitution costs its feature difference, an indel
/// the segment's feature count, and a swap of two featurally identical segments the swap cost.
pub fn feature_edit_distance(a: &[Arc<FeatureBundle>], b: &[Arc<FeatureBundle>], transposition_cost: i64) -> i64 {
    let (n, m) = (a.len(), b.len());
    let sa: Vec<Vec<(FeatId, &Value)>> = a.iter().map(|x| sorted_specified(x)).collect();
    let sb: Vec<Vec<(FeatId, &Value)>> = b.iter().map(|x| sorted_specified(x)).collect();
    let diff: Vec<Vec<i64>> = sa.iter().map(|x| sb.iter().map(|y| merged_diff(x, y)).collect()).collect();
    let mut d = vec![vec![0i64; m + 1]; n + 1];
    for i in 1..=n {
        d[i][0] = d[i - 1][0] + sa[i - 1].len() as i64;
    }
    for j in 1..=m {
        d[0][j] = d[0][j - 1] + sb[j - 1].len() as i64;
    }
    for i in 1..=n {
        for j in 1..=m {
            d[i][j] = (d[i - 1][j] + sa[i - 1].len() as i64)
                .min(d[i][j - 1] + sb[j - 1].len() as i64)
                .min(d[i - 1][j - 1] + diff[i - 1][j - 1]);
            if i > 1 && j > 1 && diff[i - 1][j - 2] == 0 && diff[i - 2][j - 1] == 0 {
                d[i][j] = d[i][j].min(d[i - 2][j - 2] + transposition_cost);
            }
        }
    }
    d[n][m]
}

/// One word assessed at one stage.
#[derive(Clone, Debug)]
pub struct DistanceToTarget {
    pub gloss: String,
    pub ipa: String,
    pub derived: String,
    pub target: String,
    pub distance: i64,
    pub feature_distance: Option<i64>,
    pub frequency: i64,
    pub derived_phones: Vec<String>,
    pub target_phones: Vec<String>,
    pub matches_at: String,
    pub closest_at: String,
}

impl DistanceToTarget {
    pub fn exact(&self) -> bool {
        self.distance == 0
    }
}

#[derive(Clone, Debug, Default)]
pub struct AccuracyReport {
    pub distances: Vec<DistanceToTarget>,
}

impl AccuracyReport {
    pub fn assessed(&self) -> usize {
        self.distances.len()
    }

    pub fn exact(&self) -> usize {
        self.distances.iter().filter(|d| d.exact()).count()
    }

    pub fn within_one(&self) -> usize {
        self.distances.iter().filter(|d| d.distance <= 1).count()
    }

    pub fn accuracy(&self) -> f64 {
        if self.distances.is_empty() { 0.0 } else { self.exact() as f64 / self.assessed() as f64 }
    }

    pub fn mean_distance(&self) -> f64 {
        if self.distances.is_empty() {
            return 0.0;
        }
        self.distances.iter().map(|d| d.distance).sum::<i64>() as f64 / self.assessed() as f64
    }

    pub fn mean_feature_distance(&self) -> f64 {
        let with: Vec<i64> = self.distances.iter().filter_map(|d| d.feature_distance).collect();
        if with.is_empty() { 0.0 } else { with.iter().sum::<i64>() as f64 / with.len() as f64 }
    }

    pub fn frequencies_vary(&self) -> bool {
        self.distances.iter().any(|d| d.frequency != 1)
    }

    pub fn weight(&self) -> i64 {
        self.distances.iter().map(|d| d.frequency).sum()
    }

    pub fn weighted_accuracy(&self) -> f64 {
        let w = self.weight();
        if w == 0 {
            return 0.0;
        }
        self.distances.iter().filter(|d| d.exact()).map(|d| d.frequency).sum::<i64>() as f64 / w as f64
    }

    pub fn weighted_mean_distance(&self) -> f64 {
        let w = self.weight();
        if w == 0 {
            return 0.0;
        }
        self.distances.iter().map(|d| d.frequency * d.distance).sum::<i64>() as f64 / w as f64
    }

    pub fn weighted_mean_feature_distance(&self) -> f64 {
        let pairs: Vec<(i64, i64)> =
            self.distances.iter().filter_map(|d| d.feature_distance.map(|fd| (d.frequency, fd))).collect();
        let w: i64 = pairs.iter().map(|(f, _)| f).sum();
        if w == 0 {
            return 0.0;
        }
        pairs.iter().map(|(f, fd)| f * fd).sum::<i64>() as f64 / w as f64
    }
}

pub struct StageAccuracy {
    pub label: String,
    pub time: Option<i64>,
    pub report: AccuracyReport,
}

/// The `matches at` / `closest at` labels of *derived* across the word's attested targets.
fn cross_time_columns(derived: &Form, word: &Word, project: &Project) -> (String, String) {
    let swap = project.settings.accuracy.transposition_cost;
    let derived = comparable_bundles(derived);
    let mut times = word.stage_form_times();
    times.sort_unstable();
    let mut targets: Vec<(String, &Form)> =
        times.iter().map(|t| (t.to_string(), word.stage_form(*t).unwrap())).collect();
    if let Some(f) = word.final_form() {
        targets.push(("final".into(), f));
    }
    let mut matches = Vec::new();
    let mut best: Option<(i64, String)> = None;
    for (label, target) in targets {
        let fd = feature_edit_distance(&derived, &comparable_bundles(target), swap);
        if fd == 0 {
            matches.push(label.clone());
        }
        if best.as_ref().is_none_or(|(b, _)| fd < *b) {
            best = Some((fd, label));
        }
    }
    (matches.join(","), best.map(|(_, l)| l).unwrap_or_default())
}

#[allow(clippy::too_many_arguments)]
fn measure(word: &Word, derived_str: String, target_str: &str, derived: &Form, target: &Form, project: &Project, r: &Renderer) -> DistanceToTarget {
    let swap = project.settings.accuracy.transposition_cost;
    let (matches_at, closest_at) = cross_time_columns(derived, word, project);
    DistanceToTarget {
        gloss: word.gloss.clone(),
        ipa: word.ipa().to_string(),
        derived: derived_str,
        target: target_str.to_string(),
        distance: edit_distance(&phone_keys(derived), &phone_keys(target), swap),
        feature_distance: Some(feature_edit_distance(&comparable_bundles(derived), &comparable_bundles(target), swap)),
        frequency: word.frequency,
        derived_phones: form_phones(derived, r),
        target_phones: form_phones(target, r),
        matches_at,
        closest_at,
    }
}

pub fn distance_to_target(d: &Derivation, project: &Project, r: &Renderer) -> Option<DistanceToTarget> {
    let word = &d.word;
    let (Some(final_ipa), Some(final_form)) = (word.final_ipa(), word.final_form()) else { return None };
    let derived_str = r.syllabified(&lower_tiers(&d.surface), &d.surface_boundaries, true);
    Some(measure(word, derived_str, final_ipa, &d.surface, final_form, project, r))
}

pub fn measure_accuracy(derivations: &[Derivation], project: &Project, r: &Renderer) -> AccuracyReport {
    AccuracyReport { distances: derivations.par_iter().filter_map(|d| distance_to_target(d, project, r)).collect() }
}

/// Each attested stage, then the final, measured across the lexicon.
pub fn accuracy_by_stage(derivations: &[Derivation], project: &Project, r: &Renderer) -> Vec<StageAccuracy> {
    let mut times: Vec<i64> = derivations.iter().flat_map(|d| d.word.stages().into_iter().map(|(t, _)| t)).collect();
    times.sort_unstable();
    times.dedup();
    let mut stages = Vec::new();
    for time in times {
        let distances: Vec<DistanceToTarget> = derivations
            .par_iter()
            .filter_map(|d| {
                let target = d.word.stage_form(time)?;
                let (form, boundaries) = Engine::form_at_time(d, time);
                let derived_str = r.syllabified(&lower_tiers(&form), &boundaries, true);
                let target_str = d.word.stage_ipa(time).unwrap_or_default();
                Some(measure(&d.word, derived_str, target_str, &form, target, project, r))
            })
            .collect();
        stages.push(StageAccuracy { label: time.to_string(), time: Some(time), report: AccuracyReport { distances } });
    }
    stages.push(StageAccuracy { label: "final".into(), time: None, report: measure_accuracy(derivations, project, r) });
    stages
}
