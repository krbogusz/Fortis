"""Derivation output: the per-word trace."""

from dataclasses import dataclass

from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Word
from src.fortis.models.rules import Rule


@dataclass(frozen=True)
class DerivationStep:
    """One firing rule: the form before, the rule, a change summary, the after."""

    before: list[FeatureBundle]
    rule: Rule
    change: str
    after: list[FeatureBundle]


@dataclass(frozen=True)
class Derivation:
    """The whole record of change."""

    word: Word
    input: list[FeatureBundle]
    steps: tuple[DerivationStep, ...]  # firing steps only
    surface: list[FeatureBundle]
