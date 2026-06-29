"""Autosegmental tier diagrams as monospace Unicode text.

The classic autosegmental picture, in text: autosegments sit on tier rows above the
segments, joined to their anchors by association lines. One autosegment forking to
several anchors is **spread**; several converging on one anchor is a **contour**; an
unlinked autosegment **floats** at its lexical position with no line. Rendered with
box-drawing characters so it stays readable in any monospace IPA font.
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.application.rendering import render_segment
from src.fortis.general.presenting import present_value
from src.fortis.general.utils import is_combining
from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.features import FeatureKind
from src.fortis.models.form import Form
from src.fortis.models.project import Project

# Tone scalar (1=extra-low … 5=extra-high) → Chao tone letter.
_TONE = {5: "˥", 4: "˦", 3: "˧", 2: "˨", 1: "˩"}
_STRESS = {2: "ˈ", 1: "ˌ"}
_SEP = 3  # blank display columns between segment slots


@dataclass(frozen=True)
class _Spread:
    """One autosegment fanning to its anchors — the common shape both change diagrams draw.

    ``label`` is the spreading thing (a tone like ``˦`` or a place node like ``lingual·back``);
    ``links`` pairs each anchor's index in the ``after`` segment row with its association glyph
    (``│`` kept · ``╎`` added · ``╪`` delinked); ``replaced`` is an optional ``(index, old_label)``
    drawn *below* that anchor — the delinked old value a node spread overwrote (``None`` for tiers).
    """

    label: str
    links: tuple[tuple[int, str], ...]
    replaced: tuple[int, str] | None = None


def _dwidth(text: str) -> int:
    """Display width — combining marks occupy no column."""
    return sum(0 if is_combining(ch) else 1 for ch in text)


def _label(autoseg, tier_name: str) -> str:
    """A short label for one autosegment (a tone letter, a stress mark, …)."""
    return _label_from_bundle(autoseg.bundle, tier_name)


def _label_from_bundle(bundle, tier_name: str) -> str:
    # A segmental geometry node (e.g. Place) labels by its node value; its autoseg carries the
    # node's features, so a place autoseg renders as its major place (Labial / Coronal / Dorsal).
    place = _place_label(bundle)
    if place is not None:
        return place
    for feature, spec in bundle.items():
        value = spec.value
        if feature == "tone":
            if isinstance(value, tuple):
                return "".join(_TONE.get(v, "?") for v in value)
            return _TONE.get(value, str(value))
        if feature == "stress":
            return _STRESS.get(value, str(value))
        return str(value)
    return "?"


def _put(row: list[str], col: int, text: str) -> None:
    for offset, ch in enumerate(text):
        if 0 <= col + offset < len(row):
            row[col + offset] = ch


def render_autosegmental(form: Form, project: Project) -> str:
    """Render *form*'s tiers as a monospace autosegmental diagram."""
    segs = form.segments
    if not segs:
        return "(empty)"
    rendered = [render_segment(s.bundle, project) or "∅" for s in segs]
    slot = max(max((_dwidth(r) for r in rendered), default=1), 3)  # ≥3 leaves room for a contour
    step = slot + _SEP
    margin = 4  # room for a floating autosegment before the first / after the last segment
    total = margin + len(segs) * step - _SEP + margin
    center = {s.id: margin + i * step + slot // 2 for i, s in enumerate(segs)}
    pos = {s.id: i for i, s in enumerate(segs)}

    lines: list[str] = []
    for name, tier in form.tiers.items():
        if tier.autosegs:
            lines.extend(_tier_band(tier, name, center, pos, segs, total))

    seg_row = [" "] * total
    for i, r in enumerate(rendered):
        col = margin + i * step + (slot - _dwidth(r)) // 2
        _put(seg_row, col, r)
    lines.append("".join(seg_row))
    return "\n".join(line.rstrip() for line in lines)


def _tier_band(
    tier: AutosegmentalTier, name: str, center, pos, segs, total: int
) -> list[str]:
    """The label row + connector row for one tier."""
    seg_ids = {s.id for s in segs}
    label_row = [" "] * total
    conn_row = [" "] * total

    spreads, singles, floats = [], {}, []
    for autoseg in tier.autosegs:
        anchors = sorted(
            center[sid] for (a, sid) in tier.links if a == autoseg.id and sid in seg_ids
        )
        if not anchors:
            floats.append(autoseg)
        elif len(anchors) > 1:
            spreads.append((autoseg, anchors))
        else:
            singles.setdefault(anchors[0], []).append(autoseg)

    for autoseg, anchors in spreads:  # one autoseg → many anchors (the fork)
        label = _label(autoseg, name)
        mid = (anchors[0] + anchors[-1]) // 2
        _put(label_row, mid - (_dwidth(label) - 1) // 2, label)
        for x in range(anchors[0], anchors[-1] + 1):
            conn_row[x] = "─"
        for a in anchors:
            conn_row[a] = "┬"
        conn_row[anchors[0]] = "┌"
        conn_row[anchors[-1]] = "┐"
        conn_row[mid] = "┼" if mid in anchors else "┴"

    for col, group in singles.items():
        if len(group) == 1:  # one tone on one anchor
            label = _label(group[0], name)
            _put(label_row, col - (_dwidth(label) - 1) // 2, label)
            conn_row[col] = "│"
        else:  # several tones converging on one anchor — a contour
            labels = [_label(a, name) for a in group]
            _put(label_row, col - 1, labels[0])
            _put(label_row, col + 1, labels[-1])
            conn_row[col - 1], conn_row[col], conn_row[col + 1] = "└", "┬", "┘"

    for autoseg in floats:  # unlinked: shown at its lexical gap, no line
        label = _label(autoseg, name)
        col = _float_col(tier, autoseg.id, center, pos, segs)
        _put(label_row, col - (_dwidth(label) - 1) // 2, label)

    return ["".join(label_row), "".join(conn_row)]


def _float_col(tier, autoseg_id, center, pos, segs) -> int:
    host = tier.float_hosts.get(autoseg_id)
    if host is None or host[0] not in center:
        return center[segs[0].id]
    sid, side = host
    return center[sid] + (2 if side == "after" else -2)


def render_autosegmental_change(before: Form, after: Form, project: Project) -> str:
    """Render one rule's autosegmental *tier* change as a single overlay diagram.

    Association lines are styled by what the rule did to them, the classic
    rule-as-diagram notation: ``│`` an association kept, ``╎`` (dashed) one newly added
    — a spread or a dock — and ``╪`` (the delink bar) one removed. The anchor row is the
    rule's *result* (``after``) segments; each autosegment keeps its label.
    """
    if not after.segments:
        return render_autosegmental(after, project)
    return _draw(after.segments, _tier_spreads(before, after), project)


def _tier_spreads(before: Form, after: Form) -> list[_Spread]:
    """The tier (tone/stress) association changes, one ``_Spread`` per autosegment that moved.

    Anchors are restricted to segments present in ``after`` (a link to a deleted segment is
    dropped) and indexed by their position in ``after.segments`` so ``_draw`` can place them.
    """
    after_index = {segment.id: i for i, segment in enumerate(after.segments)}
    spreads: list[_Spread] = []
    for name in dict.fromkeys([*before.tiers, *after.tiers]):
        before_tier = before.tiers.get(name)
        after_tier = after.tiers.get(name)
        before_links = before_tier.links if before_tier is not None else set()
        after_links = after_tier.links if after_tier is not None else set()
        # Autoseg id → bundle (prefer the after-state bundle; fall back to before for a removed).
        bundles: dict[int, object] = {}
        for tier in (after_tier, before_tier):
            if tier is not None:
                for autoseg in tier.autosegs:
                    bundles.setdefault(autoseg.id, autoseg.bundle)
        for autoseg_id, bundle in bundles.items():
            before_anchors = {s for (a, s) in before_links if a == autoseg_id and s in after_index}
            after_anchors = {s for (a, s) in after_links if a == autoseg_id and s in after_index}
            all_anchors = before_anchors | after_anchors
            if not all_anchors:
                continue
            links = tuple(
                (after_index[sid], _change_glyph(sid, before_anchors, after_anchors))
                for sid in all_anchors
            )
            spreads.append(_Spread(_label_from_bundle(bundle, name), links))
    return spreads


def _draw(segments, spreads: list[_Spread], project: Project) -> str:
    """The shared rendering core: an ``after`` segment row with each ``_Spread`` drawn over it.

    Above the segments: a fork (label / ``┌─┴─┐`` / styled descenders) for a multi-anchor spread,
    a single styled vertical for a one-anchor spread, and several one-anchor spreads sharing a
    column fanned out as a contour. Below: a ``╪`` and old-label row for each spread's ``replaced``.
    """
    rendered = [render_segment(s.bundle, project) or "∅" for s in segments]
    slot = max(max((_dwidth(r) for r in rendered), default=1), 3)  # ≥3 leaves room for a contour
    step = slot + _SEP
    margin = 4
    total = margin + len(segments) * step - _SEP + margin
    centers = [margin + i * step + slot // 2 for i in range(len(segments))]

    above: list[list[str]] = []
    if spreads:
        label_row = [" "] * total
        conn_row = [" "] * total
        fork_row = [" "] * total  # the branch row (label above, descenders below)
        multi = [s for s in spreads if len(s.links) > 1]
        singles: dict[int, list[tuple[str, str]]] = {}  # col → [(label, glyph)] — one anchor each
        for s in spreads:
            if len(s.links) == 1:
                idx, glyph = s.links[0]
                singles.setdefault(centers[idx], []).append((s.label, glyph))
        for s in multi:  # one autoseg, several anchors
            cols_glyphs = [(centers[idx], glyph) for idx, glyph in s.links]
            cols = sorted(col for col, _ in cols_glyphs)
            mid = (cols[0] + cols[-1]) // 2
            _put(label_row, mid - (_dwidth(s.label) - 1) // 2, s.label)  # the label, above the fork
            for x in range(cols[0], cols[-1] + 1):  # the branch line spanning the anchors
                fork_row[x] = "─"
            for c in cols:
                fork_row[c] = "┬"
            fork_row[cols[0]], fork_row[cols[-1]] = "┌", "┐"
            fork_row[mid] = "┼" if mid in cols else "┴"  # the join, under the label
            for col, glyph in cols_glyphs:  # styled descender: │ kept · ╎ added · ╪ delinked
                conn_row[col] = glyph
        for col, items in singles.items():  # several autosegs on one anchor ⇒ a contour, fanned out
            spread_out = range(-(len(items) - 1), len(items), 2)  # 1→[0], 2→[-1,1], 3→[-2,0,2], …
            for (label, glyph), offset in zip(items, spread_out, strict=True):
                _put(label_row, col + offset - (_dwidth(label) - 1) // 2, label)
                conn_row[col + offset] = glyph
        above = [label_row, fork_row, conn_row] if multi else [label_row, conn_row]

    seg_row = [" "] * total
    for i, r in enumerate(rendered):
        col = margin + i * step + (slot - _dwidth(r)) // 2
        _put(seg_row, col, r)

    below: list[list[str]] = []
    for s in spreads:  # the delinked old value a node spread overwrote, under its anchor
        if s.replaced is not None:
            idx, old_label = s.replaced
            delink_row = [" "] * total
            delink_row[centers[idx]] = "╪"
            old_row = [" "] * total
            _put(old_row, max(0, centers[idx] - _dwidth(old_label) // 2), old_label)
            below += [delink_row, old_row]

    lines = [*above, seg_row, *below]
    return "\n".join("".join(row).rstrip() for row in lines)


def _change_glyph(sid: int, before_anchors: set[int], after_anchors: set[int]) -> str:
    """The association glyph for one anchor: kept, newly added (dashed), or delinked."""
    if sid in before_anchors and sid in after_anchors:
        return "│"  # association kept
    if sid in after_anchors:
        return "╎"  # association added (a spread / dock) — dashed
    return "╪"  # association removed — the delink bar


def _place_label(bundle) -> str | None:
    """The segment's oral place, named by its real geometry features (not an invented label).

    Faithful to the feature inventory's own nodes — ``labial``, ``dental``, ``lingual`` with
    its ``front``/``back`` daughter — rather than the idealized Labial/Coronal/Dorsal. The
    front/back split keeps two lingual places (coronal vs velar) distinct for change detection.
    """
    if "labial" in bundle:
        return "labial"
    if "lingual" in bundle:
        if "front" in bundle:
            return "lingual·front"
        if "back" in bundle:
            return "lingual·back"
        return "lingual"
    if "dental" in bundle:
        return "dental"
    return None


def _is_consonant(bundle) -> bool:
    spec = bundle.get("consonantal")
    return spec is not None and spec.value == 1


def _node_spreads(before: Form, after: Form, project: Project) -> list[_Spread]:
    """Place assimilations as ``_Spread``s over the real ``oral`` node — one per assimilated seg.

    A consonant whose ``_place_label`` changed assimilated to a consonant neighbour (right
    ``i+1`` first — regressive — then left ``i-1``) carrying the new place: that trigger keeps
    its link (``│``), the assimilated segment's link is the new spread (``╎``), and its old
    place is delinked (``replaced``, drawn as ``╪`` below) — the tone-change notation on a node.
    """
    _ = project  # rendering happens in _draw; detection needs only the place labels
    before_by_id = {segment.id: segment.bundle for segment in before.segments}
    segments = after.segments
    spreads: list[_Spread] = []
    for i, segment in enumerate(segments):
        old_bundle = before_by_id.get(segment.id)
        # Place assimilation is a consonant phenomenon: only a consonant whose place changed
        # is a candidate — a vowel that merely matches a neighbour's place by accident is not.
        if old_bundle is None or not _is_consonant(segment.bundle):
            continue
        old, new = _place_label(old_bundle), _place_label(segment.bundle)
        if old is None or new is None or old == new:
            continue
        for j in (i + 1, i - 1):  # the consonant neighbour it matches (right first, then left)
            if (
                0 <= j < len(segments)
                and _is_consonant(segments[j].bundle)
                and _place_label(segments[j].bundle) == new
            ):
                spreads.append(_Spread(new, ((j, "│"), (i, "╎")), replaced=(i, old)))
                break
    return spreads


def render_geometry_tree(bundle: FeatureBundle, project: Project) -> str:
    """One segment's feature geometry as an indented tree — for single-segment inspection.

    The (implicit) ROOT is the segment itself; each top-level feature present in the bundle
    hangs beneath it, with its own present children nested in turn — so the picture is the
    feature geometry pruned to what this segment specifies. Binary features show their sign
    (``+voice``), scalars their value label (``length: short``), unary nodes their bare name.
    """
    lines = [render_segment(bundle, project) or "?"]
    tops = [f for f in project.features.children("root") if f in bundle]
    for i, top in enumerate(tops):
        _geometry_branch(top, bundle, project, "", i == len(tops) - 1, lines)
    return "\n".join(lines)


def _geometry_branch(
    feature: str, bundle: FeatureBundle, project: Project, prefix: str, last: bool, lines: list[str]
) -> None:
    """Append *feature*'s line and its present descendants to *lines*, with tree glyphs."""
    lines.append(prefix + ("└─ " if last else "├─ ") + _feature_label(feature, bundle, project))
    children = [c for c in project.features.children(feature) if c in bundle]
    child_prefix = prefix + ("   " if last else "│  ")
    for i, child in enumerate(children):
        _geometry_branch(child, bundle, project, child_prefix, i == len(children) - 1, lines)


def _feature_label(feature: str, bundle: FeatureBundle, project: Project) -> str:
    """A feature's label: sign for binary (``+voice``), value for scalar, bare name for unary."""
    definition = project.features[feature]
    value = bundle[feature].value  # a realized segment carries a single int, not a contour
    if definition.kind == FeatureKind.binary and isinstance(value, int):
        return f"{present_value(value)}{feature}"
    if definition.kind == FeatureKind.scalar and isinstance(value, int):
        return f"{feature}: {definition.values.get(value, str(value))}"
    return feature


def render_place_changes(before: Form, after: Form, project: Project) -> list[str]:
    """A place-change diagram for each segment whose place assimilated to a neighbour's."""
    return [_draw(after.segments, [s], project) for s in _node_spreads(before, after, project)]


def render_change(before: Form, after: Form, project: Project) -> list[str]:
    """Every autosegmental change for one rule, as fork diagrams — the single renderer to call.

    One entry point for both kinds of spread, which share the label/fork/descender notation
    (``│`` kept · ``╎`` added · ``╪`` delinked): a *tier* autosegment (tone, stress) whose links
    changed yields one diagram (all tiers together); each *segmental-node* (place) assimilation
    yields its own. Returns them in display order — tier change first, then place assimilations.
    """
    diagrams: list[str] = []
    tier = render_autosegmental_change(before, after, project)
    if "╎" in tier or "╪" in tier:  # the tier diagram is meaningful only when a link changed
        diagrams.append(tier)
    diagrams.extend(render_place_changes(before, after, project))
    return diagrams
