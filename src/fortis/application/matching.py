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

Contour matching honours the positional modifier (``@initial``/``@final``/
``@any``/``@all``/``@n``/``@n;m``): see ``_value_at_position``. The one refused
case is alpha inside a multi-limb ``@any`` (a sub-sequence search that would leak
a binding across failed window attempts).

Deferred for v1 (each is an explicit no-match or error, never a silent pass):
multi-segment reference bindings (only single-segment ``n=`` is captured), and
references *bound* in a context/exception and recalled in an earlier position —
only target bindings are order-independent; context bindings follow the
left → target → right order.

Negated alpha is fully supported at both layers, since pass 1 is alpha-blind and
defers either to pass 2: a negated *element* wrapping an alpha bundle (``![αF]``)
and a negated alpha *spec* (constructible as ``!-α``, i.e. "not opposite") both
resolve correctly. (``!α`` is the alpha-*other* value marker, not a negation.)
"""

from collections.abc import Callable, Iterator
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
from src.fortis.models.values import AlphaOp, AlphaRef, ContourEdge, ContourPosition, Limb, Value


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


def _limb_match_binding(p_limb: Limb, s_limb: Limb, bindings: Bindings | None) -> bool:
    """Compare one pattern limb to a segment limb, binding/recalling alpha."""
    if isinstance(p_limb, AlphaRef):
        return _alpha_matches(p_limb, s_limb, bindings)
    return p_limb == s_limb


def _limb_match_readonly(p_limb: Limb, s_limb: Limb, bindings: Bindings | None) -> bool:
    """Compare one limb with alpha **recall-only** — an unbound alpha never matches."""
    if isinstance(p_limb, AlphaRef):
        if bindings is None or p_limb.var not in bindings.alpha:
            return False
        bound = bindings.alpha[p_limb.var]
        bound_atom = bound[0] if isinstance(bound, tuple) and len(bound) == 1 else bound
        return s_limb == bound_atom if p_limb.op == AlphaOp.same else s_limb != bound_atom
    return p_limb == s_limb


def _window(
    p_limbs: tuple[Limb, ...],
    s_limbs: tuple[Limb, ...],
    start: int,
    cmp: Callable[[Limb, Limb], bool],
) -> bool:
    """Whether each pattern limb matches the segment limb at ``start + i``."""
    return all(cmp(p, s_limbs[start + i]) for i, p in enumerate(p_limbs))


def _value_at_position(
    p_limbs: tuple[Limb, ...],
    position: ContourPosition,
    s_limbs: tuple[Limb, ...],
    cmp: Callable[[Limb, Limb], bool],
    binds: bool,
) -> bool:
    """Whether *p_limbs* match *s_limbs* at *position*, comparing limbs with *cmp*.

    Mirrors what the parser emits (§5.9): a single pattern limb is tested at the
    named position(s) of the segment's contour; a multi-limb pattern is a window
    or a per-limb alignment. ``@all`` of a single value means it holds at *every*
    position; of a contour, same arity limb-for-limb. ``@any`` of a single value
    means *some* position; of a contour, a sub-sequence anywhere. ``@initial`` /
    ``@final`` align the pattern as a prefix / suffix; a tuple position pins each
    limb to its own segment index (1-based).

    *binds* says whether *cmp* mutates the alpha environment: a multi-limb ``@any``
    search would leak a binding from a failed window into the next, so an
    alpha-bearing one is refused (rather than risk a silent miscompare).
    """
    if isinstance(position, tuple):
        if len(p_limbs) == 1:  # one value at each listed position (e.g. 5@2;3)
            return all(1 <= n <= len(s_limbs) and cmp(p_limbs[0], s_limbs[n - 1]) for n in position)
        # a contour pinned limb-by-limb to positions (validator forces equal length)
        return len(position) == len(p_limbs) and all(
            1 <= n <= len(s_limbs) and cmp(p, s_limbs[n - 1])
            for p, n in zip(p_limbs, position, strict=True)
        )
    if isinstance(position, int):
        return (
            len(p_limbs) == 1
            and 1 <= position <= len(s_limbs)
            and cmp(p_limbs[0], s_limbs[position - 1])
        )
    if position == ContourEdge.all:
        if len(p_limbs) == 1:
            return bool(s_limbs) and all(cmp(p_limbs[0], s) for s in s_limbs)
        return len(p_limbs) == len(s_limbs) and _window(p_limbs, s_limbs, 0, cmp)
    if position == ContourEdge.any:
        if len(p_limbs) == 1:
            return any(cmp(p_limbs[0], s) for s in s_limbs)
        if binds and any(isinstance(limb, AlphaRef) for limb in p_limbs):
            raise NotImplementedError(
                "alpha in a multi-limb @any contour pattern is not supported"
            )
        return any(
            _window(p_limbs, s_limbs, i, cmp) for i in range(len(s_limbs) - len(p_limbs) + 1)
        )
    if position == ContourEdge.initial:
        return len(p_limbs) <= len(s_limbs) and _window(p_limbs, s_limbs, 0, cmp)
    if position == ContourEdge.final:
        return len(p_limbs) <= len(s_limbs) and _window(
            p_limbs, s_limbs, len(s_limbs) - len(p_limbs), cmp
        )
    return False


def _value_matches(
    value: Value, position: ContourPosition, segment_value: Value, bindings: Bindings | None
) -> bool:
    """Whether a pattern value matches a realized value at the given contour position.

    A single-value default (``@any``) holds if the value appears at any segment
    position — including against a contour segment. An unbound alpha at ``@any``
    binds to the first segment limb.
    """
    return _value_at_position(
        _limbs(value),
        position,
        _limbs(segment_value),
        lambda p, s: _limb_match_binding(p, s, bindings),
        binds=True,
    )


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
    matched = _value_matches(pattern.value, pattern.contour_position, segment.value, bindings)
    return (not matched) if pattern.negated else matched


def _value_holds(
    value: Value, position: ContourPosition, segment_value: Value, bindings: Bindings | None
) -> bool:
    """Like ``_value_matches`` but alpha is **recall-only** (for conditional features).

    Shares the positional structure; an alpha limb holds only if the variable is
    already bound and the segment atom agrees per the op — an unbound alpha never
    holds and is never bound, so a condition only reads the environment.
    """
    return _value_at_position(
        _limbs(value),
        position,
        _limbs(segment_value),
        lambda p, s: _limb_match_readonly(p, s, bindings),
        binds=False,
    )


def _condition_holds(spec: PatternSpec, segment: FeatureBundle, bindings: Bindings | None) -> bool:
    """Whether a conditional feature's condition holds against *segment* (read-only alpha).

    Mirrors the spec-matching truth but never binds and never filters: an absent
    feature satisfies only ``none``; negation flips the result, so ``<n: !+F>``
    holds exactly when F is not ``+``. Because alpha is recall-only here, an alpha
    condition (``<n: αF>``) requires α to be bound *earlier* in the
    left-context → target → right-context order; otherwise the condition is simply
    false (it never binds).
    """
    feature = spec.feature
    if feature not in segment:
        base = spec.value is None
    else:
        base = _value_holds(spec.value, spec.contour_position, segment[feature].value, bindings)
    return (not base) if spec.negated else base


def pattern_matches(
    pattern: PatternBundle,
    segment: FeatureBundle,
    bindings: Bindings | None = None,
    *,
    syllable: FeatureBundle | None = None,
    syllable_features: frozenset[str] = frozenset(),
) -> bool:
    """Whether *pattern* matches realized *segment*.

    Every (unconditional) feature the pattern mentions must be present in the
    segment with a compatible value; features the pattern does not mention are
    unconstrained.

    Against an *absent* feature: a ``none`` spec (``[F: none]``, value ``None``)
    matches — it asserts F is unspecified — as does a negated concrete spec
    (``[F: !val]``); a plain concrete spec fails, and ``[F: !none]`` (negated
    ``none``, i.e. "must be specified") fails.

    A **conditional** feature (``[<n: F>]``, ``condition_label`` set) never filters:
    it records into ``bindings.conditions[n]`` whether its condition holds
    (AND-accumulated across the positions the label appears in), which the applier
    later consults to gate the paired result feature.

    A **syllable-tier** feature (one named in *syllable_features*) is tested
    against *syllable* — the bundle of the segment's syllable nucleus — rather than
    the segment itself, so e.g. ``[+cons, tone: 3]`` checks the consonant's
    *syllable's* tone. With no *syllable* (unsyllabified, or no tier info) every
    feature falls back to the segment, preserving the prior behaviour.

    Args:
        pattern: The pattern bundle to test.
        segment: The realized segment to test against.
        bindings: Alpha-variable environment, threaded for binding/recall.
        syllable: The segment's syllable nucleus bundle (for syllable-tier specs).
        syllable_features: Names of the features that live on the syllable tier.
    """
    for feature, spec in pattern.data.items():
        target = segment
        if syllable is not None and feature in syllable_features:
            target = syllable
        if spec.condition_label is not None:
            if bindings is not None:
                label = spec.condition_label
                holds = _condition_holds(spec, target, bindings)
                bindings.conditions[label] = bindings.conditions.get(label, True) and holds
            continue
        if feature not in target:
            if spec.value is None:
                # "F: none" is satisfied by absence; "F: !none" requires presence.
                if spec.negated:
                    return False
                continue
            if spec.negated:
                continue  # "F: !val" is satisfied by absence
            return False
        if not _spec_matches(spec, target[feature], bindings):
            return False
    return True


# ---- Sequence matcher -----------------------------------------------------------------


@dataclass(frozen=True)
class SyllableView:
    """Syllable-tier context for tier-aware matching.

    ``nuclei[pos]`` is the nucleus bundle of the segment at ``pos``'s syllable (the
    ``Syllable.bundle`` view); ``features`` names the syllable-tier features. A
    syllable-tier spec is then matched against ``nuclei[pos]`` rather than the
    segment itself.
    """

    nuclei: list[FeatureBundle | None]
    features: frozenset[str]

    def at(self, pos: int) -> FeatureBundle | None:
        """The syllable (nucleus) bundle for position *pos*, if any."""
        return self.nuclei[pos] if 0 <= pos < len(self.nuclei) else None


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
        conditions=dict(bindings.conditions),
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
    syllables: SyllableView | None,
) -> Iterator[tuple[int, Bindings]]:
    """Yield every ``(end_pos, bindings)`` for matching one *element* at *pos*.

    Bindings are copied before any mutation, so each yielded branch is
    independent and the caller's environment is never disturbed. *boundaries* are
    the syllable-boundary positions (the ``$`` assertion); *syllables* supplies the
    per-position nucleus bundle for tier-aware matching of syllable-tier features.
    """
    match element:
        case BundleElem(bundle):
            if pos < len(segments):
                branch = _copy(bindings)
                syllable = syllables.at(pos) if syllables else None
                feats = syllables.features if syllables else frozenset()
                if pattern_matches(
                    bundle, segments[pos], branch, syllable=syllable, syllable_features=feats
                ):
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
            yield from _match_sequence(
                inner, segments, pos, bindings, letters, boundaries, syllables
            )

        case Disjunction(branches):
            for branch in branches:
                yield from _match_sequence(
                    branch, segments, pos, bindings, letters, boundaries, syllables
                )

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
                        inner, segments, pos, _copy(bindings), letters, boundaries, syllables
                    )
                )
                if not matched:
                    yield pos + 1, bindings

        case Quantified(inner, quant):
            yield from _match_repeat(
                inner, segments, pos, bindings, letters, boundaries, syllables, quant.min,
                quant.max, 0,
            )

        case Bound(ref, inner):
            for end, branch in _match_element(
                inner, segments, pos, bindings, letters, boundaries, syllables
            ):
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
    syllables: SyllableView | None,
    min_n: int,
    max_n: int | None,
    count: int,
) -> Iterator[tuple[int, Bindings]]:
    """Greedy quantifier match: try more repetitions before fewer."""
    if max_n is None or count < max_n:
        for end, branch in _match_element(
            inner, segments, pos, bindings, letters, boundaries, syllables
        ):
            if end == pos:  # zero-width progress would loop forever
                continue
            yield from _match_repeat(
                inner, segments, end, branch, letters, boundaries, syllables,
                min_n, max_n, count + 1,
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
    syllables: SyllableView | None,
) -> Iterator[tuple[int, Bindings]]:
    """Yield every ``(end_pos, bindings)`` for matching *elements* in order at *pos*."""
    if not elements:
        yield pos, bindings
        return
    first, rest = elements[0], elements[1:]
    for mid, branch in _match_element(
        first, segments, pos, bindings, letters, boundaries, syllables
    ):
        yield from _match_sequence(rest, segments, mid, branch, letters, boundaries, syllables)


def _match_ending_at(
    elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    end: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
    syllables: SyllableView | None,
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match a span ending exactly at *end*.

    Used for left context/exception, whose right edge is anchored to the target
    but whose left edge floats.
    """
    for start in range(end, -1, -1):
        for stop, branch in _match_sequence(
            elements, segments, start, bindings, letters, boundaries, syllables
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
    syllables: SyllableView | None,
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match a span starting at *start*.

    Used for right context/exception, whose left edge is anchored to the target
    but whose right edge floats.
    """
    for _stop, branch in _match_sequence(
        elements, segments, start, bindings, letters, boundaries, syllables
    ):
        yield branch


def _exception_blocks(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    start: int,
    end: int,
    bindings: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
    syllables: SyllableView | None,
) -> bool:
    """Whether the exception environment holds around the locus (blocking the rule)."""
    if not (sd.left_exception or sd.right_exception):
        return False
    for left in _match_ending_at(
        sd.left_exception, segments, start, bindings, letters, boundaries, syllables
    ):
        for _ in _match_starting_at(
            sd.right_exception, segments, end, left, letters, boundaries, syllables
        ):
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
    syllables: SyllableView | None,
) -> Iterator[Bindings]:
    """Yield bindings for which *elements* match *segments* consuming exactly ``[start, end)``."""
    for stop, branch in _match_sequence(
        elements, segments, start, bindings, letters, boundaries, syllables
    ):
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
    return any(
        _match_span(elements, segments, 0, len(segments), Bindings(), letters, frozenset(), None)
    )


def find_matches(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    letters: LetterInventory | None = None,
    boundaries: frozenset[int] = frozenset(),
    syllables: SyllableView | None = None,
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
        syllables: Per-position nucleus view for tier-aware syllable-tier matching
            (``None`` means every feature is matched against its own segment).
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
            sd.target, segments, start, seed_pass1, letters, boundaries, syllables
        ):
            located = _locate(
                sd, segments, start, end, _seed_references(pass1), letters, boundaries, syllables
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
    syllables: SyllableView | None,
) -> Match | None:
    """Pass 2: evaluate the environment in alpha order; return the Match or None.

    Left context binds alpha first, then the target is re-matched over its exact
    span (so its alpha resolves against the bound left context), then the right
    context, then the exception. *seed* carries the target's reference bindings
    from pass 1.
    """
    for after_left in _match_ending_at(
        sd.left_context, segments, start, seed, letters, boundaries, syllables
    ):
        for after_target in _match_span(
            sd.target, segments, start, end, after_left, letters, boundaries, syllables
        ):
            for after_right in _match_starting_at(
                sd.right_context, segments, end, after_target, letters, boundaries, syllables
            ):
                if not _exception_blocks(
                    sd, segments, start, end, after_right, letters, boundaries, syllables
                ):
                    return Match(start=start, end=end, bindings=after_right)
    return None
