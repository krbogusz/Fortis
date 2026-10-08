//! Loaders for the feature system, letters, diacritics, sonorities, syllable parts and tiers.

use std::path::Path;
use std::sync::Arc;

use indexmap::IndexMap;
use toml::{Table, Value as Toml};

use super::files::{self, CsvRow};
use crate::models::*;
use crate::parsing::bundles::{parse_feature_bundle, parse_feature_spec, parse_pattern_bundle};
use crate::parsing::notation::parse_sequence;
use crate::py;

// ---- Features ---------------------------------------------------------------------------------

fn as_table(value: &Toml) -> Table {
    match value {
        Toml::Table(t) => t.clone(),
        _ => Table::new(),
    }
}

/// Load one feature from its TOML table.
pub fn load_feature(name: &str, def: &Table) -> Result<Feature, Vec<String>> {
    let mut errors = Vec::new();
    let tier = match def.get("tier") {
        v if files::falsy(v) => Tier::Segment,
        Some(Toml::String(s)) => match py::strip(s).to_lowercase().as_str() {
            "segment" => Tier::Segment,
            "syllable" => Tier::Syllable,
            _ => {
                errors.push(format!(
                    "Feature '{name}' has an invalid tier '{s}' (expected segment, syllable)"
                ));
                Tier::Segment
            }
        },
        Some(other) => {
            errors.push(format!(
                "Feature '{name}' has an invalid tier '{}' (expected segment, syllable)",
                files::to_str(other)
            ));
            Tier::Segment
        }
        None => unreachable!(),
    };
    let kind = match def.get("kind") {
        v if files::falsy(v) => {
            errors.push(format!("Feature '{name}' is missing the required field 'kind'"));
            FeatureKind::Unary
        }
        Some(v) => {
            let raw = files::to_str(v);
            match py::strip(&raw).to_lowercase().as_str() {
                "unary" => FeatureKind::Unary,
                "binary" => FeatureKind::Binary,
                "scalar" => FeatureKind::Scalar,
                _ => {
                    errors.push(format!(
                        "Feature '{name}' has an invalid kind '{raw}' (expected unary, binary, scalar)"
                    ));
                    FeatureKind::Unary
                }
            }
        }
        None => unreachable!(),
    };
    let short_name = match def.get("short") {
        None => name.to_string(),
        Some(Toml::String(s)) => {
            let stripped = py::strip(s);
            if stripped.is_empty() {
                name.to_string()
            } else if stripped.contains([' ', '\t']) {
                errors.push(format!(
                    "Feature '{name}' has a short name '{stripped}' that contains whitespace"
                ));
                name.to_string()
            } else {
                stripped.to_string()
            }
        }
        Some(_) => {
            errors.push(format!("Feature '{name}' field 'short' is not a string"));
            name.to_string()
        }
    };
    let values = match load_values(name, def, kind) {
        Ok(v) => v,
        Err(e) => {
            errors.push(e);
            Vec::new()
        }
    };
    let children = match load_children(name, def) {
        Ok(c) => c,
        Err(e) => {
            errors.push(e);
            None
        }
    };
    if !errors.is_empty() {
        return Err(errors);
    }
    Ok(Feature { name: name.to_string(), tier, kind, short_name, values, children, parent: None })
}

fn load_values(name: &str, def: &Table, kind: FeatureKind) -> Result<Vec<(i64, String)>, String> {
    match kind {
        FeatureKind::Unary => Ok(vec![(1, "present".into())]),
        FeatureKind::Binary => Ok(vec![(0, "absent".into()), (1, "present".into())]),
        FeatureKind::Scalar => {
            let raw = def.get("values");
            if files::falsy(raw) {
                return Err(format!("Feature '{name}' is scalar, but does not have specified 'values'"));
            }
            let Some(Toml::Table(table)) = raw else {
                return Err(format!("Feature '{name}' has 'values' field that is not a dictionary"));
            };
            let mut out: Vec<(i64, String)> = Vec::new();
            for (key, label) in table {
                let Some(code) = py::parse_int(key) else {
                    return Err(format!("Feature '{name}' value '{key}' is not an integer"));
                };
                let Toml::String(label) = label else {
                    return Err(format!(
                        "Feature '{name}' value '{code}' has a label that is not a string"
                    ));
                };
                if py::strip(label).is_empty() {
                    return Err(format!("Feature '{name}' value '{code}' has an empty label"));
                }
                let label = py::strip(label).to_lowercase();
                if let Some(slot) = out.iter_mut().find(|(k, _)| *k == code) {
                    slot.1 = label;
                } else {
                    out.push((code, label));
                }
            }
            Ok(out)
        }
    }
}

fn load_children(name: &str, def: &Table) -> Result<Option<Vec<String>>, String> {
    match def.get("children") {
        None => Ok(None),
        Some(Toml::String(s)) => {
            if py::strip(s).is_empty() {
                Ok(None)
            } else {
                Ok(Some(vec![py::strip(s).to_string()]))
            }
        }
        Some(Toml::Array(items)) => {
            if items.is_empty() {
                return Ok(None);
            }
            let mut out = Vec::new();
            for item in items {
                let Toml::String(child) = item else {
                    return Err(format!(
                        "Feature '{name}' has a non-string child '{}'",
                        files::to_str(item)
                    ));
                };
                if py::strip(child).is_empty() {
                    return Err(format!("Feature '{name}' has an empty child name"));
                }
                out.push(py::strip(child).to_string());
            }
            Ok(Some(out))
        }
        Some(_) => Err(format!("Feature '{name}' field 'children' is neither a string nor a list")),
    }
}

pub fn load_feature_inventory(path: &Path) -> Result<FeatureInventory, Vec<String>> {
    let data = files::load_toml_file(path, false).map_err(|e| vec![e])?;
    let mut errors = Vec::new();
    let mut inventory = FeatureInventory::default();
    for (raw_name, def) in &data {
        let name = py::strip(raw_name);
        if name.contains([' ', '\t']) {
            errors.push(format!("Feature name '{name}' contains whitespace"));
            continue;
        }
        if inventory.contains(name) {
            errors.push(format!("Feature name '{name}' is already in use"));
            continue;
        }
        match load_feature(name, &as_table(def)) {
            Err(e) => errors.extend(e),
            Ok(feature) => inventory.insert(feature),
        }
    }
    let assignments: Vec<(String, Vec<String>)> = inventory
        .iter()
        .filter_map(|(_, f)| f.children.clone().map(|c| (f.name.clone(), c)))
        .collect();
    for (parent, children) in assignments {
        for child in children {
            match inventory.id(&child) {
                None => errors.push(format!("Feature '{parent}' references unknown child '{child}'")),
                Some(id) => inventory.get_mut(id).parent = Some(parent.clone()),
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    synthesize_root(&mut inventory);
    inventory.rebuild();
    validate_feature_inventory(&inventory)?;
    Ok(inventory)
}

fn synthesize_root(inventory: &mut FeatureInventory) {
    let tops: Vec<String> = inventory
        .iter()
        .filter(|(_, f)| f.tier == Tier::Segment && f.parent.is_none() && f.name != "root")
        .map(|(_, f)| f.name.clone())
        .collect();
    if tops.is_empty() {
        return;
    }
    match inventory.id("root") {
        Some(id) => {
            let root = inventory.get_mut(id);
            let mut children = root.children.clone().unwrap_or_default();
            children.extend(tops.iter().cloned());
            root.children = Some(children);
        }
        None => inventory.insert(Feature {
            name: "root".into(),
            tier: Tier::Segment,
            kind: FeatureKind::Unary,
            short_name: "root".into(),
            values: Vec::new(),
            children: Some(tops.clone()),
            parent: None,
        }),
    }
    for name in tops {
        let id = inventory.id(&name).unwrap();
        inventory.get_mut(id).parent = Some("root".into());
    }
}

fn validate_feature_inventory(inventory: &FeatureInventory) -> Result<(), Vec<String>> {
    let mut errors = Vec::new();
    let mut seen: IndexMap<String, String> = IndexMap::new();
    for (_, f) in inventory.iter() {
        if let Some(other) = seen.get(&f.short_name)
            && *other != f.name {
                errors.push(format!(
                    "Feature '{}' has short name '{}' already used by '{other}'",
                    f.name, f.short_name
                ));
            }
        if f.short_name != f.name {
            seen.insert(f.short_name.clone(), f.name.clone());
        }
    }
    for (_, f) in inventory.iter() {
        for child in f.children.iter().flatten() {
            let Some(id) = inventory.id(child) else { continue };
            let c = inventory.get(id);
            if c.tier != f.tier {
                errors.push(format!(
                    "Feature '{child}' (tier: {}) cannot be a child of '{}' (tier: {})",
                    c.tier.name(),
                    f.name,
                    f.tier.name()
                ));
            }
        }
    }
    for (_, f) in inventory.iter() {
        let mut visited: Vec<&str> = Vec::new();
        let mut current: Option<&str> = Some(&f.name);
        while let Some(name) = current {
            if visited.contains(&name) {
                errors.push(format!("Feature '{}' has a circular parent chain", f.name));
                break;
            }
            visited.push(name);
            current = inventory.id(name).and_then(|id| inventory.get(id).parent.as_deref());
        }
    }
    if errors.is_empty() { Ok(()) } else { Err(errors) }
}

// ---- Letters ----------------------------------------------------------------------------------

fn load_letter(row: &CsvRow, features: &FeatureInventory) -> Result<Letter, Vec<String>> {
    let raw_symbol = files::cell(row, "symbol");
    let symbol = py::strip(&raw_symbol).to_string();
    if symbol.is_empty() {
        return Err(vec!["A letter is missing the required 'symbol' field".into()]);
    }
    if raw_symbol != symbol {
        return Err(vec![format!("Letter '{symbol}' has leading/trailing whitespace in its symbol cell")]);
    }
    let mut errors = Vec::new();
    let mut bundle = FeatureBundle::new();
    for (column, raw_value) in row {
        if column == "symbol" {
            continue;
        }
        let Some(id) = features.id(column) else {
            errors.push(format!("Letter '{symbol}' has a feature '{column}' that is unknown"));
            continue;
        };
        let raw_value = raw_value.clone().unwrap_or_default();
        let raw_value = py::strip(&raw_value);
        if raw_value.is_empty() {
            continue;
        }
        match parse_feature_spec(&format!("{column}{raw_value}"), features, None) {
            Err(e) => errors.push(e),
            Ok((_, value)) => {
                if value.is_none() {
                    continue;
                }
                bundle.set(id, value);
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    Ok(Letter { symbol, bundle: Arc::new(bundle) })
}

pub fn load_letter_inventory(path: &Path, features: &FeatureInventory) -> Result<LetterInventory, Vec<String>> {
    let (header, rows) = files::load_csv_file(path).map_err(|e| vec![e])?;
    let mut errors = Vec::new();
    for column in &header {
        if column != "symbol" && !features.contains(column) {
            errors.push(format!("CSV column '{column}' is not a known feature"));
        }
    }
    let mut inventory = LetterInventory::default();
    for row in &rows {
        match load_letter(row, features) {
            Err(e) => errors.extend(e),
            Ok(letter) => {
                if inventory.contains(&letter.symbol) {
                    errors.push(format!("Duplicate symbol '{}'", letter.symbol));
                    continue;
                }
                inventory.insert(letter);
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    let mut errors = Vec::new();
    for letter in &inventory.letters {
        if letter.bundle.is_empty() {
            errors.push(format!("Symbol '{}' has no feature specifications", letter.symbol));
        }
        for f in letter.bundle.keys() {
            if let Some(parent) = &features.get(f).parent {
                let parent_in = features.id(parent).is_some_and(|p| letter.bundle.contains(p));
                if parent != "root" && !parent_in {
                    errors.push(format!(
                        "Letter '{}' sets '{}' but not its parent '{parent}'",
                        letter.symbol,
                        features.name(f)
                    ));
                }
            }
        }
    }
    let mut groups: IndexMap<BundleKey, Vec<String>> = IndexMap::new();
    for letter in &inventory.letters {
        groups.entry(letter.bundle.key()).or_default().push(letter.symbol.clone());
    }
    for symbols in groups.values() {
        if symbols.len() > 1 {
            let names: Vec<String> = symbols.iter().map(|s| py::repr_str(s)).collect();
            errors.push(format!("Letters {} have identical feature bundles", names.join(" and ")));
        }
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}

// ---- Diacritics -------------------------------------------------------------------------------

pub fn present_symbol(symbol: &str) -> String {
    let mut chars = symbol.chars();
    match (chars.next(), chars.next()) {
        (Some(c), None) if py::is_combining(c) => format!("◌{c}"),
        _ => symbol.to_string(),
    }
}

fn load_diacritic(symbol: &str, def: &Table, features: &FeatureInventory) -> Result<Diacritic, Vec<String>> {
    let shown = present_symbol(symbol);
    let mut errors = Vec::new();
    let tier = match def.get("tier") {
        v if files::falsy(v) => {
            errors.push(format!("Diacritic '{shown}' is missing the required 'tier' field"));
            Tier::Segment
        }
        Some(v) => {
            let raw = files::to_str(v);
            match py::strip(&raw).to_lowercase().as_str() {
                "segment" => Tier::Segment,
                "syllable" => Tier::Syllable,
                _ => {
                    errors.push(format!(
                        "Diacritic '{shown}' has invalid tier '{raw}' (expected segment, syllable)"
                    ));
                    Tier::Segment
                }
            }
        }
        None => unreachable!(),
    };
    let kind = match def.get("kind") {
        v if files::falsy(v) => {
            errors.push(format!("Diacritic '{shown}' is missing the required 'kind' field"));
            DiacriticKind::Combining
        }
        Some(v) => {
            let raw = files::to_str(v);
            let lowered = py::strip(&raw).to_lowercase();
            match DiacriticKind::ALL.iter().find(|(n, _)| *n == lowered) {
                Some((_, k)) => *k,
                None => {
                    errors.push(format!(
                        "Diacritic '{shown}' has invalid kind '{raw}' (expected before, combining, after)"
                    ));
                    DiacriticKind::Combining
                }
            }
        }
        None => unreachable!(),
    };
    let bundle = match def.get("bundle") {
        v if files::falsy(v) => {
            errors.push(format!("Diacritic '{shown}' is missing the required 'bundle' field"));
            FeatureBundle::new()
        }
        Some(v) => match parse_feature_bundle(&files::to_str(v), features) {
            Err(e) => {
                errors.extend(e);
                FeatureBundle::new()
            }
            Ok(b) => b,
        },
        None => unreachable!(),
    };
    let mut flag = |field: &str| match def.get(field) {
        None => false,
        Some(Toml::Boolean(b)) => *b,
        Some(_) => {
            errors.push(format!("Diacritic '{shown}' '{field}' must be 'true' or 'false'"));
            false
        }
    };
    let contour = flag("contour");
    let read_only = flag("read_only");
    let marks_boundary = flag("marks_boundary");
    if !errors.is_empty() {
        return Err(errors);
    }
    Ok(Diacritic { symbol: symbol.to_string(), tier, kind, bundle, contour, read_only, marks_boundary })
}

fn validate_diacritics(inventory: &DiacriticInventory, features: &FeatureInventory) -> Result<(), Vec<String>> {
    let mut errors = Vec::new();
    for d in &inventory.diacritics {
        for f in d.bundle.keys() {
            let Some(feature) = features.try_get(f) else { continue };
            if feature.tier != d.tier {
                errors.push(format!(
                    "Diacritic '{}' (tier: {}) uses feature '{}' which belongs to tier: {}",
                    present_symbol(&d.symbol),
                    d.tier.name(),
                    feature.name,
                    feature.tier.name()
                ));
            }
        }
    }
    if errors.is_empty() { Ok(()) } else { Err(errors) }
}

pub fn load_diacritic_inventory(path: &Path, features: &FeatureInventory) -> Result<DiacriticInventory, Vec<String>> {
    let is_csv = path.extension().is_some_and(|e| e.eq_ignore_ascii_case("csv"));
    let mut errors = Vec::new();
    let mut inventory = DiacriticInventory::default();
    if is_csv {
        let (header, rows) = files::read_csv_lines(path).map_err(|e| vec![e])?;
        let Some(header) = header else {
            return Err(vec![format!("'{}' is empty (no header row)", path.display())]);
        };
        let known = ["diacritic", "tier", "kind", "bundle", "marks_boundary", "read_only", "contour"];
        let unknown: Vec<&String> = header.iter().filter(|h| !known.contains(&h.as_str())).collect();
        if !unknown.is_empty() {
            let names: Vec<&str> = unknown.iter().map(|s| s.as_str()).collect();
            return Err(vec![format!("'{}' has unknown column(s): {}", path.display(), names.join(", "))]);
        }
        for required in ["diacritic", "tier", "kind", "bundle"] {
            if !header.iter().any(|h| h == required) {
                return Err(vec![format!("'{}' must have a '{required}' column", path.display())]);
            }
        }
        for row in &rows {
            let symbol = py::strip(&files::cell(row, "diacritic")).replace('◌', "");
            if symbol.is_empty() {
                errors.push("Diacritic has an empty symbol".into());
                continue;
            }
            if inventory.contains(&symbol) {
                errors.push(format!("Diacritic '{}' is already defined", present_symbol(&symbol)));
                continue;
            }
            let mut def = Table::new();
            for field in ["tier", "kind", "bundle"] {
                def.insert(field.into(), Toml::String(py::strip(&files::cell(row, field)).to_string()));
            }
            for flag in ["marks_boundary", "read_only", "contour"] {
                if header.iter().any(|h| h == flag) {
                    let raw = files::cell(row, flag);
                    let lowered = py::strip(&raw).to_lowercase();
                    let value = match lowered.as_str() {
                        "" | "false" => Toml::Boolean(false),
                        "true" => Toml::Boolean(true),
                        _ => Toml::String(raw),
                    };
                    def.insert(flag.into(), value);
                }
            }
            match load_diacritic(&symbol, &def, features) {
                Err(e) => errors.extend(e),
                Ok(d) => inventory.insert(d),
            }
        }
    } else {
        let data = files::load_toml_file(path, false).map_err(|e| vec![e])?;
        for (raw_symbol, def) in &data {
            let symbol = py::strip(raw_symbol).replace('◌', "");
            if symbol.is_empty() {
                errors.push("Diacritic has an empty symbol".into());
                continue;
            }
            if inventory.contains(&symbol) {
                errors.push(format!("Diacritic '{}' is already defined", present_symbol(&symbol)));
                continue;
            }
            match load_diacritic(&symbol, &as_table(def), features) {
                Err(e) => errors.extend(e),
                Ok(d) => inventory.insert(d),
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    validate_diacritics(&inventory, features)?;
    Ok(inventory)
}

// ---- Sonorities -------------------------------------------------------------------------------

fn load_sonority(label: &str, level: Option<&Toml>, bundle: Option<&Toml>, features: &FeatureInventory) -> Result<Sonority, Vec<String>> {
    let mut errors = Vec::new();
    let level = match level {
        None => {
            errors.push(format!("Sonority '{label}' is missing the required 'level' field"));
            0
        }
        Some(v) => {
            let raw = files::to_str(v);
            match py::parse_int(py::strip(&raw)) {
                Some(n) if n > 0 => n,
                _ => {
                    errors.push(format!(
                        "Sonority '{label}' has invalid level '{raw}' (expected a positive integer)"
                    ));
                    0
                }
            }
        }
    };
    let bundle = match bundle {
        None => {
            errors.push(format!("Sonority '{label}' is missing the required 'bundle' field"));
            None
        }
        Some(v) => {
            let raw = files::to_str(v);
            let raw = py::strip(&raw);
            if raw.is_empty() {
                None
            } else {
                match parse_pattern_bundle(raw, features) {
                    Err(e) => {
                        errors.extend(e);
                        None
                    }
                    Ok(b) => Some(b),
                }
            }
        }
    };
    if !errors.is_empty() {
        return Err(errors);
    }
    Ok(Sonority { label: label.to_string(), level, bundle })
}

pub fn load_sonorities_inventory(path: &Path, features: &FeatureInventory) -> Result<Vec<Sonority>, Vec<String>> {
    let is_csv = path.extension().is_some_and(|e| e.eq_ignore_ascii_case("csv"));
    let mut errors = Vec::new();
    let mut inventory: Vec<Sonority> = Vec::new();
    if is_csv {
        let (header, rows) = files::read_csv_lines(path).map_err(|e| vec![e])?;
        let Some(header) = header else {
            return Err(vec![format!("'{}' is empty (no header row)", path.display())]);
        };
        let known = ["name", "level", "bundle"];
        let unknown: Vec<&str> =
            header.iter().filter(|h| !known.contains(&h.as_str())).map(|s| s.as_str()).collect();
        if !unknown.is_empty() {
            return Err(vec![format!("'{}' has unknown column(s): {}", path.display(), unknown.join(", "))]);
        }
        for required in known {
            if !header.iter().any(|h| h == required) {
                return Err(vec![format!("'{}' must have a '{required}' column", path.display())]);
            }
        }
        for row in &rows {
            let label = py::strip(&files::cell(row, "name")).to_string();
            if label.is_empty() {
                errors.push("Sonority has an empty name".into());
                continue;
            }
            if inventory.iter().any(|s| s.label == label) {
                errors.push(format!("Sonority '{label}' is already defined"));
                continue;
            }
            let level = Toml::String(py::strip(&files::cell(row, "level")).to_string());
            let bundle = Toml::String(files::cell(row, "bundle"));
            match load_sonority(&label, Some(&level), Some(&bundle), features) {
                Err(e) => errors.extend(e),
                Ok(s) => inventory.push(s),
            }
        }
    } else {
        let data = files::load_toml_file(path, false).map_err(|e| vec![e])?;
        for (raw_label, def) in &data {
            let label = py::strip(raw_label).to_string();
            if inventory.iter().any(|s| s.label == label) {
                errors.push(format!("Sonority '{label}' is already defined"));
                continue;
            }
            let def = as_table(def);
            match load_sonority(&label, def.get("level"), def.get("bundle"), features) {
                Err(e) => errors.extend(e),
                Ok(s) => inventory.push(s),
            }
        }
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    let mut seen: Vec<(i64, &str)> = Vec::new();
    for s in &inventory {
        if let Some((_, other)) = seen.iter().find(|(l, _)| *l == s.level) {
            errors.push(format!("Sonority '{}' and '{other}' share level {}", s.label, s.level));
        } else {
            seen.push((s.level, &s.label));
        }
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}

// ---- Syllable parts ---------------------------------------------------------------------------

pub fn load_syllable_parts_inventory(path: &Path, features: &FeatureInventory) -> Result<SyllablePartsInventory, Vec<String>> {
    let data = files::load_toml_file(path, false).map_err(|e| vec![e])?;
    let mut errors = Vec::new();
    let mut inventory = SyllablePartsInventory::default();
    for (raw_time, parts) in &data {
        let Some(time) = py::parse_int(py::strip(raw_time)) else {
            errors.push(format!("Syllable part time '{raw_time}' is not a valid integer"));
            continue;
        };
        for (raw_part, part_def) in &as_table(parts) {
            let part_type = py::strip(raw_part).to_string();
            if inventory.by_time.get(&time).is_some_and(|m| m.contains_key(&part_type)) {
                errors.push(format!("Syllable part '{part_type}' at time {time} is already defined"));
                continue;
            }
            if !["onset", "nucleus", "coda"].contains(&part_type.as_str()) {
                errors.push(format!(
                    "Invalid syllable part type '{part_type}' (expected coda, nucleus, onset)"
                ));
                continue;
            }
            let raw = as_table(part_def).get("definition").map(files::to_str).unwrap_or_default();
            let raw = py::strip(&raw).to_string();
            let mut part = SyllablePart { part_type: part_type.clone(), time, definition: None, pattern: None };
            if !raw.is_empty() {
                if part_type == "nucleus" {
                    match parse_pattern_bundle(&raw, features) {
                        Err(e) => {
                            errors.extend(e);
                            continue;
                        }
                        Ok(b) => part.definition = Some(b),
                    }
                } else {
                    match parse_sequence(&raw, features) {
                        Err(e) => {
                            errors.extend(e);
                            continue;
                        }
                        Ok(p) => part.pattern = Some(p),
                    }
                }
            }
            inventory.by_time.entry(time).or_default().insert(part_type, Arc::new(part));
        }
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}

// ---- Tiers ------------------------------------------------------------------------------------

pub fn load_tier_inventory(path: &Path, features: &mut FeatureInventory) -> Result<TierInventory, Vec<String>> {
    let data = files::load_toml_file(path, true).map_err(|e| vec![e])?;
    let mut errors = Vec::new();
    let mut inventory = TierInventory::new();
    for (raw_name, def) in &data {
        let name = py::strip(raw_name).to_string();
        if inventory.contains_key(&name) {
            errors.push(format!("Tier '{name}' is already defined"));
            continue;
        }
        let def = as_table(def);
        let mut tier_errors = Vec::new();
        let mut feature_def = def.clone();
        feature_def.insert("tier".into(), Toml::String("syllable".into()));
        match load_feature(&name, &feature_def) {
            Err(e) => tier_errors.extend(e),
            Ok(feature) => features.insert(feature),
        }
        let mut anchor = None;
        let anchor_raw = def.get("anchor").map(files::to_str).unwrap_or_default();
        if files::falsy(def.get("anchor")) || py::strip(&anchor_raw).is_empty() {
            tier_errors.push(format!("Tier '{name}' is missing the required 'anchor' field"));
        } else {
            match parse_pattern_bundle(py::strip(&anchor_raw), features) {
                Err(e) => tier_errors.extend(e.into_iter().map(|e| format!("Tier '{name}' anchor: {e}"))),
                Ok(b) => anchor = Some(b),
            }
        }
        let melody = match def.get("melody") {
            Some(Toml::Boolean(b)) => *b,
            _ => {
                tier_errors.push(format!("Tier '{name}' needs a boolean 'melody' field"));
                false
            }
        };
        let mut boolean = |field: &str| match def.get(field) {
            None => true,
            Some(Toml::Boolean(b)) => *b,
            Some(_) => {
                tier_errors.push(format!("Tier '{name}' field '{field}' must be a boolean"));
                true
            }
        };
        let ocp = boolean("ocp");
        let stray_erase = boolean("stray_erase");
        let stability = match def.get("stability") {
            None => "left".to_string(),
            Some(Toml::String(s)) if s == "left" || s == "right" => s.clone(),
            Some(_) => {
                tier_errors.push(format!("Tier '{name}' field 'stability' must be 'left' or 'right'"));
                "left".to_string()
            }
        };
        if !tier_errors.is_empty() {
            errors.extend(tier_errors);
            continue;
        }
        let carries = vec![features.id(&name).unwrap()];
        inventory.insert(
            name.clone(),
            TierDeclaration { name, carries, anchor: anchor.unwrap(), melody, ocp, stray_erase, stability },
        );
    }
    if !errors.is_empty() {
        return Err(errors);
    }
    let mut owner: IndexMap<FeatId, String> = IndexMap::new();
    for (name, decl) in &inventory {
        for f in &decl.carries {
            if let Some(other) = owner.get(f) {
                errors.push(format!(
                    "Feature '{}' is carried by both tier '{other}' and '{name}'",
                    features.name(*f)
                ));
            } else {
                owner.insert(*f, name.clone());
            }
        }
    }
    if errors.is_empty() { Ok(inventory) } else { Err(errors) }
}
