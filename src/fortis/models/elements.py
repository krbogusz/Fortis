"""Element types for the phonological rule engine.

An Element is the structural unit that rules operate on — feature bundles,
letter shorthands, wildcards, boundaries, null segments, groups, disjunctions,
negations, alpha variables, conditional features, and references.  Each element
carries its own quantifier (default: exactly one match).
"""

from dataclasses import dataclass, field

from src.fortis.models.feature_bundle import FeatureBundle


@dataclass
class Quantifier:
    """How many times an element can match.

    min is the minimum number of repetitions (default 1).
    max is the maximum; None means unbounded.
    """

    min: int = 1
    max: int | None = 1  # None = unbounded

    def __post_init__(self) -> None:
        """Post initiation check."""
        if self.min < 0:
            raise ValueError(f"Quantifier min must be >= 0, got {self.min}")
        if self.max is not None and self.max < self.min:
            raise ValueError(f"Quantifier max ({self.max}) must be >= min ({self.min})")


@dataclass
class Element:
    """Base class for all rule elements. Carries a quantifier."""

    quantifier: Quantifier = field(default_factory=Quantifier)


@dataclass
class BundleElement(Element):
    """Feature pattern to match or merge — e.g. [+cons, -syll]."""

    bundle: FeatureBundle = field(default_factory=FeatureBundle)


@dataclass
class LetterShorthand(Element):
    """Letter key from the inventory — e.g. 'p', 'x'."""

    letter: str = ""


@dataclass
class WildcardElement(Element):
    """Matches any segment — written as '[]'."""


@dataclass
class BoundaryElement(Element):
    """Positional assertion — '#' for word boundary, '$' for syllable boundary."""

    boundary_type: str = "word"  # "word" or "syllable"


@dataclass
class NullElement(Element):
    """Insertion (in target) or deletion (in result) marker — written as '∅'."""


@dataclass
class GroupElement(Element):
    """Contiguous sequence of elements — (e1 e2 ...). Must match in order."""

    children: list[Element] = field(default_factory=list)


@dataclass
class DisjunctionElement(Element):
    """Alternatives — (e1 | e2 | ...). Exactly one branch must match."""

    branches: list[Element] = field(default_factory=list)


@dataclass
class NegationElement(Element):
    """Negated element — !e. Matches what does NOT match the child."""

    child: Element = field(default_factory=WildcardElement)


@dataclass
class AlphaElement(Element):
    """Alpha variable — [αF] binds/recalls a feature value using Greek letters."""

    alpha_name: str = ""
    bundle: FeatureBundle = field(default_factory=FeatureBundle)
    negated: bool = False


@dataclass
class ConditionalElement(Element):
    """Conditional feature — <n: F> applies only if paired condition is met."""

    label: int = 0
    bundle: FeatureBundle = field(default_factory=FeatureBundle)
    negated: bool = False


@dataclass
class ReferenceElement(Element):
    """Reference recall — @n recalls a previously bound group/element."""

    index: int = 0


@dataclass
class BindingElement(Element):
    """Reference binding — n=element saves a matched element as reference n."""

    index: int = 0
    binding: Element = field(default_factory=WildcardElement)
