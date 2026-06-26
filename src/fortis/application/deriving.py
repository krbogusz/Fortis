"""Derivation driver: sweep a word through every rule, recording what fired.

``apply_rule`` applies one rule to a form (``list[FeatureBundle]``) according to
its application mode; ``derive`` runs the whole rule set in chronological order
and returns the per-word ``Derivation`` trace.

The mode *is* the sweep — a rule is applied in exactly one pass, never iterated
to a fixpoint (§6.2):

* **simultaneous** — every locus is found against the original form, then all
  rewrites are spliced at once; no application sees another's output. Overlapping
  loci within the rule are resolved leftmost-longest non-overlapping (the matcher
  already yields one longest match per start, ascending; §6.3's "undefined
  interaction" governs overlapping *rules*, not loci within one rule).
* **left_to_right** — scan rewriting in place, each output immediately visible;
  the cursor advances past the rewritten *output* (Kaplan & Kay obligatory
  rewrite), so a changed segment can feed a later locus.
* **right_to_left** — the mirror image.

Directional passes terminate for deletion (the form shrinks) and feature change
(the cursor strictly advances past the output). The one shape that would not is a
self-feeding rightward epenthesis (e.g. ``∅ -> x / x _`` under left_to_right),
which inserts past its own advancing cursor without bound; such rules are outside
the realistic diachronic rule set and carry no iteration cap.

The form is threaded through every rule whether or not it fires; only rules that
change the form contribute a ``DerivationStep``. The step's ``change`` summary is
a provisional feature-level diff — IPA rendering is a later milestone — and is
cosmetic: derivation correctness never depends on it.

Syllabification (§7): each rule (re)syllabifies the current form for its match
pass, using the ``SyllablePartsInventory`` constraints in force at the rule's
``time`` — so the input is syllabified before the first rule and the structure is
refreshed after every rule. This is what makes the ``$`` boundary assertion
matchable; with no ``sonorities``/``syllable_parts`` supplied there are no
boundaries and ``$`` simply never matches. (No rule in the current set uses
``$``, so this integration is presently preparatory — it changes no derivation
output, only enables ``$``-conditioned rules.)
"""
from __future__ import annotations

from dataclasses import replace

from src.fortis.application.applying import apply_match
from src.fortis.application.combining import matches_exactly
from src.fortis.application.matching import Match, SyllableView, find_matches
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.syllabifying import (
    SyllabificationError,
    consolidate_suprasegmentals,
    nuclei_by_position,
    syllabify,
)
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.elements import (
    Bound,
    Disjunction,
    Element,
    Group,
    LetterBundle,
    LetterRef,
    Negated,
    Quantified,
)
from src.fortis.models.features import FeatureInventory
from src.fortis.models.form import Form
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    Word,
)
from src.fortis.models.project import Project
from src.fortis.models.rules import (
    ApplicationMode,
    Rule,
    RuleInventory,
    StructuralDescription,
)
from src.fortis.models.segment import Segment
from src.fortis.models.tiers import Tier


def _syllable_features(features: FeatureInventory) -> frozenset[str]:
    """The names of the syllable-tier features (tone, stress, …)."""
    return frozenset(name for name, feature in features.items() if feature.tier == Tier.syllable)


def _resolve_elements(
    elements: tuple[Element, ...], project: Project, rule_id: str
) -> tuple[Element, ...]:
    """Replace each non-letter ``LetterRef`` run with its segmented ``LetterBundle``s.

    A run of letters and diacritics the parser kept as a single ``LetterRef`` (e.g.
    ``ʁʷ`` — one segment — or ``au`` — two) is sent through the segmenter and
    spliced in as one ``LetterBundle`` per segment, so it behaves like the segments
    it spells. A plain single letter is left as a ``LetterRef`` (still resolved
    against the inventory). Recurses into all nesting; a multi-segment run nested
    under a quantifier/binding/negation is wrapped in a ``Group`` to stay one inner.
    """
    resolved: list[Element] = []
    for element in elements:
        match element:
            case LetterRef(symbol) if symbol not in project.letters:
                segments = string_to_sequence(symbol, project).bundles()
                if not segments:
                    raise ValueError(
                        f"rule '{rule_id}': letter reference '{symbol}' resolves to no "
                        "segment — it is not a known letter or letter+diacritic sequence"
                    )
                resolved.extend(LetterBundle(bundle=segment) for segment in segments)
            case Group(inner):
                resolved.append(Group(_resolve_elements(inner, project, rule_id)))
            case Disjunction(branches):
                resolved.append(
                    Disjunction(tuple(_resolve_elements(b, project, rule_id) for b in branches))
                )
            case Negated(inner):
                resolved.append(Negated(_resolve_one(inner, project, rule_id)))
            case Quantified(inner, quant):
                resolved.append(Quantified(_resolve_one(inner, project, rule_id), quant))
            case Bound(ref, inner):
                resolved.append(Bound(ref, _resolve_one(inner, project, rule_id)))
            case _:
                resolved.append(element)
    return tuple(resolved)


def _resolve_one(element: Element, project: Project, rule_id: str) -> Element:
    """Resolve a single nested element; a multi-segment run becomes a ``Group``."""
    resolved = _resolve_elements((element,), project, rule_id)
    return resolved[0] if len(resolved) == 1 else Group(resolved)


def _resolve_rule(rule: Rule, project: Project) -> Rule:
    """A copy of *rule* with every ``LetterRef`` run in its description resolved."""
    sd = rule.sd
    resolved = StructuralDescription(
        target=_resolve_elements(sd.target, project, rule.id),
        result=_resolve_elements(sd.result, project, rule.id),
        left_context=_resolve_elements(sd.left_context, project, rule.id),
        right_context=_resolve_elements(sd.right_context, project, rule.id),
        left_exception=_resolve_elements(sd.left_exception, project, rule.id),
        right_exception=_resolve_elements(sd.right_exception, project, rule.id),
    )
    return replace(rule, sd=resolved)


def resolve_rule_letters(rules: RuleInventory, project: Project) -> RuleInventory:
    """Resolve the letter+diacritic runs a rule writes into per-segment bundles.

    The notation tokenises a contiguous run of letters and diacritics as one
    ``LetterRef`` whose symbol may be a complex segment like ``ʁʷ`` or a
    multi-segment run like ``au`` — neither a plain letter, so on its own it matches
    nothing. This sends every such run through the segmenter — the same path that
    turns an IPA word into segments — and rewrites it as one ``LetterBundle`` per
    segment, so a rule may spell complex segments directly. Run before derivation.

    Raises:
        ValueError: a run resolves to no segment (an unknown symbol).
    """
    return RuleInventory(
        {
            time: tuple(_resolve_rule(rule, project) for rule in rules_at_time)
            for time, rules_at_time in rules.items()
        }
    )


def _consolidate(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    letters: LetterInventory,
    syllable_features: frozenset[str],
) -> list[FeatureBundle]:
    """Resyllabify *form* and move each syllable's suprasegmentals onto its nucleus.

    Part of resyllabification: keeps suprasegmentals on the current nucleus as the
    nucleus shifts (e.g. epenthesis). Best-effort — an unsyllabifiable form or
    unconfigured syllabification leaves the form unchanged.

    Runs after each rule fires. Note the directional modes resyllabify per *step*
    inside ``apply_rule`` for matching, but consolidation happens here, once per
    rule — so a directional rule that shifts a nucleus and then tier-matches that
    same syllable later in the *same* pass would read the pre-consolidation strand.
    Unreachable with current data (the only directional rule is segment-tier).
    """
    if sonorities is None or syllable_parts is None or not syllable_features:
        return form
    nucleus_part = syllable_parts.get_nucleus(time)
    if nucleus_part is None or nucleus_part.definition is None:
        return form
    try:
        boundaries = syllabify(form, sonorities, syllable_parts, time, letters)
    except SyllabificationError:
        return form
    return consolidate_suprasegmentals(form, boundaries, nucleus_part.definition, syllable_features)


def _syllable_context(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    letters: LetterInventory,
    syllable_features: frozenset[str],
) -> tuple[frozenset[int], SyllableView | None]:
    """Boundaries (for ``$``) and the per-position nucleus view (for tier-aware matching).

    Returns ``(frozenset(), None)`` when syllabification is unconfigured.
    """
    if sonorities is None or syllable_parts is None:
        return frozenset(), None
    try:
        boundaries = syllabify(form, sonorities, syllable_parts, time, letters)
    except SyllabificationError:
        # Syllabification runs after every rule; an unsyllabifiable form (under
        # onset/coda constraints) yields no structure rather than aborting.
        return frozenset(), None
    nucleus_part = syllable_parts.get_nucleus(time)
    if nucleus_part is None or nucleus_part.definition is None:
        return boundaries, None
    nuclei = nuclei_by_position(form, boundaries, nucleus_part.definition)
    return boundaries, SyllableView(nuclei=nuclei, features=syllable_features)


def _boundaries(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    letters: LetterInventory,
) -> frozenset[int]:
    """Syllable boundaries of *form* at *time*, or none if syllabification is unconfigured."""
    if sonorities is None or syllable_parts is None:
        return frozenset()
    return syllabify(form, sonorities, syllable_parts, time, letters)


def _display_boundaries(
    form: list[FeatureBundle],
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    letters: LetterInventory,
) -> frozenset[int]:
    """Syllable boundaries for the trace — best-effort; an unsyllabifiable form is empty.

    Unlike the matcher's boundaries this is purely for display, so it ignores the
    ``$``-usage gate and never propagates a ``SyllabificationError``.
    """
    try:
        return _boundaries(form, sonorities, syllable_parts, time, letters)
    except SyllabificationError:
        return frozenset()


def apply_rule(
    rule: Rule,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
) -> Form:
    """Apply *rule* to *form* once, per its application mode.

    Returns a new form; *form* is never mutated. A rule whose loci do not
    match returns an unchanged copy. The form is re-syllabified for every rule, so
    ``$`` and syllable-tier matching always reflect the current form; an
    unsyllabifiable form (under onset/coda constraints) yields no structure rather
    than aborting, and a rule that consults neither ``$`` nor a syllable-tier
    feature is simply unaffected by it.
    """
    syllable_features = _syllable_features(features)
    match rule.application:
        case ApplicationMode.simultaneous:
            boundaries, view = _syllable_context(
                form.bundles(), sonorities, syllable_parts, rule.time, letters, syllable_features
            )
            return _apply_simultaneous(rule.sd, form, letters, features, boundaries, view)
        case ApplicationMode.left_to_right:
            return _apply_directional(
                rule.sd, form, letters, features, sonorities, syllable_parts, rule.time,
                syllable_features, False,
            )
        case ApplicationMode.right_to_left:
            return _apply_directional(
                rule.sd, form, letters, features, sonorities, syllable_parts, rule.time,
                syllable_features, True,
            )


def _select_non_overlapping(matches: list[Match]) -> list[Match]:
    """Leftmost-longest non-overlapping subset of *matches* (ascending by start)."""
    selected: list[Match] = []
    last_end = 0
    for match in matches:
        if match.start >= last_end:
            selected.append(match)
            last_end = match.end
    return selected


def _apply_simultaneous(
    sd: StructuralDescription,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    boundaries: frozenset[int],
    syllables: SyllableView | None,
) -> Form:
    """Find every locus against the original form, then splice all rewrites at once."""
    bundles = form.bundles()
    selected = _select_non_overlapping(find_matches(sd, bundles, letters, boundaries, syllables))
    out = form.copy()
    # Splice right-to-left so each replacement's indices stay valid, and compute every
    # replacement from the ORIGINAL form (no application sees another's output). Segments
    # outside the spliced span keep their identity; the replacement gets fresh ids.
    for match in sorted(selected, key=lambda m: m.start, reverse=True):
        replacement = apply_match(sd, match, bundles, letters, features, syllables)
        out.segments[match.start : match.end] = [
            Segment(bundle, form.segments[pos].id if pos is not None else out.fresh_id())
            for (bundle, pos) in replacement
        ]
    return out


def _apply_directional(
    sd: StructuralDescription,
    form: Form,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    syllable_features: frozenset[str],
    reverse: bool,
) -> Form:
    """Scan and rewrite in place; each output is visible to later loci in the pass.

    Because the form mutates as it is rewritten, it is re-syllabified before each
    scan so the ``$`` assertion and syllable-tier matching reflect the current form.
    """
    work = form.copy()
    cursor = len(work.segments) if reverse else 0
    while True:
        bundles = work.bundles()
        boundaries, view = _syllable_context(
            bundles, sonorities, syllable_parts, time, letters, syllable_features
        )
        if reverse:
            candidates = [
                m for m in find_matches(sd, bundles, letters, boundaries, view) if m.end <= cursor
            ]
            if not candidates:
                break
            # Rightmost, tie-broken to longest (min start) — the mirror of
            # leftmost-longest. (max end, then min start.)
            match = max(candidates, key=lambda m: (m.end, -m.start))
        else:
            candidates = [
                m for m in find_matches(sd, bundles, letters, boundaries, view) if m.start >= cursor
            ]
            if not candidates:
                break
            # Leftmost; the matcher already made it longest for that start.
            match = min(candidates, key=lambda m: m.start)

        replacement = apply_match(sd, match, bundles, letters, features, view)
        work.segments[match.start : match.end] = [
            Segment(bundle, work.segments[pos].id if pos is not None else work.fresh_id())
            for (bundle, pos) in replacement
        ]

        no_op = match.end == match.start and not replacement
        if reverse:
            # Advance leftward past the output's left edge; bump only a true no-op.
            cursor = match.start - 1 if no_op else match.start
        else:
            # Advance past the rewritten output; bump only a true no-op (a deletion
            # makes progress by shrinking the form, so it must not bump).
            cursor = match.start + 1 if no_op else match.start + len(replacement)
    return work


def _fired(before: list[FeatureBundle], after: list[FeatureBundle]) -> bool:
    """Whether the rule changed the form (a vacuous match is not a firing)."""
    if len(before) != len(after):
        return True
    return any(not matches_exactly(b, a) for b, a in zip(before, after, strict=True))


def derive(
    word: Word,
    form: Form,
    rules: RuleInventory,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
) -> Derivation:
    """Sweep *form* through every rule in time order, recording firing steps.

    Each rule (re)syllabifies the current form for its match pass, so the input is
    syllabified before the first rule and the structure is refreshed after every
    rule — without ``sonorities``/``syllable_parts`` there are simply no
    boundaries and the ``$`` assertion never matches.

    Rules that spell a complex symbol (e.g. ``ʁʷ``) or a multi-segment run must be
    passed through ``resolve_rule_letters`` first; an unresolved such ``LetterRef``
    matches nothing and the rule silently does not fire.

    Args:
        word: The word being derived (carried into the trace).
        form: The starting form (already segmented, from ``string_to_sequence``).
        rules: Rules keyed by time; applied ascending by time, file order within.
            Pre-resolve with ``resolve_rule_letters`` if any rule uses a complex
            symbol or multi-segment run.
        letters: Letter inventory, for shorthands and recalls.
        features: Feature inventory, for the geometry-aware merge.
        sonorities: Sonority scale for syllabification (optional).
        syllable_parts: Syllable-part constraints supplying the nucleus (optional).
    """
    current = form
    steps: list[DerivationStep] = []
    syllable_features = _syllable_features(features)

    for time in sorted(rules.keys()):
        for rule in rules[time]:
            before = current  # Form
            before_bundles = current.bundles()
            after = apply_rule(rule, current, letters, features, sonorities, syllable_parts)
            after_bundles = after.bundles()
            if _fired(before_bundles, after_bundles):
                # Resyllabify after the rule, keeping each syllable's suprasegmentals
                # on its (possibly shifted) nucleus. (Task 3c replaces this with the tier
                # cleanup pass; the bundle round-trip mints fresh ids meanwhile.)
                after_bundles = _consolidate(
                    after_bundles, sonorities, syllable_parts, rule.time, letters, syllable_features
                )
                after = Form.from_bundles(after_bundles)
                steps.append(
                    DerivationStep(
                        before=before,
                        rule=rule,
                        after=after,
                        before_boundaries=_display_boundaries(
                            before_bundles, sonorities, syllable_parts, rule.time, letters
                        ),
                        after_boundaries=_display_boundaries(
                            after_bundles, sonorities, syllable_parts, rule.time, letters
                        ),
                    )
                )
                current = after

    surface_boundaries = _display_boundaries(
        current.bundles(), sonorities, syllable_parts, max(rules, default=0), letters
    )
    return Derivation(
        word=word,
        input=form,
        steps=tuple(steps),
        surface=current,
        surface_boundaries=surface_boundaries,
    )
