from collections import UserDict
from dataclasses import dataclass
from enum import StrEnum, auto

from src.fortis.models.elements import Element


class ApplicationMode(StrEnum):
    """How a rule should be applied when multiple loci match."""

    simultaneous = auto()  # default — find every locus, rewrite all at once
    left_to_right = auto()
    right_to_left = auto()


@dataclass(frozen=True)
class StructuralDescription:
    """A parsed rule definition: A -> B / C _ D // E _ F.

    The underscore is encoded structurally by splitting context and exception
    into their left and right halves.
    """

    target: tuple[Element, ...]
    result: tuple[Element, ...]
    left_context: tuple[Element, ...] = ()
    right_context: tuple[Element, ...] = ()
    left_exception: tuple[Element, ...] = ()
    right_exception: tuple[Element, ...] = ()


@dataclass(frozen=True)
class Rule:
    """A single phonological rule.

    Attributes:
        id: Slug from the TOML table header.
        time: Sort key for chronology (lower applies earlier; may be negative).
        raw_definition: Original definition string, kept for traces and errors.
        sd: Parsed structural description.
    """

    id: str
    time: int
    raw_definition: str
    sd: StructuralDescription
    application: ApplicationMode = ApplicationMode.simultaneous
    name: str | None = None
    description: str | None = None


class RuleInventory(UserDict[str, tuple[Rule]]):
    """Rules mapped by their time and then order in the rules.toml."""
