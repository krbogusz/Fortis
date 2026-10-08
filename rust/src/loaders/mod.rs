//! Loading a project: each inventory from the project directory, falling back to the shipped
//! defaults for any file the project omits.

pub mod files;
pub mod inventories;
pub mod lexicon;

use std::path::{Path, PathBuf};

use crate::models::*;

/// The shipped default project (`projects/default`), found next to the crate or via
/// `FORTIS_ROOT`.
pub fn default_project_dir() -> PathBuf {
    if let Ok(root) = std::env::var("FORTIS_ROOT") {
        return PathBuf::from(root).join("projects").join("default");
    }
    let manifest = Path::new(env!("CARGO_MANIFEST_DIR"));
    manifest.parent().unwrap_or(manifest).join("projects").join("default")
}

fn file_name(path: &Path) -> String {
    path.file_name().map(|n| n.to_string_lossy().into_owned()).unwrap_or_default()
}

pub fn load_project(
    project_dir: Option<&Path>,
    words_path: Option<&Path>,
    rules_path: Option<&Path>,
) -> Result<Project, Vec<String>> {
    let defaults = default_project_dir();
    let dir = project_dir.map(Path::to_path_buf).unwrap_or_else(|| defaults.clone());
    let pick = |name: &str| {
        let candidate = dir.join(name);
        if candidate.exists() { candidate } else { defaults.join(name) }
    };
    let pick_dual = |toml_name: &str, csv_name: &str| {
        for name in [toml_name, csv_name] {
            let candidate = dir.join(name);
            if candidate.exists() {
                return candidate;
            }
        }
        defaults.join(toml_name)
    };
    let words_path = words_path.map(Path::to_path_buf).unwrap_or_else(|| pick_dual("words.toml", "words.csv"));
    let rules_path = rules_path.map(Path::to_path_buf).unwrap_or_else(|| pick_dual("rules.toml", "rules.csv"));
    let diacritics_path = pick_dual("diacritics.toml", "diacritics.csv");
    let sonorities_path = pick_dual("sonorities.toml", "sonorities.csv");

    let mut features = match inventories::load_feature_inventory(&pick("features.toml")) {
        Ok(f) => f,
        Err(e) if e.len() > 1 => return Err(e.into_iter().map(|e| format!("features.toml: {e}")).collect()),
        Err(e) => return Err(e),
    };
    let mut errors: Vec<String> = Vec::new();
    let prefix = |name: String, e: Vec<String>| e.into_iter().map(move |e| format!("{name}: {e}"));

    let mut tiers = TierInventory::new();
    let tiers_path = pick("tiers.toml");
    if tiers_path.exists() {
        match inventories::load_tier_inventory(&tiers_path, &mut features) {
            Ok(t) => tiers = t,
            Err(e) => errors.extend(prefix("tiers.toml".into(), e)),
        }
    }
    let letters = inventories::load_letter_inventory(&pick("letters.csv"), &features)
        .map_err(|e| errors.extend(prefix("letters.csv".into(), e)))
        .ok();
    let diacritics = inventories::load_diacritic_inventory(&diacritics_path, &features)
        .map_err(|e| errors.extend(prefix(file_name(&diacritics_path), e)))
        .ok();
    let sonorities = inventories::load_sonorities_inventory(&sonorities_path, &features)
        .map_err(|e| errors.extend(prefix(file_name(&sonorities_path), e)))
        .ok();
    let syllable_parts = inventories::load_syllable_parts_inventory(&pick("syllable_parts.toml"), &features)
        .map_err(|e| errors.extend(prefix("syllable_parts.toml".into(), e)))
        .ok();
    let words = lexicon::load_word_inventory(&words_path)
        .map_err(|e| errors.extend(prefix(file_name(&words_path), e)))
        .ok();
    let rules = lexicon::load_rule_inventory(&rules_path, &features)
        .map_err(|e| errors.extend(prefix(file_name(&rules_path), e)))
        .ok();
    let settings = lexicon::load_settings(&pick("settings.toml"))
        .map_err(|e| errors.extend(prefix("settings.toml".into(), e)))
        .ok();
    if !errors.is_empty() {
        return Err(errors);
    }
    let (letters, diacritics, sonorities, syllable_parts, words, rules, settings) = (
        letters.unwrap(),
        diacritics.unwrap(),
        sonorities.unwrap(),
        syllable_parts.unwrap(),
        words.unwrap(),
        rules.unwrap(),
        settings.unwrap(),
    );
    let time = rules
        .by_time
        .keys()
        .flatten()
        .copied()
        .chain(syllable_parts.by_time.keys().copied())
        .min()
        .unwrap_or(0);
    let syllable_features = features.iter().filter(|(_, f)| f.tier == Tier::Syllable).map(|(id, _)| id).collect();
    Ok(Project {
        features,
        letters,
        diacritics,
        sonorities,
        syllable_parts,
        words,
        rules,
        time,
        tiers,
        settings,
        syllable_features,
    })
}

/// Word-scoped rules naming a word that is not in the lexicon, as `(rule id, name)` pairs.
pub fn unfired_scoped_rules(rules: &RuleInventory, words: &WordInventory) -> Vec<(String, String)> {
    let mut known = std::collections::HashSet::new();
    for word in words.values() {
        known.insert(word.id.as_str());
        if !word.gloss.is_empty() {
            known.insert(word.gloss.as_str());
        }
        known.insert(word.ipa());
    }
    rules
        .in_file_order()
        .flat_map(|rule| {
            rule.words
                .iter()
                .filter(|name| !known.contains(name.as_str()))
                .map(|name| (rule.id.clone(), name.clone()))
                .collect::<Vec<_>>()
        })
        .collect()
}
