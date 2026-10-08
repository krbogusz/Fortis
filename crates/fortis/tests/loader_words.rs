//! The words loader, ported from `tests/loaders/test_words.py`.

mod common;

use std::collections::BTreeSet;
use std::path::Path;

use fortis::loaders::lexicon::load_word_inventory;
use fortis::models::{Word, WordInventory, time_order};

fn load_toml(text: &str) -> Result<WordInventory, Vec<String>> {
    load_word_inventory(&common::memory(&[("words.toml", text)]), Path::new("words.toml"))
}

fn load_csv(text: &str) -> Result<WordInventory, Vec<String>> {
    load_word_inventory(&common::memory(&[("words.csv", text)]), Path::new("words.csv"))
}

/// `"<ipa>" = "<gloss>"`: a word that is only a seed, with no targets.
mod concise_form {
    use super::*;

    #[test]
    fn valid() {
        let inventory = load_toml("\"anpa\" = \"before\"\n\"atta\" = \"eight\"\n").unwrap();
        assert_eq!(inventory.keys().collect::<Vec<_>>(), ["anpa", "atta"]);
        assert_eq!(inventory["anpa"].seed().ipa, "anpa");
        assert_eq!(inventory["anpa"].gloss, "before");
        assert_eq!(inventory["anpa"].targets().count(), 0); // a seed is not something to score against
    }

    #[test]
    fn empty_gloss() {
        assert_eq!(load_toml("\"anpa\" = \"\"\n").unwrap()["anpa"].gloss, "");
    }

    #[test]
    fn a_table_value_is_rejected() {
        // The old ipa-keyed table form. A word with targets now goes in a [[words]] table.
        let errors = load_toml("\"anpa\" = {gloss = \"x\", final = \"y\"}\n").unwrap_err();
        assert_eq!(
            errors[0],
            "Word 'anpa' must be a gloss string (the concise form); a word with targets goes in a [[words]] table"
        );
    }

    #[test]
    fn missing_file() {
        let result = load_word_inventory(&common::memory(&[]), Path::new("nope.toml"));
        assert_eq!(result.unwrap_err(), ["There is no file at 'nope.toml'"]);
    }
}

/// `[[words]]`: id, gloss, frequency, and a series of forms through time.
mod words_array {
    use super::*;

    pub const LEXICON: &str = r#"
[[words]]
id = "bear-v"
gloss = "to bear"
frequency = 1200
forms = [
  { time = -2000,   ipa = "bʱereti", category = "verb.pres.3sg" },
  { time = 200,     ipa = "biriði",  category = "verb.pres.3sg.strong" },
  { time = "final", ipa = "beəz" },
]
"#;

    fn bear() -> Word {
        load_toml(LEXICON).unwrap()["bear-v"].clone()
    }

    #[test]
    fn full_word() {
        let word = bear();
        assert_eq!(word.id, "bear-v");
        assert_eq!(word.gloss, "to bear");
        assert_eq!(word.frequency, 1200);
        assert_eq!(word.seed_time(), Some(-2000));
        assert_eq!(word.seed().ipa, "bʱereti");
    }

    #[test]
    fn the_earliest_form_is_the_seed_and_is_not_a_target() {
        let word = bear();
        assert_eq!(word.ipa(), "bʱereti"); // the derivation input
        // scored against; the seed is not among them
        assert_eq!(word.targets().map(|(t, _)| *t).collect::<BTreeSet<_>>(), BTreeSet::from([Some(200), None]));
        assert_eq!(word.stages(), [(200, "biriði")]);
        assert_eq!(word.final_ipa(), Some("beəz"));
    }

    #[test]
    fn final_is_the_untimed_slot() {
        // "final" is not a year: an untimed rule runs after every timed one, so the form after
        // it cannot be dated. It keys as None, and sorts last.
        let word = bear();
        assert_eq!(word.form_at(None).unwrap().ipa, "beəz");
    }

    #[test]
    fn category_is_read_per_form() {
        let word = bear();
        assert_eq!(word.form_at(Some(-2000)).unwrap().category, "verb.pres.3sg");
        assert_eq!(word.form_at(Some(200)).unwrap().category, "verb.pres.3sg.strong");
        assert_eq!(word.form_at(None).unwrap().category, ""); // omitted means empty, never guessed
    }

    #[test]
    fn category_in_force_is_the_latest_at_or_before() {
        // This is what a category-scoped rule reads, and it is why a category given at a LATER
        // time expresses a reanalysis: every rule from that time on sees the new one.
        let word = bear();
        assert_eq!(word.category_at(Some(-2000)), "verb.pres.3sg");
        assert_eq!(word.category_at(Some(-500)), "verb.pres.3sg"); // still the seed's
        assert_eq!(word.category_at(Some(200)), "verb.pres.3sg.strong"); // the 200 entry takes effect
        assert_eq!(word.category_at(Some(900)), "verb.pres.3sg.strong"); // and stays in force
        assert_eq!(word.category_at(Some(-9999)), "verb.pres.3sg"); // before everything: the seed's
    }

    #[test]
    fn defaults() {
        let word = load_toml("[[words]]\nid = \"a\"\nforms = [{ time = 0, ipa = \"a\" }]\n").unwrap()["a"].clone();
        assert!(word.gloss.is_empty() && word.frequency == 1 && word.seed().category.is_empty());
        assert!(word.note.is_empty() && word.seed().note.is_empty());
    }

    #[test]
    fn provenance_note_round_trips_on_word_and_form() {
        // A note is free-text provenance the engine ignores; it is carried on the word and on any
        // of its forms so a lexicon can document its own evidence.
        let text = r#"
[[words]]
id = "heart"
gloss = "heart"
note = "n-stem gender reanalysis: PGmc neuter *hertô is OE feminine heorte"
forms = [
  { time = -2000, ipa = "kʲerdoː", note = "PIE *ḱḗr, cited by Wiktionary" },
  { time = 900, ipa = "xeorte" },
]
"#;
        let word = load_toml(text).unwrap()["heart"].clone();
        assert!(word.note.starts_with("n-stem gender reanalysis"));
        assert_eq!(word.form_at(Some(-2000)).unwrap().note, "PIE *ḱḗr, cited by Wiktionary");
        assert_eq!(word.form_at(Some(900)).unwrap().note, ""); // omitted means empty
    }

    #[test]
    fn a_form_with_an_unknown_key_is_rejected() {
        let errors =
            load_toml("[[words]]\nid = \"a\"\nforms = [{ time = 0, ipa = \"a\", src = \"x\" }]\n").unwrap_err();
        assert_eq!(errors[0], "Word 'a' has a form at 0 with unknown key(s): src");
    }

    #[test]
    fn coexists_with_the_concise_form() {
        // ABOVE the array: TOML binds a bare key/value to the table header above it, so a
        // concise entry written below [[words]] would become a key of that word.
        let inventory = load_toml(&format!("\"atta\" = \"eight\"\n{LEXICON}")).unwrap();
        assert_eq!(inventory.keys().map(String::as_str).collect::<BTreeSet<_>>(), BTreeSet::from(["bear-v", "atta"]));
    }

    #[test]
    fn concise_entry_below_the_array_says_why() {
        let errors = load_toml(&format!("{LEXICON}\n\"atta\" = \"eight\"\n")).unwrap_err();
        assert_eq!(
            errors[0],
            "Word 'bear-v' has unknown key(s): atta — a concise entry ('atta') must go ABOVE every [[words]] \
             table, or TOML reads it as a key of the word above it"
        );
    }

    #[test]
    fn errors() {
        let cases = [
            ("[[words]]\nforms = [{time=0, ipa=\"a\"}]", "words[0] has no 'id'"),
            ("[[words]]\nid = \"a\"", "Word 'a' has no 'forms' (a word needs at least its seed)"),
            ("[[words]]\nid = \"a\"\nforms = []", "Word 'a' has no 'forms' (a word needs at least its seed)"),
            ("[[words]]\nid = \"a\"\nforms = [{time=0}]", "Word 'a' has a form at 0 with no 'ipa'"),
            ("[[words]]\nid = \"a\"\nforms = [{ipa=\"a\"}]", "Word 'a' has a form with no integer (or 'final') 'time'"),
            (
                "[[words]]\nid = \"a\"\nforms = [{time=\"soon\", ipa=\"a\"}]",
                "Word 'a': time 'soon' is neither an integer nor 'final'",
            ),
            (
                "[[words]]\nid = \"a\"\nforms = [{time=0, ipa=\"a\", category=7}]",
                "Word 'a' has a form at 0 whose category is not a string",
            ),
            (
                "[[words]]\nid = \"a\"\nfrequency = 0\nforms = [{time=0, ipa=\"a\"}]",
                "Word 'a' has a 'frequency' that is not a positive integer",
            ),
            (
                "[[words]]\nid = \"a\"\nfrequency = true\nforms = [{time=0, ipa=\"a\"}]",
                "Word 'a' has a 'frequency' that is not a positive integer",
            ),
            ("[[words]]\nid = \"a\"\nnope = 1\nforms = [{time=0, ipa=\"a\"}]", "Word 'a' has unknown key(s): nope"),
        ];
        for (table, expected) in cases {
            assert_eq!(load_toml(table).unwrap_err()[0], expected, "for {table:?}");
        }
    }

    #[test]
    fn duplicate_id_errors() {
        let text = "[[words]]\nid = \"a\"\nforms = [{time=0, ipa=\"a\"}]\n".repeat(2);
        assert_eq!(load_toml(&text).unwrap_err()[0], "Word 'a' is already defined");
    }

    #[test]
    fn two_forms_at_one_time_errors() {
        let text = "[[words]]\nid = \"a\"\nforms = [{time=0, ipa=\"a\"}, {time=0, ipa=\"b\"}]\n";
        assert_eq!(load_toml(text).unwrap_err()[0], "Word 'a' has two forms at 0");
    }
}

/// One row per attested form: the long shape, so a category can vary with time.
mod csv {
    use super::*;

    pub const LEXICON: &str = concat!(
        "id,time,ipa,category,gloss,frequency\n",
        "bear-v,-2000,bʱereti,verb.pres.3sg,to bear,1200\n",
        "bear-v,200,biriði,verb.pres.3sg.strong,,\n",
        "bear-v,final,beəz,,,\n",
    );

    #[test]
    fn rows_sharing_an_id_are_one_word() {
        let inventory = load_csv(LEXICON).unwrap();
        assert_eq!(inventory.keys().collect::<Vec<_>>(), ["bear-v"]);
        let word = &inventory["bear-v"];
        assert_eq!(word.seed().ipa, "bʱereti");
        assert_eq!(word.stages(), [(200, "biriði")]);
        assert_eq!(word.final_ipa(), Some("beəz"));
        assert!(word.gloss == "to bear" && word.frequency == 1200);
    }

    #[test]
    fn category_per_row() {
        let inventory = load_csv(LEXICON).unwrap();
        assert_eq!(inventory["bear-v"].category_at(Some(200)), "verb.pres.3sg.strong");
    }

    #[test]
    fn row_order_does_not_matter() {
        let rows: Vec<&str> = LEXICON.lines().collect();
        let shuffled = [rows[0], rows[3], rows[1], rows[2]].join("\n") + "\n";
        assert_eq!(load_csv(&shuffled).unwrap()["bear-v"].seed().ipa, "bʱereti");
    }

    #[test]
    fn quoted_comma_gloss() {
        let text = "id,time,ipa,gloss\na,0,a,\"amère, bitter\"\n";
        assert_eq!(load_csv(text).unwrap()["a"].gloss, "amère, bitter");
    }

    #[test]
    fn errors() {
        let cases = [
            ("time,ipa\n0,a\n", "'words.csv' is missing required column(s): id"),
            ("id,time,ipa,wat\na,0,a,x\n", "'words.csv' has unknown column(s): wat"),
            ("id,time,ipa\n,0,a\n", "line 2: row has an empty 'id'"),
            ("id,time,ipa\na,0,\n", "line 2: word 'a' has an empty 'ipa'"),
            ("id,time,ipa\na,soon,a\n", "line 2: time 'soon' is neither an integer nor 'final'"),
            ("id,time,ipa\na,0,a\na,0,b\n", "line 3: word 'a' already has a form at 0"),
            ("id,time,ipa,frequency\na,0,a,0\n", "line 2: word 'a' has a 'frequency' that is not a positive integer"),
            ("id,time,ipa,gloss\na,0,a,x\na,1,b,y\n", "line 3: word 'a' has two different glosses"),
        ];
        for (text, expected) in cases {
            assert_eq!(load_csv(text).unwrap_err()[0], expected, "for {text:?}");
        }
    }
}

mod csv_toml_equivalence {
    use super::*;

    /// Python compares `Word` dataclasses, whose `forms` is a dict (order-blind). `Word` has no
    /// `PartialEq`, so compare its `Debug` text with the forms in time order.
    fn normalized(word: &Word) -> String {
        let mut word = word.clone();
        word.forms.sort_by_key(|(t, _)| time_order(*t));
        format!("{word:?}")
    }

    #[test]
    fn same_inventory() {
        // The two serialisations are two spellings of one model.
        let from_toml = load_toml(words_array::LEXICON).unwrap();
        let from_csv = load_csv(csv::LEXICON).unwrap();
        assert_eq!(from_toml.keys().collect::<BTreeSet<_>>(), from_csv.keys().collect::<BTreeSet<_>>());
        for key in from_toml.keys() {
            assert_eq!(normalized(&from_toml[key]), normalized(&from_csv[key]));
        }
    }
}
