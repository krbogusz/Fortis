//! The derivation driver: sweep a word through every rule in time order, recording each rule
//! that changed it.

use std::collections::HashMap;
use std::sync::Arc;

use rayon::prelude::*;

use super::applying::apply_match;
use super::combining::{combine, merge};
use super::matching::*;
use super::segmentation::string_to_sequence;
use super::syllabifying::{Parts, nuclei_by_position, syllabify_with};
use super::tiers::*;
use crate::models::*;

/// A rule with its letter runs resolved and its matching data precomputed.
pub struct PreparedRule {
    pub rule: Arc<Rule>,
    pub demands: Vec<(Demand, usize)>,
    pub case_b: bool,
    pub parts: Parts,
}

/// The project plus its prepared rules: everything a derivation needs.
pub struct Engine<'p> {
    pub project: &'p Project,
    /// The letter-resolved rules, as an inventory (for the reports).
    pub rules: RuleInventory,
    schedule: Vec<(Option<i64>, Vec<PreparedRule>)>,
    pub syllable_features: FeatSet,
    latest: i64,
}

// ---- Resolving letter runs --------------------------------------------------------------------

fn segments_of(symbol: &str, project: &Project) -> Result<Vec<Arc<FeatureBundle>>, String> {
    Ok(lower_tiers(&string_to_sequence(symbol, project)?))
}

fn resolve_elements(elements: &[Element], project: &Project, rule_id: &str) -> Result<Vec<Element>, String> {
    let mut out = Vec::new();
    for el in elements {
        match el {
            Element::LetterRef(symbol) if !project.letters.contains(symbol) => {
                let segments = segments_of(symbol, project)?;
                if segments.is_empty() {
                    return Err(format!(
                        "rule '{rule_id}': letter reference '{symbol}' resolves to no segment — it is not a known letter or letter+diacritic sequence"
                    ));
                }
                out.extend(segments.into_iter().map(|s| Element::LetterBundle((*s).clone())));
            }
            Element::ModifiedLetter(symbol, delta) => {
                let segments = segments_of(symbol, project)?;
                let Some((last, prefix)) = segments.split_last() else {
                    return Err(format!(
                        "rule '{rule_id}': modified letter '{symbol}^[...]' resolves to no segment — its base is not a known letter or letter+diacritic sequence"
                    ));
                };
                let (seg, supra): (Vec<_>, Vec<_>) =
                    delta.items.iter().cloned().partition(|(f, _)| project.features.is_segmental(*f));
                out.extend(prefix.iter().map(|s| Element::LetterBundle((**s).clone())));
                let merged = merge(last, &FeatureBundle { items: seg }, &project.features, false);
                out.push(Element::LetterBundle(combine(&merged, &FeatureBundle { items: supra }, false)));
            }
            Element::Group(inner) => out.push(Element::Group(resolve_elements(inner, project, rule_id)?)),
            Element::Disjunction(branches) => out.push(Element::Disjunction(
                branches.iter().map(|b| resolve_elements(b, project, rule_id)).collect::<Result<_, _>>()?,
            )),
            Element::Negated(inner) => out.push(Element::Negated(Box::new(resolve_one(inner, project, rule_id)?))),
            Element::Quantified(inner, q) => {
                out.push(Element::Quantified(Box::new(resolve_one(inner, project, rule_id)?), *q))
            }
            Element::Bound(r, inner) => out.push(Element::Bound(*r, Box::new(resolve_one(inner, project, rule_id)?))),
            other => out.push(other.clone()),
        }
    }
    Ok(out)
}

fn resolve_one(el: &Element, project: &Project, rule_id: &str) -> Result<Element, String> {
    let mut resolved = resolve_elements(std::slice::from_ref(el), project, rule_id)?;
    Ok(if resolved.len() == 1 { resolved.pop().unwrap() } else { Element::Group(resolved) })
}

/// Resolve every letter+diacritic run a rule spells into per-segment bundles.
pub fn resolve_rule_letters(rules: &RuleInventory, project: &Project) -> Result<RuleInventory, String> {
    let mut out = RuleInventory::default();
    for (time, list) in &rules.by_time {
        let mut resolved = Vec::new();
        for rule in list {
            let sd = &rule.sd;
            let id = &rule.id;
            let new_sd = StructuralDescription {
                target: resolve_elements(&sd.target, project, id)?,
                result: resolve_elements(&sd.result, project, id)?,
                left_context: resolve_elements(&sd.left_context, project, id)?,
                right_context: resolve_elements(&sd.right_context, project, id)?,
                left_exception: resolve_elements(&sd.left_exception, project, id)?,
                right_exception: resolve_elements(&sd.right_exception, project, id)?,
            };
            resolved.push(Arc::new(Rule { sd: new_sd, ..(**rule).clone() }));
        }
        out.by_time.insert(*time, resolved);
    }
    Ok(out)
}

// ---- The engine -------------------------------------------------------------------------------

impl<'p> Engine<'p> {
    pub fn new(project: &'p Project) -> Result<Engine<'p>, String> {
        Self::with_rules(project, &project.rules)
    }

    pub fn with_rules(project: &'p Project, rules: &RuleInventory) -> Result<Engine<'p>, String> {
        let rules = resolve_rule_letters(rules, project)?;
        let syllable_features = FeatSet::from_ids(project.syllable_features.iter().copied());
        let schedule = rules
            .sorted_times()
            .into_iter()
            .map(|t| {
                let prepared = rules.by_time[&t]
                    .iter()
                    .map(|rule| PreparedRule {
                        demands: required_demands(&rule.sd, &project.letters, &syllable_features),
                        case_b: target_recalls_context_binding(&rule.sd),
                        parts: Parts::at(project, rule.time),
                        rule: rule.clone(),
                    })
                    .collect();
                (t, prepared)
            })
            .collect();
        let latest = rules.by_time.keys().flatten().copied().max().unwrap_or(0);
        Ok(Engine { project, rules, schedule, syllable_features, latest })
    }

    /// Resolve and prepare one rule outside the inventory (the inducer's candidates).
    pub fn prepare(&self, rule: &Rule) -> Result<PreparedRule, String> {
        let mut single = RuleInventory::default();
        single.by_time.insert(rule.time, vec![Arc::new(rule.clone())]);
        let resolved = resolve_rule_letters(&single, self.project)?;
        let rule = resolved.by_time[&rule.time][0].clone();
        Ok(PreparedRule {
            demands: required_demands(&rule.sd, &self.project.letters, &self.syllable_features),
            case_b: target_recalls_context_binding(&rule.sd),
            parts: Parts::at(self.project, rule.time),
            rule,
        })
    }

    /// Apply one prepared rule to a form, outside a derivation: `None` when it has no locus.
    pub fn apply_once(&self, prep: &PreparedRule, form: &Form) -> Option<Form> {
        let lowered = lower_tiers(form);
        let supply = word_supply(&lowered);
        self.apply_with(prep, form, &lowered, &supply)
    }

    /// [`Engine::apply_once`] with the form's lowered bundles and supply already computed.
    pub fn apply_with(&self, prep: &PreparedRule, form: &Form, lowered: &[Arc<FeatureBundle>], supply: &Supply) -> Option<Form> {
        match prep.rule.application {
            ApplicationMode::Simultaneous => {
                if cannot_match(&prep.demands, supply) {
                    return None;
                }
                let (boundaries, view) = self.syllable_context(lowered, &prep.parts, form);
                self.apply_simultaneous(prep, form, lowered, &boundaries, view.as_ref())
            }
            ApplicationMode::LeftToRight => self.apply_directional(prep, form, supply, false),
            ApplicationMode::RightToLeft => self.apply_directional(prep, form, supply, true),
        }
    }

    /// Whether a rule's output differs from its input once the tiers are lowered.
    pub fn fired(before: &Form, after: &Form) -> bool {
        fired(&lower_tiers(before), &lower_tiers(after))
    }

    fn ctx<'a>(&'a self, segs: &'a [Arc<FeatureBundle>], boundaries: &'a Boundaries, view: Option<&'a SyllableView>) -> MatchCtx<'a> {
        MatchCtx {
            segs,
            letters: &self.project.letters,
            boundaries,
            view,
            features: &self.project.features,
            syllable_features: &self.syllable_features,
        }
    }

    pub fn boundaries(&self, segments: &[Arc<FeatureBundle>], time: Option<i64>) -> Boundaries {
        syllabify_with(segments, &Parts::at(self.project, time), self.project).0
    }

    fn syllable_context(&self, lowered: &[Arc<FeatureBundle>], parts: &Parts, form: &Form) -> (Boundaries, Option<SyllableView>) {
        let (boundaries, _) = syllabify_with(lowered, parts, self.project);
        let Some(nucleus) = parts.nucleus_definition() else { return (boundaries, None) };
        let nuclei = nuclei_by_position(lowered, &boundaries, nucleus);
        let view = SyllableView { nuclei, floating: floating_autosegs(form) };
        (boundaries, Some(view))
    }

    /// Derive every word of the lexicon, in lexicon order, in parallel.
    pub fn derive_all(&self) -> Result<Vec<Derivation>, String> {
        let words: Vec<&Word> = self.project.words.values().collect();
        words.par_iter().map(|w| self.derive_word(w)).collect()
    }

    pub fn derive_word(&self, word: &Word) -> Result<Derivation, String> {
        let form = string_to_sequence(word.ipa(), self.project)?;
        Ok(self.derive(word, form))
    }

    pub fn derive(&self, word: &Word, form: Form) -> Derivation {
        let project = self.project;
        let seed_time = word.seed_time();
        let input = Arc::new(form);
        let mut current = input.clone();
        let mut lowered = lower_tiers(&current);
        let mut supply = word_supply(&lowered);
        let mut steps = Vec::new();
        let mut context_cache: Option<([usize; 3], Boundaries, Option<SyllableView>)> = None;
        let names = [word.id.as_str(), word.gloss.as_str(), word.ipa()];
        for (time, rules) in &self.schedule {
            if let (Some(t), Some(s)) = (time, seed_time)
                && t < &s {
                    continue;
                }
            for prep in rules {
                let rule = &prep.rule;
                if !rule.words.is_empty() && !rule.words.iter().any(|w| names.contains(&w.as_str())) {
                    continue;
                }
                if !rule.categories.is_empty() && !rule.categories.contains(&word.category_at(rule.time)) {
                    continue;
                }
                let after = match rule.application {
                    ApplicationMode::Simultaneous => {
                        if cannot_match(&prep.demands, &supply) {
                            continue;
                        }
                        let key = prep.parts.key();
                        if context_cache.as_ref().is_none_or(|(k, _, _)| *k != key) {
                            let (b, v) = self.syllable_context(&lowered, &prep.parts, &current);
                            context_cache = Some((key, b, v));
                        }
                        let (_, boundaries, view) = context_cache.as_ref().unwrap();
                        self.apply_simultaneous(prep, &current, &lowered, boundaries, view.as_ref())
                    }
                    ApplicationMode::LeftToRight => self.apply_directional(prep, &current, &supply, false),
                    ApplicationMode::RightToLeft => self.apply_directional(prep, &current, &supply, true),
                };
                let Some(after) = after else { continue };
                let after_lowered = lower_tiers(&after);
                if !fired(&lowered, &after_lowered) {
                    continue;
                }
                let after = self.maintain_tiers(after, rule.time);
                let before_boundaries = self.boundaries(&current.bundles(), rule.time);
                let after_boundaries = self.boundaries(&after.bundles(), rule.time);
                let after = Arc::new(after);
                steps.push(DerivationStep {
                    before: current.clone(),
                    rule: rule.clone(),
                    after: after.clone(),
                    before_boundaries,
                    after_boundaries,
                });
                current = after;
                lowered = lower_tiers(&current);
                supply = word_supply(&lowered);
                context_cache = None;
            }
        }
        let mut surface = (*current).clone();
        cleanup_tiers(&mut surface, &project.tiers, true);
        let surface_boundaries = self.boundaries(&surface.bundles(), Some(self.latest));
        Derivation { word: word.clone(), input, steps, surface: Arc::new(surface), surface_boundaries }
    }

    pub fn maintain_tiers(&self, mut form: Form, time: Option<i64>) -> Form {
        cleanup_tiers(&mut form, &self.project.tiers, false);
        let parts = Parts::at(self.project, time);
        let (boundaries, _) = syllabify_with(&form.bundles(), &parts, self.project);
        redock_to_nuclei(&mut form, &boundaries, parts.nucleus_definition());
        form
    }

    fn apply_simultaneous(
        &self,
        prep: &PreparedRule,
        form: &Form,
        lowered: &[Arc<FeatureBundle>],
        boundaries: &Boundaries,
        view: Option<&SyllableView>,
    ) -> Option<Form> {
        let sd = &prep.rule.sd;
        let cx = self.ctx(lowered, boundaries, view);
        let selected = select_non_overlapping(cx.find_matches(sd, prep.case_b));
        if selected.is_empty() {
            return None;
        }
        let mut out = form.clone();
        for m in selected.iter().rev() {
            let replacement = apply_match(sd, m, lowered, &self.project.letters, &self.project.features);
            self.splice(&mut out, form, lowered, m, replacement, false);
        }
        Some(out)
    }

    fn apply_directional(&self, prep: &PreparedRule, form: &Form, supply: &Supply, reverse: bool) -> Option<Form> {
        if cannot_match(&prep.demands, supply) {
            return None;
        }
        let sd = &prep.rule.sd;
        let mut work = form.clone();
        let mut cursor = if reverse { work.segments.len() as isize } else { 0 };
        let mut rewrote = false;
        loop {
            let bundles = lower_tiers(&work);
            let (boundaries, view) = self.syllable_context(&bundles, &prep.parts, &work);
            let cx = self.ctx(&bundles, &boundaries, view.as_ref());
            let matches = cx.find_matches(sd, prep.case_b);
            let chosen = if reverse {
                matches
                    .into_iter()
                    .filter(|m| m.end as isize <= cursor)
                    .max_by_key(|m| (m.end, std::cmp::Reverse(m.start)))
            } else {
                matches.into_iter().filter(|m| m.start as isize >= cursor).min_by_key(|m| m.start)
            };
            let Some(m) = chosen else { break };
            let replacement = apply_match(sd, &m, &bundles, &self.project.letters, &self.project.features);
            let produced = replacement.len();
            let snapshot = work.clone();
            self.splice(&mut work, &snapshot, &bundles, &m, replacement, true);
            rewrote = true;
            let no_op = m.end == m.start && produced == 0;
            cursor = if reverse {
                if no_op { m.start as isize - 1 } else { m.start as isize }
            } else if no_op {
                m.start as isize + 1
            } else {
                (m.start + produced) as isize
            };
        }
        if rewrote { Some(work) } else { None }
    }

    /// Splice one locus's replacement into *out*, routing carried features onto the tiers and
    /// carrying stranded suprasegmentals. *source* is the form the match was found in; with
    /// *live*, *out* is that same form being rewritten in place (a directional scan), so a spread
    /// reads its current links.
    fn splice(
        &self,
        out: &mut Form,
        source: &Form,
        source_bundles: &[Arc<FeatureBundle>],
        m: &Match,
        replacement: Vec<(FeatureBundle, Option<usize>)>,
        live: bool,
    ) {
        let tiers = &self.project.tiers;
        let mut new_segments = Vec::new();
        let mut written_tiers: Vec<String> = Vec::new();
        for (bundle, pos) in replacement {
            let (seg_bundle, carried) = split_carried(&bundle, tiers);
            let seg_id = match pos {
                Some(p) => source.segments[p].id,
                None => out.fresh_id(),
            };
            new_segments.push(Segment { bundle: Arc::new(seg_bundle), id: seg_id });
            let prev = match pos {
                Some(p) => split_carried(&source_bundles[p], tiers).1,
                None => Default::default(),
            };
            let mut names: Vec<String> = carried.keys().cloned().collect();
            names.extend(prev.keys().filter(|k| !carried.contains_key(*k)).cloned());
            for name in names {
                let empty = FeatureBundle::new();
                let written = carried.get(&name).unwrap_or(&empty);
                let recall = written.items.iter().find_map(|(_, v)| match v {
                    Value::One(Limb::Recall(r)) => Some(*r),
                    _ => None,
                });
                if let Some(recall) = recall {
                    spread_autoseg(out, source, &m.bindings, recall, &name, seg_id, live);
                } else if written != prev.get(&name).unwrap_or(&empty) {
                    write_to_tier(out, seg_id, &name, written);
                    written_tiers.push(name.clone());
                }
            }
        }
        let kept: Vec<u32> = new_segments.iter().map(|s| s.id).collect();
        let stranded: Vec<u32> =
            source.segments[m.start..m.end].iter().map(|s| s.id).filter(|id| !kept.contains(id)).collect();
        if !stranded.is_empty() {
            self.carry_stranded_suprasegmentals(out, &stranded, &new_segments, &written_tiers);
            carry_stranded_melody(out, source, m.start, m.end, &stranded, tiers);
        }
        out.segments.splice(m.start..m.end, new_segments);
    }

    fn carry_stranded_suprasegmentals(&self, out: &mut Form, stranded: &[u32], new_segments: &[Segment], written_tiers: &[String]) {
        for (name, decl) in &self.project.tiers {
            if !decl.carries.iter().any(|f| self.syllable_features.contains(*f)) {
                continue;
            }
            if written_tiers.contains(name) {
                continue;
            }
            let Some(tier) = out.tiers.get_mut(name) else { continue };
            let Some(new_anchor) = new_segments.iter().find(|s| matches_plain(&decl.anchor, &s.bundle)).map(|s| s.id)
            else {
                continue;
            };
            if !decl.melody && tier.links.iter().any(|(_, anchor)| *anchor == new_anchor) {
                continue;
            }
            tier.links = tier
                .links
                .iter()
                .map(|&(a, anchor)| (a, if stranded.contains(&anchor) { new_anchor } else { anchor }))
                .collect();
        }
    }

    /// The form and its boundaries after every timed rule with time ≤ *time* has fired.
    pub fn form_at_time(derivation: &Derivation, time: i64) -> (Arc<Form>, Boundaries) {
        let mut form = derivation.input.clone();
        let mut boundaries = match derivation.steps.first() {
            Some(step) => step.before_boundaries.clone(),
            None => derivation.surface_boundaries.clone(),
        };
        for step in &derivation.steps {
            match step.rule.time {
                Some(t) if t <= time => {
                    form = step.after.clone();
                    boundaries = step.after_boundaries.clone();
                }
                _ => {}
            }
        }
        (form, boundaries)
    }
}

fn select_non_overlapping(matches: Vec<Match>) -> Vec<Match> {
    let mut selected = Vec::new();
    let mut last_end = 0;
    for m in matches {
        if m.start >= last_end {
            last_end = m.end;
            selected.push(m);
        }
    }
    selected
}

fn fired(before: &[Arc<FeatureBundle>], after: &[Arc<FeatureBundle>]) -> bool {
    before.len() != after.len() || before.iter().zip(after).any(|(a, b)| a != b)
}

/// Every unanchored autosegment as `(id, bundle, gap)`; *gap* is the position it floats beside.
pub fn floating_autosegs(form: &Form) -> Vec<(u32, FeatureBundle, Option<usize>)> {
    let position: HashMap<u32, usize> = form.segments.iter().enumerate().map(|(i, s)| (s.id, i)).collect();
    let mut out = Vec::new();
    for tier in form.tiers.values() {
        for autoseg in &tier.autosegs {
            if tier.links.iter().any(|(a, _)| *a == autoseg.id) {
                continue;
            }
            let gap = tier.float_hosts.get(&autoseg.id).and_then(|(host, side)| {
                position.get(host).map(|&p| if *side == Side::After { p + 1 } else { p })
            });
            out.push((autoseg.id, autoseg.bundle.clone(), gap));
        }
    }
    out
}

fn spread_autoseg(out: &mut Form, source: &Form, b: &Bindings, recall: AutosegRecall, tier_name: &str, seg_id: u32, live: bool) {
    if let Some(&float_id) = map_get(&b.floating_reference, recall.r) {
        out.tier_mut(tier_name).links.insert((float_id, seg_id));
        return;
    }
    let tiers = if live { &out.tiers } else { &source.tiers };
    let (Some(&bound_position), Some(source_tier)) = (map_get(&b.autoseg_reference, recall.r), tiers.get(tier_name))
    else {
        return;
    };
    let bound_anchor = source.segments[bound_position].id;
    let links: Vec<(u32, u32)> = source_tier.links.iter().filter(|(_, anchor)| *anchor == bound_anchor).copied().collect();
    let out_tier = out.tier_mut(tier_name);
    for (a, _) in links {
        out_tier.links.insert((a, seg_id));
    }
}

fn carry_stranded_melody(out: &mut Form, source: &Form, start: usize, end: usize, stranded: &[u32], tiers: &TierInventory) {
    let left = if start > 0 { Some(source.segments[start - 1].id) } else { None };
    let right = source.segments.get(end).map(|s| s.id);
    for (name, decl) in tiers {
        if !decl.melody {
            continue;
        }
        let neighbour = if decl.stability == "right" { right } else { left };
        let (Some(neighbour), Some(tier)) = (neighbour, out.tiers.get_mut(name)) else { continue };
        tier.links = tier
            .links
            .iter()
            .map(|&(a, anchor)| (a, if stranded.contains(&anchor) { neighbour } else { anchor }))
            .collect();
    }
}
