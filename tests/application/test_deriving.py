"""Tests for the derivation driver (application/deriving.py)."""

import pytest

from src.fortis.application.deriving import (
    apply_rule,
    derive,
    derive_all,
    derive_all_parallel,
    resolve_rule_letters,
)
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import associate_tiers, lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.elements import LetterBundle
from src.fortis.models.form import Form
from src.fortis.models.inventories import (
    Letter,
    LetterInventory,
    SyllablePart,
    SyllablePartsInventory,
    Word,
)
from src.fortis.models.rules import ApplicationMode, Rule, RuleInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.values import Value
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.parsing.notation import parse_definition, parse_sequence


def _word(ipa: str) -> Word:
    """A seed-only word: the id is the IPA, and there are no targets."""
    return Word.from_series(id=ipa, seed=ipa)


def _fb(**features: Value) -> FeatureBundle:
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
        assert _values(apply_rule(rule, Form.from_bundles(segs), letters, features).bundles()) == [
            {"syllabic": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 0},
        ]

    def test_left_to_right_chains_self_feeding(self, features, letters):
        # Same rule + input, but L2R: the newly voiced seg1 feeds seg2 → all voice.
        segs = [_fb(syllabic=1, voice=1), _fb(consonantal=1, voice=0), _fb(consonantal=1, voice=0)]
        rule = _rule("[+cons] -> [+voice] / [+voice] _", features, ApplicationMode.left_to_right)
        assert _values(apply_rule(rule, Form.from_bundles(segs), letters, features).bundles()) == [
            {"syllabic": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
        ]

    def test_right_to_left_chains_regressive(self, features, letters):
        # Regressive voicing: voicing spreads leftward from the voiced seg2.
        segs = [_fb(consonantal=1, voice=0), _fb(consonantal=1, voice=0), _fb(syllabic=1, voice=1)]
        rule = _rule("[+cons] -> [+voice] / _ [+voice]", features, ApplicationMode.right_to_left)
        assert _values(apply_rule(rule, Form.from_bundles(segs), letters, features).bundles()) == [
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"syllabic": 1, "voice": 1},
        ]

    def test_simultaneous_two_independent_loci(self, features, letters):
        segs = [_fb(nasal=1, voice=1), _fb(nasal=1, voice=1)]
        rule = _rule("[+nasal] -> [-voice]", features, ApplicationMode.simultaneous)
        assert _values(apply_rule(rule, Form.from_bundles(segs), letters, features).bundles()) == [
            {"nasal": 1, "voice": 0},
            {"nasal": 1, "voice": 0},
        ]

    def test_left_to_right_deletion_clears_all(self, features, letters):
        # A deletion shrinks the form; the narrow progress guard must not strand any.
        rule = _rule("[+cons] -> ∅", features, ApplicationMode.left_to_right)
        segs = [_fb(consonantal=1), _fb(consonantal=1), _fb(consonantal=1)]
        assert apply_rule(rule, Form.from_bundles(segs), letters, features).bundles() == []

    def test_right_to_left_variable_width_picks_longest(self, features, letters):
        # `[+nasal]+ -> x` is a full-replacement result with a variable-width target.
        # R2L must pick rightmost-by-end then longest (min start), collapsing the
        # whole nasal run into a single x — not rightmost-by-start, which would peel
        # off one nasal at a time and leave several x's.
        rule = _rule("[+nasal]+ -> x", features, ApplicationMode.right_to_left)
        form = [_fb(nasal=1), _fb(nasal=1), _fb(syllabic=1)]
        assert _values(apply_rule(rule, Form.from_bundles(form), letters, features).bundles()) == [
            {"consonantal": 1, "voice": 0},
            {"syllabic": 1},
        ]

    def test_apply_rule_does_not_mutate_input(self, features, letters):
        form = Form.from_bundles([_fb(nasal=1, voice=1)])
        rule = _rule("[+nasal] -> [-voice]", features, ApplicationMode.simultaneous)
        apply_rule(rule, form, letters, features)
        assert _values(form.bundles()) == [{"nasal": 1, "voice": 1}]  # input form unchanged


class TestDerive:
    def test_records_only_firing_steps_in_order(self, features, letters):
        word = _word("test")
        # rule A (time 0) voices the nasal; rule B (time 1) never matches (no lateral).
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        b = _rule("[+lateral] -> [+high]", features, time=1)
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, Form.from_bundles(segs), rules, letters, features)
        assert len(result.steps) == 1
        assert result.steps[0].rule is a
        assert _values(result.surface.bundles()) == [{"nasal": 1, "voice": 1}]
        assert _values(result.input.bundles()) == [{"nasal": 1, "voice": 0}]

    def test_cross_time_feeding(self, features, letters):
        word = _word("feed")
        # A (time 0) voices the nasal; only then does B (time 1) — which targets
        # [+voice] — have anything to apply to. Order creates the feeding relation.
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        b = _rule("[+voice] -> [+high]", features, time=1)
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, Form.from_bundles(segs), rules, letters, features)
        assert [s.rule for s in result.steps] == [a, b]
        assert _values(result.surface.bundles()) == [{"nasal": 1, "voice": 1, "high": 1}]

    def test_non_firing_rule_threads_form_forward(self, features, letters):
        word = _word("thread")
        # B does not match, but the form it passes forward must still reach C.
        a = _rule("[+lateral] -> [+high]", features, time=0)  # never matches
        b = _rule("[+nasal] -> [+voice]", features, time=1)  # fires
        rules = RuleInventory({0: (a,), 1: (b,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, Form.from_bundles(segs), rules, letters, features)
        assert [s.rule for s in result.steps] == [b]
        assert _values(result.surface.bundles()) == [{"nasal": 1, "voice": 1}]

    def test_syllable_conditioned_rule_via_full_derive(
        self, features, letters, sonorities, syllable_parts
    ):
        # apta → ap.ta (boundary at 2). A coda rule voices the consonant before a
        # syllable boundary: the p (coda) voices, the t (onset) does not. Exercises
        # syllabify → boundaries → matcher $ → derive end to end.
        word = _word("apta")
        rule = _rule("[+cons] -> [+voice] / _ $", features)
        rules = RuleInventory({0: (rule,)})
        V = _fb(syllabic=1, consonantal=0)
        p = _fb(consonantal=1, sonorant=0, voice=0)
        t = _fb(consonantal=1, sonorant=0, voice=0)
        result = derive(
            word, Form.from_bundles([V, p, t, V]), rules, letters, features, sonorities,
            syllable_parts,
        )
        assert _values(result.surface.bundles()) == [
            {"syllabic": 1, "consonantal": 0},
            {"consonantal": 1, "sonorant": 0, "voice": 1},  # coda p → voiced
            {"consonantal": 1, "sonorant": 0, "voice": 0},  # onset t → unchanged
            {"syllabic": 1, "consonantal": 0},
        ]
        # The surface syllable structure (ap.ta) is carried for output.
        assert result.surface_boundaries == frozenset({0, 2, 4})
        # Each firing step also carries the structure of its before/after forms,
        # for a syllabified trace.
        assert result.steps[0].before_boundaries == frozenset({0, 2, 4})
        assert result.steps[0].after_boundaries == frozenset({0, 2, 4})

    def test_step_boundaries_populated_for_boundary_free_rule(
        self, features, letters, sonorities, syllable_parts
    ):
        # Per-step structure is display-only, so it appears even when the rule does
        # not use $ (the matcher gate does not suppress it).
        word = _word("apa")
        rule = _rule("[+cons] -> [+voice]", features)  # no $
        rules = RuleInventory({0: (rule,)})
        segs = [_fb(syllabic=1, consonantal=0), _fb(consonantal=1, sonorant=0, voice=0),
                _fb(syllabic=1, consonantal=0)]
        result = derive(
            word, Form.from_bundles(segs), rules, letters, features, sonorities, syllable_parts
        )
        assert result.steps[0].after_boundaries == frozenset({0, 1, 3})  # a.pa

    def test_syllabification_is_inert_for_rules_without_boundary(
        self, features, letters, sonorities, syllable_parts
    ):
        # A rule set that never uses $ must derive identically with or without
        # syllabification supplied — syllabification only enables $, it never
        # perturbs unrelated derivations.
        word = _word("amna")
        rule = _rule("[+nasal] -> [+voice]", features)
        rules = RuleInventory({0: (rule,)})
        segs = [_fb(syllabic=1, consonantal=0), _fb(nasal=1, voice=0), _fb(syllabic=1)]
        without = derive(word, Form.from_bundles(segs), rules, letters, features)
        with_syll = derive(
            word, Form.from_bundles(segs), rules, letters, features, sonorities, syllable_parts
        )
        assert _values(with_syll.surface.bundles()) == _values(without.surface.bundles())

    def test_unpatternable_form_falls_back_to_sonority(self, features, letters, sonorities):
        # Onset and coda must each be a vowel → an intervocalic consonant can be neither,
        # so no pattern-legal split exists. Rather than yield no structure, the form falls
        # back to the sonority division, and a $-free rule fires as usual.
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
        result = derive(
            _word("ana"), Form.from_bundles(segs), rules, letters, features, sonorities, parts
        )
        assert _values(result.surface.bundles())[1]["voice"] == 1  # rule fired
        # Sonority fallback: the lone medial consonant is the onset of the 2nd syllable (a.na).
        assert result.surface_boundaries == frozenset({0, 1, 3})

    def test_tier_aware_match_reads_the_syllable_end_to_end(
        self, features, letters, sonorities, syllable_parts
    ):
        # [+cons, tone: 3] voices a consonant *in a tone-3 syllable*: +cons on the
        # consonant, tone:3 on its syllable's nucleus. The driver builds the view
        # because the rule mentions a syllable-tier feature.
        rule = _rule("[+cons, tone: 3] -> [+voice]", features)
        rules = RuleInventory({0: (rule,)})
        cons = _fb(consonantal=1, sonorant=0, voice=0)
        vowel = _fb(syllabic=1, consonantal=0, tone=3)
        result = derive(
            _word("CV"), Form.from_bundles([cons, vowel]), rules, letters, features,
            sonorities, syllable_parts
        )
        assert _values(result.surface.bundles())[0]["voice"] == 1  # voiced via its syllable's tone
        # The same consonant in a tone-4 syllable is left alone.
        vowel4 = _fb(syllabic=1, consonantal=0, tone=4)
        result4 = derive(
            _word("CV"), Form.from_bundles([cons, vowel4]), rules, letters, features,
            sonorities, syllable_parts
        )
        assert _values(result4.surface.bundles())[0]["voice"] == 0

    def test_syllable_tier_write_to_nucleus(self, features, letters, sonorities, syllable_parts):
        # Writing a syllable-tier feature whose target is the nucleus works (in-span merge).
        rule = _rule("[+syll] -> [tone: 3]", features)
        rules = RuleInventory({0: (rule,)})
        result = derive(_word("a"), Form.from_bundles([_fb(syllabic=1, consonantal=0)]), rules,
                        letters, features, sonorities, syllable_parts)
        assert _values(result.surface.bundles())[0]["tone"] == 3

    def test_syllable_tier_write_to_nonnucleus_redocks_to_the_nucleus(
        self, features, letters, sonorities, syllable_parts, tiers
    ):
        # Writing tone to a consonant (not its syllable's nucleus) no longer refuses:
        # the write goes to the tier and redocks onto the syllable's nucleus. (Before
        # the flip this raised; now suprasegmentals are autosegmental.)
        rule = _rule("[+cons] -> [tone: 3]", features)
        rules = RuleInventory({0: (rule,)})
        segs = [_fb(consonantal=1, sonorant=0), _fb(syllabic=1, consonantal=0)]
        result = derive(
            _word("CV"), Form.from_bundles(segs), rules, letters, features, sonorities,
            syllable_parts, tiers,
        )
        surface = lower_tiers(result.surface)
        assert "tone" not in surface[0]  # the consonant does not bear the tone
        assert surface[1]["tone"].value == 3  # it redocked onto the syllable's nucleus

    def test_redock_follows_an_epenthesis_nucleus_shift(
        self, features, letters, sonorities, syllable_parts, tiers
    ):
        # l̩(stress) → V + l (epenthesis inserts a vowel and desyllabifies the
        # sonorant): the stress strands on l, then resyllabification redocks it onto
        # the new vowel nucleus (the autosegmental analogue of the old consolidate).
        rule = _rule("∅ [+cons, +syll] → [+syll, high: 1] [-syll]", features)
        rules = RuleInventory({0: (rule,)})
        stressed_l = _fb(consonantal=1, sonorant=1, lateral=1, syllabic=1, stress=2)
        # Lift the lexical stress onto its tier first, so its link pre-exists on l and
        # redock can relocate it (the rule leaves stress' value unchanged, so the write
        # path is not what carries it across).
        form = associate_tiers(Form.from_bundles([stressed_l]), tiers)
        result = derive(
            _word("l̩"), form, rules, letters, features, sonorities, syllable_parts, tiers,
        )
        surface = lower_tiers(result.surface)
        nuclei = [s for s in surface if s.get("syllabic") and s["syllabic"].value == 1]
        assert nuclei and nuclei[0]["stress"].value == 2  # stress on the new nucleus u
        others = [s for s in surface if not (s.get("syllabic") and s["syllabic"].value == 1)]
        assert all("stress" not in s for s in others)  # no longer stranded on l

    def test_input_snapshot_unchanged_by_derivation(self, features, letters):
        word = _word("snap")
        a = _rule("[+nasal] -> [+voice]", features, time=0)
        rules = RuleInventory({0: (a,)})
        segs = [_fb(nasal=1, voice=0)]
        result = derive(word, Form.from_bundles(segs), rules, letters, features)
        assert _values(result.input.bundles()) == [{"nasal": 1, "voice": 0}]
        assert _values(result.surface.bundles()) == [{"nasal": 1, "voice": 1}]


class TestResolveRuleLetters:
    """A letter+diacritic run a rule writes is resolved into per-segment bundles."""

    def _cowgill(self, project):
        return RuleInventory({0: (_rule("ʁʷ → g / [+son] _ w", project.features),)})

    def test_complex_symbol_resolves_to_one_letterbundle(self, project):
        # ʁʷ (ʁ + labialisation) is not a plain letter; it resolves to a single
        # LetterBundle carrying that segment's features.
        resolved = resolve_rule_letters(self._cowgill(project), project)
        assert resolved[0][0].sd.target == (
            LetterBundle(bundle=string_to_sequence("ʁʷ", project).bundles()[0]),
        )

    def test_multisegment_run_resolves_to_several_bundles(self, project):
        # A run that spells two segments (au) becomes two LetterBundles — like
        # segmenting an IPA string, not a single nonexistent letter.
        rules = RuleInventory({0: (_rule("au → o", project.features),)})
        target = resolve_rule_letters(rules, project)[0][0].sd.target
        assert target == tuple(
            LetterBundle(bundle=s) for s in string_to_sequence("au", project).bundles()
        )
        assert len(target) == 2

    def test_resolved_rule_fires_where_bare_does_not(self, project):
        rules = self._cowgill(project)
        seq = string_to_sequence("gʷiʁʷwos", project)
        # The unresolved LetterRef('ʁʷ') matches nothing.
        bare = derive(_word("gʷiʁʷwos"), seq, rules, project.letters, project.features)
        assert bare.steps == ()
        # After resolution, Cowgill's law fires: ʁʷ → g.
        resolved = resolve_rule_letters(rules, project)
        fired = derive(_word("gʷiʁʷwos"), seq, resolved, project.letters, project.features)
        assert [step.rule.id for step in fired.steps] == ["r"]

    def test_multisegment_run_fires_and_collapses_the_span(self, project):
        # The two-segment run 'au' matches two consecutive segments and collapses to
        # one: kaut → kot (the whole point of "like parsing IPA strings").
        bare = RuleInventory({0: (_rule("au → o", project.features),)})
        rules = resolve_rule_letters(bare, project)
        seq = string_to_sequence("kaut", project)
        d = derive(_word("kaut"), seq, rules, project.letters, project.features)
        assert [step.rule.id for step in d.steps] == ["r"]
        assert len(d.surface.bundles()) == 3  # k a u t (4) → k o t (3)
        assert d.surface.bundles()[1] == project.letters["o"].bundle


def test_word_scoped_rule_fires_only_on_named_words(project):
    # A rule with a non-empty `words` list fires only on words it names — by ipa or gloss.
    sd = parse_definition("a → e", project.features).unwrap()
    scoped = Rule(id="r", time=0, raw_definition="a → e", sd=sd, words=("kata",))
    inv = RuleInventory({0: (scoped,)})

    def fired(ipa, gloss=""):
        d = derive(
            Word.from_series(id=ipa, seed=ipa, gloss=gloss),
            string_to_sequence(ipa, project),
            inv,
            project.letters,
            project.features,
            project.sonorities,
            project.syllable_parts,
            project.tiers,
        )
        return [step.rule.id for step in d.steps] == ["r"]

    assert fired("kata")  # named by ipa → fires
    assert not fired("taka")  # neither ipa nor gloss named → skipped
    assert fired("taka", gloss="kata")  # named by gloss → fires


def test_derive_all_parallel_matches_serial(project):
    # Forcing the process-pool path (min_words=0) on the small default lexicon must
    # reproduce the serial derivation exactly, in the same order.
    serial = derive_all(project)
    parallel = derive_all_parallel(project, workers=2, min_words=0)
    assert len(parallel) == len(serial)
    assert [d.surface for d in parallel] == [d.surface for d in serial]
    assert [len(d.steps) for d in parallel] == [len(d.steps) for d in serial]


def test_derive_all_parallel_falls_back_below_threshold(project):
    # Below the word-count floor, or with a single worker, it runs serially — same
    # result, no pool spun up.
    serial_surfaces = [d.surface for d in derive_all(project)]
    assert [d.surface for d in derive_all_parallel(project, min_words=10_000)] == serial_surfaces
    assert [d.surface for d in derive_all_parallel(project, workers=1)] == serial_surfaces
