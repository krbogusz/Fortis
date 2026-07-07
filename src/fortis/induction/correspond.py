"""Residual correspondences, read from the *derived* side (plan §2.1).

Diagnosis's autopsy conditions on the **attested**-form environment — the right coordinate
for a human reading a report, and the wrong one for a rule proposer: an induced rule fires on
the *derived* form, so its context must hold there. This module is the derived-side variant.

For each confusion ``(expected=a, got=b)`` it splits the sites where the derivation produced
``b`` into a **should-change** class (``b`` where the target wanted ``a``) and a
**should-stay** class (``b`` where the target kept ``b``), then scores each derived-side
environment predictor — a neighbour's identity (``left=p``, ``right=#``) or one of its features
(``[+nasal]``) — by the phi coefficient over that 2×2, with the same support-floor logic as
``diagnosis``. The positive-phi predictors are the environments a corrective rule should
condition on. Words whose edit distance exceeds ``alignment_distance_cap`` are excluded from
the tallies (their alignments are unreliable); they still count in the loss.

Deferred to a later milestone (documented, not silently dropped): **self**-predictors
(``self:stress=primary``) — conditioning a change on the changed segment's *own* feature.
Stress and length ride inside the segment phone (the accuracy phones fold suprasegmentals onto
their anchor), so a v1 built on neighbour predictors gains little from them; they arrive with
the tier-aware proposer (plan §2.2 / M4).
"""
from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass, field

from src.fortis.analysis.accuracy import DistanceToTarget, align, segment_form, specified_features
from src.fortis.analysis.diagnosis import f_score, phi_coefficient
from src.fortis.induction.notation import render_feature_element
from src.fortis.models.project import Project

# Word-boundary sentinel used as the neighbour of an edge phone (matches diagnosis).
BOUNDARY = "#"

# A phone → its specified {feature: value} map (or None if it will not segment), memoised.
_FeatureMapCache = dict[str, dict[str, object] | None]

# One word ready for correspondence extraction: its distance to target with the split
# target/derived phones.
_Word = tuple[DistanceToTarget, list[str], list[str]]


def _feature_map(phone: str, project: Project, cache: _FeatureMapCache) -> dict[str, object] | None:
    """The specified features of a single phone, or ``None`` if it will not segment."""
    if phone not in cache:
        bundles = segment_form(phone, project)
        bundle = bundles[0] if bundles and len(bundles) == 1 else None
        cache[phone] = specified_features(bundle) if bundle is not None else None
    return cache[phone]


@dataclass(frozen=True)
class ContextPredictor:
    """One derived-side environment predictor's association with the should-change class.

    ``side`` is ``"left"`` or ``"right"``; ``element`` is the notation fragment it becomes in a
    rule context (a phone literal, ``#``, or a bracketed feature like ``[+nasal]``). The 2×2
    counts are over the correspondence's sites: ``change_here``/``stay_here`` with the predictor
    present, ``change_away``/``stay_away`` without it. ``phi`` > 0 means the predictor
    co-occurs with the site that needs changing.
    """

    side: str
    element: str
    phi: float
    fscore: float
    change_here: int
    stay_here: int
    change_away: int
    stay_away: int

    @property
    def support(self) -> int:
        """Sites in which the predictor is present."""
        return self.change_here + self.stay_here


@dataclass(frozen=True)
class Correspondence:
    """One residual correspondence with its ranked derived-side conditioning environments.

    ``expected`` is the target phone (``None`` for an insertion — a spurious derived phone with
    no target); ``got`` the derived phone (``None`` for a deletion — a target phone the
    derivation never produced). ``count`` is how often it occurs; ``delta`` the feature
    distance between the two phones (``None`` for an indel). ``predictors`` are the positive-phi
    environments, most associated first. ``examples`` are a few word labels.
    """

    expected: str | None
    got: str | None
    count: int
    delta: int | None
    predictors: tuple[ContextPredictor, ...] = ()
    examples: tuple[str, ...] = field(default_factory=tuple)
    feature_delta: tuple[tuple[str, object], ...] = ()
    got_features: tuple[tuple[str, object], ...] = ()

    @property
    def kind(self) -> str:
        """``"substitution"``, ``"deletion"``, or ``"insertion"``."""
        if self.expected is None:
            return "insertion"
        if self.got is None:
            return "deletion"
        return "substitution"

    @property
    def delta_key(self) -> tuple[tuple[str, object], ...]:
        """A hashable grouping key for tier-4 class targets: the structured feature delta.

        Two substitutions share a class rule only when they move the *same* features to the
        *same* values (``feature_delta``), so grouping is by this key — not by the ``delta``
        count, under which two unrelated changes could collide.
        """
        return self.feature_delta


def _gradeable(distances: tuple[DistanceToTarget, ...], distance_cap: int) -> list[_Word]:
    """Non-exact words within the distance cap, each with its split target/derived phones."""
    out: list[_Word] = []
    for dtt in distances:
        if dtt.exact or dtt.distance > distance_cap:
            continue
        out.append((dtt, list(dtt.target_phones), list(dtt.derived_phones)))
    return out


def _tally_confusions(
    words: list[_Word],
) -> tuple[Counter[tuple[str | None, str | None]], dict[tuple[str | None, str | None], list[str]]]:
    """Count every non-match alignment op by its (expected, got) pair, with a few examples."""
    counts: Counter[tuple[str | None, str | None]] = Counter()
    examples: dict[tuple[str | None, str | None], list[str]] = {}
    for dtt, target_phones, derived_phones in words:
        label = dtt.gloss or dtt.ipa
        for op in align(target_phones, derived_phones):
            if op.kind == "match":
                continue
            key = (op.target, op.derived)
            counts[key] += 1
            bucket = examples.setdefault(key, [])
            if label not in bucket and len(bucket) < 3:
                bucket.append(label)
    return counts, examples


def _neighbours(phones: list[str], index: int) -> tuple[str, str]:
    """The left and right neighbours of *index* in *phones*, ``#`` at an edge."""
    left = phones[index - 1] if index > 0 else BOUNDARY
    right = phones[index + 1] if index + 1 < len(phones) else BOUNDARY
    return left, right


def _predictors_at(
    left: str, right: str, project: Project, cache: _FeatureMapCache
) -> set[tuple[str, str]]:
    """The (side, element) predictors for a site with derived neighbours *left*/*right*.

    A boundary edge contributes ``#``; a neighbour that segments contributes its identity
    literal plus one bracketed single-feature element per specified feature. A neighbour that
    will *not* segment as a lone literal contributes nothing — an unsegmentable phone cannot be
    a rule literal, so conditioning on it would only produce candidates the resolver rejects.
    """
    predictors: set[tuple[str, str]] = set()
    for side, phone in (("left", left), ("right", right)):
        if phone == BOUNDARY:
            predictors.add((side, BOUNDARY))
            continue
        features = _feature_map(phone, project, cache)
        if features is None:
            continue
        predictors.add((side, phone))  # identity literal (segmentable)
        for feature, value in features.items():
            element = render_feature_element(feature, value, project.features)
            if element is not None:
                predictors.add((side, element))
    return predictors


def _rank_predictors(
    change_with: Counter[tuple[str, str]],
    stay_with: Counter[tuple[str, str]],
    changes: int,
    stays: int,
    project: Project,
) -> tuple[ContextPredictor, ...]:
    """Score each predictor by phi over (present/absent) × (should-change/should-stay).

    Mirrors ``diagnosis.error_contexts``' support floor: a predictor must be present in at
    least ``max(min_support, ceil(min_support_percent% of all sites))`` sites. Only
    positive-phi predictors are returned, most associated first.
    """
    total = changes + stays
    settings = project.settings.diagnosis
    floor = max(settings.min_support, math.ceil(settings.min_support_percent * total / 100))
    ranked: list[ContextPredictor] = []
    for key in change_with.keys() | stay_with.keys():
        change_here = change_with[key]
        stay_here = stay_with[key]
        if change_here + stay_here < floor:
            continue
        side, element = key
        phi = phi_coefficient(change_here, stay_here, changes - change_here, stays - stay_here)
        if phi <= 0:
            continue
        ranked.append(
            ContextPredictor(
                side=side,
                element=element,
                phi=phi,
                fscore=f_score(change_here, stay_here, changes - change_here),
                change_here=change_here,
                stay_here=stay_here,
                change_away=changes - change_here,
                stay_away=stays - stay_here,
            )
        )
    ranked.sort(key=lambda p: (-p.phi, -p.change_here, p.side, p.element))
    return tuple(ranked)


def _substitution_predictors(
    words: list[_Word],
    expected: str,
    got: str,
    project: Project,
    cache: _FeatureMapCache,
) -> tuple[ContextPredictor, ...]:
    """Rank derived-side predictors for a substitution correspondence ``got→expected``.

    A **should-change** site is a derived ``got`` the target wanted as ``expected``; a
    **should-stay** site is a derived ``got`` the target kept. Both anchor on the real derived
    phone ``got``.
    """
    change_with: Counter[tuple[str, str]] = Counter()
    stay_with: Counter[tuple[str, str]] = Counter()
    changes = stays = 0
    for _measure, target_phones, derived_phones in words:
        for op in align(target_phones, derived_phones):
            if op.derived != got or op.derived_index is None:
                continue
            if op.target == expected and op.kind != "match":
                changes += 1
                bucket = change_with
            elif op.kind == "match":  # got kept as got — a should-stay site
                stays += 1
                bucket = stay_with
            else:
                continue
            left, right = _neighbours(derived_phones, op.derived_index)
            for predictor in _predictors_at(left, right, project, cache):
                bucket[predictor] += 1
    return _rank_predictors(change_with, stay_with, changes, stays, project)


def _deletion_predictors(
    words: list[_Word],
    expected: str,
    project: Project,
    cache: _FeatureMapCache,
) -> tuple[ContextPredictor, ...]:
    """Rank the derived-side gap neighbours at deletion sites (a target ``expected`` never made).

    A deletion has no derived phone to anchor on, so the environment is read from the gap: the
    derived phones flanking where ``expected`` should have been inserted. There is no clean
    should-stay population (every non-deletion position is a candidate), so this uses a lighter
    signal than phi — the frequency of each flanking predictor among the deletion sites — and
    the proposer treats these as context *suggestions*, gated afterwards by the actual ΔL.
    """
    left_counts: Counter[str] = Counter()
    right_counts: Counter[str] = Counter()
    sites = 0
    for _measure, target_phones, derived_phones in words:
        derived_pos = 0  # how many derived phones consumed so far (the gap's left index)
        for op in align(target_phones, derived_phones):
            if op.kind == "delete" and op.target == expected:
                sites += 1
                left = derived_phones[derived_pos - 1] if derived_pos > 0 else BOUNDARY
                after = derived_pos < len(derived_phones)
                right = derived_phones[derived_pos] if after else BOUNDARY
                left_counts[left] += 1
                right_counts[right] += 1
            if op.derived_index is not None:
                derived_pos = op.derived_index + 1
    predictors: list[ContextPredictor] = []
    for side, counts in (("left", left_counts), ("right", right_counts)):
        for element, count in counts.most_common():
            predictors.append(
                ContextPredictor(
                    side=side, element=element, phi=count / sites if sites else 0.0,
                    fscore=0.0, change_here=count, stay_here=0,
                    change_away=sites - count, stay_away=0,
                )
            )
    return tuple(predictors)


def correspondences(
    distances: tuple[DistanceToTarget, ...], project: Project, cap: int
) -> list[Correspondence]:
    """The top *cap* residual correspondences, each with its derived-side predictors.

    Confusions are tallied over the words within ``alignment_distance_cap`` (unreliable
    alignments are excluded), ranked by count, and the top *cap* are expanded with derived-side
    conditioning environments. A substitution/insertion anchors its predictors on the real
    derived phone; a deletion reads them from the derived gap.
    """
    distance_cap = project.settings.induction.alignment_distance_cap
    words = _gradeable(distances, distance_cap)
    counts, examples = _tally_confusions(words)
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], str(kv[0][0]), str(kv[0][1])))
    cache: _FeatureMapCache = {}
    result: list[Correspondence] = []
    for (expected, got), count in ordered[:cap]:
        delta = _delta(expected, got, project, cache)
        feature_delta: tuple[tuple[str, object], ...] = ()
        got_features: tuple[tuple[str, object], ...] = ()
        if got is None:  # deletion — a target phone the derivation never produced
            predictors = _deletion_predictors(words, expected, project, cache)  # type: ignore[arg-type]
        elif expected is None:  # insertion — a spurious derived phone
            predictors = _insertion_predictors(words, got, project, cache)
        else:  # substitution
            predictors = _substitution_predictors(words, expected, got, project, cache)
            feature_delta = _feature_delta(expected, got, project, cache)
            got_map = _feature_map(got, project, cache)
            got_features = tuple(sorted(got_map.items())) if got_map is not None else ()
        result.append(
            Correspondence(
                expected=expected, got=got, count=count, delta=delta,
                predictors=predictors, examples=tuple(examples[(expected, got)]),
                feature_delta=feature_delta, got_features=got_features,
            )
        )
    return result


def _insertion_predictors(
    words: list[_Word],
    got: str,
    project: Project,
    cache: _FeatureMapCache,
) -> tuple[ContextPredictor, ...]:
    """Rank derived-side predictors for an insertion correspondence ``got→∅`` (delete spurious).

    A **should-change** site is a spurious ``got`` (an insertion op); a **should-stay** site is a
    ``got`` the target kept. Both anchor on the real derived ``got``.
    """
    change_with: Counter[tuple[str, str]] = Counter()
    stay_with: Counter[tuple[str, str]] = Counter()
    changes = stays = 0
    for _measure, target_phones, derived_phones in words:
        for op in align(target_phones, derived_phones):
            if op.derived != got or op.derived_index is None:
                continue
            if op.kind == "insert":
                changes += 1
                bucket = change_with
            elif op.kind == "match":
                stays += 1
                bucket = stay_with
            else:
                continue
            left, right = _neighbours(derived_phones, op.derived_index)
            for predictor in _predictors_at(left, right, project, cache):
                bucket[predictor] += 1
    return _rank_predictors(change_with, stay_with, changes, stays, project)


def _delta(
    expected: str | None, got: str | None, project: Project, cache: _FeatureMapCache
) -> int | None:
    """Feature distance between the two phones of a substitution, or ``None`` for an indel."""
    if expected is None or got is None:
        return None
    a, b = _feature_map(expected, project, cache), _feature_map(got, project, cache)
    if a is None or b is None:
        return None
    keys = a.keys() | b.keys()
    sentinel = object()
    return sum(a.get(k, sentinel) != b.get(k, sentinel) for k in keys)


def _feature_delta(
    expected: str, got: str, project: Project, cache: _FeatureMapCache
) -> tuple[tuple[str, object], ...]:
    """The structured change ``got → expected``: the specified features expected sets differently.

    Each pair ``(feature, expected_value)`` names a feature whose value in ``expected`` differs
    from (or is absent in) ``got`` — the merge bundle a class rule would write. Features
    ``got`` has that ``expected`` lacks are *not* included (v1 class rules add/change, they do
    not unlink), so this is the additive core of the delta. Empty when either phone will not
    segment (no class grouping possible).
    """
    a, b = _feature_map(expected, project, cache), _feature_map(got, project, cache)
    if a is None or b is None:
        return ()
    sentinel = object()
    pairs = [(feature, value) for feature, value in a.items() if b.get(feature, sentinel) != value]
    return tuple(sorted(pairs, key=lambda kv: kv[0]))
