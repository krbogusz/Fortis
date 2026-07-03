"""Feature values: a single value, a contour, or their union."""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Literal


class AlphaOp(StrEnum):
    """Greek-variable notation; bind-vs-recall is resolved at match time."""

    same = auto()  # [alpha F]
    opposite = auto()  # [-alpha F] (binary/unary and simple only)
    other = auto()  # [!alpha F]


@dataclass(frozen=True)
class AlphaRef:
    """Alpha reference.

    ``unary`` records that the alpha sits on a unary (privative) feature, whose
    poles are *present* (1) and *absent* (none). Its opposite (``-α``) therefore
    flips 1 ↔ none, as opposed to a binary feature's 0 ↔ 1.
    """

    var: str
    op: AlphaOp = AlphaOp.same
    unary: bool = False


@dataclass(frozen=True)
class AutosegBind:
    """Bind the tier autosegment carrying this value (``tone: ~1=H``).

    The autosegment is matched by its inner ``value`` (e.g. H) and recorded under ``ref``,
    so a later ``AutosegRecall`` on another anchor can associate the **same** autosegment —
    the difference between *spreading* a tone (one autosegment, many anchors) and *copying*
    it (a fresh autosegment).
    """

    ref: int
    value: Limb


@dataclass(frozen=True)
class AutosegRecall:
    """Recall a bound tier autosegment (``tone: ~1``): associate the same one — spread."""

    ref: int


type SingleValue = int | None | Literal["any"]  # None == undefined / unspecified
type Limb = SingleValue | AlphaRef | AutosegBind | AutosegRecall
type ContourValue = tuple[Limb, ...]
type Value = SingleValue | AlphaRef | AutosegBind | AutosegRecall | ContourValue


class ContourEdge(StrEnum):
    """A named position within a feature contour (sections 5.6, 5.9)."""

    initial = auto()
    final = auto()
    any = auto()
    all = auto()


type ContourPosition = ContourEdge | int | tuple[int, ...]  # tuple for @2, @2;3


def opposite_pole(atom: Limb, unary: bool) -> Limb:
    """The opposite pole of a value — what ``-α`` resolves to.

    A **unary** (privative) feature flips present (1) ↔ absent (``None``); a
    **binary** feature flips 0 ↔ 1. Alpha-opposite is validation-restricted to
    these two kinds (scalar is rejected), so any other atom is left unchanged
    (defensive, unreachable). Shared by the matcher (binding ``-α``) and the
    applier (recalling ``-α`` in a result), so the two never diverge on what the
    opposite pole is.
    """
    if unary:
        return None if atom == 1 else 1
    if atom == 0:
        return 1
    if atom == 1:
        return 0
    return atom


def make_value(limbs: tuple[Limb, ...]) -> Value:
    """Build a feature value, normalizing away non-contrastive shape.

    A run of identical adjacent limbs is a level stretch, not a contour — it carries no
    contrast — so it folds to one (``5>5`` → ``5``, ``5>5>3`` → ``5>3``). A resulting
    length-1 contour then collapses to a scalar. This keeps two same-valued autosegments
    that land on one anchor (e.g. tone spread onto a like tone) from reading as a spurious
    ``x>x`` rather than the single value they are.
    """
    folded: list[Limb] = []
    for limb in limbs:
        if not folded or folded[-1] != limb:
            folded.append(limb)
    return folded[0] if len(folded) == 1 else tuple(folded)


def form_contour(value_1: Value, value_2: Value) -> Value:
    """Form a contour from two values, each of which can also be contour.

    Routed through ``make_value`` so a level meeting its own value (``H`` onto ``H``) yields
    the single value, not ``H>H``.
    """
    limbs_1: ContourValue = (value_1,) if not isinstance(value_1, tuple) else value_1
    limbs_2: ContourValue = (value_2,) if not isinstance(value_2, tuple) else value_2
    return make_value(limbs_1 + limbs_2)
