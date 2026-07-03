"""Derivation driver: sweep a word through every rule, recording what fired.

``apply_rule`` applies one rule to a form (``list[FeatureBundle]``) according to
its application mode; ``derive`` runs the whole rule set in chronological order
and returns the per-word ``Derivation`` trace.

The mode *is* the sweep — a rule is applied in exactly one pass, never iterated
to a fixpoint (§6.2):

* **simultaneous** — every locus is found against the original form, then all
  rewrites are spliced at once; no application sees another's output. Overlapping
  loci within the rule are resolved leftmost-longest non-overlapping (the matcher
  already yields one longest match per start, ascending; §6.3's "undefined
  interaction" governs overlapping *rules*, not loci within one rule).
* **left_to_right** — scan rewriting in place, each output immediately visible;
  the cursor advances past the rewritten *output* (Kaplan & Kay obligatory
  rewrite), so a changed segment can feed a later locus.
* **right_to_left** — the mirror image.

Directional passes terminate for deletion (the form shrinks) and feature change
(the cursor strictly advances past the output). The one shape that would not is a
self-feeding rightward epenthesis (e.g. ``∅ -> x / x _`` under left_to_right),
which inserts past its own advancing cursor without bound; such rules are outside
the realistic diachronic rule set and carry no iteration cap.

The form is threaded through every rule whether or not it fires; only rules that
change the form contribute a ``DerivationStep`` (its before/after forms and boundaries).
The human-readable change summary shown per step is formatted in the presentation layer
and is cosmetic: derivation correctness never depends on it.

Syllabification (§7): each rule (re)syllabifies the current form for its match
pass, using the ``SyllablePartsInventory`` constraints in force at the rule's
``time`` — so the input is syllabified before the first rule and the structure is
refreshed after every rule. This is what makes the ``$`` boundary assertion
matchable; with no ``sonorities``/``syllable_parts`` supplied there are no
boundaries and ``$`` simply never matches. (No rule in the current set uses
``$``, so this integration is presently preparatory — it changes no derivation
output, only enables ``$``-conditioned rules.)
"""
from __future__ import annotations

from dataclasses import replace

from src.fortis.application.applying import apply_match
from src.fortis.application.combining import matches_exactly
from src.fortis.application.matching import Match, SyllableView, find_matches, pattern_matches
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.syllabifying import (
    SyllabificationError,
    nuclei_by_position,
    syllabify,
)
from src.fortis.application.tiers import (
    cleanup_tiers,
    lower_tiers,
    redock_to_nuclei,
    split_carried,
    write_to_tier,
)
from src.fortis.general.utils import IdentityCache
from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.elements import (
    Bound,
    Disjunction,
    Element,
    Group,
    LetterBundle,
    LetterRef,
    Negated,
    Quantified,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.models.form import Form
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    Word,
)
from src.fortis.models.project import Project
from src.fortis.models.rules import (
    ApplicationMode,
    Rule,
    RuleInventory,
    StructuralDescription,
)
from src.fortis.models.segment import Segment
from src.fortis.models.tier_declaration import TierInventory
from src.fortis.models.tiers import Tier
from src.fortis.models.values import AutosegRecall

_derivation_geometry_cache = IdentityCache(maxsize=8)


def _syllable_features(features: FeatureInventory) -> frozenset[str]:
    """The names of the syllable-tier features (tone, stress, …).

    Pure function of *features* — the same ``FeatureInventory`` recurs across every
    rule application in a derivation run, so cached by its identity (see
    ``_node_descendants``, which shares this reasoning and this cache).
    """
    return _derivation_geometry_cache.get_or_compute(
        features,
        "syllable_features",
        lambda: frozenset(
            name for name, feature in features.items() if feature.tier == Tier.syllable
        ),
    )


def _node_descendants(features: FeatureInventory) -> dict[str, frozenset[str]]:
    """Each segmental feature → its descendant names, for node-spread capture (`oral: ~n`).

    Every segmental feature is included, not only those with children: a childless leaf like
    ``back`` maps to an empty set, so ``[back: ~n]`` spreads the feature itself (vowel harmony).

    Called once per rule application (``apply_rule``/``_apply_directional``) with the same
    *features* every time — the feature geometry is fixed for the whole run — so it's cached
    by identity of *features* rather than re-walking the descendant tree on every call.
    """
    return _derivation_geometry_cache.get_or_compute(
        features, "node_descendants", lambda: _node_descendants_uncached(features)
    )


def _node_descendants_uncached(features: FeatureInventory) -> dict[str, frozenset[str]]:
    return {
        name: frozenset(features.descendants(name))
        for name in features
        if features.is_segmental(name)
    }


def _resolve_elements(
    elements: tuple[Element, ...], project: Project, rule_id: str
) -> tuple[Element, ...]:
    """Replace each non-letter ``LetterRef`` run with its segmented ``LetterBundle``s.

    A run of letters and diacritics the parser kept as a single ``LetterRef`` (e.g.
    ``ʁʷ`` — one segment — or ``au`` — two) is sent through the segmenter and
    spliced in as one ``LetterBundle`` per segment, so it behaves like the segments
    it spells. A plain single letter is left as a ``LetterRef`` (still resolved
    against the inventory). Recurses into all nesting; a multi-segment run nested
    under a quantifier/binding/negation is wrapped in a ``Group`` to stay one inner.

    A literal's syllable-tier diacritics (``ˈ``/``ˌ`` stress, tone marks) are lowered
    onto the resolved bundle on **every** side, so the same ``ˌe`` carries
    ``stress: secondary``. What that value *does* depends on the side, downstream: in
    the target/contexts/exceptions it *constrains* the match (``ˌɔ`` matches only a
    secondary-stressed ɔ); in the result it *writes*, replacing the suprasegmental of
    the changed segment's syllable (``ˌa → ˈa`` promotes secondary to primary — see
    ``_carry_stranded_suprasegmentals``). A result literal with no mark carries no
    syllable feature, so the syllable's stress simply persists.

    A syllable-tier mark only lands on a nucleus: ``string_to_sequence`` attaches it to the
    literal's nucleus, so a mark on a non-nucleus result literal (``d → ˈt``) has nothing to
    attach to and is dropped — write the mark on the syllable's vowel instead.
    """

    def _segments(symbol: str) -> list:
        return lower_tiers(string_to_sequence(symbol, project))

    resolved: list[Element] = []
    for element in elements:
        match element:
            case LetterRef(symbol) if symbol not in project.letters:
                segments = _segments(symbol)
                if not segments:
                    raise ValueError(
                        f"rule '{rule_id}': letter reference '{symbol}' resolves to no "
                        "segment — it is not a known letter or letter+diacritic sequence"
                    )
                resolved.extend(LetterBundle(bundle=segment) for segment in segments)
            case Group(inner):
                resolved.append(Group(_resolve_elements(inner, project, rule_id)))
            case Disjunction(branches):
                resolved.append(
                    Disjunction(tuple(_resolve_elements(b, project, rule_id) for b in branches))
                )
            case Negated(inner):
                resolved.append(Negated(_resolve_one(inner, project, rule_id)))
            case Quantified(inner, quant):
                resolved.append(Quantified(_resolve_one(inner, project, rule_id), quant))
            case Bound(ref, inner):
                resolved.append(Bound(ref, _resolve_one(inner, project, rule_id)))
            case _:
                resolved.append(element)
    return tuple(resolved)


def _resolve_one(element: Element, project: Project, rule_id: str) -> Element:
    """Resolve a single nested element; a multi-segment run becomes a ``Group``."""
    resolved = _resolve_elements((element,), project, rule_id)
    return resolved[0] if len(resolved) == 1 else Group(resolved)


def _resolve_rule(rule: Rule, project: Project) -> Rule:
    """A copy of *rule* with every ``LetterRef`` run in its description resolved.

    Stress/tone diacritics on a literal are lowered on every side: in the target/
    context/exception they constrain the match, in the result they write (replace)
    the syllable's suprasegmental. A bare result literal carries none, so stress
    persists from the input.
    """
    sd = rule.sd
    resolved = StructuralDescription(
        target=_resolve_elements(sd.target, project, rule.id),
        result=_resolve_elements(sd.result, project, rule.id),
        left_context=_resolve_elements(sd.left_context, project, rule.id),
        right_context=_resolve_elements(sd.right_context, project, rule.id),
        left_exception=_resolve_elements(sd.left_exception, project, rule.id),
        right_exception=_resolve_elements(sd.right_exception, project, rule.id),
    )
    return replace(rule, sd=resolved)


def resolve_rule_letters(rules: RuleInventory, project: Project) -> RuleInventory:
    """Resolve the letter+diacritic runs a rule writes into per-segment bundles.

    The notation tokenises a contiguous run of letters and diacritics as one
    ``LetterRef`` whose symbol may be a complex segment like ``ʁʷ`` or a
    multi-segment run like ``au`` — neither a plain letter, so on its own it matches
    nothing. This sends every such run through the segmenter — the same path that
    turns an IPA word into segments — and rewrites it as one ``LetterBundle`` per
    segment, so a rule may spell complex segments directly. Run before derivation.

    Raises:
        ValueError: a run resolves to no segment (an unknown symbol).
    """
    return RuleInventory(
        {
            time: tuple(_resolve_rule(rule, project) for rule in rules_at_time)
            for time, rules_at_time in rules.items()
        }
    )


def _maintain_tiers(
    form: Form,
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int | None,
    letters: LetterInventory,
    tiers: TierInventory,
) -> Form:
    """Maintain the tiers after a rule fires.

    Prunes links to deleted segments (their autosegments float) and applies the OCP, then
    re-docks any suprasegmental now on a non-nucleus segment to its syllable's nucleus —
    the spatial re-pool ``consolidate_suprasegmentals`` used to do, on tier links.
    Best-effort: an unsyllabifiable form skips the re-dock.

    Copies *form* first: ``cleanup_tiers``/``redock_to_nuclei`` mutate their argument in
    place, but *form*'s identity may already be cached by ``lower_tiers``/``syllabify``
    (e.g. the ``_fired`` check just before this runs) — mutating it in place would make
    that cache stale for anyone still holding the old reference.
    """
    form = cleanup_tiers(form.copy(), tiers)
    if sonorities is None or syllable_parts is None:
        return form
    nucleus_part = syllable_parts.get_nucleus(time)
    nucleus_def = nucleus_part.definition if nucleus_part is not None else None
    try:
        boundaries = syllabify(form.bundles(), sonorities, syllable_parts, time, letters)
    except SyllabificationError:
        return form
    return redock_to_nuclei(form, boundaries, nucleus_def)


def _floating_autosegs(form: Form) -> tuple[tuple[int, FeatureBundle, int | None], ...]:
    """Every unanchored autosegment (id, bundle, gap) across the tiers — dock candidates.

    *gap* is the float's sequence position from its ``float_hosts`` anchor — the index just
    before a ``"before"`` host, or just after an ``"after"`` host — so a ``⟨⟩`` element binds
    it only where it sits. A float with no (or a now-deleted) host has *gap* ``None`` and
    matches at any position (the position-blind semantics, e.g. a tone stranded by deletion).
    """
    position_of = {segment.id: index for index, segment in enumerate(form.segments)}
    floating: list[tuple[int, FeatureBundle, int | None]] = []
    for tier in form.tiers.values():
        linked = {autoseg_id for (autoseg_id, _anchor) in tier.links}
        for autoseg in tier.autosegs:
            if autoseg.id in linked:
                continue
            gap: int | None = None
            host = tier.float_hosts.get(autoseg.id)
            if host is not None and (host_pos := position_of.get(host[0])) is not None:
                gap = host_pos + 1 if host[1] == "after" else host_pos
            floating.append((autoseg.id, autoseg.bundle, gap))
    return tuple(floating)


def _syllable_context(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int | None,
    letters: LetterInventory,
    syllable_features: frozenset[str],
    node_descendants: dict[str, frozenset[str]],
    floating: tuple[tuple[int, FeatureBundle, int | None], ...] = (),
    *,
    cache: bool = True,
) -> tuple[frozenset[int], SyllableView | None]:
    """Boundaries (for ``$``) and the per-position nucleus view (for tier-aware matching).

    Returns ``(frozenset(), None)`` when syllabification is unconfigured. ``cache=False``
    for a directional scan's working form, whose identity is reused across iterations
    while its content is rewritten in place — see ``lower_tiers``'s ``cache`` parameter.
    """
    if sonorities is None or syllable_parts is None:
        return frozenset(), None
    try:
        boundaries = syllabify(form, sonorities, syllable_parts, time, letters, cache=cache)
    except SyllabificationError:
        # Syllabification runs after every rule; an unsyllabifiable form (under
        # onset/coda constraints) yields no structure rather than aborting.
        return frozenset(), None
    nucleus_part = syllable_parts.get_nucleus(time)
    if nucleus_part is None or nucleus_part.definition is None:
        return boundaries, None
    nuclei = nuclei_by_position(form, boundaries, nucleus_part.definition)
    return boundaries, SyllableView(
        nuclei=nuclei, features=syllable_features, floating=floating,
        node_descendants=node_descendants,
    )


def _boundaries(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int | None,
    letters: LetterInventory,
) -> frozenset[int]:
    """Syllable boundaries of *form* at *time*, or none if syllabification is unconfigured."""
    if sonorities is None or syllable_parts is None:
        return frozenset()
    return syllabify(form, sonorities, syllable_parts, time, letters)


def _display_boundaries(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int | None,
    letters: LetterInventory,
) -> frozenset[int]:
    """Syllable boundaries for the trace — best-effort; an unsyllabifiable form is empty.

    Unlike the matcher's boundaries this is purely for display, so it ignores the
    ``$``-usage gate and never propagates a ``SyllabificationError``.
    """
    try:
        return _boundaries(form, sonorities, syllable_parts, time, letters)
    except SyllabificationError:
        return frozenset()


def apply_rule(
    rule: Rule,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
    tiers: TierInventory | None = None,
) -> Form:
    """Apply *rule* to *form* once, per its application mode.

    Returns a new form; *form* is never mutated. A rule whose loci do not
    match returns an unchanged copy. The form is re-syllabified for every rule, so
    ``$`` and syllable-tier matching always reflect the current form; an
    unsyllabifiable form (under onset/coda constraints) yields no structure rather
    than aborting, and a rule that consults neither ``$`` nor a syllable-tier
    feature is simply unaffected by it. The syllable view is built over *lowered*
    bundles, so syllable-tier matching reads suprasegmentals back off the tiers.
    """
    tiers = tiers if tiers is not None else TierInventory()
    syllable_features = _syllable_features(features)
    match rule.application:
        case ApplicationMode.simultaneous:
            boundaries, view = _syllable_context(
                lower_tiers(form), sonorities, syllable_parts, rule.time, letters,
                syllable_features, _node_descendants(features), _floating_autosegs(form),
            )
            return _apply_simultaneous(
                rule.sd, form, letters, features, boundaries, view, tiers, syllable_features
            )
        case ApplicationMode.left_to_right:
            return _apply_directional(
                rule.sd, form, letters, features, sonorities, syllable_parts, rule.time,
                syllable_features, tiers, False,
            )
        case ApplicationMode.right_to_left:
            return _apply_directional(
                rule.sd, form, letters, features, sonorities, syllable_parts, rule.time,
                syllable_features, tiers, True,
            )


def _select_non_overlapping(matches: list[Match]) -> list[Match]:
    """Leftmost-longest non-overlapping subset of *matches* (ascending by start)."""
    selected: list[Match] = []
    last_end = 0
    for match in matches:
        if match.start >= last_end:
            selected.append(match)
            last_end = match.end
    return selected


def _autoseg_recall(carried: FeatureBundle) -> AutosegRecall | None:
    """The ``AutosegRecall`` in a carried bundle, if any (a ``~ref`` spread directive)."""
    for spec in carried.values():
        if isinstance(spec.value, AutosegRecall):
            return spec.value
    return None


def _spread_autoseg(
    out: Form, source: Form, bindings: Bindings, recall: AutosegRecall, tier_name: str, seg_id: int
) -> None:
    """Link the autosegment bound under *recall* onto *seg_id*.

    Two binds resolve here. A **floating** bind (``⟨...⟩``) carries the autosegment's id
    directly: linking it onto the anchor *docks* it. An **on-anchor** bind (``~n=H``) carries
    the position the autosegment sits on in *source*; adding a second link to that same
    autosegment is what makes a tone *spread* (one autosegment, many anchors).
    """
    if recall.ref in bindings.floating_reference:
        out.tiers.setdefault(tier_name, AutosegmentalTier()).links.add(
            (bindings.floating_reference[recall.ref], seg_id)
        )
        return
    bound_position = bindings.autoseg_reference.get(recall.ref)
    source_tier = source.tiers.get(tier_name)
    if bound_position is None or source_tier is None:
        return
    bound_anchor = source.segments[bound_position].id
    out_tier = out.tiers.setdefault(tier_name, AutosegmentalTier())
    # Snapshot: in directional mode out_tier IS source_tier, and we add to it below.
    for autoseg_id, anchor in list(source_tier.links):
        if anchor == bound_anchor:
            out_tier.links.add((autoseg_id, seg_id))


def _spliced_segments(
    out: Form,
    replacement: list[tuple[FeatureBundle, int | None]],
    source: Form,
    source_bundles: list[FeatureBundle],
    tiers: TierInventory,
    bindings: Bindings,
) -> tuple[list[Segment], set[tuple[str, int]]]:
    """Turn apply_match's (bundle, source-pos) pairs into Segments.

    A merged segment carries its id forward from *source* (so its tier links survive); an
    insertion gets a fresh id. A carried feature is routed onto *out*'s tiers: a ``~ref``
    recall spreads the bound autosegment; otherwise a *changed* value writes (associates) or
    delinks (``none``), while an unchanged carried feature is left untouched so its
    autosegment keeps its identity.

    Also returns the ``(tier_name, segment_id)`` pairs where a result literal wrote an
    explicit, present-valued suprasegmental — the syllable's stress/tone stated by the
    rule. ``_carry_stranded_suprasegmentals`` uses this to *not* re-anchor the replaced
    nucleus's old autosegment on top: an explicit result mark replaces, it does not stack
    (which would otherwise leave two same-anchor autosegs — a spurious ``x>x`` contour).
    """
    new_segments: list[Segment] = []
    explicit_writes: set[tuple[str, int]] = set()
    for bundle, pos in replacement:
        seg_bundle, carried = split_carried(bundle, tiers)
        seg_id = source.segments[pos].id if pos is not None else out.fresh_id()
        new_segments.append(Segment(seg_bundle, seg_id))
        prev = split_carried(source_bundles[pos], tiers)[1] if pos is not None else {}
        for tier_name in set(carried) | set(prev):
            written = carried.get(tier_name, FeatureBundle())
            recall = _autoseg_recall(written)
            if recall is not None:
                _spread_autoseg(out, source, bindings, recall, tier_name, seg_id)
            elif written != prev.get(tier_name, FeatureBundle()):
                write_to_tier(out, seg_id, tier_name, written)
                if any(spec.value is not None for spec in written.values()):
                    explicit_writes.add((tier_name, seg_id))
    return new_segments, explicit_writes


def _carry_stranded_melody(
    out: Form, source: Form, start: int, end: int, stranded: set[int], tiers: TierInventory
) -> None:
    """Carry a deleted segment's melody-tier autosegments onto a surviving neighbour.

    **Runs after** ``_carry_stranded_suprasegmentals`` and reads the live (already re-anchored)
    links, so it only re-docks what a pure deletion left on a stranded anchor — the supra→melody
    fallthrough is enforced by that call order.

    Tonal stability: a tone outlives its anchor instead of floating away. Each melody tier
    carries to the neighbour named by its ``stability`` direction (``"left"`` default, or
    ``"right"``); metrical tiers (stress) stay put, which keeps the shipped stress data
    unchanged. The neighbour is taken by id from *source* (stable across the right-to-left
    splice); if it was itself deleted, ``cleanup_tiers`` prunes the link and the tone floats.
    No neighbour on the chosen side ⇒ the tone floats (and is stray-erased). ``redock_to_nuclei``
    then moves a carried tone onto the neighbour's nucleus.
    """
    left = source.segments[start - 1].id if start > 0 else None
    right = source.segments[end].id if end < len(source.segments) else None
    for name, declaration in tiers.items():
        if not declaration.melody:
            continue
        neighbour = right if declaration.stability == "right" else left
        tier = out.tiers.get(name)
        if neighbour is None or tier is None:
            continue
        tier.links = {
            (autoseg, neighbour if anchor in stranded else anchor)
            for (autoseg, anchor) in tier.links
        }


def _stranded_ids(source: Form, start: int, end: int, new_segments: list[Segment]) -> set[int]:
    """Ids of the segments in ``[start, end)`` the rewrite deleted (absent from *new_segments*)."""
    kept = {segment.id for segment in new_segments}
    return {seg.id for seg in source.segments[start:end] if seg.id not in kept}


def _carry_stranded_suprasegmentals(
    out: Form,
    stranded: set[int],
    new_segments: list[Segment],
    tiers: TierInventory,
    syllable_features: frozenset[str],
    explicit_writes: set[tuple[str, int]],
) -> None:
    """Re-anchor a replaced nucleus's suprasegmentals onto the new nucleus.

    **Runs first**, before ``_carry_stranded_melody`` — a tone re-anchored to a new nucleus here is
    then off the stranded set, so melody only re-docks what a pure deletion leaves behind.

    Suprasegmental tiers (tone, stress) are stable across a nucleus *rewrite*, not only a
    feature-merge: when a span is replaced by new segments that include a valid anchor (a
    new nucleus), the stranded suprasegmental links move onto it — so a plain letter swap
    (``a → u``, ``ʐi → ʐ̩``) keeps its tone and stress, no feature-merge required. A pure
    deletion, with no new anchor in the replacement, falls through to the melody re-docking
    (re-dock to a neighbour). A merge strands nothing, so this is a no-op there.

    Stability yields to an explicit result mark: when the result literal wrote a tier anywhere
    in the replacement (``name in written_tiers`` — e.g. ``ˌa → ˈa``, or ``e → aˈna`` whose ``ˈ``
    sits on the *second* new nucleus), the result's marks are authoritative for that tier across
    the whole span, so the stranded old value is dropped rather than re-anchored. This both keeps
    a write from stacking on its own nucleus (two same-anchor autosegs read as a spurious ``x>x``
    contour) and stops an unmarked new nucleus (the first ``a`` of ``aˈna``) from inheriting the
    replaced nucleus's stress — it stays unstressed, as the bare literal says.
    """
    written_tiers = {tier_name for (tier_name, _anchor) in explicit_writes}
    for name, declaration in tiers.items():
        # Only suprasegmental tiers (those carrying a syllable-tier feature) are exempt; a
        # segment tier is not re-anchored to the nucleus.
        if not any(feature in syllable_features for feature in declaration.carries):
            continue
        if name in written_tiers:
            continue  # the result wrote this tier in the span — its marks replace, no re-anchor
        tier = out.tiers.get(name)
        if tier is None:
            continue
        new_anchor = next(
            (seg.id for seg in new_segments if pattern_matches(declaration.anchor, seg.bundle)),
            None,
        )
        if new_anchor is None:
            continue  # no new nucleus in the replacement → leave to melody re-docking
        tier.links = {
            (autoseg, new_anchor if anchor in stranded else anchor)
            for (autoseg, anchor) in tier.links
        }


def _apply_simultaneous(
    sd: StructuralDescription,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    boundaries: frozenset[int],
    syllables: SyllableView | None,
    tiers: TierInventory,
    syllable_features: frozenset[str],
) -> Form:
    """Find every locus against the original form, then splice all rewrites at once."""
    bundles = lower_tiers(form)
    selected = _select_non_overlapping(find_matches(sd, bundles, letters, boundaries, syllables))
    out = form.copy()
    # Splice right-to-left so each replacement's indices stay valid, computing every
    # replacement from the ORIGINAL form (no application sees another's output).
    for match in sorted(selected, key=lambda m: m.start, reverse=True):
        replacement = apply_match(sd, match, bundles, letters, features, syllables)
        new_segments, explicit_writes = _spliced_segments(
            out, replacement, form, bundles, tiers, match.bindings
        )
        stranded = _stranded_ids(form, match.start, match.end, new_segments)
        if stranded:  # supra re-anchoring first, then melody re-docking — order is load-bearing
            _carry_stranded_suprasegmentals(
                out, stranded, new_segments, tiers, syllable_features, explicit_writes
            )
            _carry_stranded_melody(out, form, match.start, match.end, stranded, tiers)
        out.segments[match.start : match.end] = new_segments
    return out


def _apply_directional(
    sd: StructuralDescription,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int | None,
    syllable_features: frozenset[str],
    tiers: TierInventory,
    reverse: bool,
) -> Form:
    """Scan and rewrite in place; each output is visible to later loci in the pass.

    Because the form mutates as it is rewritten, it is re-syllabified before each
    scan so the ``$`` assertion and syllable-tier matching reflect the current form.
    """
    work = form.copy()
    node_descendants = _node_descendants(features)  # invariant for the rule; not per-locus
    cursor = len(work.segments) if reverse else 0
    while True:
        # work mutates in place each iteration (see the docstring above), so its identity
        # is reused across content changes — bypass the identity cache, which would
        # otherwise keep serving the pre-mutation syllabification/tier-lowering forever.
        bundles = lower_tiers(work, cache=False)
        boundaries, view = _syllable_context(
            bundles, sonorities, syllable_parts, time, letters,
            syllable_features, node_descendants, _floating_autosegs(work),
            cache=False,
        )
        if reverse:
            candidates = [
                m for m in find_matches(sd, bundles, letters, boundaries, view) if m.end <= cursor
            ]
            if not candidates:
                break
            # Rightmost, tie-broken to longest (min start) — the mirror of
            # leftmost-longest. (max end, then min start.)
            match = max(candidates, key=lambda m: (m.end, -m.start))
        else:
            candidates = [
                m for m in find_matches(sd, bundles, letters, boundaries, view) if m.start >= cursor
            ]
            if not candidates:
                break
            # Leftmost; the matcher already made it longest for that start.
            match = min(candidates, key=lambda m: m.start)

        replacement = apply_match(sd, match, bundles, letters, features, view)
        new_segments, explicit_writes = _spliced_segments(
            work, replacement, work, bundles, tiers, match.bindings
        )
        stranded = _stranded_ids(work, match.start, match.end, new_segments)
        if stranded:  # supra re-anchoring first, then melody re-docking — order is load-bearing
            _carry_stranded_suprasegmentals(
                work, stranded, new_segments, tiers, syllable_features, explicit_writes
            )
            _carry_stranded_melody(work, work, match.start, match.end, stranded, tiers)
        work.segments[match.start : match.end] = new_segments

        no_op = match.end == match.start and not replacement
        if reverse:
            # Advance leftward past the output's left edge; bump only a true no-op.
            cursor = match.start - 1 if no_op else match.start
        else:
            # Advance past the rewritten output; bump only a true no-op (a deletion
            # makes progress by shrinking the form, so it must not bump).
            cursor = match.start + 1 if no_op else match.start + len(replacement)
    return work


def _fired(before: list[FeatureBundle], after: list[FeatureBundle]) -> bool:
    """Whether the rule changed the form (a vacuous match is not a firing)."""
    if len(before) != len(after):
        return True
    return any(not matches_exactly(b, a) for b, a in zip(before, after, strict=True))


def derive(
    word: Word,
    form: Form,
    rules: RuleInventory,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
    tiers: TierInventory | None = None,
) -> Derivation:
    """Sweep *form* through every rule in time order, recording firing steps.

    Each rule (re)syllabifies the current form for its match pass, so the input is
    syllabified before the first rule and the structure is refreshed after every
    rule — without ``sonorities``/``syllable_parts`` there are simply no
    boundaries and the ``$`` assertion never matches.

    Rules that spell a complex symbol (e.g. ``ʁʷ``) or a multi-segment run must be
    passed through ``resolve_rule_letters`` first; an unresolved such ``LetterRef``
    matches nothing and the rule silently does not fire.

    Args:
        word: The word being derived (carried into the trace).
        form: The starting form (already segmented, from ``string_to_sequence``).
        rules: Rules keyed by time; applied ascending by time, file order within.
            Pre-resolve with ``resolve_rule_letters`` if any rule uses a complex
            symbol or multi-segment run.
        letters: Letter inventory, for shorthands and recalls.
        features: Feature inventory, for the geometry-aware merge.
        sonorities: Sonority scale for syllabification (optional).
        syllable_parts: Syllable-part constraints supplying the nucleus (optional).
        tiers: Autosegmental tier declarations; empty ⇒ no tiers run (optional).
    """
    tiers = tiers if tiers is not None else TierInventory()
    current = form
    steps: list[DerivationStep] = []

    for time in sorted(rules.keys(), key=lambda t: (t is None, t)):  # untimed (None) rules last
        for rule in rules[time]:
            if rule.words and word.ipa not in rule.words and word.gloss not in rule.words:
                continue  # a word-scoped rule that does not list this word
            before = current  # Form
            after = apply_rule(rule, current, letters, features, sonorities, syllable_parts, tiers)
            if _fired(lower_tiers(before), lower_tiers(after)):
                # Maintain the tiers: prune dead links + OCP, then re-dock suprasegmentals
                # onto their syllable's nucleus (the old consolidate's spatial job).
                after = _maintain_tiers(
                    after, sonorities, syllable_parts, rule.time, letters, tiers
                )
                steps.append(
                    DerivationStep(
                        before=before,
                        rule=rule,
                        after=after,
                        before_boundaries=_display_boundaries(
                            before.bundles(), sonorities, syllable_parts, rule.time, letters
                        ),
                        after_boundaries=_display_boundaries(
                            after.bundles(), sonorities, syllable_parts, rule.time, letters
                        ),
                    )
                )
                current = after

    # Copy first: current's identity may already be cached (see _maintain_tiers), and
    # cleanup_tiers mutates its argument in place.
    current = cleanup_tiers(current.copy(), tiers, surface=True)  # stray-erase floating autosegs
    latest = max((t for t in rules if t is not None), default=0)  # surface uses the latest parts
    surface_boundaries = _display_boundaries(
        current.bundles(), sonorities, syllable_parts, latest, letters
    )
    return Derivation(
        word=word,
        input=form,
        steps=tuple(steps),
        surface=current,
        surface_boundaries=surface_boundaries,
    )
