"""Bindings environment for alpha (Greek-letter) variable resolution.

A ``Bindings`` maps Greek letters (α, β, γ, …) to their bound ``Value``.
It is populated during pattern matching and consulted during change
application.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.fortis.models.values import AlphaValue, Value

if TYPE_CHECKING:
    from src.fortis.models.pattern_spec import PatternSpec


@dataclass
class Bindings:
    """Bindings for different elements."""

    alpha: dict[AlphaValue, Value] = field(default_factory=lambda: {})
    reference: dict[int, PatternSpec] = field(default_factory=lambda: {})
