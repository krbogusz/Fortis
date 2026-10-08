//! Loaders for the lexicon, the rules and the settings.

use std::path::Path;
use std::sync::Arc;

use toml::{Table, Value as Toml};

use super::files::{self, Source};
use crate::models::*;
use crate::parsing::notation::parse_definition;
use crate::parsing::validation::validate_structural_description;
use crate::py;

// ---- Words ------------------------------------------------------------------------------------

fn parse_time(raw: &str, where_: &str, errors: &mut Vec<String>) -> Result<Option<i64>, ()> {
    if raw == "final" {
        return Ok(None);
    }
    match py::parse_int(raw) {
        Some(n) => Ok(Some(n)),
        None => {
            errors.push(format!(
                "{where_}: time {} is neither an integer nor 'final'",
                py::repr_str(raw)
            ));
            Err(())
        }
    }
}

fn time_label(raw: Option<&Toml>) -> String {
    match raw {
        None => "None".into(),
        Some(v) => files::to_str(v),
    }
}

fn parse_word_table(index: usize, table: &Table, errors: &mut Vec<String>) -> Option<Word> {
    let id = match table.get("id") {
        Some(Toml::String(s)) if !py::strip(s).is_empty() => py::strip(s).to_string(),
        _ => {
            errors.push(format!("words[{index}] has no 'id'"));
            return None;
        }
    };
    let where_ = format!("Word '{id}'");
    let known = ["id", "gloss", "frequency", "forms", "note"];
    let mut unknown: Vec<&String> = table.keys().filter(|k| !known.contains(&k.as_str())).collect();
    if !unknown.is_empty() {
        let strings: Vec<&&String> =
            unknown.iter().filter(|k| matches!(table.get(k.as_str()), Some(Toml::String(_)))).collect();
        let hint = match strings.first() {
            Some(k) => format!(
                " — a concise entry ({}) must go ABOVE every [[words]] table, or TOML reads it as a key of the word above it",
                py::repr_str(k)
            ),
            None => String::new(),
        };
        unknown.sort();
        let names: Vec<&str> = unknown.iter().map(|s| s.as_str()).collect();
        errors.push(format!("{where_} has unknown key(s): {}{hint}", names.join(", ")));
        return None;
    }
    let gloss = match table.get("gloss") {
        None => String::new(),
        Some(Toml::String(s)) => s.clone(),
        Some(_) => {
            errors.push(format!("{where_} has a gloss that is not a string"));
            return None;
        }
    };
    let frequency = match table.get("frequency") {
        None => 1,
        Some(Toml::Integer(n)) if *n > 0 => *n,
        Some(_) => {
            errors.push(format!("{where_} has a 'frequency' that is not a positive integer"));
            return None;
        }
    };
    let raw_forms = match table.get("forms") {
        Some(Toml::Array(items)) if !items.is_empty() => items,
        _ => {
            errors.push(format!("{where_} has no 'forms' (a word needs at least its seed)"));
            return None;
        }
    };
    let mut forms: Vec<(Option<i64>, Attestation)> = Vec::new();
    for entry in raw_forms {
        let Toml::Table(entry) = entry else {
            errors.push(format!("{where_} has a form that is not a table"));
            return None;
        };
        let raw_time = entry.get("time");
        let time = match raw_time {
            Some(Toml::String(s)) => parse_time(s, &where_, errors).ok()?,
            Some(Toml::Integer(n)) => Some(*n),
            _ => {
                errors.push(format!("{where_} has a form with no integer (or 'final') 'time'"));
                return None;
            }
        };
        let at = time_label(raw_time);
        let ipa = match entry.get("ipa") {
            Some(Toml::String(s)) if !py::strip(s).is_empty() => py::strip(s).to_string(),
            _ => {
                errors.push(format!("{where_} has a form at {at} with no 'ipa'"));
                return None;
            }
        };
        let category = match entry.get("category") {
            None => String::new(),
            Some(Toml::String(s)) => py::strip(s).to_string(),
            Some(_) => {
                errors.push(format!("{where_} has a form at {at} whose category is not a string"));
                return None;
            }
        };
        let note = match entry.get("note") {
            None => String::new(),
            Some(Toml::String(s)) => py::strip(s).to_string(),
            Some(_) => {
                errors.push(format!("{where_} has a form at {at} whose note is not a string"));
                return None;
            }
        };
        let mut unknown_form: Vec<&String> = entry
            .keys()
            .filter(|k| !["time", "ipa", "category", "note"].contains(&k.as_str()))
            .collect();
        if !unknown_form.is_empty() {
            unknown_form.sort();
            let names: Vec<&str> = unknown_form.iter().map(|s| s.as_str()).collect();
            errors.push(format!("{where_} has a form at {at} with unknown key(s): {}", names.join(", ")));
            return None;
        }
        if forms.iter().any(|(t, _)| *t == time) {
            errors.push(format!("{where_} has two forms at {at}"));
            return None;
        }
        forms.push((time, Attestation { ipa, category, form: None, note }));
    }
    let note = match table.get("note") {
        None => String::new(),
        Some(Toml::String(s)) => py::strip(s).to_string(),
        Some(_) => {
            errors.push(format!("{where_} has a note that is not a string"));
            return None;
        }
    };
    Some(Word { id, forms, gloss: py::strip(&gloss).to_string(), frequency, note })
}

pub fn load_word_inventory(src: &dyn Source, path: &Path) -> Result<WordInventory, Vec<String>> {
    if path.extension().is_some_and(|e| e.eq_ignore_ascii_case("csv")) {
        return load_word_inventory_csv(src, path);
    }
    let data = files::load_toml_file(src, path, false).map_err(|e| vec![e])?;
    let mut errors = Vec::new();
    let mut inventory = WordInventory::new();
    let entries = match data.get("words") {
        None => Vec::new(),
        Some(Toml::Array(items)) => items.clone(),
        Some(_) => {
            return Err(vec![format!("'{}': 'words' must be an array of [[words]] tables", path.display())]);
        }
    };
    for (index, table) in entries.iter().enumerate() {
        let Toml::Table(table) = table else {
            errors.push(format!("words[{index}] is not a table"));
            continue;
        };
        let Some(word) = parse_word_table(index, table, &mut errors) else { continue };
        if inventory.contains_key(&word.id) {
            errors.push(format!("Word '{}' is already defined", word.id));
            continue;
        }
        inventory.insert(word.id.clone(), word);
    }
    for (key, value) in &data {
        if key == "words" {
            continue;
        }
        let Toml::String(gloss) = value else {
            errors.push(format!(
                "Word '{key}' must be a gloss string (the concise form); a word with targets goes in a [[words]] table"
            ));
            continue;
        };
        let id = py::strip(key).to_string();
        if inventory.contains_key(&id) {
            errors.push(format!("Word '{id}' is already defined"));
            continue;
        }
        let word = Word {
            id: id.clone(),
            forms: vec![(Some(0), Attestation { ipa: id.clone(), ..Default::default() })],
            gloss: py::strip(gloss).to_string(),
            frequency: 1,
            note: String::new(),
        };
        inventory.insert(id, word);
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}

fn load_word_inventory_csv(src: &dyn Source, path: &Path) -> Result<WordInventory, Vec<String>> {
    let (header, rows) = files::read_csv_lines(src, path).map_err(|e| vec![e])?;
    let Some(header) = header else {
        return Err(vec![format!("'{}' is empty (no header row)", path.display())]);
    };
    let missing: Vec<&str> =
        ["id", "time", "ipa"].into_iter().filter(|c| !header.iter().any(|h| h == c)).collect();
    if !missing.is_empty() {
        return Err(vec![format!("'{}' is missing required column(s): {}", path.display(), missing.join(", "))]);
    }
    let known = ["id", "time", "ipa", "category", "gloss", "frequency"];
    let unknown: Vec<&str> =
        header.iter().filter(|h| !known.contains(&h.as_str())).map(|s| s.as_str()).collect();
    if !unknown.is_empty() {
        return Err(vec![format!("'{}' has unknown column(s): {}", path.display(), unknown.join(", "))]);
    }
    let mut errors = Vec::new();
    let mut inventory = WordInventory::new();
    for (i, row) in rows.iter().enumerate() {
        let line = i + 2;
        let word_id = py::strip(&files::cell(row, "id")).to_string();
        if word_id.is_empty() {
            errors.push(format!("line {line}: row has an empty 'id'"));
            continue;
        }
        let Ok(time) = parse_time(py::strip(&files::cell(row, "time")), &format!("line {line}"), &mut errors) else {
            continue;
        };
        let ipa = py::strip(&files::cell(row, "ipa")).to_string();
        if ipa.is_empty() {
            errors.push(format!("line {line}: word '{word_id}' has an empty 'ipa'"));
            continue;
        }
        let word = inventory.entry(word_id.clone()).or_insert_with(|| Word {
            id: word_id.clone(),
            frequency: 1,
            ..Default::default()
        });
        if word.forms.iter().any(|(t, _)| *t == time) {
            let at = time.map_or("None".to_string(), |t| t.to_string());
            errors.push(format!("line {line}: word '{word_id}' already has a form at {at}"));
            continue;
        }
        word.forms.push((
            time,
            Attestation {
                ipa,
                category: py::strip(&files::cell(row, "category")).to_string(),
                ..Default::default()
            },
        ));
        let gloss = py::strip(&files::cell(row, "gloss")).to_string();
        if !gloss.is_empty() {
            if !word.gloss.is_empty() && word.gloss != gloss {
                errors.push(format!("line {line}: word '{word_id}' has two different glosses"));
            }
            word.gloss = gloss;
        }
        let raw = py::strip(&files::cell(row, "frequency")).to_string();
        if !raw.is_empty() {
            let frequency = py::parse_int(&raw).unwrap_or(0);
            if frequency <= 0 {
                errors.push(format!(
                    "line {line}: word '{word_id}' has a 'frequency' that is not a positive integer"
                ));
                continue;
            }
            if word.frequency != 1 && word.frequency != frequency {
                errors.push(format!("line {line}: word '{word_id}' has two different frequencies"));
            }
            word.frequency = frequency;
        }
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}

// ---- Rules ------------------------------------------------------------------------------------

fn string_list(rule_id: &str, def: &Table, field: &str) -> Result<Vec<String>, String> {
    match def.get(field) {
        None => Ok(Vec::new()),
        Some(Toml::String(s)) => Ok(vec![s.clone()]),
        Some(Toml::Array(items)) if items.iter().all(|i| matches!(i, Toml::String(_))) => {
            Ok(items.iter().map(|i| i.as_str().unwrap().to_string()).collect())
        }
        Some(_) => Err(format!("Rule '{rule_id}' has a '{field}' that is not a string or list of strings")),
    }
}

pub fn load_rule(rule_id: &str, def: &Table, features: &FeatureInventory) -> Result<Vec<Rule>, Vec<String>> {
    let mut errors = Vec::new();
    let time = match def.get("time") {
        None => None,
        Some(Toml::Integer(n)) => Some(*n),
        Some(Toml::Boolean(b)) => Some(*b as i64),
        Some(other) => {
            errors.push(format!("Rule '{rule_id}' has non-integer 'time' value: {}", files::repr(other)));
            Some(0)
        }
    };
    let definitions: Vec<String> = match def.get("definition") {
        None => {
            errors.push(format!("Rule '{rule_id}' is missing the required 'definition' field"));
            Vec::new()
        }
        Some(Toml::String(s)) => vec![s.clone()],
        Some(Toml::Array(items)) if items.iter().all(|i| matches!(i, Toml::String(_))) => {
            if items.is_empty() {
                errors.push(format!("Rule '{rule_id}' has an empty 'definition' list"));
            }
            items.iter().map(|i| i.as_str().unwrap().to_string()).collect()
        }
        Some(_) => {
            errors.push(format!(
                "Rule '{rule_id}' has a 'definition' that is not a string or list of strings"
            ));
            Vec::new()
        }
    };
    let application = match def.get("application") {
        None => ApplicationMode::Simultaneous,
        Some(Toml::String(s)) => {
            let lowered = py::strip(s).to_lowercase();
            match ApplicationMode::ALL.iter().find(|(n, _)| *n == lowered) {
                Some((_, mode)) => *mode,
                None => {
                    errors.push(format!(
                        "Rule '{rule_id}' has invalid application '{s}' (expected simultaneous, left_to_right, right_to_left)"
                    ));
                    ApplicationMode::Simultaneous
                }
            }
        }
        Some(other) => {
            errors.push(format!(
                "Rule '{rule_id}' has non-string 'application' value: {}",
                files::repr(other)
            ));
            ApplicationMode::Simultaneous
        }
    };
    let words = string_list(rule_id, def, "words").unwrap_or_else(|e| {
        errors.push(e);
        Vec::new()
    });
    let categories = string_list(rule_id, def, "categories").unwrap_or_else(|e| {
        errors.push(e);
        Vec::new()
    });
    let name = match def.get("name") {
        None => None,
        Some(Toml::String(s)) => Some(s.clone()),
        Some(_) => {
            errors.push(format!("Rule '{rule_id}' has non-string 'name' value"));
            None
        }
    };
    let description = match def.get("description") {
        None => None,
        Some(Toml::String(s)) => Some(s.clone()),
        Some(_) => {
            errors.push(format!("Rule '{rule_id}' has non-string 'description' value"));
            None
        }
    };
    let mut sds = Vec::new();
    for definition in &definitions {
        match parse_definition(definition, features) {
            Ok(sd) => {
                if let Err(e) = validate_structural_description(&sd, Some(features)) {
                    errors.extend(e);
                }
                sds.push(sd);
            }
            Err(e) => errors.extend(e),
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    let multiple = definitions.len() > 1;
    Ok(definitions
        .into_iter()
        .zip(sds)
        .enumerate()
        .map(|(i, (raw_definition, sd))| Rule {
            id: if multiple { format!("{rule_id}#{}", i + 1) } else { rule_id.to_string() },
            time,
            raw_definition,
            sd,
            application,
            name: name.clone(),
            description: description.clone(),
            words: words.clone(),
            categories: categories.clone(),
        })
        .collect())
}

fn assemble(ordered: Vec<(String, Table)>, features: &FeatureInventory) -> Result<RuleInventory, Vec<String>> {
    let mut errors = Vec::new();
    let mut inventory = RuleInventory::default();
    for (raw_id, def) in ordered {
        let rule_id = py::strip(&raw_id).to_string();
        match load_rule(&rule_id, &def, features) {
            Err(e) => errors.extend(e.into_iter().map(|e| format!("rule '{rule_id}': {e}"))),
            Ok(rules) => {
                for rule in rules {
                    inventory.by_time.entry(rule.time).or_default().push(Arc::new(rule));
                }
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    let mut seen = std::collections::HashSet::new();
    let mut duplicates = std::collections::BTreeSet::new();
    for rule in inventory.in_file_order() {
        if !seen.insert(rule.id.clone()) {
            duplicates.insert(rule.id.clone());
        }
    }
    if !duplicates.is_empty() {
        return Err(duplicates.into_iter().map(|id| format!("duplicate rule id '{id}'")).collect());
    }
    Ok(inventory)
}

pub fn load_rule_inventory(src: &dyn Source, path: &Path, features: &FeatureInventory) -> Result<RuleInventory, Vec<String>> {
    if path.extension().is_some_and(|e| e.eq_ignore_ascii_case("csv")) {
        return load_rule_inventory_csv(src, path, features);
    }
    let data = files::load_toml_file(src, path, false).map_err(|e| vec![e])?;
    let ordered = data
        .into_iter()
        .map(|(k, v)| (k, if let Toml::Table(t) = v { t } else { Table::new() }))
        .collect();
    assemble(ordered, features)
}

fn load_rule_inventory_csv(src: &dyn Source, path: &Path, features: &FeatureInventory) -> Result<RuleInventory, Vec<String>> {
    let (header, rows) = files::read_csv_lines(src, path).map_err(|e| vec![e])?;
    let Some(header) = header else {
        return Err(vec![format!("'{}' is empty (no header row)", path.display())]);
    };
    let known = ["id", "time", "name", "description", "definition", "application", "words", "categories"];
    let unknown: Vec<&str> =
        header.iter().filter(|h| !known.contains(&h.as_str())).map(|s| s.as_str()).collect();
    if !unknown.is_empty() {
        return Err(vec![format!("'{}' has unknown column(s): {}", path.display(), unknown.join(", "))]);
    }
    if !header.iter().any(|h| h == "id") {
        return Err(vec![format!("'{}' must have an 'id' column (the rule slug)", path.display())]);
    }
    if !header.iter().any(|h| h == "definition") {
        return Err(vec![format!("'{}' must have a 'definition' column", path.display())]);
    }
    let mut errors = Vec::new();
    let mut ordered = Vec::new();
    for (i, row) in rows.iter().enumerate() {
        let line = i + 2;
        let rule_id = py::strip(&files::cell(row, "id")).to_string();
        if rule_id.is_empty() {
            errors.push(format!("line {line}: empty rule id"));
            continue;
        }
        let mut def = Table::new();
        let time_cell = py::strip(&files::cell(row, "time")).to_string();
        if !time_cell.is_empty() {
            let value = match py::parse_int(&time_cell) {
                Some(n) => Toml::Integer(n),
                None => Toml::String(time_cell),
            };
            def.insert("time".into(), value);
        }
        let definition_cell = py::strip(&files::cell(row, "definition")).to_string();
        if !definition_cell.is_empty() {
            let parts: Vec<Toml> = definition_cell
                .split(';')
                .map(py::strip)
                .filter(|p| !p.is_empty())
                .map(|p| Toml::String(p.to_string()))
                .collect();
            def.insert("definition".into(), Toml::Array(parts));
        }
        for field in ["name", "description", "application"] {
            let value = py::strip(&files::cell(row, field)).to_string();
            if !value.is_empty() {
                def.insert(field.into(), Toml::String(value));
            }
        }
        for scope in ["words", "categories"] {
            let cell = py::strip(&files::cell(row, scope)).to_string();
            if !cell.is_empty() {
                let items: Vec<Toml> = cell
                    .split(';')
                    .map(py::strip)
                    .filter(|p| !p.is_empty())
                    .map(|p| Toml::String(p.to_string()))
                    .collect();
                def.insert(scope.into(), Toml::Array(items));
            }
        }
        ordered.push((rule_id, def));
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    assemble(ordered, features)
}

// ---- Settings ---------------------------------------------------------------------------------

pub fn load_settings(src: &dyn Source, path: &Path) -> Result<Settings, Vec<String>> {
    let mut settings = Settings::default();
    if !src.is_file(path) {
        return Ok(settings);
    }
    let data = files::load_toml_file(src, path, true).map_err(|e| vec![e])?;
    let schema: [(&str, &[(&str, f64)]); 3] = [
        ("accuracy", &[("transposition_cost", 0.0)]),
        (
            "diagnosis",
            &[
                ("min_support", 1.0),
                ("min_support_percent", 0.0),
                ("min_errors", 1.0),
                ("report_top", 0.0),
                ("focus_count", 0.0),
            ],
        ),
        (
            "induction",
            &[
                ("min_improved_words", 1.0),
                ("top_confusions", 1.0),
                ("contexts_per_confusion", 1.0),
                ("placement_candidates", 1.0),
                ("max_rules_per_interval", 1.0),
                ("alignment_distance_cap", 0.0),
                ("final_weight", 0.0),
            ],
        ),
    ];
    let mut errors = Vec::new();
    for (section, table) in &data {
        let Some((_, keys)) = schema.iter().find(|(name, _)| name == section) else {
            errors.push(format!("unknown section '[{section}]'"));
            continue;
        };
        let Toml::Table(table) = table else {
            errors.push(format!("[{section}] must be a table"));
            continue;
        };
        for (key, value) in table {
            let Some((_, minimum)) = keys.iter().find(|(k, _)| k == key) else {
                errors.push(format!("[{section}] has unknown key '{key}'"));
                continue;
            };
            let number = if key == "final_weight" {
                match value {
                    Toml::Integer(n) => *n as f64,
                    Toml::Float(x) => *x,
                    other => {
                        errors.push(format!("[{section}] '{key}' must be a number (got {})", files::repr(other)));
                        continue;
                    }
                }
            } else {
                match value {
                    Toml::Integer(n) => *n as f64,
                    other => {
                        errors.push(format!("[{section}] '{key}' must be an integer (got {})", files::repr(other)));
                        continue;
                    }
                }
            };
            if number < *minimum {
                let shown = match value {
                    Toml::Integer(n) => n.to_string(),
                    _ => py::float_repr(number),
                };
                let min_shown = if key == "final_weight" { "0".to_string() } else { (*minimum as i64).to_string() };
                errors.push(format!("[{section}] '{key}' must be ≥ {min_shown} (got {shown})"));
                continue;
            }
            let n = number as i64;
            match (section.as_str(), key.as_str()) {
                ("accuracy", "transposition_cost") => settings.accuracy.transposition_cost = n,
                ("diagnosis", "min_support") => settings.diagnosis.min_support = n,
                ("diagnosis", "min_support_percent") => settings.diagnosis.min_support_percent = n,
                ("diagnosis", "min_errors") => settings.diagnosis.min_errors = n,
                ("diagnosis", "report_top") => settings.diagnosis.report_top = n,
                ("diagnosis", "focus_count") => settings.diagnosis.focus_count = n,
                ("induction", "min_improved_words") => settings.induction.min_improved_words = n,
                ("induction", "top_confusions") => settings.induction.top_confusions = n,
                ("induction", "contexts_per_confusion") => settings.induction.contexts_per_confusion = n,
                ("induction", "placement_candidates") => settings.induction.placement_candidates = n,
                ("induction", "max_rules_per_interval") => settings.induction.max_rules_per_interval = n,
                ("induction", "alignment_distance_cap") => settings.induction.alignment_distance_cap = n,
                ("induction", "final_weight") => settings.induction.final_weight = number,
                _ => {}
            }
        }
    }
    if errors.is_empty() { Ok(settings) } else { Err(errors) }
}
