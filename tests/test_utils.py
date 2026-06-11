"""Tests for general utility functions."""

from src.fortis.general.utils import is_combining, safe_int


class TestSafeInt:
    def test_valid_integer(self):
        assert safe_int("42") == 42

    def test_negative_integer(self):
        assert safe_int("-7") == -7

    def test_zero(self):
        assert safe_int("0") == 0

    def test_float_string_returns_none(self):
        assert safe_int("3.14") is None

    def test_non_numeric_returns_none(self):
        assert safe_int("abc") is None

    def test_empty_string_returns_none(self):
        assert safe_int("") is None

    def test_whitespace_string_returns_none(self):
        assert safe_int("  ") is None

    def test_mixed_alphanumeric_returns_none(self):
        assert safe_int("42abc") is None


class TestIsCombining:
    def test_combining_acute(self):
        assert is_combining("́") is True  # combining acute accent

    def test_combining_grave(self):
        assert is_combining("̀") is True  # combining grave accent

    def test_regular_letter(self):
        assert is_combining("a") is False

    def test_digit(self):
        assert is_combining("5") is False

    def test_space(self):
        assert is_combining(" ") is False