//! Helpers shared by the integration tests. Include with `mod common;`.
#![allow(dead_code)]

use std::path::{Path, PathBuf};

use fortis::loaders::files::{Disk, Memory};
use fortis::loaders::load_project_from;
use fortis::models::Project;

/// The frozen copies of the shipped projects, also used by the golden tests.
pub fn projects() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("tests").join("golden").join("projects")
}

/// The frozen default project (`tests/golden/projects/default`).
pub fn default_project() -> Project {
    let dir = projects().join("default");
    load_project_from(&Disk, &dir, None, None, None).expect("the frozen default project loads")
}

/// An in-memory file source holding *files*, each a (path, text) pair.
pub fn memory(files: &[(&str, &str)]) -> Memory {
    let mut source = Memory::default();
    for (path, text) in files {
        source.0.insert(PathBuf::from(path), text.to_string());
    }
    source
}
