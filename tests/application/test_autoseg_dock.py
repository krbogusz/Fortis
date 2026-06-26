"""Tests for floating-tone docking (a ``⟨...⟩`` floating autosegment associates to an anchor)."""

from src.fortis.application.deriving import derive
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.autosegment import Autoseg
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.notation import parse_definition

_DOCK = "⟨tone: ~1=high⟩ [+syllabic, tone: none] → [+syllabic, tone: ~1]"


def _rule(definition, features):
    sd = parse_definition(definition, features).unwrap()
    return Rule(id="r", time=0, raw_definition=definition, sd=sd)


def _derive(form, project):
    return derive(
        Word(ipa="ta"),
        form,
        RuleInventory({0: (_rule(_DOCK, project.features),)}),
        project.letters,
        project.features,
        project.sonorities,
        project.syllable_parts,
        project.tiers,
    ).surface


def test_floating_tone_docks_onto_a_toneless_syllable(project):
    form = string_to_sequence("ta", project)
    floating_id = form.fresh_id()
    form.tiers["tone"].autosegs.append(
        Autoseg(FeatureBundle({"tone": FeatureSpec("tone", 4)}), floating_id)  # floating H, no link
    )
    surface = _derive(form, project)
    assert (floating_id, 1) in surface.tiers["tone"].links  # the once-floating H is now anchored
    assert lower_tiers(surface)[1]["tone"].value == 4  # the nucleus reads high


def test_no_dock_without_a_floating_tone(project):
    # No floating tone present — the ⟨⟩ matches nothing, so the rule never fires.
    surface = _derive(string_to_sequence("ta", project), project)
    assert not surface.tiers["tone"].links
