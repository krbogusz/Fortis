"""Pattern matching against realized material.

Two layers:

* ``pattern_matches`` — the leaf: does one pattern bundle match one realized
  segment? Alpha variables resolve limb by limb against a threaded ``Bindings``
  environment — a value-agreement variable: each occurrence's op (same / opposite
  / other) states how its position relates to α, and any consistent assignment
  satisfies it (binding honours the op, so it is order-independent).
* ``find_matches`` — the sequence matcher: a backtracking walk over the rule's
  Element AST that finds every locus where the target matches and the contexts
  hold (and the exception environment does not). It builds on ``pattern_matches``
  for each single segment.

The matcher runs in two passes per candidate locus:

* **References** (``n=`` / ``@n``) are scope-based, not order-based: "the target
  is ref-bound first at match time" (§2.3.1). Pass 1 matches the target alone to
  discover its span and capture its reference bindings; these are then available
  everywhere in pass 2 regardless of position.
* **Alpha** variables are order-*independent* value-agreement variables (SPE):
  binding honours the op (``same`` binds α to the atom, ``opposite`` to its
  opposite), so a ``-α`` position imposes disagreement whether it is reached
  before or after its partner. Pass 1 is alpha-blind (it only fixes the span);
  pass 2 walks left context → target → right context binding/checking alpha, but
  the *result* no longer depends on that walk order. ``!α`` (other) is a ≠
  relation that cannot bind, so it is deferred and verified once α is bound.

The ``$`` syllable boundary is a zero-width assertion checked against a set of
boundary positions threaded in alongside ``letters`` (empty when the form is
unsyllabified, so ``$`` then simply never matches); the positions come from
``application.syllabifying``.

Contour matching honours the positional modifier (``@initial``/``@final``/
``@any``/``@all``/``@n``/``@n;m``): see ``_value_at_position``. The one refused
case is alpha inside a multi-limb ``@any`` (a sub-sequence search that would leak
a binding across failed window attempts).

A reference binding captures its whole matched span — one segment for ``1=[X]``,
several for a group ``1=([X][Y])`` — and a recall ``@n`` replays that span.

A reference may be recalled earlier than it is bound: the target's own bindings are
captured in pass 1; the right context's (and the right exception's) are pre-captured
before they are matched; and a target that recalls a *context* binding — which pass
1 cannot span on its own — has its span found by enumerating the end, letting the
right-context pre-seed resolve the recall (its length then fixes the span). The
remaining deferral (an explicit no-match, never a silent pass) is a target that
recalls a binding bound *later within the target itself*; write the binding before
the recall to avoid it.

Negated alpha is fully supported at both layers, since pass 1 is alpha-blind and
defers either to pass 2: a negated *element* wrapping an alpha bundle (``![αF]``)
and a negated alpha *spec* (constructible as ``!-α``, i.e. "not opposite") both
resolve correctly. (``!α`` is the alpha-*other* value marker, not a negation.)
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass, field, replace

from src.fortis.application.combining import matches_exactly
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    FloatingAutoseg,
    Group,
    LetterBundle,
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
from src.fortis.models.values import (
    AlphaOp,
    AlphaRef,
    AutosegBind,
    AutosegRecall,
    ContourEdge,
    ContourPosition,
    Limb,
    Value,
    opposite_pole,
)


def _limbs(value: Value) -> tuple[Limb, ...]:
    """Decompose a value into its contour limbs (a scalar becomes one limb)."""
    return value if isinstance(value, tuple) else (value,)


def _alpha_matches(ref: AlphaRef, atom: Limb, bindings: Bindings | None) -> bool:
    """Resolve one alpha limb against a realized atom — order-independently.

    Alpha is a value-agreement variable (SPE): each occurrence's op states how its
    position relates to α, and *any* consistent assignment satisfies the rule —
    there is no privileged "first binder". So binding **honours the op**: a ``same``
    occurrence binds α to the atom, an ``opposite`` (``-α``) occurrence binds α to
    the atom's opposite. Either way a ``-α`` position then imposes disagreement
    whether it is reached before or after its partner, so matching order does not
    change the result. A subsequent occurrence checks: ``same`` → equal,
    ``opposite``/``other`` → unequal.

    ``other`` (``!α``) is a ≠ relation that cannot determine α, so it never binds;
    it is deferred (``pending_other``) and verified once α is bound. In a
    permissive-alpha environment (pass 1) or with no bindings, alpha always matches
    and binds nothing.
    """
    if bindings is None or bindings.permissive_alpha:
        return True
    if ref.var not in bindings.alpha:
        match ref.op:
            case AlphaOp.same:
                bindings.alpha[ref.var] = atom
            case AlphaOp.opposite:
                bindings.alpha[ref.var] = opposite_pole(atom, ref.unary)
            case AlphaOp.other:
                bindings.pending_other.append((ref.var, atom))  # ≠ α, checked later
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
    if p_limb == "any":
        return s_limb is not None  # bare feature `[F]`: present with any value
    return p_limb == s_limb


def _limb_match_readonly(p_limb: Limb, s_limb: Limb, bindings: Bindings | None) -> bool:
    """Compare one limb with alpha **recall-only** — an unbound alpha never matches."""
    if isinstance(p_limb, AlphaRef):
        if bindings is None or p_limb.var not in bindings.alpha:
            return False
        bound = bindings.alpha[p_limb.var]
        bound_atom = bound[0] if isinstance(bound, tuple) and len(bound) == 1 else bound
        return s_limb == bound_atom if p_limb.op == AlphaOp.same else s_limb != bound_atom
    if p_limb == "any":
        return s_limb is not None  # bare feature `[F]`: present with any value
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


def _has_unary_alpha(value: Value) -> bool:
    """Whether *value* carries a unary alpha limb (whose absent pole is ``none``)."""
    return any(isinstance(limb, AlphaRef) and limb.unary for limb in _limbs(value))


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


_NO_NODES: Mapping[str, frozenset[str]] = {}  # pattern_matches default when no geometry is supplied


def pattern_matches(
    pattern: PatternBundle,
    segment: FeatureBundle,
    bindings: Bindings | None = None,
    *,
    syllable: FeatureBundle | None = None,
    syllable_features: frozenset[str] = frozenset(),
    node_descendants: Mapping[str, frozenset[str]] = _NO_NODES,
    position: int | None = None,
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
        node_descendants: Each segmental node → its descendant feature names; a ``node: ~n`` spec
            then captures that node's subtree onto ``bindings.node_reference`` for the applier.
        position: The segment's index, recorded under a tier-autosegment bind (``~ref``)
            so the applier can recall the same autosegment.
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
            if _has_unary_alpha(spec.value):
                # A unary alpha's absent pole is "none": resolve α against None, so
                # `αF`/`-αF` can bind or check the present↔absent opposition.
                if not _spec_matches(spec, FeatureSpec(feature=feature, value=None), bindings):
                    return False
                continue
            if spec.value is None:
                # "F: none" is satisfied by absence; "F: !none" requires presence.
                if spec.negated:
                    return False
                continue
            if spec.negated:
                continue  # "F: !val" is satisfied by absence
            return False
        if feature in node_descendants and isinstance(spec.value, AutosegBind | AutosegRecall):
            # Node-spread reference (`oral: ~n`): the node is present (checked above), so capture
            # this segment's subtree — the node plus its descendants here — for the applier to
            # copy onto the target. A *segmental* node spreads by copying its subtree (unlike a
            # tier autosegment, which shares a link); the capture matches unconditionally.
            if bindings is not None:
                names = set(node_descendants[feature]) | {feature}
                bindings.node_reference[spec.value.ref] = FeatureBundle(
                    {f: target[f] for f in names if f in target}
                )
            continue
        if isinstance(spec.value, AutosegBind):
            # Match the bound autosegment's value, then record the position it sits on, so
            # the applier can recall the *same* autosegment (spread it) via `~ref`.
            if not _spec_matches(replace(spec, value=spec.value.value), target[feature], bindings):
                return False
            if bindings is not None and position is not None:
                bindings.autoseg_reference[spec.value.ref] = position
            continue
        if not _spec_matches(spec, target[feature], bindings):
            return False
    return True


def _floating_matches(pattern: PatternBundle, bundle: FeatureBundle) -> bool:
    """Whether a floating autosegment *bundle* satisfies *pattern* (inner value equality)."""
    for feature, spec in pattern.items():
        wanted = spec.value.value if isinstance(spec.value, AutosegBind) else spec.value
        if feature not in bundle or bundle[feature].value != wanted:
            return False
    return True


def _bind_floating(
    pattern: PatternBundle, syllables: SyllableView | None, bindings: Bindings, position: int
) -> bool:
    """Match a floating autosegment against *pattern* at *position*; bind its id under ``~ref``.

    A *positioned* float (one with a sequence gap) binds only where it sits; a host-less float
    (gap ``None``) binds at any position.
    """
    if syllables is None:
        return False
    for autoseg_id, bundle, gap in syllables.floating:
        if gap is not None and gap != position:
            continue
        if _floating_matches(pattern, bundle):
            for spec in pattern.values():
                if isinstance(spec.value, AutosegBind):
                    bindings.floating_reference[spec.value.ref] = autoseg_id
            return True
    return False


# ---- Sequence matcher -----------------------------------------------------------------


@dataclass(frozen=True)
class SyllableView:
    """Syllable-tier context for tier-aware matching.

    ``nuclei[pos]`` is the nucleus bundle of the segment at ``pos``'s syllable (the
    ``Syllable.bundle`` view); ``features`` names the syllable-tier features. A
    syllable-tier spec is then matched against ``nuclei[pos]`` rather than the
    segment itself. ``floating`` lists the unanchored autosegments as ``(id, bundle, gap)``
    — ``gap`` being the segment position it floats beside, or ``None`` — which a
    ``⟨...⟩`` element matches and binds for docking.
    """

    nuclei: list[FeatureBundle | None]
    features: frozenset[str]
    floating: tuple[tuple[int, FeatureBundle, int | None], ...] = ()
    # node → its descendant feature names, for node-spread capture (``oral: ~n``): a
    # segmental node spreads by *copying its subtree*, so the matcher records which
    # features sit under it. Empty unless a feature inventory with geometry is supplied.
    node_descendants: Mapping[str, frozenset[str]] = field(default_factory=dict)

    def at(self, pos: int) -> FeatureBundle | None:
        """The syllable (nucleus) bundle for position *pos*, if any."""
        return self.nuclei[pos] if 0 <= pos < len(self.nuclei) else None


@dataclass(frozen=True)
class Match:
    """One locus: the target spans ``segments[start:end]``, with its bindings.

    ``target_choices`` is the branch index taken at each disjunction *in the target*
    (in encounter order); the applier uses it to select the paired result branch.
    """

    start: int
    end: int
    bindings: Bindings = field(default_factory=Bindings)
    target_choices: tuple[int, ...] = ()


def _copy(bindings: Bindings) -> Bindings:
    """A shallow copy of a bindings env, safe to mutate down one backtrack branch."""
    return Bindings(
        alpha=dict(bindings.alpha),
        reference=dict(bindings.reference),
        autoseg_reference=dict(bindings.autoseg_reference),
        floating_reference=dict(bindings.floating_reference),
        permissive_alpha=bindings.permissive_alpha,
        conditions=dict(bindings.conditions),
        disjunction_choices=bindings.disjunction_choices,
        pending_other=list(bindings.pending_other),
        node_reference=dict(bindings.node_reference),
    )


def _letter_matches(
    letter: FeatureBundle, segment: FeatureBundle, syllable_features: frozenset[str] = frozenset()
) -> bool:
    """Whether *segment* IS this letter — its segmental features are exactly the letter's.

    Identity, not subset: the letter must account for every segmental feature the segment
    carries, so the dental-fricative letter ``ð̠`` no longer also matches the strident ``z``
    (whose bundle merely adds ``strident``). Syllable-tier features (tone, stress) a lowered
    vowel may carry are excluded — they live on the nucleus, not in a letter's identity.
    """
    seg = {f for f in segment.data if f not in syllable_features}
    return seg == set(letter.data) and all(
        segment[f].value == spec.value for f, spec in letter.items()
    )


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
                nodes = syllables.node_descendants if syllables else _NO_NODES
                if pattern_matches(
                    bundle, segments[pos], branch, syllable=syllable, syllable_features=feats,
                    node_descendants=nodes, position=pos,
                ):
                    yield pos + 1, branch

        case FloatingAutoseg(pattern):
            # Zero-width: a floating autosegment must exist (and is bound for docking),
            # but no segment is consumed.
            branch = _copy(bindings)
            if _bind_floating(pattern, syllables, branch, pos):
                yield pos, branch

        case LetterRef(symbol):
            if pos < len(segments) and symbol in letters:
                feats = syllables.features if syllables else frozenset()
                if _letter_matches(letters[symbol].bundle, segments[pos], feats):
                    yield pos + 1, bindings

        case LetterBundle(bundle):
            if pos < len(segments):
                feats = syllables.features if syllables else frozenset()
                if _letter_matches(bundle, segments[pos], feats):
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
            # Record which branch matched so the applier can select the paired
            # result branch; only a branch that yields carries its index forward.
            for index, branch in enumerate(branches):
                chosen = _copy(bindings)
                chosen.disjunction_choices = bindings.disjunction_choices + (index,)
                yield from _match_sequence(
                    branch, segments, pos, chosen, letters, boundaries, syllables
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
                # Capture the whole matched span — one segment for `1=[X]`, several
                # for a group `1=([X][Y])` (a multi-segment binding).
                captured.reference[ref] = tuple(segments[pos:end])
                yield end, captured

        case RecallRef(ref):
            # Recall replays the bound span: each captured segment must match the
            # corresponding segment here (single- or multi-segment), consuming them.
            bound = bindings.reference.get(ref)
            if bound is None:
                return
            end = pos + len(bound)
            if end <= len(segments) and all(
                matches_exactly(segments[pos + offset], seg) for offset, seg in enumerate(bound)
            ):
                yield end, bindings

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
    # Scope-based references within the exception too: pre-bind the right exception's
    # references so a recall in the left exception (matched first) can resolve them.
    bindings = _seed_right_references(
        sd.right_exception, segments, end, bindings, letters, boundaries, syllables
    )
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


# --- Necessary-condition pruning ----------------------------------------------------------------
# A cheap pre-check that skips a rule when the word provably cannot satisfy it. Pure optimisation:
# the requirement is a conservative *lower bound* — only unconditionally-required, value-forcing
# specs contribute — so a word failing it has no locus, and pruning never drops a real match.


def _spec_demands(bundle: PatternBundle | FeatureBundle) -> Iterator[tuple[str, object]]:
    """The (feature, value) pairs a bundle forces a segment to carry.

    Skips everything that does not pin a present value: conditional and negated
    specs, alpha (variable), ``none`` (absence), and contours.
    """
    for feature, spec in bundle.items():
        if getattr(spec, "condition_label", None) is not None or getattr(spec, "negated", False):
            continue
        value = spec.value
        if value is None or value == "any" or isinstance(value, (AlphaRef, tuple)):
            continue  # `any` is a wildcard — it pins no concrete value, so demands nothing
        if isinstance(value, (AutosegBind, AutosegRecall)):
            continue  # a tier reference matches an autosegment, not a segment-bundle value
        yield (feature, value)


def _element_demands(element: Element, letters: LetterInventory) -> list[tuple[str, object]]:
    """The demands of a single bundle/letter element (empty for anything else)."""
    match element:
        case BundleElem(bundle) | LetterBundle(bundle):
            return list(_spec_demands(bundle))
        case LetterRef(symbol) if symbol in letters:
            return list(_spec_demands(letters[symbol].bundle))
        case _:
            return []


def _binding_demands(
    sd: StructuralDescription, letters: LetterInventory
) -> dict[int, list[tuple[str, object]]]:
    """Each *unconditionally-bound* single-element reference's demands, by ref number.

    Used to charge a recall ``@n`` with its binding's demands (the recall must match
    an identical copy). Only required bindings are recorded, so a recall of an
    optional/disjoined binding contributes nothing (staying a true lower bound).
    """
    out: dict[int, list[tuple[str, object]]] = {}

    def walk(elements: tuple[Element, ...], required: bool) -> None:
        for element in elements:
            match element:
                case Bound(ref, inner) if required:
                    demands = _element_demands(inner, letters)
                    if demands:
                        out[ref] = demands
                    walk((inner,), required)
                case Group(inner):
                    walk(inner, required)
                case Quantified(inner, quant):
                    walk((inner,), required and quant.min >= 1)
                case _:
                    pass  # disjunction / negated / leaf — no required binding here

    for elements in (sd.target, sd.left_context, sd.right_context):
        walk(elements, required=True)
    return out


def _required_counts(sd: StructuralDescription, letters: LetterInventory) -> Counter:
    """A conservative lower bound on (feature, value) occurrences any locus needs.

    Walks the target and contexts (not exceptions — they are negative). Only
    unconditionally-required positions contribute: a disjunction branch, an optional
    quantifier (``min`` 0), a negation, and exceptions add nothing. A reference's
    binding demands are charged once per recall too, so ``1=[+nasal] @1`` needs two
    ``[+nasal]`` segments.
    """
    bindings = _binding_demands(sd, letters)
    counts: Counter = Counter()

    def accumulate(elements: tuple[Element, ...], required: bool) -> None:
        for element in elements:
            match element:
                case (BundleElem(bundle) | LetterBundle(bundle)) if required:
                    counts.update(_spec_demands(bundle))
                case LetterRef(symbol) if required and symbol in letters:
                    counts.update(_spec_demands(letters[symbol].bundle))
                case RecallRef(ref) if required and ref in bindings:
                    counts.update(bindings[ref])
                case Bound(_, inner):
                    accumulate((inner,), required)
                case Group(inner):
                    accumulate(inner, required)
                case Quantified(inner, quant):
                    accumulate((inner,), required and quant.min >= 1)
                case _:
                    pass  # disjunction / negated / wildcard / boundary / null — no demand

    for elements in (sd.target, sd.left_context, sd.right_context):
        accumulate(elements, required=True)
    return counts


def _word_supply(segments: list[FeatureBundle]) -> Counter:
    """How many segments carry each (feature, value)."""
    supply: Counter = Counter()
    for segment in segments:
        for feature, spec in segment.items():
            supply[(feature, spec.value)] += 1
    return supply


def _cannot_match(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    letters: LetterInventory,
    syllable_features: frozenset[str] = frozenset(),
) -> bool:
    """Whether *segments* provably lack the material *sd* needs (so it cannot fire).

    Syllable-tier demands are skipped: those features are checked against the syllable
    nucleus (the syllable view), not the segment bundle, so the per-segment supply can't
    account for them.
    """
    supply = _word_supply(segments)
    return any(
        supply[demand] < count
        for demand, count in _required_counts(sd, letters).items()
        if demand[0] not in syllable_features
    )


def _bound_refs(elements: tuple[Element, ...]) -> set[int]:
    """Reference numbers bound (``n=``) anywhere in *elements*, descending into nesting."""
    refs: set[int] = set()
    for element in elements:
        match element:
            case Bound(ref, inner):
                refs.add(ref)
                refs |= _bound_refs((inner,))
            case Group(inner):
                refs |= _bound_refs(inner)
            case Disjunction(branches):
                for branch in branches:
                    refs |= _bound_refs(branch)
            case Quantified(inner, _) | Negated(inner):
                refs |= _bound_refs((inner,))
    return refs


def _recall_refs(elements: tuple[Element, ...]) -> set[int]:
    """Reference numbers recalled (``@n``) anywhere in *elements*, descending into nesting."""
    refs: set[int] = set()
    for element in elements:
        match element:
            case RecallRef(ref):
                refs.add(ref)
            case Bound(_, inner):
                refs |= _recall_refs((inner,))
            case Group(inner):
                refs |= _recall_refs(inner)
            case Disjunction(branches):
                for branch in branches:
                    refs |= _recall_refs(branch)
            case Quantified(inner, _) | Negated(inner):
                refs |= _recall_refs((inner,))
    return refs


def _target_recalls_a_context_binding(sd: StructuralDescription) -> bool:
    """Whether the target recalls a reference bound only in a context (Case B).

    Such a target cannot fix its own span in pass 1 — the recall is unbound there —
    so find_matches enumerates the span and lets the right-context pre-seed resolve
    the recall (whose length then fixes the span).
    """
    context_binds = _bound_refs(sd.left_context) | _bound_refs(sd.right_context)
    return bool((_recall_refs(sd.target) - _bound_refs(sd.target)) & context_binds)


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
    re-evaluates left context → target → right context → exception, with the
    target *and* right-context references pre-seeded (references are scope-based)
    and alpha resolved order-independently.

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
    syllable_features = syllables.features if syllables else frozenset()
    if _cannot_match(sd, segments, letters, syllable_features):
        return []  # the word lacks material the rule provably needs — skip the search
    matches: list[Match] = []
    case_b = _target_recalls_a_context_binding(sd)

    for start in range(len(segments) + 1):
        # Pass 1: target alone, alpha-permissive — captures the structural span and
        # its reference bindings while committing no alpha (that is pass 2's job,
        # and must bind left-context first). Being fully alpha-blind, pass 1 yields
        # a true superset of valid spans in greedy order, so the greediest fully
        # valid span is still reached and none is missed.
        located = None
        seed_pass1 = Bindings(permissive_alpha=True)
        for end, pass1 in _match_sequence(
            sd.target, segments, start, seed_pass1, letters, boundaries, syllables
        ):
            located = _locate(
                sd, segments, start, end, _seed_references(pass1), letters, boundaries, syllables
            )
            if located is not None:
                break  # greediest fully-valid target parse at this start wins
        if located is None and case_b:
            # Case B: the target recalls a binding it does not contain, so pass 1
            # cannot fix its span. Enumerate the end (longest first, to stay greedy
            # like the rest of the matcher); _locate pre-seeds the right context's
            # binding, the recall resolves, and its length fixes the span.
            for end in range(len(segments), start - 1, -1):
                located = _locate(
                    sd, segments, start, end, _seed_references(Bindings()),
                    letters, boundaries, syllables,
                )
                if located is not None:
                    break
        if located is not None:
            matches.append(located)
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
    """Pass 2: evaluate the whole environment; return the Match or None.

    Left context → target → right context → exception. *seed* carries the target's
    reference bindings from pass 1; we additionally pre-bind the right context's
    references so an earlier position may recall them (references are scope-based,
    not left → right). Alpha is order-independent, so the walk order does not affect
    which alpha assignment is accepted.
    """
    seed = _seed_right_references(
        sd.right_context, segments, end, seed, letters, boundaries, syllables
    )
    for after_left in _match_ending_at(
        sd.left_context, segments, start, seed, letters, boundaries, syllables
    ):
        for after_target in _match_span(
            sd.target, segments, start, end, after_left, letters, boundaries, syllables
        ):
            # The target's own branch choices are those gained over the left context.
            target_choices = after_target.disjunction_choices[
                len(after_left.disjunction_choices) :
            ]
            for after_right in _match_starting_at(
                sd.right_context, segments, end, after_target, letters, boundaries, syllables
            ):
                if _pending_other_holds(after_right) and not _exception_blocks(
                    sd, segments, start, end, after_right, letters, boundaries, syllables
                ):
                    return Match(
                        start=start, end=end, bindings=after_right, target_choices=target_choices
                    )
    return None


def _seed_right_references(
    right_elements: tuple[Element, ...],
    segments: list[FeatureBundle],
    at: int,
    seed: Bindings,
    letters: LetterInventory,
    boundaries: frozenset[int],
    syllables: SyllableView | None,
) -> Bindings:
    """Pre-bind a right-anchored sequence's references so a position to its left can recall them.

    References are scope-based, not left → right (§2.3.1): a reference bound in the
    right context — or in the right exception — must be visible to the position that
    recalls it. We capture the *first* match alpha-blind (alpha is order-independent,
    so this commits nothing about alpha) and seed any references it binds. For a
    deterministic sequence the captured binding matches the one re-bound later; an
    ambiguous one (multiple matches binding differently) seeds the first, the only
    edge where the recall could see a different binding.
    """
    if not right_elements:
        return seed
    blind = _copy(seed)
    blind.permissive_alpha = True
    for captured in _match_starting_at(
        right_elements, segments, at, blind, letters, boundaries, syllables
    ):
        if captured.reference == seed.reference:
            return seed  # binds no new references
        enriched = _copy(seed)
        enriched.reference.update(captured.reference)
        return enriched
    return seed


def _pending_other_holds(bindings: Bindings) -> bool:
    """Every deferred ``!α`` constraint holds: α is bound and the atom differs."""
    return all(
        var in bindings.alpha and atom != bindings.alpha[var]
        for var, atom in bindings.pending_other
    )
