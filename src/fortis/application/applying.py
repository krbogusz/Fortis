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

Complex elements are resolved before the merge/replace logic: a disjunction to its
matched branch, a group to its sub-sequence, a fixed-count quantifier to that many
copies. A **variable** quantifier in the result mirrors the target — it repeats as
many times as the target matched, taking that count from the span — on the merge
path (``X* -> Y*``) and the replacement path (``X* -> a*``) alike. What still raises
(rather than misapply silently): *two* variable-width target elements (the span
split is ambiguous), a variable quantifier whose inner is itself variable-width, and
a variable result quantifier with no single variable target to mirror.
"""
from __future__ import annotations

from src.fortis.application.combining import merge

# Forward reference only; importing the class would be circular-safe but the type
# is used purely for annotation here.
from src.fortis.application.matching import Match, SyllableView
from src.fortis.models.bindings import Bindings
from src.fortis.models.bundles import FeatureBundle, ResultBundle
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    Group,
    LetterBundle,
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
from src.fortis.models.values import AlphaRef

# Reused verbatim from the validator so the applier's path decision can never
# disagree with what the parser accepted. ``parsing/rule_validation`` is the
# single source of truth for "does this result element merge or replace?".
from src.fortis.parsing.rule_validation import _is_merge_bundle

# Target elements the merge path can pair one-to-one with the span: each consumes
# exactly one segment, except Null, which consumes none. A ``Bound`` wrapping a
# wider inner is caught by the ``consumed == len(span)`` guard below, not here.
_CONSUMES_ONE = (BundleElem, LetterRef, LetterBundle, Wildcard, RecallRef, Negated, Bound)


def _content(elements: tuple[Element, ...]) -> list[Element]:
    """Top-level elements with zero-width boundary assertions removed.

    Boundaries are positional markers that never count toward cardinality.
    """
    return [e for e in elements if not isinstance(e, (WordBoundary, SyllableBoundary))]


def _resolve_disjunctions(content: list[Element], choices: tuple[int, ...]) -> list[Element]:
    """Replace each top-level ``Disjunction`` with its chosen branch's elements.

    The i-th disjunction encountered takes branch ``choices[i]`` — the branch the
    *target* matched (``Match.target_choices``). A result disjunction therefore
    reuses the matching target disjunction's branch (positional 1-to-1); resolving
    the target disjunction to a plain element is also what lets it ride the merge
    path. Validation guarantees ≤1 disjunction per side and an in-range index, so a
    bare element (collapse, ``(A|B|C) -> x``) simply has no disjunction to resolve.
    """
    resolved: list[Element] = []
    index = 0
    for element in content:
        if isinstance(element, Disjunction):
            resolved.extend(element.branches[choices[index]])
            index += 1
        else:
            resolved.append(element)
    return resolved


def _expand(content: list[Element], variable_count: int | None = None) -> list[Element]:
    """Flatten groups and expand quantifiers to a flat, one-element-per-segment list.

    A ``Group``'s sub-sequence is spliced in; a fixed ``Quantified`` (``{n,n}``) is
    repeated ``n`` times. A *variable* quantifier (``*``, ``{1,2}``, …) is repeated
    ``variable_count`` times when that is given — its per-locus width, recovered
    from the matched span — and otherwise left in place (so the caller can decide
    the merge vs replacement path first, then re-expand with the count).
    """
    flat: list[Element] = []
    for element in content:
        if isinstance(element, Group):
            flat.extend(_expand(list(element.elements), variable_count))
        elif isinstance(element, Quantified):
            quant = element.quant
            if quant.max is not None and quant.min == quant.max:
                flat.extend(_expand([element.inner], variable_count) * quant.min)
            elif variable_count is not None:
                flat.extend(_expand([element.inner], variable_count) * variable_count)
            else:
                flat.append(element)  # variable width unknown here — left for the merge path
        else:
            flat.append(element)
    return flat


def _min_width(element: Element) -> int | None:
    """The fixed number of segments an element consumes, or ``None`` if variable."""
    match element:
        case Null():
            return 0
        case Group(inner):
            widths = [_min_width(e) for e in inner]
            return None if any(w is None for w in widths) else sum(widths)
        case Quantified(inner, quant):
            if quant.max is not None and quant.min == quant.max:
                inner_width = _min_width(inner)
                return None if inner_width is None else inner_width * quant.min
            return None
        case Bound(_, inner):
            return _min_width(inner)  # a bound element spans whatever its content does
        case _:
            return 1


def _variable_count(flat_target: list[Element], span_width: int) -> int | None:
    """Repetitions a single variable-width target quantifier needs to fill the span.

    *flat_target* has groups and fixed quantifiers already expanded, so only flat
    one-segment elements, the null, and leftover variable ``Quantified``s remain.
    Returns ``None`` when the target is all fixed-width. Refuses (loudly) when more
    than one variable element remains — the split between them is ambiguous.
    """
    variable = [el for el in flat_target if isinstance(el, Quantified)]
    if not variable:
        return None
    fixed = 0
    for el in flat_target:
        if isinstance(el, Quantified):
            continue
        width = _min_width(el)  # a Bound/group consumes more than one segment
        if width is None:
            raise NotImplementedError(
                "a variable-width non-quantifier element on the merge path is unsupported"
            )
        fixed += width
    if len(variable) > 1:
        raise NotImplementedError(
            "more than one variable-width element on the merge path (ambiguous span split)"
        )
    inner_width = _min_width(variable[0].inner)
    if not inner_width:  # None (variable inner) or 0
        raise NotImplementedError("a variable quantifier with a non-fixed-width inner is refused")
    remaining = span_width - fixed
    if remaining < 0 or remaining % inner_width:
        raise NotImplementedError("span width does not divide evenly across the quantifier")
    return remaining // inner_width


def _resolve_result_bundle(bundle: ResultBundle, bindings: Bindings) -> FeatureBundle:
    """Turn a result bundle into a realized delta, resolving alpha recalls.

    A spec value of ``None`` is kept (it instructs ``merge`` to delink). A bare
    ``AlphaRef`` is replaced by its bound value. A **conditional** feature
    (``[<n: F>]``) is applied only when its label's condition held during matching
    (recorded in ``bindings.conditions``); when the condition was false the feature
    is skipped. A missing label means the condition was never evaluated (e.g. the
    target conditional sat in a branch that did not run) — a real inconsistency, so
    it raises rather than silently dropping the feature. An alpha recall inside a
    contour is resolved limb by limb (``[F: α>3]`` recalls α into the first limb).
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
        elif isinstance(value, tuple):
            # A contour: resolve any alpha recall limb by limb, keeping the shape. A
            # limb must be a single value, so an alpha bound to a contour cannot nest
            # into one — refuse loudly rather than build a malformed nested value.
            limbs: list[object] = []
            for limb in value:
                if not isinstance(limb, AlphaRef):
                    limbs.append(limb)
                    continue
                bound = bindings.alpha[limb.var]
                if isinstance(bound, tuple):
                    raise NotImplementedError(
                        f"alpha '{limb.var}' is bound to a contour and cannot be recalled "
                        f"into a single contour limb of '{feature}'"
                    )
                limbs.append(bound)
            value = tuple(limbs)
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

        case LetterBundle(bundle):
            return [FeatureBundle(dict(bundle.data))]

        case RecallRef(ref):
            bound = bindings.reference.get(ref)
            if bound is None:
                raise KeyError(f"result recall @{ref} has no bound element")
            # Replay every captured segment (one for 1=[X], several for 1=([X][Y])).
            return [FeatureBundle(dict(seg.data)) for seg in bound]

        case Null():
            return []

        case _:
            raise NotImplementedError(f"result element {element!r} is not yet supported")


def _refuse_nonnucleus_syllable_write(
    result_elem: Element,
    pos: int | None,
    segments: list[FeatureBundle],
    syllables: SyllableView | None,
) -> None:
    """Refuse a syllable-tier result feature whose target segment is not the nucleus.

    Suprasegmentals live on the syllable's nucleus, so a syllable-tier write that
    does not land on the nucleus is a cross-syllable edit (unsupported). With no
    syllable view (syllabification unconfigured) there is no nucleus to check
    against, so the write proceeds as an ordinary segment merge.
    """
    if syllables is None or not isinstance(result_elem, ResultElem):
        return
    tier_features = [f for f in result_elem.bundle if f in syllables.features]
    if not tier_features:
        return
    is_nucleus = pos is not None and syllables.at(pos) is segments[pos]
    if not is_nucleus:
        raise NotImplementedError(
            f"writing syllable-tier feature(s) {sorted(tier_features)} to a non-nucleus "
            "target is not supported (suprasegmentals live on the syllable nucleus)"
        )


def apply_match(
    sd: StructuralDescription,
    match: Match,
    segments: list[FeatureBundle],
    letters: LetterInventory,
    features: FeatureInventory,
    syllables: SyllableView | None = None,
) -> list[FeatureBundle]:
    """Compute the bundles that replace ``segments[match.start:match.end]``.

    Args:
        sd: The rule being applied.
        match: One locus from the matcher (target span + bindings).
        segments: The whole current word.
        letters: Letter inventory, for letter shorthands / recalls in the result.
        features: Feature inventory, for the geometry-aware merge.
        syllables: Per-position nucleus view. A syllable-tier result feature is
            written only when its target is the nucleus; a non-nucleus syllable-tier
            write is refused.
    """
    span = segments[match.start : match.end]
    # Resolve disjunction branches, flatten groups, and expand fixed quantifiers.
    # A *variable* quantifier in the result mirrors the target: it repeats as many
    # times as the target matched, taking that count from the span — on the merge
    # path (X* -> Y*) and the replacement path (X* -> a*) alike. The count is only
    # derived when the result actually has one, so a fixed or collapsing result over
    # a multi-variable target (e.g. X* Y* -> z) stays valid.
    target_content = _expand(_resolve_disjunctions(_content(sd.target), match.target_choices))
    result_content = _expand(_resolve_disjunctions(_content(sd.result), match.target_choices))
    if any(isinstance(element, Quantified) for element in result_content):
        count = _variable_count(target_content, len(span))
        target_content = _expand(target_content, count)
        result_content = _expand(result_content, count)

    if not any(_is_merge_bundle(e) for e in result_content):
        # Replacement path: the result fully specifies the output; the span
        # collapses into or expands to it, with no per-segment correspondence.
        out: list[FeatureBundle] = []
        for element in result_content:
            out.extend(_render_result_element(element, None, match.bindings, letters, features))
        return out

    # Merge path: target and result line up one-to-one.
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
            source, pos = None, None  # insertion point — nothing to merge onto
        else:
            source, pos = segments[cursor], cursor
            cursor += 1
        _refuse_nonnucleus_syllable_write(result_elem, pos, segments, syllables)
        out.extend(_render_result_element(result_elem, source, match.bindings, letters, features))
    return out
