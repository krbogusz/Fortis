//! The core derivation reports: the long trace, the word × rule matrix, and the per-rule firings.

use indexmap::IndexMap;
use rayon::prelude::*;

use crate::analysis::dependencies::base_id;
use crate::engine::rendering::Renderer;
use crate::engine::tiers::lower_tiers;
use crate::models::*;
use crate::py::{Cell, CsvWriter};

fn time_cell(t: Option<i64>) -> Cell {
    match t {
        Some(t) => Cell::Int(t),
        None => Cell::Text(String::new()),
    }
}

/// `derivations.csv`: one row per word × firing rule, bookended by `input` and `output`.
pub fn derivations_csv(derivations: &[Derivation], r: &Renderer) -> String {
    let blocks: Vec<String> = derivations
        .par_iter()
        .map(|d| {
            let mut w = CsvWriter::new();
            let name = &d.word.id;
            let input_boundaries = d.steps.first().map_or(&d.surface_boundaries, |s| &s.before_boundaries);
            let ingested = r.syllabified(&lower_tiers(&d.input), input_boundaries, true);
            w.row([name.as_str(), "input", "", d.word.ipa(), &ingested, ""]);
            for step in &d.steps {
                let before = lower_tiers(&step.before);
                let after = lower_tiers(&step.after);
                let label = step.rule.name.clone().unwrap_or_else(|| base_id(&step.rule.id).to_string());
                w.row([
                    Cell::from(name),
                    Cell::from(label),
                    time_cell(step.rule.time),
                    Cell::from(r.syllabified(&before, &step.before_boundaries, true)),
                    Cell::from(r.syllabified(&after, &step.after_boundaries, true)),
                    Cell::from(r.describe_change(&before, &after)),
                ]);
            }
            let surface = r.syllabified(&lower_tiers(&d.surface), &d.surface_boundaries, true);
            w.row([name.as_str(), "output", "", "", &surface, ""]);
            w.out
        })
        .collect();
    let mut w = CsvWriter::new();
    w.row(["word", "rule", "t", "before", "after", "change"]);
    w.out + &blocks.concat()
}

/// Each rule once (sub-rules merged), in firing order: `(base id, rule)`.
fn rule_bases(rules: &RuleInventory) -> Vec<(String, std::sync::Arc<Rule>)> {
    let mut seen: IndexMap<String, std::sync::Arc<Rule>> = IndexMap::new();
    for rule in rules.in_order() {
        seen.entry(base_id(&rule.id).to_string()).or_insert(rule);
    }
    seen.into_iter().collect()
}

/// `(base id, column title)` per rule: `<time>: <name>`, or the name for an untimed rule.
pub fn rule_columns(rules: &RuleInventory) -> Vec<(String, String)> {
    rule_bases(rules)
        .into_iter()
        .map(|(base, rule)| {
            let label = rule.name.clone().unwrap_or_else(|| base.clone());
            let title = match rule.time {
                Some(t) => format!("{t}: {label}"),
                None => label,
            };
            (base, title)
        })
        .collect()
}

/// `rule_firings.csv`: one row per rule with its count, distinct changes and matched words.
pub fn rule_firings_csv(derivations: &[Derivation], rules: &RuleInventory, r: &Renderer) -> String {
    let per_word: Vec<Vec<(String, String, String)>> = derivations
        .par_iter()
        .map(|d| {
            d.steps
                .iter()
                .map(|step| {
                    let before = lower_tiers(&step.before);
                    let after = lower_tiers(&step.after);
                    let b = r.syllabified(&before, &step.before_boundaries, true);
                    let a = r.syllabified(&after, &step.after_boundaries, true);
                    (base_id(&step.rule.id).to_string(), format!("{b} → {a}"), r.describe_change(&before, &after))
                })
                .collect()
        })
        .collect();
    let mut matched: IndexMap<String, Vec<String>> = IndexMap::new();
    let mut changes: IndexMap<String, IndexMap<String, ()>> = IndexMap::new();
    for (base, firing, change) in per_word.into_iter().flatten() {
        matched.entry(base.clone()).or_default().push(firing);
        for delta in change.split(", ") {
            if !delta.is_empty() {
                changes.entry(base.clone()).or_default().insert(delta.to_string(), ());
            }
        }
    }
    let mut w = CsvWriter::new();
    w.row(["rule", "t", "sporadic", "count", "changes", "matched"]);
    for (base, rule) in rule_bases(rules) {
        let firings = matched.get(&base).cloned().unwrap_or_default();
        let deltas: Vec<String> = changes.get(&base).map(|c| c.keys().cloned().collect()).unwrap_or_default();
        w.row([
            Cell::from(rule.name.clone().unwrap_or(base.clone())),
            time_cell(rule.time),
            Cell::from(rule.words.join(", ")),
            Cell::from(firings.len()),
            Cell::from(deltas.join(", ")),
            Cell::from(firings.join(", ")),
        ]);
    }
    w.out
}

/// `derivation_matrix.csv`: one row per word, one column per rule, the form after it fired.
pub fn matrix_csv(derivations: &[Derivation], rules: &RuleInventory, r: &Renderer) -> String {
    let columns = rule_columns(rules);
    let mut w = CsvWriter::new();
    let mut header = vec!["ipa".to_string(), "gloss".to_string()];
    header.extend(columns.iter().map(|(_, title)| title.clone()));
    w.row(header);
    let rows: Vec<String> = derivations
        .par_iter()
        .map(|d| {
            let mut after_by_base: std::collections::HashMap<&str, String> = std::collections::HashMap::new();
            for step in &d.steps {
                after_by_base
                    .insert(base_id(&step.rule.id), r.syllabified(&lower_tiers(&step.after), &step.after_boundaries, true));
            }
            let mut row = vec![d.word.ipa().to_string(), d.word.gloss.clone()];
            row.extend(columns.iter().map(|(base, _)| after_by_base.get(base.as_str()).cloned().unwrap_or_default()));
            let mut line = CsvWriter::new();
            line.row(row);
            line.out
        })
        .collect();
    w.out + &rows.concat()
}
