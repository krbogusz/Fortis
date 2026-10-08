//! Rendering bundles back to IPA: a letter plus the diacritics that cover its differences, and
//! the suprasegmental marks placed per syllable.

use std::collections::HashMap;
use std::sync::{Arc, RwLock};

use super::combining::differing;
use super::matching::FeatSet;
use super::syllabifying::{Parts, syllabify_with, syllables};
use crate::models::*;

/// One segment's best spelling: the rendering (`�` when features are left over), the features
/// no spelling expresses, and the nearest spelling regardless.
pub struct Fit {
    pub text: String,
    pub residue: Vec<FeatId>,
    pub nearest: String,
}

pub struct Renderer<'p> {
    pub project: &'p Project,
    pub syllable_features: FeatSet,
    diacritics: Vec<&'p Diacritic>,
    nucleus: Option<&'p PatternBundle>,
    parts: Parts,
    cache: RwLock<HashMap<(BundleKey, bool), Arc<Fit>>>,
}

#[derive(Default)]
struct Marks {
    before: Vec<String>,
    combining: Vec<String>,
    after: Vec<String>,
}

impl Marks {
    fn push(&mut self, kind: DiacriticKind, symbol: &str) {
        match kind {
            DiacriticKind::Before => self.before.push(symbol.to_string()),
            DiacriticKind::Combining => self.combining.push(symbol.to_string()),
            DiacriticKind::After => self.after.push(symbol.to_string()),
        }
    }
}

impl<'p> Renderer<'p> {
    pub fn new(project: &'p Project) -> Renderer<'p> {
        Renderer {
            project,
            syllable_features: FeatSet::from_ids(project.syllable_features.iter().copied()),
            diacritics: project
                .diacritics
                .diacritics
                .iter()
                .filter(|d| !d.read_only && !d.bundle.is_empty())
                .collect(),
            nucleus: project.syllable_parts.nucleus_definition(Some(project.time)),
            parts: Parts::at(project, Some(project.time)),
            cache: RwLock::new(HashMap::new()),
        }
    }

    /// Greedily add the diacritic covering the most remaining differences, until none fits.
    fn find_diacritics(&self, target: &FeatureBundle, remaining: &mut Vec<FeatId>, marks: &mut Marks) {
        while !remaining.is_empty() {
            let mut best: Option<&Diacritic> = None;
            let mut best_coverage = 0;
            for d in &self.diacritics {
                let fits = d.bundle.items.iter().all(|(f, v)| target.get(*f).unwrap_or(&Value::NONE) == v);
                if !fits {
                    continue;
                }
                let coverage = d.bundle.keys().filter(|f| remaining.contains(f)).count();
                if coverage > best_coverage {
                    best = Some(d);
                    best_coverage = coverage;
                }
            }
            match best {
                Some(d) => {
                    remaining.retain(|f| !d.bundle.contains(*f));
                    marks.push(d.kind, &d.symbol);
                }
                None => {
                    if !self.render_contour(target, remaining, marks) {
                        break;
                    }
                }
            }
        }
    }

    /// Spell one remaining contour-valued feature as a sequence of its levels' contour marks.
    fn render_contour(&self, target: &FeatureBundle, remaining: &mut Vec<FeatId>, marks: &mut Marks) -> bool {
        for &feature in remaining.iter() {
            let Some(Value::Contour(levels)) = target.get(feature) else { continue };
            let mut sequence = Vec::new();
            for level in levels.iter() {
                let found = self.project.diacritics.diacritics.iter().find(|d| {
                    d.contour
                        && !d.read_only
                        && d.bundle.len() == 1
                        && d.bundle.items[0].0 == feature
                        && d.bundle.items[0].1 == Value::One(*level)
                });
                match found {
                    Some(d) => sequence.push(d),
                    None => break,
                }
            }
            if sequence.len() == levels.len() {
                for d in sequence {
                    marks.push(d.kind, &d.symbol);
                }
                remaining.retain(|f| *f != feature);
                return true;
            }
        }
        false
    }

    fn best_fit(&self, segment: &FeatureBundle, exclude: bool) -> Fit {
        let filtered;
        let segment = if exclude {
            filtered = FeatureBundle {
                items: segment.items.iter().filter(|(f, _)| !self.syllable_features.contains(*f)).cloned().collect(),
            };
            &filtered
        } else {
            segment
        };
        for letter in &self.project.letters.letters {
            if *segment == *letter.bundle {
                return Fit { text: letter.symbol.clone(), residue: Vec::new(), nearest: letter.symbol.clone() };
            }
        }
        let mut best: Option<(&Letter, usize, usize, Vec<FeatId>, Marks)> = None;
        for letter in &self.project.letters.letters {
            let total = differing(segment, &letter.bundle);
            let mut remaining = total.clone();
            let mut marks = Marks::default();
            self.find_diacritics(segment, &mut remaining, &mut marks);
            let better = match &best {
                None => true,
                Some((_, r, t, _, _)) => remaining.len() < *r || (remaining.len() == *r && total.len() < *t),
            };
            if better {
                best = Some((letter, remaining.len(), total.len(), remaining, marks));
            }
        }
        let Some((letter, _, _, mut residue, marks)) = best else {
            let mut residue: Vec<FeatId> = segment.keys().collect();
            residue.sort_unstable();
            return Fit { text: "�".into(), residue, nearest: "�".into() };
        };
        let nearest = format!(
            "{}{}{}{}",
            marks.before.concat(),
            letter.symbol,
            marks.combining.concat(),
            marks.after.concat()
        );
        residue.sort_unstable();
        let text = if residue.is_empty() { nearest.clone() } else { "�".into() };
        Fit { text, residue, nearest }
    }

    fn fit(&self, segment: &FeatureBundle, exclude: bool) -> Arc<Fit> {
        let key = (segment.key(), exclude);
        if let Some(hit) = self.cache.read().unwrap().get(&key) {
            return hit.clone();
        }
        let fit = Arc::new(self.best_fit(segment, exclude));
        self.cache.write().unwrap().insert(key, fit.clone());
        fit
    }

    /// One segment as IPA; with *exclude*, its syllable-tier features are left out.
    pub fn segment(&self, segment: &FeatureBundle, exclude: bool) -> String {
        if is_morpheme_boundary(segment) {
            return "-".into();
        }
        self.fit(segment, exclude).text.clone()
    }

    pub fn nearest(&self, segment: &FeatureBundle) -> String {
        self.fit(segment, false).nearest.clone()
    }

    pub fn residue(&self, segment: &FeatureBundle) -> Vec<FeatId> {
        if is_morpheme_boundary(segment) {
            return Vec::new();
        }
        self.fit(segment, false).residue.clone()
    }

    /// The sequence as IPA, with `.` at each interior syllable boundary (when *dots*) and the
    /// suprasegmental marks placed per syllable.
    pub fn syllabified(&self, sequence: &[Arc<FeatureBundle>], boundaries: &Boundaries, dots: bool) -> String {
        let n = sequence.len();
        let mut out = String::new();
        for syl in syllables(sequence, boundaries, self.nucleus) {
            let mut marks = Marks::default();
            if let Some(c) = syl.nucleus {
                let mut present: Vec<FeatId> =
                    sequence[c].keys().filter(|f| self.syllable_features.contains(*f)).collect();
                if !present.is_empty() {
                    self.find_diacritics(&sequence[c], &mut present, &mut marks);
                }
            }
            let marks_boundary =
                marks.before.iter().any(|s| self.project.diacritics.get(s).is_some_and(|d| d.marks_boundary));
            let interior = syl.start != 0 && syl.start != n && boundaries.contains(&syl.start);
            if dots && interior && !marks_boundary && !is_morpheme_boundary(&sequence[syl.start]) {
                out.push('.');
            }
            out.push_str(&marks.before.concat());
            for i in syl.start..syl.end {
                out.push_str(&self.segment(&sequence[i], true));
                if Some(i) == syl.nucleus {
                    out.push_str(&marks.combining.concat());
                }
            }
            out.push_str(&marks.after.concat());
        }
        out
    }

    /// A flat, re-segmentable string: syllabified for mark placement, without dots.
    pub fn sequence(&self, sequence: &[Arc<FeatureBundle>]) -> String {
        let (boundaries, _) = syllabify_with(sequence, &self.parts, self.project);
        if !boundaries.is_empty() {
            return self.syllabified(sequence, &boundaries, false);
        }
        sequence.iter().map(|s| self.segment(s, false)).collect()
    }

    /// `old→new` for each changed segment, or the differing region of a length change.
    pub fn describe_change(&self, before: &[Arc<FeatureBundle>], after: &[Arc<FeatureBundle>]) -> String {
        if before.len() == after.len() {
            let changed: Vec<String> = before
                .iter()
                .zip(after)
                .filter(|(b, a)| b != a)
                .map(|(b, a)| format!("{}→{}", self.segment(b, false), self.segment(a, false)))
                .collect();
            return changed.join(", ");
        }
        let mut head = 0;
        while head < before.len() && head < after.len() && before[head] == after[head] {
            head += 1;
        }
        let mut tail = 0;
        while tail < before.len() - head
            && tail < after.len() - head
            && before[before.len() - 1 - tail] == after[after.len() - 1 - tail]
        {
            tail += 1;
        }
        let side = |s: &[Arc<FeatureBundle>]| if s.is_empty() { "∅".to_string() } else { self.sequence(s) };
        format!(
            "{}→{}",
            side(&before[head..before.len() - tail]),
            side(&after[head..after.len() - tail])
        )
    }
}
