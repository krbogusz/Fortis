//! The rule feeding graph, read off the firings: a firing depends on the latest earlier firing
//! in the same word that produced a segment it consumed.

use std::collections::{BTreeSet, HashMap};

use indexmap::IndexMap;
use rayon::prelude::*;

use crate::engine::rendering::Renderer;
use crate::engine::tiers::lower_tiers;
use crate::models::*;
use crate::py::Json;

pub struct RuleNode {
    pub index: usize,
    pub id: String,
    pub name: String,
    pub time: Option<i64>,
    pub requires: Vec<String>,
    pub produces: Vec<String>,
    pub deps: Vec<usize>,
    pub depth: usize,
}

pub struct DependencyGraph {
    pub nodes: Vec<RuleNode>,
    /// `(dependent, dependency)` pairs.
    pub edges: Vec<(usize, usize)>,
}

/// A rule id without its list-definition suffix (`name#2` → `name`).
pub fn base_id(id: &str) -> &str {
    if let Some(i) = id.rfind('#') {
        let suffix = &id[i + 1..];
        if !suffix.is_empty() && suffix.chars().all(|c| c.is_ascii_digit()) {
            return &id[..i];
        }
    }
    id
}

fn change(before: &[std::sync::Arc<FeatureBundle>], after: &[std::sync::Arc<FeatureBundle>], r: &Renderer) -> (BTreeSet<String>, BTreeSet<String>) {
    let mut consumed = BTreeSet::new();
    let mut produced = BTreeSet::new();
    for delta in r.describe_change(before, after).split(", ") {
        let (left, right) = delta.split_once('→').unwrap_or((delta, ""));
        if !left.is_empty() && left != "∅" {
            consumed.insert(left.to_string());
        }
        if !right.is_empty() && right != "∅" {
            produced.insert(right.to_string());
        }
    }
    (consumed, produced)
}

pub fn build_dependency_graph(derivations: &[Derivation], rules: &RuleInventory, r: &Renderer) -> DependencyGraph {
    let mut index: HashMap<String, usize> = HashMap::new();
    let mut meta: Vec<(String, String, Option<i64>)> = Vec::new();
    for rule in rules.in_order() {
        let base = base_id(&rule.id).to_string();
        if !index.contains_key(&base) {
            index.insert(base.clone(), meta.len());
            meta.push((base.clone(), rule.name.clone().unwrap_or(base), rule.time));
        }
    }
    let mut requires: Vec<BTreeSet<String>> = vec![BTreeSet::new(); meta.len()];
    let mut produces: Vec<BTreeSet<String>> = vec![BTreeSet::new(); meta.len()];
    let mut edge_via: IndexMap<(usize, usize), ()> = IndexMap::new();
    let changes: Vec<Vec<Option<(usize, BTreeSet<String>, BTreeSet<String>)>>> = derivations
        .par_iter()
        .map(|d| {
            d.steps
                .iter()
                .map(|step| {
                    let &i = index.get(base_id(&step.rule.id))?;
                    let (required, produced) = change(&lower_tiers(&step.before), &lower_tiers(&step.after), r);
                    Some((i, required, produced))
                })
                .collect()
        })
        .collect();
    for steps in changes {
        let mut producer: HashMap<String, usize> = HashMap::new();
        for (i, required, produced) in steps.into_iter().flatten() {
            for value in &required {
                if let Some(&source) = producer.get(value)
                    && source != i && source < i {
                        edge_via.insert((i, source), ());
                    }
            }
            for value in &produced {
                producer.insert(value.clone(), i);
            }
            requires[i].extend(required);
            produces[i].extend(produced);
        }
    }
    let mut deps: Vec<BTreeSet<usize>> = vec![BTreeSet::new(); meta.len()];
    let edges: Vec<(usize, usize)> = edge_via.keys().copied().collect();
    for &(dependent, dependency) in &edges {
        deps[dependent].insert(dependency);
    }
    let mut depth = vec![0usize; meta.len()];
    for i in 0..meta.len() {
        depth[i] = deps[i].iter().map(|&d| depth[d] + 1).max().unwrap_or(0);
    }
    let nodes = meta
        .into_iter()
        .enumerate()
        .map(|(i, (id, name, time))| RuleNode {
            index: i,
            id,
            name,
            time,
            requires: requires[i].iter().cloned().collect(),
            produces: produces[i].iter().cloned().collect(),
            deps: deps[i].iter().copied().collect(),
            depth: depth[i],
        })
        .collect();
    DependencyGraph { nodes, edges }
}

const TEMPLATE: &str = include_str!("dependencies.html");

pub fn render_dependency_html(graph: &DependencyGraph) -> String {
    let (sub_w, row_h, pad_x, pad_y, gap) = (150.0f64, 16i64, 60.0f64, 80i64, 34.0f64);
    let nodes = &graph.nodes;
    let mut column = vec![0usize; nodes.len()];
    for n in nodes {
        column[n.index] = n
            .deps
            .iter()
            .filter(|&&d| nodes[d].time == n.time)
            .map(|&d| column[d] + 1)
            .max()
            .unwrap_or(0);
    }
    let mut times: Vec<Option<i64>> = nodes.iter().map(|n| n.time).collect();
    times.sort_by_key(|t| time_order(*t));
    times.dedup();
    let mut max_col: HashMap<Option<i64>, usize> = times.iter().map(|t| (*t, 0)).collect();
    for n in nodes {
        let entry = max_col.get_mut(&n.time).unwrap();
        *entry = (*entry).max(column[n.index]);
    }
    let mut base_x: HashMap<Option<i64>, f64> = HashMap::new();
    let mut cursor = pad_x;
    for t in &times {
        base_x.insert(*t, cursor);
        cursor += (max_col[t] + 1) as f64 * sub_w + gap;
    }
    let mut positions = vec![(0.0f64, 0i64); nodes.len()];
    let mut stack: IndexMap<(Option<i64>, usize), i64> = IndexMap::new();
    for n in nodes {
        let col = column[n.index];
        let row = stack.get(&(n.time, col)).copied().unwrap_or(0);
        positions[n.index] = (base_x[&n.time] + col as f64 * sub_w, pad_y + row * row_h);
        stack.insert((n.time, col), row + 1);
    }
    let strings = |v: &[String]| Json::List(v.iter().map(|s| Json::Str(s.clone())).collect());
    let node_json: Vec<Json> = nodes
        .iter()
        .map(|n| {
            Json::Obj(vec![
                ("i".into(), Json::Int(n.index as i64)),
                ("id".into(), Json::Str(n.id.clone())),
                ("name".into(), Json::Str(n.name.clone())),
                ("t".into(), n.time.map_or(Json::Null, Json::Int)),
                ("depth".into(), Json::Int(n.depth as i64)),
                ("x".into(), Json::Float(positions[n.index].0)),
                ("y".into(), Json::Int(positions[n.index].1)),
                ("requires".into(), strings(&n.requires)),
                ("produces".into(), strings(&n.produces)),
                ("deps".into(), Json::List(n.deps.iter().map(|&d| Json::Int(d as i64)).collect())),
            ])
        })
        .collect();
    let edge_json: Vec<Json> = graph
        .edges
        .iter()
        .map(|&(from, to)| Json::Obj(vec![("from".into(), Json::Int(from as i64)), ("to".into(), Json::Int(to as i64))]))
        .collect();
    let bands: Vec<Json> = times
        .iter()
        .map(|t| {
            Json::Obj(vec![
                ("x0".into(), Json::Float(base_x[t] - sub_w / 2.0)),
                ("x1".into(), Json::Float(base_x[t] + max_col[t] as f64 * sub_w + sub_w / 2.0)),
                ("label".into(), Json::Str(t.map_or("untimed".into(), |t| t.to_string()))),
            ])
        })
        .collect();
    let width = (cursor + pad_x) as i64;
    let height = pad_y + stack.values().copied().max().unwrap_or(1) * row_h + 40;
    let roots = nodes.iter().filter(|n| n.deps.is_empty()).count();
    let data = Json::Obj(vec![("nodes".into(), Json::List(node_json)), ("edges".into(), Json::List(edge_json))]);
    TEMPLATE
        .replace("__WIDTH__", &width.to_string())
        .replace("__HEIGHT__", &height.to_string())
        .replace("__HEIGHT_MINUS__", &(height - 40).to_string())
        .replace("__NRULES__", &nodes.len().to_string())
        .replace("__NEDGES__", &graph.edges.len().to_string())
        .replace("__NROOTS__", &roots.to_string())
        .replace("__BANDS__", &Json::List(bands).dumps())
        .replace("__DATA__", &data.dumps())
}
