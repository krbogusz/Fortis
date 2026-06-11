"""Tests for rule definition parsing."""

from src.fortis.parsing.rules import split_rule_definition


class TestSplitRuleDefinition:
    def test_full_rule(self):
        result = split_rule_definition("a -> b / c _ d // e _ f")
        assert result["target"] == "a"
        assert result["result"] == "b"
        assert result["context_left"] == "c"
        assert result["context_right"] == "d"
        assert result["exception_left"] == "e"
        assert result["exception_right"] == "f"

    def test_no_exception(self):
        result = split_rule_definition("a -> b / c _ d")
        assert result["target"] == "a"
        assert result["result"] == "b"
        assert result["context_left"] == "c"
        assert result["context_right"] == "d"
        assert "exception_left" not in result

    def test_no_context(self):
        result = split_rule_definition("a -> b")
        assert result["target"] == "a"
        assert result["result"] == "b"
        assert "context_left" not in result

    def test_unicode_arrow(self):
        result = split_rule_definition("a → b / c _ d")
        assert result["target"] == "a"
        assert result["result"] == "b"
        assert result["context_left"] == "c"

    def test_spaces_removed(self):
        result = split_rule_definition(" a  ->  b  /  c  _  d ")
        assert result["target"] == "a"
        assert result["result"] == "b"

    def test_empty_result(self):
        result = split_rule_definition("a -> b")
        assert result["target"] == "a"
        assert result["result"] == "b"
        assert len(result) == 2