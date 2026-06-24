"""Tests for single-segment pattern matching (application/matching.py)."""

import pytest

from src.fortis.application.matching import (
    Match,
    SyllableView,
    _cannot_match,
    find_matches,
    pattern_matches,
)
from src.fortis.application.syllabifying import nuclei_by_position
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.inventories import Letter, LetterInventory
from src.fortis.models.specs import FeatureSpec, PatternSpec
from src.fortis.models.values import AlphaOp, AlphaRef, ContourEdge
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.parsing.notation import parse_definition


def _fb(**features: object) -> FeatureBundle:
    """Build a realized FeatureBundle from feature=value kwargs."""
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def _pb(*specs: PatternSpec) -> PatternBundle:
    """Build a PatternBundle from pattern specs."""
    return PatternBundle({s.feature: s for s in specs})


class TestPatternMatches:
    def test_subsumption_match(self):
        # Pattern mentions a subset; extra segment features are unconstrained.
        assert pattern_matches(_pb(PatternSpec("voice", 1)), _fb(voice=1, nasal=0))

    def test_value_mismatch_fails(self):
        assert not pattern_matches(_pb(PatternSpec("voice", 1)), _fb(voice=0))

    def test_absent_feature_fails_positive(self):
        assert not pattern_matches(_pb(PatternSpec("voice", 1)), _fb(nasal=0))

    def test_absent_feature_passes_negated(self):
        assert pattern_matches(_pb(PatternSpec("voice", 1, negated=True)), _fb(nasal=0))

    def test_negated_blocks_matching_value(self):
        assert not pattern_matches(_pb(PatternSpec("voice", 1, negated=True)), _fb(voice=1))

    def test_none_matches_absent_feature(self):
        # "F: none" asserts F is unspecified — satisfied by an absent feature.
        assert pattern_matches(_pb(PatternSpec("nasal", None)), _fb(voice=1))

    def test_none_fails_specified_feature(self):
        # A present feature is specified, so "F: none" does not match.
        assert not pattern_matches(_pb(PatternSpec("nasal", None)), _fb(nasal=0))

    def test_negated_none_requires_presence(self):
        # "F: !none" means F must be specified — an absent feature fails it.
        assert not pattern_matches(_pb(PatternSpec("nasal", None, negated=True)), _fb(voice=1))
        assert pattern_matches(_pb(PatternSpec("nasal", None, negated=True)), _fb(nasal=0))

    def test_contour_matches_equal_length(self):
        # A contour defaults to @all (same arity, limb for limb) — as the parser sets it.
        pat = _pb(PatternSpec("tone", (1, 2), contour_position=ContourEdge.all))
        assert pattern_matches(pat, _fb(tone=(1, 2)))

    def test_contour_length_mismatch_fails(self):
        pat = _pb(PatternSpec("tone", (1, 2), contour_position=ContourEdge.all))
        assert not pattern_matches(pat, _fb(tone=1))


class TestAlpha:
    def test_alpha_binds_then_agrees(self):
        bindings = Bindings()
        pat = _pb(PatternSpec("high", AlphaRef("α")), PatternSpec("back", AlphaRef("α")))
        # high=1 binds α to 1; back must also be 1 to agree.
        assert pattern_matches(pat, _fb(high=1, back=1), bindings)
        assert bindings.alpha["α"] == 1

    def test_alpha_disagreement_fails(self):
        bindings = Bindings()
        pat = _pb(PatternSpec("high", AlphaRef("α")), PatternSpec("back", AlphaRef("α")))
        assert not pattern_matches(pat, _fb(high=1, back=0), bindings)

    def test_alpha_in_contour_limb(self):
        bindings = Bindings()
        bindings.alpha["α"] = 2
        # tone: 2>α — first limb concrete, second recalls α (=2 here). @all alignment.
        spec = PatternSpec(
            "tone", (2, AlphaRef("α", AlphaOp.same)), contour_position=ContourEdge.all
        )
        pat = _pb(spec)
        assert pattern_matches(pat, _fb(tone=(2, 2)), bindings)
        assert not pattern_matches(pat, _fb(tone=(2, 3)), bindings)


class TestContourPosition:
    def _m(self, features, spec: str, **seg) -> bool:
        bundle = parse_pattern_bundle(spec, features).unwrap()
        return pattern_matches(bundle, _fb(**seg), Bindings())

    def test_single_value_at_named_edges(self, features):
        assert self._m(features, "tone: 5@final", tone=(1, 5))
        assert not self._m(features, "tone: 5@final", tone=(5, 1))
        assert self._m(features, "tone: 5@initial", tone=(5, 1))
        assert not self._m(features, "tone: 5@initial", tone=(1, 5))

    def test_single_value_at_numeric_position(self, features):
        # @n is 1-indexed: @2 is the second limb.
        assert self._m(features, "tone: 5@2", tone=(1, 5))
        assert not self._m(features, "tone: 5@2", tone=(5, 1))

    def test_single_value_at_multiple_positions(self, features):
        assert self._m(features, "tone: 5@2;3", tone=(1, 5, 5))
        assert not self._m(features, "tone: 5@2;3", tone=(1, 5, 1))

    def test_single_value_all(self, features):
        assert self._m(features, "tone: 5@all", tone=(5, 5))
        assert not self._m(features, "tone: 5@all", tone=(5, 1))

    def test_single_value_any_matches_contour(self, features):
        # @any is the single-value default; it matches a contour containing the value
        # (previously a length mismatch silently failed) and is unchanged for scalars.
        assert self._m(features, "+high", high=(0, 1))
        assert not self._m(features, "+high", high=(0, 0))
        assert self._m(features, "+high", high=1)

    def test_contour_initial_final_window(self, features):
        assert self._m(features, "tone: 1>2@initial", tone=(1, 2, 3))
        assert not self._m(features, "tone: 1>2@initial", tone=(3, 1, 2))
        assert self._m(features, "tone: 1>2@final", tone=(3, 1, 2))

    def test_contour_any_is_subsequence(self, features):
        assert self._m(features, "tone: 1>2@any", tone=(3, 1, 2))
        assert not self._m(features, "tone: 1>2@any", tone=(1, 3, 2))

    def test_contour_default_all_is_exact(self, features):
        assert self._m(features, "tone: 1>2", tone=(1, 2))
        assert not self._m(features, "tone: 1>2", tone=(1, 2, 3))

    def test_negated_positional(self, features):
        # !5@final → the final limb is not 5.
        assert self._m(features, "tone: !5@final", tone=(1, 3))
        assert not self._m(features, "tone: !5@final", tone=(1, 5))
        # !+F → F at no position.
        assert not self._m(features, "!+high", high=(0, 1))
        assert self._m(features, "!+high", high=(0, 0))

    def test_alpha_in_multi_limb_any_is_refused(self, features):
        bundle = parse_pattern_bundle("tone: α>2@any", features).unwrap()
        with pytest.raises(NotImplementedError):
            pattern_matches(bundle, _fb(tone=(1, 2)), Bindings())


class TestTierAwareMatching:
    def test_syllable_tier_spec_reads_the_nucleus(self, features):
        # A consonant and a tone-3 vowel forming one syllable. [+cons, tone: 3]
        # matches the consonant: +cons against the segment, tone:3 against its
        # syllable's nucleus (where suprasegmentals live).
        cons = _fb(consonantal=1)
        vowel = _fb(syllabic=1, tone=3)
        segs = [cons, vowel]
        nucleus_def = parse_pattern_bundle("+syll", features).unwrap()
        nuclei = nuclei_by_position(segs, frozenset({0, 2}), nucleus_def)
        view = SyllableView(nuclei=nuclei, features=frozenset({"tone"}))
        sd = parse_definition("[+cons, tone: 3] -> [+voice]", features).unwrap()
        assert [(m.start, m.end) for m in find_matches(sd, segs, syllables=view)] == [(0, 1)]
        # The same vowel's syllable at tone 4 → the consonant no longer matches.
        segs4 = [cons, _fb(syllabic=1, tone=4)]
        view4 = SyllableView(
            nuclei=nuclei_by_position(segs4, frozenset({0, 2}), nucleus_def),
            features=frozenset({"tone"}),
        )
        assert find_matches(sd, segs4, syllables=view4) == []
        # Without the view, tone is matched on the consonant itself (no tone) → no match.
        assert find_matches(sd, segs) == []


def _spans(matches: list[Match]) -> list[tuple[int, int]]:
    """The (start, end) spans of a list of matches."""
    return [(m.start, m.end) for m in matches]


class TestSequenceMatcher:
    def test_target_only_finds_every_locus(self, features):
        sd = parse_definition("[+nasal] -> [+voice]", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(0, 1), (2, 3)]

    def test_no_locus_when_target_absent(self, features):
        sd = parse_definition("[+nasal] -> [+voice]", features).unwrap()
        assert find_matches(sd, [_fb(voice=1), _fb(voice=1)]) == []

    def test_left_context_required(self, features):
        sd = parse_definition("[+nasal] -> [+voice] / [+voice] _", features).unwrap()
        # nasal at 1 is preceded by voice; nasal at 2 is preceded by a nasal.
        segs = [_fb(voice=1), _fb(nasal=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(1, 2)]

    def test_right_context_required(self, features):
        sd = parse_definition("[+nasal] -> [+voice] / _ [+voice]", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(0, 1)]

    def test_word_boundary_left(self, features):
        sd = parse_definition("[+nasal] -> [+voice] / # _", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(0, 1)]

    def test_word_boundary_right(self, features):
        sd = parse_definition("[+nasal] -> [+voice] / _ #", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(2, 3)]

    def test_syllable_boundary_never_matches_when_unsyllabified(self, features):
        sd = parse_definition("[+cons] -> [+voice] / $ _", features).unwrap()
        segs = [_fb(consonantal=1), _fb(consonantal=1)]
        assert find_matches(sd, segs) == []  # no boundaries supplied

    def test_syllable_boundary_left_onset(self, features):
        sd = parse_definition("[+cons] -> [+voice] / $ _", features).unwrap()
        segs = [_fb(consonantal=1), _fb(consonantal=1), _fb(consonantal=1)]
        # Onset consonants sit just after a syllable boundary.
        assert _spans(find_matches(sd, segs, boundaries=frozenset({0, 2}))) == [(0, 1), (2, 3)]

    def test_syllable_boundary_right_coda(self, features):
        sd = parse_definition("[+cons] -> [+voice] / _ $", features).unwrap()
        segs = [_fb(consonantal=1), _fb(consonantal=1), _fb(consonantal=1)]
        # A coda consonant sits just before a syllable boundary.
        assert _spans(find_matches(sd, segs, boundaries=frozenset({2}))) == [(1, 2)]

    def test_exception_blocks(self, features):
        sd = parse_definition("[+nasal] -> [+voice] // [+voice] _", features).unwrap()
        # The nasal at 1 is preceded by voice, so the exception blocks it.
        segs = [_fb(voice=1), _fb(nasal=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(2, 3)]

    def test_quantifier_greedy(self, features):
        sd = parse_definition("[+nasal]{2} -> [+voice]", features).unwrap()
        segs = [_fb(nasal=1), _fb(nasal=1), _fb(voice=1)]
        assert _spans(find_matches(sd, segs)) == [(0, 2)]

    def test_disjunction_matches_either_branch(self, features):
        sd = parse_definition("([+nasal]|[+lateral]) -> [+voice]", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1), _fb(lateral=1)]
        assert _spans(find_matches(sd, segs)) == [(0, 1), (2, 3)]

    def test_negation_matches_non_target(self, features):
        sd = parse_definition("![+nasal] -> [+voice]", features).unwrap()
        segs = [_fb(nasal=1), _fb(voice=1)]
        assert _spans(find_matches(sd, segs)) == [(1, 2)]

    def test_alpha_agreement_across_context(self, features):
        sd = parse_definition("[αhigh] -> [+voice] / [αhigh] _", features).unwrap()
        # `same` agreement is symmetric, so binding-site order is invisible here:
        # the left neighbour and target must share a high value either way.
        assert _spans(find_matches(sd, [_fb(high=1), _fb(high=1)])) == [(1, 2)]
        assert find_matches(sd, [_fb(high=0), _fb(high=1)]) == []

    def test_letter_ref_resolves_against_inventory(self, features):
        sd = parse_definition("m -> [+voice]", features).unwrap()
        m = _fb(nasal=1, labial=1)
        letters = LetterInventory({"m": Letter(symbol="m", bundle=m)})
        segs = [_fb(voice=1), m]
        assert _spans(find_matches(sd, segs, letters)) == [(1, 2)]

    def test_reference_bind_and_recall(self, features):
        sd = parse_definition("1=[+nasal] -> [+voice] / @1 _", features).unwrap()
        # @1 in the left context must be the same realized material as the target.
        # References are scope-based: the target is ref-bound first (pass 1), so a
        # recall to its left resolves even though it sits earlier in the string.
        same = _fb(nasal=1, labial=1)
        assert _spans(find_matches(sd, [same, same])) == [(1, 2)]
        # A different left neighbour does not satisfy the recall.
        other = _fb(nasal=1, labial=0)
        assert find_matches(sd, [other, same]) == []

    def test_multisegment_reference_bind_and_recall(self, features):
        # A group binding captures the whole span; @1 must match an identical copy.
        # CVCV (second CV == first) is a locus; a differing second C is not.
        sd = parse_definition("1=([+cons][+syll]) @1 -> @1", features).unwrap()
        c, v = _fb(consonantal=1, voice=1), _fb(syllabic=1, high=1)
        assert _spans(find_matches(sd, [c, v, c, v])) == [(0, 4)]
        assert find_matches(sd, [c, v, _fb(consonantal=1, voice=0), v]) == []

    def test_reference_bound_in_right_context_recalled_to_the_left(self, features):
        # A reference bound in the RIGHT context is recalled by the LEFT context — the
        # two flanks of the target must be identical. References are scope-based, so the
        # right-context binding is pre-captured and visible to the earlier recall.
        sd = parse_definition("[+cons] -> [+voice] / @1 _ 1=[+nasal]", features).unwrap()
        same, other, c = _fb(nasal=1, labial=1), _fb(nasal=1, labial=0), _fb(consonantal=1)
        assert _spans(find_matches(sd, [same, c, same])) == [(1, 2)]  # identical flanks
        assert find_matches(sd, [other, c, same]) == []  # differing flanks → no locus

    def test_target_recalling_a_right_context_binding(self, features):
        # Case B: the target IS a recall of a binding in the right context. Pass 1
        # cannot span it, so the end is enumerated and the right-context pre-seed
        # resolves the recall. @1 -> x / _ 1=[+nasal] matches the first of two
        # identical nasals; nothing when they differ, or when there is no pair.
        sd = parse_definition("@1 -> x / _ 1=[+nasal]", features).unwrap()
        same, other = _fb(nasal=1, labial=1), _fb(nasal=1, labial=0)
        assert _spans(find_matches(sd, [same, same])) == [(0, 1)]
        assert find_matches(sd, [other, same]) == []
        assert find_matches(sd, [same]) == []  # no right-context nasal to bind

    def test_reference_bound_in_right_exception_recalled_to_the_left(self, features):
        # Scope-based references hold inside the exception too: @1 in the left
        # exception recalls 1 bound in the right exception, so the rule is blocked
        # only when the locus is flanked by *identical* nasals.
        sd = parse_definition("[+cons] -> [+voice] // @1 _ 1=[+nasal]", features).unwrap()
        same, other, c = _fb(nasal=1, labial=1), _fb(nasal=1, labial=0), _fb(consonantal=1)
        assert find_matches(sd, [same, c, same]) == []  # exception holds → blocked
        assert _spans(find_matches(sd, [other, c, same])) == [(1, 2)]  # exception fails → fires


class TestBindingOrder:
    """Pin the matcher semantics: alpha is order-independent, references target-first."""

    def test_alpha_opposite_is_order_independent_disagreement(self, features):
        # α is a value-agreement variable (SPE): [αhigh] and [-αhigh] must DISAGREE,
        # regardless of which position is reached first. (The old engine read this as
        # agreement because the binder dropped its op — the bug this fix corrects.)
        ctx_left = parse_definition("[αhigh] -> [+voice] / [-αhigh] _", features).unwrap()
        # left high=0, target high=1 → disagree → match; high=1,high=1 → agree → none.
        assert _spans(find_matches(ctx_left, [_fb(high=0), _fb(high=1)])) == [(1, 2)]
        assert find_matches(ctx_left, [_fb(high=1), _fb(high=1)]) == []
        # Putting the opposite spec on the TARGET instead gives the SAME disagreement —
        # the relation is symmetric, proving order-independence.
        ctx_right = parse_definition("[-αhigh] -> [+voice] / [αhigh] _", features).unwrap()
        assert _spans(find_matches(ctx_right, [_fb(high=0), _fb(high=1)])) == [(1, 2)]
        assert find_matches(ctx_right, [_fb(high=1), _fb(high=1)]) == []

    def test_unary_opposite_is_present_absent_opposition(self, features):
        # On a unary (privative) feature, -α flips present(1) ↔ absent(none): [α manner]
        # and [-α manner] must disagree in manner presence (manner is unary here). This
        # needs α to bind/match an *absent* feature as the "none" pole.
        sd = parse_definition("[α manner] -> [+voice] / [-α manner] _", features).unwrap()
        has, lacks = _fb(manner=1), _fb(consonantal=1)
        assert _spans(find_matches(sd, [has, lacks])) == [(1, 2)]  # present vs absent → disagree
        assert find_matches(sd, [has, has]) == []  # both present → agree → no match
        assert _spans(find_matches(sd, [lacks, has])) == [(1, 2)]  # absent vs present → disagree

    def test_alpha_other_is_deferred_until_bound(self, features):
        # !α (other) is a ≠ relation that cannot bind α, so it is deferred and checked
        # once α is bound — here the binder sits to its RIGHT, yet it still resolves.
        sd = parse_definition("[!αhigh] -> [+voice] / _ [αhigh]", features).unwrap()
        assert _spans(find_matches(sd, [_fb(high=1), _fb(high=0)])) == [(0, 1)]  # differ → holds
        assert find_matches(sd, [_fb(high=0), _fb(high=0)]) == []  # equal → !α fails

    def test_pass1_is_alpha_blind_for_multi_occurrence_target(self, features):
        # Regression: a two-segment target whose FIRST alpha occurrence is non-`same`,
        # with α bound in the left context. Pass 2 honours the op against the bound
        # context (target[0] opposite → differs; target[1] same → agrees). Pass 1 must
        # be alpha-blind: were it to bind α from target[0] instead, it would impose a
        # bogus stricter constraint and miss the span entirely.
        sd = parse_definition("[-αhigh][αhigh] -> [+voice] / [αhigh] _", features).unwrap()
        # left binds α=1; target high [0, 1]: 0≠1 ✓ then 1==1 ✓.
        assert _spans(find_matches(sd, [_fb(high=1), _fb(high=0), _fb(high=1)])) == [(1, 3)]
        # left binds α=0; target high [1, 1]: 1≠0 ✓ then 1==0 ✗ → no locus.
        assert find_matches(sd, [_fb(high=0), _fb(high=1), _fb(high=1)]) == []

    def test_negated_alpha_element_defers_to_pass_two(self, features):
        # Regression: a negated element wrapping an alpha bundle. Alpha-blind pass 1
        # must defer (consume + leave the truth to pass 2), not treat the inner as a
        # guaranteed match — which would make the negation never hold and miss the span.
        sd = parse_definition("![αhigh] -> [+voice] / [αhigh] _", features).unwrap()
        # left binds α=1; target high=0 → [αhigh] fails → ![αhigh] holds.
        assert _spans(find_matches(sd, [_fb(high=1), _fb(high=0)])) == [(1, 2)]
        # left binds α=1; target high=1 → [αhigh] holds → ![αhigh] fails.
        assert find_matches(sd, [_fb(high=1), _fb(high=1)]) == []

    def test_negated_alpha_spec_defers_to_pass_two(self, features):
        # Regression: `!-α` is a negated alpha *spec* (negated=True over an opposite
        # alpha) — "not opposite", i.e. agreement. Alpha-blind pass 1 must defer the
        # whole spec; letting permissive alpha resolve it would flip under negation
        # and miss the span.
        sd = parse_definition("[!-αhigh] -> [+voice] / [αhigh] _", features).unwrap()
        # left binds α=1; target high=1 → not-opposite holds → match.
        assert _spans(find_matches(sd, [_fb(high=1), _fb(high=1)])) == [(1, 2)]
        # left binds α=1; target high=0 → opposite holds → not-opposite fails.
        assert find_matches(sd, [_fb(high=1), _fb(high=0)]) == []


class TestSequenceEdgeCases:
    def test_null_target_marks_insertion_points(self, features):
        sd = parse_definition("∅ -> [+voice] / [+nasal] _", features).unwrap()
        # A zero-width locus sits just after each nasal.
        segs = [_fb(nasal=1), _fb(voice=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(1, 1), (3, 3)]

    def test_zero_rep_quantifier(self, features):
        sd = parse_definition("[+nasal]{0,2} [+voice] -> [+lateral]", features).unwrap()
        # With no nasal present the {0,2} contributes zero reps; the voice still matches.
        assert _spans(find_matches(sd, [_fb(voice=1)])) == [(0, 1)]

    def test_right_only_exception(self, features):
        sd = parse_definition("[+nasal] -> [+voice] // _ [+lateral]", features).unwrap()
        # The nasal before the lateral is blocked; the final nasal applies.
        segs = [_fb(nasal=1), _fb(lateral=1), _fb(nasal=1)]
        assert _spans(find_matches(sd, segs)) == [(2, 3)]


class TestNecessaryConditionPruning:
    """`_cannot_match` is a conservative pre-check.

    It skips a rule the word provably cannot satisfy, and must never prune a rule
    that could still match.
    """

    def test_prunes_when_a_required_feature_is_absent(self, features):
        sd = parse_definition("[+nasal] -> [+voice]", features).unwrap()
        assert _cannot_match(sd, [_fb(consonantal=1), _fb(voice=1)], LetterInventory())
        assert not _cannot_match(sd, [_fb(nasal=1), _fb(voice=1)], LetterInventory())

    def test_charges_a_recall_for_a_second_copy(self, features):
        # 1=[+nasal] @1 needs TWO nasals — the binding and its identical recall.
        sd = parse_definition("1=[+nasal] @1 -> [+voice] @1", features).unwrap()
        n = _fb(nasal=1, labial=1)
        assert _cannot_match(sd, [n, _fb(consonantal=1)], LetterInventory())  # only one nasal
        assert not _cannot_match(sd, [n, n], LetterInventory())  # two

    def test_never_prunes_a_disjunction_branch_away(self, features):
        # ([+nasal]|[+cons]) can match via [+cons]; a nasal-less word must NOT be pruned,
        # and the locus must still be found.
        sd = parse_definition("([+nasal]|[+cons]) -> [+voice]", features).unwrap()
        segs = [_fb(consonantal=1, sonorant=0), _fb(voice=1)]
        assert not _cannot_match(sd, segs, LetterInventory())
        assert _spans(find_matches(sd, segs)) == [(0, 1)]

    def test_never_prunes_an_optional_element_away(self, features):
        # [+nasal]? imposes no requirement (min 0); a cons-only word is not pruned.
        sd = parse_definition("[+nasal]? [+cons] -> [-voice]", features).unwrap()
        assert not _cannot_match(sd, [_fb(consonantal=1, voice=1)], LetterInventory())
