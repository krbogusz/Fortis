"""Tests for element types."""

import pytest

from src.fortis.models.bundles import PatternBundle
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Group,
    LetterRef,
    Negated,
    Null,
    Quantified,
    Quantifier,
    RecallRef,
    ResultElem,
    SyllableBoundary,
    Wildcard,
    WordBoundary,
)
from src.fortis.models.specs import PatternSpec, ResultSpec
from src.fortis.models.bundles import ResultBundle


class TestLetterRef:
    def test_construction(self):
        ref = LetterRef(symbol="a")
        assert ref.symbol == "a"

    def test_frozen(self):
        ref = LetterRef(symbol="a")
        with pytest.raises(AttributeError):
            ref.symbol = "b"  # type: ignore[misc]


class TestBundleElem:
    def test_construction(self):
        bundle = PatternBundle(voice=PatternSpec(feature="voice", value=1))
        elem = BundleElem(bundle=bundle)
        assert elem.bundle == bundle


class TestResultElem:
    def test_construction(self):
        bundle = ResultBundle(voice=ResultSpec(feature="voice", value=1))
        elem = ResultElem(bundle=bundle)
        assert elem.bundle == bundle


class TestSingletons:
    def test_wildcard(self):
        w = Wildcard()
        assert isinstance(w, Wildcard)

    def test_word_boundary(self):
        b = WordBoundary()
        assert isinstance(b, WordBoundary)

    def test_syllable_boundary(self):
        b = SyllableBoundary()
        assert isinstance(b, SyllableBoundary)

    def test_null(self):
        n = Null()
        assert isinstance(n, Null)


class TestQuantifier:
    def test_finite(self):
        q = Quantifier(min=1, max=3)
        assert q.min == 1
        assert q.max == 3

    def test_unbounded(self):
        q = Quantifier(min=1, max=None)
        assert q.max is None

    def test_frozen(self):
        q = Quantifier(min=1, max=3)
        with pytest.raises(AttributeError):
            q.min = 2  # type: ignore[misc]


class TestGroup:
    def test_construction(self):
        inner: tuple = (LetterRef(symbol="a"), Wildcard())
        group = Group(elements=inner)
        assert len(group.elements) == 2

    def test_nested(self):
        inner = Group(elements=(LetterRef(symbol="b"),))
        outer = Group(elements=(LetterRef(symbol="a"), inner))
        assert len(outer.elements) == 2


class TestDisjunction:
    def test_construction(self):
        branch1: tuple = (LetterRef(symbol="a"),)
        branch2: tuple = (LetterRef(symbol="b"),)
        disj = Disjunction(branches=(branch1, branch2))
        assert len(disj.branches) == 2


class TestNegated:
    def test_construction(self):
        inner = LetterRef(symbol="a")
        neg = Negated(inner=inner)
        assert neg.inner == inner


class TestQuantified:
    def test_construction(self):
        inner = LetterRef(symbol="a")
        quant = Quantifier(min=1, max=3)
        q = Quantified(inner=inner, quant=quant)
        assert q.inner == inner
        assert q.quant.max == 3


class TestBound:
    def test_construction(self):
        inner = LetterRef(symbol="a")
        b = Bound(ref=0, inner=inner)
        assert b.ref == 0
        assert b.inner == inner


class TestRecallRef:
    def test_construction(self):
        r = RecallRef(ref=0)
        assert r.ref == 0