"""The greedy boosting loop for one interval (plan §2, M1 slice: append placement only).

Stagewise additive modeling with sound-change rules as the weak learners. Starting from the
identity map (the interval's attested source forms), each iteration:

1. reads the residual — the confusion tally on the current derived side — into the top
   correspondences and their derived-side conditioning environments (:mod:`correspond`);
2. proposes a candidate set per correspondence (:mod:`candidates`), the corrective rewrite at
   several context generalities plus indels;
3. scores every candidate at the append placement (one ``apply_rule`` sweep per word, no
   re-derivation — :meth:`IntervalState.score_append`);
4. accepts the single candidate with the lowest ΔL, iff it strictly lowers ``L`` and improves
   at least ``min_improved_words`` words (the MDL criterion plus the anti-overfitting floor).

The loop stops when no candidate lowers ``L``, ``fit_bits`` reaches 0, or
``max_rules_per_interval`` is hit. This M1 slice uses append placement only; the placement
search, shrink pass, class-target candidates, and escape ladder are M2.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src.fortis.induction.candidates import Candidate, class_candidates, propose
from src.fortis.induction.correspond import correspondences
from src.fortis.induction.evaluate import AppendScore, IntervalState
from src.fortis.induction.intervals import Interval
from src.fortis.induction.objective import BitsModel, bits_model, rule_bits
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule

# A candidate must beat the incumbent loss by more than this to be accepted — ties (and the
# floating-point noise around 0) are rejected, so the loop cannot churn on a null change.
_EPSILON = 1e-6


@dataclass(frozen=True)
class InductionStep:
    """One accepted rule and the loss change it bought.

    ``fit_before``/``fit_after`` bracket the interval's fit bits; ``exact_before``/
    ``exact_after`` its exact-match count. ``delta_l`` is the accepted candidate's MDL change.
    """

    definition: str
    delta_l: float
    delta_fit: float
    rule_cost: float
    improved: int
    moved: int
    fit_before: float
    fit_after: float
    exact_before: int
    exact_after: int
    placement: int = -1  # list index the rule was inserted at (-1 = append, set by the loop)


@dataclass(frozen=True)
class InducedInterval:
    """The outcome of inducing one interval: the rules, the trace, and why it stopped.

    ``rules`` is the induced cascade in application order (each a valid ``Rule`` with its
    original notation). ``stopped`` is ``"converged"`` (no candidate lowered ``L``),
    ``"fit_zero"`` (nothing left to fix), or ``"max_rules"``.
    """

    label: str
    rules: list[Rule]
    steps: list[InductionStep]
    stopped: str
    start_fit: float
    final_fit: float
    start_exact: int
    final_exact: int
    assessed: int
    shrink_log: list[str] = field(default_factory=list)


def _exact(state: IntervalState) -> int:
    """The number of exactly-derived words in the current baseline."""
    return sum(1 for dtt in state.baseline_distances if dtt is not None and dtt.exact)


def _gather(
    state: IntervalState, project: Project, confusion_cap: int, use_class: bool = True
) -> list[Candidate]:
    """The candidate set at a confusion depth: per-correspondence lattice plus class targets.

    Deduped by definition so an expanded confusion cap (the escape ladder) re-scores only new
    candidates cheaply upstream — the caller tracks what it has already scored.
    """
    distances = tuple(dtt for dtt in state.baseline_distances if dtt is not None)
    corrs = correspondences(distances, project, confusion_cap)
    candidates: list[Candidate] = []
    seen: set[str] = set()
    for correspondence in corrs:
        for candidate in propose(correspondence, project):
            if candidate.definition not in seen:
                seen.add(candidate.definition)
                candidates.append(candidate)
    if use_class:
        for candidate in class_candidates(corrs, project):
            if candidate.definition not in seen:
                seen.add(candidate.definition)
                candidates.append(candidate)
    return candidates


def _qualifying(
    state: IntervalState, candidates: list[Candidate], min_improved: int
) -> list[tuple[Candidate, AppendScore]]:
    """Every candidate that strictly lowers ``L`` and clears the min-improved floor, by ΔL.

    Scored at the append placement (the cheap fast path); the caller reserves the costly
    placement search for the best few of these.
    """
    scored: list[tuple[Candidate, AppendScore]] = []
    for candidate in candidates:
        if len(candidate.rules) != 1:
            continue  # the v1 lattice is single-rule; a multi-rule pair is M4 (pair lookahead)
        score = state.score_append(candidate.rules[0])
        if score.delta_l < -_EPSILON and score.improved >= min_improved:
            scored.append((candidate, score))
    scored.sort(key=lambda cs: cs[1].delta_l)
    return scored


def _placement_positions(cascade_length: int) -> list[int]:
    """Non-append insertion positions to try for a finalist (plan §2.3, M2 subset).

    Append (``index == cascade_length``) is already scored; this adds the interval start and,
    for a longer cascade, the midpoint — the positions where a candidate would *feed* later
    rules. Blame-guided positions (before/after the rule blame names most) are M3.
    """
    positions = {0}
    if cascade_length >= 2:
        positions.add(cascade_length // 2)
    positions.discard(cascade_length)
    return sorted(positions)


def _best_candidate(
    state: IntervalState,
    project: Project,
    settings,
    *,
    use_class: bool = True,
    escape: bool = True,
    placement: bool = True,
) -> tuple[Candidate, int, AppendScore] | None:
    """Find the best accept-worthy (candidate, placement), walking the escape ladder if needed.

    Starts at ``top_confusions`` residual correspondences; if nothing qualifies there (the top
    confusion may be irreducible noise while a deeper one is a clean rule — plan §2.5), it
    expands the confusion cap and retries, up to a bounded depth. The top
    ``placement_candidates`` finalists (by append ΔL) then get the placement search — evaluated
    at a few non-append positions — and the global lowest-ΔL (candidate, index) wins. Returns
    ``None`` only when no expansion yields a ΔL-lowering candidate.
    """
    depths = (1, 2, 4) if escape else (1,)
    finalists: list[tuple[Candidate, AppendScore]] = []
    for depth in depths:
        candidates = _gather(state, project, settings.top_confusions * depth, use_class)
        finalists = _qualifying(state, candidates, settings.min_improved_words)
        if finalists:
            break
    if not finalists:
        return None

    append_index = len(state.rules)
    best_candidate, best_score = finalists[0]
    best = (best_candidate, append_index, best_score)
    if placement:
        for candidate, _append_score in finalists[: settings.placement_candidates]:
            for index in _placement_positions(append_index):
                score = state.score_at(candidate.rules[0], index)
                if score.delta_l < best[2].delta_l - _EPSILON and score.improved >= (
                    settings.min_improved_words
                ):
                    best = (candidate, index, score)
    return best


def _loss_and_exact(project: Project, rules: list[Rule], model: BitsModel) -> tuple[float, int]:
    """The interval loss ``L = fit_bits + rule_bits`` and the exact-match count (one mini-run)."""
    state = IntervalState(project, rules)
    loss = state.baseline_fit + sum(rule_bits(rule, project, model) for rule in rules)
    return loss, _exact(state)


def _shrink(
    project: Project, rules: list[Rule], model: BitsModel, *, guard_exact: bool = False
) -> tuple[list[Rule], list[str]]:
    """Delete any induced rule whose removal lowers ``L``, greediest first, to fixpoint (§2.6).

    The boosting-pruning analog: a later rule routinely makes an earlier greedy step redundant,
    and MDL now charges it rent. Each pass re-scores the cascade without each remaining rule and
    removes the single most profitable deletion; it repeats until none helps. Worst case
    ``rules²`` mini-runs, a handful of passes in practice.

    This is faithful MDL — it removes exactly the rules the objective says to. Fit bits and
    exact accuracy coincide only at the ``fit_bits`` = 0 optimum; short of it (the v1
    expressivity limit) they can diverge, so removing an *over-broad unconditioned* rule that
    completes whole words but regresses feature-weighted fit on the words it shouldn't touch
    (e.g. an unconditioned final-schwa deletion in French, where some finals keep the schwa)
    can lower ``L`` yet drop exact. The right fix is a better-conditioned candidate, not a
    shrink patch — so shrink stays faithful to ``L``. The optional ``guard_exact`` refuses any
    removal that lowers the exact-match count: an explicit accuracy-first mode, off by default
    because it silently optimizes a different objective than the rest of the loop (and it is a
    single-checkpoint notion of "exact" that would not carry to Phase-B composition). On the
    real Latin −100→750 interval it is a no-op (shrink removes nothing either way); it only
    bites on clean synthetic intervals where the greedy path grabbed an over-broad indel.
    """
    rules = list(rules)
    log: list[str] = []
    while len(rules) > 1:
        base_loss, base_exact = _loss_and_exact(project, rules, model)
        best_index: int | None = None
        best_loss = base_loss - _EPSILON
        for index in range(len(rules)):
            trial = rules[:index] + rules[index + 1 :]
            loss, exact = _loss_and_exact(project, trial, model)
            if loss < best_loss and (not guard_exact or exact >= base_exact):
                best_index, best_loss = index, loss
        if best_index is None:
            break
        log.append(
            f"removed `{rules[best_index].raw_definition}` (L {base_loss:.0f} → {best_loss:.0f})"
        )
        rules = rules[:best_index] + rules[best_index + 1 :]
    return rules, log


def induce_interval(
    interval: Interval,
    *,
    shrink: bool = True,
    shrink_guards_exact: bool = False,
    use_class: bool = True,
    escape: bool = True,
    placement: bool = True,
) -> InducedInterval:
    """Induce one interval's rule cascade by greedy MDL boosting (plan §2).

    Runs on the interval's mini-project (attested source → attested target). Reads its tuning
    from the project's ``induction`` settings. ``shrink_guards_exact`` switches the shrink pass
    to the explicit accuracy-first mode (never drop a rule that lowers exact) — off by default,
    since faithful MDL shrink is the coherent objective (see :func:`_shrink`).
    """
    project = interval.project
    settings = project.settings.induction
    state = IntervalState(project, [])
    start_fit = state.baseline_fit
    start_exact = _exact(state)
    assessed = sum(1 for dtt in state.baseline_distances if dtt is not None)

    steps: list[InductionStep] = []
    stopped = "converged"
    for _iteration in range(settings.max_rules_per_interval):
        if state.baseline_fit <= _EPSILON:
            stopped = "fit_zero"
            break
        fit_before, exact_before = state.baseline_fit, _exact(state)
        best = _best_candidate(
            state, project, settings,
            use_class=use_class, escape=escape, placement=placement,
        )
        if best is None:
            stopped = "converged"
            break
        candidate, index, score = best
        state.accept_at(candidate.rules[0], index)
        steps.append(
            InductionStep(
                definition=candidate.definition,
                delta_l=score.delta_l,
                delta_fit=score.delta_fit,
                rule_cost=score.rule_cost,
                improved=score.improved,
                moved=score.moved,
                fit_before=fit_before,
                fit_after=state.baseline_fit,
                exact_before=exact_before,
                exact_after=_exact(state),
                placement=index,
            )
        )
    else:
        stopped = "max_rules"

    # Shrink pass: drop any greedy rule a later one made redundant (plan §2.6). Re-derive the
    # kept cascade once so the reported final fit/exact reflect the pruned rule set.
    shrink_log: list[str] = []
    if shrink and len(state.rules) > 1:
        kept, shrink_log = _shrink(
            project, state.rules, bits_model(project), guard_exact=shrink_guards_exact
        )
        state = IntervalState(project, kept)

    return InducedInterval(
        label=interval.label,
        rules=list(state.rules),
        steps=steps,
        stopped=stopped,
        start_fit=start_fit,
        final_fit=state.baseline_fit,
        start_exact=start_exact,
        final_exact=_exact(state),
        assessed=assessed,
        shrink_log=shrink_log,
    )
