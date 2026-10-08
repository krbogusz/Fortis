//! Autosegmental diagrams as monospace text, for `--autosegmental`: tonal tiers in Goldsmith's
//! notation, and segmental node spreads as Halle-Vaux-Wolfe feature-geometry trees.

use std::collections::{BTreeSet, HashMap, HashSet};

use indexmap::IndexMap;

use crate::engine::rendering::Renderer;
use crate::engine::syllabifying::{syllabify, syllables};
use crate::engine::tiers::lower_tiers;
use crate::models::*;

fn dwidth(text: &str) -> i64 {
    text.chars().filter(|c| !crate::py::is_combining(*c)).count() as i64
}

fn fdiv(a: i64, b: i64) -> i64 {
    a.div_euclid(b)
}

fn put(row: &mut [char], col: i64, text: &str) {
    for (offset, ch) in text.chars().enumerate() {
        let idx = col + offset as i64;
        if idx >= 0 && (idx as usize) < row.len() {
            row[idx as usize] = ch;
        }
    }
}

fn set(row: &mut [char], col: i64, ch: char) {
    if col >= 0 && (col as usize) < row.len() {
        row[col as usize] = ch;
    }
}

fn joined(row: &[char]) -> String {
    row.iter().collect::<String>().trim_end().to_string()
}

fn feature_label(f: FeatId, bundle: &FeatureBundle, project: &Project) -> String {
    let def = project.features.get(f);
    let value = bundle.get(f).unwrap_or_else(|| panic!("feature '{}' is not in the bundle", def.name));
    let level = |l: &Limb| match l {
        Limb::Int(n) => def.label_of(*n).map_or(n.to_string(), str::to_string),
        Limb::None => "None".into(),
        other => format!("{other:?}"),
    };
    match (def.kind, value) {
        (FeatureKind::Binary, Value::One(Limb::Int(n))) => {
            let sign = match n {
                1 => "+".to_string(),
                0 => "-".to_string(),
                other => other.to_string(),
            };
            format!("{sign}{}", def.name)
        }
        (FeatureKind::Scalar, Value::Contour(limbs)) => {
            format!("{}: {}", def.name, limbs.iter().map(level).collect::<Vec<_>>().join(">"))
        }
        (FeatureKind::Scalar, Value::One(l @ Limb::Int(_))) => format!("{}: {}", def.name, level(l)),
        _ => def.name.clone(),
    }
}

fn label_from_bundle(bundle: &FeatureBundle, project: &Project) -> String {
    let label: Vec<String> = bundle.keys().map(|f| feature_label(f, bundle, project)).collect();
    if label.is_empty() { "?".into() } else { label.join("·") }
}

// ---- Tonal tiers ------------------------------------------------------------------------------

struct Tone {
    label: String,
    cols: Vec<usize>,
    glyph: HashMap<usize, char>,
}

fn syllable_columns(form: &Form, project: &Project, r: &Renderer) -> Vec<(String, Option<u32>)> {
    let lowered = lower_tiers(form);
    let boundaries = syllabify(&lowered, project, Some(project.time));
    let nucleus = project.syllable_parts.nucleus_definition(Some(project.time));
    syllables(&lowered, &boundaries, nucleus)
        .into_iter()
        .map(|s| {
            let chunk = &lowered[s.start..s.end];
            let edges: Boundaries = [0, chunk.len()].into_iter().collect();
            let text = r.syllabified(chunk, &edges, false);
            let text = if text.is_empty() { "∅".to_string() } else { text };
            (text, s.nucleus.map(|n| form.segments[n].id))
        })
        .collect()
}

#[allow(clippy::type_complexity)]
fn tones(form: &Form, project: &Project, before: Option<&Form>, r: &Renderer) -> (Vec<(String, Option<u32>)>, Vec<Tone>, Vec<(usize, Side, String)>) {
    let syllables = syllable_columns(form, project, r);
    let col_of: HashMap<u32, usize> =
        syllables.iter().enumerate().filter_map(|(i, (_, n))| n.map(|n| (n, i))).collect();
    let cols_of = |links: &BTreeSet<(u32, u32)>, id: u32| -> Vec<usize> {
        let set: BTreeSet<usize> = links.iter().filter(|(a, _)| *a == id).filter_map(|(_, s)| col_of.get(s).copied()).collect();
        set.into_iter().collect()
    };
    let mut tones = Vec::new();
    let mut floats = Vec::new();
    let mut drawn = HashSet::new();
    let empty = BTreeSet::new();
    for (name, tier) in &form.tiers {
        let before_links = before.and_then(|b| b.tiers.get(name)).map_or(&empty, |t| &t.links);
        for autoseg in &tier.autosegs {
            let cols = cols_of(&tier.links, autoseg.id);
            if cols.is_empty() {
                if let Some((host, side)) = tier.float_hosts.get(&autoseg.id)
                    && let Some(&col) = col_of.get(host) {
                        floats.push((col, *side, label_from_bundle(&autoseg.bundle, project)));
                    }
                continue;
            }
            drawn.insert(autoseg.id);
            let was: HashSet<usize> = cols_of(before_links, autoseg.id).into_iter().collect();
            let glyph = cols.iter().map(|c| (*c, if before.is_none() || was.contains(c) { '│' } else { '┊' })).collect();
            tones.push(Tone { label: label_from_bundle(&autoseg.bundle, project), cols, glyph });
        }
    }
    if let Some(before) = before {
        for btier in before.tiers.values() {
            for autoseg in &btier.autosegs {
                if drawn.contains(&autoseg.id) {
                    continue;
                }
                let cols = cols_of(&btier.links, autoseg.id);
                if !cols.is_empty() {
                    let glyph = cols.iter().map(|c| (*c, '╪')).collect();
                    tones.push(Tone { label: label_from_bundle(&autoseg.bundle, project), cols, glyph });
                }
            }
        }
    }
    (syllables, tones, floats)
}

fn tonal_block(form: &Form, project: &Project, before: Option<&Form>, r: &Renderer) -> Vec<String> {
    let (syllables, tones, floats) = tones(form, project, before, r);
    let n = syllables.len();
    let mut stacked: Vec<Vec<&Tone>> = vec![Vec::new(); n];
    let mut forks: Vec<&Tone> = Vec::new();
    for tone in &tones {
        if tone.cols.len() == 1 {
            stacked[tone.cols[0]].push(tone);
        } else {
            forks.push(tone);
        }
    }
    let widths: Vec<i64> = syllables
        .iter()
        .enumerate()
        .map(|(i, (text, _))| stacked[i].iter().map(|t| dwidth(&t.label)).chain([dwidth(text), 1]).max().unwrap())
        .collect();
    let gap = 3;
    let mut centers: Vec<i64> = Vec::new();
    let mut x = 0;
    for w in &widths {
        centers.push(x + fdiv(w - 1, 2));
        x += w + gap;
    }
    let mut total = (x - gap).max(1);
    let float_start = |centers: &[i64], col: usize, side: Side, text: &str| -> i64 {
        if side == Side::After {
            centers[col] + fdiv(widths[col], 2) + 1
        } else {
            centers[col] - fdiv(widths[col] - 1, 2) - 1 - dwidth(text)
        }
    };
    let (mut pad_left, mut pad_right) = (0i64, 0i64);
    for tone in &forks {
        let legs: Vec<i64> = tone.cols.iter().map(|c| centers[*c]).collect();
        let mid = fdiv(legs.iter().min().unwrap() + legs.iter().max().unwrap(), 2);
        let start = mid - fdiv(dwidth(&tone.label) - 1, 2);
        pad_left = pad_left.max(-start);
        pad_right = pad_right.max(start + dwidth(&tone.label) - total);
    }
    for (col, side, label) in &floats {
        let text = format!("({label})");
        let start = float_start(&centers, *col, *side, &text);
        pad_left = pad_left.max(-start);
        pad_right = pad_right.max(start + dwidth(&text) - total);
    }
    let centers: Vec<i64> = centers.iter().map(|c| c + pad_left).collect();
    total += pad_left + pad_right.max(0);
    let blank = || vec![' '; total as usize];
    let mut seg = blank();
    for (i, (text, _)) in syllables.iter().enumerate() {
        put(&mut seg, centers[i] - fdiv(dwidth(text) - 1, 2), text);
        if i > 0 {
            put(&mut seg, fdiv(centers[i - 1] + centers[i], 2), "-");
        }
    }
    let mut rows = vec![seg];
    let depth = stacked.iter().map(Vec::len).max().unwrap_or(0);
    for k in 0..depth {
        let (mut line, mut label) = (blank(), blank());
        for i in 0..n {
            if let Some(tone) = stacked[i].get(k) {
                set(&mut line, centers[i], tone.glyph[&i]);
                put(&mut label, centers[i] - fdiv(dwidth(&tone.label) - 1, 2), &tone.label);
            }
        }
        rows.push(line);
        rows.push(label);
    }
    for tone in &forks {
        let (mut legs, mut bar, mut label) = (blank(), blank(), blank());
        let leg_cols: Vec<i64> = tone.cols.iter().map(|c| centers[*c]).collect();
        for c in &tone.cols {
            set(&mut legs, centers[*c], tone.glyph[c]);
        }
        let (lo, hi) = (*leg_cols.iter().min().unwrap(), *leg_cols.iter().max().unwrap());
        for column in lo..=hi {
            set(&mut bar, column, '─');
        }
        set(&mut bar, lo, '└');
        set(&mut bar, hi, '┘');
        let mid = fdiv(lo + hi, 2);
        set(&mut bar, mid, if leg_cols.contains(&mid) { '┼' } else { '┬' });
        put(&mut label, mid - fdiv(dwidth(&tone.label) - 1, 2), &tone.label);
        rows.extend([legs, bar, label]);
    }
    if !floats.is_empty() {
        let mut row = blank();
        for (col, side, label) in &floats {
            let text = format!("({label})");
            put(&mut row, float_start(&centers, *col, *side, &text), &text);
        }
        rows.push(row);
    }
    rows.iter().map(|r| joined(r)).collect()
}

fn render_autosegmental_change(before: &Form, after: &Form, project: &Project, r: &Renderer) -> String {
    if after.segments.is_empty() {
        return "(empty)".into();
    }
    tonal_block(after, project, Some(before), r).join("\n")
}

fn tier_changed(before: &Form, after: &Form) -> bool {
    let names: HashSet<&String> = before.tiers.keys().chain(after.tiers.keys()).collect();
    let empty = AutosegmentalTier::default();
    for name in names {
        let b = before.tiers.get(name).unwrap_or(&empty);
        let a = after.tiers.get(name).unwrap_or(&empty);
        if b.links != a.links {
            return true;
        }
        let by_id = |t: &AutosegmentalTier| -> HashMap<u32, FeatureBundle> {
            t.autosegs.iter().map(|x| (x.id, x.bundle.clone())).collect()
        };
        if by_id(b) != by_id(a) {
            return true;
        }
    }
    false
}

// ---- Segmental spreads ------------------------------------------------------------------------

struct Spread {
    label: Vec<String>,
    links: Vec<(usize, char)>,
    replaced: bool,
    focus: FeatId,
}

fn result_bundles<'a>(elements: &'a [Element], out: &mut Vec<&'a ResultBundle>) {
    for el in elements {
        match el {
            Element::ResultElem(b) => out.push(b),
            Element::Quantified(inner, _) | Element::Negated(inner) | Element::Bound(_, inner) => {
                result_bundles(std::slice::from_ref(inner), out)
            }
            Element::Group(inner) => result_bundles(inner, out),
            Element::Disjunction(branches) => branches.iter().for_each(|b| result_bundles(b, out)),
            _ => {}
        }
    }
}

fn spread_features(rule: &Rule, project: &Project) -> Vec<FeatId> {
    let mut bundles = Vec::new();
    result_bundles(&rule.sd.result, &mut bundles);
    let mut feats: Vec<FeatId> = Vec::new();
    for b in bundles {
        for spec in b {
            if matches!(spec.value, Value::One(Limb::Recall(_))) && project.features.is_segmental(spec.feature) && !feats.contains(&spec.feature) {
                feats.push(spec.feature);
            }
        }
    }
    let mut top: Vec<FeatId> = feats
        .iter()
        .copied()
        .filter(|f| !feats.iter().any(|a| project.features.descendants(*a).contains(f)))
        .collect();
    top.sort_by(|a, b| project.features.name(*a).cmp(project.features.name(*b)));
    top
}

fn subtree(bundle: &FeatureBundle, f: FeatId, project: &Project) -> Vec<(FeatId, Value)> {
    let mut out: Vec<(FeatId, Value)> = std::iter::once(f)
        .chain(project.features.descendants(f).iter().copied())
        .filter_map(|n| bundle.get(n).map(|v| (n, v.clone())))
        .collect();
    out.sort_by_key(|(n, _)| *n);
    out
}

fn node_label(f: FeatId, bundle: &FeatureBundle, project: &Project) -> Vec<String> {
    let mut names = vec![f];
    names.extend(project.features.descendants(f).iter().copied().filter(|d| bundle.contains(*d)));
    path_label(&names, &names, bundle, project)
}

fn path_label(names: &[FeatId], on_path: &[FeatId], bundle: &FeatureBundle, project: &Project) -> Vec<String> {
    let mut lines = Vec::new();
    let mut leaves = Vec::new();
    for &name in names {
        if project.features.children(name).iter().any(|c| on_path.contains(c)) {
            lines.push(feature_label(name, bundle, project));
        } else {
            leaves.push(feature_label(name, bundle, project));
        }
    }
    if !leaves.is_empty() {
        lines.push(leaves.join("·"));
    }
    lines
}

fn lca(features: &[FeatId], project: &Project) -> FeatId {
    let chains: Vec<Vec<FeatId>> = features
        .iter()
        .map(|f| std::iter::once(*f).chain(project.features.ancestors(*f)).collect())
        .collect();
    let common: Vec<FeatId> = chains[0].iter().copied().filter(|f| chains.iter().all(|c| c.contains(f))).collect();
    chains[0].iter().copied().find(|f| common.contains(f)).unwrap_or(*chains[0].last().unwrap())
}

fn spread_label(features: &[FeatId], bundle: &FeatureBundle, project: &Project) -> Vec<String> {
    let ancestor = lca(features, project);
    let mut on_path: Vec<FeatId> = features.to_vec();
    for &f in features {
        let mut node = f;
        while node != ancestor {
            node = project.features.parent(node).expect("ancestor dominates feature");
            if !on_path.contains(&node) {
                on_path.push(node);
            }
        }
    }
    let mut names = vec![ancestor];
    names.extend(project.features.descendants(ancestor).iter().copied().filter(|d| on_path.contains(d)));
    path_label(&names, &on_path, bundle, project)
}

fn rule_spreads(before: &Form, after: &Form, rule: &Rule, project: &Project) -> Vec<Spread> {
    let before_by_id: HashMap<u32, &FeatureBundle> = before.segments.iter().map(|s| (s.id, &*s.bundle)).collect();
    let segments = &after.segments;
    let empty = FeatureBundle::new();
    let mut entries: Vec<(FeatId, FeatureBundle, Spread)> = Vec::new();
    for feature in spread_features(rule, project) {
        let mut groups: Vec<(Vec<(FeatId, Value)>, Vec<usize>)> = Vec::new();
        for (i, s) in segments.iter().enumerate() {
            if s.bundle.contains(feature) {
                let key = subtree(&s.bundle, feature, project);
                match groups.iter_mut().find(|(k, _)| *k == key) {
                    Some((_, list)) => list.push(i),
                    None => groups.push((key, vec![i])),
                }
            }
        }
        for (value, indices) in groups {
            let old: HashMap<usize, Vec<(FeatId, Value)>> = indices
                .iter()
                .map(|&i| (i, subtree(before_by_id.get(&segments[i].id).copied().unwrap_or(&empty), feature, project)))
                .collect();
            let changed: Vec<usize> = indices.iter().copied().filter(|i| old[i] != value).collect();
            if changed.is_empty() || changed.len() == indices.len() {
                continue;
            }
            let bundle = (*segments[indices[0]].bundle).clone();
            let mut label = vec![feature_label(feature, &bundle, project)];
            let links: Vec<(usize, char)> = indices.iter().map(|i| (*i, if changed.contains(i) { '┊' } else { '│' })).collect();
            let mut replaced = false;
            if changed.len() == 1 && !old[&changed[0]].is_empty() {
                label = node_label(feature, &bundle, project);
                replaced = true;
            }
            entries.push((feature, bundle, Spread { label, links, replaced, focus: feature }));
        }
    }
    let mut spreads = Vec::new();
    let mut by_links: IndexMap<Vec<(usize, char)>, Vec<(FeatId, FeatureBundle)>> = IndexMap::new();
    for (feature, bundle, s) in entries {
        if s.replaced {
            spreads.push(s);
            continue;
        }
        by_links.entry(s.links).or_default().push((feature, bundle));
    }
    for (links, items) in by_links {
        if items.len() == 1 {
            let (feature, bundle) = &items[0];
            spreads.push(Spread { label: vec![feature_label(*feature, bundle, project)], links, replaced: false, focus: *feature });
        } else {
            let feats: Vec<FeatId> = items.iter().map(|(f, _)| *f).collect();
            let focus = lca(&feats, project);
            spreads.push(Spread { label: spread_label(&feats, &items[0].1, project), links, replaced: false, focus });
        }
    }
    spreads
}

fn pad(line: &str, width: i64) -> String {
    format!("{line}{}", " ".repeat((width - dwidth(line)).max(0) as usize))
}

fn block_width(lines: &[String]) -> i64 {
    lines.iter().map(|l| dwidth(l)).max().unwrap_or(0)
}

type Positions = IndexMap<String, (i64, i64, i64, i64)>;

fn tree_block(node: FeatId, root: bool, bundle: &FeatureBundle, project: &Project, include: &[FeatId], r: &Renderer) -> (Vec<String>, i64, Positions) {
    let label = if root {
        let s = r.segment(bundle, false);
        if s.is_empty() { "∅".to_string() } else { s }
    } else {
        feature_label(node, bundle, project)
    };
    let key = if root { "root".to_string() } else { project.features.name(node).to_string() };
    let kids: Vec<FeatId> = project.features.children(node).iter().copied().filter(|c| include.contains(c)).collect();
    if kids.is_empty() {
        let w = dwidth(&label);
        let mut positions = Positions::new();
        positions.insert(key, (0, fdiv(w, 2), 0, w));
        return (vec![label], fdiv(w, 2), positions);
    }
    let blocks: Vec<(Vec<String>, i64, Positions)> = kids.iter().map(|c| tree_block(*c, false, bundle, project, include, r)).collect();
    let height = blocks.iter().map(|(b, _, _)| b.len()).max().unwrap();
    let mut rows = vec![String::new(); height];
    let mut roots = Vec::new();
    let mut positions = Positions::new();
    let mut x = 0;
    for (bl, broot, pos) in &blocks {
        for (i, row) in rows.iter_mut().enumerate() {
            *row = format!("{}{}", pad(row, x), bl.get(i).map_or("", |s| s.as_str()));
        }
        roots.push(x + broot);
        for (name, (pr, mid, start, w)) in pos {
            positions.insert(name.clone(), (pr + 2, mid + x, start + x, *w));
        }
        x += block_width(bl) + 3;
    }
    let width = (x - 3).max(dwidth(&label));
    let mid = fdiv(roots[0] + roots[roots.len() - 1], 2);
    let mut conn = vec![' '; width as usize];
    if roots.len() == 1 {
        set(&mut conn, roots[0], '│');
    } else {
        for c in roots[0]..=roots[roots.len() - 1] {
            set(&mut conn, c, '─');
        }
        for &c in &roots {
            set(&mut conn, c, '┬');
        }
        set(&mut conn, roots[0], '┌');
        set(&mut conn, roots[roots.len() - 1], '┐');
        set(&mut conn, mid, if roots.contains(&mid) { '┼' } else { '┴' });
    }
    let mut node_line = vec![' '; width as usize];
    let lw = dwidth(&label);
    let start = (mid - fdiv(lw - 1, 2)).max(0);
    put(&mut node_line, start, &label);
    positions.insert(key, (0, mid, start, lw));
    let mut lines = vec![node_line.iter().collect::<String>(), conn.iter().collect::<String>()];
    lines.extend(rows.iter().map(|r| pad(r, width)));
    (lines, mid, positions)
}

fn tree_diagram(target: &FeatureBundle, source: &FeatureBundle, focus: FeatId, project: &Project, delink: bool, r: &Renderer) -> String {
    let features = &project.features;
    let root = features.id("root");
    let ancestry: Vec<FeatId> = std::iter::once(focus).chain(features.ancestors(focus)).collect();
    let top = ancestry.iter().copied().find(|a| features.parent(*a) == root).unwrap_or(focus);
    let include = |bundle: &FeatureBundle| -> Vec<FeatId> {
        std::iter::once(top).chain(features.descendants(top).iter().copied().filter(|d| bundle.contains(*d))).collect()
    };
    let root_id = root.expect("a feature geometry has a root");
    let (mut tlines, _, tpos) = tree_block(root_id, true, target, project, &include(target), r);
    let (mut slines, _, spos) = tree_block(root_id, true, source, project, &include(source), r);
    let gap = 8;
    let tw = block_width(&tlines);
    let height = tlines.len().max(slines.len());
    tlines.resize(height, String::new());
    slines.resize(height, String::new());
    let sw = block_width(&slines);
    let mut grid: Vec<Vec<char>> = (0..height)
        .map(|i| format!("{}{}{}", pad(&tlines[i], tw), " ".repeat(gap), pad(&slines[i], sw)).chars().collect())
        .collect();
    let name = features.name(focus);
    let (frow, tmid, tstart, twdt) = *tpos.get(name).unwrap_or(&tpos["root"]);
    let (_, _, sstart, _) = *spos.get(name).unwrap_or(&spos["root"]);
    let sstart = sstart + tw + gap as i64;
    let (left, right) = (tstart + twdt + 1, sstart - 2);
    if left <= right && (frow as usize) < grid.len() {
        for c in left..=right {
            set(&mut grid[frow as usize], c, '┈');
        }
        set(&mut grid[frow as usize], left, '◀');
    }
    if delink && frow >= 1 {
        set(&mut grid[frow as usize - 1], tmid, '⧧');
    }
    grid.iter().map(|row| joined(row)).collect::<Vec<_>>().join("\n")
}

/// Every autosegmental change one rule made, as `(sublabel, diagram)`: a tier change first,
/// then each segmental spread.
pub fn render_change(before: &Form, after: &Form, rule: &Rule, project: &Project, r: &Renderer) -> Vec<(String, String)> {
    let mut out = Vec::new();
    if tier_changed(before, after) {
        out.push((String::new(), render_autosegmental_change(before, after, project, r)));
    }
    for s in rule_spreads(before, after, rule, project) {
        let target_idx = s.links.iter().find(|(_, g)| *g == '┊').unwrap().0;
        let source_idx = s.links.iter().find(|(_, g)| *g == '│').unwrap().0;
        let target = &before.segments[target_idx].bundle;
        let source = &after.segments[source_idx].bundle;
        out.push((s.label.join("·"), tree_diagram(target, source, s.focus, project, s.replaced, r)));
    }
    out
}

/// `autosegmental.md`: every autosegmental change, one section per word.
pub fn autosegmental_md(derivations: &[Derivation], project: &Project, r: &Renderer) -> String {
    let mut lines: Vec<String> = vec!["# Autosegmental changes".into(), String::new()];
    for d in derivations {
        let mut sections: Vec<String> = Vec::new();
        for step in &d.steps {
            for (sublabel, diagram) in render_change(&step.before, &step.after, &step.rule, project, r) {
                let name = step.rule.name.clone().unwrap_or_else(|| "None".into());
                let title = if sublabel.is_empty() { name } else { format!("{name} · {sublabel}") };
                sections.extend([format!("### {title}"), String::new(), "```".into(), diagram, "```".into(), String::new()]);
            }
        }
        if !sections.is_empty() {
            let gloss = if d.word.gloss.is_empty() { String::new() } else { format!(" ‘{}’", d.word.gloss) };
            lines.push(format!("## {}{gloss}", d.word.ipa()));
            lines.push(String::new());
            lines.extend(sections);
        }
    }
    if lines.len() == 2 {
        lines.push("_No rule in this run uses autosegmental mechanisms._".into());
    }
    format!("{}\n", lines.join("\n").trim_end())
}
