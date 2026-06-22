"""Pattern matching against realized material.

Two layers:

* ``pattern_matches`` — the leaf: does one pattern bundle match one realized
  segment? Alpha variables resolve limb by limb against a threaded ``Bindings``
  environment (first occurrence binds, later ones compare per the alpha op).
* ``find_matches`` — the sequence matcher: a backtracking walk over the rule's
  Element AST that finds every locus where the target matches and the contexts
  hold (and the exception environment does not). It builds on ``pattern_matches``
  for each single segment.

The two binding namespaces have *different* ordering rules (per the notation
spec), so the matcher runs in two passes per candidate locus:

* **References** (``n=`` / ``@n``) are scope-based, not order-based: "the target
  is ref-bound first at match time" (§2.3.1). Pass 1 matches the target alone to
  discover its span and capture its reference bindings; these are then available
  everywhere in pass 2 regardless of position.
* **Alpha** variables are order-based — first occurrence binds, evaluated
  left context → target → right context (§5.6 / §2.4). Pass 2 re-evaluates the
  whole environment in that order (seeded with pass 1's references), so the
  target's alpha resolves against an already-bound left context.

The ``$`` syllable boundary is a zero-width assertion checked against a set of
boundary positions threaded in alongside ``letters`` (empty when the form is
unsyllabified, so ``$`` then simply never matches); the positions come from
``application.syllabifying``.

Deferred for v1 (each is an explicit no-match or error, never a silent pass):
multi-segment reference bindings (only single-segment ``n=`` is captured),
contour positional windowing (inherited from ``pattern_matches``), and references
*bound* in a context/exception and recalled in an earlier position — only target
bindings are order-independent; context bindings follow the left → target → right
order.

Negated alpha is fully supported at both layers, since pass 1 is alpha-blind and
defers either to pass 2: a negated *element* wrapping an alpha bundle (``![αF]``)
and a negated alpha *spec* (constructible as ``!-α``, i.e. "not opposite") both
resolve correctly. (``!α`` is the alpha-*other* value marker, not a negation.)
"""

from collections.abc import Iterator
from dataclasses import dataclass, field

from src.fortis.application.combining import matches_exactly
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    Group,
    LetterRef,
    Negated,
    Null,
    Quantified,
    RecallRef,
    SyllableBoundary,
    Wildcard,
    WordBoundary,
)
from src.fortis.models.inventories import LetterInventory
from src.fortis.models.rules import StructuralDescription
from src.fortis.models.specs import FeatureSpec, PatternSpec
from src.fortis.models.values import AlphaOp, AlphaRef, Limb, Value


def _limbs(value: Value) -> tuple[Limb, ...]:
    """Decompose a value into its contour limbs (a scalar becomes one limb)."""
    return value if isinstance(value, tuple) else (value,)


def _alpha_matches(ref: AlphaRef, atom: Limb, bindings: Bindings | None) -> bool:
    """Resolve one alpha limb against a realized atom.

    First occurrence binds the variable to the atom and succeeds. A later
    occurrence compares per the alpha op: ``same`` requires equality;
    ``opposite``/``other`` require inequality. With no bindings context, or in a
    permissive-alpha environment, alpha always matches and binds nothing.
    """
    if bindings is None or bindings.permissive_alpha:
        return True
    if ref.var not in bindings.alpha:
        bindings.alpha[ref.var] = atom
        return True
    bound = bindings.alpha[ref.var]
    bound_atom = bound[0] if isinstance(bound, tuple) and len(bound) == 1 else bound
    match ref.op:
        case AlphaOp.same:
            return atom == bound_atom
        case AlphaOp.opposite | AlphaOp.other:
            return atom != bound_atom
    return atom == bound_atom


def _value_matches(pattern: Value, segment: Value, bindings: Bindings | None) -> bool:
    """Whether a pattern value matches a realized segment value, limb by limb.

    A contour matches only a contour of the same length (no positional
    windowing yet — deferred). Each pattern limb is either an alpha reference
    (resolved against the segment atom) or a concrete value (compared equal).
    """
    pattern_limbs = _limbs(pattern)
    segment_limbs = _limbs(segment)
    if len(pattern_limbs) != len(segment_limbs):
        return False
    for p_limb, s_limb in zip(pattern_limbs, segment_limbs, strict=True):
        if isinstance(p_limb, AlphaRef):
            if not _alpha_matches(p_limb, s_limb, bindings):
                return False
        elif p_limb != s_limb:
            return False
    return True


def _has_alpha(value: Value) -> bool:
    """Whether *value* references an alpha variable in any of its limbs."""
    return any(isinstance(limb, AlphaRef) for limb in _limbs(value))


def _spec_matches(pattern: PatternSpec, segment: FeatureSpec, bindings: Bindings | None) -> bool:
    """Whether one pattern spec matches a realized feature spec (negation-aware)."""
    if bindings is not None and bindings.permissive_alpha and _has_alpha(pattern.value):
        # Alpha-blind pass 1: an alpha-bearing spec is satisfiable either way (the
        # more so when negated, e.g. ``!-α``), so defer the whole spec to pass 2
        # rather than letting permissive alpha decide — and, under negation, flip.
        return True
    matched = _value_matches(pattern.value, segment.value, bindings)
    return (not matched) if pattern.negated else matched


def pattern_matches(
    pattern: PatternBundle, segment: FeatureBundle, bindings: Bindings | None = None
) -> bool:
    """Whether *pattern* matches realized *segment*.

    Every feature the pattern mentions must be present in the segment with a
    compatible value; features the pattern does not mention are unconstrained.

    Against an *absent* feature: a ``none`` spec (``[F: none]``, value ``None``)
    matches — it asserts F is unspecified — as does a negated concrete spec
    (``[F: !val]``); a plain concrete spec fails, and ``[F: !none]`` (negated
    ``none``, i.e. "must be specified") fails.

    Args:
        pattern: The pattern bundle to test.
        segment: The realized segment to test against.
        bindings: Alpha-variable environment, threaded for binding/recall.
    """
    for feature, pattern_spec in pattern.data.items():
        if feature not in segment:
            if pattern_spec.value is None:
                # "F: none" is satisfied by absence; "F: !none" requires presence.
                if pattern_spec.negated:
                    return False
                continue
            if pattern_spec.negated:
                continue  # "F: !val" is satisfied by absence
            return False
        if not _spec_matches(pattern_spec, segment[feature], bindings):
            return False
    return True


# ---- Sequence matcher -----------------------------------------------------------------


@dataclass(frozen=True)
class Match:
    """One locus: the target spans ``segments[start:end]``, with its bindings."""

    start: int
    end: int
    bindings: Bindings = field(default_factory=Bindings)


def _copy(bindings: Bindings) -> Bindings:
    """A shallow copy of a bindings env, safe to mutate down one backtrack branch."""
    return Bindings(
        alpha=dict(bindings.alpha),
        reference=dict(bindings.reference),
        permissive_alpha=bindings.permissive_alpha,
    )


def _letter_matches(letter: FeatureBundle, segment: FeatureBundle) -> bool:
    """Whether a letter's features are all present in *segment* with equal values."""
    return all(f in segment and segment[f].value == spec.value for f, spec in letter.items())


def _match_element(
    element: Element,
    segments: list[FeatureBundle],
    pos: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Iterator[tuple[int, Bindings]]:
    """Yield every ``(end_pos, bindings)`` for matching one *element* at *pos*.

    Bindings are copied before any mutation, so each yielded branch is
    independent and the caller's environment is never disturbed. *boundaries* are
    the syllable-boundary positions, consulted only by the ``$`` assertion.
    """
    match element:
        case BundleElem(bundle):
            if pos < len(segments):
                branch = _copy(bindings)
                if pattern_matches(bundle, segments[pos], branch):
                    yield pos + 1, branch

        case LetterRef(symbol):
            if pos < len(segments) and symbol in letters:
                if _letter_matches(letters[symbol].bundle, segments[pos]):
                    yield pos + 1, bindings

        case Wildcard():
            if pos < len(segments):
                yield pos + 1, bindings

        case WordBoundary():
            if pos == 0 or pos == len(segments):
                yield pos, bindings

        case SyllableBoundary():
            # Zero-width assertion at a syllable edge; boundaries come from
            # syllabification (empty when the form is unsyllabified).
            if pos in boundaries:
                yield pos, bindings

        case Null():
            # ∅ in target is a zero-width insertion point.
            yield pos, bindings

        case Group(inner):
            yield from _match_sequence(inner, segments, pos, bindings, letters, boundaries)

        case Disjunction(branches):
            for branch in branches:
                yield from _match_sequence(branch, segments, pos, bindings, letters, boundaries)

        case Negated(inner):
            # One segment that the inner element does NOT match. Bindings from the
            # failed inner attempt are discarded (a negative match binds nothing).
            if pos < len(segments):
                if bindings.permissive_alpha:
                    # Pass 1 is alpha-blind, but "always matches" would wrongly force
                    # an alpha-bearing negation to *never* hold. The negation is
                    # satisfiable under some alpha assignment, so consume one segment
                    # and defer the real (alpha-aware) check to pass 2.
                    yield pos + 1, bindings
                    return
                matched = any(
                    end == pos + 1
                    for end, _ in _match_element(
                        inner, segments, pos, _copy(bindings), letters, boundaries
                    )
                )
                if not matched:
                    yield pos + 1, bindings

        case Quantified(inner, quant):
            yield from _match_repeat(
                inner, segments, pos, bindings, letters, boundaries, quant.min, quant.max, 0
            )

        case Bound(ref, inner):
            for end, branch in _match_element(inner, segments, pos, bindings, letters, boundaries):
                captured = _copy(branch)
                if end == pos + 1:  # single-segment binding (multi-segment deferred)
                    captured.reference[ref] = segments[pos]
                yield end, captured

        case RecallRef(ref):
            bound = bindings.reference.get(ref)
            if bound is not None and pos < len(segments) and matches_exactly(segments[pos], bound):
                yield pos + 1, bindings

        case _:
            raise NotImplementedError(f"cannot match element {element!r} in this position")


def _match_repeat(
    inner: Element,
    segments: list[FeatureBundle],
    pos: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
    min_n: int,
    max_n: int | None,
    count: int,
) -> Iterator[tuple[int, Bindings]]:
    """Greedy quantifier match: try more repetitions before fewer."""
    if max_n is None or count < max_n:
        for end, branch in _match_element(inner, segments, pos, bindings, letters, boundaries):
            if end == pos:  # zero-width progress would loop forever
                continue
            yield from _match_repeat(
                inner, segments, end, branch, letters, boundaries, min_n, max_n, count + 1
            )
    if count >= min_n:
        yield pos, bindings


def _match_sequence(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    pos: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Iterator[tuple[int, Bindings]]:
    """Yield every ``(end_pos, bindings)`` for matching *elements* in order at *pos*."""
    if not elements:
        yield pos, bindings
        return
    first, rest = elements[0], elements[1:]
    for mid, branch in _match_element(first, segments, pos, bindings, letters, boundaries):
        yield from _match_sequence(rest, segments, mid, branch, letters, boundaries)


def _match_ending_at(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    end: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match a span ending exactly at *end*.

    Used for left context/exception, whose right edge is anchored to the target
    but whose left edge floats.
    """
    for start in range(end, -1, -1):
        for stop, branch in _match_sequence(
            elements, segments, start, bindings, letters, boundaries
        ):
            if stop == end:
                yield branch


def _match_starting_at(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    start: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match a span starting at *start*.

    Used for right context/exception, whose left edge is anchored to the target
    but whose right edge floats.
    """
    for _stop, branch in _match_sequence(elements, segments, start, bindings, letters, boundaries):
        yield branch


def _exception_blocks(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    start: int,
    end: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> bool:
    """Whether the exception environment holds around the locus (blocking the rule)."""
    if not (sd.left_exception or sd.right_exception):
        return False
    for left in _match_ending_at(sd.left_exception, segments, start, bindings, letters, boundaries):
        for _ in _match_starting_at(sd.right_exception, segments, end, left, letters, boundaries):
            return True
    return False


def _seed_references(bindings: Bindings) -> Bindings:
    """A fresh env carrying only *bindings*' references; alpha is re-bound in pass 2."""
    return Bindings(reference=dict(bindings.reference))


def _match_span(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    start: int,
    end: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match *segments* consuming exactly ``[start, end)``."""
    for stop, branch in _match_sequence(elements, segments, start, bindings, letters, boundaries):
        if stop == end:
            yield branch


def full_match(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    letters: LetterInventory | None = None,
) -> bool:
    """Whether *elements* match *segments* exactly — the whole list, start to end.

    Used to test a candidate onset/coda against a syllable-part pattern. An empty
    *elements* matches only an empty *segments*; quantifiers express optionality.
    """
    letters = letters if letters is not None else LetterInventory()
    return any(_match_span(elements, segments, 0, len(segments), Bindings(), letters, frozenset()))


def find_matches(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    letters: LetterInventory | None = None,
    boundaries: frozenset[int] = frozenset(),
) -> list[Match]:
    """Find every locus in *segments* where rule *sd* applies.

    A locus is a target span whose left context matches immediately to its left,
    whose right context matches immediately to its right, and around which the
    exception environment does not hold. The greediest fully-valid target parse
    at each start position is taken.

    Two passes per candidate span (see module docstring): pass 1 matches the
    target alone to fix its span and capture its reference bindings; pass 2
    re-evaluates left context → target → right context → exception, binding alpha
    in that order with the target references pre-seeded.

    Args:
        sd: The parsed rule to apply.
        segments: The realized word, as a list of feature bundles.
        letters: Letter inventory for resolving letter shorthands in the rule.
        boundaries: Syllable-boundary positions for the ``$`` assertion; empty
            (the default) means the form is unsyllabified, so ``$`` never matches.
    """
    letters = letters if letters is not None else LetterInventory()
    matches: list[Match] = []

    for start in range(len(segments) + 1):
        # Pass 1: target alone, alpha-permissive — captures the structural span and
        # its reference bindings while committing no alpha (that is pass 2's job,
        # and must bind left-context first). Being fully alpha-blind, pass 1 yields
        # a true superset of valid spans in greedy order, so the greediest fully
        # valid span is still reached and none is missed.
        seed_pass1 = Bindings(permissive_alpha=True)
        for end, pass1 in _match_sequence(
            sd.target, segments, start, seed_pass1, letters, boundaries
        ):
            located = _locate(
                sd, segments, start, end, _seed_references(pass1), letters, boundaries
            )
            if located is not None:
                matches.append(located)
                break  # greediest fully-valid target parse at this start wins
    return matches


def _locate(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    start: int,
    end: int,
    seed: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
) -> Match | None:
    """Pass 2: evaluate the environment in alpha order; return the Match or None.

    Left context binds alpha first, then the target is re-matched over its exact
    span (so its alpha resolves against the bound left context), then the right
    context, then the exception. *seed* carries the target's reference bindings
    from pass 1.
    """
    for after_left in _match_ending_at(sd.left_context, segments, start, seed, letters, boundaries):
        for after_target in _match_span(
            sd.target, segments, start, end, after_left, letters, boundaries
        ):
            for after_right in _match_starting_at(
                sd.right_context, segments, end, after_target, letters, boundaries
            ):
                if not _exception_blocks(
                    sd, segments, start, end, after_right, letters, boundaries
                ):
                    return Match(start=start, end=end, bindings=after_right)
    return None
