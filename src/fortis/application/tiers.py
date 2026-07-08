"""Autosegmental tier operations over a Form.

Suprasegmental features (tone, stress) live on declared tiers, not in the segment bundles.
``associate_tiers`` builds a tier at construction (lifting the features off the bundles and
stripping them); ``cleanup_tiers`` and ``redock_to_nuclei`` maintain it after each rule —
pruning links to deleted segments (the source of tonal stability), applying the OCP, and
following a shifted nucleus; ``split_carried``/``write_to_tier`` route a rule's
suprasegmental writes onto the tier; ``carried_features``/``lower_tiers`` read them back so
the matcher and renderer keep working on bundles as before.
"""
from __future__ import annotations

from typing import cast

from src.fortis.application.matching import pattern_matches
from src.fortis.application.syllabifying import syllables
from src.fortis.general.utils import IdentityCache
from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.form import Form
from src.fortis.models.segment import Segment
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.tier_declaration import TierInventory
from src.fortis.models.values import Limb, make_value

_lower_tiers_cache = IdentityCache(maxsize=8)


def associate_tiers(form: Form, tiers: TierInventory) -> Form:
    """Build each declared tier from the carried features already in *form*'s segments.

    For every declared tier, each anchor segment that carries the tier's feature(s) gets
    an autosegment (those features lifted out) linked to it by id. Mutates and returns
    *form*; an absent or empty tier declaration leaves the form untouched.
    """
    for name, declaration in tiers.items():
        tier = AutosegmentalTier()
        for segment in form.segments:
            if not pattern_matches(declaration.anchor, segment.bundle):
                continue
            carried = {
                feature: segment.bundle[feature]
                for feature in declaration.carries
                if feature in segment.bundle
            }
            if not carried:
                continue
            autoseg = Autoseg(FeatureBundle(carried), form.fresh_id())
            tier.autosegs.append(autoseg)
            tier.links.add((autoseg.id, segment.id))
        form.tiers[name] = tier
    # The carried features now live on the tiers; strip them from the segment bundles.
    carried_names = {feature for declaration in tiers.values() for feature in declaration.carries}
    if carried_names:
        form.segments = [
            Segment(
                FeatureBundle({f: s for f, s in segment.bundle.items() if f not in carried_names}),
                segment.id,
            )
            for segment in form.segments
        ]
    return form


def lower_tiers(form: Form, *, cache: bool = True) -> list[FeatureBundle]:
    """Merge each segment's carried features back into its bundle (the inverse of associate).

    Lets the matcher and renderer read suprasegmentals from bundles as before the flip,
    without threading the tiers into them. The carried features are indexed by anchor in one
    pass (rather than re-scanning every tier per segment), so this is O(autosegs), not quadratic.

    A rule sweep re-derives this for the same unchanged ``form`` across every rule that
    doesn't fire, so results are cached by *identity* of ``form`` when ``cache`` is true —
    safe wherever a ``Form`` is treated as immutable (a rewrite produces a fresh copy).
    Pass ``cache=False`` for a form mutated in place across calls (e.g. a directional
    scan's working copy), where the same identity can legitimately hold new content.
    """
    if not cache:
        return _lower_tiers_uncached(form)
    return _lower_tiers_cache.get_or_compute(form, None, lambda: _lower_tiers_uncached(form))


def _lower_tiers_uncached(form: Form) -> list[FeatureBundle]:
    carried = _carried_by_anchor(form)
    empty = FeatureBundle()
    return [
        FeatureBundle({**segment.bundle, **carried.get(segment.id, empty)})
        for segment in form.segments
    ]


def _carried_by_anchor(form: Form) -> dict[int, FeatureBundle]:
    """Every anchor's carried features, built in a single pass over the tiers.

    Visits each tier then its autosegs in list order, routing each linked autoseg's specs to its
    anchor(s); so per-anchor limb order — hence contour direction — is identical to a per-segment
    ``carried_features`` scan, but without re-walking every tier for every segment.
    """
    by_feature: dict[int, dict[str, list[FeatureSpec]]] = {}
    for tier in form.tiers.values():
        anchors_of: dict[int, list[int]] = {}
        for autoseg_id, anchor in tier.links:
            anchors_of.setdefault(autoseg_id, []).append(anchor)
        for autoseg in tier.autosegs:  # tier-autoseg order ⇒ correct contour direction per anchor
            for anchor in anchors_of.get(autoseg.id, ()):
                anchor_features = by_feature.setdefault(anchor, {})
                for feature, spec in autoseg.bundle.items():
                    anchor_features.setdefault(feature, []).append(spec)
    return {anchor: _collapse_carried(feats) for anchor, feats in by_feature.items()}


def cleanup_tiers(form: Form, tiers: TierInventory, *, surface: bool = False) -> Form:
    """Maintain every tier after a rewrite.

    Prunes links to segments that no longer exist — stranding their autosegments as
    floating, which is where tonal stability comes from. Then applies the OCP (merging
    adjacent identical autosegments into one multiply-linked autosegment) and, at the
    *surface* only, stray-erases any autosegment that never docked. Mutates and returns
    *form*; a tier with no declaration keeps its links pruned but no policy applied.
    """
    live = {segment.id for segment in form.segments}
    position = {segment.id: index for index, segment in enumerate(form.segments)}
    for name, tier in form.tiers.items():
        declaration = tiers.get(name)
        tier.links = {(autoseg, anchor) for (autoseg, anchor) in tier.links if anchor in live}
        if declaration is not None and declaration.ocp:
            _merge_adjacent_identical(tier, position)
        if surface and declaration is not None and declaration.stray_erase:
            linked = {autoseg for (autoseg, _anchor) in tier.links}
            tier.autosegs = [seg for seg in tier.autosegs if seg.id in linked]
    return form


def _merge_adjacent_identical(tier: AutosegmentalTier, position: dict[int, int]) -> None:
    """Fold each run of identical adjacent autosegments into one (the OCP).

    Adjacency is order on the tier (by leftmost anchor), not on segments; the survivor
    takes over every merged autosegment's links.
    """

    def leftmost(autoseg: Autoseg) -> float:
        anchors = [position[anchor] for (a, anchor) in tier.links if a == autoseg.id]
        return min(anchors) if anchors else float("inf")

    kept: list[Autoseg] = []
    for autoseg in sorted(tier.autosegs, key=leftmost):
        if kept and kept[-1].bundle == autoseg.bundle:
            survivor = kept[-1].id
            tier.links = {
                (survivor if a == autoseg.id else a, anchor) for (a, anchor) in tier.links
            }
        else:
            kept.append(autoseg)
    tier.autosegs = kept


def split_carried(
    bundle: FeatureBundle, tiers: TierInventory
) -> tuple[FeatureBundle, dict[str, FeatureBundle]]:
    """Split a written bundle into segment-tier and carried (tier) parts.

    Returns the bundle that stays on the segment and a ``{tier name: carried bundle}``
    map of the features bound for each tier.
    """
    owner = {feature: name for name, decl in tiers.items() for feature in decl.carries}
    segment_specs: dict[str, FeatureSpec] = {}
    by_tier: dict[str, dict[str, FeatureSpec]] = {}
    for feature, spec in bundle.items():
        name = owner.get(feature)
        if name is None:
            segment_specs[feature] = spec
        else:
            by_tier.setdefault(name, {})[feature] = spec
    return FeatureBundle(segment_specs), {name: FeatureBundle(s) for name, s in by_tier.items()}


def write_to_tier(form: Form, segment_id: int, tier_name: str, carried: FeatureBundle) -> None:
    """Route a carried-feature write to a segment's tier.

    The segment's current autosegment on that tier is delinked (it floats); if *carried*
    holds any present value a fresh autosegment is built from it and linked. A write whose
    value is ``none`` therefore just delinks.
    """
    tier = form.tiers.setdefault(tier_name, AutosegmentalTier())
    tier.links = {(autoseg, anchor) for (autoseg, anchor) in tier.links if anchor != segment_id}
    present = FeatureBundle({f: s for f, s in carried.items() if s.value is not None})
    if present:
        autoseg = Autoseg(present, form.fresh_id())
        tier.autosegs.append(autoseg)
        tier.links.add((autoseg.id, segment_id))


def carried_features(form: Form, segment_id: int) -> FeatureBundle:
    """The carried (tier) features a segment bears, read back as a bundle.

    Merges the features of every autosegment linked to *segment_id* — the read side of the
    tiers, mirroring the bundle lookup the matcher and renderer used before the flip. Several
    autosegments of the same feature on one anchor form a **contour** (e.g. H + L → a falling
    tone), in tier order. (Tier order is creation/lexical order, so the contour direction is
    reliable for lexical melodies and tone crowding — not after operations that reorder a tier.)
    """
    by_feature: dict[str, list[FeatureSpec]] = {}
    for tier in form.tiers.values():
        linked = {autoseg for (autoseg, anchor) in tier.links if anchor == segment_id}
        for autoseg in tier.autosegs:
            if autoseg.id in linked:
                for feature, spec in autoseg.bundle.items():
                    by_feature.setdefault(feature, []).append(spec)
    return _collapse_carried(by_feature)


def _collapse_carried(by_feature: dict[str, list[FeatureSpec]]) -> FeatureBundle:
    """Collapse per-feature spec lists to a bundle: a lone spec, or several limbs as a contour."""
    specs: dict[str, FeatureSpec] = {}
    for feature, feature_specs in by_feature.items():
        if len(feature_specs) == 1:
            specs[feature] = feature_specs[0]
        else:
            limbs = tuple(
                limb
                for spec in feature_specs
                for limb in (spec.value if isinstance(spec.value, tuple) else (spec.value,))
            )
            specs[feature] = FeatureSpec(
                feature=feature, value=make_value(cast("tuple[Limb, ...]", limbs))
            )
    return FeatureBundle(specs)


def redock_to_nuclei(form: Form, boundaries: frozenset[int], nucleus: PatternBundle | None) -> Form:
    """Move every suprasegmental link off a non-nucleus segment onto its syllable's nucleus.

    The autosegmental analogue of consolidate's spatial re-pool: when a nucleus shifts (e.g.
    epenthesis turns a syllabic consonant into a coda), the suprasegmental follows the
    syllable to its new nucleus. No nucleus definition ⇒ nothing to re-dock.
    """
    if nucleus is None:
        return form
    nucleus_id_for: dict[int, int] = {}
    for syllable in syllables(form.bundles(), boundaries, nucleus):
        if syllable.nucleus is None:
            continue
        nucleus_id = form.segments[syllable.nucleus].id
        for position in range(syllable.start, syllable.end):
            nucleus_id_for[position] = nucleus_id
    position_of = {segment.id: index for index, segment in enumerate(form.segments)}
    for tier in form.tiers.values():
        tier.links = {
            (autoseg, nucleus_id_for.get(position_of.get(anchor, -1), anchor))
            for (autoseg, anchor) in tier.links
        }
    return form
