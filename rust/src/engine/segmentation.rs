//! Turning an IPA string into a form: letters and diacritics by greedy longest match.

use super::combining::combine;
use super::matching::matches_plain;
use super::tiers::associate_tiers;
use crate::models::*;

fn is_nucleus(segment: &FeatureBundle, project: &Project) -> bool {
    project.syllable_parts.nucleus_definition(Some(project.time)).is_some_and(|d| matches_plain(d, segment))
}

fn split_suprasegmentals(segment: &FeatureBundle, project: &Project) -> (FeatureBundle, FeatureBundle) {
    let is_syl = |f: FeatId| project.features.is_syllable(f);
    if !segment.keys().any(is_syl) {
        return (segment.clone(), FeatureBundle::new());
    }
    let (syl, seg): (Vec<_>, Vec<_>) = segment.items.iter().cloned().partition(|(f, _)| is_syl(*f));
    (FeatureBundle { items: seg }, FeatureBundle { items: syl })
}

fn parse_float_tone(inner: &str, project: &Project) -> Result<FeatureBundle, String> {
    let mut bundle = FeatureBundle::new();
    for ch in inner.chars() {
        if ch == '◌' || crate::py::is_space(ch) {
            continue;
        }
        let Some(d) = project.diacritics.get(&ch.to_string()) else {
            return Err(format!("floating tone '⟨{inner}⟩' has no diacritic '{ch}'"));
        };
        bundle = combine(&bundle, &d.bundle, d.contour);
    }
    Ok(bundle)
}

/// Segment *raw* into a form, each segment id-tagged, with the tiers associated.
pub fn string_to_sequence(raw: &str, project: &Project) -> Result<Form, String> {
    let mut segments: Vec<FeatureBundle> = Vec::new();
    let mut floats: Vec<(FeatureBundle, (u32, Side))> = Vec::new();
    let mut buffer = FeatureBundle::new();
    let mut syllable_buffer = FeatureBundle::new();
    let mut last_nucleus: Option<usize> = None;
    let mut i = 0;
    let position = |byte: usize| raw[..byte].chars().count();
    while i < raw.len() {
        let rest = &raw[i..];
        if rest.starts_with('⟨') {
            let Some(close) = rest.find('⟩') else {
                return Err(format!("unterminated floating tone '⟨' at position {}", position(i)));
            };
            let tone = parse_float_tone(&rest['⟨'.len_utf8()..close], project)?;
            let at = if segments.is_empty() { (0, Side::Before) } else { (segments.len() as u32 - 1, Side::After) };
            floats.push((tone, at));
            i += close + '⟩'.len_utf8();
            continue;
        }
        if rest.starts_with('-') {
            segments.push(morpheme_boundary_bundle());
            i += 1;
            continue;
        }
        if let Some(d) = project.diacritics.before().find(|d| rest.starts_with(d.symbol.as_str())) {
            if d.tier == Tier::Syllable {
                syllable_buffer = combine(&syllable_buffer, &d.bundle, d.contour);
            } else {
                buffer = combine(&buffer, &d.bundle, d.contour);
            }
            i += d.symbol.len();
            continue;
        }
        if let Some(letter) = project.letters.sorted().find(|l| rest.starts_with(l.symbol.as_str())) {
            let mut segment = combine(&letter.bundle, &buffer, false);
            if is_nucleus(&segment, project) {
                segment = combine(&segment, &syllable_buffer, false);
                last_nucleus = Some(segments.len());
                syllable_buffer = FeatureBundle::new();
            }
            segments.push(segment);
            buffer = FeatureBundle::new();
            i += letter.symbol.len();
            continue;
        }
        if let Some(d) = project.diacritics.attaching().find(|d| rest.starts_with(d.symbol.as_str())) {
            if d.tier == Tier::Syllable {
                let Some(n) = last_nucleus else {
                    return Err(format!(
                        "Suprasegmental diacritic '{}' at position {} has no preceding nucleus to attach to",
                        d.symbol,
                        position(i)
                    ));
                };
                segments[n] = combine(&segments[n], &d.bundle, d.contour);
            } else {
                let Some(last) = segments.last_mut() else {
                    return Err(format!(
                        "Diacritic '{}' at position {} has no preceding segment to attach to",
                        d.symbol,
                        position(i)
                    ));
                };
                *last = combine(last, &d.bundle, d.contour);
                let index = segments.len() - 1;
                if is_nucleus(&segments[index], project) {
                    if !syllable_buffer.is_empty() {
                        segments[index] = combine(&segments[index], &syllable_buffer, false);
                        syllable_buffer = FeatureBundle::new();
                    }
                    last_nucleus = Some(index);
                } else {
                    let (segmental, returned) = split_suprasegmentals(&segments[index], project);
                    segments[index] = segmental;
                    if !returned.is_empty() {
                        syllable_buffer = combine(&syllable_buffer, &returned, false);
                    }
                    if last_nucleus == Some(index) {
                        last_nucleus = (0..index).rev().find(|&j| is_nucleus(&segments[j], project));
                    }
                }
            }
            i += d.symbol.len();
            continue;
        }
        if rest.starts_with('.') {
            i += 1;
            continue;
        }
        let ch = rest.chars().next().unwrap();
        return Err(format!("Unknown character '{ch}' at position {}", position(i)));
    }
    let mut form = Form::from_bundles(segments);
    associate_tiers(&mut form, &project.tiers);
    for (tone, at) in floats {
        let Some((name, _)) = project.tiers.iter().find(|(_, d)| tone.keys().any(|f| d.carries.contains(&f))) else {
            continue;
        };
        let id = form.fresh_id();
        let tier = form.tier_mut(name);
        tier.autosegs.push(Autoseg { bundle: tone, id });
        tier.float_hosts.insert(id, at);
    }
    Ok(form)
}
