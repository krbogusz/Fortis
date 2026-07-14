"""Measure derived surface forms' distance to the lexicon's target annotations.

The engine derives a surface form from each word's IPA; a word may also carry an
attested target in ``Word.final`` (a *target* annotation, native to ``words.toml``).
This module measures the distance between the two — per word and in aggregate —
so a rule set's accuracy can be tracked as it is developed.

Both the derived surface and the attested target are segmented **against the project
inventory** — the target ingested once at load (:func:`ingest_targets`, stored on
``Word.final_form``/``stage_forms``), the derived surface re-segmented from its rendered
string. So the unit of comparison is one *inventory segment*: an affricate ``d͡ʒ`` or a
tie-barred ``k͡p`` is one phone, not several codepoints. Suprasegmentals (tone, stress) are
folded onto their anchor segment (``lower_tiers``) and compared there, which makes the
comparison placement-invariant — ``ˈkon`` and ``kˈon`` both read as ``['k', 'ˈo', 'n']``.

Two distances per word, off the *same* segments (so a feature distance of 0 coincides
exactly with a phone distance of 0):

- **Phone distance** (headline; distance 0 = exact) — the Damerau–Levenshtein distance
  over the per-segment phones (:func:`form_phones`).
- **Feature distance** — a feature-weighted edit distance over the same bundles: a
  substitution costs the number of features that differ, so ``ɑ̃`` is one edit from ``ɑ``
  (nasal) but eleven from ``t`` — the finer diagnostic a phone distance flattens to 1.

Both count an adjacent-segment swap (a metathesis) as one edit. A target that uses a symbol
the inventory cannot segment is skipped (warned at ingestion).
"""

from __future__ import annotations

import warnings
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from src.fortis.application.deriving import form_at_time
from src.fortis.application.rendering import render_segment, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import FeatureBundle, is_morpheme_boundary
from src.fortis.models.derivation import Derivation
from src.fortis.models.form import Form
from src.fortis.models.project import Project

# Dropped when segmenting a rendered string for comparison — structural, not segmental:
# syllable dots, morpheme boundaries, whitespace, and stress marks ``ˈ``/``ˌ`` (a stress mark's
# rendered position is a syllabification convention, so it is stripped from the string and the
# stress feature is instead read off the segment it anchors to — see :func:`form_phones`).
_IGNORED = frozenset(".-ˈˌ")


def edit_distance(a: Sequence[str], b: Sequence[str], transposition_cost: int = 1) -> int:
    """The Damerau–Levenshtein distance between two phone sequences (unit costs).

    Insert/delete/substitute each cost 1; swapping two *adjacent* phones costs
    ``transposition_cost`` (default 1), so a metathesis reads as one edit rather
    than two substitutions. This is the restricted (optimal string alignment)
    variant: a phone participates in at most one transposition.
    """
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i
    for j in range(1, m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(
                d[i - 1][j] + 1,  # deletion
                d[i][j - 1] + 1,  # insertion
                d[i - 1][j - 1] + (a[i - 1] != b[j - 1]),  # match/substitution
            )
            # Fires on any exact adjacent reversal in the optimal alignment — not
            # necessarily a linguistic metathesis; a future op-trace must not label it one.
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + transposition_cost)  # transposition
    return d[n][m]


def comparable_bundles(form: Form) -> list[FeatureBundle]:
    """The form's segments as flat bundles for comparison.

    Suprasegmentals folded onto their anchor by :func:`lower_tiers`, morpheme
    boundaries dropped (structural, not segmental).
    """
    return [bundle for bundle in lower_tiers(form) if not is_morpheme_boundary(bundle)]


def form_phones(form: Form, project: Project) -> list[str]:
    """A form's phones as *inventory segments* — one phone per segment, suprasegmentals kept.

    Each segment renders through :func:`render_segment` *with* the tone/stress features
    :func:`lower_tiers` folded onto it, so — unlike the string codepoint heuristic — a
    multi-codepoint segment (an affricate ``d͡ʒ``, a tie-barred ``k͡p``) is *one* phone, and
    stress/tone is compared on the segment it anchors to rather than dropped. Anchoring makes
    the comparison placement-invariant: ``ˈkon`` and ``kˈon`` both yield ``['k', 'ˈo', 'n']``.
    This is the phone unit the error analyses and the confusion matrix *label* with. It is not
    what the DISTANCES compare — see :func:`phone_keys`.
    """
    return [render_segment(bundle, project) for bundle in comparable_bundles(form)]


def phone_keys(form: Form, project: Project) -> list[frozenset[tuple[str, object]]]:
    """A form's phones as BUNDLE identities — what the distances actually compare.

    One key per segment, in order, exactly parallel to :func:`form_phones`. Two phones are the
    same iff their feature bundles are the same, so the phone distance and the feature distance
    are answering the same question about the same segments and ``phone-0 ⟺ feature-0`` holds
    *by construction* rather than by coincidence.

    It very nearly held on the rendered strings, because rendering is injective: across every
    shipped project, no two distinct bundles share a label. The exception is ``�`` — the symbol
    for a segment no letter can express (see analysis/warnings.py). Every unspellable segment
    renders as the same ``�``, so compared as strings two *different* broken segments count as
    the same phone and the distance understates. Compared as bundles they do not. The label
    stays a label; identity is the bundle's business.
    """
    return [
        frozenset((feature, spec.value) for feature, spec in bundle.items())
        for bundle in comparable_bundles(form)
    ]


def try_segment(string: str, project: Project) -> Form | None:
    """Segment a raw IPA string into a :class:`Form`, or ``None`` if a symbol is unknown.

    Segments the string as written (stress/dots kept, carried on the syllable tier), so the
    ingested attested form keeps its full autosegmental structure; ``None`` when the inventory
    cannot segment some letter/diacritic.
    """
    try:
        return string_to_sequence(string, project)
    except ValueError:
        return None


def ingest_targets(derivations: Iterable[Derivation], project: Project) -> None:
    """Segment each derived word's attested ``final``/``stages`` against the inventory, in place.

    Populates ``Word.final_form``/``stage_forms`` with the segmented :class:`Form` — the
    *ingested* record the accuracy and error analyses compare against (so a segment is one
    inventory unit). An attested form that uses a symbol the inventory cannot segment is left
    unset and a warning is issued; the analyses then skip that one form (a word with a bad
    ``final`` but clean ``stages`` still counts at its stages, and vice versa).

    Operates on the ``Word`` each derivation references — the objects the analysis actually
    reads — so it is correct whether derivation ran serially (the ``project.words`` objects) or
    across worker processes (unpickled copies). Run once, in the main process, after deriving
    and before any analysis; never inside the parallel fan-out (workers derive from ``ipa`` and
    never touch the attested forms).
    """
    for derivation in derivations:
        _ingest_word(derivation.word, project)


def ingest_words(project: Project) -> None:
    """Ingest every word's attested forms on ``project.words`` (see :func:`ingest_targets`).

    For serial callers whose derivations share the ``project.words`` objects (the induction
    loop re-derives ``replace(project, rules=…)``, which keeps the same words) — one call and
    every later derivation sees the ingested forms. The engine CLIs instead ingest the
    *derivations'* words, because the parallel path returns unpickled copies.
    """
    for word in project.words.values():
        _ingest_word(word, project)


def _ingest_word(word, project: Project) -> None:
    """Segment every TARGET in place, onto its own ``Attestation.form``.

    The seed is skipped: it is the derivation's input, not something the derivation is scored
    against, and it is segmented on the way in by the engine itself.
    """
    who = word.gloss or word.ipa
    for time, attestation in word.targets.items():
        attestation.form = try_segment(attestation.ipa, project)
        if attestation.form is None:
            where = "final" if time is None else f"stage {time}"
            warnings.warn(
                f"attested {where} form {attestation.ipa!r} for {who!r} uses a symbol not in "
                "the inventory — skipped from the accuracy and error analyses",
                stacklevel=2,
            )


@dataclass(frozen=True)
class AlignOp:
    """One step in a target→derived alignment, for error diagnosis.

    ``kind`` is ``"match"`` (target phone reproduced), ``"sub"`` (a different phone
    produced), ``"delete"`` (target phone with no derived counterpart), or
    ``"insert"`` (a spurious derived phone with no target counterpart). ``target``
    and ``derived`` hold the phones (``None`` on the side that is absent).
    ``target_index``/``derived_index`` are the phone's positions in the target and
    derived sequences — each ``None`` on the side that is absent (``target_index`` for
    an insertion, ``derived_index`` for a deletion).
    """

    kind: str
    target: str | None
    derived: str | None
    target_index: int | None
    derived_index: int | None = None


def align(target: Sequence[str], derived: Sequence[str]) -> list[AlignOp]:
    """Align a target phone sequence to a derived one, returning the edit ops.

    A plain Levenshtein alignment (unit insert/delete/substitute costs) with a
    *deterministic* traceback: on a tie the diagonal (match/substitution) is taken
    before a deletion, and a deletion before an insertion. Substitution-on-the-
    diagonal is preferred so a mismatch reads as one ``x→y`` confusion rather than a
    delete-plus-insert pair — the reproducible policy the confusion tally depends on.

    Unlike :func:`edit_distance` this carries no transposition discount, so a
    metathesis reads here as an *adjacent pair of substitutions* (``x→y`` then
    ``y→x``), not one reordering. Diagnosis wants the phone-for-phone confusions;
    the transposition-aware distance stays the headline metric.
    """
    a, b = list(target), list(derived)
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i
    for j in range(1, m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(
                d[i - 1][j - 1] + (a[i - 1] != b[j - 1]),  # match/substitution
                d[i - 1][j] + 1,  # deletion
                d[i][j - 1] + 1,  # insertion
            )
    ops: list[AlignOp] = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and d[i][j] == d[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            kind = "match" if a[i - 1] == b[j - 1] else "sub"
            ops.append(AlignOp(kind, a[i - 1], b[j - 1], i - 1, j - 1))
            i, j = i - 1, j - 1
        elif i > 0 and d[i][j] == d[i - 1][j] + 1:
            ops.append(AlignOp("delete", a[i - 1], None, i - 1, None))
            i -= 1
        else:
            ops.append(AlignOp("insert", None, b[j - 1], None, j - 1))
            j -= 1
    ops.reverse()
    return ops


# Sentinel for a feature absent from a bundle, distinct from any real value so
# that present-vs-absent reads as a difference.
_ABSENT = object()


def specified_features(bundle: FeatureBundle) -> dict[str, object]:
    """The bundle's features that carry a value, as ``{feature: value}``.

    Public so the induction bits model can price a phone by its specified-feature
    count (:mod:`src.fortis.induction.objective`).
    """
    return {feature: spec.value for feature, spec in bundle.items() if spec.value is not None}


def feature_diff(a: FeatureBundle, b: FeatureBundle) -> int:
    """Number of features on which two segments disagree.

    A feature present on one segment and absent on the other counts as one
    difference, as does a feature present on both with different values. So
    ``ɑ̃`` and ``ɑ`` differ by one (nasal), ``ɑ̃`` and ``t`` by many.
    """
    left, right = specified_features(a), specified_features(b)
    return sum(left.get(f, _ABSENT) != right.get(f, _ABSENT) for f in left.keys() | right.keys())


def feature_edit_distance(
    a: Sequence[FeatureBundle], b: Sequence[FeatureBundle], transposition_cost: int = 1
) -> int:
    """Feature-weighted Damerau–Levenshtein over two segment sequences.

    Substituting one segment for another costs :func:`feature_diff`; inserting or
    deleting a segment costs its own feature count — its distance from nothing,
    ``feature_diff(x, ∅)``. Because a segment shares some features with any other
    (both are ``[consonantal …]``), a substitution never costs more than the
    delete-plus-insert alternative, so segments align by feature similarity and
    an indel falls out only on a genuine length mismatch.

    Swapping two *adjacent* segments costs ``transposition_cost`` (default 1) —
    but only when the swapped pair is featurally identical (each
    :func:`feature_diff` is 0), i.e. a true metathesis that reorders segments
    without changing any features. That one reordering event would otherwise be
    charged as two substitutions (up to ``2 × feature_diff``). This is the
    restricted (optimal string alignment) variant.
    """
    n, m = len(a), len(b)
    a_sizes = [len(specified_features(bundle)) for bundle in a]
    b_sizes = [len(specified_features(bundle)) for bundle in b]
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = d[i - 1][0] + a_sizes[i - 1]
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + b_sizes[j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(
                d[i - 1][j] + a_sizes[i - 1],  # delete a[i-1]
                d[i][j - 1] + b_sizes[j - 1],  # insert b[j-1]
                d[i - 1][j - 1] + feature_diff(a[i - 1], b[j - 1]),  # substitute
            )
            # Fires on any exact adjacent reversal in the optimal alignment — not
            # necessarily a linguistic metathesis; a future op-trace must not label it one.
            if (
                i > 1
                and j > 1
                and feature_diff(a[i - 1], b[j - 2]) == 0
                and feature_diff(a[i - 2], b[j - 1]) == 0
            ):
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + transposition_cost)  # transposition
    return d[n][m]


def segment_form(form: str, project: Project) -> list[FeatureBundle] | None:
    """Segment a rendered string into feature bundles, or ``None`` if a symbol is unknown.

    Syllable dots, morpheme boundaries, whitespace, and stress marks are stripped first, then
    the rest is segmented against the inventory and its tiers lowered. Used where a *string* is
    all a caller has — the induction bits model featurising a phone. (The accuracy/error
    comparison works from ``Form``s and
    :func:`form_phones`/:func:`comparable_bundles` instead, keeping suprasegmentals.)
    """
    cleaned = "".join(char for char in form if char not in _IGNORED and not char.isspace())
    try:
        return lower_tiers(string_to_sequence(cleaned, project))
    except ValueError:
        return None


@dataclass(frozen=True)
class DistanceToTarget:
    """One word assessed: its derived surface against the attested target form.

    ``derived`` and ``target`` are kept as rendered (dots and all) for display.
    ``distance`` is the phone edit distance (the headline). ``feature_distance``
    is the finer feature-weighted distance, or ``None`` when a form could not be
    segmented into features. ``derived_phones``/``target_phones`` are the *inventory*
    segments (:func:`form_phones`) the distance and the error diagnosis align on — one
    entry per segment, so an affricate is one phone.

    ``matches_at``/``closest_at`` look *across the word's other attested targets* at the
    same ``derived`` form: ``matches_at`` lists every attested stage whose target this
    derived form reproduces exactly (feature distance 0), comma-joined; ``closest_at`` is the
    single attested stage whose target this derived form is closest to by feature distance.
    Both hold ``derived`` fixed and scan the targets (:func:`_cross_time_columns`), so a row
    whose derived form equals a *different* stage's attested target names that stage here. The
    current row's own stage is a candidate too — it appears in ``matches_at`` when ``distance``
    is 0 and can be ``closest_at`` when it is the closest.
    """

    gloss: str
    ipa: str
    derived: str
    target: str
    distance: int
    feature_distance: int | None = None
    frequency: int = 1
    derived_phones: tuple[str, ...] = ()
    target_phones: tuple[str, ...] = ()
    matches_at: str = ""
    closest_at: str = ""

    @property
    def exact(self) -> bool:
        """Whether the derived form matches the target exactly (distance 0)."""
        return self.distance == 0


@dataclass(frozen=True)
class AccuracyReport:
    """A set of per-word distances to target with the aggregate accuracy statistics.

    ``assessed`` is the denominator throughout: words that carry a target ``final``.
    ``skipped`` counts words with no target to compare against.
    """

    distances: tuple[DistanceToTarget, ...]
    skipped: int = 0

    @property
    def assessed(self) -> int:
        """Number of words assessed (those with a target ``final``)."""
        return len(self.distances)

    @property
    def exact(self) -> int:
        """Number of words derived exactly (distance 0)."""
        return sum(dtt.exact for dtt in self.distances)

    @property
    def within_one(self) -> int:
        """Number of words within one phone of the target (distance ≤ 1)."""
        return sum(dtt.distance <= 1 for dtt in self.distances)

    @property
    def total_distance(self) -> int:
        """Summed phone edit distance across all assessed words."""
        return sum(dtt.distance for dtt in self.distances)

    @property
    def accuracy(self) -> float:
        """Fraction derived exactly, ``exact / assessed`` (0.0 if none assessed)."""
        return self.exact / self.assessed if self.distances else 0.0

    @property
    def mean_distance(self) -> float:
        """Mean phone edit distance per assessed word (0.0 if none assessed)."""
        return self.total_distance / self.assessed if self.distances else 0.0

    @property
    def feature_assessed(self) -> int:
        """Number of assessed words that also have a feature distance."""
        return sum(dtt.feature_distance is not None for dtt in self.distances)

    @property
    def unsegmentable(self) -> int:
        """Assessed words whose forms could not be segmented (no feature distance)."""
        return sum(dtt.feature_distance is None for dtt in self.distances)

    @property
    def total_feature_distance(self) -> int:
        """Summed feature edit distance across words that have one."""
        return sum(g.feature_distance for g in self.distances if g.feature_distance is not None)

    @property
    def mean_feature_distance(self) -> float:
        """Mean feature edit distance per word that has one (0.0 if none)."""
        return self.total_feature_distance / self.feature_assessed if self.feature_assessed else 0.0

    # ---- Token-frequency-weighted aggregates (each word counts ``frequency`` times) ----

    @property
    def frequencies_vary(self) -> bool:
        """Whether any assessed word carries a non-default frequency (else weighting is a no-op)."""
        return any(dtt.frequency != 1 for dtt in self.distances)

    @property
    def weight(self) -> int:
        """Total token weight across assessed words (the weighted denominator)."""
        return sum(dtt.frequency for dtt in self.distances)

    @property
    def weighted_accuracy(self) -> float:
        """Token-weighted exact-match fraction (0.0 if no weight)."""
        exact = sum(dtt.frequency for dtt in self.distances if dtt.exact)
        return exact / self.weight if self.weight else 0.0

    @property
    def weighted_mean_distance(self) -> float:
        """Token-weighted mean phone distance (0.0 if no weight)."""
        total = sum(dtt.frequency * dtt.distance for dtt in self.distances)
        return total / self.weight if self.weight else 0.0

    @property
    def weighted_mean_feature_distance(self) -> float:
        """Token-weighted mean feature distance over words that have one (0.0 if none)."""
        weighted = [
            (g.frequency, g.feature_distance)
            for g in self.distances
            if g.feature_distance is not None
        ]
        weight = sum(freq for freq, _ in weighted)
        return sum(freq * fd for freq, fd in weighted) / weight if weight else 0.0


def distance_to_target(derivation: Derivation, project: Project) -> DistanceToTarget | None:
    """Measure one derivation's distance to its word's ingested target ``final_form``.

    Returns ``None`` when the word carries no target (``final_form`` unset) — whether it had
    no ``final`` at all or one the inventory could not segment (warned at ingestion, then
    skipped). Assumes :func:`ingest_targets` has run.
    """
    word = derivation.word
    if word.final is None or word.final_form is None:
        return None  # no target at all, or one the inventory could not segment
    derived_str = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    # The surface's own bundles ARE the derived form. No string round-trip: the analysis is
    # bundle-based on both sides — the target ingested once into a Form, the derived taken
    # straight off the derivation — and text appears only where it belongs, in the report.
    #
    # This used to render the surface to a string and segment it back, which looked defensive and
    # was in fact two bugs holding hands. It could not survive a `�` (a segment no letter can
    # express): `try_segment` rightly refused it, this returned None, and the word dropped out of
    # `assessed` altogether — quietly INFLATING the exact-match percentage, which is the very
    # thing `�` exists to stop. And it silently laundered a bug in the other direction:
    # `string_to_sequence` was DROPPING the stress of any syllable whose first vowel a diacritic
    # makes non-syllabic (`ˈɲe̯aws`), so re-segmenting broke the derived form in exactly the way
    # ingestion had already broken the target, and the two agreed by both being wrong.
    # With that fixed at the source, removing this is a no-op — proven byte-identical.
    derived_form = derivation.surface
    matches_at, closest_at = _cross_time_columns(derived_form, word, project)
    return _measure(
        word.gloss,
        word.ipa,
        derived_str,
        word.final,
        derived_form,
        word.final_form,
        project,
        frequency=word.frequency,
        matches_at=matches_at,
        closest_at=closest_at,
    )


def _cross_time_columns(derived_form: Form, word, project: Project) -> tuple[str, str]:
    """The ``matches at`` / ``closest at`` labels for *derived_form* across the word's targets.

    Holds *derived_form* fixed and scans it against every one of the word's ingested attested
    forms — each :class:`StageAccuracy` time in ``word.stage_forms`` (label ``str(time)``),
    in ascending time order, then ``word.final_form`` (label ``"final"``) if present. For each
    target the feature edit distance to *derived_form* is computed; ``matches_at`` collects
    every label at distance 0 (comma-joined, in scan order — the current row's own stage
    appears when the row is itself an exact match), and ``closest_at`` is the label of the
    minimum (ties broken by scan order, so the earliest stage wins and ``final`` only when it
    is strictly closer than every stage). Returns ``("", "")`` when the word has no attested
    target at all.
    """
    swap = project.settings.accuracy.transposition_cost
    derived = comparable_bundles(derived_form)
    # Chronological: stages ascending, then the final surface last.
    targets: list[tuple[str, list[FeatureBundle]]] = [
        (str(time), comparable_bundles(word.stage_forms[time]))
        for time in sorted(word.stage_forms)
    ]
    if word.final_form is not None:
        targets.append(("final", comparable_bundles(word.final_form)))

    matches: list[str] = []
    best_label, best_fd = "", None
    for label, target in targets:
        fd = feature_edit_distance(derived, target, swap)
        if fd == 0:
            matches.append(label)
        if best_fd is None or fd < best_fd:  # strict <: first-seen wins a tie
            best_fd, best_label = fd, label
    return ",".join(matches), best_label


def _measure(
    gloss: str,
    ipa: str,
    derived_str: str,
    target_str: str | None,
    derived_form: Form,
    target_form: Form,
    project: Project,
    frequency: int = 1,
    matches_at: str = "",
    closest_at: str = "",
) -> DistanceToTarget:
    """Build a :class:`DistanceToTarget` by comparing two segmented forms.

    Both the phone distance and the feature distance come off the *same* segments
    (:func:`comparable_bundles`) and compare them the same way — by BUNDLE (:func:`phone_keys`),
    not by rendered label — so phone-0 ⟺ feature-0 holds by construction. The phones are
    inventory segments, so an affricate is one unit and stress/tone is compared on its anchor.
    ``derived_str``/``target_str`` and the ``*_phones`` labels are kept only for display.
    ``matches_at``/``closest_at`` are the cross-target scan results for *derived_form* against
    the word's other attested forms (:func:`_cross_time_columns`), carried through unchanged.
    """
    swap = project.settings.accuracy.transposition_cost
    derived_phones = form_phones(derived_form, project)   # labels, for display
    target_phones = form_phones(target_form, project)
    return DistanceToTarget(
        gloss=gloss,
        ipa=ipa,
        derived=derived_str,
        target=target_str or "",
        # On BUNDLE keys, not the labels: two segments are the same phone iff their bundles are.
        distance=edit_distance(
            phone_keys(derived_form, project), phone_keys(target_form, project), swap
        ),
        feature_distance=feature_edit_distance(
            comparable_bundles(derived_form), comparable_bundles(target_form), swap
        ),
        frequency=frequency,
        derived_phones=tuple(derived_phones),
        target_phones=tuple(target_phones),
        matches_at=matches_at,
        closest_at=closest_at,
    )


def measure_accuracy(derivations: Iterable[Derivation], project: Project) -> AccuracyReport:
    """Measure every derivation that has a target ``final``, in input order."""
    distances: list[DistanceToTarget] = []
    skipped = 0
    for derivation in derivations:
        result = distance_to_target(derivation, project)
        if result is None:
            skipped += 1
        else:
            distances.append(result)
    return AccuracyReport(distances=tuple(distances), skipped=skipped)


@dataclass(frozen=True)
class StageAccuracy:
    """An :class:`AccuracyReport` for one measurement step — an intermediate stage or the final.

    ``time`` is the stage time (``None`` for the final surface). ``label`` names
    the step in a report (the time as a string, or ``"final"``).
    """

    label: str
    time: int | None
    report: AccuracyReport


def accuracy_by_stage(derivations: Iterable[Derivation], project: Project) -> list[StageAccuracy]:
    """Measure each attested stage form, then the final, across the lexicon.

    For every stage time present in any word's ``Word.stages``, the derived
    snapshot *as of that rule-time* (see :func:`form_at_time`) is assessed against
    the attested stage form — over just the words that carry a form for that
    stage. A trailing ``final`` step distances the surface against ``Word.final``.

    Note that a stage's derived form is taken at the matching *rule-time*; this is
    only meaningful if the rule times are calibrated to whatever timescale the
    attested stages use. The ``final`` step does not depend on that alignment.
    """
    derivations = list(derivations)
    stage_times = sorted({time for d in derivations for time in d.word.stages})
    stages: list[StageAccuracy] = []
    for time in stage_times:
        distances: list[DistanceToTarget] = []
        for derivation in derivations:
            target_form = derivation.word.stage_forms.get(time)
            if target_form is None:  # no attested form for this stage, or unsegmentable
                continue
            form, boundaries = form_at_time(derivation, time)
            derived_str = render_syllabified(lower_tiers(form), boundaries, project)
            # The form at this time, as bundles (see `distance_to_target`). This one used to
            # `continue` when the re-segmentation failed, which bit harder: a word the engine got
            # so wrong it could not even spell simply LEFT the stage it was wrong at, and that
            # stage's percentage went up. The denominator must not move.
            derived_form = form
            matches_at, closest_at = _cross_time_columns(derived_form, derivation.word, project)
            distances.append(
                _measure(
                    derivation.word.gloss,
                    derivation.word.ipa,
                    derived_str,
                    derivation.word.stages[time],
                    derived_form,
                    target_form,
                    project,
                    frequency=derivation.word.frequency,
                    matches_at=matches_at,
                    closest_at=closest_at,
                )
            )
        stages.append(StageAccuracy(str(time), time, AccuracyReport(tuple(distances))))
    stages.append(StageAccuracy("final", None, measure_accuracy(derivations, project)))
    return stages
