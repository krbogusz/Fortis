"""Diagnose *where* a rule set goes wrong, not just *how much*.

The grader (:mod:`src.fortis.analysis.grading`) scores each derived form against its
attested target. This module reads the same graded forms but asks the follow-up
question — *what is going wrong, and in what environment* — so a score becomes a
lead on the next rule to fix. Two views, both built on the target→derived alignment
in :func:`src.fortis.analysis.grading.align`:

- **Confusions** — a ranked tally of the phone mismatches across the whole lexicon:
  which target phone was reproduced as which other phone (or dropped, or a spurious
  phone inserted). Answers "which phones am I getting wrong, and how often".

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

import math
from collections import Counter
from dataclasses import dataclass, field

from src.fortis.analysis.blame import Blame, blame_all
from src.fortis.analysis.grading import Grade, align, grade_stages, split_phones
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project

# The support floor, min-errors gate, per-phone row cap, and focus count are all
# tunable per project via ``settings.toml`` (:class:`DiagnosisSettings`); the analysis
# functions read them off ``project.settings.diagnosis``.

# Word-boundary sentinel used as the neighbour of an edge phone.
_BOUNDARY = "#"
# Per-stage confusion tables are capped in the report — an intermediate stage often has a
# long noisy tail (notation differences), and the full tally lives in the final section.
_STAGE_CONFUSION_CAP = 15


@dataclass(frozen=True)
class Confusion:
    """One aggregated phone mismatch across the graded lexicon.

    ``expected`` is the target phone, ``got`` the phone produced in its place; a
    ``None`` on either side marks the op that has no counterpart — ``got is None`` is
    a deletion (target phone dropped), ``expected is None`` an insertion (spurious
    derived phone). ``examples`` holds a few word labels showing the confusion.
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


def confusions(grades: tuple[Grade, ...], limit: int | None = None) -> list[Confusion]:
    """Tally every non-match alignment op across the graded words, most frequent first.

    Each graded word's target is aligned to its derived form; substitutions,
    deletions, and insertions are counted by their (expected, got) phone pair. Exact
    words contribute nothing. Ties break by the string pair for a stable order.
    """
    counts: Counter[tuple[str | None, str | None]] = Counter()
    examples: dict[tuple[str | None, str | None], list[str]] = {}
    for grade in grades:
        if grade.exact:
            continue
        label = grade.gloss or grade.ipa
        for op in align(split_phones(grade.target), split_phones(grade.derived)):
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
    means the predictor co-occurs with error.
    """

    predictor: str
    phi: float
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


def error_contexts(grades: tuple[Grade, ...], focus: str, project: Project) -> FocusAutopsy:
    """The conditioned context autopsy for one focus target phone.

    Over every graded word, each target position holding *focus* is a trial: an error
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
    for grade in grades:
        target_phones = split_phones(grade.target)
        for op in align(target_phones, split_phones(grade.derived)):
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
    support_floor = max(diagnosis.min_support, math.ceil(diagnosis.min_support_percent * total / 100))
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
                    phi=phi_coefficient(err_here, ok_here, errors - err_here, (total - errors) - ok_here),
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
    grades: tuple[Grade, ...], project: Project, top: int | None = None
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
    for confusion in confusions(grades):
        if confusion.expected is not None and confusion.expected not in focus_phones:
            focus_phones.append(confusion.expected)
        if len(focus_phones) >= top:
            break
    return [error_contexts(grades, phone, project) for phone in focus_phones]


@dataclass(frozen=True)
class TimeBucket:
    """The wrong phones a rule-time introduced, from blame provenance.

    ``time`` is the rule-time whose rules produced these wrong phones (``None`` groups
    the residuals no single rule owns — omissions, deletions, and unattributed phones).
    ``count`` is how many wrong phones fall in the bucket; ``confusions`` tally them by
    ``expected→got`` within the time.
    """

    time: int | None
    count: int
    confusions: tuple[Confusion, ...]


def errors_by_time(blames: list[Blame]) -> list[TimeBucket]:
    """Bucket every wrong phone by the rule-time that produced it, worst bucket first.

    Reads blame's segment-id provenance: each residual's ``culprit_time`` is the time of
    the rule that set the wrong phone. Answers "which period introduces the most errors".
    Residuals with no attributable rule (omissions, deletions, unattributed phones) group
    under ``time=None``.
    """
    counts: dict[int | None, Counter[tuple[str | None, str | None]]] = {}
    examples: dict[tuple[int | None, str | None, str | None], list[str]] = {}
    for blame in blames:
        label = blame.gloss or blame.ipa
        for residual in blame.residuals:
            time = residual.culprit_time if residual.culprit else None
            pair = (residual.expected, residual.got)
            counts.setdefault(time, Counter())[pair] += 1
            bucket = examples.setdefault((time, *pair), [])
            if label not in bucket and len(bucket) < 3:
                bucket.append(label)
    result = [
        TimeBucket(
            time=time,
            count=sum(pairs.values()),
            confusions=tuple(
                Confusion(exp, got, n, tuple(examples[(time, exp, got)]))
                for (exp, got), n in sorted(pairs.items(), key=lambda kv: (-kv[1], str(kv[0])))
            ),
        )
        for time, pairs in counts.items()
    ]
    # Worst bucket first; the None (no-rule) bucket sorts by its count like any other.
    result.sort(key=lambda b: (-b.count, b.time is None, b.time or 0))
    return result


@dataclass(frozen=True)
class StageDiagnosis:
    """A full diagnosis (confusions + autopsy) computed at one attested stage."""

    label: str
    time: int | None
    confusions: tuple[Confusion, ...]
    autopsy: tuple[FocusAutopsy, ...]


def diagnose_stages(derivations: list[Derivation], project: Project) -> list[StageDiagnosis]:
    """Diagnose each attested stage (and the final), from its derived-vs-attested grades.

    For every stage :func:`grade_stages` scores (each attested ``Word.stages[T]`` plus
    the final ``Word.final``), runs the confusion tally and context autopsy on that
    stage's grades — so the errors present at each historical checkpoint are visible,
    not only the final. Only meaningful where the attested stage forms are notationally
    comparable to the engine's output (see the stage-grading caveat).
    """
    stages: list[StageDiagnosis] = []
    for stage in grade_stages(derivations, project):
        grades = stage.report.grades
        stages.append(
            StageDiagnosis(
                label=stage.label,
                time=stage.time,
                confusions=tuple(confusions(grades)),
                autopsy=tuple(diagnose(grades, project)),
            )
        )
    return stages


def _confusion_label(value: str | None, *, missing: str) -> str:
    """Render one side of a confusion, using *missing* for the absent side."""
    return f"`{value}`" if value is not None else missing


def diagnosis_summary_line(grades: tuple[Grade, ...]) -> str:
    """A one-line headline for stderr."""
    table = confusions(grades)
    if not table:
        return "no confusions — every graded word is exact"
    sites = sum(c.count for c in table)
    top = table[0]
    exp = top.expected if top.expected is not None else "∅"
    got = top.got if top.got is not None else "∅"
    return (
        f"{sites} error site(s), {len(table)} distinct confusion(s); "
        f"most common {exp}→{got} ({top.count}×) — see diagnosis.md"
    )


def render_diagnosis(grades: tuple[Grade, ...], project: Project, where: str) -> str:
    """The ``diagnosis.md`` snapshot: the final confusion tally then per-phone autopsy.

    The *temporal* views — errors bucketed by rule-time and the per-stage diagnosis —
    live in their own :func:`render_timeline` report (``timeline.md``).
    """
    lines = [
        f"# Diagnosis — {where}",
        "",
        "*Where* the derivation goes wrong, from the same forms `distances.md` scores.",
        "Environments are read from the **attested** form (a stable coordinate to condition",
        "on — the derived form's own environment may differ, and often that difference is",
        "the cause). A metathesis reads as an adjacent pair of substitutions.",
        "",
    ]
    table = confusions(grades)
    if not table:
        lines.append("Every graded word is exact — no confusions to report.")
        return "\n".join(lines).rstrip() + "\n"

    lines += [
        "## Confusions",
        "",
        "Phone mismatches across all graded words, most frequent first. `∅` on the",
        "*got* side is a dropped phone; on the *expected* side, a spurious inserted one.",
        "",
        "| expected | got | count | kind | examples |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for c in table:
        expected = _confusion_label(c.expected, missing="`∅`")
        got = _confusion_label(c.got, missing="`∅`")
        lines.append(
            f"| {expected} | {got} | {c.count} | {c.kind} | {', '.join(c.examples)} |"
        )
    diagnosis = project.settings.diagnosis
    lines += ["", "## Context autopsy", ""]
    lines += _autopsy_intro(diagnosis.min_support, diagnosis.min_support_percent)
    for autopsy in diagnose(grades, project):
        lines += _autopsy_section(autopsy, diagnosis.min_errors, diagnosis.report_top)
    return "\n".join(lines).rstrip() + "\n"


def timeline_summary_line(buckets: list[TimeBucket]) -> str:
    """A one-line headline for stderr, naming the period that introduces the most errors."""
    attributed = [b for b in buckets if b.time is not None]
    if not attributed:
        return "no rule-time attributed errors — see timeline.md"
    worst = max(attributed, key=lambda b: b.count)
    return f"errors enter mostly at t={worst.time} ({worst.count} phones) — see timeline.md"


def render_timeline(
    buckets: list[TimeBucket],
    stages: list[StageDiagnosis],
    project: Project,
    where: str,
) -> str:
    """The ``timeline.md`` report: errors by rule-time, then a per-stage diagnosis.

    The two *temporal* views split out of the diagnosis snapshot — *when* in the cascade
    errors enter (from blame provenance) and *what* is wrong at each attested stage.
    """
    lines = [
        f"# Timeline — {where}",
        "",
        "*When* the derivation goes wrong, alongside the `diagnosis.md` snapshot of *what*",
        "goes wrong at the end. Two views: errors bucketed by the rule-time that produced",
        "them, and the full diagnosis recomputed at each attested stage.",
    ]
    if buckets:
        lines += _by_time_section(buckets)
    if stages:
        lines += _stages_section(stages, project.settings.diagnosis)
    if not buckets and not stages:
        lines += ["", "Every graded word is exact — no timeline to report."]
    return "\n".join(lines).rstrip() + "\n"


def _confusion_rows(table: tuple[Confusion, ...]) -> list[str]:
    """A confusion table body (header + rows), shared by the sections."""
    rows = ["| expected | got | count | kind | examples |", "| --- | --- | ---: | --- | --- |"]
    for c in table:
        rows.append(
            f"| {_confusion_label(c.expected, missing='`∅`')} "
            f"| {_confusion_label(c.got, missing='`∅`')} "
            f"| {c.count} | {c.kind} | {', '.join(c.examples)} |"
        )
    return rows


def _by_time_section(buckets: list[TimeBucket]) -> list[str]:
    """"Errors by rule-time": which period introduced the most wrong phones."""
    lines = [
        "",
        "## Errors by rule-time",
        "",
        "Each wrong phone attributed (via blame provenance) to the rule-time that produced",
        "it — where errors *enter* the derivation. `t=∅` groups phones no single rule owns",
        "(omissions, deletions, unattributed). Worst period first.",
        "",
        "| rule-time | wrong phones | top confusions |",
        "| --- | ---: | --- |",
    ]
    for b in buckets:
        time = "∅" if b.time is None else f"t={b.time}"
        top = ", ".join(
            f"{c.expected or '∅'}→{c.got or '∅'} ×{c.count}" for c in b.confusions[:4]
        )
        lines.append(f"| {time} | {b.count} | {top} |")
    return lines


def _stages_section(stages: list[StageDiagnosis], diagnosis) -> list[str]:
    """"Per-stage diagnosis": the confusion tally + autopsy at each attested stage."""
    lines = [
        "",
        "## Per-stage diagnosis",
        "",
        "The confusions and context autopsy at each attested stage (and the final) — the",
        "errors present at each historical checkpoint. Trust an intermediate stage only",
        "where its attested forms are notationally comparable to the engine's output.",
        "",
    ]
    for stage in stages:
        lines += [f"### stage {stage.label}", ""]
        if not stage.confusions:
            lines += ["All graded words at this stage are exact.", ""]
            continue
        shown = stage.confusions[:_STAGE_CONFUSION_CAP]
        if len(stage.confusions) > len(shown):
            lines.append(f"Top {len(shown)} of {len(stage.confusions)} confusions.")
            lines.append("")
        lines += _confusion_rows(shown)
        lines.append("")
        for autopsy in stage.autopsy:
            lines += _autopsy_section(autopsy, diagnosis.min_errors, diagnosis.report_top)
    return lines


def _autopsy_intro(min_support: int, min_support_percent: int) -> list[str]:
    return [
        "For each target phone that most often comes out wrong, the attested-form",
        "environments most associated with the error, by phi coefficient (positive =",
        "more error-prone). A predictor is shown only if it clears the support floor —",
        f"max({min_support}, {min_support_percent}% of the phone's occurrences), so the bar rises",
        "with a bigger word base; the raw *err/ok* counts, present (here) vs. absent (away),",
        "travel with each row so a thin cell is visible. `left`/`right` name the",
        "neighbouring attested phone; `left:f=v` a feature of that neighbour.",
        "",
    ]


def _autopsy_section(autopsy: FocusAutopsy, min_errors: int, report_top: int) -> list[str]:
    rate = autopsy.errors / autopsy.total if autopsy.total else 0.0
    header = [
        f"### `{autopsy.phone}` — wrong {autopsy.errors}/{autopsy.total} ({rate:.0%})",
        "",
    ]
    if autopsy.errors < min_errors:
        return [*header, f"Too few errors to autopsy (< {min_errors}).", ""]
    shown = [a for a in autopsy.associations if a.phi > 0][:report_top]
    if not shown:
        return [*header, "No environment predictor was positively associated with the error.", ""]
    note = (
        f"Top {len(shown)} of {len(autopsy.associations)} predictors "
        f"(support ≥ {autopsy.support_floor})."
    )
    rows = [
        note,
        "",
        "| context | phi | err/ok here | err/ok away |",
        "| --- | ---: | ---: | ---: |",
    ]
    for a in shown:
        rows.append(
            f"| `{a.predictor}` | {a.phi:+.2f} "
            f"| {a.err_here}/{a.ok_here} | {a.err_away}/{a.ok_away} |"
        )
    return [*header, *rows, ""]
