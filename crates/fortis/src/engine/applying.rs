//! Rewrite one matched span per the rule's result.

use super::combining::merge;
use super::matching::Match;
use crate::models::*;
use crate::parsing::validation::is_merge_bundle;

fn content(elements: &[Element]) -> Vec<&Element> {
    elements
        .iter()
        .filter(|e| !matches!(e, Element::WordBoundary | Element::SyllableBoundary | Element::FloatingAutoseg(_)))
        .collect()
}

fn resolve_disjunctions<'a>(content: Vec<&'a Element>, choices: &[usize]) -> Vec<&'a Element> {
    let mut out = Vec::new();
    let mut index = 0;
    for el in content {
        if let Element::Disjunction(branches) = el {
            out.extend(branches[choices[index]].iter());
            index += 1;
        } else {
            out.push(el);
        }
    }
    out
}

fn expand<'a>(content: &[&'a Element], count: Option<usize>) -> Vec<&'a Element> {
    let mut flat = Vec::new();
    for &el in content {
        match el {
            Element::Group(inner) => {
                let refs: Vec<&Element> = inner.iter().collect();
                flat.extend(expand(&refs, count));
            }
            Element::Quantified(inner, q) => {
                if q.max == Some(q.min) {
                    let one = expand(&[inner.as_ref()], count);
                    for _ in 0..q.min {
                        flat.extend(one.iter().copied());
                    }
                } else if let Some(n) = count {
                    let one = expand(&[inner.as_ref()], count);
                    for _ in 0..n {
                        flat.extend(one.iter().copied());
                    }
                } else {
                    flat.push(el);
                }
            }
            _ => flat.push(el),
        }
    }
    flat
}

fn min_width(el: &Element) -> Option<usize> {
    match el {
        Element::Null => Some(0),
        Element::Group(inner) => inner.iter().map(min_width).sum(),
        Element::Quantified(inner, q) if q.max == Some(q.min) => min_width(inner).map(|w| w * q.min),
        Element::Quantified(..) => None,
        Element::Bound(_, inner) => min_width(inner),
        _ => Some(1),
    }
}

fn variable_count(flat_target: &[&Element], span_width: usize) -> Option<usize> {
    let variable: Vec<&&Element> = flat_target.iter().filter(|e| matches!(e, Element::Quantified(..))).collect();
    if variable.is_empty() {
        return None;
    }
    let mut fixed = 0;
    for el in flat_target {
        if matches!(el, Element::Quantified(..)) {
            continue;
        }
        fixed += min_width(el)
            .expect("a variable-width non-quantifier element on the merge path is unsupported");
    }
    assert!(variable.len() == 1, "more than one variable-width element on the merge path (ambiguous span split)");
    let Element::Quantified(inner, _) = variable[0] else { unreachable!() };
    let inner_width = match min_width(inner) {
        Some(w) if w > 0 => w,
        _ => panic!("a variable quantifier with a non-fixed-width inner is refused"),
    };
    let remaining = span_width.checked_sub(fixed).expect("span width does not divide evenly across the quantifier");
    assert!(remaining % inner_width == 0, "span width does not divide evenly across the quantifier");
    Some(remaining / inner_width)
}

fn resolve_result_bundle(bundle: &[ResultSpec], b: &Bindings) -> FeatureBundle {
    let mut delta = FeatureBundle::new();
    for spec in bundle {
        if let Some(label) = spec.condition_label {
            let held = map_get(&b.conditions, label)
                .unwrap_or_else(|| panic!("conditional result feature (label {label}) has no condition recorded from matching"));
            if !held {
                continue;
            }
        }
        let recall = |r: &AlphaRef| {
            let bound = *map_get(&b.alpha, r.var).expect("alpha bound in matching");
            if r.op == AlphaOp::Opposite { opposite_pole(bound, r.unary) } else { bound }
        };
        let value = match &spec.value {
            Value::One(Limb::Alpha(r)) => Value::One(recall(r)),
            Value::Contour(limbs) => {
                let resolved: Vec<Limb> = limbs
                    .iter()
                    .map(|l| match l {
                        Limb::Alpha(r) => recall(r),
                        other => *other,
                    })
                    .collect();
                make_value(&resolved)
            }
            other => other.clone(),
        };
        delta.set(spec.feature, value);
    }
    delta
}

fn render_result_element(
    el: &Element,
    source: Option<&FeatureBundle>,
    b: &Bindings,
    letters: &LetterInventory,
    features: &FeatureInventory,
) -> Vec<FeatureBundle> {
    match el {
        Element::ResultElem(bundle) => {
            let mut base = source.cloned().unwrap_or_default();
            let mut node_recalls: Vec<(FeatId, i64)> = Vec::new();
            for spec in bundle {
                if let Value::One(Limb::Recall(r)) = spec.value {
                    let applies = spec.condition_label.is_none_or(|l| map_get(&b.conditions, l).copied().unwrap_or(false));
                    if features.is_segmental(spec.feature) && applies {
                        node_recalls.push((spec.feature, r.r));
                    }
                }
            }
            for (node, r) in &node_recalls {
                let cleared = FeatureBundle { items: vec![(*node, Value::NONE)] };
                base = merge(&base, &cleared, features, false);
                let captured = map_get(&b.node_reference, *r).cloned().unwrap_or_default();
                base = merge(&base, &captured, features, false);
            }
            let rest: Vec<ResultSpec> =
                bundle.iter().filter(|s| !node_recalls.iter().any(|(f, _)| *f == s.feature)).cloned().collect();
            let delta = resolve_result_bundle(&rest, b);
            vec![merge(&base, &delta, features, false)]
        }
        Element::LetterRef(symbol) => {
            let letter = letters
                .get(symbol)
                .unwrap_or_else(|| panic!("result letter '{symbol}' is not in the letter inventory"));
            vec![(*letter.bundle).clone()]
        }
        Element::LetterBundle(bundle) => vec![bundle.clone()],
        Element::RecallRef(r) => {
            let bound = map_get(&b.reference, *r).unwrap_or_else(|| panic!("result recall @{r} has no bound element"));
            bound.iter().map(|s| (**s).clone()).collect()
        }
        Element::Null => Vec::new(),
        Element::MorphemeBoundary => vec![morpheme_boundary_bundle()],
        other => panic!("result element {other:?} is not yet supported"),
    }
}

/// The `(bundle, source position)` pairs that replace `segments[m.start..m.end]`.
pub fn apply_match(
    sd: &StructuralDescription,
    m: &Match,
    segments: &[std::sync::Arc<FeatureBundle>],
    letters: &LetterInventory,
    features: &FeatureInventory,
) -> Vec<(FeatureBundle, Option<usize>)> {
    let span_width = m.end - m.start;
    let mut target = expand(&resolve_disjunctions(content(&sd.target), &m.target_choices), None);
    let mut result = expand(&resolve_disjunctions(content(&sd.result), &m.target_choices), None);
    if result.iter().any(|e| matches!(e, Element::Quantified(..))) {
        let count = variable_count(&target, span_width);
        target = expand(&target, count);
        result = expand(&result, count);
    }
    if !result.iter().any(|e| is_merge_bundle(e)) {
        return result
            .iter()
            .flat_map(|el| render_result_element(el, None, &m.bindings, letters, features))
            .map(|b| (b, None))
            .collect();
    }
    assert!(
        target.len() == result.len(),
        "merge result with unequal target/result counts is not supported (target {}, result {})",
        target.len(),
        result.len()
    );
    for el in &target {
        let ok = matches!(
            el,
            Element::BundleElem(_)
                | Element::LetterRef(_)
                | Element::LetterBundle(_)
                | Element::Wildcard
                | Element::RecallRef(_)
                | Element::Negated(_)
                | Element::Bound(..)
                | Element::Null
        );
        assert!(ok, "merge-path target element {el:?} is not yet supported");
    }
    let consumed = target.iter().filter(|e| !matches!(e, Element::Null)).count();
    assert!(consumed == span_width, "merge-path span width {span_width} does not match target {consumed}");
    let mut out = Vec::new();
    let mut cursor = m.start;
    for (t, r) in target.iter().zip(&result) {
        let (source, pos) = if matches!(t, Element::Null) {
            (None, None)
        } else {
            cursor += 1;
            (Some(&*segments[cursor - 1]), Some(cursor - 1))
        };
        let rendered = render_result_element(r, source, &m.bindings, letters, features);
        match (pos, rendered.len()) {
            (Some(p), 1) => out.push((rendered.into_iter().next().unwrap(), Some(p))),
            _ => out.extend(rendered.into_iter().map(|b| (b, None))),
        }
    }
    out
}
