"""Syllabification: place syllable boundaries on a form from sonority.

``syllabify`` is a structural pass (not a rule). It identifies nuclei (segments
matching the time-appropriate nucleus definition), then divides the consonants
between each adjacent pair of nuclei into a coda + onset by the **Maximal Onset
Principle** under **sonority sequencing**: the onset is the longest rightmost run
whose sonority strictly rises toward the following nucleus; whatever is left
becomes the preceding nucleus's coda. No segments are inserted or deleted (§7).

The result is the set of boundary positions — a boundary at index ``k`` sits
*before* segment ``k`` (between ``k-1`` and ``k``). A syllabified word also counts
its two word edges (``0`` and ``len``) as syllable boundaries, so the ``$``
assertion holds there as well as at interior divisions; a word with no nucleus is
unsyllabifiable and yields no boundaries at all.

Sonority levels come from the user's scale by first-match in file order
(``SonoritiesInventory`` preserves it); a segment matching no predicate is
treated as least sonorous.

Onset/coda **patterns** from ``syllable_parts`` are element sequences (the same
notation as a rule context) that a candidate constituent must match in full.
When a pattern is defined, it *defines* legality: every split point is a
candidate, the longest pattern-legal onset wins, and sonority is not consulted —
so a pattern may license a non-sonority-rising onset (e.g. ``s``+stop). With no
pattern, the sonority Maximal Onset division above is used. ``[nasal]`` is a
mandatory single-nasal coda; ``[nasal]?`` an optional one (the matcher's
quantifiers express optionality — there is no implicit empty). If no split is
pattern-legal for a cluster, syllabification **falls back to the sonority Maximal
Onset division** for that cluster (rather than failing) and reports the fallback,
so the derivation always has structure; the caller can surface a warning. Patterns
apply only at the interior split where there is a choice; word-edge onsets/codas
are forced and not checked.
"""
from __future__ import annotations

from src.fortis.application.matching import full_match, pattern_matches
from src.fortis.general.utils import IdentityCache
from src.fortis.models.bundles import FeatureBundle, PatternBundle, is_morpheme_boundary
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePart,
    SyllablePartsInventory,
)
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.syllable import Syllable

# A fallen-back cluster, as the ``(start, end)`` half-open span of segment positions whose
# division the patterns could not make and that used the sonority split instead.
type Fallback = tuple[int, int]


def syllables(
    segments: list[FeatureBundle], boundaries: frozenset[int], nucleus: PatternBundle | None
) -> list[Syllable]:
    """The syllables of *segments* under *boundaries* — the one place this grouping lives.

    Consecutive boundaries (plus the word edges 0 and ``len``) delimit each syllable; its nucleus
    is the first segment matching *nucleus* (the project's nucleus pattern, e.g. ``+syllabic``), or
    ``None`` when the span has no nucleus (or no pattern is given).
    """
    edges = sorted(set(boundaries) | {0, len(segments)})
    out: list[Syllable] = []
    for left, right in zip(edges, edges[1:], strict=False):
        nuc = None
        if nucleus is not None:
            nuc = next(
                (i for i in range(left, right) if pattern_matches(nucleus, segments[i])), None
            )
        out.append(Syllable(left, right, nuc))
    return out


_sonority_cache = IdentityCache(maxsize=4096)


def _sonority(segment: FeatureBundle, sonorities: SonoritiesInventory) -> int:
    """The sonority level of *segment* by first-match; least sonorous if unmatched.

    Cached by *segment*'s identity: bundles are immutable in practice and shared
    between successive forms (a rewrite splices new segments but keeps the rest),
    so the same bundle object is re-scored across every rule of a derivation. The
    inventory is stored in the entry and verified by ``is``; a mismatch (a
    different scale under a reused id) just recomputes.
    """
    cached_scale, level = _sonority_cache.get_or_compute(
        segment, None, lambda: (sonorities, _sonority_uncached(segment, sonorities))
    )
    if cached_scale is sonorities:
        return level
    return _sonority_uncached(segment, sonorities)


def _sonority_uncached(segment: FeatureBundle, sonorities: SonoritiesInventory) -> int:
    for sonority in sonorities.values():
        if sonority.bundle is not None and pattern_matches(sonority.bundle, segment):
            return sonority.level
    return 0


def _onset_start(cluster: list[int]) -> int:
    """Index within an intervocalic *cluster* where the onset begins.

    *cluster* is the sonority levels of the consonants strictly between two
    nuclei. The onset is the maximal suffix whose sonority strictly rises toward
    the nucleus; the returned index splits coda (``cluster[:i]``) from onset
    (``cluster[i:]``). An empty cluster returns ``0``.
    """
    if not cluster:
        return 0
    start = len(cluster) - 1  # the consonant adjacent to the nucleus is always onset
    i = start - 1
    while i >= 0 and cluster[i] < cluster[i + 1]:
        start = i
        i -= 1
    return start


def _has_pattern(part: SyllablePart | None) -> bool:
    """Whether *part* carries an onset/coda pattern."""
    return part is not None and part.pattern is not None


def _legal_constituent(
    segments: list[FeatureBundle], part: SyllablePart | None, letters: LetterInventory
) -> bool:
    """Whether a candidate onset/coda fully matches *part*'s pattern (None = unconstrained)."""
    if not _has_pattern(part):
        return True
    assert part is not None and part.pattern is not None
    return full_match(part.pattern, segments, letters)


def _split(
    levels: list[int],
    segments: list[FeatureBundle],
    onset_part: SyllablePart | None,
    coda_part: SyllablePart | None,
    letters: LetterInventory,
) -> tuple[int, bool]:
    """The onset-start index for an interior cluster, and whether sonority was a fallback.

    With an onset or coda pattern defined, every split point is a candidate and the
    longest pattern-legal onset wins — the patterns define legality, so sonority is
    not consulted (this is what lets a pattern license a non-sonority-rising onset).
    With no pattern, the sonority Maximal Onset division is used. When a pattern *is*
    defined but no split point is legal, this falls back to the sonority division (so
    the form still syllabifies) and returns ``True`` as the second element, letting the
    caller record a warning. The bool is ``False`` on the pattern and no-pattern paths.
    """
    if not (_has_pattern(onset_part) or _has_pattern(coda_part)):
        return _onset_start(levels), False
    for k in range(len(segments) + 1):  # k = 0 is the maximal (whole-cluster) onset
        if _legal_constituent(segments[k:], onset_part, letters) and _legal_constituent(
            segments[:k], coda_part, letters
        ):
            return k, False
    return _onset_start(levels), True  # no pattern-legal split → sonority fallback (flagged)


_syllabify_cache = IdentityCache(maxsize=8)
_parts_cache: dict[tuple[int, int | None], tuple[object, object, object]] = {}


def _parts_at(
    syllable_parts: SyllablePartsInventory, time: int | None
) -> tuple[object, object, object]:
    """The nucleus/onset/coda in force at *time* — the ONLY way *time* reaches the result.

    Memoized per (inventory, time) because ``get_part`` re-sorts the inventory's time keys on
    every call and syllabification asks three times per form.
    """
    key = (id(syllable_parts), time)
    parts = _parts_cache.get(key)
    if parts is None:
        parts = (
            syllable_parts.get_nucleus(time),
            syllable_parts.get_part(time, "onset"),
            syllable_parts.get_part(time, "coda"),
        )
        _parts_cache[key] = parts
    return parts


def syllabify(
    segments: list[FeatureBundle],
    sonorities: SonoritiesInventory,
    syllable_parts: SyllablePartsInventory,
    time: int | None,
    letters: LetterInventory | None = None,
    *,
    cache: bool = True,
) -> frozenset[int]:
    """Return the syllable-boundary positions of *segments* at *time*.

    Args:
        segments: The form to syllabify.
        sonorities: The sonority scale (first-match in file order).
        syllable_parts: Syllable-part constraints; supplies the nucleus definition
            and the optional onset/coda patterns.
        time: Derivation time, selecting the constraints in force.
        letters: Letter inventory, for letter shorthands inside onset/coda patterns.
        cache: Whether to memoize by identity of *segments*. A rule sweep re-syllabifies
            the same unchanged *segments* across every rule that doesn't fire, so caching
            (the default) skips that redundant work — safe wherever *segments* is treated
            as immutable. Pass ``False`` for a list that can recur under the same identity
            with different content (e.g. a directional scan's working form).

    A cluster the onset/coda patterns cannot divide falls back to the sonority split (see
    :func:`syllabification_fallbacks` to detect where that happened).
    """
    if not cache:
        return _syllabify_uncached(segments, sonorities, syllable_parts, time, letters)[0]
    letters_id = id(letters) if letters is not None else None
    # Keyed on the PARTS in force, not on `time` — and that is exact, not an optimisation that
    # assumes anything about the project. `time` reaches `_syllabify_uncached`'s result through
    # exactly three lookups (the nucleus, onset and coda in force) and through nothing else, so
    # (segments, sonorities, nucleus, onset, coda, letters) is the COMPLETE input set. A project
    # that redefines its parts mid-cascade simply resolves to different part objects at those
    # times and gets different entries, which is the correct behaviour, not a missed one.
    #
    # What this buys: keyed on the raw time, an unchanged form was re-syllabified at every new
    # timestamp even when the parts had not moved — 80 real syllabifications for a word that only
    # changes 15 times, because a rule sweep visits ~40 distinct times. Keyed on the parts, a
    # sweep of non-firing rules over an unchanged form costs one.
    nucleus, onset, coda = _parts_at(syllable_parts, time)
    extra = (id(sonorities), id(nucleus), id(onset), id(coda), letters_id)
    return _syllabify_cache.get_or_compute(
        segments,
        extra,
        lambda: _syllabify_uncached(segments, sonorities, syllable_parts, time, letters),
    )[0]


def syllabification_fallbacks(
    segments: list[FeatureBundle],
    sonorities: SonoritiesInventory,
    syllable_parts: SyllablePartsInventory,
    time: int | None,
    letters: LetterInventory | None = None,
) -> tuple[Fallback, ...]:
    """The clusters of *segments* whose division the patterns could not make at *time*.

    Each is the ``(start, end)`` span (a nucleus's cluster) that fell back to the sonority
    Maximal Onset split. Empty when nothing fell back. Recomputed from the same core as
    :func:`syllabify`, so the detection cannot drift from the split actually used.
    """
    return _syllabify_uncached(segments, sonorities, syllable_parts, time, letters)[1]


def _syllabify_uncached(
    segments: list[FeatureBundle],
    sonorities: SonoritiesInventory,
    syllable_parts: SyllablePartsInventory,
    time: int | None,
    letters: LetterInventory | None,
) -> tuple[frozenset[int], tuple[Fallback, ...]]:
    letters = letters if letters is not None else LetterInventory()
    nucleus_part = syllable_parts.get_nucleus(time)
    if nucleus_part is None or nucleus_part.definition is None:
        return frozenset(), ()

    nuclei = [i for i, seg in enumerate(segments) if pattern_matches(nucleus_part.definition, seg)]
    if not nuclei:
        return frozenset(), ()

    onset_part = syllable_parts.get_part(time, "onset")
    coda_part = syllable_parts.get_part(time, "coda")
    levels = [_sonority(seg, sonorities) for seg in segments]
    boundaries = {0, len(segments)}  # word edges are syllable edges
    fallbacks: list[Fallback] = []
    for left, right in zip(nuclei, nuclei[1:], strict=False):
        # A morpheme boundary in the cluster forces the split at its own position,
        # overriding sonority/MOP: material before it is the left syllable's coda, material
        # after it the right syllable's onset. (So ``at-a`` is ``at.a``, not ``a.ta``.)
        morpheme_splits = [j for j in range(left + 1, right) if is_morpheme_boundary(segments[j])]
        if morpheme_splits:
            boundaries.update(morpheme_splits)
            continue
        cluster_levels = levels[left + 1 : right]
        cluster_segs = segments[left + 1 : right]
        start, fell_back = _split(cluster_levels, cluster_segs, onset_part, coda_part, letters)
        boundaries.add(left + 1 + start)
        if fell_back:
            fallbacks.append((left + 1, right))
    return frozenset(boundaries), tuple(fallbacks)


def nuclei_by_position(
    segments: list[FeatureBundle],
    boundaries: frozenset[int],
    nucleus_definition: PatternBundle,
) -> list[FeatureBundle | None]:
    """For each segment position, the nucleus bundle of its syllable (or ``None``).

    This realises the ``Syllable.bundle`` *view*: a segment's syllable-tier features
    are those of its syllable's nucleus, so syllable-tier matching reads them here.
    Consecutive *boundaries* delimit each syllable; the nucleus is its first segment
    matching *nucleus_definition*. Positions in a syllable with no nucleus stay
    ``None`` (no syllable-tier info).
    """
    nuclei: list[FeatureBundle | None] = [None] * len(segments)
    for syllable in syllables(segments, boundaries, nucleus_definition):
        if syllable.nucleus is not None:
            for i in range(syllable.start, syllable.end):
                nuclei[i] = segments[syllable.nucleus]
    return nuclei


def consolidate_suprasegmentals(
    segments: list[FeatureBundle],
    boundaries: frozenset[int],
    nucleus_definition: PatternBundle,
    syllable_features: frozenset[str],
) -> list[FeatureBundle]:
    """Move each syllable's syllable-tier features onto its current nucleus.

    Suprasegmentals belong to the syllable, so when the nucleus shifts — e.g.
    u-epenthesis turns syllabic ``l̩`` into onset-vowel ``u`` + coda ``l``, stranding
    the stress on ``l`` — this gathers the syllable-tier features from every segment
    of the syllable onto its current nucleus and strips them from the rest. Run as
    part of resyllabification; segments are otherwise unchanged.

    This is **spatial**, not identity-tracking: a strand is reunited with the
    nucleus of whatever syllable that segment currently sits in. For epenthesis the
    strand stays co-syllabic with the new nucleus, so it is correct; but if a rule
    ever moved the carrying segment into a neighbouring syllable, the suprasegmental
    would follow to *that* syllable's nucleus. That is the defined behaviour of the
    no-cross-pass-identity design, not a bug.
    """
    if not syllable_features:
        return segments
    out = list(segments)
    for syllable in syllables(segments, boundaries, nucleus_definition):
        nucleus_pos = syllable.nucleus
        if nucleus_pos is None:
            continue
        span = range(syllable.start, syllable.end)
        # Pool the span's syllable-tier features (the nucleus's own values win).
        pooled: dict[str, FeatureSpec] = {}
        for i in span:
            if i == nucleus_pos:
                continue
            pooled.update({f: s for f, s in segments[i].items() if f in syllable_features})
        pooled.update({f: s for f, s in segments[nucleus_pos].items() if f in syllable_features})
        # Rebuild: nucleus = segmental + pooled suprasegmentals; others drop theirs.
        for i in span:
            segmental = {f: s for f, s in out[i].items() if f not in syllable_features}
            if i == nucleus_pos:
                out[i] = FeatureBundle({**segmental, **pooled})
            elif len(segmental) != len(out[i]):
                out[i] = FeatureBundle(segmental)
    return out
