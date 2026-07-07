"""The rule AST: parsed structural descriptions and their building blocks.

Permissive on purpose — it can represent invalid rules so that load-time
validation can collect every problem at once instead of failing on the first.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.fortis.models.bundles import FeatureBundle, PatternBundle, ResultBundle


@dataclass(frozen=True)
class Quantifier:
    """A repetition count. ``?`` ``*`` ``+`` are sugar over (min, max)."""

    min: int
    max: int | None  # None = unbounded


@dataclass(frozen=True)
class LetterRef:
    """Matches by features; in result position replaces the segment wholesale."""

    symbol: str


@dataclass(frozen=True)
class LetterBundle:
    """A run of letters+diacritics resolved (via the segmenter) to one segment.

    Behaves exactly like a :class:`LetterRef` — subset match in target/context,
    wholesale replacement in result — but carries the feature bundle directly, so a
    complex symbol like ``ʁʷ`` (or one segment of a multi-segment run like ``au``)
    needs no entry in the letter inventory. Distinct from :class:`BundleElem`, which
    is a pattern that *merges* in result position.
    """

    bundle: FeatureBundle


@dataclass(frozen=True)
class ModifiedLetter:
    """A letter shorthand with a concrete feature override: ``e^[stress: none]``.

    The base letter's full specification with *delta* combined on top — a wholesale
    replacement (like a letter), but with the named features changed (or delinked, for a
    ``none`` value). ``resolve_rule_letters`` expands it to a :class:`LetterBundle` of
    ``combine(letter, delta)``, so nothing downstream needs a new case; the ``^`` binds the
    **last** letter of a run (``au^[length: long]`` = ``a`` then a lengthened ``u``). *delta*
    is a realized (concrete) bundle — no negation, alpha, or conditional features.
    """

    symbol: str
    delta: FeatureBundle


@dataclass(frozen=True)
class BundleElem:
    """A pattern bundle in target, context, or exception position."""

    bundle: PatternBundle


@dataclass(frozen=True)
class FloatingAutoseg:
    """A floating autosegment ``⟨...⟩`` — a tier element carrying no association line.

    Matched against an autosegment with no anchor (e.g. a tone stranded by its vowel's
    deletion); a ``~ref`` bind inside lets a result recall it onto an anchor (docking).
    """

    pattern: PatternBundle


@dataclass(frozen=True)
class ResultElem:
    """A result bundle in result position."""

    bundle: ResultBundle


@dataclass(frozen=True)
class Wildcard:
    """Matches any single segment. ``[]``."""


@dataclass(frozen=True)
class WordBoundary:
    """Zero-width word-edge assertion; excluded from cardinality checks."""


@dataclass(frozen=True)
class SyllableBoundary:
    """Zero-width syllable-edge assertion; excluded from cardinality checks."""


type Boundary = SyllableBoundary | WordBoundary


@dataclass(frozen=True)
class MorphemeBoundary:
    """The morpheme-boundary token ``-``: a real, deletable one-wide segment.

    Unlike :class:`WordBoundary`/:class:`SyllableBoundary` (zero-width assertions), a
    morpheme boundary occupies a position on the segmental tier. It forces a syllable
    break, and an ordinary rule can match and delete it (``- -> ∅``) or insert one
    (``∅ -> -``). It is matched only against a boundary segment — no phonological
    pattern matches it — so it counts toward a side's cardinality like any segment.
    """


@dataclass(frozen=True)
class Null:
    """The null segment, for insertion and deletion."""


@dataclass(frozen=True)
class Group:
    """A parenthesised sub-sequence."""

    elements: tuple[Element, ...]


@dataclass(frozen=True)
class Disjunction:
    """An alternation: any one of its branches may match."""

    branches: tuple[tuple[Element, ...], ...]


@dataclass(frozen=True)
class Negated:
    """A negated element. ``!X``."""

    inner: Element


@dataclass(frozen=True)
class Quantified:
    """An element under a repetition count."""

    inner: Element
    quant: Quantifier


@dataclass(frozen=True)
class Bound:
    """An element bound to a back-reference index. ``1=...``."""

    ref: int
    inner: Element


@dataclass(frozen=True)
class RecallRef:
    """A recall of a bound element. ``@1``."""

    ref: int


type Element = (
    LetterRef
    | LetterBundle
    | ModifiedLetter
    | BundleElem
    | FloatingAutoseg
    | ResultElem
    | Wildcard
    | SyllableBoundary
    | WordBoundary
    | MorphemeBoundary
    | Null
    | Group
    | Disjunction
    | Negated
    | Quantified
    | Bound
    | RecallRef
)
