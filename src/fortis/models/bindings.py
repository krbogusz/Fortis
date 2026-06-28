"""Bindings environment for alpha (Greek-letter) variable resolution.

A ``Bindings`` maps Greek letters (α, β, γ, …) to their bound ``Value``.
It is populated during pattern matching and consulted during change
application.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.values import Value


@dataclass
class Bindings:
    """Bindings for different elements.

    ``permissive_alpha`` is a resolution mode, not stored data: when set, alpha
    references match unconditionally and bind nothing. The sequence matcher's
    first pass uses it to find a target's structural span and capture its
    reference bindings without committing alpha (which must bind left-context
    first, in the second pass).

    ``conditions`` records, per conditional-feature label, whether that label's
    condition(s) held — accumulated (AND) across the target and context as the
    matcher evaluates them, then consulted by the applier to gate the paired
    result feature.

    ``disjunction_choices`` records, in encounter order, the branch index taken at
    each disjunction matched so far. The applier reads the *target's* slice of these
    (see ``Match.target_choices``) to select the paired result branch.

    ``pending_other`` holds deferred ``!α`` (alpha-*other*) constraints — ``(var,
    atom)`` pairs that require ``atom != α[var]``. Because ``!α`` is a ≠ relation it
    cannot itself *bind* α, so it is recorded here and verified once matching has
    bound the variable (keeping alpha resolution order-independent).
    """

    alpha: dict[str, Value] = field(default_factory=dict)
    reference: dict[int, tuple[FeatureBundle, ...]] = field(default_factory=dict)
    # Tier-autosegment references (``tone: ~1=H``): the matched *position* a bound
    # autosegment sits on, so the applier can recall the same autosegment for spread.
    autoseg_reference: dict[int, int] = field(default_factory=dict)
    # Floating-autosegment references (``⟨tone: ~1=H⟩``): the *id* of a matched floating
    # autosegment, so the applier can dock that same autosegment onto an anchor.
    floating_reference: dict[int, int] = field(default_factory=dict)
    # Node-spread references (``oral: ~1`` on a *segmental* node): the captured subtree — the
    # trigger's features under that node — so the applier can copy (merge) it onto the target.
    # Unlike tier ``~n`` (which shares a link), a segmental node spreads by copying its subtree.
    node_reference: dict[int, FeatureBundle] = field(default_factory=dict)
    permissive_alpha: bool = False
    conditions: dict[int, bool] = field(default_factory=dict)
    disjunction_choices: tuple[int, ...] = ()
    pending_other: list[tuple[str, object]] = field(default_factory=list)
