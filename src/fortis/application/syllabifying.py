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
pattern-legal the cluster is unsyllabifiable and ``SyllabificationError`` is
raised rather than emitting an illegal division. Patterns apply only at the
interior split where there is a choice; word-edge onsets/codas are forced and not
checked.
"""
from __future__ import annotations

from src.fortis.application.matching import full_match, pattern_matches
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePart,
    SyllablePartsInventory,
)
from src.fortis.models.specs import FeatureSpec


class SyllabificationError(Exception):
    """No legal syllable division exists for a cluster under the onset/coda constraints."""


def _sonority(segment: FeatureBundle, sonorities: SonoritiesInventory) -> int:
    """The sonority level of *segment* by first-match; least sonorous if unmatched."""
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
) -> int:
    """The onset-start index for an interior cluster.

    With an onset or coda pattern defined, every split point is a candidate and the
    longest pattern-legal onset wins — the patterns define legality, so sonority is
    not consulted (this is what lets a pattern license a non-sonority-rising onset).
    With no pattern, the sonority Maximal Onset division is used. Raises
    ``SyllabificationError`` when a pattern admits no division.
    """
    if not (_has_pattern(onset_part) or _has_pattern(coda_part)):
        return _onset_start(levels)
    for k in range(len(segments) + 1):  # k = 0 is the maximal (whole-cluster) onset
        if _legal_constituent(segments[k:], onset_part, letters) and _legal_constituent(
            segments[:k], coda_part, letters
        ):
            return k
    raise SyllabificationError("no pattern-legal onset/coda division for an intervocalic cluster")


def syllabify(
    segments: list[FeatureBundle],
    sonorities: SonoritiesInventory,
    syllable_parts: SyllablePartsInventory,
    time: int,
    letters: LetterInventory | None = None,
) -> frozenset[int]:
    """Return the syllable-boundary positions of *segments* at *time*.

    Args:
        segments: The form to syllabify.
        sonorities: The sonority scale (first-match in file order).
        syllable_parts: Syllable-part constraints; supplies the nucleus definition
            and the optional onset/coda patterns.
        time: Derivation time, selecting the constraints in force.
        letters: Letter inventory, for letter shorthands inside onset/coda patterns.

    Raises:
        SyllabificationError: if an interior cluster admits no pattern-legal division.
    """
    letters = letters if letters is not None else LetterInventory()
    nucleus_part = syllable_parts.get_nucleus(time)
    if nucleus_part is None or nucleus_part.definition is None:
        return frozenset()

    nuclei = [i for i, seg in enumerate(segments) if pattern_matches(nucleus_part.definition, seg)]
    if not nuclei:
        return frozenset()

    onset_part = syllable_parts.get_part(time, "onset")
    coda_part = syllable_parts.get_part(time, "coda")
    levels = [_sonority(seg, sonorities) for seg in segments]
    boundaries = {0, len(segments)}  # word edges are syllable edges
    for left, right in zip(nuclei, nuclei[1:], strict=False):
        cluster_levels = levels[left + 1 : right]
        cluster_segs = segments[left + 1 : right]
        start = _split(cluster_levels, cluster_segs, onset_part, coda_part, letters)
        boundaries.add(left + 1 + start)
    return frozenset(boundaries)


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
    edges = sorted(set(boundaries) | {0, len(segments)})
    for left, right in zip(edges, edges[1:], strict=False):
        nucleus: FeatureBundle | None = None
        for i in range(left, right):
            if pattern_matches(nucleus_definition, segments[i]):
                nucleus = segments[i]
                break
        if nucleus is not None:
            for i in range(left, right):
                nuclei[i] = nucleus
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
    edges = sorted(boundaries | {0, len(segments)})
    for left, right in zip(edges, edges[1:], strict=False):
        nucleus_pos: int | None = None
        for i in range(left, right):
            if pattern_matches(nucleus_definition, segments[i]):
                nucleus_pos = i
                break
        if nucleus_pos is None:
            continue
        # Pool the span's syllable-tier features (the nucleus's own values win).
        pooled: dict[str, FeatureSpec] = {}
        for i in range(left, right):
            if i == nucleus_pos:
                continue
            pooled.update({f: s for f, s in segments[i].items() if f in syllable_features})
        pooled.update({f: s for f, s in segments[nucleus_pos].items() if f in syllable_features})
        # Rebuild: nucleus = segmental + pooled suprasegmentals; others drop theirs.
        for i in range(left, right):
            segmental = {f: s for f, s in out[i].items() if f not in syllable_features}
            if i == nucleus_pos:
                out[i] = FeatureBundle({**segmental, **pooled})
            elif len(segmental) != len(out[i]):
                out[i] = FeatureBundle(segmental)
    return out
