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
    """Bindings for different elements."""

    alpha: dict[str, Value] = field(default_factory=dict)
    reference: dict[int, FeatureBundle] = field(default_factory=dict)
