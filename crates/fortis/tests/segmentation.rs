//! IPA segmentation: a port of `tests/application/test_segmentation.py`. These run against the
//! frozen default project's inventories. The expected error messages are the Python program's.
//! Combining marks are written as escapes so the base letter they attach to stays visible.

mod common;

use fortis::engine::rendering::Renderer;
use fortis::engine::segmentation::string_to_sequence;
use fortis::engine::tiers::lower_tiers;
use fortis::models::*;

fn id(project: &Project, feature: &str) -> FeatId {
    project.features.id(feature).unwrap()
}

mod string_to_sequence {
    use super::*;

    #[test]
    fn known_word_segments() {
        // xenti is five segments: x e n t i.
        let project = common::default_project();
        assert_eq!(string_to_sequence("xenti", &project).unwrap().bundles().len(), 5);
    }

    #[test]
    fn diacritics_attach_to_their_base() {
        // ɣʷeroː is four segments: the labialisation and length are diacritics on their bases,
        // not separate segments.
        let project = common::default_project();
        assert_eq!(string_to_sequence("ɣʷeroː", &project).unwrap().bundles().len(), 4);
    }

    #[test]
    fn unknown_character_raises() {
        // A section sign is not in any inventory.
        let project = common::default_project();
        assert_eq!(string_to_sequence("xen§ti", &project).unwrap_err(), "Unknown character '§' at position 3");
    }

    #[test]
    fn syllable_tier_diacritic_attaches_to_nucleus() {
        // A syllable-tier tone mark written after the coda must land on the syllable's nucleus,
        // not an earlier segment (U+0304 is tone 3). Guards the last-nucleus path, which no plain
        // lexicon word exercises. Tone lives on the tier, so read it back per segment through
        // lower_tiers.
        let project = common::default_project();
        let seq = lower_tiers(&string_to_sequence("tan\u{304}", &project).unwrap());
        let tone = id(&project, "tone");
        assert_eq!(seq.iter().map(|s| s.contains(tone)).collect::<Vec<_>>(), [false, true, false]); // on the a
    }

    #[test]
    fn word_initial_nucleus_tier_diacritic() {
        // The nucleus is segment 0 here; the tone must land on it (not on index -1).
        let project = common::default_project();
        let seq = lower_tiers(&string_to_sequence("an\u{304}", &project).unwrap());
        assert_eq!(seq[0].get(id(&project, "tone")), Some(&Value::int(3)));
    }

    #[test]
    fn stress_attaches_to_a_diacritic_made_nucleus() {
        // ˈl̩: the syllabic diacritic makes l a nucleus *after* the letter is read; the pending
        // stress must still attach to it (not get stranded or skipped).
        let project = common::default_project();
        let seq = lower_tiers(&string_to_sequence("ˈl\u{329}", &project).unwrap());
        assert!(seq[0].contains(id(&project, "stress")));
    }

    #[test]
    fn stress_not_stolen_by_a_later_plain_vowel() {
        // ˈl̩a: stress belongs to the syllabic l̩, not the following plain vowel a.
        let project = common::default_project();
        let seq = lower_tiers(&string_to_sequence("ˈl\u{329}a", &project).unwrap());
        let stress = id(&project, "stress");
        assert!(seq[0].contains(stress) && !seq[1].contains(stress));
    }
}

mod round_trip {
    use super::*;

    #[test]
    fn feature_level_round_trip_for_all_words() {
        // Render-then-resegment recovers the same segments for every lexicon word. (String
        // equality can differ only by diacritic ordering, e.g. gʲʱ vs gʱʲ, the same feature
        // bundle written two ways, so the feature level is the invariant that must hold.)
        // The Python test looped over the lexicon's keys, which are word ids, not IPA.
        let project = common::default_project();
        let r = Renderer::new(&project);
        for word in project.words.values() {
            let seq = string_to_sequence(word.ipa(), &project).unwrap().bundles();
            let reseg = string_to_sequence(&r.sequence(&seq), &project).unwrap().bundles();
            assert_eq!(seq, reseg, "{}", word.ipa());
        }
    }
}

mod floating_tone {
    use super::*;

    /// A floating high tone: dotted circle + combining acute, in float brackets.
    const FLOAT_HIGH: &str = "⟨◌\u{301}⟩";

    #[test]
    fn marker_creates_a_positioned_float() {
        let project = common::default_project();
        let form = string_to_sequence(&format!("kata{FLOAT_HIGH}"), &project).unwrap();
        assert_eq!(form.segments.len(), 4); // the marker adds no segment
        let tier = &form.tiers["tone"];
        assert_eq!(tier.autosegs.len(), 1);
        let autoseg = &tier.autosegs[0];
        assert_eq!(autoseg.bundle.get(id(&project, "tone")), Some(&Value::int(4))); // high
        assert!(!tier.links.iter().any(|(a, _)| *a == autoseg.id)); // floating, no anchor
        assert_eq!(tier.float_hosts.get(&autoseg.id), Some(&(3, Side::After))); // after the final segment
    }

    #[test]
    fn word_initial_float_is_before_the_first_segment() {
        let project = common::default_project();
        let form = string_to_sequence(&format!("{FLOAT_HIGH}kata"), &project).unwrap();
        let tier = &form.tiers["tone"];
        assert_eq!(tier.float_hosts.get(&tier.autosegs[0].id), Some(&(0, Side::Before)));
    }

    #[test]
    fn unterminated_float_marker_rejected() {
        let project = common::default_project();
        let err = string_to_sequence("ka⟨◌\u{301}", &project).unwrap_err();
        assert_eq!(err, "unterminated floating tone '⟨' at position 2");
    }
}

/// A ˈ is not lost when the syllable's first vowel is made non-syllabic by a diacritic.
///
/// The mark is buffered and flushed onto the first segment that is a nucleus AT LETTER-APPEND
/// time. In `ˈe̯a`, the letter `e` IS syllabic when appended and so claims the stress, and then
/// the `̯` makes it non-syllabic, no tier can anchor the autoseg (`anchor: +syllabic`) and
/// `stray_erase` deleted it. `ˈɲaws` kept its stress; `ˈɲe̯aws` silently lost it, in the
/// lexicon's ATTESTED forms as much as in derived ones (targets are ingested through here).
/// The suprasegmentals must be handed back so the syllable's real nucleus claims them.
#[test]
fn stress_survives_a_diacritic_that_unmakes_the_nucleus() {
    let project = common::default_project();
    // The syllable-tier features of each segment that carries any.
    let carriers = |text: &str| -> Vec<Vec<(&str, Value)>> {
        let form = string_to_sequence(text, &project).unwrap();
        lower_tiers(&form)
            .iter()
            .map(|bundle| {
                project
                    .syllable_features
                    .iter()
                    .filter_map(|&f| bundle.get(f).map(|v| (project.features.name(f), v.clone())))
                    .collect::<Vec<_>>()
            })
            .filter(|carried| !carried.is_empty())
            .collect()
    };
    let stressed = vec![vec![("stress", Value::int(2))]];
    assert_eq!(carriers("ˈnaws"), stressed); // control: no unmaking diacritic
    // The on-glide is made non-syllabic; the stress must move on to the real nucleus, not vanish.
    assert_eq!(carriers("ˈne\u{32F}aws"), stressed);
    assert_eq!(carriers("ˈe\u{32F}aws"), stressed);
}
