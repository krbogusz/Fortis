from __future__ import annotations

from collections.abc import Mapping

from src.fortis.application.combining import differing, matches_exactly
from src.fortis.application.syllabifying import syllabify, syllables
from src.fortis.general.utils import IdentityCache
from src.fortis.models.bundles import FeatureBundle, is_morpheme_boundary
from src.fortis.models.inventories import Diacritic, DiacriticKind
from src.fortis.models.project import Project
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.tiers import Tier


def sequence_to_string(sequence: list[FeatureBundle], inventories: Project) -> str:
    """Turn a sequence of FeatureBundles back into an IPA string.

    Each segment renders as a letter plus diacritics (exact letter match if there
    is one; otherwise the letter whose remaining differences the fewest diacritics
    cover). Suprasegmental (syllable-tier) marks are positioned per syllable: a
    before-kind mark like stress ``ˈ`` at the syllable's left edge, a combining/
    after-kind mark like tone on the nucleus — so a stressed word round-trips as
    ``ˈseχmoː``, not ``sˈeχmoː``. To do that the sequence is syllabified; when it
    has no nucleus, it falls back to a flat per-segment render with no repositioning.
    """
    boundaries = syllabify(
        sequence,
        inventories.sonorities,
        inventories.syllable_parts,
        inventories.time,
        inventories.letters,
    )
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


_syllable_features_cache = IdentityCache(maxsize=8)  # see render_syllabified


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
    features; those (tone, stress) are positioned per syllable instead by attachment
    kind: before-kind marks (e.g. stress ``ˈ``) at the syllable's left edge,
    combining marks on the nucleus that carries them, and after-kind marks (e.g.
    tone letters) at the syllable's right edge. So ``ˈxenti`` surfaces as ``ˈxen.ti``
    (stress at the syllable onset), and a toned ``san`` as ``san˥`` (tone after the
    coda), not ``sa˥n``.

    A before-mark whose diacritic ``marks_boundary`` (e.g. stress ``ˈ``) *is* the
    syllable boundary, so it replaces the ``.`` there: ``kumˈtom``, not ``kum.ˈtom``.

    With ``dots=False`` the interior boundary dots are omitted but the suprasegmental
    repositioning is kept — used by ``sequence_to_string`` for a flat, re-segmentable
    string that still places stress/tone correctly.
    """
    # Fixed for the run's feature inventory; cached by its identity (hot: every
    # trace line, report row, and CSV cell renders through here).
    syllable_features = _syllable_features_cache.get_or_compute(
        inventories.features,
        None,
        lambda: frozenset(
            name for name, feature in inventories.features.items() if feature.tier == Tier.syllable
        ),
    )
    all_diacritics = inventories.diacritics
    nucleus_part = inventories.syllable_parts.get_nucleus(inventories.time)
    nucleus = nucleus_part.definition if nucleus_part is not None else None
    interior = boundaries - {0, len(sequence)}
    parts: list[str] = []
    for syllable in syllables(sequence, boundaries, nucleus):
        # The syllable's suprasegmentals live on its nucleus; split its marks by attachment kind.
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        carrier = syllable.nucleus
        if carrier is not None:
            present = {f for f in sequence[carrier] if f in syllable_features}
            if present:
                bundle = sequence[carrier]
                _find_diacritics(bundle, present, all_diacritics, before, combining, after)
        # A boundary-marking before-mark stands in for the "." at an interior edge; so does a
        # morpheme boundary starting the syllable (``at-a``, not ``at-.a`` / ``at.-a``).
        marks_boundary = any(inventories.diacritics[s].marks_boundary for s in before)
        starts_with_boundary = is_morpheme_boundary(sequence[syllable.start])
        if dots and syllable.start in interior and not marks_boundary and not starts_with_boundary:
            parts.append(".")
        parts.append("".join(before))  # syllable-initial marks (e.g. stress)
        for i in range(syllable.start, syllable.end):
            parts.append(render_segment(sequence[i], inventories, syllable_features))
            if i == carrier:
                parts.append("".join(combining))  # combining marks sit on the nucleus
        parts.append("".join(after))  # syllable-final marks (e.g. tone letters): san˥, not sa˥n
    return "".join(parts)


_render_segment_cache: dict[tuple[int, frozenset[tuple[str, object]], frozenset[str]], str] = {}
_residue_cache: dict[
    tuple[int, frozenset[tuple[str, object]], frozenset[str]], frozenset[str]
] = {}


def render_segment(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str] = frozenset()
) -> str:
    """Render a single FeatureBundle as an IPA string (letter + diacritics).

    Features named in *exclude* are ignored — used by ``render_syllabified`` to
    render a segment without its syllable-tier features, which it positions itself.

    The engine re-renders the same handful of realized segments over and over — one
    word's derivation revisits the same phoneme at every step where it didn't change,
    and the same phonemes recur across words. Cached by *value* (segment's features,
    ``exclude``, and identity of ``inventories``), unlike the identity caches elsewhere
    in the engine: a rendered segment is closed-over pattern-free data, so equal content
    always renders the same, and the realized segments in play are a small, bounded set
    (unlike the transient ``Form``s those other caches guard against unbounded growth for).
    """
    if is_morpheme_boundary(segment):
        return "-"  # a morpheme boundary renders as its own symbol, never as a letter
    key = (id(inventories), frozenset((f, spec.value) for f, spec in segment.items()), exclude)
    cached = _render_segment_cache.get(key)
    if cached is not None:
        return cached
    result = _render_segment_uncached(segment, inventories, exclude)
    _render_segment_cache[key] = result
    return result


def render_nearest(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str] = frozenset()
) -> str:
    """The closest spelling for *segment* — what it ALMOST is, even when it renders as ``�``.

    For a segment the inventory can spell this is just its rendering. For one it cannot, this
    is the near-miss: the letter it is one or two features away from, and therefore the letter
    it will be mistaken for. That is the useful half of the diagnostic — "renders as � (nearest
    ``ɑ``), dropping ``labial``" tells you both that something is wrong and where to look.
    """
    return _best_fit(segment, inventories, exclude)[2]


def render_residue(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str] = frozenset()
) -> frozenset[str]:
    """The features *segment* carries that its rendered symbol cannot express.

    Empty when the rendering is faithful — the segment IS some letter (plus diacritics that
    spell every difference). Non-empty means the renderer fell back to the nearest letter and
    **silently dropped** these features: the symbol you read is not the segment you have.

    That gap is the engine's one genuinely invisible failure mode, because rendering and
    matching disagree about it. Rendering is lossy and many-to-one (nearest letter wins);
    ``_letter_matches`` is exact identity. So a bundle one feature away from ``ɑ`` still
    *prints* ``ɑ`` while no rule written ``ɑ → …`` will ever match it — it fires on some words
    and passes silently over identical-looking others, with no error anywhere.

    The usual cause is a rule whose merge changed a segment's quality but left a feature of the
    old quality behind: a merge keeps every feature it does not mention, so un-rounding *o with
    ``rounded: none`` and forgetting ``labial: none`` yields an ``ɑ`` that is still labial.

    Cached by value alongside ``render_segment``, and for the same reason: the warning pass asks
    this of every segment of every step of every derivation, which is the same small, bounded set
    of realized segments over and over.
    """
    if is_morpheme_boundary(segment):
        return frozenset()
    key = (id(inventories), frozenset((f, spec.value) for f, spec in segment.items()), exclude)
    cached = _residue_cache.get(key)
    if cached is None:
        cached = _best_fit(segment, inventories, exclude)[1]
        _residue_cache[key] = cached
    return cached


def _render_segment_uncached(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str]
) -> str:
    return _best_fit(segment, inventories, exclude)[0]


def _best_fit(
    segment: FeatureBundle, inventories: Project, exclude: frozenset[str]
) -> tuple[str, frozenset[str], str]:
    """The rendering, the features it could not express, and the nearest spelling.

    The rendering is ``�`` whenever the residue is non-empty; the nearest spelling is the
    best-fit letter regardless, so a caller can report what the segment will be MISTAKEN for.
    """
    if exclude:
        segment = FeatureBundle({f: spec for f, spec in segment.items() if f not in exclude})
    # 1. Try exact match first
    for letter_symbol, letter_def in inventories.letters.items():
        if matches_exactly(segment, letter_def.bundle):
            return letter_symbol, frozenset(), letter_symbol

    # 2. Find the best letter: the one whose differences leave the
    #    fewest remaining features after applying diacritics.
    #    Break ties by fewest total differences.
    best_symbol = None
    best_remaining = float("inf")
    best_total_diffs = float("inf")
    best_left: frozenset[str] = frozenset()
    best_diacritics: tuple[list[str], list[str], list[str]] | None = None

    # All diacritics, segment- and syllable-tier: a segment carrying syllable-tier
    # features (a nucleus, where suprasegmentals live) gets its tone/stress marks;
    # non-nuclei have no syllable-tier features, so syllable-tier diacritics never fit.
    all_diacritics = inventories.diacritics
    # A plain dict, built once: every letter below re-runs the same fit-checks against
    # this unchanged segment, and a native dict.get beats FeatureBundle's Mapping-mixin
    # __contains__/__getitem__ pair on a loop this hot.
    target = dict(segment)

    for letter_symbol, letter_def in inventories.letters.items():
        total_diffs = differing(segment, letter_def.bundle)
        remaining = set(total_diffs)
        before: list[str] = []
        combining: list[str] = []
        after: list[str] = []
        _find_diacritics(target, remaining, all_diacritics, before, combining, after)

        if (len(remaining) < best_remaining) or (
            len(remaining) == best_remaining and len(total_diffs) < best_total_diffs
        ):
            best_symbol = letter_symbol
            best_remaining = len(remaining)
            best_total_diffs = len(total_diffs)
            best_left = frozenset(remaining)
            best_diacritics = (before, combining, after)

    if best_symbol is None or best_diacritics is None:
        return "�", frozenset(segment.data), "�"

    # A segment the inventory cannot spell renders as �, NOT as the nearest letter. It used to
    # fall back to the closest fit and quietly drop whatever features that letter could not
    # express, which made the one failure the engine cannot otherwise show you invisible: the
    # symbol in the trace was not the segment being held. Worse, it was a *plausible* symbol —
    # an ɑ one feature away from the letter ɑ printed as ɑ, while no rule written `ɑ → …` would
    # ever match it, because letter patterns match by exact identity. The rule fired on some
    # words and passed silently over identical-looking others.
    #
    # So say so. � is loud, it survives into every report and the accuracy score, and
    # `render_residue` names the missing features and the rule that produced them (warnings.md).
    before, combining, after = best_diacritics
    nearest = "".join(before) + best_symbol + "".join(combining) + "".join(after)
    if best_left:
        return "�", best_left, nearest
    return nearest, best_left, nearest


def _bucket_for(
    kind: DiacriticKind, before: list[str], combining: list[str], after: list[str]
) -> list[str]:
    """The output list a diacritic of *kind* appends to (before / combining / after)."""
    if kind == DiacriticKind.before:
        return before
    if kind == DiacriticKind.combining:
        return combining
    return after


_DiacriticEntry = tuple[str, Diacritic, frozenset[str], tuple[tuple[str, object], ...]]
_diacritic_entries_cache = IdentityCache(maxsize=8)


def _diacritic_entries(diacritics: Mapping[str, Diacritic]) -> tuple[_DiacriticEntry, ...]:
    """A precomputed, cached view of the eligible (non-read-only) diacritics.

    ``_find_diacritics`` re-scans every diacritic on every greedy round, for every
    candidate letter, for every segment rendered — but a diacritic's own feature set
    and (feature, value) pairs never change across those calls, so re-deriving them
    from *diacritics* (a ``Mapping``, walked through the slow generic ``KeysView``/
    ``ItemsView`` machinery) on each round was pure waste. Cached by identity of
    *diacritics*, which is one long-lived inventory shared by the whole run.
    """
    return _diacritic_entries_cache.get_or_compute(
        diacritics,
        None,
        lambda: tuple(
            (
                symbol,
                dia_def,
                frozenset(dia_def.bundle.keys()),
                tuple((feature, value.value) for feature, value in dia_def.bundle.items()),
            )
            for symbol, dia_def in diacritics.items()
            if not dia_def.read_only and dia_def.bundle  # input-only alias, or no features to give
        ),
    )


def _find_diacritics(
    target: Mapping[str, FeatureSpec],
    remaining_diffs: set[str],
    diacritics: Mapping[str, Diacritic],
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
    entries = _diacritic_entries(diacritics)
    while remaining_diffs:
        best_symbol: str | None = None
        best_def: Diacritic | None = None
        best_features: frozenset[str] = frozenset()
        best_coverage = 0

        for dia_symbol, dia_def, dia_features, dia_items in entries:
            # Every feature in the diacritic must hold in the target with the same
            # value (otherwise the diacritic would create a new difference or express
            # the wrong value). A feature absent from the target is unspecified —
            # equivalent to None — matching how patterns treat absence elsewhere.
            fits = True
            for feature, value in dia_items:
                spec = target.get(feature)
                if (spec.value if spec is not None else None) != value:
                    fits = False
                    break
            if not fits:
                continue

            # At least one feature must still be needed; prefer the diacritic covering the most.
            coverage = len(dia_features & remaining_diffs)
            if coverage > best_coverage:
                best_symbol = dia_symbol
                best_def = dia_def
                best_features = dia_features
                best_coverage = coverage

        if best_def is None or best_symbol is None:
            # No exact diacritic — but a contour (tuple) value can still render as a
            # sequence of its levels' contour diacritics (e.g. tone (2,1,4) → ˨˩˦).
            if _render_contour(target, remaining_diffs, diacritics, before, combining, after):
                continue
            break

        remaining_diffs -= best_features
        _bucket_for(best_def.kind, before, combining, after).append(best_symbol)


def _render_contour(
    target: Mapping[str, FeatureSpec],
    remaining_diffs: set[str],
    diacritics: Mapping[str, Diacritic],
    before: list[str],
    combining: list[str],
    after: list[str],
) -> bool:
    """Render one remaining contour-valued feature as a sequence of its levels.

    A feature whose value is a contour (a tuple, e.g. a tone ``(2, 1, 4)``) usually
    has no single diacritic. Instead each level is written with the ``contour=true``
    diacritic carrying that single value, in order (˨ ˩ ˦ → ``˨˩˦``) — the output
    counterpart of combining tone letters into a contour on input. Returns ``True``
    if a contour feature was rendered (and removed from *remaining_diffs*); ``False``
    if none could be (so the caller stops). Tried only after exact-match diacritics,
    so a contour with its own single diacritic still uses that.
    """
    for feature in list(remaining_diffs):
        spec = target.get(feature)
        if spec is None or not isinstance(spec.value, tuple):
            continue
        sequence: list[tuple[str, Diacritic]] = []
        for level in spec.value:
            match = next(
                (
                    (symbol, dia)
                    for symbol, dia in diacritics.items()
                    if dia.contour
                    and not dia.read_only
                    and set(dia.bundle.keys()) == {feature}
                    and dia.bundle[feature].value == level
                ),
                None,
            )
            if match is None:
                break
            sequence.append(match)
        else:  # every level found a contour diacritic
            for symbol, dia in sequence:
                _bucket_for(dia.kind, before, combining, after).append(symbol)
            remaining_diffs.discard(feature)
            return True
    return False
