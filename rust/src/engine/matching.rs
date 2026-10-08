//! Pattern matching: one pattern bundle against one segment, and the backtracking sequence
//! matcher that finds every locus where a rule applies.
//!
//! The sequence matcher is written in continuation-passing style: each matcher calls `k` with
//! every `(end, bindings)` it can reach, in the order a Python generator would yield them, and
//! stops as soon as `k` returns `true`.

use std::sync::Arc;

use crate::models::*;

/// A set of feature ids.
#[derive(Clone, Debug, Default)]
pub struct FeatSet {
    bits: Vec<u64>,
}

impl FeatSet {
    pub fn from_ids(ids: impl IntoIterator<Item = FeatId>) -> Self {
        let mut set = FeatSet::default();
        for id in ids {
            set.insert(id);
        }
        set
    }

    pub fn insert(&mut self, id: FeatId) {
        let (w, b) = (id as usize / 64, id as usize % 64);
        if self.bits.len() <= w {
            self.bits.resize(w + 1, 0);
        }
        self.bits[w] |= 1 << b;
    }

    pub fn contains(&self, id: FeatId) -> bool {
        let (w, b) = (id as usize / 64, id as usize % 64);
        self.bits.get(w).is_some_and(|word| word & (1 << b) != 0)
    }

    pub fn is_empty(&self) -> bool {
        self.bits.iter().all(|w| *w == 0)
    }
}

/// Syllable-tier context for matching: each position's nucleus bundle, the floating
/// autosegments, and (through `features`) the geometry for node-spread capture.
pub struct SyllableView {
    pub nuclei: Vec<Option<Arc<FeatureBundle>>>,
    pub floating: Vec<(u32, FeatureBundle, Option<usize>)>,
}

impl SyllableView {
    fn at(&self, pos: usize) -> Option<&FeatureBundle> {
        self.nuclei.get(pos).and_then(|n| n.as_deref())
    }
}

/// Everything the matcher reads besides the rule.
pub struct MatchCtx<'a> {
    pub segs: &'a [Arc<FeatureBundle>],
    pub letters: &'a LetterInventory,
    pub boundaries: &'a Boundaries,
    pub view: Option<&'a SyllableView>,
    pub features: &'a FeatureInventory,
    pub syllable_features: &'a FeatSet,
}

#[derive(Clone, Debug)]
pub struct Match {
    pub start: usize,
    pub end: usize,
    pub bindings: Bindings,
    pub target_choices: Vec<usize>,
}

// ---- One pattern against one segment ----------------------------------------------------------

/// Optional context for [`pattern_matches`]: the syllable nucleus, and node-spread capture.
#[derive(Clone, Copy, Default)]
pub struct PatternCtx<'a> {
    pub syllable: Option<&'a FeatureBundle>,
    pub syllable_features: Option<&'a FeatSet>,
    /// The feature geometry, when node-spread references (`node: ~n`) should be captured.
    pub nodes: Option<&'a FeatureInventory>,
    pub position: Option<usize>,
}

fn alpha_matches(r: &AlphaRef, atom: Limb, bindings: &mut Option<&mut Bindings>) -> bool {
    let Some(b) = bindings else { return true };
    if b.permissive_alpha {
        return true;
    }
    match map_get(&b.alpha, r.var) {
        None => {
            match r.op {
                AlphaOp::Same => map_set(&mut b.alpha, r.var, atom),
                AlphaOp::Opposite => map_set(&mut b.alpha, r.var, opposite_pole(atom, r.unary)),
                AlphaOp::Other => b.pending_other.push((r.var, atom)),
            }
            true
        }
        Some(&bound) => match r.op {
            AlphaOp::Same => atom == bound,
            AlphaOp::Opposite | AlphaOp::Other => atom != bound,
        },
    }
}

fn limb_binding(p: Limb, s: Limb, bindings: &mut Option<&mut Bindings>) -> bool {
    match p {
        Limb::Alpha(r) => alpha_matches(&r, s, bindings),
        Limb::Any => s != Limb::None,
        _ => p == s,
    }
}

fn limb_readonly(p: Limb, s: Limb, bindings: &Option<&mut Bindings>) -> bool {
    match p {
        Limb::Alpha(r) => {
            let Some(bound) = bindings.as_ref().and_then(|b| map_get(&b.alpha, r.var)).copied() else {
                return false;
            };
            if r.op == AlphaOp::Same { s == bound } else { s != bound }
        }
        Limb::Any => s != Limb::None,
        _ => p == s,
    }
}

fn window(p: &[Limb], s: &[Limb], start: usize, cmp: &mut dyn FnMut(Limb, Limb) -> bool) -> bool {
    p.iter().enumerate().all(|(i, &pl)| cmp(pl, s[start + i]))
}

fn value_at_position(
    p: &[Limb],
    position: &ContourPosition,
    s: &[Limb],
    cmp: &mut dyn FnMut(Limb, Limb) -> bool,
    binds: bool,
) -> bool {
    let in_range = |n: i64| n >= 1 && (n as usize) <= s.len();
    match position {
        ContourPosition::List(list) => {
            if p.len() == 1 {
                return list.iter().all(|&n| in_range(n) && cmp(p[0], s[n as usize - 1]));
            }
            list.len() == p.len()
                && p.iter().zip(list).all(|(&pl, &n)| in_range(n) && cmp(pl, s[n as usize - 1]))
        }
        ContourPosition::Index(n) => p.len() == 1 && in_range(*n) && cmp(p[0], s[*n as usize - 1]),
        ContourPosition::Edge(ContourEdge::All) => {
            if p.len() == 1 {
                return !s.is_empty() && s.iter().all(|&sl| cmp(p[0], sl));
            }
            p.len() == s.len() && window(p, s, 0, cmp)
        }
        ContourPosition::Edge(ContourEdge::Any) => {
            if p.len() == 1 {
                return s.iter().any(|&sl| cmp(p[0], sl));
            }
            if binds && p.iter().any(|l| matches!(l, Limb::Alpha(_))) {
                panic!("alpha in a multi-limb @any contour pattern is not supported");
            }
            if s.len() < p.len() {
                return false;
            }
            (0..=s.len() - p.len()).any(|i| window(p, s, i, cmp))
        }
        ContourPosition::Edge(ContourEdge::Initial) => p.len() <= s.len() && window(p, s, 0, cmp),
        ContourPosition::Edge(ContourEdge::Final) => {
            p.len() <= s.len() && window(p, s, s.len() - p.len(), cmp)
        }
    }
}

fn has_alpha(value: &Value) -> bool {
    value.limbs().iter().any(|l| matches!(l, Limb::Alpha(_)))
}

fn has_unary_alpha(value: &Value) -> bool {
    value.limbs().iter().any(|l| matches!(l, Limb::Alpha(a) if a.unary))
}

fn spec_matches(
    value: &Value,
    position: &ContourPosition,
    negated: bool,
    segment_value: &Value,
    bindings: &mut Option<&mut Bindings>,
) -> bool {
    if bindings.as_ref().is_some_and(|b| b.permissive_alpha) && has_alpha(value) {
        return true;
    }
    let matched = value_at_position(
        value.limbs(),
        position,
        segment_value.limbs(),
        &mut |p, s| limb_binding(p, s, bindings),
        true,
    );
    if negated { !matched } else { matched }
}

fn condition_holds(spec: &PatternSpec, target: &FeatureBundle, bindings: &Option<&mut Bindings>) -> bool {
    let base = match target.get(spec.feature) {
        None => spec.value.is_none(),
        Some(v) => value_at_position(
            spec.value.limbs(),
            &spec.contour_position,
            v.limbs(),
            &mut |p, s| limb_readonly(p, s, bindings),
            false,
        ),
    };
    if spec.negated { !base } else { base }
}

/// Whether *pattern* matches realized *segment*, binding alpha and references into *bindings*.
pub fn pattern_matches(
    pattern: &[PatternSpec],
    segment: &FeatureBundle,
    mut bindings: Option<&mut Bindings>,
    cx: PatternCtx,
) -> bool {
    for spec in pattern {
        let target = match (cx.syllable, cx.syllable_features) {
            (Some(syl), Some(feats)) if feats.contains(spec.feature) => syl,
            _ => segment,
        };
        if let Some(label) = spec.condition_label {
            if bindings.is_some() {
                let holds = condition_holds(spec, target, &bindings);
                let b = bindings.as_mut().unwrap();
                let previous = map_get(&b.conditions, label).copied().unwrap_or(true);
                map_set(&mut b.conditions, label, previous && holds);
            }
            continue;
        }
        let reference = match spec.value {
            Value::One(Limb::Bind(bind)) => Some((bind.r, bind.optional, Some(bind.value))),
            Value::One(Limb::Recall(recall)) => Some((recall.r, recall.optional, None)),
            _ => None,
        };
        let node = cx.nodes.filter(|f| f.is_segmental(spec.feature));
        match target.get(spec.feature) {
            None => {
                if has_unary_alpha(&spec.value) {
                    if !spec_matches(&spec.value, &spec.contour_position, spec.negated, &Value::NONE, &mut bindings) {
                        return false;
                    }
                    continue;
                }
                if let (Some(_), Some((r, true, _))) = (node, reference) {
                    if let Some(b) = bindings.as_mut() {
                        map_set(&mut b.node_reference, r, FeatureBundle::new());
                    }
                    continue;
                }
                if spec.value.is_none() {
                    if spec.negated {
                        return false;
                    }
                    continue;
                }
                if spec.negated {
                    continue;
                }
                return false;
            }
            Some(seg_value) => {
                if let (Some(features), Some((r, _, bind_value))) = (node, reference) {
                    if let Some(v) = bind_value
                        && !spec_matches(&Value::int(v), &spec.contour_position, spec.negated, seg_value, &mut bindings) {
                            return false;
                        }
                    if let Some(b) = bindings.as_mut() {
                        let names = features.descendants(spec.feature);
                        let captured = FeatureBundle {
                            items: target
                                .items
                                .iter()
                                .filter(|(f, _)| *f == spec.feature || names.contains(f))
                                .cloned()
                                .collect(),
                        };
                        map_set(&mut b.node_reference, r, captured);
                    }
                    continue;
                }
                if let Some((r, _, Some(v))) = reference {
                    if !spec_matches(&Value::int(v), &spec.contour_position, spec.negated, seg_value, &mut bindings) {
                        return false;
                    }
                    if let (Some(b), Some(pos)) = (bindings.as_mut(), cx.position) {
                        map_set(&mut b.autoseg_reference, r, pos);
                    }
                    continue;
                }
                if !spec_matches(&spec.value, &spec.contour_position, spec.negated, seg_value, &mut bindings) {
                    return false;
                }
            }
        }
    }
    true
}

/// [`pattern_matches`] with no bindings and no syllable context.
pub fn matches_plain(pattern: &[PatternSpec], segment: &FeatureBundle) -> bool {
    pattern_matches(pattern, segment, None, PatternCtx::default())
}

fn floating_matches(pattern: &[PatternSpec], bundle: &FeatureBundle) -> bool {
    pattern.iter().all(|spec| {
        let wanted = match spec.value {
            Value::One(Limb::Bind(b)) => Value::int(b.value),
            ref other => other.clone(),
        };
        bundle.get(spec.feature) == Some(&wanted)
    })
}

/// Whether *segment* is exactly this letter (segmental features), with any syllable-tier
/// feature the letter carries checked against the segment's nucleus.
fn letter_matches(
    letter: &FeatureBundle,
    segment: &FeatureBundle,
    syllable_features: Option<&FeatSet>,
    syllable: Option<&FeatureBundle>,
) -> bool {
    let is_syl = |f: FeatId| syllable_features.is_some_and(|s| s.contains(f));
    let seg_count = segment.items.iter().filter(|(f, _)| !is_syl(*f)).count();
    let let_count = letter.items.iter().filter(|(f, _)| !is_syl(*f)).count();
    if seg_count != let_count {
        return false;
    }
    for (f, v) in &letter.items {
        if is_syl(*f) {
            continue;
        }
        if segment.get(*f) != Some(v) {
            return false;
        }
    }
    for (f, v) in &letter.items {
        if is_syl(*f) {
            let have = syllable.and_then(|s| s.get(*f)).cloned().unwrap_or(Value::NONE);
            if have != *v {
                return false;
            }
        }
    }
    true
}

// ---- The sequence matcher ---------------------------------------------------------------------

type K<'k> = &'k mut dyn FnMut(usize, &Bindings) -> bool;

impl MatchCtx<'_> {
    fn at_boundary(&self, pos: usize) -> bool {
        pos < self.segs.len() && is_morpheme_boundary(&self.segs[pos])
    }

    fn content_at(&self, pos: usize) -> bool {
        pos < self.segs.len() && !self.at_boundary(pos)
    }

    fn syl_feats(&self) -> Option<&FeatSet> {
        self.view.map(|_| self.syllable_features)
    }

    pub fn element(&self, el: &Element, pos: usize, b: &Bindings, k: K) -> bool {
        match el {
            Element::BundleElem(bundle) => {
                if !self.content_at(pos) {
                    return false;
                }
                let mut branch = b.clone();
                let cx = PatternCtx {
                    syllable: self.view.and_then(|v| v.at(pos)),
                    syllable_features: self.syl_feats(),
                    nodes: self.view.map(|_| self.features),
                    position: Some(pos),
                };
                if pattern_matches(bundle, &self.segs[pos], Some(&mut branch), cx) {
                    return k(pos + 1, &branch);
                }
                false
            }
            Element::FloatingAutoseg(pattern) => {
                let Some(view) = self.view else { return false };
                let mut branch = b.clone();
                for (id, bundle, gap) in &view.floating {
                    if gap.is_some_and(|g| g != pos) {
                        continue;
                    }
                    if floating_matches(pattern, bundle) {
                        for spec in pattern {
                            if let Value::One(Limb::Bind(bind)) = spec.value {
                                map_set(&mut branch.floating_reference, bind.r, *id);
                            }
                        }
                        return k(pos, &branch);
                    }
                }
                false
            }
            Element::LetterRef(symbol) => {
                if !self.content_at(pos) {
                    return false;
                }
                let Some(letter) = self.letters.get(symbol) else { return false };
                let syl = self.view.and_then(|v| v.at(pos));
                if letter_matches(&letter.bundle, &self.segs[pos], self.syl_feats(), syl) {
                    return k(pos + 1, b);
                }
                false
            }
            Element::LetterBundle(bundle) => {
                if !self.content_at(pos) {
                    return false;
                }
                let syl = self.view.and_then(|v| v.at(pos));
                if letter_matches(bundle, &self.segs[pos], self.syl_feats(), syl) {
                    return k(pos + 1, b);
                }
                false
            }
            Element::Wildcard => self.content_at(pos) && k(pos + 1, b),
            Element::MorphemeBoundary => self.at_boundary(pos) && k(pos + 1, b),
            Element::WordBoundary => (pos == 0 || pos == self.segs.len()) && k(pos, b),
            Element::SyllableBoundary => self.boundaries.contains(&pos) && k(pos, b),
            Element::Null => k(pos, b),
            Element::Group(inner) => self.sequence(inner, pos, b, k),
            Element::Disjunction(branches) => {
                for (index, branch) in branches.iter().enumerate() {
                    let mut chosen = b.clone();
                    chosen.disjunction_choices.push(index);
                    if self.sequence(branch, pos, &chosen, k) {
                        return true;
                    }
                }
                false
            }
            Element::Negated(inner) => {
                if !self.content_at(pos) {
                    return false;
                }
                if b.permissive_alpha {
                    return k(pos + 1, b);
                }
                let copy = b.clone();
                let mut matched = false;
                self.element(inner, pos, &copy, &mut |end, _| {
                    if end == pos + 1 {
                        matched = true;
                        return true;
                    }
                    false
                });
                !matched && k(pos + 1, b)
            }
            Element::Quantified(inner, q) => self.repeat(inner, pos, b, q.min, q.max, 0, k),
            Element::Bound(r, inner) => self.element(inner, pos, b, &mut |end, branch| {
                let mut captured = branch.clone();
                let span: Arc<[Arc<FeatureBundle>]> = self.segs[pos..end].to_vec().into();
                map_set(&mut captured.reference, *r, span);
                k(end, &captured)
            }),
            Element::RecallRef(r) => {
                let Some(bound) = map_get(&b.reference, *r) else { return false };
                let end = pos + bound.len();
                if end <= self.segs.len() && bound.iter().enumerate().all(|(o, seg)| *self.segs[pos + o] == **seg) {
                    return k(end, b);
                }
                false
            }
            other => panic!("cannot match element {other:?} in this position"),
        }
    }

    #[allow(clippy::too_many_arguments)]
    fn repeat(&self, inner: &Element, pos: usize, b: &Bindings, min: usize, max: Option<usize>, count: usize, k: K) -> bool {
        if max.is_none_or(|m| count < m)
            && self.element(inner, pos, b, &mut |end, branch| {
                end != pos && self.repeat(inner, end, branch, min, max, count + 1, k)
            })
        {
            return true;
        }
        count >= min && k(pos, b)
    }

    pub fn sequence(&self, elements: &[Element], pos: usize, b: &Bindings, k: K) -> bool {
        match elements.split_first() {
            None => k(pos, b),
            Some((first, rest)) => self.element(first, pos, b, &mut |mid, branch| self.sequence(rest, mid, branch, k)),
        }
    }

    /// Bindings for which *elements* match a span ending exactly at *end* (left edge floats).
    fn ending_at(&self, elements: &[Element], end: usize, b: &Bindings, k: &mut dyn FnMut(&Bindings) -> bool) -> bool {
        for start in (0..=end).rev() {
            if self.sequence(elements, start, b, &mut |stop, branch| stop == end && k(branch)) {
                return true;
            }
        }
        false
    }

    fn starting_at(&self, elements: &[Element], start: usize, b: &Bindings, k: &mut dyn FnMut(&Bindings) -> bool) -> bool {
        self.sequence(elements, start, b, &mut |_, branch| k(branch))
    }

    fn span(&self, elements: &[Element], start: usize, end: usize, b: &Bindings, k: &mut dyn FnMut(&Bindings) -> bool) -> bool {
        self.sequence(elements, start, b, &mut |stop, branch| stop == end && k(branch))
    }

    /// Pre-bind a right-anchored sequence's references so a position to its left can recall them.
    fn seed_right_references(&self, right: &[Element], at: usize, seed: &Bindings) -> Bindings {
        if right.is_empty() {
            return seed.clone();
        }
        let mut blind = seed.clone();
        blind.permissive_alpha = true;
        let mut result = None;
        self.starting_at(right, at, &blind, &mut |captured| {
            if captured.same_references(seed) {
                result = Some(seed.clone());
            } else {
                let mut enriched = seed.clone();
                for (key, value) in &captured.reference {
                    map_set(&mut enriched.reference, *key, value.clone());
                }
                result = Some(enriched);
            }
            true
        });
        result.unwrap_or_else(|| seed.clone())
    }

    fn exception_blocks(&self, sd: &StructuralDescription, start: usize, end: usize, b: &Bindings) -> bool {
        if sd.left_exception.is_empty() && sd.right_exception.is_empty() {
            return false;
        }
        let seeded = self.seed_right_references(&sd.right_exception, end, b);
        self.ending_at(&sd.left_exception, start, &seeded, &mut |left| {
            self.starting_at(&sd.right_exception, end, left, &mut |_| true)
        })
    }

    /// Pass 2: the whole environment around a candidate span.
    fn locate(&self, sd: &StructuralDescription, start: usize, end: usize, seed: &Bindings) -> Option<Match> {
        let seed = self.seed_right_references(&sd.right_context, end, seed);
        let mut found = None;
        self.ending_at(&sd.left_context, start, &seed, &mut |after_left| {
            let left_choices = after_left.disjunction_choices.len();
            self.span(&sd.target, start, end, after_left, &mut |after_target| {
                let choices = &after_target.disjunction_choices[left_choices..];
                self.starting_at(&sd.right_context, end, after_target, &mut |after_right| {
                    if pending_other_holds(after_right) && !self.exception_blocks(sd, start, end, after_right) {
                        found = Some(Match {
                            start,
                            end,
                            bindings: after_right.clone(),
                            target_choices: choices.to_vec(),
                        });
                        return true;
                    }
                    false
                })
            })
        });
        found
    }

    /// Every locus where *sd* applies: the greediest fully-valid target span at each start.
    pub fn find_matches(&self, sd: &StructuralDescription, case_b: bool) -> Vec<Match> {
        let mut matches = Vec::new();
        let n = self.segs.len();
        for start in 0..=n {
            let mut located = None;
            let seed = Bindings { permissive_alpha: true, ..Default::default() };
            self.sequence(&sd.target, start, &seed, &mut |end, pass1| {
                let refs = Bindings { reference: pass1.reference.clone(), ..Default::default() };
                located = self.locate(sd, start, end, &refs);
                located.is_some()
            });
            if located.is_none() && case_b {
                for end in (start..=n).rev() {
                    located = self.locate(sd, start, end, &Bindings::default());
                    if located.is_some() {
                        break;
                    }
                }
            }
            if let Some(m) = located {
                matches.push(m);
            }
        }
        matches
    }
}

fn pending_other_holds(b: &Bindings) -> bool {
    b.pending_other
        .iter()
        .all(|(var, atom)| map_get(&b.alpha, *var).is_some_and(|bound| atom != bound))
}

/// Whether *elements* match *segments* exactly, start to end (an onset/coda pattern check).
pub fn full_match(elements: &[Element], segments: &[Arc<FeatureBundle>], letters: &LetterInventory, features: &FeatureInventory) -> bool {
    let boundaries = Boundaries::new();
    let empty = FeatSet::default();
    let cx = MatchCtx { segs: segments, letters, boundaries: &boundaries, view: None, features, syllable_features: &empty };
    cx.span(elements, 0, segments.len(), &Bindings::default(), &mut |_| true)
}

// ---- Necessary-condition pruning --------------------------------------------------------------

/// A demand: a `(feature, value)` pair some segment must carry.
pub type Demand = (FeatId, i64);

fn spec_demand(feature: FeatId, value: &Value) -> Option<Demand> {
    match value {
        Value::One(Limb::Int(n)) => Some((feature, *n)),
        _ => None,
    }
}

fn pattern_demands(bundle: &[PatternSpec]) -> Vec<Demand> {
    bundle
        .iter()
        .filter(|s| s.condition_label.is_none() && !s.negated)
        .filter_map(|s| spec_demand(s.feature, &s.value))
        .collect()
}

fn feature_demands(bundle: &FeatureBundle) -> Vec<Demand> {
    bundle.items.iter().filter_map(|(f, v)| spec_demand(*f, v)).collect()
}

fn element_demands(el: &Element, letters: &LetterInventory) -> Vec<Demand> {
    match el {
        Element::BundleElem(b) => pattern_demands(b),
        Element::LetterBundle(b) => feature_demands(b),
        Element::LetterRef(s) => letters.get(s).map(|l| feature_demands(&l.bundle)).unwrap_or_default(),
        _ => Vec::new(),
    }
}

fn binding_demands(sd: &StructuralDescription, letters: &LetterInventory) -> Vec<(i64, Vec<Demand>)> {
    fn walk(elements: &[Element], required: bool, letters: &LetterInventory, out: &mut Vec<(i64, Vec<Demand>)>) {
        for el in elements {
            match el {
                Element::Bound(r, inner) if required => {
                    let d = element_demands(inner, letters);
                    if !d.is_empty() {
                        map_set(out, *r, d);
                    }
                    walk(std::slice::from_ref(inner), required, letters, out);
                }
                Element::Group(inner) => walk(inner, required, letters, out),
                Element::Quantified(inner, q) => walk(std::slice::from_ref(inner), required && q.min >= 1, letters, out),
                _ => {}
            }
        }
    }
    let mut out = Vec::new();
    for elements in [&sd.target, &sd.left_context, &sd.right_context] {
        walk(elements, true, letters, &mut out);
    }
    out
}

/// A conservative lower bound on the `(feature, value)` occurrences any locus of *sd* needs,
/// with syllable-tier demands dropped (they are checked against the nucleus).
pub fn required_demands(sd: &StructuralDescription, letters: &LetterInventory, syllable_features: &FeatSet) -> Vec<(Demand, usize)> {
    let bindings = binding_demands(sd, letters);
    let mut counts: Vec<(Demand, usize)> = Vec::new();
    fn add(counts: &mut Vec<(Demand, usize)>, demands: &[Demand]) {
        for d in demands {
            if let Some(slot) = counts.iter_mut().find(|(k, _)| k == d) {
                slot.1 += 1;
            } else {
                counts.push((*d, 1));
            }
        }
    }
    fn accumulate(elements: &[Element], required: bool, letters: &LetterInventory, bindings: &[(i64, Vec<Demand>)], counts: &mut Vec<(Demand, usize)>) {
        for el in elements {
            match el {
                Element::BundleElem(_) | Element::LetterBundle(_) | Element::LetterRef(_) if required => {
                    add(counts, &element_demands(el, letters))
                }
                Element::RecallRef(r) if required => {
                    if let Some(d) = map_get(bindings, *r) {
                        add(counts, d);
                    }
                }
                Element::MorphemeBoundary if required => add(counts, &[(MORPHEME_BOUNDARY, 1)]),
                Element::Bound(_, inner) => accumulate(std::slice::from_ref(inner), required, letters, bindings, counts),
                Element::Group(inner) => accumulate(inner, required, letters, bindings, counts),
                Element::Quantified(inner, q) => {
                    accumulate(std::slice::from_ref(inner), required && q.min >= 1, letters, bindings, counts)
                }
                _ => {}
            }
        }
    }
    for elements in [&sd.target, &sd.left_context, &sd.right_context] {
        accumulate(elements, true, letters, &bindings, &mut counts);
    }
    counts.retain(|((f, _), _)| !syllable_features.contains(*f));
    counts
}

/// How many segments carry each `(feature, value)`, sorted for binary search.
#[derive(Clone, Debug, Default)]
pub struct Supply(Vec<(Demand, usize)>);

pub fn word_supply(segments: &[Arc<FeatureBundle>]) -> Supply {
    let mut all: Vec<Demand> = Vec::new();
    for seg in segments {
        for (f, v) in &seg.items {
            if let Value::One(Limb::Int(n)) = v {
                all.push((*f, *n));
            }
        }
    }
    all.sort_unstable();
    let mut out: Vec<(Demand, usize)> = Vec::new();
    for d in all {
        match out.last_mut() {
            Some((last, count)) if *last == d => *count += 1,
            _ => out.push((d, 1)),
        }
    }
    Supply(out)
}

pub fn cannot_match(demands: &[(Demand, usize)], supply: &Supply) -> bool {
    demands.iter().any(|(d, count)| {
        let have = supply.0.binary_search_by(|(k, _)| k.cmp(d)).map_or(0, |i| supply.0[i].1);
        have < *count
    })
}

fn bound_refs(elements: &[Element], out: &mut Vec<i64>) {
    for el in elements {
        match el {
            Element::Bound(r, inner) => {
                out.push(*r);
                bound_refs(std::slice::from_ref(inner), out);
            }
            Element::Group(inner) => bound_refs(inner, out),
            Element::Disjunction(branches) => branches.iter().for_each(|b| bound_refs(b, out)),
            Element::Quantified(inner, _) | Element::Negated(inner) => bound_refs(std::slice::from_ref(inner), out),
            _ => {}
        }
    }
}

fn recall_refs(elements: &[Element], out: &mut Vec<i64>) {
    for el in elements {
        match el {
            Element::RecallRef(r) => out.push(*r),
            Element::Bound(_, inner) | Element::Quantified(inner, _) | Element::Negated(inner) => {
                recall_refs(std::slice::from_ref(inner), out)
            }
            Element::Group(inner) => recall_refs(inner, out),
            Element::Disjunction(branches) => branches.iter().for_each(|b| recall_refs(b, out)),
            _ => {}
        }
    }
}

/// Whether the target recalls a reference bound only in a context (so pass 1 cannot fix its span).
pub fn target_recalls_context_binding(sd: &StructuralDescription) -> bool {
    let mut context = Vec::new();
    bound_refs(&sd.left_context, &mut context);
    bound_refs(&sd.right_context, &mut context);
    let mut recalled = Vec::new();
    recall_refs(&sd.target, &mut recalled);
    let mut target_bound = Vec::new();
    bound_refs(&sd.target, &mut target_bound);
    recalled.iter().any(|r| !target_bound.contains(r) && context.contains(r))
}
