from __future__ import annotations

from src.fortis.application.combining import differing, matches_exactly
from src.fortis.application.syllabifying import SyllabificationError, syllabify
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.inventories import Diacritic, DiacriticKind
from src.fortis.models.project import Project
from src.fortis.models.tiers import Tier


def sequence_to_string(sequence: list[FeatureBundle], inventories: Project) -> str:
    """Turn a sequence of FeatureBundles back into an IPA string.

    Each segment renders as a letter plus diacritics (exact letter match if there
    is one; otherwise the letter whose remaining differences the fewest diacritics
    cover). Suprasegmental (syllable-tier) marks are positioned per syllable: a
    before-kind mark like stress ``ˈ`` at the syllable's left edge, a combining/
    after-kind mark like tone on the nucleus — so a stressed word round-trips as
    ``ˈseχmoː``, not ``sˈeχmoː``. To do that the sequence is syllabified; when it
    has no nucleus or no legal division (e.g. a bare cluster), it falls back to a
    flat per-segment render with no repositioning.
    """
    try:
        boundaries = syllabify(
            sequence,
            inventories.sonorities,
            inventories.syllable_parts,
            inventories.time,
            inventories.letters,
        )
    except SyllabificationError:
        boundaries = frozenset()
    if boundaries:
        return render_syllabified(sequence, boundaries, inventories, dots=False)
    return "".join(render_segment(segment, inventories) for segment in sequence)


def describe_change(
    before: list[FeatureBundle], after: list[FeatureBundle], inventories: Project
) -> str:
    """A human-readable IPA summary of how *before* became *after*.

    For an equal-length change, the segments that actually changed are shown as
    ``old→new`` (e.g. ``kʲ→k``). For a length change (insertion, deletion,
    coalescence) the common prefix and suffix are trimmed and only the differing
    region is shown (e.g. ``m̩→um``; an empty side is ``∅``).
    """
    if len(before) == len(after):
        changed = [
            f"{render_segment(b, inventories)}→{render_segment(a, inventories)}"
            for b, a in zip(before, after, strict=True)
            if not matches_exactly(b, a)
        ]
        return ", ".join(changed)

    before_mid, after_mid = _trim_common(before, after)
    return f"{_render_or_null(before_mid, inventories)}→{_render_or_null(after_mid, inventories)}"


def _trim_common(
    before: list[FeatureBundle], after: list[FeatureBundle]
) -> tuple[list[FeatureBundle], list[FeatureBundle]]:
    """Strip the shared leading/trailing segments, leaving just the differing region."""
    head = 0
    while head < len(before) and head < len(after) and matches_exactly(before[head], after[head]):
        head += 1
    tail = 0
    while (
        tail < len(before) - head
        and tail < len(after) - head
        and matches_exactly(before[-1 - tail], after[-1 - tail])
    ):
        tail += 1
    return before[head : len(before) - tail], after[head : len(after) - tail]


def _render_or_null(sequence: list[FeatureBundle], inventories: Project) -> str:
    """Render *sequence*, or ``∅`` if it is empty (a fully deleted/inserted side)."""
    return sequence_to_string(sequence, inventories) if sequence else "∅"


def render_syllabified(
    sequence: list[FeatureBundle],
    boundaries: frozenset[int],
    inventories: Project,
    dots: bool = True,
) -> str:
    """Render *sequence* as IPA with ``.`` at each interior syllable boundary.

    Segments render through ``render_segment`` *without* their syllable-tier
    features; those (tone, stress) are positioned per syllable instead: before-kind
    marks (e.g. stress ``ˈ``) at the syllable's left edge, combining/after-kind
    (e.g. tone) on the nucleus that carries them. So ``ˈxenti`` surfaces as
    ``ˈxen.ti`` (stress at the syllable onset), not ``xˈen.ti``.

    A before-mark whose diacritic ``marks_boundary`` (e.g. stress ``ˈ``) *is* the
    syllable boundary, so it replaces the ``.`` there: ``kumˈtom``, not ``kum.ˈtom``.

    With ``dots=False`` the interior boundary dots are omitted but the suprasegmental
    repositioning is kept — used by ``sequence_to_string`` for a flat, re-segmentable
    string that still places stress/tone correctly.
    """
    syllable_features = frozenset(
        name for name, feature in inventories.features.items() if feature.tier == Tier.syllable
    )
    all_diacritics = dict(inventories.diacritics)
    interior = boundaries - {0, len(sequence)}
    edges = sorted(boundaries | {0, len(sequence)})
    parts: list[str] = []
    for left, right in zip(edges, edges[1:], strict=False):
        # The syllable's suprasegmentals live on its nucleus — the segment in the
        # span carrying syllable-tier features. Split its marks by attachment kind.
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        carrier: int | None = None
        for i in range(left, right):
            present = {f for f in sequence[i] if f in syllable_features}
            if present:
                _find_diacritics(sequence[i], present, all_diacritics, before, combining, after)
                carrier = i
                break
        # A boundary-marking before-mark stands in for the "." at an interior edge.
        marks_boundary = any(inventories.diacritics[s].marks_boundary for s in before)
        if dots and left in interior and not marks_boundary:
            parts.append(".")
        parts.append("".join(before))  # syllable-initial marks (e.g. stress)
        for i in range(left, right):
            parts.append(render_segment(sequence[i], inventories, syllable_features))
            if i == carrier:
                parts.append("".join(combining) + "".join(after))  # nucleus marks (e.g. tone)
    return "".join(parts)


def render_segment(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str] = frozenset()
) -> str:
    """Render a single FeatureBundle as an IPA string (letter + diacritics).

    Features named in *exclude* are ignored — used by ``render_syllabified`` to
    render a segment without its syllable-tier features, which it positions itself.
    """
    if exclude:
        segment = FeatureBundle({f: spec for f, spec in segment.items() if f not in exclude})
    # 1. Try exact match first
    for letter_symbol, letter_def in inventories.letters.items():
        if matches_exactly(segment, letter_def.bundle):
            return letter_symbol

    # 2. Find the best letter: the one whose differences leave the
    #    fewest remaining features after applying diacritics.
    #    Break ties by fewest total differences.
    best_symbol = None
    best_remaining = float("inf")
    best_total_diffs = float("inf")
    best_diacritics: tuple[list[str], list[str], list[str]] | None = None

    # All diacritics, segment- and syllable-tier: a segment carrying syllable-tier
    # features (a nucleus, where suprasegmentals live) gets its tone/stress marks;
    # non-nuclei have no syllable-tier features, so syllable-tier diacritics never fit.
    all_diacritics = dict(inventories.diacritics)

    for letter_symbol, letter_def in inventories.letters.items():
        total_diffs = differing(segment, letter_def.bundle)
        remaining = set(total_diffs)
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(segment, remaining, all_diacritics, before, combining, after)

        if (len(remaining) < best_remaining) or (
            len(remaining) == best_remaining and len(total_diffs) < best_total_diffs
        ):
            best_symbol = letter_symbol
            best_remaining = len(remaining)
            best_total_diffs = len(total_diffs)
            best_diacritics = (before, combining, after)

    if best_symbol is None:
        return "�"

    if best_diacritics is None:
        return "�"

    before, combining, after = best_diacritics
    return "".join(before) + best_symbol + "".join(combining) + "".join(after)


def _find_diacritics(
    target_bundle: FeatureBundle,
    remaining_diffs: set[str],
    diacritics: dict[str, Diacritic],
    before: list[str],
    combining: list[str],
    after: list[str],
) -> None:
    """Greedily find diacritics that cover the remaining feature differences.

    Each iteration picks the diacritic that covers the most remaining
    differences. A diacritic fits when all of its features exist in the
    target bundle with matching values. The search repeats until no
    diacritic can fill any remaining gap.
    """
    while remaining_diffs:
        best_symbol: str | None = None
        best_def: Diacritic | None = None
        best_coverage = 0

        for dia_symbol, dia_def in diacritics.items():
            dia_features = set(dia_def.bundle.keys())
            if not dia_features:
                continue

            # Every feature in the diacritic must exist in the target
            # with the same value (otherwise the diacritic would create
            # a new difference or express the wrong value).
            fits = True
            for feature, value in dia_def.bundle.items():
                if feature not in target_bundle or value.value != target_bundle[feature].value:
                    fits = False
                    break
            if not fits:
                continue

            # At least one feature must still be needed
            coverage = len(dia_features & remaining_diffs)
            if coverage == 0:
                continue

            # Prefer diacritics that cover more remaining differences;
            # break ties by preferring default diacritics
            if coverage > best_coverage or (
                coverage == best_coverage
                and best_def is not None
                and dia_def.default
                and not best_def.default
            ):
                best_symbol = dia_symbol
                best_def = dia_def
                best_coverage = coverage

        if best_def is None or best_symbol is None:
            # No diacritic can fill any remaining gap — stop
            break

        remaining_diffs -= set(best_def.bundle.keys())
        if best_def.kind == DiacriticKind.before:
            before.append(best_symbol)
        elif best_def.kind == DiacriticKind.combining:
            combining.append(best_symbol)
        else:
            after.append(best_symbol)
