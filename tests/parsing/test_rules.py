"""Tests for rule-definition parsing (``parse_definition``).

Exercises the splitting of a rule string into target / result / context /
exception. The old ``split_rule_definition`` helper returned a dict of raw
strings; that job now belongs to ``parse_definition``, which returns a
``StructuralDescription`` of parsed elements.
"""

from src.fortis.models.elements import BundleElem, LetterRef, ModifiedLetter, ResultElem
from src.fortis.parsing.notation import parse_definition


class TestModifiedLetter:
    def test_result_side(self, features):
        sd = parse_definition("ˈe -> a^[stress: none]", features).unwrap()
        (mod,) = sd.result
        assert isinstance(mod, ModifiedLetter)
        assert mod.symbol == "a"
        assert mod.delta["stress"].value is None

    def test_target_side(self, features):
        sd = parse_definition("e^[nasal: 1] -> i", features).unwrap()
        (mod,) = sd.target
        assert isinstance(mod, ModifiedLetter)
        assert mod.symbol == "e"
        assert "nasal" in mod.delta

    def test_multi_letter_run_keeps_whole_symbol_for_resolve(self, features):
        # The ^ binds the last letter, but that split needs the letter inventory, so the
        # parser keeps the whole run; resolve_rule_letters segments it later.
        sd = parse_definition("au^[nasal: 1] -> e", features).unwrap()
        assert sd.target == (ModifiedLetter(symbol="au", delta=sd.target[0].delta),)

    def test_pattern_delta_is_rejected(self, features):
        # Δ must be a realized bundle — no negation, alpha, or conditional.
        assert parse_definition("e^[!nasal] -> a", features).is_err()

    def test_caret_requires_a_following_bundle(self, features):
        assert parse_definition("e^ -> a", features).is_err()


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
        target = sd.target[0]
        result = sd.result[0]
        assert isinstance(target, BundleElem)
        assert isinstance(result, ResultElem)
        assert target.bundle["high"].condition_label == 1
        assert result.bundle["voice"].condition_label == 1
