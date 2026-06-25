"""Derivation output: the per-word trace."""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule


@dataclass(frozen=True)
class DerivationStep:
    """One firing rule: the form before, the rule, and the form after.

    The step carries only data — the human-readable change summary is formatted
    from ``before``/``after`` in the presentation layer (``rendering.describe_change``),
    which has the inventories needed to render segments as IPA.
    ``before_boundaries``/``after_boundaries`` carry each form's syllable structure
    for the trace; empty when syllabification is unconfigured or the form is
    unsyllabifiable.
    """

    before: list[FeatureBundle]
    rule: Rule
    after: list[FeatureBundle]
    before_boundaries: frozenset[int] = frozenset()
    after_boundaries: frozenset[int] = frozenset()


@dataclass(frozen=True)
class Derivation:
    """The whole record of change.

    ``surface_boundaries`` carries the syllable structure of the surface form (the
    boundary positions from syllabification), so the structure is available to the
    output without re-syllabifying; empty when syllabification is unconfigured.
    """

    word: Word
    input: list[FeatureBundle]
    steps: tuple[DerivationStep, ...]  # firing steps only
    surface: list[FeatureBundle]
    surface_boundaries: frozenset[int] = frozenset()
