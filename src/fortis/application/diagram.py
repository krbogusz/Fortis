"""Autosegmental tier diagrams as monospace Unicode text.

The classic autosegmental picture, in text: autosegments sit on tier rows above the
segments, joined to their anchors by association lines. One autosegment forking to
several anchors is **spread**; several converging on one anchor is a **contour**; an
unlinked autosegment **floats** at its lexical position with no line. Rendered with
box-drawing characters so it stays readable in any monospace IPA font.
"""
from __future__ import annotations

from src.fortis.application.rendering import render_segment
from src.fortis.general.utils import is_combining
from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.form import Form
from src.fortis.models.project import Project

# Tone scalar (1=extra-low … 5=extra-high) → Chao tone letter.
_TONE = {5: "˥", 4: "˦", 3: "˧", 2: "˨", 1: "˩"}
_STRESS = {2: "ˈ", 1: "ˌ"}
_SEP = 3  # blank display columns between segment slots


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
    """Render one rule's autosegmental change as a single overlay diagram.

    Association lines are styled by what the rule did to them, the classic
    rule-as-diagram notation: ``│`` an association kept, ``╎`` (dashed) one newly added
    — a spread or a dock — and ``╪`` (the delink bar) one removed. The anchor row is the
    rule's *result* (``after``) segments; each autosegment keeps its label.
    """
    segs = after.segments
    if not segs:
        return render_autosegmental(after, project)
    rendered = [render_segment(s.bundle, project) or "∅" for s in segs]
    slot = max(max((_dwidth(r) for r in rendered), default=1), 3)
    step = slot + _SEP
    margin = 4
    total = margin + len(segs) * step - _SEP + margin
    center = {s.id: margin + i * step + slot // 2 for i, s in enumerate(segs)}
    seg_ids = {s.id for s in segs}

    lines: list[str] = []
    for name in dict.fromkeys([*before.tiers, *after.tiers]):
        lines.extend(
            _change_tier_band(
                before.tiers.get(name), after.tiers.get(name), name, center, seg_ids, total
            )
        )

    seg_row = [" "] * total
    for i, r in enumerate(rendered):
        col = margin + i * step + (slot - _dwidth(r)) // 2
        _put(seg_row, col, r)
    lines.append("".join(seg_row))
    return "\n".join(line.rstrip() for line in lines)


def _change_tier_band(before_tier, after_tier, name: str, center, seg_ids, total: int) -> list[str]:
    """The label + connector rows for one tier's before→after association change."""
    before_links = before_tier.links if before_tier is not None else set()
    after_links = after_tier.links if after_tier is not None else set()
    # Autoseg id → bundle (prefer the after-state bundle; fall back to before for a removed one).
    bundles: dict[int, object] = {}
    for tier in (after_tier, before_tier):
        if tier is not None:
            for autoseg in tier.autosegs:
                bundles.setdefault(autoseg.id, autoseg.bundle)

    label_row = [" "] * total
    conn_row = [" "] * total
    spreads: list[tuple[str, list[tuple[int, str]]]] = []  # (label, [(col, glyph)]) — many anchors
    singles: dict[int, list[tuple[str, str]]] = {}  # col → [(label, glyph)] — one anchor each
    for autoseg_id, bundle in bundles.items():
        before_anchors = {sid for (a, sid) in before_links if a == autoseg_id and sid in seg_ids}
        after_anchors = {sid for (a, sid) in after_links if a == autoseg_id and sid in seg_ids}
        all_anchors = before_anchors | after_anchors
        if not all_anchors:
            continue
        label = _label_from_bundle(bundle, name)
        cols_glyphs = [
            (center[sid], _change_glyph(sid, before_anchors, after_anchors)) for sid in all_anchors
        ]
        if len(all_anchors) > 1:
            spreads.append((label, cols_glyphs))
        else:
            singles.setdefault(cols_glyphs[0][0], []).append((label, cols_glyphs[0][1]))

    if not spreads and not singles:
        return []

    for label, cols_glyphs in spreads:  # one autoseg, many anchors — label centred over them
        cols = sorted(col for col, _ in cols_glyphs)
        mid = (cols[0] + cols[-1]) // 2
        _put(label_row, mid - (_dwidth(label) - 1) // 2, label)
        for col, glyph in cols_glyphs:
            conn_row[col] = glyph
    for col, items in singles.items():  # one anchor; several autosegs here ⇒ a contour, fanned out
        spread_out = range(-(len(items) - 1), len(items), 2)  # 1→[0], 2→[-1,1], 3→[-2,0,2], …
        for (label, glyph), offset in zip(items, spread_out, strict=True):
            _put(label_row, col + offset - (_dwidth(label) - 1) // 2, label)
            conn_row[col + offset] = glyph

    return ["".join(label_row), "".join(conn_row)]


def _change_glyph(sid: int, before_anchors: set[int], after_anchors: set[int]) -> str:
    """The association glyph for one anchor: kept, newly added (dashed), or delinked."""
    if sid in before_anchors and sid in after_anchors:
        return "│"  # association kept
    if sid in after_anchors:
        return "╎"  # association added (a spread / dock) — dashed
    return "╪"  # association removed — the delink bar


def _place_label(bundle) -> str | None:
    """The major place of articulation as a node label, or None if undefined."""
    if "labial" in bundle:
        return "Labial"
    if "lingual" in bundle:
        return "Dorsal" if "back" in bundle else "Coronal"
    return None


def _is_consonant(bundle) -> bool:
    spec = bundle.get("consonantal")
    return spec is not None and spec.value == 1


def render_place_change(nasal_before, nasal_after, trigger, project: Project) -> str:
    """Place assimilation as an autosegmental Place-tier diagram.

    The trigger's place node forks to both segments with the assimilating segment's link
    **dashed** (the spread, a new link), while that segment's old place is **delinked**
    (``╪``) below — the tone-change notation applied to the Place node.
    """
    new_place = _place_label(nasal_after) or "?"
    old_place = _place_label(nasal_before) or "?"
    nasal_sym = render_segment(nasal_before, project) or "?"
    trigger_sym = render_segment(trigger, project) or "?"
    nasal_col, trigger_col = 5, 15
    mid = (nasal_col + trigger_col) // 2
    width = trigger_col + 8
    rows = [[" "] * width for _ in range(6)]
    _put(rows[0], mid - _dwidth(new_place) // 2, new_place)  # the shared place node
    for x in range(nasal_col, trigger_col + 1):
        rows[1][x] = "─"
    rows[1][nasal_col], rows[1][trigger_col], rows[1][mid] = "┌", "┐", "┴"
    rows[2][nasal_col], rows[2][trigger_col] = "╎", "│"  # nasal link dashed (new); trigger solid
    rows[3][nasal_col], rows[3][trigger_col] = nasal_sym, trigger_sym
    rows[4][nasal_col] = "╪"  # the old place, delinked
    _put(rows[5], nasal_col - _dwidth(old_place) // 2, old_place)
    return "\n".join("".join(row).rstrip() for row in rows)


def render_place_changes(before: Form, after: Form, project: Project) -> list[str]:
    """A place-change diagram for each segment whose place assimilated to a neighbour's."""
    before_by_id = {segment.id: segment.bundle for segment in before.segments}
    segments = after.segments
    diagrams: list[str] = []
    for i, segment in enumerate(segments):
        old_bundle = before_by_id.get(segment.id)
        # Place assimilation is a consonant phenomenon: only a consonant whose place changed
        # is a candidate — a vowel that merely matches a neighbour's place by accident is not.
        if old_bundle is None or not _is_consonant(segment.bundle):
            continue
        old, new = _place_label(old_bundle), _place_label(segment.bundle)
        if old is None or new is None or old == new:
            continue
        # The trigger is the consonant neighbour (right first — regressive — then left) it matches.
        for j in (i + 1, i - 1):
            if (
                0 <= j < len(segments)
                and _is_consonant(segments[j].bundle)
                and _place_label(segments[j].bundle) == new
            ):
                diagrams.append(
                    render_place_change(old_bundle, segment.bundle, segments[j].bundle, project)
                )
                break
    return diagrams
