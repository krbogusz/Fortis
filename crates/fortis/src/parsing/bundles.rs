//! Bundle and value parsing: realized, pattern and result material from strings.

use crate::models::*;
use crate::py;

const PRESENT: [&str; 3] = ["+", "1", "present"];
const ABSENT: [&str; 3] = ["-", "0", "absent"];
const UNSPECIFIED: [&str; 3] = ["∅", "none", "unspecified"];
const GREEK: [char; 25] = [
    'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'ς',
    'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
];

pub fn is_greek(c: char) -> bool {
    GREEK.contains(&c)
}

fn strip_spaces(s: &str) -> String {
    s.replace(' ', "")
}

/// Where *name* first occurs in *text* as a whole word: no ASCII letter or `_` touches it on
/// either side. A sign, a Greek variable or an `@` position may sit next to it (`+voice`, `αback`,
/// `tone@2`), but the `t` inside `nonexistent` is not the short name `t`.
fn find_word(text: &str, name: &str) -> Option<usize> {
    let is_word = |c: char| c.is_ascii_alphabetic() || c == '_';
    text.match_indices(name).map(|(i, _)| i).find(|&i| {
        let before = text[..i].chars().next_back();
        let after = text[i + name.len()..].chars().next();
        !before.is_some_and(is_word) && !after.is_some_and(is_word)
    })
}

/// The value part of a spec: *spaced* without the feature name that [`identify_feature`]
/// matched, and without spaces.
fn without_word(spaced: &str, name: &str) -> String {
    let i = find_word(spaced, name).unwrap();
    strip_spaces(&format!("{}{}", &spaced[..i], &spaced[i + name.len()..]))
}

/// The inner spec of a conditional `<n: F>`, with its spaces. Call it after [`split_conditional`]
/// has checked the form.
fn conditional_inner(spaced: &str) -> &str {
    let body = &spaced[1..spaced.len() - 1];
    body.split_once(':').map_or(body, |(_, inner)| inner)
}

/// The feature named in a spec string: longest full name first, then longest short name, each
/// searched as a whole word in the part before any `:`. *raw* keeps its spaces, since a space
/// separates words: in `mid tone`, `tone` is a word.
pub fn identify_feature(raw: &str, features: &FeatureInventory) -> Result<(FeatId, String), String> {
    let lhs = raw.split(':').next().unwrap_or("");
    for &id in features.names_by_length() {
        let name = &features.get(id).name;
        if find_word(lhs, name).is_some() {
            return Ok((id, name.clone()));
        }
    }
    for short in features.short_names_by_length() {
        if find_word(lhs, short).is_some() {
            return Ok((features.short_to_long(short).unwrap(), short.clone()));
        }
    }
    Err(format!("No feature could be identified from '{}'", strip_spaces(raw)))
}

fn scalar_label_requires_colon(
    feature: FeatId,
    raw_value: &str,
    had_colon: bool,
    features: &FeatureInventory,
) -> Option<String> {
    let f = features.get(feature);
    if had_colon || f.kind != FeatureKind::Scalar {
        return None;
    }
    if raw_value.split('>').any(|limb| f.values.iter().any(|(_, label)| label == limb)) {
        return Some(format!(
            "Scalar feature '{}': a value label must follow a colon (write '{}: {}', not a bare label)",
            f.name, f.name, raw_value
        ));
    }
    None
}

pub fn split_conditional(raw: &str) -> Result<(i64, String), String> {
    if !raw.ends_with('>') {
        return Err(format!("Malformed conditional feature (missing closing '>'): '{raw}'"));
    }
    let inner_all = &raw[1..raw.len() - 1];
    let Some((label_str, inner)) = inner_all.split_once(':') else {
        return Err(format!("Conditional feature is missing its ':' label separator: '{raw}'"));
    };
    let Some(label) = py::parse_int(label_str) else {
        return Err(format!("Conditional feature label must be an integer: '{raw}'"));
    };
    if inner.is_empty() {
        return Err(format!("Conditional feature has no inner spec: '{raw}'"));
    }
    Ok((label, inner.to_string()))
}

pub fn determine_contour_position(s: &str) -> Result<ContourPosition, String> {
    if s.contains("initial") {
        return Ok(ContourPosition::Edge(ContourEdge::Initial));
    }
    if s.contains("final") {
        return Ok(ContourPosition::Edge(ContourEdge::Final));
    }
    if s.contains("all") {
        return Ok(ContourPosition::Edge(ContourEdge::All));
    }
    if s.contains("any") {
        return Ok(ContourPosition::Edge(ContourEdge::Any));
    }
    if s.contains(';') {
        let mut list = Vec::new();
        for piece in s.split(';') {
            match py::parse_int(piece) {
                None => return Err(format!("Could not identify contour specification from '{s}'")),
                Some(n) if n < 1 => {
                    return Err(format!("Contour position cannot be smaller than 1: '{s}'"));
                }
                Some(n) => list.push(n),
            }
        }
        return Ok(ContourPosition::List(list));
    }
    match py::parse_int(s) {
        None => Err(format!("Could not identify contour specification from '{s}'")),
        Some(n) if n < 1 => Err(format!("Contour position cannot be smaller than 1: '{s}'")),
        Some(n) => Ok(ContourPosition::Index(n)),
    }
}

pub fn parse_kind_value(raw: &str, feature: FeatId, features: &FeatureInventory) -> Result<Limb, String> {
    let f = features.get(feature);
    match f.kind {
        FeatureKind::Unary => {
            if PRESENT.contains(&raw) {
                return Ok(Limb::Int(1));
            }
            if raw == "0" || raw == "-" {
                return Err(format!("Unary features don't support 'absent' values like '{raw}'"));
            }
        }
        FeatureKind::Binary => {
            if PRESENT.contains(&raw) {
                return Ok(Limb::Int(1));
            }
            if ABSENT.contains(&raw) {
                return Ok(Limb::Int(0));
            }
        }
        FeatureKind::Scalar => {
            if let Some(n) = py::parse_int(raw)
                && f.values.iter().any(|(k, _)| *k == n) {
                    return Ok(Limb::Int(n));
                }
            if let Some((k, _)) = f.values.iter().find(|(_, label)| label == raw) {
                return Ok(Limb::Int(*k));
            }
        }
    }
    Err(format!("Could not identify value for '{}' from string '{raw}'", f.name))
}

/// The shared bundle loop: comma-split, parse each spec, collect every error.
fn parse_bundle_with<S, F>(
    raw: &str,
    features: &FeatureInventory,
    feature_of: impl Fn(&S) -> FeatId,
    parse: F,
) -> Result<Vec<S>, Vec<String>>
where
    F: Fn(&str, &FeatureInventory) -> Result<S, String>,
{
    let mut errors = Vec::new();
    let mut bundle: Vec<S> = Vec::new();
    for piece in raw.split(',') {
        let piece = py::strip(piece);
        if piece.is_empty() {
            continue;
        }
        match parse(piece, features) {
            Err(e) => errors.push(e),
            Ok(spec) => {
                let f = feature_of(&spec);
                if let Some(slot) = bundle.iter_mut().find(|s| feature_of(s) == f) {
                    errors.push(format!(
                        "feature '{}' is specified more than once",
                        features.name(f)
                    ));
                    *slot = spec;
                } else {
                    bundle.push(spec);
                }
            }
        }
    }
    if errors.is_empty() { Ok(bundle) } else { Err(errors) }
}

// ---- Realized ---------------------------------------------------------------------------------

pub fn parse_feature_bundle(raw: &str, features: &FeatureInventory) -> Result<FeatureBundle, Vec<String>> {
    parse_bundle_with(raw, features, |s: &(FeatId, Value)| s.0, |p, f| parse_feature_spec(p, f, None))
        .map(|items| FeatureBundle { items })
}

pub fn parse_feature_spec(
    raw: &str,
    features: &FeatureInventory,
    feature: Option<FeatId>,
) -> Result<(FeatId, Value), String> {
    let spaced = raw.trim();
    let raw = strip_spaces(raw);
    let (feature, raw_value, had_colon) = match feature {
        None => {
            let Ok((feature, matched)) = identify_feature(spaced, features) else {
                return Err(format!("Could not identify feature spec from string '{raw}'"));
            };
            let raw_value = without_word(spaced, &matched).replace(':', "");
            (feature, raw_value, raw.contains(':'))
        }
        Some(feature) => {
            let raw_value = raw.strip_prefix(':').unwrap_or(&raw).to_string();
            (feature, raw_value, true)
        }
    };
    let f = features.get(feature);
    if raw_value.is_empty() {
        if f.kind == FeatureKind::Unary {
            return Ok((feature, Value::int(1)));
        }
        return Err(format!(
            "Realized feature '{}' needs an explicit value; a bare feature name matches any value and is pattern-only",
            f.name
        ));
    }
    if raw_value.contains('!') {
        return Err("Realized feature specifications don't support negation".into());
    }
    if raw_value.contains('@') {
        return Err("Realized feature specifications don't support contour positions".into());
    }
    if let Some(e) = scalar_label_requires_colon(feature, &raw_value, had_colon, features) {
        return Err(e);
    }
    let value = if raw_value.contains('>') {
        let mut limbs = Vec::new();
        for piece in raw_value.split('>') {
            limbs.push(parse_feature_value(piece, feature, features)?);
        }
        make_value(&limbs)
    } else {
        Value::One(parse_feature_value(&raw_value, feature, features)?)
    };
    Ok((feature, value))
}

fn parse_feature_value(raw: &str, feature: FeatId, features: &FeatureInventory) -> Result<Limb, String> {
    if UNSPECIFIED.contains(&raw) {
        return Ok(Limb::None);
    }
    if raw.chars().any(is_greek) {
        return Err("Alpha value notation is not supported for realized features".into());
    }
    if raw.contains('@') {
        return Err("Realized feature specifications don't support contour positions".into());
    }
    parse_kind_value(raw, feature, features)
}

// ---- Pattern ----------------------------------------------------------------------------------

pub fn parse_pattern_bundle(raw: &str, features: &FeatureInventory) -> Result<PatternBundle, Vec<String>> {
    parse_bundle_with(raw, features, |s: &PatternSpec| s.feature, parse_pattern_spec)
}

fn negation_prefix(raw_value: &str) -> bool {
    let mut chars = raw_value.chars();
    chars.next() == Some('!') && !chars.next().is_some_and(is_greek)
}

pub fn parse_pattern_spec(raw: &str, features: &FeatureInventory) -> Result<PatternSpec, String> {
    let spaced = raw.trim();
    let raw = strip_spaces(raw);
    if raw.starts_with('<') {
        let (label, _) = split_conditional(&raw)?;
        let mut spec = parse_pattern_spec(conditional_inner(spaced), features)?;
        spec.condition_label = Some(label);
        return Ok(spec);
    }
    let (feature, matched) = identify_feature(spaced, features)?;
    let mut raw_value = without_word(spaced, &matched).replace(':', "");
    let had_colon = raw.contains(':');
    let mut negated = false;
    if negation_prefix(&raw_value) {
        negated = true;
        raw_value.remove(0);
    }
    if raw_value.is_empty() {
        let value = if features.get(feature).kind == FeatureKind::Unary {
            Value::int(1)
        } else {
            Value::One(Limb::Any)
        };
        let spec = PatternSpec {
            feature,
            value,
            negated,
            contour_position: ContourPosition::Edge(ContourEdge::Any),
            condition_label: None,
        };
        validate_pattern_spec(&spec, features).map_err(|e| e.join("\n"))?;
        return Ok(spec);
    }
    let mut position = ContourPosition::Edge(ContourEdge::Any);
    let mut assigned = false;
    if raw_value.contains('@') {
        let after = raw_value.split('@').nth(1).unwrap_or("").to_string();
        position = determine_contour_position(&after)?;
        assigned = true;
        raw_value = raw_value.split('@').next().unwrap_or("").to_string();
    }
    if let Some(e) = scalar_label_requires_colon(feature, &raw_value, had_colon, features) {
        return Err(e);
    }
    let value = if raw_value.contains('>') {
        if !assigned {
            position = ContourPosition::Edge(ContourEdge::All);
        }
        let mut limbs = Vec::new();
        for piece in raw_value.split('>') {
            limbs.push(parse_pattern_value(piece, feature, features)?);
        }
        make_value(&limbs)
    } else {
        Value::One(parse_pattern_value(&raw_value, feature, features)?)
    };
    let spec = PatternSpec { feature, value, negated, contour_position: position, condition_label: None };
    validate_pattern_spec(&spec, features).map_err(|e| e.join("\n"))?;
    Ok(spec)
}

fn opposite_alpha_on_scalar(feature: FeatId, value: &Value, features: &FeatureInventory) -> Option<String> {
    let f = features.get(feature);
    if f.kind != FeatureKind::Scalar {
        return None;
    }
    if value
        .limbs()
        .iter()
        .any(|l| matches!(l, Limb::Alpha(a) if a.op == AlphaOp::Opposite))
    {
        return Some(format!(
            "Alpha-opposite ('-α') is not valid for scalar feature '{}' (binary/unary only)",
            f.name
        ));
    }
    None
}

fn spec_repr(spec: &PatternSpec, features: &FeatureInventory) -> String {
    format!("{}: {:?} @ {:?}", features.name(spec.feature), spec.value, spec.contour_position)
}

pub fn validate_pattern_spec(spec: &PatternSpec, features: &FeatureInventory) -> Result<(), Vec<String>> {
    let mut errors = Vec::new();
    if let Some(m) = opposite_alpha_on_scalar(spec.feature, &spec.value, features) {
        errors.push(m);
    }
    if let Value::Contour(limbs) = &spec.value {
        if let ContourPosition::Index(_) = spec.contour_position {
            errors.push(format!(
                "Contour position for a contour must be a list or an edge: '{}'",
                spec_repr(spec, features)
            ));
        }
        if let ContourPosition::List(list) = &spec.contour_position {
            if limbs.len() != list.len() {
                errors.push(format!(
                    "Contour position and a contour must be the same length: '{}'",
                    spec_repr(spec, features)
                ));
            }
            for i in 1..list.len() {
                if list[i] - list[i - 1] != 1 {
                    errors.push(format!(
                        "Contour positions must be contiguous: '{}'",
                        spec_repr(spec, features)
                    ));
                }
            }
        }
    }
    if errors.is_empty() { Ok(()) } else { Err(errors) }
}

fn parse_autoseg_ref(raw: &str, feature: FeatId, features: &FeatureInventory) -> Result<Limb, String> {
    let rest = &raw['~'.len_utf8()..];
    let (ref_part, sep, value_str) = match rest.split_once('=') {
        Some((a, b)) => (a, true, b),
        None => (rest, false, ""),
    };
    let optional = ref_part.ends_with('?');
    let ref_str = if optional { &ref_part[..ref_part.len() - 1] } else { ref_part };
    if !py::is_digit_str(ref_str) {
        return Err(format!("tier reference '{raw}' must be ~ followed by a reference number"));
    }
    let r: i64 = ref_str.parse().map_err(|_| format!("tier reference '{raw}' is too large"))?;
    if !sep {
        return Ok(Limb::Recall(AutosegRecall { r, optional }));
    }
    match parse_kind_value(value_str, feature, features)? {
        Limb::Int(value) => Ok(Limb::Bind(AutosegBind { r, value, optional })),
        _ => unreachable!("a kind value is an integer"),
    }
}

/// An alpha reference inside *raw*, with its op read off the character before the letter.
fn alpha_in(raw: &str) -> Option<(char, Option<char>)> {
    let chars: Vec<char> = raw.chars().collect();
    for g in GREEK {
        if let Some(i) = chars.iter().position(|&c| c == g) {
            return Some((g, if i > 0 { Some(chars[i - 1]) } else { None }));
        }
    }
    None
}

fn parse_pattern_value(raw: &str, feature: FeatId, features: &FeatureInventory) -> Result<Limb, String> {
    if UNSPECIFIED.contains(&raw) {
        return Ok(Limb::None);
    }
    if raw.starts_with('~') {
        return parse_autoseg_ref(raw, feature, features);
    }
    if let Some((var, prev)) = alpha_in(raw) {
        let op = match prev {
            Some('-') => AlphaOp::Opposite,
            Some('!') => AlphaOp::Other,
            _ => AlphaOp::Same,
        };
        let unary = features.get(feature).kind == FeatureKind::Unary;
        return Ok(Limb::Alpha(AlphaRef { var, op, unary }));
    }
    parse_kind_value(raw, feature, features)
}

// ---- Result -----------------------------------------------------------------------------------

pub fn parse_result_bundle(raw: &str, features: &FeatureInventory) -> Result<ResultBundle, Vec<String>> {
    parse_bundle_with(raw, features, |s: &ResultSpec| s.feature, parse_result_spec)
}

pub fn parse_result_spec(raw: &str, features: &FeatureInventory) -> Result<ResultSpec, String> {
    let spaced = raw.trim();
    let raw = strip_spaces(raw);
    if raw.starts_with('<') {
        let (label, _) = split_conditional(&raw)?;
        let mut spec = parse_result_spec(conditional_inner(spaced), features)?;
        spec.condition_label = Some(label);
        return Ok(spec);
    }
    let (feature, matched) = identify_feature(spaced, features)?;
    let raw_value = without_word(spaced, &matched).replace(':', "");
    let had_colon = raw.contains(':');
    if negation_prefix(&raw_value) {
        return Err("Result spec does not support negation".into());
    }
    if raw_value.contains('@') {
        return Err("Result spec does not support contour position".into());
    }
    if let Some(e) = scalar_label_requires_colon(feature, &raw_value, had_colon, features) {
        return Err(e);
    }
    let value = if raw_value.is_empty() {
        if features.get(feature).kind == FeatureKind::Unary {
            Value::int(1)
        } else {
            return Err(format!(
                "Could not identify value for '{}' from string '{raw}'",
                features.name(feature)
            ));
        }
    } else if raw_value.contains('>') {
        let mut limbs = Vec::new();
        for piece in raw_value.split('>') {
            limbs.push(parse_result_value(piece, feature, features)?);
        }
        make_value(&limbs)
    } else {
        Value::One(parse_result_value(&raw_value, feature, features)?)
    };
    if let Some(m) = opposite_alpha_on_scalar(feature, &value, features) {
        return Err(m);
    }
    Ok(ResultSpec { feature, value, condition_label: None })
}

fn parse_result_value(raw: &str, feature: FeatId, features: &FeatureInventory) -> Result<Limb, String> {
    if UNSPECIFIED.contains(&raw) {
        return Ok(Limb::None);
    }
    if raw.starts_with('~') {
        return parse_autoseg_ref(raw, feature, features);
    }
    if let Some((var, prev)) = alpha_in(raw) {
        let op = match prev {
            Some('-') => AlphaOp::Opposite,
            Some('!') => return Err("Result spec does not support 'other' alpha notation".into()),
            _ => AlphaOp::Same,
        };
        let unary = features.get(feature).kind == FeatureKind::Unary;
        return Ok(Limb::Alpha(AlphaRef { var, op, unary }));
    }
    parse_kind_value(raw, feature, features)
}
