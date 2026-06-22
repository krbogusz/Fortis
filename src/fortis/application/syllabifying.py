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

Onset/coda **constraints** from ``syllable_parts`` (per-segment ``required`` /
``forbidden`` predicates) narrow the choice. Sonority remains a hard filter: the
candidates are the sonority-rising onsets (suffixes of the maximal rising onset,
i.e. progressively shorter onsets with more in the coda); among those whose onset
and coda satisfy the constraints, the longest onset wins. With no constraints
this is exactly the Maximal Onset division. If no candidate is legal, the cluster
is unsyllabifiable and ``SyllabificationError`` is raised rather than emitting a
constraint-violating division. Constraints apply only at the interior split where
there is a choice; word-edge onsets/codas are forced and not constraint-checked.
"""

from src.fortis.application.combining import matches_exactly
from src.fortis.application.matching import pattern_matches
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePart,
    SyllablePartsInventory,
)


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


def _legal(segments: list[FeatureBundle], part: SyllablePart | None) -> bool:
    """Whether every segment satisfies *part*'s required/forbidden predicates."""
    if part is None:
        return True
    for segment in segments:
        if part.required is not None and not pattern_matches(part.required, segment):
            return False
        if part.forbidden is not None and pattern_matches(part.forbidden, segment):
            return False
    return True


def _split(
    levels: list[int],
    segments: list[FeatureBundle],
    onset_part: SyllablePart | None,
    coda_part: SyllablePart | None,
) -> int:
    """The onset-start index for an interior cluster, narrowing sonority by constraints.

    Candidates are the sonority-rising onsets — ``segments[k:]`` for ``k`` from the
    maximal rising onset down to the empty onset — and the longest legal one wins.
    Raises ``SyllabificationError`` if none is legal.
    """
    for k in range(_onset_start(levels), len(segments) + 1):
        if _legal(segments[k:], onset_part) and _legal(segments[:k], coda_part):
            return k
    raise SyllabificationError(
        "no legal onset/coda division for an intervocalic cluster"
    )


def syllabify(
    segments: list[FeatureBundle],
    sonorities: SonoritiesInventory,
    syllable_parts: SyllablePartsInventory,
    time: int,
) -> frozenset[int]:
    """Return the syllable-boundary positions of *segments* at *time*.

    Args:
        segments: The form to syllabify.
        sonorities: The sonority scale (first-match in file order).
        syllable_parts: Syllable-part constraints; supplies the nucleus definition
            and the optional onset/coda phonotactic predicates.
        time: Derivation time, selecting the constraints in force.

    Raises:
        SyllabificationError: if an interior cluster admits no constraint-legal
            division.
    """
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
        boundaries.add(left + 1 + _split(cluster_levels, cluster_segs, onset_part, coda_part))
    return frozenset(boundaries)


def render_syllabified(
    segments: list[FeatureBundle],
    boundaries: frozenset[int],
    letters: LetterInventory,
) -> str:
    """Render *segments* as a string with ``.`` at each interior syllable boundary.

    Each segment is shown as the letter whose bundle matches it exactly, or ``?``
    if none does. This is a minimal syllable-aware view for traces and tests — full
    IPA rendering (diacritics, partial matches) is the separate rendering milestone.
    """
    interior = boundaries - {0, len(segments)}
    out: list[str] = []
    for i, segment in enumerate(segments):
        if i in interior:
            out.append(".")
        out.append(_symbol(segment, letters))
    return "".join(out)


def _symbol(segment: FeatureBundle, letters: LetterInventory) -> str:
    """The letter whose bundle exactly matches *segment*, or ``?`` if none does."""
    for symbol, letter in letters.items():
        if matches_exactly(letter.bundle, segment):
            return symbol
    return "?"
