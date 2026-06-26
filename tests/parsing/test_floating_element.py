"""Tests for the floating-autosegment notation ``⟨...⟩`` (parsing)."""

from src.fortis.models.elements import FloatingAutoseg
from src.fortis.models.values import AutosegBind
from src.fortis.parsing.notation import parse_definition
from src.fortis.parsing.rule_validation import validate_structural_description


def test_floating_element_parses_as_floating_autoseg(project):
    sd = parse_definition(
        "⟨tone: ~1=high⟩ [+syllabic, tone: none] -> [+syllabic, tone: ~1]", project.features
    ).unwrap()
    first = sd.target[0]
    assert isinstance(first, FloatingAutoseg)
    value = first.pattern["tone"].value
    assert isinstance(value, AutosegBind) and value.ref == 1


def test_plain_floating_tone_parses(project):
    # ⟨tone: high⟩ with no bind — a floating tone matched by value alone.
    sd = parse_definition("⟨tone: high⟩ [+syllabic] -> [+syllabic]", project.features).unwrap()
    assert isinstance(sd.target[0], FloatingAutoseg)
    assert sd.target[0].pattern["tone"].value == 4


def test_unterminated_floating_bracket_rejected(project):
    assert parse_definition("⟨tone: high [+syll] -> [+syll]", project.features).is_err()


def test_dock_rule_validates(project):
    # The ⟨⟩ is zero-width, so cardinality is 1:1 (one target segment, one result) — well-formed.
    sd = parse_definition(
        "⟨tone: ~1=high⟩ [+syllabic, tone: none] -> [+syllabic, tone: ~1]", project.features
    ).unwrap()
    assert validate_structural_description(sd).is_ok()
