"""Tests for automatic tonal stability (a deleted vowel's tone survives; stress does not)."""

from src.fortis.application.deriving import derive
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.autosegment import Autoseg
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.notation import parse_definition

# Delete the first vowel (the one after the word-initial consonant).
_DELETE_FIRST_VOWEL = "[+syllabic] → ∅ / # [-syllabic] _"


def _autoseg(feature, value, autoseg_id):
    return Autoseg(FeatureBundle({feature: FeatureSpec(feature, value)}), autoseg_id)


def _derive_deleting_first_vowel(form, project):
    sd = parse_definition(_DELETE_FIRST_VOWEL, project.features).unwrap()
    rule = Rule(id="del", time=0, raw_definition="del", sd=sd)
    return derive(
        Word(ipa="taka"),
        form,
        RuleInventory({0: (rule,)}),
        project.letters,
        project.features,
        project.sonorities,
        project.syllable_parts,
        project.tiers,
    ).surface


def test_tone_survives_its_vowels_deletion(project):
    form = string_to_sequence("taka", project)  # t a k a
    h_id = form.fresh_id()
    form.tiers["tone"].autosegs.append(_autoseg("tone", 4, h_id))
    form.tiers["tone"].links.add((h_id, 1))  # H on the first vowel
    surface = _derive_deleting_first_vowel(form, project)
    assert len(surface.segments) == 3  # the first vowel is gone
    # the H is not lost: it survives, anchored to the surviving nucleus
    assert any(autoseg == h_id for (autoseg, _anchor) in surface.tiers["tone"].links)
    assert 4 in [b["tone"].value for b in lower_tiers(surface) if "tone" in b]


def test_stress_does_not_follow_a_deletion(project):
    # Stress is metrical (melody=false): a deleted stressed vowel's stress does NOT carry.
    form = string_to_sequence("taka", project)
    s_id = form.fresh_id()
    form.tiers["stress"].autosegs.append(_autoseg("stress", 2, s_id))
    form.tiers["stress"].links.add((s_id, 1))  # stress on the first vowel
    surface = _derive_deleting_first_vowel(form, project)
    assert not any(autoseg == s_id for (autoseg, _anchor) in surface.tiers["stress"].links)
