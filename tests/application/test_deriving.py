"""Tests for the derivation driver (application/deriving.py)."""

import pytest

from src.fortis.application.deriving import apply_rule, derive
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import (
    Letter,
    LetterInventory,
    SyllablePart,
    SyllablePartsInventory,
    Word,
)
from src.fortis.models.rules import ApplicationMode, Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.parsing.notation import parse_definition, parse_sequence


def _fb(**features: object) -> FeatureBundle:
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def _values(bundles) -> list[dict]:
    return [{f: s.value for f, s in b.items()} for b in bundles]


@pytest.fixture
def letters() -> LetterInventory:
    return LetterInventory(
        {"x": Letter(symbol="x", bundle=_fb(consonantal=1, voice=0))}
    )


def _rule(definition, features, mode=ApplicationMode.simultaneous, time=0):
    sd = parse_definition(definition, features).unwrap()
    return Rule(id="r", time=time, raw_definition=definition, sd=sd, application=mode)


class TestApplicationModes:
    def test_simultaneous_only_original_triggers_fire(self, features, letters):
        # Progressive voicing: a voiced segment voices a following consonant.
        # Under simultaneous, only the originally voiced seg0 triggers (seg1).
        segs = [_fb(syllabic=1, voice=1), _fb(consonantal=1, voice=0), _fb(consonantal=1, voice=0)]
        rule = _rule("[+cons] -> [+voice] / [+voice] _", features, ApplicationMode.simultaneous)
        assert _values(apply_rule(rule, segs, letters, features)) == [
            {"syllabic": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 0},
        ]

    def test_left_to_right_chains_self_feeding(self, features, letters):
        # Same rule + input, but L2R: the newly voiced seg1 feeds seg2 → all voice.
        segs = [_fb(syllabic=1, voice=1), _fb(consonantal=1, voice=0), _fb(consonantal=1, voice=0)]
        rule = _rule("[+cons] -> [+voice] / [+voice] _", features, ApplicationMode.left_to_right)
        assert _values(apply_rule(rule, segs, letters, features)) == [
            {"syllabic": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
        ]

    def test_right_to_left_chains_regressive(self, features, letters):
        # Regressive voicing: voicing spreads leftward from the voiced seg2.
        segs = [_fb(consonantal=1, voice=0), _fb(consonantal=1, voice=0), _fb(syllabic=1, voice=1)]
        rule = _rule("[+cons] -> [+voice] / _ [+voice]", features, ApplicationMode.right_to_left)
        assert _values(apply_rule(rule, segs, letters, features)) == [
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"syllabic": 1, "voice": 1},
        ]

    def test_simultaneous_two_independent_loci(self, features, letters):
        segs = [_fb(nasal=1, voice=1), _fb(nasal=1, voice=1)]
        rule = _rule("[+nasal] -> [-voice]", features, ApplicationMode.simultaneous)
        assert _values(apply_rule(rule, segs, letters, features)) == [
            {"nasal": 1, "voice": 0},
            {"nasal": 1, "voice": 0},
        ]

    def test_left_to_right_deletion_clears_all(self, features, letters):
        # A deletion shrinks the form; the narrow progress guard must not strand any.
        rule = _rule("[+cons] -> ∅", features, ApplicationMode.left_to_right)
        segs = [_fb(consonantal=1), _fb(consonantal=1), _fb(consonantal=1)]
        assert apply_rule(rule, segs, letters, features) == []

    def test_right_to_left_variable_width_picks_longest(self, features, letters):
        # `[+nasal]+ -> x` is a full-replacement result with a variable-width target.
        # R2L must pick rightmost-by-end then longest (min start), collapsing the
        # whole nasal run into a single x — not rightmost-by-start, which would peel
        # off one nasal at a time and leave several x's.
        rule = _rule("[+nasal]+ -> x", features, ApplicationMode.right_to_left)
        form = [_fb(nasal=1), _fb(nasal=1), _fb(syllabic=1)]
        assert _values(apply_rule(rule, form, letters, features)) == [
            {"consonantal": 1, "voice": 0},
            {"syllabic": 1},
        ]

    def test_apply_rule_does_not_mutate_input(self, features, letters):
        segs = [_fb(nasal=1, voice=1)]
        rule = _rule("[+nasal] -> [-voice]", features, ApplicationMode.simultaneous)
        apply_rule(rule, segs, letters, features)
        assert _values(segs) == [{"nasal": 1, "voice": 1}]


class TestDerive:
    def test_records_only_firing_steps_in_order(self, features, letters):
        word = Word(ipa="test")
        # rule A (time 0) voices the nasal; rule B (time 1) never matches (no lateral).
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        b = _rule("[+lateral] -> [+high]", features, time=1)
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, segs, rules, letters, features)
        assert len(result.steps) == 1
        assert result.steps[0].rule is a
        assert _values(result.surface) == [{"nasal": 1, "voice": 1}]
        assert _values(result.input) == [{"nasal": 1, "voice": 0}]

    def test_cross_time_feeding(self, features, letters):
        word = Word(ipa="feed")
        # A (time 0) voices the nasal; only then does B (time 1) — which targets
        # [+voice] — have anything to apply to. Order creates the feeding relation.
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        b = _rule("[+voice] -> [+high]", features, time=1)
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, segs, rules, letters, features)
        assert [s.rule for s in result.steps] == [a, b]
        assert _values(result.surface) == [{"nasal": 1, "voice": 1, "high": 1}]

    def test_non_firing_rule_threads_form_forward(self, features, letters):
        word = Word(ipa="thread")
        # B does not match, but the form it passes forward must still reach C.
        a = _rule("[+lateral] -> [+high]", features, time=0)  # never matches
        b = _rule("[+nasal] -> [+voice]", features, time=1)  # fires
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, segs, rules, letters, features)
        assert [s.rule for s in result.steps] == [b]
        assert _values(result.surface) == [{"nasal": 1, "voice": 1}]

    def test_syllable_conditioned_rule_via_full_derive(
        self, features, letters, sonorities, syllable_parts
    ):
        # apta → ap.ta (boundary at 2). A coda rule voices the consonant before a
        # syllable boundary: the p (coda) voices, the t (onset) does not. Exercises
        # syllabify → boundaries → matcher $ → derive end to end.
        word = Word(ipa="apta")
        rule = _rule("[+cons] -> [+voice] / _ $", features)
        rules = RuleInventory({0: (rule,)})
        V = _fb(syllabic=1, consonantal=0)
        p = _fb(consonantal=1, sonorant=0, voice=0)
        t = _fb(consonantal=1, sonorant=0, voice=0)
        result = derive(word, [V, p, t, V], rules, letters, features, sonorities, syllable_parts)
        assert _values(result.surface) == [
            {"syllabic": 1, "consonantal": 0},
            {"consonantal": 1, "sonorant": 0, "voice": 1},  # coda p → voiced
            {"consonantal": 1, "sonorant": 0, "voice": 0},  # onset t → unchanged
            {"syllabic": 1, "consonantal": 0},
        ]
        # The surface syllable structure (ap.ta) is carried for output.
        assert result.surface_boundaries == frozenset({0, 2, 4})

    def test_syllabification_is_inert_for_rules_without_boundary(
        self, features, letters, sonorities, syllable_parts
    ):
        # A rule set that never uses $ must derive identically with or without
        # syllabification supplied — syllabification only enables $, it never
        # perturbs unrelated derivations.
        word = Word(ipa="amna")
        rule = _rule("[+nasal] -> [+voice]", features)
        rules = RuleInventory({0: (rule,)})
        segs = [_fb(syllabic=1, consonantal=0), _fb(nasal=1, voice=0), _fb(syllabic=1)]
        without = derive(word, segs, rules, letters, features)
        with_syll = derive(word, segs, rules, letters, features, sonorities, syllable_parts)
        assert _values(with_syll.surface) == _values(without.surface)

    def test_boundary_free_rule_does_not_abort_on_unsyllabifiable_form(
        self, features, letters, sonorities
    ):
        # Onset and coda must each be a vowel → an intervocalic consonant can be
        # neither, so the form is unsyllabifiable. A $-free rule must not syllabify
        # at all, so it cannot abort on it.
        nucleus = SyllablePart("nucleus", 0, parse_pattern_bundle("+syll", features).unwrap())
        vowel_only = parse_sequence("[+syllabic]", features).unwrap()
        parts = SyllablePartsInventory(
            {
                0: {
                    "nucleus": nucleus,
                    "onset": SyllablePart("onset", 0, pattern=vowel_only),
                    "coda": SyllablePart("coda", 0, pattern=vowel_only),
                }
            }
        )
        rule = _rule("[+nasal] -> [+voice]", features)  # does not use $
        rules = RuleInventory({0: (rule,)})
        segs = [_fb(syllabic=1, consonantal=0), _fb(nasal=1, voice=0), _fb(syllabic=1)]
        result = derive(Word(ipa="ana"), segs, rules, letters, features, sonorities, parts)
        assert _values(result.surface)[1]["voice"] == 1  # rule fired, no abort
        assert result.surface_boundaries == frozenset()  # surface unsyllabifiable → no structure

    def test_input_snapshot_unchanged_by_derivation(self, features, letters):
        word = Word(ipa="snap")
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        rules = RuleInventory({0: (a,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, segs, rules, letters, features)
        assert _values(result.input) == [{"nasal": 1, "voice": 0}]
        assert _values(result.surface) == [{"nasal": 1, "voice": 1}]
