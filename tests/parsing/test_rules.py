"""Tests for rule-definition parsing (``parse_definition``).

Exercises the splitting of a rule string into target / result / context /
exception. The old ``split_rule_definition`` helper returned a dict of raw
strings; that job now belongs to ``parse_definition``, which returns a
``StructuralDescription`` of parsed elements.
"""

from src.fortis.models.elements import LetterRef
from src.fortis.parsing.notation import parse_definition


class TestParseDefinition:
    def test_full_rule(self, features):
        sd = parse_definition("a -> b / c _ d // e _ f", features).unwrap()
        assert sd.target == (LetterRef(symbol="a"),)
        assert sd.result == (LetterRef(symbol="b"),)
        assert sd.left_context == (LetterRef(symbol="c"),)
        assert sd.right_context == (LetterRef(symbol="d"),)
        assert sd.left_exception == (LetterRef(symbol="e"),)
        assert sd.right_exception == (LetterRef(symbol="f"),)

    def test_no_exception(self, features):
        sd = parse_definition("a -> b / c _ d", features).unwrap()
        assert sd.target == (LetterRef(symbol="a"),)
        assert sd.result == (LetterRef(symbol="b"),)
        assert sd.left_context == (LetterRef(symbol="c"),)
        assert sd.right_context == (LetterRef(symbol="d"),)
        assert sd.left_exception == ()
        assert sd.right_exception == ()

    def test_no_context(self, features):
        sd = parse_definition("a -> b", features).unwrap()
        assert sd.target == (LetterRef(symbol="a"),)
        assert sd.result == (LetterRef(symbol="b"),)
        assert sd.left_context == ()
        assert sd.right_context == ()
        assert sd.left_exception == ()
        assert sd.right_exception == ()

    def test_unicode_arrow(self, features):
        sd = parse_definition("a → b / c _ d", features).unwrap()
        assert sd.target == (LetterRef(symbol="a"),)
        assert sd.result == (LetterRef(symbol="b"),)
        assert sd.left_context == (LetterRef(symbol="c"),)

    def test_extra_whitespace_ignored(self, features):
        sd = parse_definition(" a  ->  b  /  c  _  d ", features).unwrap()
        assert sd.target == (LetterRef(symbol="a"),)
        assert sd.result == (LetterRef(symbol="b"),)
        assert sd.left_context == (LetterRef(symbol="c"),)
        assert sd.right_context == (LetterRef(symbol="d"),)

    def test_conditional_features_round_trip(self, features):
        # A '<n: F>' conditional in target and result carries its label through.
        sd = parse_definition("[<1: +high>] → [<1: +voice>] / a _", features).unwrap()
        assert sd.target[0].bundle["high"].condition_label == 1
        assert sd.result[0].bundle["voice"].condition_label == 1
