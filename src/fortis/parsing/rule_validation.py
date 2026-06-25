"""Structural validation of a parsed rule (the §2.x well-formedness rules).

Operates on an assembled ``StructuralDescription`` — a pure, feature-free
function, so it can be tested on hand-built descriptions. Called from
``load_rule`` after a successful parse. The rule AST is permissive by design
(it can represent invalid rules); this layer is where those problems are
caught, accumulating every error rather than failing on the first.

Implemented:
    §2.1.1  a result feature-bundle (which merges) requires equal target/result
            counts; letter-shorthand results may collapse or expand a span, so a
            count mismatch is invalid only when a result bundle is present
    §2.1.2  a merge-bundle result must carry the same quantifier as its target;
            full-replacement letter results are unconstrained (§2.1.3: ∅ exempt)
    §2.2.1  ∅ is not valid in context or exception positions
    §2.2.4  a boundary may not be the sole element on the target or result side
    §2.3    references — every ``@n`` has an ``n=``; every ``n=`` is recalled;
            ``n=`` is not allowed in result. Binding/recall is scope-based, not
            order-based (the target is ref-bound first at match time), so no
            cross-position ordering is imposed — `1=a → b / @1 _` is valid.
    §2.4.1  every alpha variable is bound in target or context
    §2.5.4  ∅ as the entire target is invalid without a context
    §2.7    a result disjunction needs a paired target disjunction (same arity);
            at most one disjunction per side, top-level (§2.7.1)
    §2.8.1  negation is not valid in result position
    §2.8.2  negation may not be applied to ∅ or []
    §2.9    each conditional label is a condition (target or context) and applies
            ≥1 result feature; only orphan labels error

Deferred: §2.5.1-.3/.5 null insertion/deletion *semantics* (runtime, not
validation). (The old §2.3.1 'binding must precede recall' ordering constraint
was dropped — binding/recall is scope-based, not order-based.)
"""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    Group,
    Negated,
    Null,
    Quantified,
    Quantifier,
    RecallRef,
    ResultElem,
    SyllableBoundary,
    Wildcard,
    WordBoundary,
)
from src.fortis.models.rules import StructuralDescription
from src.fortis.models.values import AlphaRef
from src.fortis.result import Err, Ok, Result


@dataclass
class _Markers:
    """Markers gathered from one position's element sequence."""

    binds: list[int] = field(default_factory=list)
    recalls: set[int] = field(default_factory=set)
    alphas: set[str] = field(default_factory=set)
    labels: list[int] = field(default_factory=list)


def _alphas_in_value(value: object) -> set[str]:
    """Alpha variable names in a spec value — single value or contour limbs."""
    limbs = value if isinstance(value, tuple) else (value,)
    return {limb.var for limb in limbs if isinstance(limb, AlphaRef)}


def _collect(elements: tuple[Element, ...], markers: _Markers) -> None:
    """Recursively gather reference/alpha/label markers, descending into nesting."""
    for element in elements:
        match element:
            case BundleElem(bundle) | ResultElem(bundle):
                for spec in bundle.values():
                    markers.alphas |= _alphas_in_value(spec.value)
                    if spec.condition_label is not None:
                        markers.labels.append(spec.condition_label)
            case Bound(ref, inner):
                markers.binds.append(ref)
                _collect((inner,), markers)
            case RecallRef(ref):
                markers.recalls.add(ref)
            case Group(inner):
                _collect(inner, markers)
            case Quantified(inner, _):
                _collect((inner,), markers)
            case Negated(inner):
                _collect((inner,), markers)
            case Disjunction(branches):
                for branch in branches:
                    _collect(branch, markers)
            case _:
                pass


def _markers(elements: tuple[Element, ...]) -> _Markers:
    markers = _Markers()
    _collect(elements, markers)
    return markers


def _cardinality(elements: tuple[Element, ...]) -> int:
    """Top-level element count, excluding zero-width boundary assertions."""
    return sum(1 for e in elements if not isinstance(e, (WordBoundary, SyllableBoundary)))


def _is_merge_bundle(element: Element) -> bool:
    """Whether a result element merges into a source segment (vs. replaces it).

    Only feature bundles merge (preserving the target's unspecified features);
    letter shorthands and recalls replace wholesale. A quantified bundle still
    merges.
    """
    match element:
        case ResultElem():
            return True
        case Quantified(inner, _):
            return _is_merge_bundle(inner)
        case _:
            return False


def _walk(elements: tuple[Element, ...]) -> Iterator[Element]:
    """Yield every element in a sequence, descending into all nesting."""
    for element in elements:
        yield element
        match element:
            case Group(inner):
                yield from _walk(inner)
            case Disjunction(branches):
                for branch in branches:
                    yield from _walk(branch)
            case Negated(inner) | Quantified(inner, _) | Bound(_, inner):
                yield from _walk((inner,))
            case _:
                pass


def _without_boundaries(elements: tuple[Element, ...]) -> list[Element]:
    """Top-level elements with zero-width boundary assertions removed."""
    return [e for e in elements if not isinstance(e, (WordBoundary, SyllableBoundary))]


def _quant(element: Element) -> Quantifier | None:
    """The quantifier on an element, or None if it carries none."""
    return element.quant if isinstance(element, Quantified) else None


def validate_structural_description(sd: StructuralDescription) -> Result[None, list[str]]:
    """Validate a parsed rule against the structural well-formedness rules.

    Args:
        sd: The parsed structural description to check.
    """
    errors: list[str] = []

    target = _markers(sd.target)
    result = _markers(sd.result)
    left_ctx = _markers(sd.left_context)
    right_ctx = _markers(sd.right_context)
    left_exc = _markers(sd.left_exception)
    right_exc = _markers(sd.right_exception)

    # §2.1.1 — a result feature-bundle merges into its corresponding target
    # (preserving the target's other features), so a bundle result requires
    # equal target/result counts. Letter shorthands (and other full
    # replacements) specify the output outright, so an all-replacement result
    # may freely collapse or expand a span. A count mismatch with any result
    # bundle is therefore ambiguous — "which target does the bundle merge with?".
    target_count = _cardinality(sd.target)
    result_count = _cardinality(sd.result)
    if target_count != result_count and any(_is_merge_bundle(e) for e in sd.result):
        errors.append(
            f"Ambiguous rule: target has {target_count} element(s) but result has "
            f"{result_count}, and a result feature-bundle has no unambiguous target to "
            "merge with — a count mismatch is only allowed with letter-shorthand results"
        )

    # §2.3 — references.
    bound_refs = {
        *target.binds,
        *result.binds,
        *left_ctx.binds,
        *right_ctx.binds,
        *left_exc.binds,
        *right_exc.binds,
    }
    recalled_refs = (
        target.recalls
        | result.recalls
        | left_ctx.recalls
        | right_ctx.recalls
        | left_exc.recalls
        | right_exc.recalls
    )
    for ref in sorted(recalled_refs - bound_refs):
        errors.append(f"Recall '@{ref}' has no matching binding '{ref}='")
    for ref in sorted(bound_refs - recalled_refs):
        errors.append(f"Binding '{ref}=' is never recalled by '@{ref}'")
    for ref in sorted(set(result.binds)):
        errors.append(f"Binding '{ref}=' is not allowed in result position")

    # §2.4.1 — every alpha variable must be bound in target or context.
    bound_alphas = target.alphas | left_ctx.alphas | right_ctx.alphas
    used_alphas = result.alphas | left_exc.alphas | right_exc.alphas
    for var in sorted(used_alphas - bound_alphas):
        errors.append(f"Alpha variable '{var}' is used but never bound in target or context")

    # §2.9 — a conditional label must be a *condition* somewhere (target or context)
    # AND drive at least one *result* feature. A label may repeat: several result
    # features can share it (a conditional multi-feature change, e.g. "become a"), and
    # several conditions can share it (target + context, AND-ed). Only orphans error:
    # a result feature with no condition, or a condition that gates nothing.
    condition_labels = set(target.labels) | set(left_ctx.labels) | set(right_ctx.labels)
    result_labels = set(result.labels)
    for label in sorted(result_labels - condition_labels):
        errors.append(
            f"Conditional label '{label}' is applied in the result but has no condition "
            "in the target or context"
        )
    for label in sorted(condition_labels - result_labels):
        errors.append(
            f"Conditional label '{label}' is a condition but applies no result feature"
        )

    has_context = bool(sd.left_context or sd.right_context)

    # §2.2.1 — ∅ is not valid in context or exception positions.
    for label, position in (
        ("left context", sd.left_context),
        ("right context", sd.right_context),
        ("left exception", sd.left_exception),
        ("right exception", sd.right_exception),
    ):
        if any(isinstance(e, Null) for e in _walk(position)):
            errors.append(f"∅ (null) is not valid in {label} position")

    # §2.2.4 — a boundary may not be the sole element on the target or result side.
    for label, side in (("target", sd.target), ("result", sd.result)):
        if side and all(isinstance(e, (WordBoundary, SyllableBoundary)) for e in side):
            errors.append(f"A boundary may not be the only element in {label} position")

    # §2.5.4 — ∅ as the entire target is invalid without a context.
    if len(sd.target) == 1 and isinstance(sd.target[0], Null) and not has_context:
        errors.append("∅ as the entire target requires a context")

    # §2.8.1 — negation is not valid in result position.
    if any(isinstance(e, Negated) for e in _walk(sd.result)):
        errors.append("Negation '!' is not valid in result position")

    # §2.8.2 — negation may not be applied to ∅ or [].
    all_positions = (
        sd.target,
        sd.result,
        sd.left_context,
        sd.right_context,
        sd.left_exception,
        sd.right_exception,
    )
    if any(
        isinstance(e, Negated) and isinstance(e.inner, (Null, Wildcard))
        for position in all_positions
        for e in _walk(position)
    ):
        errors.append("Negation '!' may not be applied to ∅ or []")

    # §2.1.2 — a merge-bundle result lines up 1:1 with its target (§2.1.1), so it
    # must carry the same quantifier. A full-replacement letter result is
    # unconstrained by the target's quantifier (e.g. `a{2} → b` collapses freely).
    # (§2.1.3: ∅ carries no quantifier and is exempt.)
    target_seq = _without_boundaries(sd.target)
    result_seq = _without_boundaries(sd.result)
    if len(target_seq) == len(result_seq):
        for left, right in zip(target_seq, result_seq, strict=True):
            if isinstance(left, Null) or isinstance(right, Null):
                continue
            if _is_merge_bundle(right) and _quant(left) != _quant(right):
                errors.append(
                    "A merge-bundle result element must carry the same quantifier as "
                    "its corresponding target element"
                )
                break

    # §2.7 — a disjunction in result must pair with a target disjunction (same arity).
    for index, right in enumerate(result_seq):
        if isinstance(right, Disjunction):
            paired = target_seq[index] if index < len(target_seq) else None
            if not isinstance(paired, Disjunction) or len(paired.branches) != len(right.branches):
                errors.append(
                    "A disjunction in result position needs a corresponding target "
                    "disjunction with the same number of branches"
                )
                break

    # §2.7.1 — result/target branch pairing resolves *top-level* disjunctions
    # positionally, so a side may carry at most one top-level disjunction, and a
    # nested disjunction may not coexist with a top-level one (the recorded choice
    # would desync from how the result is resolved). A nested disjunction on its own
    # — e.g. a `(j|w)?` alternation under a quantifier, with no result disjunction to
    # pair — is fine: the matcher handles it and no branch is resolved into a result.
    for side, top_seq, elements in (
        ("target", target_seq, sd.target),
        ("result", result_seq, sd.result),
    ):
        top_level = [e for e in top_seq if isinstance(e, Disjunction)]
        nested = sum(1 for e in _walk(elements) if isinstance(e, Disjunction)) - len(top_level)
        if len(top_level) > 1:
            errors.append(f"at most one top-level disjunction per side (in the {side})")
        if nested and top_level:
            errors.append(
                f"a nested disjunction cannot coexist with a top-level disjunction (in the {side})"
            )

    if errors:
        return Err(errors)
    return Ok(None)
