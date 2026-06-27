"""Tests for syllabification (application/syllabifying.py).

The ``sonorities`` and ``syllable_parts`` fixtures come from conftest.
"""

import pytest

from src.fortis.application.syllabifying import (
    SyllabificationError,
    consolidate_suprasegmentals,
    nuclei_by_position,
    syllabify,
)
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import SyllablePart, SyllablePartsInventory
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.values import Value
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.parsing.notation import parse_sequence


def _fb(**features: Value) -> FeatureBundle:
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


class TestNucleiByPosition:
    def test_every_position_maps_to_its_syllable_nucleus(self, features):
        # C V . C V  (two syllables); every position maps to its syllable's nucleus.
        nuc = parse_pattern_bundle("+syll", features).unwrap()
        c1, v1, c2, v2 = _stop(), _v(), _stop(), _v()
        segs = [c1, v1, c2, v2]
        nuclei = nuclei_by_position(segs, frozenset({0, 2, 4}), nuc)
        assert nuclei == [v1, v1, v2, v2]

    def test_no_nucleus_in_a_span_is_none(self, features):
        nuc = parse_pattern_bundle("+syll", features).unwrap()
        segs = [_stop(), _stop()]  # no nucleus
        assert nuclei_by_position(segs, frozenset({0, 2}), nuc) == [None, None]


class TestConsolidateSuprasegmentals:
    def test_strands_move_to_the_nucleus(self, features):
        # A syllable [u(nucleus) l(coda, with a stranded stress)] — consolidation
        # moves the stress onto the nucleus u and strips it from l.
        nuc = parse_pattern_bundle("+syll", features).unwrap()
        u = _fb(syllabic=1, consonantal=0)
        coda = _fb(consonantal=1, sonorant=1, lateral=1, stress=2)  # stranded stress
        out = consolidate_suprasegmentals([u, coda], frozenset({0, 2}), nuc, frozenset({"stress"}))
        assert out[0]["stress"].value == 2  # moved onto the nucleus
        assert "stress" not in out[1]  # stripped from the coda

    def test_no_op_when_already_on_the_nucleus(self, features):
        nuc = parse_pattern_bundle("+syll", features).unwrap()
        u = _fb(syllabic=1, consonantal=0, stress=2)
        coda = _fb(consonantal=1, sonorant=1, lateral=1)
        out = consolidate_suprasegmentals([u, coda], frozenset({0, 2}), nuc, frozenset({"stress"}))
        assert out[0]["stress"].value == 2 and "stress" not in out[1]

    def test_per_syllable_isolation(self, features):
        # Two syllables: syl 1 has a stranded stress on its coda; syl 2 carries its
        # own tone on its nucleus. Each consolidates within its own span — no merge.
        nuc = parse_pattern_bundle("+syll", features).unwrap()
        segs = [
            _stop(),                                                   # 0  syl1 onset
            _fb(syllabic=1, consonantal=0),                            # 1  syl1 nucleus
            _fb(consonantal=1, sonorant=1, lateral=1, stress=2),       # 2  syl1 coda (strand)
            _stop(),                                                   # 3  syl2 onset
            _fb(syllabic=1, consonantal=0, tone=3),                    # 4  syl2 nucleus (own tone)
        ]
        out = consolidate_suprasegmentals(
            segs, frozenset({0, 3, 5}), nuc, frozenset({"stress", "tone"})
        )
        assert out[1]["stress"].value == 2 and "stress" not in out[2]  # syl1 strand → syl1 nucleus
        assert "tone" not in out[1]  # syl 2's tone did not bleed into syl 1
        assert out[4]["tone"].value == 3 and "stress" not in out[4]  # syl 2 unchanged


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
