"""Tests for tier-autosegment reference parsing (``~n=value`` binds, ``~n`` recalls/spread)."""

from src.fortis.models.values import AutosegBind, AutosegRecall
from src.fortis.parsing.bundles import parse_pattern_bundle, parse_result_bundle


def test_bind_in_a_pattern(project):
    bundle = parse_pattern_bundle("+syllabic, tone: ~1=high", project.features).unwrap()
    value = bundle["tone"].value
    assert isinstance(value, AutosegBind)
    assert value.ref == 1 and value.value == 4  # 'high' is tone value 4


def test_recall_in_a_result(project):
    bundle = parse_result_bundle("tone: ~1", project.features).unwrap()
    assert bundle["tone"].value == AutosegRecall(1)


def test_recall_also_parses_in_a_pattern(project):
    bundle = parse_pattern_bundle("+syllabic, tone: ~2", project.features).unwrap()
    assert bundle["tone"].value == AutosegRecall(2)


def test_non_numeric_reference_rejected(project):
    assert parse_pattern_bundle("tone: ~x", project.features).is_err()
    assert parse_pattern_bundle("tone: ~", project.features).is_err()


def test_bind_with_an_invalid_inner_value_rejected(project):
    # ~1=nope — the bound value is parsed in pattern context and rejected.
    assert parse_pattern_bundle("tone: ~1=nope", project.features).is_err()
