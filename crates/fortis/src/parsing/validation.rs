//! Structural validation of a parsed rule: the well-formedness rules of the user guide's §2.

use std::collections::BTreeSet;

use crate::models::*;

#[derive(Default)]
struct Markers {
    binds: Vec<i64>,
    recalls: BTreeSet<i64>,
    alphas: BTreeSet<char>,
    labels: Vec<i64>,
    autoseg_binds: BTreeSet<i64>,
    autoseg_recalls: BTreeSet<i64>,
    node_refs: BTreeSet<i64>,
}

fn alphas_in(value: &Value) -> impl Iterator<Item = char> + '_ {
    value.limbs().iter().filter_map(|l| match l {
        Limb::Alpha(a) => Some(a.var),
        _ => None,
    })
}

fn autoseg_refs(value: &Value) -> (BTreeSet<i64>, BTreeSet<i64>) {
    let mut binds = BTreeSet::new();
    let mut recalls = BTreeSet::new();
    for limb in value.limbs() {
        match limb {
            Limb::Bind(b) => {
                binds.insert(b.r);
            }
            Limb::Recall(r) => {
                recalls.insert(r.r);
            }
            _ => {}
        }
    }
    (binds, recalls)
}

fn collect(elements: &[Element], m: &mut Markers, features: Option<&FeatureInventory>) {
    for element in elements {
        match element {
            Element::BundleElem(bundle) => {
                for spec in bundle {
                    note_spec(spec.feature, &spec.value, spec.condition_label, m, features);
                }
            }
            Element::ResultElem(bundle) => {
                for spec in bundle {
                    note_spec(spec.feature, &spec.value, spec.condition_label, m, features);
                }
            }
            Element::FloatingAutoseg(pattern) => {
                for spec in pattern {
                    let (b, r) = autoseg_refs(&spec.value);
                    m.autoseg_binds.extend(b);
                    m.autoseg_recalls.extend(r);
                }
            }
            Element::Bound(r, inner) => {
                m.binds.push(*r);
                collect(std::slice::from_ref(inner), m, features);
            }
            Element::RecallRef(r) => {
                m.recalls.insert(*r);
            }
            Element::Group(inner) => collect(inner, m, features),
            Element::Quantified(inner, _) | Element::Negated(inner) => {
                collect(std::slice::from_ref(inner), m, features)
            }
            Element::Disjunction(branches) => {
                for branch in branches {
                    collect(branch, m, features);
                }
            }
            _ => {}
        }
    }
}

fn note_spec(
    feature: FeatId,
    value: &Value,
    label: Option<i64>,
    m: &mut Markers,
    features: Option<&FeatureInventory>,
) {
    m.alphas.extend(alphas_in(value));
    let (binds, recalls) = autoseg_refs(value);
    if features.is_some_and(|f| f.is_segmental(feature)) {
        m.node_refs.extend(binds);
        m.node_refs.extend(recalls);
    } else {
        m.autoseg_binds.extend(binds);
        m.autoseg_recalls.extend(recalls);
    }
    if let Some(l) = label {
        m.labels.push(l);
    }
}

fn markers(elements: &[Element], features: Option<&FeatureInventory>) -> Markers {
    let mut m = Markers::default();
    collect(elements, &mut m, features);
    m
}

fn zero_width(e: &Element) -> bool {
    matches!(e, Element::WordBoundary | Element::SyllableBoundary | Element::FloatingAutoseg(_))
}

pub fn without_boundaries(elements: &[Element]) -> Vec<&Element> {
    elements.iter().filter(|e| !zero_width(e)).collect()
}

/// Whether a result element merges into a source segment (a feature bundle) or replaces it.
pub fn is_merge_bundle(element: &Element) -> bool {
    match element {
        Element::ResultElem(_) => true,
        Element::Quantified(inner, _) => is_merge_bundle(inner),
        _ => false,
    }
}

/// Every element in a sequence, descending into all nesting.
pub fn walk(elements: &[Element]) -> Vec<&Element> {
    let mut out = Vec::new();
    fn go<'a>(elements: &'a [Element], out: &mut Vec<&'a Element>) {
        for element in elements {
            out.push(element);
            match element {
                Element::Group(inner) => go(inner, out),
                Element::Disjunction(branches) => {
                    for b in branches {
                        go(b, out);
                    }
                }
                Element::Negated(inner) | Element::Quantified(inner, _) | Element::Bound(_, inner) => {
                    go(std::slice::from_ref(inner), out)
                }
                _ => {}
            }
        }
    }
    go(elements, &mut out);
    out
}

fn quant(e: &Element) -> Option<Quantifier> {
    match e {
        Element::Quantified(_, q) => Some(*q),
        _ => None,
    }
}

pub fn validate_structural_description(
    sd: &StructuralDescription,
    features: Option<&FeatureInventory>,
) -> Result<(), Vec<String>> {
    let mut errors = Vec::new();
    let target = markers(&sd.target, features);
    let result = markers(&sd.result, features);
    let left_ctx = markers(&sd.left_context, features);
    let right_ctx = markers(&sd.right_context, features);
    let left_exc = markers(&sd.left_exception, features);
    let right_exc = markers(&sd.right_exception, features);
    let all = [&target, &result, &left_ctx, &right_ctx, &left_exc, &right_exc];

    let target_count = without_boundaries(&sd.target).len();
    let result_count = without_boundaries(&sd.result).len();
    if target_count != result_count && sd.result.iter().any(is_merge_bundle) {
        errors.push(format!(
            "Ambiguous rule: target has {target_count} element(s) but result has {result_count}, and a result feature-bundle has no unambiguous target to merge with — a count mismatch is only allowed with letter-shorthand results"
        ));
    }

    let bound: BTreeSet<i64> = all.iter().flat_map(|m| m.binds.iter().copied()).collect();
    let recalled: BTreeSet<i64> = all.iter().flat_map(|m| m.recalls.iter().copied()).collect();
    for r in recalled.difference(&bound) {
        errors.push(format!("Recall '@{r}' has no matching binding '{r}='"));
    }
    for r in bound.difference(&recalled) {
        errors.push(format!("Binding '{r}=' is never recalled by '@{r}'"));
    }
    let result_binds: BTreeSet<i64> = result.binds.iter().copied().collect();
    for r in result_binds {
        errors.push(format!("Binding '{r}=' is not allowed in result position"));
    }

    let a_bound: BTreeSet<i64> = all.iter().flat_map(|m| m.autoseg_binds.iter().copied()).collect();
    let a_recalled: BTreeSet<i64> = all.iter().flat_map(|m| m.autoseg_recalls.iter().copied()).collect();
    for r in a_recalled.difference(&a_bound) {
        errors.push(format!("Tier recall '~{r}' has no matching binding '~{r}='"));
    }
    for r in a_bound.difference(&a_recalled) {
        errors.push(format!("Tier binding '~{r}=' is never recalled by '~{r}'"));
    }
    if walk(&sd.result).iter().any(|e| matches!(e, Element::FloatingAutoseg(_))) {
        errors.push("A floating autosegment '⟨...⟩' is not valid in result position".into());
    }

    let bound_alphas: BTreeSet<char> =
        target.alphas.iter().chain(&left_ctx.alphas).chain(&right_ctx.alphas).copied().collect();
    let used_alphas: BTreeSet<char> =
        result.alphas.iter().chain(&left_exc.alphas).chain(&right_exc.alphas).copied().collect();
    for var in used_alphas.difference(&bound_alphas) {
        errors.push(format!("Alpha variable '{var}' is used but never bound in target or context"));
    }

    let condition_labels: BTreeSet<i64> =
        target.labels.iter().chain(&left_ctx.labels).chain(&right_ctx.labels).copied().collect();
    let result_labels: BTreeSet<i64> = result.labels.iter().copied().collect();
    for l in result_labels.difference(&condition_labels) {
        errors.push(format!(
            "Conditional label '{l}' is applied in the result but has no condition in the target or context"
        ));
    }
    for l in condition_labels.difference(&result_labels) {
        errors.push(format!("Conditional label '{l}' is a condition but applies no result feature"));
    }

    let has_context = !sd.left_context.is_empty() || !sd.right_context.is_empty();
    for (label, position) in [
        ("left context", &sd.left_context),
        ("right context", &sd.right_context),
        ("left exception", &sd.left_exception),
        ("right exception", &sd.right_exception),
    ] {
        if walk(position).iter().any(|e| matches!(e, Element::Null)) {
            errors.push(format!("∅ (null) is not valid in {label} position"));
        }
    }
    for (label, side) in [("target", &sd.target), ("result", &sd.result)] {
        if !side.is_empty()
            && side.iter().all(|e| matches!(e, Element::WordBoundary | Element::SyllableBoundary))
        {
            errors.push(format!("A boundary may not be the only element in {label} position"));
        }
    }
    if sd.target.len() == 1 && matches!(sd.target[0], Element::Null) && !has_context {
        errors.push("∅ as the entire target requires a context".into());
    }
    if walk(&sd.result).iter().any(|e| matches!(e, Element::Negated(_))) {
        errors.push("Negation '!' is not valid in result position".into());
    }
    let positions = [
        &sd.target,
        &sd.result,
        &sd.left_context,
        &sd.right_context,
        &sd.left_exception,
        &sd.right_exception,
    ];
    if positions.iter().any(|p| {
        walk(p).iter().any(|e| {
            matches!(e, Element::Negated(inner) if matches!(**inner, Element::Null | Element::Wildcard))
        })
    }) {
        errors.push("Negation '!' may not be applied to ∅ or []".into());
    }

    let target_seq = without_boundaries(&sd.target);
    let result_seq = without_boundaries(&sd.result);
    if target_seq.len() == result_seq.len() {
        for (left, right) in target_seq.iter().zip(&result_seq) {
            if matches!(left, Element::Null) || matches!(right, Element::Null) {
                continue;
            }
            if is_merge_bundle(right) && quant(left) != quant(right) {
                errors.push(
                    "A merge-bundle result element must carry the same quantifier as its corresponding target element".into(),
                );
                break;
            }
        }
    }
    for (index, right) in result_seq.iter().enumerate() {
        if let Element::Disjunction(branches) = right {
            let ok = matches!(target_seq.get(index), Some(Element::Disjunction(t)) if t.len() == branches.len());
            if !ok {
                errors.push(
                    "A disjunction in result position needs a corresponding target disjunction with the same number of branches".into(),
                );
                break;
            }
        }
    }
    for (side, top_seq, elements) in
        [("target", &target_seq, &sd.target), ("result", &result_seq, &sd.result)]
    {
        let top_level = top_seq.iter().filter(|e| matches!(e, Element::Disjunction(_))).count();
        let total = walk(elements).iter().filter(|e| matches!(e, Element::Disjunction(_))).count();
        let nested = total - top_level;
        if top_level > 1 {
            errors.push(format!("at most one top-level disjunction per side (in the {side})"));
        }
        if nested > 0 && top_level > 0 {
            errors.push(format!(
                "a nested disjunction cannot coexist with a top-level disjunction (in the {side})"
            ));
        }
    }
    if errors.is_empty() { Ok(()) } else { Err(errors) }
}
