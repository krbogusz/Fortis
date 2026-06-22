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
from src.fortis.parsing.notation import parse_sequence


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
    """Onset/coda patterns define legality and override the sonority division."""

    def _parts(self, features, onset=None, coda=None):
        nucleus = SyllablePart("nucleus", 0, parse_pattern_bundle("+syll", features).unwrap())
        parts = {"nucleus": nucleus}
        if onset is not None:
            seq = parse_sequence(onset, features).unwrap()
            parts["onset"] = SyllablePart("onset", 0, pattern=seq)
        if coda is not None:
            seq = parse_sequence(coda, features).unwrap()
            parts["coda"] = SyllablePart("coda", 0, pattern=seq)
        return SyllablePartsInventory({0: parts})

    def _stop(self):
        return _fb(consonantal=1, sonorant=0)

    def _fric(self):
        return _fb(consonantal=1, sonorant=0, continuant=1)

    def test_unconstrained_split_is_maximal_onset(self, sonorities, features):
        # a S F a (stop<fric, rising) → a.SF.a (maximal onset) with no pattern.
        word = [_v(), self._stop(), self._fric(), _v()]
        assert sorted(syllabify(word, sonorities, self._parts(features), 0)) == [0, 1, 4]

    def test_onset_pattern_forces_a_different_split(self, sonorities, features):
        # An onset of exactly one segment ("[]") overrides sonority: the stop, which
        # MOP would put in the onset (a.SF), is pushed to the coda (aS.F).
        word = [_v(), self._stop(), self._fric(), _v()]
        parts = self._parts(features, onset="[]")
        assert sorted(syllabify(word, sonorities, parts, 0)) == [0, 2, 4]

    def test_non_sonority_rising_onset_is_licensed(self, sonorities, features):
        # s+stop is sonority-FALLING (fric 2 > stop 1); MOP would split it (aF.Sa),
        # but an onset pattern that allows it keeps both in the onset (a.FSa).
        word = [_v(), self._fric(), self._stop(), _v()]
        parts = self._parts(features, onset="[+cons][+cons]")
        assert sorted(syllabify(word, sonorities, parts, 0)) == [0, 1, 4]

    def test_no_legal_division_raises(self, sonorities, features):
        # Onset and coda must each be exactly one segment, but the cluster has three.
        word = [_v(), self._stop(), self._fric(), _lat(), _v()]
        parts = self._parts(features, onset="[]", coda="[]")
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
