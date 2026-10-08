//! The rules loader, ported from `tests/loaders/test_rules.py`. Python's `load_time` and
//! `load_application` are private in Rust, so their cases run through `load_rule`.

mod common;

use std::path::Path;

use fortis::loaders::inventories::load_feature_inventory;
use fortis::loaders::lexicon::{load_rule, load_rule_inventory};
use fortis::models::{ApplicationMode, FeatureInventory, RuleInventory};
use toml::Table;

/// `MINIMAL_FEATURES_TOML` from `tests/conftest.py`.
const FEATURES_TOML: &str = r#"[consonantal]
tier = "segment"
kind = "binary"
short = "cons"

[sonorant]
tier = "segment"
kind = "binary"
short = "son"

[syllabic]
tier = "segment"
kind = "binary"
short = "syll"

[nasal]
tier = "segment"
kind = "binary"
short = "nas"

[lateral]
tier = "segment"
kind = "binary"
short = "lat"

[continuant]
tier = "segment"
kind = "binary"
short = "cont"

[labial]
tier = "segment"
kind = "binary"
short = "lab"

[rounded]
tier = "segment"
kind = "binary"
short = "rd"

[front]
tier = "segment"
kind = "binary"
short = "frnt"

[high]
tier = "segment"
kind = "binary"
short = "hi"

[voice]
tier = "segment"
kind = "binary"
short = "vc"

[glop]
tier = "segment"
kind = "binary"
short = "gl"

[tense]
tier = "segment"
kind = "binary"
short = "tns"

[stress]
tier = "syllable"
kind = "scalar"
short = "str"
values = { 1 = "primary", 2 = "secondary" }

[tone]
tier = "syllable"
kind = "scalar"
short = "t"
values = { 1 = "low", 2 = "mid", 3 = "high", 4 = "extra_high", 5 = "super_high" }

[length]
tier = "segment"
kind = "scalar"
short = "ln"
values = { 1 = "short", 2 = "long", 3 = "overlong" }

[manner]
tier = "segment"
kind = "unary"
short = "man"
children = ["continuant", "sonorant", "nasal", "lateral"]
"#;

/// The `features` fixture.
fn features() -> FeatureInventory {
    load_feature_inventory(&common::memory(&[("features.toml", FEATURES_TOML)]), Path::new("features.toml"))
        .expect("the minimal features load")
}

/// A rule's raw table, as the TOML loader hands it to `load_rule`.
fn table(text: &str) -> Table {
    text.parse().unwrap()
}

/// `load_rule_inventory` on a file at *path* holding *text*.
fn inventory(path: &str, text: &str) -> Result<RuleInventory, Vec<String>> {
    load_rule_inventory(&common::memory(&[(path, text)]), Path::new(path), &features())
}

fn errors(text: &[&str]) -> Vec<String> {
    text.iter().map(|e| e.to_string()).collect()
}

mod load_time {
    use super::*;

    #[test]
    fn valid() {
        let rules = load_rule("test_rule", &table("time = -2000\ndefinition = \"a → b\""), &features()).unwrap();
        assert_eq!(rules[0].time, Some(-2000));
    }

    #[test]
    fn zero() {
        let rules = load_rule("test_rule", &table("time = 0\ndefinition = \"a → b\""), &features()).unwrap();
        assert_eq!(rules[0].time, Some(0));
    }

    #[test]
    fn missing_defaults_to_none() {
        // time is optional; an untimed rule has time None (applied after every timed rule)
        let rules = load_rule("test_rule", &table("definition = \"a → b\""), &features()).unwrap();
        assert_eq!(rules[0].time, None);
    }

    #[test]
    fn non_integer() {
        let result = load_rule("test_rule", &table("time = \"not_a_number\"\ndefinition = \"a → b\""), &features());
        assert_eq!(result.unwrap_err(), errors(&["Rule 'test_rule' has non-integer 'time' value: 'not_a_number'"]));
    }
}

mod load_application {
    use super::*;

    fn application(text: &str) -> Result<ApplicationMode, Vec<String>> {
        let def = table(&format!("{text}\ndefinition = \"a → b\""));
        load_rule("test_rule", &def, &features()).map(|rules| rules[0].application)
    }

    #[test]
    fn simultaneous() {
        assert_eq!(application("application = \"simultaneous\"").unwrap(), ApplicationMode::Simultaneous);
    }

    #[test]
    fn left_to_right() {
        assert_eq!(application("application = \"left_to_right\"").unwrap(), ApplicationMode::LeftToRight);
    }

    #[test]
    fn right_to_left() {
        assert_eq!(application("application = \"right_to_left\"").unwrap(), ApplicationMode::RightToLeft);
    }

    #[test]
    fn missing_defaults_to_simultaneous() {
        assert_eq!(application("").unwrap(), ApplicationMode::Simultaneous);
    }

    #[test]
    fn invalid() {
        assert_eq!(
            application("application = \"diagonal\"").unwrap_err(),
            errors(&[
                "Rule 'test_rule' has invalid application 'diagonal' (expected simultaneous, left_to_right, right_to_left)"
            ])
        );
    }

    #[test]
    fn non_string() {
        assert_eq!(
            application("application = 42").unwrap_err(),
            errors(&["Rule 'test_rule' has non-string 'application' value: 42"])
        );
    }
}

mod load_rule {
    use super::*;

    #[test]
    fn minimal_rule() {
        let rules = load_rule("test_rule", &table("time = -2000\ndefinition = \"a → b\""), &features()).unwrap();
        let [rule] = rules.as_slice() else { panic!("a string definition yields exactly one rule") };
        assert_eq!(rule.id, "test_rule");
        assert_eq!(rule.time, Some(-2000));
        assert_eq!(rule.application, ApplicationMode::Simultaneous);
        assert_eq!(rule.name, None);
        assert_eq!(rule.description, None);
    }

    #[test]
    fn full_rule() {
        let def = table(
            r#"time = 1300
name = "Backness harmony"
description = "Backness spreads rightward"
definition = "[+syll] → [-syll]"
application = "left_to_right""#,
        );
        let rules = load_rule("backness_harmony", &def, &features()).unwrap();
        let [rule] = rules.as_slice() else { panic!("a string definition yields exactly one rule") };
        assert_eq!(rule.id, "backness_harmony");
        assert_eq!(rule.time, Some(1300));
        assert_eq!(rule.name.as_deref(), Some("Backness harmony"));
        assert_eq!(rule.description.as_deref(), Some("Backness spreads rightward"));
        assert_eq!(rule.application, ApplicationMode::LeftToRight);
    }

    #[test]
    fn list_definition_yields_ordered_subrules() {
        // A list 'definition' becomes one sub-rule per entry, with the same time and name, in
        // order, with id-suffixed ids, so a multi-step change reads as one rule.
        let def = table("time = -1500\nname = \"Final vowel loss\"\ndefinition = [\"a → b\", \"c → d\"]");
        let rules = load_rule("final_loss", &def, &features()).unwrap();
        assert_eq!(rules.iter().map(|r| r.id.as_str()).collect::<Vec<_>>(), ["final_loss#1", "final_loss#2"]);
        assert!(rules.iter().all(|r| r.time == Some(-1500) && r.name.as_deref() == Some("Final vowel loss")));
        assert_eq!(rules.iter().map(|r| r.raw_definition.as_str()).collect::<Vec<_>>(), ["a → b", "c → d"]);
    }

    #[test]
    fn empty_definition_list_is_an_error() {
        let result = load_rule("bad", &table("time = 0\ndefinition = []"), &features());
        assert_eq!(result.unwrap_err(), errors(&["Rule 'bad' has an empty 'definition' list"]));
    }

    #[test]
    fn one_bad_definition_fails_the_whole_rule() {
        let result = load_rule("bad", &table("time = 0\ndefinition = [\"a → b\", \"→ → →\"]"), &features());
        assert_eq!(result.unwrap_err(), errors(&["unexpected ARROW at position 2"]));
    }

    #[test]
    fn missing_time_defaults_to_none() {
        let rules = load_rule("untimed", &table("definition = \"a → b\""), &features()).unwrap();
        assert_eq!(rules[0].time, None);
    }

    #[test]
    fn words_restricts_the_rule() {
        // a 'words' list (string or list) scopes the rule to those words by ipa or gloss
        let single = load_rule("sporadic", &table("definition = \"a → b\"\nwords = \"sun\""), &features());
        assert_eq!(single.unwrap()[0].words, ["sun"]);
        let listed = load_rule("sporadic", &table("definition = \"a → b\"\nwords = [\"sun\", \"ear\"]"), &features());
        assert_eq!(listed.unwrap()[0].words, ["sun", "ear"]);
        let bad = load_rule("sporadic", &table("definition = \"a → b\"\nwords = [1]"), &features());
        assert_eq!(
            bad.unwrap_err(),
            errors(&["Rule 'sporadic' has a 'words' that is not a string or list of strings"])
        );
    }

    #[test]
    fn missing_definition() {
        let result = load_rule("bad", &table("time = 0"), &features());
        assert_eq!(result.unwrap_err(), errors(&["Rule 'bad' is missing the required 'definition' field"]));
    }

    #[test]
    fn invalid_definition() {
        let result = load_rule("bad", &table("time = 0\ndefinition = \"→ → →\""), &features());
        assert_eq!(result.unwrap_err(), errors(&["unexpected ARROW at position 2"]));
    }
}

mod load_rule_inventory {
    use super::*;

    #[test]
    fn from_file() {
        let text = r#"[laryngeal_coloring]
time = -2000
name = "Laryngeal coloring"
definition = "m → n"

[voicing_assimilation]
time = -2000
definition = "[+cons, -voice] → [-voice]"
"#;
        let inv = inventory("rules.toml", text).unwrap();
        let rules = &inv.by_time[&Some(-2000)];
        assert_eq!(rules.len(), 2);
        assert_eq!(rules[0].id, "laryngeal_coloring");
        assert_eq!(rules[1].id, "voicing_assimilation");
    }

    #[test]
    fn rules_at_different_times() {
        let text = r#"[early_rule]
time = -2000
definition = "m → n"

[late_rule]
time = 1000
definition = "a → b"
"#;
        let inv = inventory("rules.toml", text).unwrap();
        assert_eq!(inv.by_time[&Some(-2000)].len(), 1);
        assert_eq!(inv.by_time[&Some(1000)].len(), 1);
    }

    #[test]
    fn missing_file() {
        let result = load_rule_inventory(&common::memory(&[]), Path::new("nonexistent.toml"), &features());
        assert_eq!(result.unwrap_err(), errors(&["There is no file at 'nonexistent.toml'"]));
    }

    #[test]
    fn null_insertion_rule() {
        // Rule with ∅ (null) in definition.
        let text = "[epenthesis]\ntime = -1000\ndefinition = \"∅ [+cons] → u\"\n";
        assert!(inventory("rules.toml", text).is_ok());
    }

    #[test]
    fn duplicate_rule_id_is_an_error() {
        // A list definition mints foo#1/foo#2; an explicit "foo#1" table collides.
        let text = r#"[foo]
time = 0
definition = ["a → b", "c → d"]

["foo#1"]
time = 0
definition = "e → f"
"#;
        assert_eq!(inventory("rules.toml", text).unwrap_err(), errors(&["duplicate rule id 'foo#1'"]));
    }
}

mod load_rule_inventory_csv {
    use super::*;

    #[test]
    fn from_file() {
        let text = concat!(
            "id,time,name,description,definition,application,words\n",
            "laryngeal_coloring,-2000,Laryngeal coloring,,m → n,,\n",
            // the definition contains a comma, so it must be quoted (RFC 4180)
            "voicing_assimilation,-2000,,,\"[+cons, -voice] → [-voice]\",,\n",
        );
        let inv = inventory("rules.csv", text).unwrap();
        let rules = &inv.by_time[&Some(-2000)];
        assert_eq!(rules.len(), 2);
        assert_eq!(rules[0].id, "laryngeal_coloring");
        assert_eq!(rules[0].name.as_deref(), Some("Laryngeal coloring"));
        assert_eq!(rules[1].id, "voicing_assimilation");
    }

    #[test]
    fn empty_time_is_untimed() {
        let inv = inventory("rules.csv", "id,time,definition\nr,,a → b\n").unwrap();
        assert_eq!(inv.by_time[&None][0].time, None);
    }

    #[test]
    fn multipart_definition_via_semicolons() {
        let inv = inventory("rules.csv", "id,time,definition\nmulti,0,a → b;c → d\n").unwrap();
        let rules = &inv.by_time[&Some(0)];
        assert_eq!(rules.iter().map(|r| r.id.as_str()).collect::<Vec<_>>(), ["multi#1", "multi#2"]);
        assert_eq!(rules.iter().map(|r| r.raw_definition.as_str()).collect::<Vec<_>>(), ["a → b", "c → d"]);
    }

    #[test]
    fn words_scope_via_semicolons() {
        let inv = inventory("rules.csv", "id,definition,words\nr,a → b,sun;ear\n").unwrap();
        assert_eq!(inv.by_time[&None][0].words, ["sun", "ear"]);
    }

    #[test]
    fn column_order_is_free() {
        let inv = inventory("rules.csv", "definition,id,time\na → b,r,-100\n").unwrap();
        assert_eq!(inv.by_time[&Some(-100)][0].id, "r");
        assert_eq!(inv.by_time[&Some(-100)][0].raw_definition, "a → b");
    }

    #[test]
    fn empty_id_is_an_error() {
        let result = inventory("rules.csv", "id,definition\n,a → b\n");
        assert_eq!(result.unwrap_err(), errors(&["line 2: empty rule id"]));
    }

    #[test]
    fn missing_definition_cell_is_an_error() {
        let result = inventory("rules.csv", "id,definition\nr,\n");
        assert_eq!(result.unwrap_err(), errors(&["rule 'r': Rule 'r' is missing the required 'definition' field"]));
    }

    #[test]
    fn missing_id_column_is_an_error() {
        let result = inventory("rules.csv", "time,definition\n0,a → b\n");
        assert_eq!(result.unwrap_err(), errors(&["'rules.csv' must have an 'id' column (the rule slug)"]));
    }

    #[test]
    fn missing_definition_column_is_an_error() {
        let result = inventory("rules.csv", "id,time\nr,0\n");
        assert_eq!(result.unwrap_err(), errors(&["'rules.csv' must have a 'definition' column"]));
    }

    #[test]
    fn unknown_column_is_an_error() {
        let result = inventory("rules.csv", "id,definition,colour\nr,a → b,blue\n");
        assert_eq!(result.unwrap_err(), errors(&["'rules.csv' has unknown column(s): colour"]));
    }

    #[test]
    fn non_integer_time_is_an_error() {
        let result = inventory("rules.csv", "id,time,definition\nr,soon,a → b\n");
        assert_eq!(result.unwrap_err(), errors(&["rule 'r': Rule 'r' has non-integer 'time' value: 'soon'"]));
    }
}

/// A representative rules block must load identically from CSV and from TOML.
mod csv_toml_equivalence {
    use super::*;

    type Flat = (String, Option<i64>, String, Option<String>, Option<String>, ApplicationMode, Vec<String>);

    fn flat(inv: &RuleInventory) -> Vec<Flat> {
        inv.in_file_order()
            .map(|r| {
                let r = r.as_ref().clone();
                (r.id, r.time, r.raw_definition, r.name, r.description, r.application, r.words)
            })
            .collect()
    }

    #[test]
    fn round_trip_is_identical() {
        let toml_content = r#"[cl_assim]
time = -100
name = "Assimilation"
description = "n before a velar"
definition = "n → ŋ / _ k"

[cl_multi]
time = -100
definition = ["a → e", "o → u"]

[cl_scoped]
time = -100
application = "left_to_right"
words = ["sun", "ear"]
definition = "s → h / _ #"

[untimed_last]
definition = "b → p / _ #"
"#;
        let csv_content = concat!(
            "id,time,name,description,definition,application,words\n",
            "cl_assim,-100,Assimilation,n before a velar,n → ŋ / _ k,,\n",
            "cl_multi,-100,,,a → e;o → u,,\n",
            "cl_scoped,-100,,,s → h / _ #,left_to_right,sun;ear\n",
            "untimed_last,,,,b → p / _ #,,\n",
        );
        let inv_toml = inventory("rules.toml", toml_content).unwrap();
        let inv_csv = inventory("rules.csv", csv_content).unwrap();
        assert_eq!(flat(&inv_toml), flat(&inv_csv));
    }
}
