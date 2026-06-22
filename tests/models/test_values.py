"""Tests for value types."""

import pytest

from src.fortis.models.values import (
    AlphaOp,
    ContourEdge,
    ContourValue,
    SingleValue,
    Value,
    form_contour,
    make_value,
)


class TestEnums:
    def test_alpha_op_values(self):
        assert AlphaOp.same == "same"
        assert AlphaOp.opposite == "opposite"
        assert AlphaOp.other == "other"

    def test_contour_edge_values(self):
        assert ContourEdge.initial == "initial"
        assert ContourEdge.final == "final"
        assert ContourEdge.any == "any"
        assert ContourEdge.all == "all"


class TestMakeValue:
    def test_single_element_tuple_returns_scalar(self):
        assert make_value((1,)) == 1

    def test_multi_element_tuple_returns_contour(self):
        result = make_value((1, 0))
        assert isinstance(result, tuple)
        assert result == (1, 0)

    def test_longer_contour(self):
        result = make_value((1, 0, 1))
        assert result == (1, 0, 1)


class TestFormContour:
    def test_two_scalars(self):
        result = form_contour(1, 0)
        assert isinstance(result, tuple)
        assert result == (1, 0)

    def test_scalar_and_contour(self):
        result = form_contour(1, (0, 1))
        assert result == (1, 0, 1)

    def test_contour_and_scalar(self):
        result = form_contour((1, 0), 1)
        assert result == (1, 0, 1)

    def test_two_contours(self):
        result = form_contour((1, 0), (1,))
        assert result == (1, 0, 1)