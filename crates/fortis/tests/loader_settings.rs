//! The settings loader, ported from `tests/loaders/test_settings.py`. The settings structs have
//! no `PartialEq`, so their `Debug` text stands in for Python's dataclass equality.

mod common;

use std::fmt::Debug;
use std::path::Path;

use fortis::loaders::default_project_dir;
use fortis::loaders::files::Disk;
use fortis::loaders::lexicon::load_settings;
use fortis::models::{DiagnosisSettings, InductionSettings, Settings};

fn load(text: &str) -> Result<Settings, Vec<String>> {
    load_settings(&common::memory(&[("settings.toml", text)]), Path::new("settings.toml"))
}

fn debug<T: Debug>(value: &T) -> String {
    format!("{value:?}")
}

mod defaults {
    use super::*;

    #[test]
    fn missing_file_is_all_defaults() {
        let settings = load_settings(&common::memory(&[]), Path::new("nope.toml")).unwrap();
        assert_eq!(debug(&settings), debug(&Settings::default()));
    }

    #[test]
    fn empty_file_is_all_defaults() {
        assert_eq!(debug(&load("").unwrap()), debug(&Settings::default()));
    }

    #[test]
    fn shipped_default_mirrors_code_defaults() {
        // The invariant: projects/default/settings.toml must equal the built-in
        // defaults, so "file present" and "file absent" can never diverge.
        // This reads the live shipped file, as Python does, not the frozen golden copy.
        let shipped = default_project_dir().join("settings.toml");
        assert_eq!(debug(&load_settings(&Disk, &shipped).unwrap()), debug(&Settings::default()));
    }
}

mod overrides {
    use super::*;

    #[test]
    fn single_key_overrides_rest_default() {
        let settings = load("[diagnosis]\nmin_support = 5\n").unwrap();
        assert_eq!(settings.diagnosis.min_support, 5);
        assert_eq!(settings.diagnosis.min_errors, Settings::default().diagnosis.min_errors); // untouched
        assert_eq!(debug(&settings.accuracy), debug(&Settings::default().accuracy)); // whole section defaults
    }

    #[test]
    fn all_keys() {
        let text = concat!(
            "[accuracy]\ntransposition_cost = 2\n",
            "[diagnosis]\nmin_support = 4\nmin_support_percent = 25\n",
            "min_errors = 1\nreport_top = 10\nfocus_count = 3\n",
            "[induction]\nmin_improved_words = 3\ntop_confusions = 7\n",
            "contexts_per_confusion = 40\nplacement_candidates = 6\n",
            "max_rules_per_interval = 80\nalignment_distance_cap = 5\nfinal_weight = 0.5\n",
        );
        let settings = load(text).unwrap();
        assert_eq!(settings.accuracy.transposition_cost, 2);
        let diagnosis = DiagnosisSettings {
            min_support: 4,
            min_support_percent: 25,
            min_errors: 1,
            report_top: 10,
            focus_count: 3,
        };
        assert_eq!(debug(&settings.diagnosis), debug(&diagnosis));
        let induction = InductionSettings {
            min_improved_words: 3,
            top_confusions: 7,
            contexts_per_confusion: 40,
            placement_candidates: 6,
            max_rules_per_interval: 80,
            alignment_distance_cap: 5,
            final_weight: 0.5,
        };
        assert_eq!(debug(&settings.induction), debug(&induction));
    }

    #[test]
    fn final_weight_accepts_int() {
        // A bare integer is promoted to float for the one float-valued key. Python also checks
        // isinstance(..., float); the field's f64 type makes that check here.
        let settings = load("[induction]\nfinal_weight = 2\n").unwrap();
        assert_eq!(settings.induction.final_weight, 2.0);
    }
}

mod validation {
    use super::*;

    #[test]
    fn unknown_section() {
        assert_eq!(load("[nope]\nx = 1\n").unwrap_err(), ["unknown section '[nope]'"]);
    }

    #[test]
    fn unknown_key() {
        assert_eq!(load("[diagnosis]\nmadeup = 1\n").unwrap_err(), ["[diagnosis] has unknown key 'madeup'"]);
    }

    #[test]
    fn bool_is_rejected_not_coerced_to_int() {
        // bool is an int subclass in Python; `true` must NOT silently become 1.
        assert_eq!(
            load("[diagnosis]\nmin_support = true\n").unwrap_err(),
            ["[diagnosis] 'min_support' must be an integer (got True)"]
        );
    }

    #[test]
    fn non_integer_rejected() {
        assert_eq!(
            load("[accuracy]\ntransposition_cost = 1.5\n").unwrap_err(),
            ["[accuracy] 'transposition_cost' must be an integer (got 1.5)"]
        );
    }

    #[test]
    fn below_minimum_rejected() {
        assert_eq!(
            load("[diagnosis]\nmin_support = 0\n").unwrap_err(),
            ["[diagnosis] 'min_support' must be ≥ 1 (got 0)"]
        );
    }

    #[test]
    fn negative_transposition_cost_rejected() {
        assert_eq!(
            load("[accuracy]\ntransposition_cost = -1\n").unwrap_err(),
            ["[accuracy] 'transposition_cost' must be ≥ 0 (got -1)"]
        );
    }

    #[test]
    fn final_weight_bool_rejected() {
        // bool is an int subclass in Python; `true` must NOT become 1.0 on a float-valued key.
        assert_eq!(
            load("[induction]\nfinal_weight = true\n").unwrap_err(),
            ["[induction] 'final_weight' must be a number (got True)"]
        );
    }

    #[test]
    fn induction_below_minimum_rejected() {
        assert_eq!(
            load("[induction]\ntop_confusions = 0\n").unwrap_err(),
            ["[induction] 'top_confusions' must be ≥ 1 (got 0)"]
        );
    }

    #[test]
    fn errors_accumulate() {
        assert_eq!(
            load("[diagnosis]\nmin_support = 0\nmadeup = 1\n").unwrap_err(),
            ["[diagnosis] 'min_support' must be ≥ 1 (got 0)", "[diagnosis] has unknown key 'madeup'"]
        );
    }
}
