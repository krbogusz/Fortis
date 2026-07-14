from __future__ import annotations

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
            Optional in the TOML, defaulting to 0.
        raw_definition: Original definition string, kept for traces and errors.
        sd: Parsed structural description.
        words: If non-empty, the rule fires only on words whose id or gloss is listed
            — a sporadic / lexically-restricted change, or one staged to show a synchronic
            mechanism on a particular word. Empty ⇒ applies to every word.
        categories: If non-empty, the rule fires only on words whose grammatical category *at
            this rule's time* is listed — the class-wide counterpart of ``words``, which names
            individual words. The strings are matched literally against
            :attr:`~src.fortis.models.inventories.Attestation.category`, which is opaque and
            project-defined: the engine has no vocabulary of categories and never parses one, so
            a project chooses whatever scheme it likes. Empty ⇒ applies to every word.

            This is what makes a MORPHOLOGICALLY conditioned change expressible — one that
            applies to the verbs but not the nouns. Such a rule is not a sound law, and the
            distinction is worth keeping visible: a cascade that needs one is making a different
            (weaker) claim about the words it lands.
    """

    id: str
    time: int | None  # None = untimed: applied after every timed rule, shown without a prefix
    raw_definition: str
    sd: StructuralDescription
    application: ApplicationMode = ApplicationMode.simultaneous
    name: str | None = None
    description: str | None = None
    words: tuple[str, ...] = ()
    categories: tuple[str, ...] = ()


class RuleInventory(UserDict["int | None", tuple[Rule, ...]]):
    """Rules keyed by time, in file order at each time.

    The ``None`` key holds the untimed rules, applied after every timed one. Access
    ``inventory[-2000]`` to get all rules that apply at time −2000.
    """
