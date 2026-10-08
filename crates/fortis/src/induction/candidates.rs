//! Candidate rules for a correspondence, built as notation strings and parsed by the loader.

use std::collections::HashSet;

use indexmap::IndexMap;
use toml::{Table, Value as Toml};

use super::correspond::{ContextPredictor, Correspondence, render_feature_map};
use crate::engine::segmentation::string_to_sequence;
use crate::loaders::lexicon::load_rule;
use crate::models::*;

const NULL: &str = "∅";

#[derive(Clone)]
pub struct Candidate {
    pub definition: String,
    pub rules: Vec<Rule>,
}

fn segments(phone: &str, project: &Project) -> bool {
    phone == NULL || string_to_sequence(phone, project).is_ok()
}

pub fn parse_candidate(definition: &str, project: &Project) -> Option<Vec<Rule>> {
    let mut def = Table::new();
    def.insert("definition".into(), Toml::String(definition.to_string()));
    def.insert("time".into(), Toml::Integer(0));
    load_rule("candidate", &def, &project.features).ok()
}

fn context(p: &ContextPredictor) -> String {
    if p.side == "left" { format!("{} _", p.element) } else { format!("_ {}", p.element) }
}

/// The candidate lattice for one correspondence: unconditioned, single predictors, then pairs.
pub fn propose(c: &Correspondence, project: &Project) -> Vec<Candidate> {
    let (target, result) = match c.kind() {
        "substitution" => (c.got.clone().unwrap(), c.expected.clone().unwrap()),
        "insertion" => (c.got.clone().unwrap(), NULL.to_string()),
        _ => (NULL.to_string(), c.expected.clone().unwrap()),
    };
    if !segments(&target, project) || !segments(&result, project) {
        return Vec::new();
    }
    let mut definitions: Vec<String> = Vec::new();
    if c.kind() == "substitution" {
        definitions.push(format!("{target} → {result}"));
    }
    for p in &c.predictors {
        definitions.push(format!("{target} → {result} / {}", context(p)));
    }
    let lefts: Vec<&ContextPredictor> = c.predictors.iter().filter(|p| p.side == "left").collect();
    let rights: Vec<&ContextPredictor> = c.predictors.iter().filter(|p| p.side == "right").collect();
    for left in lefts.iter().take(3) {
        for right in rights.iter().take(3) {
            definitions.push(format!("{target} → {result} / {} _ {}", left.element, right.element));
        }
    }
    let cap = project.settings.induction.contexts_per_confusion as usize;
    let mut out = Vec::new();
    let mut seen = HashSet::new();
    for definition in definitions {
        if !seen.insert(definition.clone()) {
            continue;
        }
        if let Some(rules) = parse_candidate(&definition, project) {
            out.push(Candidate { definition, rules });
        }
        if out.len() >= cap {
            break;
        }
    }
    out
}

/// Natural-class candidates: substitutions sharing one feature delta fused into one class rule.
pub fn class_candidates(corrs: &[Correspondence], project: &Project) -> Vec<Candidate> {
    let mut groups: IndexMap<Vec<(String, Value)>, Vec<&Correspondence>> = IndexMap::new();
    for c in corrs {
        if c.kind() != "substitution" || c.feature_delta.is_empty() {
            continue;
        }
        groups.entry(c.feature_delta.clone()).or_default().push(c);
    }
    let mut out = Vec::new();
    for (delta, members) in groups {
        if members.len() < 2 {
            continue;
        }
        let maps: Vec<&Vec<(String, Value)>> = members.iter().map(|m| &m.got_features).collect();
        let source: Vec<(String, Value)> = if maps.iter().any(|m| m.is_empty()) {
            Vec::new()
        } else {
            let mut shared: Vec<(String, Value)> = maps[0]
                .iter()
                .filter(|(f, v)| maps[1..].iter().all(|m| m.iter().find(|(g, _)| g == f).map(|(_, w)| w) == Some(v)))
                .cloned()
                .collect();
            shared.sort_by(|a, b| a.0.cmp(&b.0));
            shared
        };
        let (Some(source), Some(result)) =
            (render_feature_map(&source, &project.features), render_feature_map(&delta, &project.features))
        else {
            continue;
        };
        let definition = format!("{source} → {result}");
        if let Some(rules) = parse_candidate(&definition, project) {
            out.push(Candidate { definition, rules });
        }
    }
    out
}
