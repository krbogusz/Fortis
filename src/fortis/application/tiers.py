"""Autosegmental tier operations over a Form.

For now this is just *construction*: lifting the suprasegmental features already sitting
in the segment bundles onto their declared tiers, as autosegments linked to their anchor.
The in-bundle copy is left in place (dual representation) — task 3c removes it and flips
the readers (matcher, rendering) to consult the tier instead.
"""
from __future__ import annotations

from src.fortis.application.matching import pattern_matches
from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.form import Form
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.tier_declaration import TierInventory


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
    return form


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
