from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass
from enum import StrEnum, auto
from functools import cached_property

from src.fortis.models.tiers import Tier


class FeatureKind(StrEnum):
    """Whether a feature is unary, binary, or scalar."""

    unary = auto()
    binary = auto()
    scalar = auto()


@dataclass
class Feature:
    """A feature's tier, type, short name, values, and hierarchical relations.

    Args:
        name: Feature name (also its key in the inventory).
        tier: Phonological tier this feature belongs to.
        kind: Whether the feature is unary, binary, or scalar.
        short_name: Short/abbreviated name for compact notation.
        values: Mapping of integer codes to human-readable labels.
        children: Sub-features in the feature hierarchy, if any.
        parent: Name of the parent feature, assigned after loading.
    """

    name: str
    tier: Tier
    kind: FeatureKind
    short_name: str
    values: dict[int, str]
    children: tuple[str, ...] | None
    parent: str | None = None


class FeatureInventory(UserDict[str, Feature]):
    """Feature definitions keyed by name, loaded from TOML with cross-feature validation."""

    def is_node(self, feature: str) -> bool:
        """Does this feature have children?"""
        return bool(self.data[feature].children)

    def children(self, feature: str) -> tuple[str, ...]:
        """Immediate children of the feature."""
        return tuple(self.data[feature].children or ())

    def descendants(self, feature: str) -> tuple[str, ...]:
        """All descendants of the feature, depth-first; empty if it is a leaf."""
        result: list[str] = []
        for child in self.children(feature):
            result.append(child)
            result.extend(self.descendants(child))
        return tuple(result)

    def parent(self, feature: str) -> str | None:
        """Parent of the feature."""
        return self.data[feature].parent

    def ancestors(self, feature: str) -> tuple[str, ...]:
        """All ancestor nodes of the feature, nearest first; empty if it is a root."""
        result: list[str] = []
        parent = self.parent(feature)
        while parent is not None:
            result.append(parent)
            parent = self.parent(parent)
        return tuple(result)

    @cached_property
    def names_by_length(self) -> tuple[str, ...]:
        """Feature names sorted longest-first (for greedy matching)."""
        return tuple(sorted(self.data.keys(), key=len, reverse=True))

    @cached_property
    def short_names_by_length(self) -> tuple[str, ...]:
        """Short names sorted longest-first (for greedy matching)."""
        return tuple(
            sorted(
                (f.short_name for f in self.data.values()),
                key=len,
                reverse=True,
            )
        )

    @cached_property
    def short_to_long_name(self) -> dict[str, str]:
        """Map short names to full feature names."""
        return {f.short_name: name for name, f in self.data.items()}
