"""Diagnose *where* a rule set goes wrong, not just *how much*.

The accuracy analysis (:mod:`src.fortis.analysis.accuracy`) scores each derived form
against its attested target. This module reads the same assessed forms but asks the
follow-up question — *what is going wrong, and in what environment* — so a score becomes
a lead on the next rule to fix. It powers two per-stage analyses (``errors.csv`` and
``error_context.csv``), both built on the target→derived alignment in
:func:`src.fortis.analysis.accuracy.align`:

- **Errors** (confusions) — a ranked tally of the phone mismatches at each attested
  stage: which target phone was reproduced as which other phone (or dropped, or a
  spurious phone inserted). Answers "which segments am I getting wrong, and how often".

- **Context autopsy** — for one *focus* target phone, the attested-form environments most
  associated with getting that phone wrong, scored by the phi coefficient. Answers
  "when I get /e/ wrong, what conditions it".

The autopsy is deliberately **conditioned on a focus phone**. A global "does this
context predict any error" correlation is confounded by phone difficulty: if /e/ is
hard and happens to precede /r/, then "next=/r/" lights up as error-predicting when it
is really a proxy for the focus phone. Conditioning on the focus phone — comparing the
/e/ that came out right against the /e/ that came out wrong — removes that confound and
matches how a linguist actually debugs a cascade.

Two caveats the reports repeat:

- The environment is read from the **attested** form, a proxy: the derived form's
  environment may differ (and that difference is often the very cause). It is the
  stable coordinate to condition on, not a claim about the derivation's own context.
- Because the alignment carries no transposition discount, a metathesis reads as an
  adjacent pair of substitutions, not one reordering.
"""
from __future__ import annotations

import csv
import io
import math
from collections import Counter
from dataclasses import dataclass, field

from src.fortis.analysis.accuracy import DistanceToTarget, accuracy_by_stage, align
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project

# The support floor, min-errors gate, per-phone row cap, and focus count are all
# tunable per project via ``settings.toml`` (:class:`DiagnosisSettings`); the analysis
# functions read them off ``project.settings.diagnosis``.

# Word-boundary sentinel used as the neighbour of an edge phone.
_BOUNDARY = "#"


@dataclass(frozen=True)
class Confusion:
    """One aggregated phone mismatch across the assessed lexicon.

    ``expected`` is the target phone, ``got`` the phone produced in its place; a
    ``None`` on either side marks the op that has no counterpart — ``got is None`` is
    a deletion (target phone dropped), ``expected is None`` an insertion (spurious
    derived phone). ``examples`` holds a few ``"gloss: derived/attested"`` labels — the word,
    the form it came out as at this checkpoint, and its attested target — showing the confusion.
    """

    expected: str | None
    got: str | None
    count: int
    examples: tuple[str, ...]

    @property
    def kind(self) -> str:
        """``"substitution"``, ``"deletion"``, or ``"insertion"``."""
        if self.expected is None:
            return "insertion"
        if self.got is None:
            return "deletion"
        return "substitution"


def confusions(
    distances: tuple[DistanceToTarget, ...], limit: int | None = None
) -> list[Confusion]:
    """Tally every non-match alignment op across the assessed words, most frequent first.

    Each assessed word's target is aligned to its derived form; substitutions,
    deletions, and insertions are counted by their (expected, got) phone pair. Exact
    words contribute nothing. Ties break by the string pair for a stable order.
    """
    counts: Counter[tuple[str | None, str | None]] = Counter()
    examples: dict[tuple[str | None, str | None], list[str]] = {}
    for dtt in distances:
        if dtt.exact:
            continue
        # "gloss: derived/attested" — the word, how it came out at this checkpoint, and what
        # it should be (at a stage, the stage forms; at the final, surface vs attested).
        label = (
            f"{dtt.gloss}: {dtt.derived}/{dtt.target}"
            if dtt.gloss
            else f"{dtt.derived}/{dtt.target}"
        )
        for op in align(dtt.target_phones, dtt.derived_phones):
            if op.kind == "match":
                continue
            key = (op.target, op.derived)
            counts[key] += 1
            bucket = examples.setdefault(key, [])
            if label not in bucket and len(bucket) < 3:
                bucket.append(label)
    ordered = sorted(
        counts.items(),
        key=lambda kv: (-kv[1], str(kv[0][0]), str(kv[0][1])),
    )
    result = [
        Confusion(expected=exp, got=got, count=count, examples=tuple(examples[(exp, got)]))
        for (exp, got), count in ordered
    ]
    return result if limit is None else result[:limit]


@dataclass(frozen=True)
class ContextAssociation:
    """One environment predictor's association with getting a focus phone wrong.

    ``predictor`` names the attested-form environment (e.g. ``"right=n"`` or
    ``"left:voice=1"``). The 2×2 counts are over the focus phone's positions:
    ``err_here``/``ok_here`` are error vs. correct *with* the predictor present,
    ``err_away``/``ok_away`` without it. ``phi`` is the phi coefficient — positive
    means the predictor co-occurs with error. ``fscore`` is the F1 of treating the
    predictor as a *prediction* of error (precision × recall); shown alongside phi,
    but ranking is by phi, which is chance-corrected where F1 is not.
    """

    predictor: str
    phi: float
    fscore: float
    err_here: int
    ok_here: int
    err_away: int
    ok_away: int

    @property
    def support(self) -> int:
        """Focus positions in which the predictor is present."""
        return self.err_here + self.ok_here


@dataclass(frozen=True)
class FocusAutopsy:
    """The conditioned context autopsy for one focus target phone.

    ``errors``/``total`` are how often the focus phone came out wrong vs. how often
    it occurred. ``support_floor`` is the effective minimum support a predictor needed
    to appear (``max(min_support, ceil(min_support_percent% of total))``), which scales
    with the phone's occurrences. ``associations`` are the predictors that cleared it,
    most error-associated first.
    """

    phone: str
    errors: int
    total: int
    support_floor: int = 0
    associations: tuple[ContextAssociation, ...] = field(default_factory=tuple)


def phi_coefficient(err_here: int, ok_here: int, err_away: int, ok_away: int) -> float:
    """The phi coefficient for a 2×2 of (predictor present/absent) × (error/correct).

    Ranges [-1, 1]; positive when the predictor co-occurs with error. Returns 0.0
    when any margin is zero (the coefficient is undefined — no association to read).
    """
    numerator = err_here * ok_away - ok_here * err_away
    margins = (
        (err_here + ok_here)
        * (err_away + ok_away)
        * (err_here + err_away)
        * (ok_here + ok_away)
    )
    return numerator / math.sqrt(margins) if margins else 0.0


def f_score(err_here: int, ok_here: int, err_away: int) -> float:
    """F1 of treating "predictor present" as a prediction of "error".

    Precision = errors among the predictor's positions (``err_here / support``);
    recall = the predictor's share of all errors (``err_here / all errors``); F1 is
    their harmonic mean. Returns 0.0 when the predictor covers no error (either
    numerator, hence the sum, is zero). Unlike phi it is not chance-corrected — a
    predictor present almost everywhere can post a high F1 at phi ≈ 0 — so it is a
    companion measure, not the ranking key.
    """
    precision_denom = err_here + ok_here
    recall_denom = err_here + err_away
    if err_here == 0 or precision_denom == 0 or recall_denom == 0:
        return 0.0
    precision = err_here / precision_denom
    recall = err_here / recall_denom
    return 2 * precision * recall / (precision + recall)


def _feature_map(phone: str, project: Project, cache: dict[str, dict | None]) -> dict | None:
    """The specified features of a single phone, or ``None`` if it will not segment.

    Featurises the phone on its own (not via the whole form), so it never depends on
    the target/derived alignment lining up with a re-segmentation of the string.
    """
    if phone not in cache:
        try:
            bundles = lower_tiers(string_to_sequence(phone, project))
        except ValueError:
            cache[phone] = None
        else:
            bundle = bundles[0] if bundles else None
            cache[phone] = (
                None
                if bundle is None
                else {f: spec.value for f, spec in bundle.items() if spec.value is not None}
            )
    return cache[phone]


def _predictors(
    left: str, right: str, project: Project, cache: dict[str, dict | None]
) -> set[str]:
    """The environment predictors for a focus position with neighbours *left*/*right*.

    Always the two neighbour identities (``left=<phone>``/``right=<phone>``); plus,
    when a neighbour segments, one predictor per specified feature value
    (``left:<feature>=<value>``). A boundary neighbour contributes only its identity.
    """
    predictors = {f"left={left}", f"right={right}"}
    for side, phone in (("left", left), ("right", right)):
        if phone == _BOUNDARY:
            continue
        features = _feature_map(phone, project, cache)
        if features is None:
            continue
        for feature, value in features.items():
            predictors.add(f"{side}:{feature}={value}")
    return predictors


def error_contexts(
    distances: tuple[DistanceToTarget, ...], focus: str, project: Project
) -> FocusAutopsy:
    """The conditioned context autopsy for one focus target phone.

    Over every assessed word, each target position holding *focus* is a trial: an error
    if the phone was substituted or deleted, correct if reproduced. Each trial's
    attested-form neighbours yield a set of environment predictors; for every predictor a
    2×2 of (present/absent) × (error/correct) gives a phi coefficient. Predictors
    below the support floor are dropped; the rest are returned most-error-associated
    first. Insertions have no focus target phone and never enter this analysis.
    """
    errors = 0
    total = 0
    err_with: Counter[str] = Counter()
    ok_with: Counter[str] = Counter()
    cache: dict[str, dict | None] = {}
    for dtt in distances:
        target_phones = dtt.target_phones
        for op in align(target_phones, dtt.derived_phones):
            if op.target != focus or op.target_index is None:
                continue
            total += 1
            is_error = op.kind != "match"
            errors += is_error
            i = op.target_index
            left = target_phones[i - 1] if i > 0 else _BOUNDARY
            right = target_phones[i + 1] if i + 1 < len(target_phones) else _BOUNDARY
            for predictor in _predictors(left, right, project, cache):
                (err_with if is_error else ok_with)[predictor] += 1
    diagnosis = project.settings.diagnosis
    # The floor scales with the phone's occurrences: a predictor covering a trivial slice
    # of a common phone is noise, while the absolute floor keeps phi stable on rare ones.
    support_floor = max(
        diagnosis.min_support, math.ceil(diagnosis.min_support_percent * total / 100)
    )
    associations: list[ContextAssociation] = []
    if errors >= diagnosis.min_errors:
        for predictor in err_with.keys() | ok_with.keys():
            err_here = err_with[predictor]
            ok_here = ok_with[predictor]
            if err_here + ok_here < support_floor:
                continue
            associations.append(
                ContextAssociation(
                    predictor=predictor,
                    phi=phi_coefficient(
                        err_here, ok_here, errors - err_here, (total - errors) - ok_here
                    ),
                    fscore=f_score(err_here, ok_here, errors - err_here),
                    err_here=err_here,
                    ok_here=ok_here,
                    err_away=errors - err_here,
                    ok_away=(total - errors) - ok_here,
                )
            )
    associations.sort(key=lambda a: (-a.phi, -a.err_here, a.predictor))
    return FocusAutopsy(
        phone=focus, errors=errors, total=total,
        support_floor=support_floor, associations=tuple(associations),
    )


def diagnose(
    distances: tuple[DistanceToTarget, ...], project: Project, top: int | None = None
) -> list[FocusAutopsy]:
    """Autopsy the focus phones behind the *top* most frequent substitution/deletion.

    The confusion tally names the phones going wrong most; this conditions a context
    autopsy on each distinct target phone among them (an insertion has no target phone
    and is skipped). Autopsies with no surviving predictor are still returned so the
    report can say a phone had no discernible conditioning. *top* defaults to the
    project's ``diagnosis.focus_count`` setting.
    """
    if top is None:
        top = project.settings.diagnosis.focus_count
    focus_phones: list[str] = []
    for confusion in confusions(distances):
        if confusion.expected is not None and confusion.expected not in focus_phones:
            focus_phones.append(confusion.expected)
        if len(focus_phones) >= top:
            break
    return [error_contexts(distances, phone, project) for phone in focus_phones]


@dataclass(frozen=True)
class StageDiagnosis:
    """A full diagnosis (confusions + autopsy) computed at one attested stage."""

    label: str
    time: int | None
    confusions: tuple[Confusion, ...]
    autopsy: tuple[FocusAutopsy, ...]


def diagnose_stages(derivations: list[Derivation], project: Project) -> list[StageDiagnosis]:
    """Diagnose each attested stage (and the final), from its derived-vs-attested distances.

    For every stage :func:`accuracy_by_stage` scores (each attested ``Word.stages[T]`` plus
    the final ``Word.final``), the *complete* confusion tally and a context autopsy for
    *every* erroring focus segment on that stage's distances — so the errors present at each
    historical checkpoint are visible, not only the final, and nothing is truncated for a
    display cap (the ``errors.csv``/``error_context.csv`` exports are complete). Only
    meaningful where the attested stage forms are notationally comparable to the engine's
    output (see the stage-accuracy caveat).
    """
    stages: list[StageDiagnosis] = []
    for stage in accuracy_by_stage(derivations, project):
        distances = stage.report.distances
        stage_confusions = tuple(confusions(distances))
        # Autopsy every distinct erroring target segment (an insertion has no target
        # segment and is skipped), not just the top ``focus_count`` — the CSV is complete.
        focus: list[str] = []
        for confusion in stage_confusions:
            if confusion.expected is not None and confusion.expected not in focus:
                focus.append(confusion.expected)
        stages.append(
            StageDiagnosis(
                label=stage.label,
                time=stage.time,
                confusions=stage_confusions,
                autopsy=tuple(error_contexts(distances, phone, project) for phone in focus),
            )
        )
    return stages


def errors_summary_line(stages: list[StageDiagnosis]) -> str:
    """A one-line stderr headline, built from the final stage's confusions."""
    final = next((s for s in stages if s.time is None), None)
    if final is None or not final.confusions:
        return "no errors — every assessed word is exact at the final"
    sites = sum(c.count for c in final.confusions)
    top = final.confusions[0]
    exp = top.expected if top.expected is not None else "∅"
    got = top.got if top.got is not None else "∅"
    return (
        f"final: {sites} error site(s), {len(final.confusions)} distinct; "
        f"most common {exp}→{got} ({top.count}×) — see errors.csv"
    )


def render_errors_csv(stages: list[StageDiagnosis]) -> str:
    """The per-stage confusion tally as CSV — which segments were errors at each stage.

    Columns: ``stage, expected, got, count, kind, examples (gloss: derived vs. attested)``.
    ``∅`` marks the absent side (an insertion has no *expected*, a deletion no *got* — the
    ``kind`` column disambiguates). Complete: every confusion at every stage, no display cap.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(
        ["stage", "expected", "got", "count", "kind", "examples (gloss: derived vs. attested)"]
    )
    for stage in stages:
        for c in stage.confusions:
            writer.writerow([
                stage.label,
                c.expected if c.expected is not None else "∅",
                c.got if c.got is not None else "∅",
                c.count, c.kind, "; ".join(c.examples),
            ])
    return buffer.getvalue()


def render_error_context_csv(stages: list[StageDiagnosis]) -> str:
    """The per-stage, per-segment context autopsy as CSV.

    Columns: ``stage, segment, environment, assoc. (φ), F₁, err/ok · with, err/ok · without``.
    For each erroring focus *segment*, the attested-form *environment* predictors positively
    associated with getting it wrong (phi > 0), each with its phi, F1, and the raw err/ok
    counts with vs. without the predictor. Complete: every such predictor at every stage,
    no top-N cap; segments with no error-associated predictor contribute no rows.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "stage", "segment", "environment", "assoc. (φ)", "F₁", "err/ok · with", "err/ok · without",
    ])
    for stage in stages:
        for autopsy in stage.autopsy:
            for a in autopsy.associations:
                if a.phi <= 0:
                    continue  # error *context* = predictors associated with the error
                writer.writerow([
                    stage.label, autopsy.phone, a.predictor,
                    f"{a.phi:+.2f}", f"{a.fscore:.2f}",
                    f"{a.err_here}/{a.ok_here}", f"{a.err_away}/{a.ok_away}",
                ])
    return buffer.getvalue()


def error_context_omissions(stages: list[StageDiagnosis]) -> list[tuple[str, str]]:
    """The ``(stage, segment)`` autopsies that ``error_context.csv`` leaves out.

    A focus segment appears in ``error_context.csv`` only if at least one environment
    predictor is positively associated with the error (phi > 0). A segment that erred too
    few times to autopsy (< ``min_errors``) or whose predictors were all non-associated
    contributes no row — it is present in ``errors.csv`` but silent in the context export.
    This lists those omissions, one per ``(stage, segment)``, so a caller can say plainly
    what was cut rather than let it vanish.
    """
    return [
        (stage.label, autopsy.phone)
        for stage in stages
        for autopsy in stage.autopsy
        if not any(a.phi > 0 for a in autopsy.associations)
    ]
