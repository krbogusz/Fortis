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

from src.fortis.application.applying import apply_match
from src.fortis.application.combining import matches_exactly
from src.fortis.application.matching import Match, find_matches
from src.fortis.application.syllabifying import SyllabificationError, syllabify
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.elements import SyllableBoundary
from src.fortis.models.features import FeatureInventory
from src.fortis.models.inventories import (
    LetterInventory,
    SonoritiesInventory,
    SyllablePartsInventory,
    Word,
)
from src.fortis.models.rules import (
    ApplicationMode,
    Rule,
    RuleInventory,
    StructuralDescription,
)
from src.fortis.parsing.rule_validation import _walk


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


def _uses_boundary(sd: StructuralDescription) -> bool:
    """Whether the rule references the ``$`` syllable-boundary assertion anywhere."""
    sequences = (
        sd.target,
        sd.result,
        sd.left_context,
        sd.right_context,
        sd.left_exception,
        sd.right_exception,
    )
    return any(isinstance(e, SyllableBoundary) for seq in sequences for e in _walk(seq))


def apply_rule(
    rule: Rule,
    segments: list[FeatureBundle],
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
) -> list[FeatureBundle]:
    """Apply *rule* to *segments* once, per its application mode.

    Returns a new form; *segments* is never mutated. A rule whose loci do not
    match returns an unchanged copy. Syllabification runs only for rules that
    actually reference ``$`` (its sole consumer) — so a ``$``-free rule never
    syllabifies, and thus never aborts on a transiently-unsyllabifiable form under
    onset/coda constraints it does not consult.
    """
    if not _uses_boundary(rule.sd):
        sonorities = syllable_parts = None  # $ unused → skip syllabification entirely
    match rule.application:
        case ApplicationMode.simultaneous:
            boundaries = _boundaries(segments, sonorities, syllable_parts, rule.time, letters)
            return _apply_simultaneous(rule.sd, segments, letters, features, boundaries)
        case ApplicationMode.left_to_right:
            return _apply_directional(
                rule.sd, segments, letters, features, sonorities, syllable_parts, rule.time, False
            )
        case ApplicationMode.right_to_left:
            return _apply_directional(
                rule.sd, segments, letters, features, sonorities, syllable_parts, rule.time, True
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
    segments: list[FeatureBundle],
    letters: LetterInventory,
    features: FeatureInventory,
    boundaries: frozenset[int],
) -> list[FeatureBundle]:
    """Find every locus against the original form, then splice all rewrites at once."""
    selected = _select_non_overlapping(find_matches(sd, segments, letters, boundaries))
    out = list(segments)
    # Splice right-to-left so each replacement's indices stay valid, and compute
    # every replacement from the ORIGINAL form (no application sees another's output).
    for match in sorted(selected, key=lambda m: m.start, reverse=True):
        out[match.start : match.end] = apply_match(sd, match, segments, letters, features)
    return out


def _apply_directional(
    sd: StructuralDescription,
    segments: list[FeatureBundle],
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None,
    syllable_parts: SyllablePartsInventory | None,
    time: int,
    reverse: bool,
) -> list[FeatureBundle]:
    """Scan and rewrite in place; each output is visible to later loci in the pass.

    Because the form mutates as it is rewritten, it is re-syllabified before each
    scan so the ``$`` assertion always reflects the current form.
    """
    form = list(segments)
    cursor = len(form) if reverse else 0
    while True:
        boundaries = _boundaries(form, sonorities, syllable_parts, time, letters)
        if reverse:
            candidates = [m for m in find_matches(sd, form, letters, boundaries) if m.end <= cursor]
            if not candidates:
                break
            # Rightmost, tie-broken to longest (min start) — the mirror of
            # leftmost-longest. (max end, then min start.)
            match = max(candidates, key=lambda m: (m.end, -m.start))
        else:
            candidates = [
                m for m in find_matches(sd, form, letters, boundaries) if m.start >= cursor
            ]
            if not candidates:
                break
            # Leftmost; the matcher already made it longest for that start.
            match = min(candidates, key=lambda m: m.start)

        replacement = apply_match(sd, match, form, letters, features)
        form[match.start : match.end] = replacement

        no_op = match.end == match.start and not replacement
        if reverse:
            # Advance leftward past the output's left edge; bump only a true no-op.
            cursor = match.start - 1 if no_op else match.start
        else:
            # Advance past the rewritten output; bump only a true no-op (a deletion
            # makes progress by shrinking the form, so it must not bump).
            cursor = match.start + 1 if no_op else match.start + len(replacement)
    return form


def _fired(before: list[FeatureBundle], after: list[FeatureBundle]) -> bool:
    """Whether the rule changed the form (a vacuous match is not a firing)."""
    if len(before) != len(after):
        return True
    return any(not matches_exactly(b, a) for b, a in zip(before, after, strict=True))


def derive(
    word: Word,
    segments: list[FeatureBundle],
    rules: RuleInventory,
    letters: LetterInventory,
    features: FeatureInventory,
    sonorities: SonoritiesInventory | None = None,
    syllable_parts: SyllablePartsInventory | None = None,
) -> Derivation:
    """Sweep *segments* through every rule in time order, recording firing steps.

    Each rule (re)syllabifies the current form for its match pass, so the input is
    syllabified before the first rule and the structure is refreshed after every
    rule — without ``sonorities``/``syllable_parts`` there are simply no
    boundaries and the ``$`` assertion never matches.

    Args:
        word: The word being derived (carried into the trace).
        segments: The starting form (already segmented).
        rules: Rules keyed by time; applied ascending by time, file order within.
        letters: Letter inventory, for shorthands and recalls.
        features: Feature inventory, for the geometry-aware merge.
        sonorities: Sonority scale for syllabification (optional).
        syllable_parts: Syllable-part constraints supplying the nucleus (optional).
    """
    input_form = list(segments)
    current = list(segments)
    steps: list[DerivationStep] = []

    for time in sorted(rules.keys()):
        for rule in rules[time]:
            before = list(current)
            after = apply_rule(rule, current, letters, features, sonorities, syllable_parts)
            if _fired(before, after):
                steps.append(
                    DerivationStep(
                        before=before,
                        rule=rule,
                        after=list(after),
                        before_boundaries=_display_boundaries(
                            before, sonorities, syllable_parts, rule.time, letters
                        ),
                        after_boundaries=_display_boundaries(
                            after, sonorities, syllable_parts, rule.time, letters
                        ),
                    )
                )
                current = after

    surface_boundaries = _display_boundaries(
        current, sonorities, syllable_parts, max(rules, default=0), letters
    )
    return Derivation(
        word=word,
        input=input_form,
        steps=tuple(steps),
        surface=current,
        surface_boundaries=surface_boundaries,
    )
