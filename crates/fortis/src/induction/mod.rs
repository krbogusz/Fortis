//! Supervised rule induction: recover a sound-change cascade from a project's attested targets
//! by greedy MDL boosting, interval by interval.

pub mod boost;
pub mod candidates;
pub mod correspond;
pub mod evaluate;
pub mod intervals;
pub mod objective;
pub mod refine;
pub mod report;

use crate::engine::deriving::Engine;
use crate::engine::rendering::Renderer;
use crate::engine::tiers::lower_tiers;
use crate::models::*;
use objective::{CascadeScore, cascade_score};
use report::Scoreboard;

fn score(project: &Project) -> CascadeScore {
    let mut derivations = Engine::new(project).expect("rules resolve").derive_all().expect("words segment");
    cascade_score(&mut derivations, project, &Renderer::new(project))
}

/// The project with each word's targets replaced by the hand cascade's own output.
pub fn synthetic_project(project: &Project) -> Project {
    let derivations = Engine::new(project).expect("rules resolve").derive_all().expect("words segment");
    let r = Renderer::new(project);
    let render_at = |d: &Derivation, time: Option<i64>| match time {
        None => r.syllabified(&lower_tiers(&d.surface), &d.surface_boundaries, true),
        Some(t) => {
            let (form, boundaries) = Engine::form_at_time(d, t);
            r.syllabified(&lower_tiers(&form), &boundaries, true)
        }
    };
    let mut words = WordInventory::new();
    for (d, (key, word)) in derivations.iter().zip(&project.words) {
        let mut times: Vec<i64> = word.stages().into_iter().map(|(t, _)| t).collect();
        times.sort_unstable();
        let mut forms = vec![(word.seed_time(), Attestation { ipa: word.ipa().to_string(), ..Default::default() })];
        for t in times {
            forms.push((Some(t), Attestation { ipa: render_at(d, Some(t)), ..Default::default() }));
        }
        forms.push((None, Attestation { ipa: render_at(d, None), ..Default::default() }));
        words.insert(
            key.clone(),
            Word { id: word.id.clone(), forms, gloss: word.gloss.clone(), frequency: word.frequency, note: String::new() },
        );
    }
    Project { words, ..project.clone() }
}

pub fn compute_scoreboard(project: &Project) -> Scoreboard {
    let identity = Project { rules: RuleInventory::default(), ..project.clone() };
    let synth = synthetic_project(project);
    let synth_identity = Project { rules: RuleInventory::default(), ..synth.clone() };
    Scoreboard {
        real_identity: score(&identity),
        real_hand: score(project),
        synthetic_identity: score(&synth_identity),
        synthetic_hand: score(&synth),
    }
}
