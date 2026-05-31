"""Stage 2 — Recursive backtracking match generator.

``match(elements, seq, pos, env)`` yields ``(next_pos, updated_env)`` for
every way the element list can match the sequence starting at *pos*.  Failed
branches simply stop yielding; the caller's ``for`` loop moves to the next
alternative, and because ``Env`` is frozen there is nothing to unwind.

Supported element types:
- ``Bundle`` with quantifier and negation — match one or more segments
- ``Boundary`` — zero-width positional assertion (# word, $ syllable)
- ``Null`` — zero-width insertion point (matches zero segments)
- ``Group`` — parenthesised group with optional quantifier
- ``Disjunction`` — alternation (``|``)
- ``Binding`` — capture a matched span under a name
- ``Ref`` — recall a previously saved reference
"""

from __future__ import annotations

from collections.abc import Iterator

from src.fortis.models.sequence import Sequence
from src.fortis.rules.elements import (
    _EMPTY_ENV,
    _ONE,
    Binding,
    Boundary,
    Bundle,
    Disjunction,
    Element,
    Env,
    Group,
    Null,
    Quantifier,
    Ref,
)


def match(
    elements: list[Element],
    seq: Sequence,
    pos: int,
    env: Env | None = None,
) -> Iterator[tuple[int, Env]]:
    """Yield ``(next_pos, updated_env)`` for every way *elements* matches *seq* from *pos*.

    Args:
        elements: The pattern to match (a list of Elements).
        seq: The sequence of feature bundles to match against.
        pos: The starting position in the sequence.
        env: The current environment (alpha bindings, refs, conditions).
            Defaults to an empty Env if not provided.

    Yields:
        ``(next_pos, updated_env)`` for each successful match.  ``next_pos``
        is the position in *seq* immediately after the last consumed segment.
    """
    if env is None:
        env = _EMPTY_ENV
    yield from _match_rest(elements, 0, seq, pos, env)


def _match_rest(
    elements: list[Element],
    idx: int,
    seq: Sequence,
    pos: int,
    env: Env,
) -> Iterator[tuple[int, Env]]:
    """Match elements[idx:] against seq starting at pos.

    This is the recursive core.  Each element type is dispatched to its
    own handler which yields (next_pos, env) for every way that element
    (and the remaining elements) can match.
    """
    # Base case: all elements consumed
    if idx >= len(elements):
        yield (pos, env)
        return

    el = elements[idx]

    if isinstance(el, Bundle):
        yield from _match_bundle(el, elements, idx, seq, pos, env)
    elif isinstance(el, Boundary):
        yield from _match_boundary(el, elements, idx, seq, pos, env)
    elif isinstance(el, Null):
        # Null matches zero segments — just advance to the next element
        yield from _match_rest(elements, idx + 1, seq, pos, env)
    elif isinstance(el, Group):
        yield from _match_quantified_group(el, elements, idx, seq, pos, env)
    elif isinstance(el, Disjunction):
        for branch in el.branches:
            expanded = branch + elements[idx + 1 :]
            yield from _match_rest(expanded, 0, seq, pos, env)
    elif isinstance(el, Ref):
        if el.name in env.refs:
            start, end = env.refs[el.name]
            span_len = end - start
            if pos + span_len <= len(seq.data):
                # Phase 1: check that the referenced span matches
                for offset in range(span_len):
                    if seq.data[pos + offset] != seq.data[start + offset]:
                        return
                yield from _match_rest(elements, idx + 1, seq, pos + span_len, env)
    elif isinstance(el, Binding):
        # Match the inner pattern, record the span in env.refs
        for next_pos, new_env in _match_rest(el.pattern, 0, seq, pos, env):
            updated = Env(
                alphas=new_env.alphas,
                refs={**new_env.refs, el.name: (pos, next_pos)},
            )
            yield from _match_rest(elements, idx + 1, seq, next_pos, updated)


# ---------------------------------------------------------------------------
# Bundle matching
# ---------------------------------------------------------------------------


def _match_bundle(
    bundle: Bundle,
    elements: list[Element],
    idx: int,
    seq: Sequence,
    pos: int,
    env: Env,
) -> Iterator[tuple[int, Env]]:
    """Match a Bundle element against the sequence.

    For quantifiers other than (1,1), delegates to _match_quantified.
    For the default (1,1) quantifier, matches exactly one segment.
    """
    quant = bundle.quantifier

    # Optimised path for the common case: exactly one match
    if quant is _ONE:
        if pos >= len(seq.data):
            return
        segment = seq.data[pos]
        if bundle.negated:
            if not segment.match_pattern(bundle.bundle, ignore_none=True):
                yield from _match_rest(elements, idx + 1, seq, pos + 1, env)
        else:
            if segment.match_pattern(bundle.bundle, ignore_none=True):
                yield from _match_rest(elements, idx + 1, seq, pos + 1, env)
        return

    # General quantifier path
    yield from _match_quantified(bundle, quant, elements, idx, seq, pos, env)


def _match_quantified(
    bundle: Bundle,
    quant: Quantifier,
    elements: list[Element],
    idx: int,
    seq: Sequence,
    pos: int,
    env: Env,
) -> Iterator[tuple[int, Env]]:
    """Match a Bundle element with an arbitrary quantifier.

    Tries matching the bundle between quant.min and quant.max times.
    For each valid count, continues matching the remaining elements.
    """
    # Collect all positions reachable by matching the bundle 0..max times
    # We do this iteratively, trying each count in turn
    current_pos = pos
    count = 0

    while True:
        # If we've matched enough (≥ min), try continuing with remaining elements
        if count >= quant.min:
            yield from _match_rest(elements, idx + 1, seq, current_pos, env)

        # Stop if we've reached max
        if quant.max is not None and count >= quant.max:
            break

        # Try to match one more occurrence
        if current_pos >= len(seq.data):
            break

        segment = seq.data[current_pos]
        if bundle.negated:
            if segment.match_pattern(bundle.bundle, ignore_none=True):
                break  # negated bundle matched — negation fails
        else:
            if not segment.match_pattern(bundle.bundle, ignore_none=True):
                break  # bundle didn't match — can't extend

        current_pos += 1
        count += 1


# ---------------------------------------------------------------------------
# Group matching
# ---------------------------------------------------------------------------


def _match_quantified_group(
    group: Group,
    elements: list[Element],
    idx: int,
    seq: Sequence,
    pos: int,
    env: Env,
) -> Iterator[tuple[int, Env]]:
    """Match a Group element with its quantifier.

    For quantifier (1,1): match the inner elements once (equivalent to
    flattening).  For other quantifiers, try matching the inner elements
    min..max times, yielding after each valid count ≥ min.
    """
    quant = group.quantifier

    # Optimised path for the common case: exactly one match
    if quant is _ONE:
        # Flatten: match inner elements once then continue with remaining
        expanded = group.elements + elements[idx + 1 :]
        yield from _match_rest(expanded, 0, seq, pos, env)
        return

    # General quantified group: try matching the group 0..max times
    current_pos = pos
    current_env = env
    count = 0

    while True:
        # If we've matched enough (≥ min), try continuing with remaining elements
        if count >= quant.min:
            yield from _match_rest(elements, idx + 1, seq, current_pos, current_env)

        # Stop if we've reached max
        if quant.max is not None and count >= quant.max:
            break

        # Try to match one more occurrence of the inner elements
        found_match = False
        for next_pos, next_env in _match_rest(group.elements, 0, seq, current_pos, current_env):
            current_pos = next_pos
            current_env = next_env
            found_match = True
            break  # Take the first match; backtracking explores alternatives

        if not found_match:
            break

        count += 1


# ---------------------------------------------------------------------------
# Boundary matching
# ---------------------------------------------------------------------------


def _match_boundary(
    boundary: Boundary,
    elements: list[Element],
    idx: int,
    seq: Sequence,
    pos: int,
    env: Env,
) -> Iterator[tuple[int, Env]]:
    """Match a Boundary element (zero-width assertion).

    Word boundary (#): matches at position 0 or at the end of the sequence.
    Syllable boundary ($): matches at positions stored in
        ``seq.syllable_boundaries``.  Position i means "between segment i-1
        and i".  Also matches at position 0 (start) and len(data) (end).
    """
    if boundary.kind == "word":
        if pos == 0 or pos == len(seq.data):
            yield from _match_rest(elements, idx + 1, seq, pos, env)
    elif boundary.kind == "syllable":
        if pos in seq.syllable_boundaries:
            yield from _match_rest(elements, idx + 1, seq, pos, env)
