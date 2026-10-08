//! The lint: rule positions whose bundle can never match a segment, because a feature is
//! required present under a geometry node required absent.

use crate::engine::matching::matches_plain;
use crate::models::*;
use crate::parsing::bundles::parse_pattern_bundle;

/// The letters a feature bundle matches, in inventory order, and the inventory size: the
/// engine's own reading of the bundle.
pub fn match_set(raw: &str, project: &Project) -> Result<(Vec<String>, usize), String> {
    let mut raw = raw.trim();
    if raw.starts_with('[') && raw.ends_with(']') {
        raw = raw[1..raw.len() - 1].trim();
    }
    if raw.is_empty() {
        return Err("Enter a feature bundle, e.g. +front, +sonorant, -syllabic".into());
    }
    let pattern = parse_pattern_bundle(raw, &project.features).map_err(|e| e.join("; "))?;
    // A conditional, an alpha variable, or a recall needs a rule's bindings to mean anything.
    let offenders: Vec<&str> = pattern
        .iter()
        .filter(|spec| {
            spec.condition_label.is_some()
                || spec.value.limbs().iter().any(|l| matches!(l, Limb::Alpha(_)))
                || matches!(spec.value, Value::One(Limb::Bind(_) | Limb::Recall(_)))
        })
        .map(|spec| project.features.name(spec.feature))
        .collect();
    if !offenders.is_empty() {
        return Err(format!(
            "References (~n), agreement variables (α), and conditionals (<n: …>) only mean something inside a rule — remove: {}",
            offenders.join(", ")
        ));
    }
    let letters = &project.letters.letters;
    let matched = letters.iter().filter(|l| matches_plain(&pattern, &l.bundle)).map(|l| l.symbol.clone()).collect();
    Ok((matched, letters.len()))
}

pub struct Unsatisfiable {
    pub rule: String,
    pub time: Option<i64>,
    pub role: &'static str,
    pub label: String,
    pub reason: String,
}

fn token(f: FeatId, value: &Value, features: &FeatureInventory) -> String {
    let name = features.name(f).to_string();
    let Value::One(Limb::Int(n)) = value else {
        return if value.is_none() { format!("{name}: none") } else { name };
    };
    match features.kind(f) {
        FeatureKind::Binary => if *n == 1 { format!("+{name}") } else { format!("-{name}") },
        FeatureKind::Scalar => match features.get(f).label_of(*n) {
            Some(label) => format!("{name}: {label}"),
            None => name,
        },
        FeatureKind::Unary => name,
    }
}

fn bundle_positions(elements: &[Element], out: &mut Vec<PatternBundle>) {
    for el in elements {
        match el {
            Element::BundleElem(b) => out.push(b.clone()),
            Element::Group(inner) => bundle_positions(inner, out),
            Element::Bound(_, inner) | Element::Quantified(inner, _) => bundle_positions(std::slice::from_ref(inner), out),
            _ => {}
        }
    }
}

fn contradiction(bundle: &PatternBundle, features: &FeatureInventory) -> Option<String> {
    let absent: Vec<FeatId> = bundle
        .iter()
        .filter(|s| s.value.is_none() && !s.negated && s.condition_label.is_none())
        .map(|s| s.feature)
        .collect();
    if absent.is_empty() {
        return None;
    }
    for spec in bundle {
        if spec.condition_label.is_some() || !(!spec.value.is_none() || spec.negated) {
            continue;
        }
        for ancestor in features.ancestors(spec.feature) {
            if absent.contains(&ancestor) {
                return Some(format!(
                    "{} is required present, but its parent node {} is absent (`{}: none`)",
                    features.name(spec.feature),
                    features.name(ancestor),
                    features.name(ancestor)
                ));
            }
        }
    }
    None
}

pub fn unsatisfiable_rules(project: &Project) -> Vec<Unsatisfiable> {
    let features = &project.features;
    let mut findings = Vec::new();
    for rule in project.rules.in_file_order() {
        let name = rule.name.clone().unwrap_or_else(|| rule.id.clone());
        let sd = &rule.sd;
        for (role, elements) in [
            ("target", &sd.target),
            ("left context", &sd.left_context),
            ("right context", &sd.right_context),
            ("left exception", &sd.left_exception),
            ("right exception", &sd.right_exception),
        ] {
            let mut bundles = Vec::new();
            bundle_positions(elements, &mut bundles);
            for bundle in bundles {
                if let Some(reason) = contradiction(&bundle, features) {
                    let tokens: Vec<String> = bundle.iter().map(|s| token(s.feature, &s.value, features)).collect();
                    findings.push(Unsatisfiable {
                        rule: name.clone(),
                        time: rule.time,
                        role,
                        label: format!("[{}]", tokens.join(", ")),
                        reason,
                    });
                }
            }
        }
    }
    findings.sort_by_key(|f| f.time.unwrap_or(1 << 30));
    findings
}
