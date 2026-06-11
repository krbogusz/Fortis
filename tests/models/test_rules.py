"""Tests for rule types."""

from src.fortis.models.bundles import PatternBundle
from src.fortis.models.elements import LetterRef
from src.fortis.models.rules import ApplicationMode, Rule, StructuralDescription
from src.fortis.models.specs import PatternSpec


class TestApplicationMode:
    def test_values(self):
        assert ApplicationMode.simultaneous == "simultaneous"
        assert ApplicationMode.left_to_right == "left_to_right"
        assert ApplicationMode.right_to_left == "right_to_left"


class TestStructuralDescription:
    def test_with_defaults(self):
        sd = StructuralDescription(target=(), result=())
        assert sd.target == ()
        assert sd.result == ()
        assert sd.left_context == ()
        assert sd.right_context == ()
        assert sd.left_exception == ()
        assert sd.right_exception == ()

    def test_with_target_and_result(self):
        target = (LetterRef(symbol="a"),)
        result = (LetterRef(symbol="b"),)
        sd = StructuralDescription(target=target, result=result)
        assert sd.target == target
        assert sd.result == result


class TestRule:
    def test_construction(self):
        sd = StructuralDescription(target=(), result=())
        rule = Rule(id="r1", time=0, raw_definition="a -> b", sd=sd)
        assert rule.id == "r1"
        assert rule.time == 0
        assert rule.name is None
        assert rule.description is None