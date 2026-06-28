"""Tests for automatic tonal stability (a deleted vowel's tone survives; stress does not)."""

from dataclasses import replace

from src.fortis.application.deriving import derive
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.autosegment import Autoseg
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.tier_declaration import TierInventory
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


# Replace the first vowel with a different one — a letter swap, so a fresh segment (not a
# feature-merge); the nucleus is rewritten in place rather than deleted.
def _derive_replacing_first_vowel(form, project):
    sd = parse_definition("a → e / # [-syllabic] _", project.features).unwrap()
    rule = Rule(id="rep", time=0, raw_definition="rep", sd=sd)
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


def test_tone_survives_a_nucleus_replacement(project):
    # Suprasegmentals are exempt from the merge requirement: a letter swap that REPLACES the
    # nucleus (a fresh segment) still keeps its tone, re-anchored onto the new vowel.
    form = string_to_sequence("taka", project)  # t a k a
    h_id = form.fresh_id()
    form.tiers["tone"].autosegs.append(_autoseg("tone", 4, h_id))
    form.tiers["tone"].links.add((h_id, 1))  # H on the first vowel
    surface = _derive_replacing_first_vowel(form, project)  # a → e in place
    assert any(autoseg == h_id for (autoseg, _anchor) in surface.tiers["tone"].links)
    assert 4 in [b["tone"].value for b in lower_tiers(surface) if "tone" in b]


def test_stress_survives_a_nucleus_replacement(project):
    # Unlike a deletion, a nucleus REWRITE keeps the stress too — suprasegmentals are exempt.
    form = string_to_sequence("taka", project)
    s_id = form.fresh_id()
    form.tiers["stress"].autosegs.append(_autoseg("stress", 2, s_id))
    form.tiers["stress"].links.add((s_id, 1))  # stress on the first vowel
    surface = _derive_replacing_first_vowel(form, project)
    assert any(autoseg == s_id for (autoseg, _anchor) in surface.tiers["stress"].links)


def test_stability_direction_is_per_tier(project):
    # stability="right" carries a stranded tone to the RIGHT syllable; left (default) to the
    # left. takata, deleting the middle vowel: left lands on vowel 1, right on the last vowel.
    definition = "[+syllabic] → ∅ / [+syllabic] [-syllabic] _ [-syllabic]"
    rule = Rule(
        id="del",
        time=0,
        raw_definition="del",
        sd=parse_definition(definition, project.features).unwrap(),
    )

    def carried_position(direction):
        form = string_to_sequence("takata", project)  # t a k a t a — vowels at 1, 3, 5
        h_id = form.fresh_id()
        form.tiers["tone"].autosegs.append(_autoseg("tone", 4, h_id))
        form.tiers["tone"].links.add((h_id, 3))  # H on the middle vowel
        tiers = TierInventory()
        tiers["tone"] = replace(project.tiers["tone"], stability=direction)
        tiers["stress"] = project.tiers["stress"]
        surface = derive(
            Word(ipa="takata"),
            form,
            RuleInventory({0: (rule,)}),
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
            tiers,
        ).surface
        return [i for i, b in enumerate(lower_tiers(surface)) if "tone" in b]

    assert carried_position("left") == [1]  # the preceding syllable
    assert carried_position("right") == [4]  # the following syllable
