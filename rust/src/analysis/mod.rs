//! Analyses that read the derivations: accuracy, error diagnosis, blame, warnings, the
//! dependency graph and the lint.

pub mod accuracy;
pub mod blame;
pub mod dependencies;
pub mod diagnosis;
pub mod diagnostics;
pub mod reporting;
pub mod warnings;
