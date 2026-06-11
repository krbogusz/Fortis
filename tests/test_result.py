"""Tests for the Result type."""

import pytest

from src.fortis.result import Err, Ok, ResultError, present_errors


class TestOk:
    def test_construction(self):
        ok = Ok(42)
        assert ok.value == 42

    def test_is_ok(self):
        assert Ok(1).is_ok()
        assert not Ok(1).is_err()

    def test_unwrap(self):
        assert Ok("hello").unwrap() == "hello"

    def test_unwrap_err_raises(self):
        with pytest.raises(ResultError):
            Ok(1).unwrap_err()

    def test_unwrap_or(self):
        assert Ok(5).unwrap_or(99) == 5

    def test_unwrap_or_else(self):
        assert Ok(5).unwrap_or_else(lambda e: 99) == 5

    def test_expect(self):
        assert Ok(10).expect("should be ok") == 10

    def test_map(self):
        assert Ok(3).map(lambda x: x * 2) == Ok(6)

    def test_map_err(self):
        ok = Ok(3)
        assert ok.map_err(lambda e: f"err: {e}") == Ok(3)

    def test_and_then(self):
        assert Ok(3).and_then(lambda x: Ok(x + 1)) == Ok(4)
        assert Ok(3).and_then(lambda x: Err("fail")) == Err("fail")

    def test_or_else(self):
        assert Ok(3).or_else(lambda e: Ok(0)) == Ok(3)

    def test_frozen(self):
        ok = Ok(1)
        with pytest.raises(AttributeError):
            ok.value = 2  # type: ignore[misc]


class TestErr:
    def test_construction(self):
        err = Err("oops")
        assert err.error == "oops"

    def test_is_err(self):
        assert Err("x").is_err()
        assert not Err("x").is_ok()

    def test_unwrap_raises(self):
        with pytest.raises(ResultError):
            Err("bad").unwrap()

    def test_unwrap_err(self):
        assert Err("bad").unwrap_err() == "bad"

    def test_unwrap_or(self):
        assert Err("bad").unwrap_or(99) == 99

    def test_unwrap_or_else(self):
        assert Err("bad").unwrap_or_else(lambda e: e.upper()) == "BAD"

    def test_expect_raises(self):
        with pytest.raises(ResultError):
            Err("bad").expect("expected ok")

    def test_map(self):
        assert Err("bad").map(lambda x: x * 2) == Err("bad")

    def test_map_err(self):
        assert Err("bad").map_err(lambda e: e.upper()) == Err("BAD")

    def test_and_then(self):
        assert Err("bad").and_then(lambda x: Ok(x + 1)) == Err("bad")

    def test_or_else(self):
        assert Err("bad").or_else(lambda e: Ok(0)) == Ok(0)
        assert Err("bad").or_else(lambda e: Err(e.upper())) == Err("BAD")

    def test_frozen(self):
        err = Err("x")
        with pytest.raises(AttributeError):
            err.error = "y"  # type: ignore[misc]


class TestPresentErrors:
    def test_string_passthrough(self):
        assert present_errors("single error") == "single error"

    def test_list_joined(self):
        assert present_errors(["a", "b", "c"]) == "a\nb\nc"

    def test_empty_list(self):
        assert present_errors([]) == ""