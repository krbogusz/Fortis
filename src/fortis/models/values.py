"""Feature values: a single value, a contour, or their union."""

from dataclasses import dataclass
from enum import StrEnum, auto


class AlphaOp(StrEnum):
    """Greek-variable notation; bind-vs-recall is resolved at match time."""

    same = auto()  # [alpha F]
    opposite = auto()  # [-alpha F] (binary/unary and simple only)
    other = auto()  # [!alpha F]


@dataclass(frozen=True)
class AlphaRef:
    """Alpha reference."""

    var: str
    op: AlphaOp = AlphaOp.same


class Wildcard(StrEnum):
    """Match-only sentinels standing in for a concrete value."""

    wildcard = auto()


type SingleValue = int | None | Wildcard  # None == undefined / unspecified
type Limb = SingleValue | AlphaRef
type ContourValue = tuple[Limb, ...]
type Value = SingleValue | AlphaRef | ContourValue


class ContourEdge(StrEnum):
    """A named position within a feature contour (sections 5.6, 5.9)."""

    initial = auto()
    final = auto()
    any = auto()
    all = auto()


type ContourPosition = ContourEdge | int | tuple[int, ...]  # tuple for @2, @2;3


def make_value(limbs: tuple[SingleValue, ...]) -> Value:
    """Build a feature value, collapsing a length-1 contour to a scalar."""
    return limbs[0] if len(limbs) == 1 else limbs


def form_contour(value_1: Value, value_2: Value) -> Value:
    """Form a contour from two values, each of which can also be contour."""
    limbs_1: ContourValue = (value_1,) if not isinstance(value_1, tuple) else value_1
    limbs_2: ContourValue = (value_2,) if not isinstance(value_2, tuple) else value_2
    return limbs_1 + limbs_2
