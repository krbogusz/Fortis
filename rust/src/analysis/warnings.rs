//! Warnings for what the engine does silently: syllabification that fell back to sonority, and
//! segments no letter can spell.

use std::collections::HashSet;

use indexmap::IndexMap;

use crate::engine::rendering::Renderer;
use crate::engine::syllabifying::{Parts, syllabify_with};
use crate::engine::tiers::lower_tiers;
use crate::models::*;

pub struct SyllabificationWarning {
    pub ipa: String,
    pub gloss: String,
    pub form: String,
    pub clusters: Vec<String>,
    pub syllabified: String,
}

pub fn syllabification_warnings(derivations: &[Derivation], project: &Project, r: &Renderer) -> Vec<SyllabificationWarning> {
    let latest = project.rules.by_time.keys().flatten().copied().max().unwrap_or(0);
    let input_parts = Parts::at(project, Some(project.time));
    let surface_parts = Parts::at(project, Some(latest));
    let mut out = Vec::new();
    let mut seen: HashSet<(String, Vec<String>, String)> = HashSet::new();
    for d in derivations {
        for (form, parts) in [(&d.input, &input_parts), (&d.surface, &surface_parts)] {
            let bundles = lower_tiers(form);
            let (boundaries, spans) = syllabify_with(&bundles, parts, project);
            if spans.is_empty() {
                continue;
            }
            let clusters: Vec<String> = spans
                .iter()
                .map(|(s, e)| bundles[*s..*e].iter().map(|b| r.segment(b, false)).collect())
                .collect();
            let warning = SyllabificationWarning {
                ipa: d.word.ipa().to_string(),
                gloss: d.word.gloss.clone(),
                form: r.syllabified(&bundles, &boundaries, false),
                clusters,
                syllabified: r.syllabified(&bundles, &boundaries, true),
            };
            let key = (warning.ipa.clone(), warning.clusters.clone(), warning.syllabified.clone());
            if seen.insert(key) {
                out.push(warning);
            }
        }
    }
    out
}

pub struct RenderingWarning {
    pub nearest: String,
    pub dropped: Vec<String>,
    pub rule: String,
    pub words: Vec<String>,
    pub count: usize,
}

pub fn rendering_warnings(derivations: &[Derivation], project: &Project, r: &Renderer) -> Vec<RenderingWarning> {
    let mut found: IndexMap<(String, Vec<String>), (usize, Vec<String>, String)> = IndexMap::new();
    let names = |residue: &[FeatId]| {
        let mut n: Vec<String> = residue.iter().map(|f| project.features.name(*f).to_string()).collect();
        n.sort();
        n
    };
    let mut note = |bundle: &FeatureBundle, rule: &str, gloss: &str| {
        let residue = r.residue(bundle);
        if residue.is_empty() {
            return;
        }
        let entry = found.entry((r.nearest(bundle), names(&residue))).or_insert((0, Vec::new(), rule.to_string()));
        entry.0 += 1;
        if !entry.1.iter().any(|g| g == gloss) && entry.1.len() < 3 {
            entry.1.push(gloss.to_string());
        }
    };
    for d in derivations {
        let gloss = if d.word.gloss.is_empty() { d.word.ipa() } else { d.word.gloss.as_str() };
        for segment in lower_tiers(&d.input) {
            note(&segment, "input", gloss);
        }
        for step in &d.steps {
            let already: HashSet<Vec<FeatId>> = lower_tiers(&step.before).iter().map(|s| r.residue(s)).collect();
            let rule = step.rule.name.as_deref().unwrap_or("None");
            for segment in lower_tiers(&step.after) {
                if !already.contains(&r.residue(&segment)) {
                    note(&segment, rule, gloss);
                }
            }
        }
    }
    let mut out: Vec<RenderingWarning> = found
        .into_iter()
        .map(|((nearest, dropped), (count, words, rule))| RenderingWarning { nearest, dropped, rule, words, count })
        .collect();
    out.sort_by(|a, b| b.count.cmp(&a.count).then_with(|| a.nearest.cmp(&b.nearest)).then_with(|| a.rule.cmp(&b.rule)));
    out
}

pub fn warnings_summary_line(warnings: &[SyllabificationWarning], rendering: &[RenderingWarning]) -> String {
    let mut parts = Vec::new();
    if !warnings.is_empty() {
        let words: HashSet<&str> = warnings.iter().map(|w| w.ipa.as_str()).collect();
        parts.push(format!(
            "⚠ {} word(s) fell back to sonority syllabification (onset/coda patterns admitted no split)",
            words.len()
        ));
    }
    if let Some(worst) = rendering.first() {
        let sites: usize = rendering.iter().map(|w| w.count).sum();
        parts.push(format!(
            "⚠ {} unspellable segment(s), {sites} site(s) — no letter can express them, so they render as �; worst: nearest '{}' loses {} from '{}'",
            rendering.len(),
            worst.nearest,
            worst.dropped.join("/"),
            worst.rule
        ));
    }
    if parts.is_empty() {
        return "no warnings".into();
    }
    format!("{} — see warnings.md", parts.join(" · "))
}

pub fn render_warnings(warnings: &[SyllabificationWarning], where_: &str, rendering: &[RenderingWarning]) -> String {
    let mut lines: Vec<String> = vec![format!("# Warnings — {where_}"), String::new()];
    if !rendering.is_empty() {
        for line in [
            "## Unspellable segments",
            "",
            "These segments carry features **no letter can express**, so they render as `�`.",
            "",
            "They used to render as the nearest letter, with the leftover features silently",
            "dropped — which made the one failure the engine cannot otherwise show you invisible.",
            "A bundle one feature away from `ɑ` printed as a perfectly ordinary `ɑ`, and yet **no",
            "rule written `ɑ → …` would ever match it**, because rendering is lossy and",
            "many-to-one while a letter PATTERN matches by exact identity. The rule fired on some",
            "words and passed silently over identical-looking others, with no error anywhere.",
            "",
            "The **mistaken for** column is the letter each one is a near-miss of — the letter it",
            "used to print as, and the letter whose rules will not match it.",
            "",
            "The usual cause is in the **rule named below**: a merge changed a segment's quality",
            "and left a feature of the old quality behind. A merge keeps every feature it does not",
            "mention, so un-rounding `o` with `rounded: none` and forgetting `labial: none` leaves",
            "an `ɑ` that is still labial. Clear the whole set of features that go with the quality",
            "you are changing (`rounded` **and** `labial`; `front` **and** `back`) — or, if the",
            "segment is real, add a letter or diacritic that can spell it.",
            "",
            "| renders as | mistaken for | features it carries that the letter cannot | produced by | sites | examples |",
            "| --- | --- | --- | --- | --- | --- |",
        ] {
            lines.push(line.to_string());
        }
        for w in rendering {
            let dropped: Vec<String> = w.dropped.iter().map(|f| format!("`{f}`")).collect();
            lines.push(format!(
                "| `�` | `{}` | {} | `{}` | {} | {} |",
                w.nearest,
                dropped.join(", "),
                w.rule,
                w.count,
                w.words.join(", ")
            ));
        }
        lines.push(String::new());
    }
    for line in [
        "## Syllabification fallback",
        "",
        "Syllabification fell back to the **sonority Maximal Onset** division for the words",
        "below: the project's onset/coda patterns admitted no legal split for the listed",
        "cluster, so the sonority-based division was used instead (rather than leaving the",
        "word unsyllabified). Loosen the onset/coda patterns to cover these clusters, or",
        "accept the sonority fallback.",
        "",
    ] {
        lines.push(line.to_string());
    }
    if warnings.is_empty() {
        lines.push("No syllabification fell back — every word matched the onset/coda patterns.".into());
    } else {
        lines.push("| word | gloss | form | cluster | syllabified as |".into());
        lines.push("| --- | --- | --- | --- | --- |".into());
        for w in warnings {
            let clusters: Vec<String> = w.clusters.iter().map(|c| format!("`{c}`")).collect();
            lines.push(format!(
                "| `{}` | {} | `{}` | {} | `{}` |",
                w.ipa,
                w.gloss,
                w.form,
                clusters.join(", "),
                w.syllabified
            ));
        }
    }
    format!("{}\n", lines.join("\n").trim_end())
}
