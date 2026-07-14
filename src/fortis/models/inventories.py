from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass, field
from enum import StrEnum, auto
from functools import cached_property

from src.fortis.general.utils import by_length
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.elements import Element
from src.fortis.models.form import Form
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


def time_order(time: int | None) -> tuple[bool, int]:
    """Sort key putting the untimed slot (``None``) last — the engine's convention throughout.

    ``None`` means "after everything" in both inventories, and for the same reason: a
    :class:`~src.fortis.models.rules.RuleInventory` applies its untimed rules after every timed
    one, so a word's ``None`` attestation is its surface after every rule has run — the old
    ``final`` column. A year cannot express that, because the untimed rules have no year.
    """
    return (time is None, 0 if time is None else time)


@dataclass
class Attestation:
    """A word's form at one point in time.

    The same object serves as the derivation *seed* (the earliest one) and as a *target* (every
    later one). That is the point: an input is not a different kind of thing from an attested
    form, it is simply the earliest one we have, and the old model's split into ``ipa`` (the
    input) plus ``final`` (the last target) plus ``stages`` (the middle ones) was three names for
    one relation.

    Attributes:
        ipa: The IPA transcription at this time.
        category: The word's grammatical category here — an opaque, project-defined string
            (``"verb.pres.3sg.weak"``, ``"noun.acc.sg"``, ``"n-stem"``; the engine has no
            vocabulary of its own and never parses it). A rule may be scoped to a set of these
            (:attr:`~src.fortis.models.rules.Rule.categories`), which is how a change is
            restricted to one word class.

            It is **given, not derived** — an annotation supplied by the analyst, exactly like
            the seed IPA, and never predicted by the engine. That is what keeps it out of
            circularity: the engine still predicts only the *IPA*, and the category conditions
            the sound laws the way "this is a weak class-1 verb" conditions them in a handbook.
            Giving a *different* category at a later time is therefore how a REANALYSIS is
            expressed (PGmc ``*hwehwlą`` is neuter where its PIE source is masculine): rules
            after that time see the new category. See :meth:`Word.category_at`.
        form: The IPA segmented against the project inventory — the *ingested* record the
            accuracy/errors analyses compare against, kept as a ``Form`` so it retains the full
            autosegmental structure (a segment is one inventory unit — an affricate ``d͡ʒ`` is
            one, not split by codepoint — and any tone/stress tiers survive). Populated by a
            post-load pass (:func:`src.fortis.analysis.accuracy.ingest_targets`); ``None`` when
            the IPA uses a symbol the inventory cannot segment (that form is then skipped, with
            a warning) — so ``ipa`` present but ``form`` None means UNSEGMENTABLE, not "absent".
    """

    ipa: str
    category: str = ""
    form: Form | None = None


@dataclass
class Word:
    """A word as a series of attested forms through time.

    Attributes:
        id: Stable identifier, and the inventory key. Deliberately NOT the gloss: identity and
            human-label are different concerns, glosses collide (``lay`` is both a verb and a
            noun), and a generated lexicon's gloss is often not even a gloss — where a word has
            no modern reflex there is nothing to gloss it with. Write ``bear-v``/``bear-n``.
        forms: Attested forms keyed by time. The EARLIEST is the derivation seed (the input);
            every later one is a target the derived form is scored against at that time. A seed
            is not scored against itself.
        gloss: A human label. Free text; never load-bearing.
        frequency: A token frequency (a positive integer weight; default 1) for
            frequency-weighted accuracy — a word counts this many times toward the weighted
            accuracy and mean distances. A property of the word, not of any one time. Ignored by
            the engine.
    """

    id: str
    forms: dict[int | None, Attestation] = field(default_factory=dict)
    gloss: str = ""
    frequency: int = 1

    @classmethod
    def from_series(
        cls,
        id: str,  # noqa: A002 — matches the field name
        seed: str,
        *,
        seed_time: int | None = 0,
        stages: dict[int, str] | None = None,
        final: str | None = None,
        gloss: str = "",
        frequency: int = 1,
        category: str = "",
    ) -> Word:
        """Build a word from a seed plus the old-style ``stages``/``final`` targets.

        A convenience for callers that synthesise a lexicon (the inducer's interval projects),
        where the forms arrive as separate source/target strings rather than as a series.
        """
        # The seed is "the earliest form", so a seed_time that is NOT earliest would silently
        # demote it to a target and promote a stage to the input. Fail loudly instead: the
        # default (0) is wrong the moment a project has negative stage times.
        too_early = [t for t in (stages or {}) if time_order(t) <= time_order(seed_time)]
        if too_early:
            raise ValueError(
                f"word {id!r}: seed_time {seed_time} is not before every stage "
                f"({', '.join(map(str, sorted(too_early)))}) — the earliest form is the seed, "
                "so this would make a stage the derivation input"
            )
        forms: dict[int | None, Attestation] = {seed_time: Attestation(seed, category)}
        for time, ipa in (stages or {}).items():
            forms[time] = Attestation(ipa, category)
        if final is not None:
            forms[None] = Attestation(final, category)
        return cls(id=id, forms=forms, gloss=gloss, frequency=frequency)

    @property
    def seed_time(self) -> int | None:
        """The time the derivation starts from: the earliest attested form."""
        return min(self.forms, key=time_order)

    @property
    def seed(self) -> Attestation:
        """The derivation input — the earliest attested form."""
        return self.forms[self.seed_time]

    @property
    def targets(self) -> dict[int | None, Attestation]:
        """Every form the derivation is scored against: all but the seed."""
        return {t: a for t, a in self.forms.items() if t != self.seed_time}

    def category_at(self, time: int | None) -> str:
        """The category in force at *time* — from the latest attestation at or before it.

        A rule at time T asks this, so a category given at a LATER time takes effect for every
        rule from that time on: that is how a reanalysis is expressed. A rule earlier than any
        attestation sees the seed's category.
        """
        at_or_before = [t for t in self.forms if time_order(t) <= time_order(time)]
        if not at_or_before:
            return self.seed.category
        return self.forms[max(at_or_before, key=time_order)].category

    def set_stages(self, stages: dict[int, str], category: str = "") -> None:
        """Replace every TIMED target with *stages*, leaving the seed and the surface alone."""
        for time in list(self.forms):
            if time is not None and time != self.seed_time:
                del self.forms[time]
        for time, ipa in stages.items():
            self.forms[time] = Attestation(ipa, category)

    # --- Views onto `forms`, for the analysis layer -------------------------------------------
    # These are the questions the accuracy/blame/diagnosis code actually asks — "the seed", "the
    # surface target", "the timed targets" — so they stay as named accessors rather than making
    # every caller re-derive them. They are READ-ONLY: `forms` is the single source of truth.

    @property
    def ipa(self) -> str:
        """The derivation input: the seed's IPA."""
        return self.seed.ipa

    @property
    def final(self) -> str | None:
        """The attested surface — the target at the untimed slot — or None if absent."""
        attestation = self.forms.get(None)
        return attestation.ipa if attestation is not None else None

    @property
    def final_form(self) -> Form | None:
        """The surface target, segmented. None if absent OR unsegmentable."""
        attestation = self.forms.get(None)
        return attestation.form if attestation is not None else None

    @property
    def stages(self) -> dict[int, str]:
        """The TIMED targets, by time — every attestation but the seed and the surface."""
        return {
            time: attestation.ipa
            for time, attestation in self.forms.items()
            if time is not None and time != self.seed_time
        }

    @property
    def stage_forms(self) -> dict[int, Form]:
        """The timed targets, segmented. A target the inventory could not segment is absent."""
        return {
            time: attestation.form
            for time, attestation in self.forms.items()
            if time is not None and time != self.seed_time and attestation.form is not None
        }


class WordInventory(UserDict[str, Word]):
    """Words keyed by :attr:`Word.id`."""
