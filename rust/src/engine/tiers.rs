//! Autosegmental tier operations over a form.

use std::collections::HashMap;
use std::sync::Arc;

use indexmap::IndexMap;

use super::matching::matches_plain;
use super::syllabifying::syllables;
use crate::models::*;

/// Lift each declared tier's features off its anchor segments into autosegments.
pub fn associate_tiers(form: &mut Form, tiers: &TierInventory) {
    for (name, decl) in tiers {
        let mut tier = AutosegmentalTier::default();
        for i in 0..form.segments.len() {
            let segment = &form.segments[i];
            if !matches_plain(&decl.anchor, &segment.bundle) {
                continue;
            }
            let carried: Vec<(FeatId, Value)> = decl
                .carries
                .iter()
                .filter_map(|f| segment.bundle.get(*f).map(|v| (*f, v.clone())))
                .collect();
            if carried.is_empty() {
                continue;
            }
            let seg_id = segment.id;
            let id = form.fresh_id();
            tier.autosegs.push(Autoseg { bundle: FeatureBundle { items: carried }, id });
            tier.links.insert((id, seg_id));
        }
        form.tiers.insert(name.clone(), tier);
    }
    let carried: Vec<FeatId> = tiers.values().flat_map(|d| d.carries.iter().copied()).collect();
    if !carried.is_empty() {
        for segment in &mut form.segments {
            if segment.bundle.keys().any(|f| carried.contains(&f)) {
                let items = segment.bundle.items.iter().filter(|(f, _)| !carried.contains(f)).cloned().collect();
                segment.bundle = Arc::new(FeatureBundle { items });
            }
        }
    }
}

fn collapse(by_feature: IndexMap<FeatId, Vec<Value>>) -> FeatureBundle {
    let items = by_feature
        .into_iter()
        .map(|(f, values)| {
            if values.len() == 1 {
                (f, values.into_iter().next().unwrap())
            } else {
                let limbs: Vec<Limb> = values.iter().flat_map(|v| v.limbs().iter().copied()).collect();
                (f, make_value(&limbs))
            }
        })
        .collect();
    FeatureBundle { items }
}

fn carried_by_anchor(form: &Form) -> HashMap<u32, FeatureBundle> {
    let mut by_anchor: HashMap<u32, IndexMap<FeatId, Vec<Value>>> = HashMap::new();
    for tier in form.tiers.values() {
        if tier.links.is_empty() {
            continue;
        }
        let mut anchors_of: HashMap<u32, Vec<u32>> = HashMap::new();
        for &(autoseg, anchor) in &tier.links {
            anchors_of.entry(autoseg).or_default().push(anchor);
        }
        for autoseg in &tier.autosegs {
            for anchor in anchors_of.get(&autoseg.id).into_iter().flatten() {
                let features = by_anchor.entry(*anchor).or_default();
                for (f, v) in &autoseg.bundle.items {
                    features.entry(*f).or_default().push(v.clone());
                }
            }
        }
    }
    by_anchor.into_iter().map(|(a, f)| (a, collapse(f))).collect()
}

/// Each segment's bundle with its carried (tier) features merged back in.
pub fn lower_tiers(form: &Form) -> Vec<Arc<FeatureBundle>> {
    if form.tiers.values().all(|t| t.links.is_empty()) {
        return form.bundles();
    }
    let carried = carried_by_anchor(form);
    form.segments
        .iter()
        .map(|s| match carried.get(&s.id) {
            None => s.bundle.clone(),
            Some(extra) => {
                let mut b = (*s.bundle).clone();
                for (f, v) in &extra.items {
                    b.set(*f, v.clone());
                }
                Arc::new(b)
            }
        })
        .collect()
}

/// Prune links to deleted segments, apply the OCP, and (at the surface) stray-erase.
pub fn cleanup_tiers(form: &mut Form, tiers: &TierInventory, surface: bool) {
    let live: std::collections::HashSet<u32> = form.segments.iter().map(|s| s.id).collect();
    let position: HashMap<u32, usize> = form.segments.iter().enumerate().map(|(i, s)| (s.id, i)).collect();
    for (name, tier) in form.tiers.iter_mut() {
        let decl = tiers.get(name);
        tier.links.retain(|(_, anchor)| live.contains(anchor));
        if decl.is_some_and(|d| d.ocp) {
            merge_adjacent_identical(tier, &position);
        }
        if surface && decl.is_some_and(|d| d.stray_erase) {
            let linked: std::collections::HashSet<u32> = tier.links.iter().map(|(a, _)| *a).collect();
            tier.autosegs.retain(|a| linked.contains(&a.id));
        }
    }
}

fn merge_adjacent_identical(tier: &mut AutosegmentalTier, position: &HashMap<u32, usize>) {
    let leftmost = |id: u32| {
        tier.links.iter().filter(|(a, _)| *a == id).map(|(_, anchor)| position[anchor]).min().unwrap_or(usize::MAX)
    };
    let mut keyed: Vec<(usize, Autoseg)> = tier.autosegs.iter().map(|a| (leftmost(a.id), a.clone())).collect();
    keyed.sort_by_key(|(k, _)| *k);
    let mut kept: Vec<Autoseg> = Vec::new();
    for (_, autoseg) in keyed {
        match kept.last() {
            Some(last) if last.bundle == autoseg.bundle => {
                let survivor = last.id;
                tier.links = tier
                    .links
                    .iter()
                    .map(|&(a, anchor)| (if a == autoseg.id { survivor } else { a }, anchor))
                    .collect();
            }
            _ => kept.push(autoseg),
        }
    }
    tier.autosegs = kept;
}

/// Split a written bundle into the part that stays on the segment and the part bound for each
/// tier.
pub fn split_carried(bundle: &FeatureBundle, tiers: &TierInventory) -> (FeatureBundle, IndexMap<String, FeatureBundle>) {
    let mut segment = FeatureBundle::new();
    let mut by_tier: IndexMap<String, FeatureBundle> = IndexMap::new();
    for (f, v) in &bundle.items {
        match tiers.iter().find(|(_, d)| d.carries.contains(f)) {
            None => segment.items.push((*f, v.clone())),
            Some((name, _)) => by_tier.entry(name.clone()).or_default().items.push((*f, v.clone())),
        }
    }
    (segment, by_tier)
}

/// Delink the segment's autosegment on the tier and, if *carried* has a present value, link a
/// fresh one.
pub fn write_to_tier(form: &mut Form, segment_id: u32, tier_name: &str, carried: &FeatureBundle) {
    let present: Vec<(FeatId, Value)> = carried.items.iter().filter(|(_, v)| !v.is_none()).cloned().collect();
    let id = if present.is_empty() { None } else { Some(form.fresh_id()) };
    let tier = form.tier_mut(tier_name);
    tier.links.retain(|(_, anchor)| *anchor != segment_id);
    if let Some(id) = id {
        tier.autosegs.push(Autoseg { bundle: FeatureBundle { items: present }, id });
        tier.links.insert((id, segment_id));
    }
}

/// Move every link on a non-nucleus segment onto its syllable's nucleus.
pub fn redock_to_nuclei(form: &mut Form, boundaries: &Boundaries, nucleus: Option<&PatternBundle>) {
    let Some(nucleus) = nucleus else { return };
    let bundles = form.bundles();
    let mut nucleus_for: HashMap<usize, u32> = HashMap::new();
    for syl in syllables(&bundles, boundaries, Some(nucleus)) {
        let Some(n) = syl.nucleus else { continue };
        let id = form.segments[n].id;
        for p in syl.start..syl.end {
            nucleus_for.insert(p, id);
        }
    }
    let position: HashMap<u32, usize> = form.segments.iter().enumerate().map(|(i, s)| (s.id, i)).collect();
    for tier in form.tiers.values_mut() {
        tier.links = tier
            .links
            .iter()
            .map(|&(a, anchor)| {
                let target = position.get(&anchor).and_then(|p| nucleus_for.get(p)).copied().unwrap_or(anchor);
                (a, target)
            })
            .collect();
    }
}
