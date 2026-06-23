"""Result application: rewrite a matched span per a rule's result.

``apply_match`` takes one locus found by the matcher (a ``Match``) and the rule,
and returns the feature bundles that replace the matched span ``[start, end)``.
The driver splices that replacement back into the word and handles application
modes; this module only computes a single locus's rewrite.

Two paths, decided exactly as the parser's validator decides cardinality
(``_is_merge_bundle``, reused verbatim below so the two never diverge):

* **Replacement** — the result is all letters / recalls / ``∅`` (no merge
  bundle). It fully specifies the output, so the whole span collapses into or
  expands to the rendered result, with no per-segment correspondence
  (``au → e``, ``e → au``, deletion, insertion).
* **Merge** — the result contains a feature bundle, which preserves the
  unspecified features of its source segment. Target and result then line up
  one-to-one (equal counts, ``∅`` included). The span is walked with a cursor
  that advances past each consuming target element but not past a ``∅`` (which
  consumes nothing and marks an insertion point).

A merge-path target may be any single-segment element — feature bundle, letter,
wildcard, recall, a negated class (``![+nasal]``), or a single-segment binding
(``1=[X]``) — plus ``∅`` for an insertion point.

Conditional result features (``[<n: F>]``) are applied only when their label's
condition held during matching (recorded in ``bindings.conditions``); otherwise
the feature is skipped.

Deferred (each raises ``NotImplementedError`` rather than silently misapplying):
quantified / grouped / disjoined target or result elements on the merge path,
disjunction-result branch pairing, and alpha recall into a *contour* limb in the
result.
"""

from src.fortis.application.combining import merge

# Forward reference only; importing the class would be circular-safe but the type
# is used purely for annotation here.
from src.fortis.application.matching import Match
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle, ResultBundle
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Element,
    LetterRef,
    Negated,
    Null,
    Quantified,
    RecallRef,
    ResultElem,
    SyllableBoundary,
    Wildcard,
    WordBoundary,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import LetterInventory
from src.fortis.models.rules import StructuralDescription
from src.fortis.models.specs import FeatureSpec
from src.fortis.models.values import AlphaRef, Value

# Reused verbatim from the validator so the applier's path decision can never
# disagree with what the parser accepted. ``parsing/rule_validation`` is the
# single source of truth for "does this result element merge or replace?".
from src.fortis.parsing.rule_validation import _is_merge_bundle

# Target elements the merge path can pair one-to-one with the span: each consumes
# exactly one segment, except Null, which consumes none. A ``Bound`` wrapping a
# wider inner is caught by the ``consumed == len(span)`` guard below, not here.
_CONSUMES_ONE = (BundleElem, LetterRef, Wildcard, RecallRef, Negated, Bound)


def _content(elements: tuple[Element, ...]) -> list[Element]:
    """Top-level elements with zero-width boundary assertions removed.

    Boundaries are positional markers that never count toward cardinality.
    """
    return [e for e in elements if not isinstance(e, (WordBoundary, SyllableBoundary))]


def _limbs(value: Value) -> tuple[object, ...]:
    """The contour limbs of a value (a scalar becomes a single limb)."""
    return value if isinstance(value, tuple) else (value,)


def _resolve_result_bundle(bundle: ResultBundle, bindings: Bindings) -> FeatureBundle:
    """Turn a result bundle into a realized delta, resolving alpha recalls.

    A spec value of ``None`` is kept (it instructs ``merge`` to delink). A bare
    ``AlphaRef`` is replaced by its bound value. A **conditional** feature
    (``[<n: F>]``) is applied only when its label's condition held during matching
    (recorded in ``bindings.conditions``); when the condition was false the feature
    is skipped. A missing label means the condition was never evaluated (e.g. the
    target conditional sat in a branch that did not run) — a real inconsistency, so
    it raises rather than silently dropping the feature. An alpha recall buried in a
    contour limb is still unsupported and raises.
    """
    delta = FeatureBundle()
    for feature, spec in bundle.items():
        if spec.condition_label is not None:
            if spec.condition_label not in bindings.conditions:
                raise NotImplementedError(
                    f"conditional result feature '{feature}' (label {spec.condition_label}) "
                    "has no condition recorded from matching"
                )
            if not bindings.conditions[spec.condition_label]:
                continue  # condition was false → do not apply this feature
        value = spec.value
        if isinstance(value, AlphaRef):
            value = bindings.alpha[value.var]
        elif isinstance(value, tuple) and any(isinstance(limb, AlphaRef) for limb in _limbs(value)):
            raise NotImplementedError(
                f"alpha recall inside a contour result ('{feature}') is not yet supported"
            )
        delta[feature] = FeatureSpec(feature=feature, value=value)
    return delta


def _render_result_element(
    element: Element,
    source: FeatureBundle | None,
    bindings: Bindings,
    letters: LetterInventory,
    features: FeatureInventory,
) -> list[FeatureBundle]:
    """The bundles a single result element produces, given its paired *source*.

    *source* is the matched segment a merge bundle merges onto, or ``None`` at an
    insertion point (a ``∅`` target). Letters and recalls replace wholesale and
    ignore *source*; ``∅`` in the result deletes (produces nothing).
    """
    match element:
        case ResultElem(bundle):
            delta = _resolve_result_bundle(bundle, bindings)
            base = source if source is not None else FeatureBundle()
            return [merge(base, delta, features)]

        case LetterRef(symbol):
            if symbol not in letters:
                raise KeyError(f"result letter '{symbol}' is not in the letter inventory")
            return [FeatureBundle(dict(letters[symbol].bundle.data))]

        case RecallRef(ref):
            bound = bindings.reference.get(ref)
            if bound is None:
                raise KeyError(f"result recall @{ref} has no bound element")
            return [FeatureBundle(dict(bound.data))]

        case Null():
            return []

        case _:
            raise NotImplementedError(f"result element {element!r} is not yet supported")


def apply_match(
    sd: StructuralDescription,
    match: Match,
    segments: list[FeatureBundle],
    letters: LetterInventory,
    features: FeatureInventory,
) -> list[FeatureBundle]:
    """Compute the bundles that replace ``segments[match.start:match.end]``.

    Args:
        sd: The rule being applied.
        match: One locus from the matcher (target span + bindings).
        segments: The whole current word.
        letters: Letter inventory, for letter shorthands / recalls in the result.
        features: Feature inventory, for the geometry-aware merge.
    """
    span = segments[match.start : match.end]
    result_content = _content(sd.result)

    if not any(_is_merge_bundle(e) for e in result_content):
        # Replacement path: the result fully specifies the output; the span
        # collapses into or expands to it, with no per-segment correspondence.
        out: list[FeatureBundle] = []
        for element in result_content:
            out.extend(_render_result_element(element, None, match.bindings, letters, features))
        return out

    # Merge path: target and result line up one-to-one. Only flat, fixed-width
    # target elements are supported; anything else is deferred rather than
    # silently misaligned.
    target_content = _content(sd.target)
    if len(target_content) != len(result_content):
        raise NotImplementedError(
            "merge result with unequal target/result counts is not supported "
            f"(target {len(target_content)}, result {len(result_content)})"
        )
    for element in target_content:
        if isinstance(element, Quantified) or not isinstance(element, (*_CONSUMES_ONE, Null)):
            raise NotImplementedError(f"merge-path target element {element!r} is not yet supported")
    consumed = sum(0 if isinstance(e, Null) else 1 for e in target_content)
    if consumed != len(span):
        raise NotImplementedError(
            f"merge-path span width {len(span)} does not match target {consumed}"
        )

    out = []
    cursor = match.start
    for target_elem, result_elem in zip(target_content, result_content, strict=True):
        if isinstance(target_elem, Null):
            source = None  # insertion point — nothing to merge onto
        else:
            source = segments[cursor]
            cursor += 1
        out.extend(_render_result_element(result_elem, source, match.bindings, letters, features))
    return out
