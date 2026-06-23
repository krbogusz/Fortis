"""Bindings environment for alpha (Greek-letter) variable resolution.

A ``Bindings`` maps Greek letters (α, β, γ, …) to their bound ``Value``.
It is populated during pattern matching and consulted during change
application.
"""

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
    """

    alpha: dict[str, Value] = field(default_factory=dict)
    reference: dict[int, FeatureBundle] = field(default_factory=dict)
    permissive_alpha: bool = False
    conditions: dict[int, bool] = field(default_factory=dict)
    disjunction_choices: tuple[int, ...] = ()
