"""Stages 3 & 4 — Locus finding and rewrite, plus the top-level apply_rules.

Stage 3 (locus finding):  For each position in the sequence, match left
context so it lands exactly at the target position, then match the target,
then match the right context.  If the exception generator yields nothing,
the locus is valid.

Stage 4 (rewrite):  From the winning Env and target span, instantiate the
result template and splice into the Sequence.  Supports feature-bundle
deltas (combine_with), insertion (Null in target), deletion (Null in result),
and reference copying (Ref).

The top-level ``apply_rules`` orchestrates the full pipeline: for each rule
(in time order), find all loci, then rewrite simultaneously (one rule
sees the original state for all its matches).
"""

from __future__ import annotations

from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.sequence import Sequence
from src.fortis.rules.elements import _EMPTY_ENV, Application, Bundle, Disjunction, Element, Env, Group, Null, Ref
from src.fortis.rules.match import match
from src.fortis.rules.rule import Rule

# ---------------------------------------------------------------------------
# Locus — a match site in the sequence
# ---------------------------------------------------------------------------


class Locus:
    """A site where a rule's target matches in the sequence.

    Attributes:
        start: Start index (inclusive) of the target span.
        end: End index (exclusive) of the target span.
        env: The environment captured during matching (alpha bindings, refs).
    """

    __slots__ = ("start", "end", "env")

    def __init__(self, start: int, end: int, env: Env) -> None:
        """Create a locus at the given span with the captured environment."""
        self.start = start
        self.end = end
        self.env = env

    def __repr__(self) -> str:
        """Return a compact string representation of the locus."""
        return f"Locus({self.start}:{self.end})"


# ---------------------------------------------------------------------------
# Stage 3 — Locus finding
# ---------------------------------------------------------------------------


def find_loci(rule: Rule, seq: Sequence) -> list[Locus]:
    """Find all loci where *rule* matches *seq*.

    For each position in the sequence, the algorithm:
      1. Match the left context so it lands exactly at pos (or check boundary).
      2. Match the target starting at pos, recording its span (start, end).
      3. Match the right context starting at end (or check boundary).
      4. Check that no exception context matches.

    All loci are collected before rewriting, ensuring simultaneous application.
    """
    loci: list[Locus] = []
    seen: set[tuple[int, int]] = set()

    # Pre-compute the minimum consuming length of the target to skip
    # positions where it could never fit.
    min_target_len = _min_consuming(rule.target)
    max_start = len(seq.data) - min_target_len + 1

    for pos in range(max(0, max_start) + 1):
        for locus in _try_locus_at(rule, seq, pos):
            key = (locus.start, locus.end)
            if key not in seen:
                seen.add(key)
                loci.append(locus)

    return loci


def _try_locus_at(rule: Rule, seq: Sequence, pos: int) -> list[Locus]:
    """Try to match the full rule with the target starting at *pos*.

    Steps:
      1. Match left context ending at pos (left context "lands" at pos).
      2. Match target starting at pos.
      3. Match right context starting after target.
      4. Check exception doesn't match.
    """
    results: list[Locus] = []
    left_ctx = rule.left_context
    right_ctx = rule.right_context

    # Step 1: Match left context
    if left_ctx is not None:
        left_matches = _match_left_context(left_ctx, seq, pos)
        if not left_matches:
            return results
    else:
        left_matches = [(pos, _EMPTY_ENV)]

    for target_start, env_after_left in left_matches:
        # Step 2: Match target starting at target_start
        for target_end, env_after_target in match(rule.target, seq, target_start, env_after_left):
            # Step 3: Match right context starting after target
            if right_ctx is not None:
                first_match = next(match(right_ctx, seq, target_end, env_after_target), None)
                if first_match is None:
                    continue
                _, env_after_all = first_match
            else:
                env_after_all = env_after_target

            locus = Locus(target_start, target_end, env_after_all)

            # Step 4: Check exception doesn't match
            if _exception_matches(rule, seq, target_start, target_end):
                continue

            results.append(locus)

    return results


def _match_left_context(left_ctx: list[Element], seq: Sequence, end_pos: int) -> list[tuple[int, Env]]:
    """Match left context so it lands exactly at *end_pos*.

    Tries matching left_ctx from every position that would make it end at
    end_pos.  Uses _min_consuming to narrow the search range for fixed-length
    contexts.
    """
    results: list[tuple[int, Env]] = []
    min_consume = _min_consuming(left_ctx)

    # Start positions range from (end_pos - min_consume) down to 0.
    # For contexts with only (1,1) quantifiers and boundaries, there is
    # exactly one valid start position.
    earliest = max(0, end_pos - min_consume)
    for start in range(earliest, end_pos + 1):
        for next_pos, env in match(left_ctx, seq, start, _EMPTY_ENV):
            if next_pos == end_pos:
                results.append((next_pos, env))

    return results


def _exception_matches(rule: Rule, seq: Sequence, target_start: int, target_end: int) -> bool:
    """Check whether any exception context matches.

    Returns True if the exception matches (meaning the rule should NOT apply).
    """
    exc_left = rule.exception_left
    exc_right = rule.exception_right

    if exc_left is None and exc_right is None:
        return False

    # Left exception: match ending at target_start
    if exc_left is not None:
        min_consume = _min_consuming(exc_left)
        earliest = max(0, target_start - min_consume)
        for start in range(earliest, target_start + 1):
            first_match = next(match(exc_left, seq, start, _EMPTY_ENV), None)
            if first_match is not None:
                end_pos, _ = first_match
                if end_pos == target_start:
                    # Left exception matches — check right if present
                    if exc_right is not None:
                        if next(match(exc_right, seq, target_end, _EMPTY_ENV), None) is not None:
                            return True
                    else:
                        return True

    # Right exception only: match starting at target_end
    if exc_left is None and exc_right is not None:
        if next(match(exc_right, seq, target_end, _EMPTY_ENV), None) is not None:
            return True

    return False


def _min_consuming(elements: list[Element]) -> int:
    """Count the minimum number of segments consumed by an element list.

    Boundaries consume zero; Null consumes zero; Bundles consume their
    quantifier.min; Groups consume their quantifier.min times inner min;
    Disjunction consumes the minimum across all branches.
    """
    count = 0
    for el in elements:
        if isinstance(el, Bundle):
            count += el.quantifier.min
        elif isinstance(el, Null):
            pass  # consumes zero
        elif isinstance(el, Group):
            inner_min = _min_consuming(el.elements)
            count += el.quantifier.min * inner_min
        elif isinstance(el, Disjunction):
            # Use the minimum across all branches
            branch_mins = [_min_consuming(branch) for branch in el.branches]
            count += min(branch_mins) if branch_mins else 0
        # Boundary, Ref, Binding consume zero (or variable)
    return count


# ---------------------------------------------------------------------------
# Stage 4 — Rewrite
# ---------------------------------------------------------------------------


def rewrite(seq: Sequence, loci: list[Locus], rule: Rule) -> Sequence:
    """Apply the result template to all matched loci simultaneously.

    Supports three result element types:
    - ``Bundle``: a feature delta combined with the corresponding target segment
      via ``combine_with``.  If there is no corresponding target segment
      (insertion), the bundle is inserted as-is.
    - ``Null``: delete the corresponding target segment.
    - ``Ref``: copy the referenced span's segments from the matched locus.

    All loci are applied to the original sequence state (simultaneous
    application), so later loci don't see each other's changes.  Loci are
    processed in reverse position order so that insertions/deletions don't
    shift earlier loci's indices.
    """
    if not loci:
        return seq

    # Sort loci in reverse order by start position so that
    # insertions/deletions don't shift earlier loci's indices.
    sorted_loci = sorted(loci, key=lambda l: l.start, reverse=True)

    new_data = list(seq.data)

    for locus in sorted_loci:
        replacement = _instantiate_result(
            rule.result, seq.data, locus.start, locus.end, locus.env
        )
        new_data[locus.start : locus.end] = replacement

    return Sequence(new_data)


def _instantiate_result(
    result_elements: list[Element],
    seq_data: list[FeatureBundle],
    target_start: int,
    target_end: int,
    env: Env,
) -> list[FeatureBundle]:
    """Build the replacement segments from a rule's result template.

    Iterates through result elements and produces a list of FeatureBundles:

    - ``Bundle``: if there is a corresponding target segment (i within the
      target span), combine the delta with it.  Otherwise, insert the bundle
      as-is (pure insertion).
    - ``Null``: skip the corresponding target segment (deletion).  If there
      is no corresponding target segment, Null is ignored.
    - ``Ref``: copy the referenced span's segments from the environment.

    Args:
        result_elements: The rule's result element list.
        seq_data: The sequence data (list of feature bundles).
        target_start: Start index of the matched target span.
        target_end: End index (exclusive) of the matched target span.
        env: The environment captured during matching (carries ref bindings).

    Returns:
        A list of FeatureBundles to splice in at the target span.
    """
    replacement: list[FeatureBundle] = []
    target_idx = 0  # index into the target span [target_start, target_end)

    for el in result_elements:
        if isinstance(el, Bundle):
            if target_start + target_idx < target_end:
                # Delta: combine with the corresponding target segment
                replacement.append(
                    seq_data[target_start + target_idx].combine_with(el.bundle)
                )
                target_idx += 1
            else:
                # Pure insertion: no target segment to combine with
                replacement.append(FeatureBundle(dict(el.bundle.data)))
            # Note: for quantified bundles in result position, we'd need
            # to loop, but result bundles currently use (1,1) quantifier.
        elif isinstance(el, Null):
            # Deletion: skip one target segment
            if target_start + target_idx < target_end:
                target_idx += 1
            # If no target segment left, Null is a no-op
        elif isinstance(el, Ref):
            # Copy referenced span's segments
            if el.name in env.refs:
                ref_start, ref_end = env.refs[el.name]
                replacement.extend(seq_data[ref_start:ref_end])
            # If ref not found in env, skip (shouldn't happen with valid rules)

    return replacement


# ---------------------------------------------------------------------------
# Top-level API
# ---------------------------------------------------------------------------


def apply_rules(seq: Sequence, rules: list[Rule]) -> Sequence:
    """Apply all rules in time order to the sequence.

    Rules are applied sequentially: each rule sees the result of all
    previous rules.  Within a single rule, the application mode controls
    how multiple matches interact:

    - **simultaneous**: find every locus against the original input, then
      rewrite all at once.  No application sees another's output.
    - **left_to_right**: scan from left to right, apply at the first locus,
      then resume scanning just past the rewritten span.  Changed segments
      are visible as context for later applications in the same pass.
    - **right_to_left**: mirror of left_to_right — scan from right to left.

    Args:
        seq: The input sequence of feature bundles.
        rules: Rules sorted by time (ascending — lower time number
            means applied earlier).

    Returns:
        A new Sequence with all rule applications applied.
    """
    current = seq
    for rule in rules:
        current = _apply_single_rule(current, rule)
    return current


def _apply_single_rule(seq: Sequence, rule: Rule) -> Sequence:
    """Apply a single rule to the sequence according to its application mode."""
    if rule.application == Application.simultaneous:
        loci = find_loci(rule, seq)
        if loci:
            return rewrite(seq, loci, rule)
        return seq

    if rule.application == Application.left_to_right:
        return _apply_sequential(seq, rule, reverse=False)

    if rule.application == Application.right_to_left:
        return _apply_sequential(seq, rule, reverse=True)

    # Fallback (shouldn't reach here if Application is exhaustive)
    return seq


def _apply_sequential(seq: Sequence, rule: Rule, reverse: bool = False) -> Sequence:
    """Apply a rule sequentially — find one locus, rewrite, resume scanning.

    For left-to-right (reverse=False), scan from position 0 forward.
    For right-to-left (reverse=True), scan from the end backward.

    After each successful rewrite, the scan restarts just past the rewritten
    span (left-to-right) or just before it (right-to-left).  Rewritten
    segments are visible as context for later matches in the same pass.

    A locus is rejected if its target span overlaps with any previously
    rewritten span — each position can only be part of one match per pass.
    """
    min_target_len = _min_consuming(rule.target)
    if min_target_len == 0:
        min_target_len = 1  # Guard against zero-length target scans

    current = seq
    consumed: list[tuple[int, int]] = []  # rewritten target spans
    pos = len(current.data) - min_target_len if reverse else 0
    end = len(current.data)

    while True:
        if reverse:
            if pos < 0:
                break
        else:
            if pos > end - min_target_len:
                break

        loci = _try_locus_at(rule, current, pos)

        if loci:
            # Find the first locus whose target span doesn't overlap
            # with any previously rewritten span.
            locus = None
            for candidate in loci:
                if not _spans_overlap(consumed, candidate.start, candidate.end):
                    locus = candidate
                    break

            if locus is not None:
                current = rewrite(current, [locus], rule)
                consumed.append((locus.start, locus.end))
                end = len(current.data)
                if reverse:
                    pos = locus.start - 1
                else:
                    pos = locus.end
                continue

        pos += -1 if reverse else 1

    return current


def _spans_overlap(consumed: list[tuple[int, int]], start: int, end: int) -> bool:
    """Check whether [start, end) overlaps with any span in consumed."""
    for cs, ce in consumed:
        if start < ce and end > cs:
            return True
    return False
