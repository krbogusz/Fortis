//! Reading TOML and CSV files from disk: a port of `tests/test_file_handling.py`. The expected
//! error messages are the Python program's.

use std::fs;
use std::path::{Path, PathBuf};

use fortis::loaders::files::Disk;

/// A fresh, empty scratch folder for one case (pytest's `tmp_path`).
fn scratch(case: &str) -> PathBuf {
    let dir = std::env::temp_dir().join(format!("fortis-file-handling-{}-{case}", std::process::id()));
    let _ = fs::remove_dir_all(&dir);
    fs::create_dir_all(&dir).unwrap();
    dir
}

fn write(dir: &Path, name: &str, text: &str) -> PathBuf {
    let path = dir.join(name);
    fs::write(&path, text).unwrap();
    path
}

mod load_toml_file {
    use super::*;
    use fortis::loaders::files::load_toml_file;

    #[test]
    fn valid_file() {
        let path = write(&scratch("toml-valid"), "test.toml", "[section]\nkey = \"value\"\n");
        let data = load_toml_file(&Disk, &path, false).unwrap();
        assert_eq!(data["section"]["key"].as_str(), Some("value"));
    }

    #[test]
    fn missing_file() {
        let path = scratch("toml-missing").join("missing.toml");
        let err = load_toml_file(&Disk, &path, false).unwrap_err();
        assert_eq!(err, format!("There is no file at '{}'", path.display()));
    }

    #[test]
    fn wrong_extension() {
        let path = write(&scratch("toml-extension"), "test.json", "{\"key\": \"value\"}");
        let err = load_toml_file(&Disk, &path, false).unwrap_err();
        assert_eq!(err, format!("File at '{}' is not a TOML file", path.display()));
    }

    #[test]
    fn empty_file() {
        let path = write(&scratch("toml-empty"), "empty.toml", "");
        let err = load_toml_file(&Disk, &path, false).unwrap_err();
        assert_eq!(err, format!("File '{}' is empty", path.display()));
    }

    #[test]
    fn non_dict_top_level() {
        // `[1, 2, 3]` is a malformed table header, so the parser rejects it. Python appends
        // tomllib's own text ("Expected ']' at the end of a table declaration (at line 1,
        // column 3)"); the toml crate words it differently, so only the Fortis part is compared.
        let path = write(&scratch("toml-list"), "list.toml", "[1, 2, 3]\n");
        let err = load_toml_file(&Disk, &path, false).unwrap_err();
        let prefix = format!("Could not open '{}': ", path.display());
        assert!(err.starts_with(&prefix), "{err}");
    }
}

mod load_csv_file {
    use super::*;
    use fortis::loaders::files::load_csv_file;

    #[test]
    fn valid_file() {
        let path = write(&scratch("csv-valid"), "test.csv", "name,age\nAlice,30\nBob,25\n");
        let (header, rows) = load_csv_file(&Disk, &path).unwrap();
        assert_eq!(header, ["name", "age"]);
        assert_eq!(rows.len(), 2);
        let cells = |i: usize| -> Vec<(String, Option<String>)> { rows[i].clone().into_iter().collect() };
        let row = |name: &str, age: &str| {
            vec![("name".to_string(), Some(name.to_string())), ("age".to_string(), Some(age.to_string()))]
        };
        assert_eq!(cells(0), row("Alice", "30"));
        assert_eq!(cells(1), row("Bob", "25"));
    }

    #[test]
    fn missing_file() {
        let path = scratch("csv-missing").join("missing.csv");
        let err = load_csv_file(&Disk, &path).unwrap_err();
        assert_eq!(err, format!("There is no file at '{}'", path.display()));
    }

    #[test]
    fn wrong_extension() {
        let path = write(&scratch("csv-extension"), "test.json", "name,age\n");
        let err = load_csv_file(&Disk, &path).unwrap_err();
        assert_eq!(err, format!("File at '{}' is not a CSV file", path.display()));
    }

    #[test]
    fn empty_file() {
        let path = write(&scratch("csv-empty"), "empty.csv", "");
        let err = load_csv_file(&Disk, &path).unwrap_err();
        assert_eq!(err, format!("File '{}' has no header row", path.display()));
    }

    #[test]
    fn header_only() {
        let path = write(&scratch("csv-header"), "header.csv", "name,age\n");
        let err = load_csv_file(&Disk, &path).unwrap_err();
        assert_eq!(err, format!("File '{}' has no data rows", path.display()));
    }
}
