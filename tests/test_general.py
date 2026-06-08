"""Tests for src.fortis.result, src.fortis.general.utils, src.fortis.general.presentation."""

from __future__ import annotations

import pytest

from src.fortis.general.presentation import format_feature, present_symbol, present_value
from src.fortis.general.utils import is_combining, safe_int
from src.fortis.result import Err, Ok, ResultError, present_errors

# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


class TestOk:
    def test_is_ok(self):
        assert Ok(42).is_ok() is True

    def test_is_err(self):
        assert Ok(42).is_err() is False

    def test_unwrap(self):
        assert Ok(42).unwrap() == 42

    def test_unwrap_err_raises(self):
        with pytest.raises(ResultError, match="Called unwrap_err"):
            Ok(42).unwrap_err()

    def test_unwrap_or_returns_value(self):
        assert Ok(42).unwrap_or(0) == 42


class TestErr:
    def test_is_ok(self):
        assert Err("fail").is_ok() is False

    def test_is_err(self):
        assert Err("fail").is_err() is True

    def test_unwrap_raises(self):
        with pytest.raises(ResultError, match="Called unwrap"):
            Err("fail").unwrap()

    def test_unwrap_err(self):
        assert Err("fail").unwrap_err() == "fail"

    def test_unwrap_or_returns_default(self):
        assert Err("fail").unwrap_or(99) == 99


class TestPresentErrors:
    def test_string_passthrough(self):
        assert present_errors("single error") == "single error"

    def test_list_joined(self):
        assert present_errors(["a", "b", "c"]) == "a\nb\nc"


# ---------------------------------------------------------------------------
# Utils
# ---------------------------------------------------------------------------


class TestSafeInt:
    def test_valid_integer(self):
        assert safe_int("42") == 42

    def test_negative(self):
        assert safe_int("-3") == -3

    def test_zero(self):
        assert safe_int("0") == 0

    def test_non_numeric(self):
        assert safe_int("abc") is None

    def test_float_string(self):
        assert safe_int("3.14") is None

    def test_empty(self):
        assert safe_int("") is None


class TestIsCombining:
    def test_combining_accent(self):
        assert is_combining("́") is True  # combining acute

    def test_regular_letter(self):
        assert is_combining("a") is False

    def test_digit(self):
        assert is_combining("1") is False

    def test_space(self):
        assert is_combining(" ") is False


# ---------------------------------------------------------------------------
# Presentation
# ---------------------------------------------------------------------------


class TestPresentSymbol:
    def test_regular_char(self):
        assert present_symbol("a") == "a"

    def test_combining_gets_dotted_circle(self):
        assert present_symbol("́") == "◌́"

    def test_multi_char_symbol(self):
        assert present_symbol("ts") == "ts"


class TestPresentValue:
    def test_none(self):
        assert present_value(None) == "∅"

    def test_plus(self):
        assert present_value(1) == "+"

    def test_minus(self):
        assert present_value(0) == "-"

    def test_scalar(self):
        assert present_value(3) == "3"

    def test_negative(self):
        assert present_value(-1) == "-1"


class TestFormatFeature:
    def test_unary_present(self):
        assert format_feature("nas", "unary", 1) == "nas"

    def test_binary_present(self):
        assert format_feature("cons", "binary", 1) == "cons: +"

    def test_binary_absent(self):
        assert format_feature("cons", "binary", 0) == "cons: -"

    def test_binary_none(self):
        assert format_feature("cons", "binary", None) == "cons: ∅"

    def test_scalar(self):
        assert format_feature("hgt", "scalar", 3) == "hgt: 3"

    def test_scalar_none(self):
        assert format_feature("hgt", "scalar", None) == "hgt: ∅"

    def test_binary_contour(self):
        assert format_feature("cons", "binary", [1, 0]) == "cons: +>-"

    def test_unary_contour(self):
        assert format_feature("nas", "unary", [1, None]) == "nas: +>∅"

    def test_scalar_contour(self):
        assert format_feature("hgt", "scalar", [3, 1]) == "hgt: 3>+"
