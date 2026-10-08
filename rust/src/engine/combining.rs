//! Bundle algebra: combine, geometry-aware merge, and comparison.

use crate::models::*;

/// *other* over *base*: a feature in both takes *other*'s value, or forms a contour.
pub fn combine(base: &FeatureBundle, other: &FeatureBundle, form_contours: bool) -> FeatureBundle {
    let mut result = base.clone();
    for (f, v) in &other.items {
        match result.get(*f) {
            Some(existing) if form_contours => {
                let contour = form_contour(existing, v);
                result.set(*f, contour);
            }
            _ => result.set(*f, v.clone()),
        }
    }
    result
}

/// `combine`, then delink every node set to `none` with its subtree, and imply the unary
/// ancestors of every feature the delta set.
pub fn merge(base: &FeatureBundle, delta: &FeatureBundle, features: &FeatureInventory, form_contours: bool) -> FeatureBundle {
    let mut merged = combine(base, delta, form_contours);
    let mut drop: Vec<FeatId> = Vec::new();
    for (f, v) in &merged.items {
        if v.is_none() {
            drop.push(*f);
            drop.extend_from_slice(features.descendants(*f));
        }
    }
    if !drop.is_empty() {
        merged.items.retain(|(f, _)| !drop.contains(f));
    }
    for f in delta.keys() {
        if !merged.contains(f) || f == MORPHEME_BOUNDARY {
            continue;
        }
        for ancestor in features.ancestors(f) {
            if !merged.contains(ancestor)
                && features.kind(ancestor) == FeatureKind::Unary
                && features.parent(ancestor).is_some()
            {
                merged.set(ancestor, Value::int(1));
            }
        }
    }
    merged
}

/// The features whose presence or value differs between two bundles.
pub fn differing(a: &FeatureBundle, b: &FeatureBundle) -> Vec<FeatId> {
    let mut diffs = Vec::new();
    for (f, v) in &a.items {
        if b.get(*f) != Some(v) {
            diffs.push(*f);
        }
    }
    for (f, _) in &b.items {
        if !a.contains(*f) {
            diffs.push(*f);
        }
    }
    diffs
}
