"""Autosegmental diagrams as monospace Unicode text.

The classic autosegmental picture, in text. A **suprasegmental** change (tone, stress) is drawn
as a *before* → *after* pair, one column per syllable (the tone-bearing units), with the tones on
a tier **below** the segments joined by association lines: a tone forking up to several syllables
is a **spread**, several tones stacked under one syllable a **contour**. A **segmental** node
spread (place assimilation, vowel harmony) is drawn per segment with the spread node *above* the
row. Association lines are styled ``│`` kept · ``┊`` added · ``╪`` delinked. Box-drawing characters
keep it readable in any monospace IPA font.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from src.fortis.application.rendering import render_segment, render_syllabified
from src.fortis.application.syllabifying import syllabify, syllables
from src.fortis.application.tiers import lower_tiers
from src.fortis.general.presenting import present_value
from src.fortis.general.utils import is_combining
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

    ``label`` is the spreading thing as a stack of display lines (a one-line tone ``[˦]``, or a
    place path ``[place, tongue_body, +high·-low·+back·dorsal]`` drawn as a little geometry);
    ``links`` pairs each anchor's index in the ``after`` segment row with its association glyph
    (``│`` kept · ``┊`` added · ``╪`` delinked); ``replaced`` is an optional ``(index, old_label)``
    drawn *below* that anchor — the delinked old value a node spread overwrote (``None`` for tiers).
    """

    label: list[str]
    links: tuple[tuple[int, str], ...]
    replaced: tuple[int, list[str]] | None = None


def _dwidth(text: str) -> int:
    """Display width — combining marks occupy no column."""
    return sum(0 if is_combining(ch) else 1 for ch in text)


def _lw(lines: list[str]) -> int:
    """The widest display line of a stacked label."""
    return max((_dwidth(line) for line in lines), default=0)


def _margin(widths: Iterable[int], floor: int = 4) -> int:
    """Side padding wide enough that a label centred over the first/last anchor never clips.

    A centred label overhangs its anchor by half its width on each side, so the side margins must
    cover that overhang — feature labels (``oral·lingual·back…``) are far wider than the old
    glyphs. ``floor`` (≥4) keeps room for a floating autoseg even when there are no labels.
    """
    return max(floor, max(widths, default=0) // 2 + 1)


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


def _geometry(slot: int, step: int, margin: int, count: int) -> tuple[int, list[int]]:
    """The row width and each segment's centre column — the shared coordinate system.

    Both diagram paths (snapshot and change) derive their canvas here, so the geometry
    can't drift between them.
    """
    total = margin + count * step - _SEP + margin
    return total, [margin + i * step + slot // 2 for i in range(count)]


def _segment_row(rendered: list[str], slot: int, step: int, margin: int, total: int) -> list[str]:
    """The segment row: each rendered segment centred in its slot."""
    row = [" "] * total
    for i, text in enumerate(rendered):
        _put(row, margin + i * step + (slot - _dwidth(text)) // 2, text)
    return row


def _syllables(form: Form, project: Project) -> list[tuple[str, int | None]]:
    """One entry per syllable (the tone-bearing units): rendered surface text and nucleus id.

    Each syllable has exactly one nucleus, so a syllable column and its nucleus anchor are the
    same TBU — the column is a display grouping over the ``syllables`` lens.
    """
    lowered = lower_tiers(form)
    # syllabify no longer raises — an unsplittable cluster falls back to a sonority split and
    # warns, so it always returns boundaries here.
    boundaries = syllabify(
        lowered, project.sonorities, project.syllable_parts, project.time, project.letters
    )
    nucleus_part = project.syllable_parts.get_nucleus(project.time)
    nucleus = nucleus_part.definition if nucleus_part is not None else None
    columns: list[tuple[str, int | None]] = []
    for syllable in syllables(lowered, boundaries, nucleus):
        chunk = lowered[syllable.start : syllable.end]
        # render the whole syllable so an after-mark (tone letter) lands at its edge: kat˦, not ka˦t
        text = render_syllabified(chunk, frozenset({0, len(chunk)}), project, dots=False) or "∅"
        nucleus_id = form.segments[syllable.nucleus].id if syllable.nucleus is not None else None
        columns.append((text, nucleus_id))
    return columns


@dataclass(frozen=True)
class _Tone:
    """One autosegment drawn below the syllable row.

    Its ``label``, the syllable ``cols`` it links to, and the association ``glyph`` per column
    (``│`` kept · ``┊`` added · ``╪`` delinked).
    """

    label: str
    cols: tuple[int, ...]
    glyph: dict[int, str]


def _tones(
    form: Form, project: Project, before: Form | None
) -> tuple[list[tuple[str, int | None]], list[_Tone], list[tuple[int, str, str]]]:
    """The tier autosegs to draw, styled vs *before* (``None`` ⇒ a plain snapshot: all ``│``).

    Returns the syllables, the linked tones, and the **floating** tones as ``(column, side, label)``
    — an unlinked autoseg positioned beside the syllable of its ``float_hosts`` segment, drawn with
    no association line.
    """
    syllables = _syllables(form, project)
    col_of = {nucleus: i for i, (_text, nucleus) in enumerate(syllables)}
    tones: list[_Tone] = []
    floats: list[tuple[int, str, str]] = []
    drawn: set[int] = set()
    for name, tier in form.tiers.items():
        before_links = before.tiers[name].links if before and name in before.tiers else set()
        for autoseg in tier.autosegs:
            cols = tuple(
                sorted({col_of[s] for (a, s) in tier.links if a == autoseg.id and s in col_of})
            )
            if not cols:  # unlinked ⇒ floating; place beside its lexical host, no line
                host = tier.float_hosts.get(autoseg.id)
                if host is not None and host[0] in col_of:
                    label = _label_from_bundle(autoseg.bundle, project)
                    floats.append((col_of[host[0]], host[1], label))
                continue
            drawn.add(autoseg.id)
            was = {col_of[s] for (a, s) in before_links if a == autoseg.id and s in col_of}
            glyph = {c: ("│" if before is None or c in was else "┊") for c in cols}
            tones.append(_Tone(_label_from_bundle(autoseg.bundle, project), cols, glyph))
    if before is not None:  # autosegs the rule delinked: draw at their old syllable with ╪
        for btier in before.tiers.values():
            for autoseg in btier.autosegs:
                if autoseg.id in drawn:
                    continue
                cols = tuple(
                    sorted({col_of[s] for (a, s) in btier.links if a == autoseg.id and s in col_of})
                )
                if cols:
                    label = _label_from_bundle(autoseg.bundle, project)
                    tones.append(_Tone(label, cols, dict.fromkeys(cols, "╪")))
    return syllables, tones, floats


def _tonal_block(form: Form, project: Project, before: Form | None = None) -> list[str]:
    """A tier-below per-syllable diagram as rows: the syllables, then their tones below them.

    Single-anchor tones stack under their syllable; a spread is a fork opening *up* to the
    syllables it reaches; the tone is styled against *before* when given (the after side of a
    change). Tier below the segments, one column per syllable — the classic tonal notation.
    """
    syllables, tones, floats = _tones(form, project, before)
    n = len(syllables)
    stacked: list[list[_Tone]] = [[] for _ in range(n)]  # column → single-anchor tones
    forks: list[_Tone] = []
    for tone in tones:
        if len(tone.cols) == 1:
            stacked[tone.cols[0]].append(tone)
        else:
            forks.append(tone)
    widths = [
        max([_dwidth(text), *(_dwidth(t.label) for t in stacked[i]), 1])
        for i, (text, _n) in enumerate(syllables)
    ]
    gap = 3
    centers: list[int] = []
    x = 0
    for w in widths:
        centers.append(x + (w - 1) // 2)  # middle of the column [x, x+w) — content fills it exactly
        x += w + gap
    total = max(x - gap, 1)

    def _float_start(col: int, side: str, text: str) -> int:
        """Where a floating label starts: just past its host syllable, on *side*."""
        if side == "after":
            return centers[col] + widths[col] // 2 + 1
        return centers[col] - (widths[col] - 1) // 2 - 1 - _dwidth(text)

    # A spread's label sits below the fork (and a float beside its host) and can be wider than the
    # span — pad the canvas so nothing clips at either edge.
    pad_left = pad_right = 0
    for tone in forks:
        leg_cols = [centers[c] for c in tone.cols]
        mid = (min(leg_cols) + max(leg_cols)) // 2
        start = mid - (_dwidth(tone.label) - 1) // 2
        pad_left = max(pad_left, -start)
        pad_right = max(pad_right, start + _dwidth(tone.label) - total)
    for col, side, label in floats:
        text = f"({label})"
        start = _float_start(col, side, text)
        pad_left = max(pad_left, -start)
        pad_right = max(pad_right, start + _dwidth(text) - total)
    centers = [c + pad_left for c in centers]
    total += pad_left + max(0, pad_right)

    def blank() -> list[str]:
        return [" "] * total

    seg = blank()
    for i, (text, _n) in enumerate(syllables):
        _put(seg, centers[i] - (_dwidth(text) - 1) // 2, text)
        if i:
            _put(seg, (centers[i - 1] + centers[i]) // 2, "-")
    rows = [seg]
    for k in range(max((len(s) for s in stacked), default=0)):  # stacked single-anchor tones
        line, label = blank(), blank()
        for i in range(n):
            if k < len(stacked[i]):
                tone = stacked[i][k]
                line[centers[i]] = tone.glyph[i]
                _put(label, centers[i] - (_dwidth(tone.label) - 1) // 2, tone.label)
        rows += [line, label]
    for tone in forks:  # a spread: styled legs up to each syllable, a bar joining down to the label
        legs, bar, label = blank(), blank(), blank()
        leg_cols = [centers[c] for c in tone.cols]
        for c in tone.cols:
            legs[centers[c]] = tone.glyph[c]
        lo, hi = min(leg_cols), max(leg_cols)
        for column in range(lo, hi + 1):
            bar[column] = "─"
        bar[lo], bar[hi] = "└", "┘"
        mid = (lo + hi) // 2
        bar[mid] = "┼" if mid in leg_cols else "┬"
        _put(label, mid - (_dwidth(tone.label) - 1) // 2, tone.label)
        rows += [legs, bar, label]
    if floats:  # floating (unlinked) tones at their lexical position, parenthesised, no line
        row = blank()
        for col, side, label in floats:
            text = f"({label})"
            _put(row, _float_start(col, side, text), text)
        rows.append(row)
    return ["".join(r).rstrip() for r in rows]


def _join_pair(left: list[str], right: list[str]) -> str:
    """Two blocks side by side, joined by ``→`` on the segment row."""
    width = max((_dwidth(r) for r in left), default=0)
    height = max(len(left), len(right))
    left = left + [""] * (height - len(left))
    right = right + [""] * (height - len(right))
    rows = []
    for i in range(height):
        padded = left[i] + " " * (width - _dwidth(left[i]))
        rows.append((padded + ("  →  " if i == 0 else "     ") + right[i]).rstrip())
    return "\n".join(rows)


def render_autosegmental(form: Form, project: Project) -> str:
    """A form's suprasegmental tiers as a per-syllable diagram (syllables over their tones)."""
    if not form.segments:
        return "(empty)"
    return "\n".join(_tonal_block(form, project))


def render_autosegmental_change(before: Form, after: Form, project: Project) -> str:
    """One rule's tier change as a *before* → *after* pair of per-syllable diagrams.

    Each association is styled on the after side, the classic rule-as-diagram notation: ``│`` kept ·
    ``┊`` added (a spread/dock) · ``╪`` delinked — read off the before/after tiers.
    """
    if not after.segments:
        return render_autosegmental(after, project)
    return _join_pair(_tonal_block(before, project), _tonal_block(after, project, before=before))


def _tier_changed(before: Form, after: Form) -> bool:
    """Whether any suprasegmental tier's autosegments or associations differ (a tonal change)."""
    for name in {*before.tiers, *after.tiers}:
        b, a = before.tiers.get(name), after.tiers.get(name)
        if (b.links if b else set()) != (a.links if a else set()):
            return True
        if {x.id: dict(x.bundle) for x in (b.autosegs if b else [])} != {
            x.id: dict(x.bundle) for x in (a.autosegs if a else [])
        }:
            return True
    return False


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
    # group's width (sum of labels + the gaps), not just a single label, so it doesn't overflow.
    anchor_widths: dict[int, list[int]] = {}
    for s in spreads:
        if len(s.links) == 1:
            anchor_widths.setdefault(s.links[0][0], []).append(_lw(s.label))
    group_widths = [sum(ws) + len(ws) - 1 for ws in anchor_widths.values()]
    margin = _margin([_lw(label) for label in labels] + group_widths)
    total, centers = _geometry(slot, step, margin, len(segments))

    def _centre(row: list[str], col: int, line: str) -> None:
        _put(row, col - (_dwidth(line) - 1) // 2, line)

    above: list[list[str]] = []
    if spreads:
        conn_row = [" "] * total
        fork_row = [" "] * total  # the branch row (label above, descenders below)
        # Stacked label rows: tall enough for the deepest label, each label bottom-aligned so its
        # terminal line sits just above the fork (nearest the segments), the root node up top.
        height = max([len(s.label) for s in spreads] + [1])
        label_rows = [[" "] * total for _ in range(height)]

        def stack(col: int, lines: list[str]) -> None:  # centre a stacked label on col
            for k, line in enumerate(lines):
                _centre(label_rows[height - len(lines) + k], col, line)

        multi = [s for s in spreads if len(s.links) > 1]
        singles: dict[int, list[tuple[list[str], str]]] = {}  # col → [(label, glyph)] — one anchor
        for s in spreads:
            if len(s.links) == 1:
                idx, glyph = s.links[0]
                singles.setdefault(centers[idx], []).append((s.label, glyph))
        for s in multi:  # one autoseg, several anchors
            cols_glyphs = [(centers[idx], glyph) for idx, glyph in s.links]
            cols = sorted(col for col, _ in cols_glyphs)
            mid = (cols[0] + cols[-1]) // 2
            stack(mid, s.label)  # the label stack, above the fork
            for x in range(cols[0], cols[-1] + 1):  # the branch line spanning the anchors
                fork_row[x] = "─"
            for c in cols:
                fork_row[c] = "┬"
            fork_row[cols[0]], fork_row[cols[-1]] = "┌", "┐"
            fork_row[mid] = "┼" if mid in cols else "┴"  # the join, under the label
            for col, glyph in cols_glyphs:  # styled descender: │ kept · ┊ added · ╪ delinked
                conn_row[col] = glyph
        for col, items in singles.items():  # autosegs sharing one anchor
            if len(items) == 1:  # the common case: one spread on one anchor, centred
                lines, glyph = items[0]
                stack(col, lines)
                conn_row[col] = glyph
            else:  # a contour change ⇒ lay the (one-line tone) labels side by side, no overlap
                flat = [("·".join(lines), glyph) for lines, glyph in items]
                widths = [_dwidth(text) for text, _ in flat]
                x = col - (sum(widths) + (len(flat) - 1)) // 2  # centre the group on the anchor
                for (text, glyph), w in zip(flat, widths, strict=True):
                    _put(label_rows[-1], x, text)
                    conn_row[x + (w - 1) // 2] = glyph  # descender under each label's centre
                    x += w + 1
        above = [*label_rows, fork_row, conn_row] if multi else [*label_rows, conn_row]

    seg_row = _segment_row(rendered, slot, step, margin, total)

    below: list[list[str]] = []
    for s in spreads:  # the delinked old value a node spread overwrote, under its anchor
        if s.replaced is not None:
            idx, old_label = s.replaced
            col = centers[idx]
            delink_row = [" "] * total
            delink_row[col] = "╪"
            below.append(delink_row)
            for line in reversed(old_label):  # leaves nearest the ╪, the root node furthest below
                row = [" "] * total
                _centre(row, col, line)
                below.append(row)

    lines = [*above, seg_row, *below]
    return "\n".join("".join(row).rstrip() for row in lines)


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


def _node_label(feature: str, bundle: FeatureBundle, project: Project) -> list[str]:
    """The exchanged node's path as a stack of display lines — a little geometry, not one long
    ``·`` run::

                    place
             tongue_body
        +high·-low·+back·dorsal

    Naming starts at the rule's exchanged feature (the ``~n`` node — e.g. ``place``). Each node on
    the path that still has a present child gets its own line; the terminal features (the leaves)
    share the last line, joined by ``·``. So the spread-in place and the delinked old place are
    named from the same root and the reader sees where the two diverge, level by level.
    """
    names = [feature, *(d for d in project.features.descendants(feature) if d in bundle)]
    present = set(names)
    lines, leaves = [], []
    for name in names:
        if any(child in present for child in project.features.children(name)):
            lines.append(_feature_label(name, bundle, project))  # an internal node on the path
        else:
            leaves.append(_feature_label(name, bundle, project))  # a terminal feature
    if leaves:
        lines.append("·".join(leaves))
    return lines


def _rule_spreads(before: Form, after: Form, rule: Rule | None, project: Project) -> list[_Spread]:
    """Every segmental spread the rule performed, as ``_Spread`` forks.

    The autosegmental reading of its ``~n`` operations, irrespective of which feature spread
    (place assimilation and vowel harmony are the same operation through different features).
    For each spread feature, the *after* segments carrying it are grouped by their subtree value
    (one value = one shared autosegment); a group with both a changed anchor (the link the rule
    added → ``┊``) and an unchanged source (``│``) is a spread. A lone changed anchor that
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
            # By default label by the spread node itself (a harmony spread of ``back`` reads
            # ``back``): a unary node's bare name, a binary feature's sign, a scalar's value.
            label = [_feature_label(feature, segments[indices[0]].bundle, project)]
            links = tuple((i, "┊" if i in changed else "│") for i in indices)
            replaced = None
            if len(changed) == 1 and old[changed[0]]:  # one anchor over a non-empty old value
                # A node spread that overwrote a place: the incoming and the delinked old node are
                # the same exchanged feature (``oral``), so name each from that node down through
                # its specified children — ``oral·lingual·back·aperture: high`` (spread in) vs
                # ``oral·lingual·front·anterior`` (delinked) — showing where the two places differ.
                now = segments[indices[0]].bundle
                was = before_by_id[segments[changed[0]].id]
                label = _node_label(feature, now, project)
                replaced = (changed[0], _node_label(feature, was, project))
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
            levels = (
                definition.values.get(v, str(v)) if isinstance(v, int) else str(v) for v in value
            )
            return f"{feature}: " + ">".join(levels)
        if isinstance(value, int):
            return f"{feature}: {definition.values.get(value, str(value))}"
    return feature


def render_segmental_spreads(
    before: Form, after: Form, rule: Rule | None, project: Project
) -> list[tuple[str, str]]:
    """One canonical rule diagram for each segmental spread (place, harmony, ``~n``).

    The classic autosegmental single picture: the ``~n`` node forks over the **input** segments,
    ``│`` its kept link on the trigger and ``┊`` the newly spread (dashed) link on the target, with
    the target's overwritten old node struck out below (``╪``, the delink double-bar). Drawn over
    ``before`` — the input the rule operates on — so the target segment's derived identity (``n``
    becoming ``ŋ``) is left to fall out of the Place change rather than pre-empted in the picture.
    Vowel harmony spreads several nodes at once (``back`` and ``labial``): one diagram each.
    """
    spreads = _rule_spreads(before, after, rule, project)
    # The sublabel (the CLI md ``###`` heading) stays a flat one-liner; the diagram stacks it.
    return [("·".join(s.label), _draw(before.segments, [s], project)) for s in spreads]


def render_change(
    before: Form, after: Form, rule: Rule | None, project: Project
) -> list[tuple[str, str]]:
    """Every autosegmental change for one rule, as ``(sublabel, diagram)`` — the single renderer.

    A *tier* change (tone, stress) yields a *before* → *after* pair of per-syllable diagrams (all
    tiers together) with an empty sublabel; each *segmental* spread the rule performed via ``~n`` —
    place assimilation, vowel harmony, or any other — yields a fork sublabelled by its spread node
    (``back``, ``labial``, ``oral``), detected from the rule's operations not guessed from which
    features changed. Display order: tier change, then the segmental spreads. All share the
    ``│`` kept · ``┊`` added · ``╪`` delinked notation.
    """
    diagrams: list[tuple[str, str]] = []
    if _tier_changed(before, after):
        diagrams.append(("", render_autosegmental_change(before, after, project)))
    diagrams.extend(render_segmental_spreads(before, after, rule, project))
    return diagrams
