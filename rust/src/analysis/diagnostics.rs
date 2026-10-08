//! The lint: rule positions whose bundle can never match a segment, because a feature is
//! required present under a geometry node required absent.

use crate::models::*;

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
