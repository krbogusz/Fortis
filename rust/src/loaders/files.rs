//! Reading TOML and CSV files the way the Python loaders read them.

use std::path::Path;

use indexmap::IndexMap;
use toml::{Table, Value as Toml};

pub fn load_toml_file(path: &Path, allow_empty: bool) -> Result<Table, String> {
    if !path.is_file() {
        return Err(format!("There is no file at '{}'", path.display()));
    }
    if !path.extension().is_some_and(|e| e.eq_ignore_ascii_case("toml")) {
        return Err(format!("File at '{}' is not a TOML file", path.display()));
    }
    let text = std::fs::read_to_string(path)
        .map_err(|e| format!("Could not open '{}': {e}", path.display()))?;
    let data: Table = text
        .parse::<Table>()
        .map_err(|e| format!("Could not open '{}': {e}", path.display()))?;
    if data.is_empty() {
        if allow_empty {
            return Ok(data);
        }
        return Err(format!("File '{}' is empty", path.display()));
    }
    Ok(data)
}

/// One CSV row as `csv.DictReader` gives it: header → cell, in header order. A short row maps
/// the missing headers to `None`.
pub type CsvRow = IndexMap<String, Option<String>>;

/// Parse CSV text into its header and rows, skipping blank lines as `csv.DictReader` does.
pub fn parse_csv(text: &str) -> Result<(Option<Vec<String>>, Vec<CsvRow>), String> {
    let mut reader = csv::ReaderBuilder::new()
        .has_headers(false)
        .flexible(true)
        .from_reader(text.as_bytes());
    let mut header: Option<Vec<String>> = None;
    let mut rows = Vec::new();
    for record in reader.records() {
        let record = record.map_err(|e| e.to_string())?;
        let fields: Vec<String> = record.iter().map(str::to_string).collect();
        if fields.is_empty() || (fields.len() == 1 && fields[0].is_empty() && record.as_slice().is_empty())
        {
            continue;
        }
        match &header {
            None => header = Some(fields),
            Some(names) => {
                let mut row = CsvRow::new();
                for (i, name) in names.iter().enumerate() {
                    row.insert(name.clone(), fields.get(i).cloned());
                }
                rows.push(row);
            }
        }
    }
    Ok((header, rows))
}

/// `load_csv_file`: every row of a CSV file with a header, at least one data row.
pub fn load_csv_file(path: &Path) -> Result<(Vec<String>, Vec<CsvRow>), String> {
    if !path.is_file() {
        return Err(format!("There is no file at '{}'", path.display()));
    }
    if !path.extension().is_some_and(|e| e.eq_ignore_ascii_case("csv")) {
        return Err(format!("File at '{}' is not a CSV file", path.display()));
    }
    let text = std::fs::read_to_string(path)
        .map_err(|e| format!("Could not read '{}': {e}", path.display()))?;
    let (header, rows) =
        parse_csv(&text).map_err(|e| format!("Could not read '{}': {e}", path.display()))?;
    let Some(header) = header else {
        return Err(format!("File '{}' has no header row", path.display()));
    };
    if rows.is_empty() {
        return Err(format!("File '{}' has no data rows", path.display()));
    }
    Ok((header, rows))
}

/// Read a CSV inventory the way the dual-format loaders do: `text.splitlines()` fed to
/// `csv.DictReader`.
pub fn read_csv_lines(path: &Path) -> Result<(Option<Vec<String>>, Vec<CsvRow>), String> {
    let text = std::fs::read_to_string(path)
        .map_err(|e| format!("could not read '{}': {e}", path.display()))?;
    let joined = crate::py::splitlines(&text).join("\n");
    parse_csv(&joined).map_err(|e| format!("could not read '{}': {e}", path.display()))
}

pub fn cell(row: &CsvRow, key: &str) -> String {
    row.get(key).cloned().flatten().unwrap_or_default()
}

/// A short Python-ish `repr()` of a TOML value, for error messages.
pub fn repr(value: &Toml) -> String {
    match value {
        Toml::String(s) => crate::py::repr_str(s),
        Toml::Integer(n) => n.to_string(),
        Toml::Float(x) => crate::py::float_repr(*x),
        Toml::Boolean(b) => if *b { "True".into() } else { "False".into() },
        other => other.to_string(),
    }
}

/// `str(value)` of a TOML value, for the few loaders that stringify a field.
pub fn to_str(value: &Toml) -> String {
    match value {
        Toml::String(s) => s.clone(),
        Toml::Boolean(b) => if *b { "True".into() } else { "False".into() },
        Toml::Float(x) => crate::py::float_repr(*x),
        other => other.to_string(),
    }
}

/// Python truthiness of an optional TOML value (`not value`).
pub fn falsy(value: Option<&Toml>) -> bool {
    match value {
        None => true,
        Some(Toml::String(s)) => s.is_empty(),
        Some(Toml::Integer(n)) => *n == 0,
        Some(Toml::Float(x)) => *x == 0.0,
        Some(Toml::Boolean(b)) => !b,
        Some(Toml::Array(a)) => a.is_empty(),
        Some(Toml::Table(t)) => t.is_empty(),
        Some(_) => false,
    }
}
