"""Tests for syllabification (application/syllabifying.py).

The ``sonorities`` and ``syllable_parts`` fixtures come from conftest.
"""

import pytest

from src.fortis.application.syllabifying import (
    SyllabificationError,
    render_syllabified,
    syllabify,
)
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import (
    Letter,
    LetterInventory,
    SyllablePart,
    SyllablePartsInventory,
)
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.bundles import parse_pattern_bundle


def _fb(**features: object) -> FeatureBundle:
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


# Segment builders (rhotic needs nasal/lateral ABSENT to match its "none" predicate).
def _v():
    return _fb(syllabic=1, consonantal=0)


def _stop():
    return _fb(consonantal=1, sonorant=0)


def _lat():
    return _fb(consonantal=1, sonorant=1, lateral=1)


def _rho():
    return _fb(consonantal=1, sonorant=1)


def _nas():
    return _fb(consonantal=1, sonorant=1, nasal=1)


def _syl(segments, sonorities, syllable_parts):
    return sorted(syllabify(segments, sonorities, syllable_parts, time=0))


class TestSyllabify:
    def test_single_nucleus_marks_word_edges(self, sonorities, syllable_parts):
        assert _syl([_v()], sonorities, syllable_parts) == [0, 1]

    def test_no_nucleus_is_unsyllabifiable(self, sonorities, syllable_parts):
        assert _syl([_stop(), _stop()], sonorities, syllable_parts) == []

    def test_hiatus_boundary_between_adjacent_nuclei(self, sonorities, syllable_parts):
        assert _syl([_v(), _v()], sonorities, syllable_parts) == [0, 1, 2]

    def test_single_intervocalic_consonant_is_onset(self, sonorities, syllable_parts):
        # V C V → V.CV (maximal onset).
        assert _syl([_v(), _stop(), _v()], sonorities, syllable_parts) == [0, 1, 3]

    def test_rising_cluster_is_all_onset(self, sonorities, syllable_parts):
        # a t l a → a.tla : stop(1) < lateral(4) rises toward the nucleus.
        assert _syl([_v(), _stop(), _lat(), _v()], sonorities, syllable_parts) == [0, 1, 4]

    def test_falling_cluster_splits_to_coda(self, sonorities, syllable_parts):
        # a l t a → al.ta : lateral(4) > stop(1), so the lateral is a coda.
        assert _syl([_v(), _lat(), _stop(), _v()], sonorities, syllable_parts) == [0, 2, 4]

    def test_nasal_coda_before_stop_onset(self, sonorities, syllable_parts):
        # p l a n t a → plan.ta : nasal(3) > stop(1) splits the nt cluster.
        word = [_stop(), _lat(), _v(), _nas(), _stop(), _v()]
        assert _syl(word, sonorities, syllable_parts) == [0, 4, 6]

    def test_rhotic_maximal_onset(self, sonorities, syllable_parts):
        # a t r a → a.tra : stop(1) < rhotic(5). Confirms the "none" predicate scores
        # the rhotic (nasal/lateral absent), not the least-sonorous fallback.
        assert _syl([_v(), _stop(), _rho(), _v()], sonorities, syllable_parts) == [0, 1, 4]

    def test_no_nucleus_definition_yields_nothing(self, sonorities, features):
        empty_parts = SyllablePartsInventory()
        assert syllabify([_v()], sonorities, empty_parts, time=0) == frozenset()


class TestOnsetCodaConstraints:
    """Constraints narrow the sonority-legal splits (a stop forbidden in the onset)."""

    def _parts(self, features, **parts):
        nucleus = SyllablePart("nucleus", 0, parse_pattern_bundle("+syll", features).unwrap())
        return SyllablePartsInventory({0: {"nucleus": nucleus, **parts}})

    def _stop0(self):
        # continuant given explicitly so a "continuant: 0" predicate can match it
        return _fb(consonantal=1, sonorant=0, continuant=0)

    def _fric(self):
        return _fb(consonantal=1, sonorant=0, continuant=1)

    def test_unconstrained_split_is_maximal_onset(self, sonorities, features):
        # a S F L a (stop<fric<lat, all rising) → a.SFL.a with no constraints.
        word = [_v(), self._stop0(), self._fric(), _lat(), _v()]
        parts = self._parts(features)
        assert sorted(syllabify(word, sonorities, parts, 0)) == [0, 1, 5]

    def test_onset_forbidden_forces_a_different_split(self, sonorities, features):
        # Forbid stops (continuant:0) in the onset: the stop is pushed into the coda,
        # moving the boundary from 1 (a.SFL) to 2 (aS.FL) — a split sonority alone
        # would not pick.
        word = [_v(), self._stop0(), self._fric(), _lat(), _v()]
        forbid_stop = parse_pattern_bundle("continuant: 0", features).unwrap()
        parts = self._parts(features, onset=SyllablePart("onset", 0, forbidden=forbid_stop))
        assert sorted(syllabify(word, sonorities, parts, 0)) == [0, 2, 5]

    def test_no_legal_division_raises(self, sonorities, features):
        # Forbidding the stop in both onset and coda leaves it nowhere to go.
        word = [_v(), self._stop0(), self._fric(), _lat(), _v()]
        forbid_stop = parse_pattern_bundle("continuant: 0", features).unwrap()
        parts = self._parts(
            features,
            onset=SyllablePart("onset", 0, forbidden=forbid_stop),
            coda=SyllablePart("coda", 0, forbidden=forbid_stop),
        )
        with pytest.raises(SyllabificationError):
            syllabify(word, sonorities, parts, 0)


class TestRenderSyllabified:
    def test_boundaries_shown_as_dots(self, sonorities, syllable_parts):
        # planta → plan.ta; each segment is an exact-match letter (distinct bundles).
        p = _fb(consonantal=1, sonorant=0, labial=1)
        ll = _fb(consonantal=1, sonorant=1, lateral=1)
        a = _fb(syllabic=1, consonantal=0)
        n = _fb(consonantal=1, sonorant=1, nasal=1)
        t = _fb(consonantal=1, sonorant=0)
        letters = LetterInventory(
            {"p": Letter("p", p), "l": Letter("l", ll), "a": Letter("a", a),
             "n": Letter("n", n), "t": Letter("t", t)}
        )
        word = [p, ll, a, n, t, a]
        boundaries = syllabify(word, sonorities, syllable_parts, 0)
        assert render_syllabified(word, boundaries, letters) == "plan.ta"

    def test_unmatched_segment_is_question_mark(self):
        seg = _fb(consonantal=1)
        assert render_syllabified([seg], frozenset({0, 1}), LetterInventory()) == "?"
