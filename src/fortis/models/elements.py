"""The rule AST: parsed structural descriptions and their building blocks.

Permissive on purpose — it can represent invalid rules so that load-time
validation can collect every problem at once instead of failing on the first.
"""

from dataclasses import dataclass
from enum import Enum, auto

from src.fortis.models.values import Value

# --------------------------------------------------------------------------- #
# Enums consumed by the AST
# --------------------------------------------------------------------------- #


class AlphaOp(Enum):
    """Greek-variable notation; bind-vs-recall is resolved at match time."""

    SAME = auto()  # [alpha F]
    OPPOSITE = auto()  # [-alpha F]   (binary/unary only)
    OTHER = auto()  # [!alpha F]


class ContourEdge(Enum):
    """A named position within a feature contour (sections 5.6, 5.9)."""

    INITIAL = auto()
    FINAL = auto()
    ANY = auto()
    ALL = auto()


type ContourPosition = ContourEdge | tuple[int, ...]  # tuple for @2, @2;3


class BoundaryKind(Enum):
    WORD = auto()  # #
    SYLLABLE = auto()  # $   (inert until syllabification lands)


class ApplicationMode(Enum):
    SIMULTANEOUS = auto()
    LEFT_TO_RIGHT = auto()
    RIGHT_TO_LEFT = auto()


@dataclass(frozen=True)
class Quantifier:
    """A repetition count. ``?`` ``*`` ``+`` are sugar over (min, max)."""

    min: int
    max: int | None  # None = unbounded


# --------------------------------------------------------------------------- #
# Pattern side (target / context / exception)
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ValueSpec:
    """Match a feature against a value. ``value=None`` means 'unspecified'.

    The feature being constrained is the key in the enclosing ``PatternBundle``.
    """

    value: Value
    negated: bool = False  # [!+syll]
    at: ContourPosition | None = None  # None = @any; target/context only


@dataclass(frozen=True)
class AlphaSpec:
    """Bind or recall a Greek variable over a feature.

    ``at`` selects a contour edge to bind to; None binds the whole contour.
    """

    var: str
    op: AlphaOp
    at: ContourPosition | None = None  # target/context only


# + ConditionalSpec later; + PresenceSpec only if a binary/scalar node is
#   ever named bare (a unary node named bare is just ValueSpec(present)).
type PatternSpec = ValueSpec | AlphaSpec


@dataclass(frozen=True)
class PatternBundle:
    """A pattern bundle: every feature's spec must hold against one segment."""

    specs: dict[str, PatternSpec]


# --------------------------------------------------------------------------- #
# Result side
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ValueAssign:
    """Assign a value. ``value=None`` delinks (cascades via geometry)."""

    value: Value


@dataclass(frozen=True)
class AlphaAssign:
    """Recall a bound Greek variable into the output segment."""

    var: str
    op: AlphaOp = AlphaOp.SAME


# + ConditionalAssign later
type ResultSpec = ValueAssign | AlphaAssign


@dataclass(frozen=True)
class ResultBundle:
    """A result bundle merges its per-feature specs into the matched segment."""

    specs: dict[str, ResultSpec]


# --------------------------------------------------------------------------- #
# Sequence elements
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class LetterRef:
    """Matches by features; in result position replaces the segment wholesale."""

    symbol: str


@dataclass(frozen=True)
class BundleElem:
    """Bundle element."""

    bundle: PatternBundle


@dataclass(frozen=True)
class ResultElem:
    """Result element."""

    bundle: ResultBundle


@dataclass(frozen=True)
class Wildcard:
    """Wildcard."""

    pass  # []


@dataclass(frozen=True)
class WordBoundary:  # zero-width assertion; excluded from cardinality checks
    """Word boundary."""

    pass


@dataclass(frozen=True)
class SyllableBoundary:  # zero-width assertion; excluded from cardinality checks
    """Syllable boundary."""

    pass


@dataclass(frozen=True)
class Null:
    """Null element."""

    pass  # the null segment, for insertion/deletion


@dataclass(frozen=True)
class Group:
    """Group."""

    elements: tuple[Element, ...]


@dataclass(frozen=True)
class Disjunction:
    """Disjunction."""

    branches: tuple[tuple[Element, ...], ...]


@dataclass(frozen=True)
class Negated:
    """Not element."""

    inner: Element  # !X


@dataclass(frozen=True)
class Quantified:
    """Quantified element."""

    inner: Element
    quant: Quantifier


@dataclass(frozen=True)
class Bound:
    """Binding for an element."""

    ref: int  # 1=...
    inner: Element


@dataclass(frozen=True)
class RecallRef:
    """Recall reference like '@1'."""

    ref: int


type Element = (
    LetterRef
    | BundleElem
    | ResultElem
    | Wildcard
    | Boundary
    | Null
    | Group
    | Disjunction
    | Negated
    | Quantified
    | Bound
    | RecallRef
)
