from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass, field
from enum import StrEnum, auto
from functools import cached_property

from src.fortis.general.utils import by_length
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.elements import Element
from src.fortis.models.tiers import Tier


@dataclass(frozen=True)
class Letter:
    """A letter symbol with its symbol and feature bundle."""

    symbol: str
    bundle: FeatureBundle


class LetterInventory(UserDict[str, Letter]):
    """Segment symbols mapped to their feature bundles.

    Pre-computes sorted symbol lists at construction time for greedy
    longest-first matching in IPA tokenisation.  Access them via the
    ``sorted_keys`` property.
    """

    @cached_property
    def sorted_keys(self) -> list[str]:
        """All symbol keys sorted longest-first."""
        return by_length(self.data)


class DiacriticKind(StrEnum):
    """Where a diacritic attaches relative to its base symbol."""

    before = auto()
    combining = auto()
    after = auto()


@dataclass(frozen=True)
class Diacritic:
    """A diacritic symbol with its tier, attachment type, and feature bundle.

    Args:
        symbol: The diacritic character(s).
        tier: Phonological tier this diacritic belongs to.
        kind: Where the diacritic attaches relative to its base.
        bundle: Feature bundle the diacritic contributes.
        contour: Whether this diacritic forms contours when combined.
        read_only: An input-only alias — accepted when reading the lexicon, but never emitted on
            output (rendering uses the non-``read_only`` diacritic for each value).
        marks_boundary: Whether this diacritic, placed at a syllable edge, is
            itself the boundary marker — so rendering omits the separate ``.``.
    """

    symbol: str
    tier: Tier
    kind: DiacriticKind
    bundle: FeatureBundle
    contour: bool
    read_only: bool = False
    marks_boundary: bool = False


class DiacriticInventory(UserDict[str, Diacritic]):
    """Diacritic symbols mapped to their definitions.

    Pre-computes sorted symbol lists at construction time for greedy
    longest-first matching in IPA tokenisation.  Access them via the
    ``segment_keys``, ``syllable_keys``, ``before_keys``, and
    ``attaching_keys`` properties.
    """

    @cached_property
    def segment_keys(self) -> list[str]:
        """Segment-tier diacritic symbols sorted longest-first."""
        return by_length(self.segment_dict)

    @cached_property
    def segment_dict(self) -> dict[str, Diacritic]:
        """Segment-tier diacritics keyed by symbol."""
        return {s: d for s, d in self.data.items() if d.tier == Tier.segment}

    @cached_property
    def syllable_keys(self) -> list[str]:
        """Syllable-tier diacritic symbols sorted longest-first."""
        return by_length(s for s, d in self.data.items() if d.tier == Tier.syllable)

    @cached_property
    def before_keys(self) -> list[str]:
        """Before-type diacritic symbols sorted longest-first."""
        return by_length(s for s, d in self.data.items() if d.kind == DiacriticKind.before)

    @cached_property
    def attaching_keys(self) -> list[str]:
        """Combining/after-type diacritic symbols sorted longest-first."""
        return by_length(s for s, d in self.data.items() if d.kind != DiacriticKind.before)


@dataclass
class Sonority:
    """A sonority level with its feature bundle.

    Args:
        label: Name/label of this sonority level.
        level: Numerical sonority level (higher = more sonorous).
        bundle: Feature bundle for this level, or None.
    """

    label: str
    level: int
    bundle: PatternBundle | None


class SonoritiesInventory(UserDict[str, Sonority]):
    """Sonority levels keyed by label."""


@dataclass
class SyllablePart:
    """A constraint definition for one syllable part (onset, nucleus, or coda).

    The **nucleus** is a single-segment predicate (``definition``): a segment is a
    nucleus iff it matches. An **onset** or **coda** is an element-sequence
    ``pattern`` (the same notation as a rule context) that a candidate constituent
    must match in full — so length, cluster shape, and optionality are expressed
    directly (``[+cons][-syll, -cons]?`` is "≤2, a consonant then optional glide";
    ``[nasal]?`` is an optional nasal coda).

    Args:
        part_type: Which part of the syllable ("onset", "nucleus", or "coda").
        time: Application time for this constraint.
        definition: Single-segment pattern identifying nuclei (nucleus only).
        pattern: Element sequence a constituent must fully match (onset/coda only).
    """

    part_type: str
    time: int
    definition: PatternBundle | None = None
    pattern: tuple[Element, ...] | None = None


class SyllablePartsInventory(UserDict[int, dict[str, SyllablePart]]):
    """Syllable part constraints keyed by application time.

    Each time key maps to a dict of part_type → SyllablePart (e.g. "onset",
    "nucleus", "coda"). Dict keys enforce one of each part per time.

    Definitions carry forward independently per part: a later time that
    redefines only some parts leaves the others in force from earlier.
    """

    def get_part(self, time: int | None, part_type: str) -> SyllablePart | None:
        """Return the ``part_type`` definition in effect at ``time``.

        The active part is the one from the greatest time ≤ ``time`` that
        defines ``part_type``; a later time redefining only other parts does
        not clear it. Returns ``None`` if no such part exists at or before
        ``time``. A ``time`` of ``None`` (an untimed rule, applied last) takes the latest.

        Args:
            time: The current derivation time.
            part_type: Which part to resolve ("onset", "nucleus", or "coda").
        """
        applicable = (t for t in self.data if time is None or t <= time)  # None ⇒ latest
        for defined_time in sorted(applicable, reverse=True):
            part = self.data[defined_time].get(part_type)
            if part is not None:
                return part
        return None

    def get_nucleus(self, time: int | None) -> SyllablePart | None:
        """Return the nucleus definition in effect at ``time``.

        Args:
            time: The current derivation time.
        """
        return self.get_part(time, "nucleus")


@dataclass
class Word:
    """A word with its IPA transcription and optional gloss + attested forms.

    Only ``ipa`` feeds derivation. ``final`` and ``stages`` are optional *target*
    annotations co-located with the input — attested surface forms a grader can
    compare the derived output against — and are ignored by the engine itself.

    Attributes:
        ipa: The IPA transcription string (the derivation input).
        gloss: An optional gloss or translation.
        final: The attested final/target surface form, if known (for grading).
        stages: Attested forms keyed by time stage (for per-period grading);
            keys are stage times, values the attested form at that stage.
    """

    ipa: str
    gloss: str = ""
    final: str | None = None
    stages: dict[int, str] = field(default_factory=dict)


class WordInventory(UserDict[str, Word]):
    """Words keyed by their IPA form, loaded from TOML.

    The key is the IPA string itself (same as ``Word.ipa``).
    """
