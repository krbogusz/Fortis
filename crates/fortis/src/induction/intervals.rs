//! The attested stage times split the cascade into intervals; each interval is a mini-project
//! whose words map the attested earlier form to the attested later one (teacher forcing).

use crate::engine::segmentation::string_to_sequence;
use crate::models::*;

pub struct Interval {
    pub start: Option<i64>,
    pub end: Option<i64>,
    pub project: Project,
}

impl Interval {
    pub fn label(&self) -> String {
        interval_label(self.start, self.end)
    }
}

pub fn interval_label(start: Option<i64>, end: Option<i64>) -> String {
    let s = start.map_or("input".to_string(), |t| t.to_string());
    let e = end.map_or("final".to_string(), |t| t.to_string());
    format!("{s}→{e}")
}

pub fn stage_times(project: &Project) -> Vec<i64> {
    let mut times: Vec<i64> = project.words.values().flat_map(|w| w.stages().into_iter().map(|(t, _)| t)).collect();
    times.sort_unstable();
    times.dedup();
    times
}

/// A word whose seed is *source* at time 0 and whose surface target is *target*.
pub fn series_word(source: &str, gloss: &str, target: &str, frequency: i64) -> Word {
    Word {
        id: source.to_string(),
        forms: vec![
            (Some(0), Attestation { ipa: source.to_string(), ..Default::default() }),
            (None, Attestation { ipa: target.to_string(), ..Default::default() }),
        ],
        gloss: gloss.to_string(),
        frequency,
        note: String::new(),
    }
}

/// The project with its lexicon replaced and its rules emptied.
pub fn mini_project(project: &Project, words: WordInventory) -> Project {
    Project { words, rules: RuleInventory::default(), ..project.clone() }
}

pub fn build_interval(project: &Project, start: Option<i64>, end: Option<i64>) -> Interval {
    let mut mini = WordInventory::new();
    for word in project.words.values() {
        let source = match start {
            None => Some(word.ipa()),
            Some(t) => word.stage_ipa(t),
        };
        let target = match end {
            None => word.final_ipa(),
            Some(t) => word.stage_ipa(t),
        };
        let (Some(source), Some(target)) = (source, target) else { continue };
        if string_to_sequence(source, project).is_err() {
            continue;
        }
        mini.insert(source.to_string(), series_word(source, &word.gloss, target, word.frequency));
    }
    Interval { start, end, project: mini_project(project, mini) }
}

pub fn build_intervals(project: &Project) -> Vec<Interval> {
    let mut checkpoints: Vec<Option<i64>> = vec![None];
    checkpoints.extend(stage_times(project).into_iter().map(Some));
    checkpoints.push(None);
    checkpoints.windows(2).map(|w| build_interval(project, w[0], w[1])).collect()
}
