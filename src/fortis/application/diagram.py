"""Autosegmental tier diagrams as monospace Unicode text.

The classic autosegmental picture, in text: autosegments sit on tier rows above the
segments, joined to their anchors by association lines. One autosegment forking to
several anchors is **spread**; several converging on one anchor is a **contour**; an
unlinked autosegment **floats** at its lexical position with no line. Rendered with
box-drawing characters so it stays readable in any monospace IPA font.
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

from src.fortis.application.rendering import render_segment
from src.fortis.general.presenting import present_value
from src.fortis.general.utils import is_combining
from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle, ResultBundle
from src.fortis.models.elements import Bound, Disjunction, Group, Negated, Quantified, ResultElem
from src.fortis.models.features import FeatureKind
from src.fortis.models.form import Form
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule
from src.fortis.models.values import AutosegRecall

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


def _margin(labels: list[str], floor: int = 4) -> int:
    """Side padding wide enough that a label centred over the first/last anchor never clips.

    A centred label overhangs its anchor by half its width on each side, so the side margins must
    cover that overhang — feature labels (``oral·lingual·back…``) are far wider than the old
    glyphs. ``floor`` (≥4) keeps room for a floating autoseg even when there are no labels.
    """
    widest = max((_dwidth(label) for label in labels), default=0)
    return max(floor, widest // 2 + 1)


def _label(autoseg, project: Project) -> str:
    """A short label for one autosegment (``tone: high``, a place subtree, …)."""
    return _label_from_bundle(autoseg.bundle, project)


def _label_from_bundle(bundle, project: Project) -> str:
    """Label an autoseg by its features, not a glyph — an autosegmental tier carries features.

    Each present feature is shown with the geometry tree's ``_feature_label`` (``tone: high``,
    ``+back``, a unary node's bare name), joined by ``·``. A suprasegmental autoseg is one
    feature (``tone: high``, ``stress: primary``); a place-node spread is its whole present
    subtree (``oral·lingual·back``). Derived from the feature inventory, so any geometry works.
    """
    return "·".join(_feature_label(f, bundle, project) for f in bundle) or "?"


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
    labels = [_label(a, project) for tier in form.tiers.values() for a in tier.autosegs]
    step = slot + _SEP
    if len(labels) >= 2:  # two labels on neighbouring anchors must not collide on the tier row
        step = max(step, max(_dwidth(label) for label in labels) + 2)
    margin = _margin(labels)  # wide enough that a centered feature label never clips at the edges
    total = margin + len(segs) * step - _SEP + margin
    center = {s.id: margin + i * step + slot // 2 for i, s in enumerate(segs)}
    pos = {s.id: i for i, s in enumerate(segs)}

    lines: list[str] = []
    for tier in form.tiers.values():
        if tier.autosegs:
            lines.extend(_tier_band(tier, center, pos, segs, total, project))

    seg_row = [" "] * total
    for i, r in enumerate(rendered):
        col = margin + i * step + (slot - _dwidth(r)) // 2
        _put(seg_row, col, r)
    lines.append("".join(seg_row))
    return "\n".join(line.rstrip() for line in lines)


def _tier_band(
    tier: AutosegmentalTier, center, pos, segs, total: int, project: Project
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
        label = _label(autoseg, project)
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
            label = _label(group[0], project)
            _put(label_row, col - (_dwidth(label) - 1) // 2, label)
            conn_row[col] = "│"
        else:  # several tones converging on one anchor — a contour
            labels = [_label(a, project) for a in group]
            left, right = labels[0], labels[-1]
            _put(label_row, col - 1 - (_dwidth(left) - 1), left)  # left label's right edge at col-1
            _put(label_row, col + 1, right)  # right label starts just past the join
            conn_row[col - 1], conn_row[col], conn_row[col + 1] = "└", "┬", "┘"

    for autoseg in floats:  # unlinked: shown at its lexical gap, no line
        label = _label(autoseg, project)
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
    return _draw(after.segments, _tier_spreads(before, after, project), project)


def _tier_spreads(before: Form, after: Form, project: Project) -> list[_Spread]:
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
            spreads.append(_Spread(_label_from_bundle(bundle, project), links))
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
    labels = [s.label for s in spreads] + [s.replaced[1] for s in spreads if s.replaced]
    # A contour change lays several labels side by side on one anchor — size the margin to that
    # group's width, not just a single label, so the group doesn't overflow the row edge.
    groups: dict[int, int] = {}
    for s in spreads:
        if len(s.links) == 1:
            groups[s.links[0][0]] = groups.get(s.links[0][0], -1) + _dwidth(s.label) + 1
    widest = max([_dwidth(label) for label in labels] + list(groups.values()), default=0)
    margin = max(4, widest // 2 + 1)  # fit the labels, single or grouped, without clipping
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
        for col, items in singles.items():  # autosegs sharing one anchor
            if len(items) == 1:  # the common case: one spread on one anchor, centred
                label, glyph = items[0]
                _put(label_row, col - (_dwidth(label) - 1) // 2, label)
                conn_row[col] = glyph
            else:  # a contour change ⇒ lay the (wide feature) labels side by side, no overlap
                widths = [_dwidth(label) for label, _ in items]
                x = col - (sum(widths) + (len(items) - 1)) // 2  # centre the group on the anchor
                for (label, glyph), w in zip(items, widths, strict=True):
                    _put(label_row, x, label)
                    conn_row[x + (w - 1) // 2] = glyph  # descender under each label's centre
                    x += w + 1
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


def _result_bundles(elements: tuple) -> Iterator[ResultBundle]:
    """Yield each ``ResultElem``'s bundle in a result element sequence, descending into nesting."""
    for element in elements:
        match element:
            case ResultElem(bundle):
                yield bundle
            case Quantified(inner, _) | Negated(inner) | Bound(_, inner):
                yield from _result_bundles((inner,))
            case Group(inner):
                yield from _result_bundles(inner)
            case Disjunction(branches):
                for branch in branches:
                    yield from _result_bundles(branch)
            case _:
                pass


def _spread_features(rule: Rule | None, project: Project) -> set[str]:
    """The segmental features the rule SPREADS — its result's ``~n`` node-recalls.

    Reduced to the highest node (a recalled ancestor subsumes its descendants — ``oral`` over
    its place leaves, ``labial`` over ``rounded``). Empty with no rule (e.g. a tier-only change).
    """
    if rule is None:
        return set()
    feats = {
        feature
        for bundle in _result_bundles(rule.sd.result)
        for feature, spec in bundle.items()
        if isinstance(spec.value, AutosegRecall) and project.features.is_segmental(feature)
    }
    return {f for f in feats if not any(f in project.features.descendants(a) for a in feats)}


def _subtree(bundle: FeatureBundle, feature: str, project: Project) -> frozenset:
    """*feature* and its present descendants in *bundle* as a frozen ``(name, value)`` set.

    The unit a node-spread copies, so two equal snapshots are one shared autosegment (∅ if absent).
    """
    names = (feature, *project.features.descendants(feature))
    return frozenset((n, bundle[n].value) for n in names if n in bundle)


def _rule_spreads(before: Form, after: Form, rule: Rule | None, project: Project) -> list[_Spread]:
    """Every segmental spread the rule performed, as ``_Spread`` forks.

    The autosegmental reading of its ``~n`` operations, irrespective of which feature spread
    (place assimilation and vowel harmony are the same operation through different features).
    For each spread feature, the *after* segments carrying it are grouped by their subtree value
    (one value = one shared autosegment); a group with both a changed anchor (the link the rule
    added → ``╎``) and an unchanged source (``│``) is a spread. A lone changed anchor that
    replaced a non-empty old subtree also shows that old value delinked (``╪``), as place does.
    """
    before_by_id = {segment.id: segment.bundle for segment in before.segments}
    segments = after.segments
    spreads: list[_Spread] = []
    for feature in sorted(_spread_features(rule, project)):
        groups: dict[frozenset, list[int]] = {}
        for i, segment in enumerate(segments):
            if feature in segment.bundle:
                groups.setdefault(_subtree(segment.bundle, feature, project), []).append(i)
        for value, indices in groups.items():
            old = {
                i: _subtree(before_by_id.get(segments[i].id, FeatureBundle()), feature, project)
                for i in indices
            }
            changed = [i for i in indices if old[i] != value]
            if not changed or len(changed) == len(indices):  # need a stable source to spread from
                continue
            # Label by the spread node itself (``oral``), not its whole subtree — a unary node's
            # bare name, a binary feature's sign, a scalar's value (the geometry tree's labeller).
            label = _feature_label(feature, segments[indices[0]].bundle, project)
            links = tuple((i, "╎" if i in changed else "│") for i in indices)
            replaced = None
            if len(changed) == 1 and old[changed[0]]:  # one anchor over a non-empty old value
                was = before_by_id[segments[changed[0]].id]
                replaced = (changed[0], _feature_label(feature, was, project))
            spreads.append(_Spread(label, links, replaced))
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
    """A feature's label: sign for binary (``+voice``), value for scalar, bare name for unary.

    A scalar may carry a contour (a tuple, e.g. a tone on its tier): each level shows its own
    value label, joined with ``>`` (``tone: low>extra-low>high``). A geometry-tree segment only
    ever has a single int, so this matters only for a tier autoseg's label.
    """
    definition = project.features[feature]
    value = bundle[feature].value
    if definition.kind == FeatureKind.binary and isinstance(value, int):
        return f"{present_value(value)}{feature}"
    if definition.kind == FeatureKind.scalar:
        if isinstance(value, tuple):
            return f"{feature}: " + ">".join(definition.values.get(v, str(v)) for v in value)
        if isinstance(value, int):
            return f"{feature}: {definition.values.get(value, str(value))}"
    return feature


def render_segmental_spreads(
    before: Form, after: Form, rule: Rule | None, project: Project
) -> list[str]:
    """A fork diagram for each segmental spread *rule* performed (place, harmony, any ``~n``)."""
    spreads = _rule_spreads(before, after, rule, project)
    return [_draw(after.segments, [s], project) for s in spreads]


def render_change(before: Form, after: Form, rule: Rule | None, project: Project) -> list[str]:
    """Every autosegmental change for one rule, as fork diagrams — the single renderer to call.

    One entry point for every autosegmental process, all sharing the label/fork/descender
    notation (``│`` kept · ``╎`` added · ``╪`` delinked). A *tier* autosegment (tone, stress)
    whose links changed yields one diagram (all tiers together); each *segmental* spread the
    rule performed via ``~n`` — place assimilation, vowel harmony, or any other — yields a fork,
    detected from the rule's operations rather than guessed from which features changed. Returned
    in display order: tier change, then the segmental spreads.
    """
    diagrams: list[str] = []
    tier = render_autosegmental_change(before, after, project)
    if "╎" in tier or "╪" in tier:  # the tier diagram is meaningful only when a link changed
        diagrams.append(tier)
    diagrams.extend(render_segmental_spreads(before, after, rule, project))
    return diagrams
