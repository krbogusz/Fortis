"""Tests for tier-autosegment spread (the applier links one autosegment to many anchors)."""

from src.fortis.application.deriving import derive
from src.fortis.application.tiers import associate_tiers, lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.form import Form
from src.fortis.models.inventories import Word
from src.fortis.models.rules import ApplicationMode, Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.notation import parse_definition


def _fb(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def _rule(definition, features):
    sd = parse_definition(definition, features).unwrap()
    return Rule(id="r", time=0, raw_definition=definition, sd=sd)


def _derive(form, rule, project):
    return derive(
        Word(ipa="x"),
        form,
        RuleInventory({0: (rule,)}),
        project.letters,
        project.features,
        tiers=project.tiers,
    ).surface


def test_high_tone_spreads_as_one_autoseg(project):
    # a(H) a(toneless) → both high, sharing ONE autosegment (spread, not a copy).
    form = associate_tiers(
        Form.from_bundles([_fb(syllabic=1, tone=4), _fb(syllabic=1)]), project.tiers
    )
    rule = _rule(
        "[+syllabic, tone: ~1=high] [+syllabic, tone: none] "
        "-> [+syllabic, tone: ~1] [+syllabic, tone: ~1]",
        project.features,
    )
    surface = _derive(form, rule, project)
    tier = surface.tiers["tone"]
    assert len(tier.autosegs) == 1  # one H autosegment...
    assert tier.links == {(tier.autosegs[0].id, 0), (tier.autosegs[0].id, 1)}  # ...on both anchors
    assert [b["tone"].value for b in lower_tiers(surface)] == [4, 4]  # both read high


def test_high_spreads_across_a_consonant_via_context(project):
    # The realistic case the docs show: a vowel's tone spreads to the next syllable, over the
    # consonant between them — the source vowel sits in the left context, with [-syll]* spanning
    # the gap.
    form = associate_tiers(
        Form.from_bundles(
            [
                _fb(consonantal=1, syllabic=0),
                _fb(syllabic=1, tone=4),
                _fb(consonantal=1, syllabic=0),
                _fb(syllabic=1),
            ]
        ),
        project.tiers,
    )  # t a(H) k a — H on the first vowel only
    rule = _rule(
        "[+syllabic, tone: none] → [+syllabic, tone: ~1] "
        "/ [+syllabic, tone: ~1=high] [-syllabic]* _",
        project.features,
    )
    surface = _derive(form, rule, project)
    tier = surface.tiers["tone"]
    assert len(tier.autosegs) == 1  # still one H autosegment...
    assert tier.links == {(tier.autosegs[0].id, 1), (tier.autosegs[0].id, 3)}  # ...on both vowels
    assert [b["tone"].value if "tone" in b else None for b in lower_tiers(surface)] == [
        None,
        4,
        None,
        4,
    ]


def test_spread_propagates_across_a_run_left_to_right(project):
    # Under left_to_right, one H spreads across a whole toneless run, each step feeding the
    # next. Regression: directional mode shares source/out, which once crashed the spread
    # (a set mutated during iteration).
    form = associate_tiers(
        Form.from_bundles(
            [
                _fb(syllabic=1, tone=4),
                _fb(consonantal=1, syllabic=0),
                _fb(syllabic=1),
                _fb(consonantal=1, syllabic=0),
                _fb(syllabic=1),
            ]
        ),
        project.tiers,
    )  # a(H) k a k a — H on the first vowel only
    definition = (
        "[+syllabic, tone: none] -> [+syllabic, tone: ~1] "
        "/ [+syllabic, tone: ~1=high] [-syllabic]* _"
    )
    rule = Rule(
        id="spread",
        time=0,
        raw_definition="spread",
        sd=parse_definition(definition, project.features).unwrap(),
        application=ApplicationMode.left_to_right,
    )
    surface = derive(
        Word(ipa="akaka"),
        form,
        RuleInventory({0: (rule,)}),
        project.letters,
        project.features,
        tiers=project.tiers,
    ).surface
    tier = surface.tiers["tone"]
    assert len(tier.autosegs) == 1  # one H autosegment...
    h = tier.autosegs[0].id
    assert tier.links == {(h, 0), (h, 2), (h, 4)}  # ...spread onto all three vowels


def test_unbound_recall_is_a_no_op(project):
    # Nothing binds ~1 — the recall must be a quiet no-op, not a crash or a phantom tone.
    form = associate_tiers(Form.from_bundles([_fb(syllabic=1)]), project.tiers)
    rule = _rule("[+syllabic, tone: none] -> [+syllabic, tone: ~1]", project.features)
    surface = _derive(form, rule, project)
    assert not surface.tiers["tone"].links
