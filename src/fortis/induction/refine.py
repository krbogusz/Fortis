"""Composition and Phase-B refinement: from per-interval cascades to one whole-lexicon cascade.

Phase A (:mod:`boost`) induces each interval independently under teacher forcing. This module
stitches those interval cascades into a single time-keyed :class:`RuleInventory` over the real
timescale (:func:`compose`), and — once M3's Phase B lands — refines that composed cascade
against the full multi-checkpoint objective from the true inputs.

Composition assigns each interval's induced rules real times evenly spaced *strictly inside*
the interval's ``(start, end]`` span, so they never collide with the attested boundary stages
and leave room for later insertions (plan §3.3). Rule ids are minted ``ind_<interval>_<n>``;
the ``name`` carries the rule's notation and the ``description`` its provenance, so the composed
inventory reads as a normal hand-written ``rules.toml`` and round-trips through the loader.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, replace

from src.fortis.application.deriving import derive_all_parallel, form_at_time
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.induction.boost import InducedInterval, induce_interval
from src.fortis.induction.intervals import Interval, build_interval, build_intervals, stage_times
from src.fortis.induction.objective import CascadeScore, cascade_score
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule, RuleInventory

# The open interval endpoints (input, final) have no attested time; give them a span this wide
# below the first / above the last stage so their induced rules get distinct real times.
_OPEN_SPAN = 1000


def _interval_bounds(
    interval: InducedInterval, stage_times: list[int]
) -> tuple[int, int]:
    """The real-time ``(lo, hi)`` an interval's induced rules are placed strictly inside.

    Reads the interval label (``input→-200``, ``-100→750``, ``1400→final``): a bounded interval
    uses its two stage times; the input interval floors ``lo`` an ``_OPEN_SPAN`` below the first
    stage; the final interval ceils ``hi`` an ``_OPEN_SPAN`` above the last stage.
    """
    start_label, end_label = interval.label.split("→")
    lo = (stage_times[0] - _OPEN_SPAN) if start_label == "input" else int(start_label)
    hi = (stage_times[-1] + _OPEN_SPAN) if end_label == "final" else int(end_label)
    return lo, hi


def _spaced_times(lo: int, hi: int, count: int) -> list[int]:
    """*count* integer times evenly spaced strictly inside ``(lo, hi)``, ascending.

    Rules at a colliding time keep their list order (the loader preserves file order within a
    time), so a tight span degrades to shared times rather than reordering.
    """
    step = (hi - lo) / (count + 1)
    return [round(lo + step * (index + 1)) for index in range(count)]


def _safe_label(label: str) -> str:
    """A label sanitised for use inside a rule id (``input→-200`` → ``input_-200``)."""
    return re.sub(r"[^A-Za-z0-9-]+", "_", label)


@dataclass(frozen=True)
class InductionResult:
    """The whole-project induction outcome: the per-interval traces and the composed cascade."""

    intervals: list[InducedInterval]
    inventory: RuleInventory


def _intervals_to_run(project: Project, ignore_stages: bool) -> list[Interval]:
    """The intervals to induce: every attested-stage interval, or one ``input→final`` span.

    ``ignore_stages`` forces the single-interval mode of §3.5 even on stage-bearing data — the
    ablation that measures what dense chronological supervision buys.
    """
    if ignore_stages or not stage_times(project):
        return [build_interval(project, None, None)]
    return build_intervals(project)


def induce_project(
    project: Project,
    *,
    ignore_stages: bool = False,
    only_interval: tuple[int | None, int | None] | None = None,
    **boost_kwargs: object,
) -> InductionResult:
    """Induce every interval (Phase A) and compose them into one real-time cascade (§3.1–3.3).

    Each interval is induced independently under teacher forcing; the results compose into a
    single loadable :class:`RuleInventory`. ``ignore_stages`` collapses to one ``input→final``
    interval (the ablation, §3.5); ``only_interval`` runs a single named span (for development).
    Extra keyword arguments pass straight through to :func:`induce_interval`.
    """
    if only_interval is not None:
        intervals_to_run = [build_interval(project, *only_interval)]
    else:
        intervals_to_run = _intervals_to_run(project, ignore_stages)
    induced = [induce_interval(interval, **boost_kwargs) for interval in intervals_to_run]  # type: ignore[arg-type]
    return InductionResult(intervals=induced, inventory=compose(induced, project))


def compose(intervals: list[InducedInterval], project: Project) -> RuleInventory:
    """Stitch the per-interval induced cascades into one real-time :class:`RuleInventory`.

    Each interval's rules are placed at real times strictly inside its span and given ids
    ``ind_<interval>_<n>``, a ``name`` (their notation, marked induced), and a ``description``
    recording the interval and placement. The result is a normal loadable inventory.
    """
    stage_times = sorted({time for word in project.words.values() for time in word.stages})
    composed: dict[int | None, list[Rule]] = {}
    for interval in intervals:
        if not interval.rules:
            continue
        if stage_times:
            lo, hi = _interval_bounds(interval, stage_times)
        else:
            lo, hi = 0, len(interval.rules) + 1
        times = _spaced_times(lo, hi, len(interval.rules))
        safe = _safe_label(interval.label)
        for number, (rule, time) in enumerate(zip(interval.rules, times, strict=True), start=1):
            placed = replace(
                rule,
                id=f"ind_{safe}_{number}",
                time=time,
                name=f"{rule.raw_definition} (induced)",
                description=f"induced in interval {interval.label}, step {number}",
            )
            composed.setdefault(time, []).append(placed)
    return RuleInventory({time: tuple(rules) for time, rules in sorted(composed.items())})


# --- Phase B: global refinement of the composed cascade (plan §3.4) ---------------------


@dataclass(frozen=True)
class RefineTrace:
    """The Phase-B record: what global shrink removed and what final-residual boosting added."""

    removed: list[str] = field(default_factory=list)
    added: list[str] = field(default_factory=list)
    start_score: CascadeScore | None = None
    final_score: CascadeScore | None = None


def _flat(inventory: RuleInventory) -> list[Rule]:
    """Every rule in ``(time, file-order)`` — the composed cascade as an ordered list."""
    return [
        rule
        for time in sorted(inventory, key=lambda t: (t is None, t))
        for rule in inventory[time]
    ]


def _inventory(rules: list[Rule]) -> RuleInventory:
    """Rebuild an inventory keyed by ``rule.time`` from an ordered rule list."""
    by_time: dict[int | None, list[Rule]] = {}
    for rule in rules:
        by_time.setdefault(rule.time, []).append(rule)
    return RuleInventory({time: tuple(rules) for time, rules in by_time.items()})


def _score(project: Project, inventory: RuleInventory, workers: int | None) -> CascadeScore:
    """The full multi-checkpoint ``L`` of a cascade over the whole lexicon (from true inputs)."""
    runnable = replace(project, rules=inventory)
    return cascade_score(derive_all_parallel(runnable, workers=workers), runnable)


def _global_shrink(project: Project, rules: list[Rule]) -> tuple[list[Rule], list[str]]:
    """Remove composed rules whose individual deletion lowers the whole-lexicon ``L`` (§3.4).

    This kills rules that only earned their keep under teacher forcing: composed and run from
    the true inputs over every checkpoint, a rule that no longer pays for its bits is retired.
    One batch pass — each rule's removal is scored once against the full cascade, and every rule
    whose removal individually lowers ``L`` is dropped together (``rules`` mini-runs, per the
    §5 cost, not ``rules²``). Trials are serial (a pool per trial would cost more in startup than
    it saves). If the batch removal did not in fact lower ``L`` (an interaction), it falls back
    to removing only the single most profitable rule.
    """
    base = _score(project, _inventory(rules), workers=1).total
    deltas = [
        base - _score(project, _inventory(rules[:i] + rules[i + 1 :]), workers=1).total
        for i in range(len(rules))
    ]
    helpful = [i for i, delta in enumerate(deltas) if delta > 1e-6]
    if not helpful:
        return rules, []
    kept = [rule for i, rule in enumerate(rules) if i not in set(helpful)]
    if len(kept) >= 1 and _score(project, _inventory(kept), workers=1).total < base - 1e-6:
        log = [f"removed `{rules[i].raw_definition}`" for i in helpful]
        return kept, log
    best = max(helpful, key=lambda i: deltas[i])  # batch interacted — remove just the best
    return (
        rules[:best] + rules[best + 1 :],
        [f"removed `{rules[best].raw_definition}` (L {base:.0f} → {base - deltas[best]:.0f})"],
    )


def _final_residual_interval(
    project: Project, inventory: RuleInventory, workers: int | None
) -> Interval:
    """A mini-project whose input is the composed *derived* surface and target the attested final.

    Phase A teacher-forced each interval from the *attested* earlier form; composed and run from
    the true inputs, the derived form reaching the final can differ. That systematic gap is a
    residual — captured here as an ``input → final`` interval whose source is the composed
    surface, so boosting it appends the corrective rules the composition needs (§3.4).
    """
    runnable = replace(project, rules=inventory)
    derivations = derive_all_parallel(runnable, workers=workers)
    words: dict[str, Word] = {}
    for derivation in derivations:
        if derivation.word.final is None:
            continue
        surface = render_syllabified(
            lower_tiers(derivation.surface), derivation.surface_boundaries, project
        )
        words.setdefault(
            surface,
            Word.from_series(
                id=surface, seed=surface, gloss=derivation.word.gloss,
                final=derivation.word.final, frequency=derivation.word.frequency,
            ),
        )
    mini = replace(project, words=WordInventory(words), rules=RuleInventory())
    return Interval(start=None, end=None, project=mini)


def refine(
    project: Project,
    inventory: RuleInventory,
    *,
    max_rounds: int = 2,
    workers: int | None = None,
    **boost_kwargs: object,
) -> tuple[RuleInventory, RefineTrace]:
    """Phase-B refinement: global shrink + final-residual boosting until a sweep changes nothing.

    Each round (plan §3.4): (1) global shrink retires rules that only worked under teacher
    forcing; (2) the composed cascade's final residual — the gap between the derived and attested
    final forms, invisible during teacher forcing — is boosted into corrective rules appended
    after the cascade. Loops until neither step changes anything or ``max_rounds`` is hit.
    """
    start = _score(project, inventory, workers)
    rules = _flat(inventory)
    removed: list[str] = []
    added: list[str] = []
    for _round in range(max_rounds):
        rules, shrink_log = _global_shrink(project, rules)
        removed.extend(shrink_log)

        residual = _final_residual_interval(project, _inventory(rules), workers)
        induced = induce_interval(residual, **boost_kwargs)  # type: ignore[arg-type]
        if not induced.rules:
            if not shrink_log:
                break  # a full sweep changed nothing — converged
            continue
        # Append the corrective rules after the cascade, at fresh trailing times.
        latest = max((r.time for r in rules if r.time is not None), default=0)
        for offset, rule in enumerate(induced.rules, start=1):
            appended = replace(
                rule, id=f"ind_refine_{len(added) + offset}", time=latest + offset,
                name=f"{rule.raw_definition} (refined)",
                description="Phase-B final-residual correction",
            )
            rules.append(appended)
            added.append(rule.raw_definition)

    final_inventory = _inventory(rules)
    return final_inventory, RefineTrace(
        removed=removed, added=added, start_score=start,
        final_score=_score(project, final_inventory, workers),
    )


# --- Localized per-interval refinement (the plan's full Phase-B boosting, §3.4) ----------


def _stage_residual_interval(
    project: Project,
    inventory: RuleInventory,
    start: int | None,
    end: int | None,
    workers: int | None,
) -> Interval:
    """A residual mini-project correcting one attested stage from the composed cascade's own output.

    Each word's source is the composed cascade's *derived* snapshot **at ``end``** (the stage
    being corrected) — the form the cascade actually reaches there — and the target is the
    *attested* form at ``end``. Boosting maps derived-at-stage → attested-at-stage, so the
    corrective rules, inserted just before ``end``, fire on exactly the form they were fit to
    and pull that checkpoint back onto its attested value. Fixing the stage in place stops the
    error compounding into the next interval (§3.4). ``start`` only bounds the insertion window.
    """
    runnable = replace(project, rules=inventory)
    derivations = derive_all_parallel(runnable, workers=workers)
    words: dict[str, Word] = {}
    for derivation in derivations:
        target = derivation.word.final if end is None else derivation.word.stages.get(end)
        if target is None:
            continue
        if end is None:
            form, boundaries = derivation.surface, derivation.surface_boundaries
        else:
            form, boundaries = form_at_time(derivation, end)
        source = render_syllabified(lower_tiers(form), boundaries, project)
        if source in words:
            continue
        try:
            string_to_sequence(source, project)
        except ValueError:
            continue
        words[source] = Word.from_series(
            id=source, seed=source, gloss=derivation.word.gloss, final=target,
            frequency=derivation.word.frequency,
        )
    mini = replace(project, words=WordInventory(words), rules=RuleInventory())
    return Interval(start=start, end=end, project=mini)


def _localized_bounds(start: int | None, end: int | None, times: list[int]) -> tuple[int, int]:
    """The real-time window an interval's corrective rules are inserted into."""
    lo = (times[0] - _OPEN_SPAN) if start is None else start
    hi = (times[-1] + _OPEN_SPAN) if end is None else end
    return lo, hi


def refine_localized(
    project: Project,
    inventory: RuleInventory,
    *,
    max_rounds: int = 2,
    workers: int | None = None,
    **boost_kwargs: object,
) -> tuple[RuleInventory, RefineTrace]:
    """Phase-B localized refinement: repair each interval on its *composed-derived* input (§3.4).

    The composed cascade's weakness is that interval k, teacher-forced from the attested stage
    ``t_{k-1}``, misfires when it instead receives the *derived* (error-laden) ``t_{k-1}`` —
    errors compound. This walks the attested stages in time order; for each it boosts a residual
    mini-project mapping the composed *derived* form at that stage to the *attested* one, then
    inserts the corrective rules just before that stage's boundary. Re-deriving between stages
    means each later interval sees the repaired earlier stage — breaking the compounding. Loops
    until a full sweep adds nothing.
    """
    start_score = _score(project, inventory, workers)
    rules = _flat(inventory)
    added: list[str] = []
    times = stage_times(project)
    checkpoints: list[int | None] = [None, *times, None]
    boundaries = list(zip(checkpoints, checkpoints[1:], strict=False))
    for _round in range(max_rounds):
        changed = False
        for start, end in boundaries:
            interval = _stage_residual_interval(project, _inventory(rules), start, end, workers)
            if not interval.project.words:
                continue
            induced = induce_interval(interval, **boost_kwargs)  # type: ignore[arg-type]
            if not induced.rules:
                continue
            changed = True
            lo, hi = _localized_bounds(start, end, times)
            after = max(
                (r.time for r in rules if r.time is not None and lo < r.time < hi), default=lo
            )
            new_times = _spaced_times(after, hi, len(induced.rules))
            for offset, (rule, time) in enumerate(
                zip(induced.rules, new_times, strict=True), start=1
            ):
                rules.append(replace(
                    rule, id=f"ind_loc_{len(added) + offset}", time=time,
                    name=f"{rule.raw_definition} (localized)",
                    description=f"Phase-B localized refinement of interval {start}→{end}",
                ))
                added.append(rule.raw_definition)
            rules.sort(key=lambda r: (r.time is None, r.time))
        if not changed:
            break

    final_inventory = _inventory(rules)
    return final_inventory, RefineTrace(
        removed=[], added=added, start_score=start_score,
        final_score=_score(project, final_inventory, workers),
    )
