//! Syllabification: nuclei from the nucleus pattern, then each intervocalic cluster split by the
//! onset/coda patterns or, without them, by sonority under the Maximal Onset Principle.

use std::sync::Arc;

use super::matching::{full_match, matches_plain};
use crate::models::*;

/// The syllables of *segments* under *boundaries* (the word edges are always edges).
pub fn syllables(segments: &[Arc<FeatureBundle>], boundaries: &Boundaries, nucleus: Option<&PatternBundle>) -> Vec<Syllable> {
    let mut edges: Vec<usize> = boundaries.iter().copied().collect();
    edges.push(0);
    edges.push(segments.len());
    edges.sort_unstable();
    edges.dedup();
    edges
        .windows(2)
        .map(|w| {
            let nucleus = nucleus.and_then(|n| (w[0]..w[1]).find(|&i| matches_plain(n, &segments[i])));
            Syllable { start: w[0], end: w[1], nucleus }
        })
        .collect()
}

pub fn sonority(segment: &FeatureBundle, sonorities: &[Sonority]) -> i64 {
    sonorities
        .iter()
        .find(|s| s.bundle.as_ref().is_some_and(|b| matches_plain(b, segment)))
        .map_or(0, |s| s.level)
}

fn onset_start(cluster: &[i64]) -> usize {
    if cluster.is_empty() {
        return 0;
    }
    let mut start = cluster.len() - 1;
    while start > 0 && cluster[start - 1] < cluster[start] {
        start -= 1;
    }
    start
}

fn legal(segments: &[Arc<FeatureBundle>], part: Option<&Arc<SyllablePart>>, project: &Project) -> bool {
    match part.and_then(|p| p.pattern.as_ref()) {
        None => true,
        Some(pattern) => full_match(pattern, segments, &project.letters, &project.features),
    }
}

/// The syllable parts in force at a time: nucleus, onset, coda.
#[derive(Clone)]
pub struct Parts {
    pub nucleus: Option<Arc<SyllablePart>>,
    pub onset: Option<Arc<SyllablePart>>,
    pub coda: Option<Arc<SyllablePart>>,
}

impl Parts {
    pub fn at(project: &Project, time: Option<i64>) -> Parts {
        let sp = &project.syllable_parts;
        Parts {
            nucleus: sp.get_nucleus(time).cloned(),
            onset: sp.get_part(time, "onset").cloned(),
            coda: sp.get_part(time, "coda").cloned(),
        }
    }

    /// An identity key for the parts, so a cache keyed on it is exact.
    pub fn key(&self) -> [usize; 3] {
        let ptr = |p: &Option<Arc<SyllablePart>>| p.as_ref().map_or(0, |a| Arc::as_ptr(a) as usize);
        [ptr(&self.nucleus), ptr(&self.onset), ptr(&self.coda)]
    }

    pub fn nucleus_definition(&self) -> Option<&PatternBundle> {
        self.nucleus.as_ref().and_then(|n| n.definition.as_ref())
    }
}

/// The boundaries of *segments*, and the clusters whose division fell back to sonority.
pub fn syllabify_with(segments: &[Arc<FeatureBundle>], parts: &Parts, project: &Project) -> (Boundaries, Vec<(usize, usize)>) {
    let Some(definition) = parts.nucleus_definition() else {
        return (Boundaries::new(), Vec::new());
    };
    let nuclei: Vec<usize> = (0..segments.len()).filter(|&i| matches_plain(definition, &segments[i])).collect();
    if nuclei.is_empty() {
        return (Boundaries::new(), Vec::new());
    }
    let has_pattern = |p: &Option<Arc<SyllablePart>>| p.as_ref().is_some_and(|p| p.pattern.is_some());
    let patterned = has_pattern(&parts.onset) || has_pattern(&parts.coda);
    let mut boundaries = Boundaries::new();
    boundaries.insert(0);
    boundaries.insert(segments.len());
    let mut fallbacks = Vec::new();
    for w in nuclei.windows(2) {
        let (left, right) = (w[0], w[1]);
        let splits: Vec<usize> = (left + 1..right).filter(|&j| is_morpheme_boundary(&segments[j])).collect();
        if !splits.is_empty() {
            boundaries.extend(splits);
            continue;
        }
        let cluster = &segments[left + 1..right];
        let levels = || cluster.iter().map(|s| sonority(s, &project.sonorities)).collect::<Vec<i64>>();
        let (start, fell_back) = if !patterned {
            (onset_start(&levels()), false)
        } else {
            match (0..=cluster.len()).find(|&k| {
                legal(&cluster[k..], parts.onset.as_ref(), project) && legal(&cluster[..k], parts.coda.as_ref(), project)
            }) {
                Some(k) => (k, false),
                None => (onset_start(&levels()), true),
            }
        };
        boundaries.insert(left + 1 + start);
        if fell_back {
            fallbacks.push((left + 1, right));
        }
    }
    (boundaries, fallbacks)
}

pub fn syllabify(segments: &[Arc<FeatureBundle>], project: &Project, time: Option<i64>) -> Boundaries {
    syllabify_with(segments, &Parts::at(project, time), project).0
}

pub fn syllabification_fallbacks(segments: &[Arc<FeatureBundle>], project: &Project, time: Option<i64>) -> Vec<(usize, usize)> {
    syllabify_with(segments, &Parts::at(project, time), project).1
}

/// For each position, the nucleus bundle of its syllable.
pub fn nuclei_by_position(segments: &[Arc<FeatureBundle>], boundaries: &Boundaries, nucleus: &PatternBundle) -> Vec<Option<Arc<FeatureBundle>>> {
    let mut nuclei = vec![None; segments.len()];
    for syl in syllables(segments, boundaries, Some(nucleus)) {
        if let Some(n) = syl.nucleus {
            for slot in &mut nuclei[syl.start..syl.end] {
                *slot = Some(segments[n].clone());
            }
        }
    }
    nuclei
}
