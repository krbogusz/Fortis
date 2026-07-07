"""Incremental candidate scoring: the append fast path (plan §2.3).

The boosting default places a candidate *after* every current interval rule, so its input is
each word's already-derived form. Scoring is then one ``apply_rule`` per word — no
re-derivation: ``cannot_match`` prunes most words for free (the identity contract makes a
non-firing sweep cheap), and only the words the candidate actually moves get re-assessed. This
is the whole reason the search is affordable — the candidate count never multiplies a full
derivation (plan §5).

The one correctness subtlety: ``apply_rule`` alone does not reproduce what ``derive`` threads
forward. After a rule fires, ``derive`` runs ``_maintain_tiers`` (prune dead links, OCP,
re-dock suprasegmentals to nuclei), and at the very end ``cleanup_tiers(surface=True)`` before
rendering. This module mirrors that tail exactly, and caches each word's **running form**
(pre-surface-cleanup) — appending to a surface-cleaned form would change results (stray-erased
floats a later rule would have docked). :class:`IntervalState.append_derivation` is proven
byte-identical to a real appended ``derive`` by ``tests/induction/test_evaluate.py``.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

from src.fortis.analysis.accuracy import DistanceToTarget, distance_to_target, ingest_words
from src.fortis.application.deriving import (
    _display_boundaries,
    _fired,
    _maintain_tiers,
    _resolve_rule,
    apply_rule,
    derive_all,
)
from src.fortis.application.tiers import cleanup_tiers, lower_tiers
from src.fortis.induction.objective import (
    BitsModel,
    PhoneCache,
    bits_model,
    residual_bits,
    rule_bits,
)
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule, RuleInventory


def timed_inventory(rules: list[Rule]) -> RuleInventory:
    """A rule inventory keying each rule to its list index — the interval's ordering (plan §2.4).

    Within an interval the inducer owns a plain ordered list; ``time`` keys are synthesized as
    the list index for evaluation runs, mapped to real times only at composition. One rule per
    index keeps the order strict.
    """
    return RuleInventory({index: (replace(rule, time=index),) for index, rule in enumerate(rules)})


@dataclass(frozen=True)
class AppendScore:
    """The result of scoring one candidate at the append placement.

    ``delta_l`` is the MDL change ``bits(r) + Δfit`` — negative means the candidate pays for
    itself. ``delta_fit`` is the fit-bits change alone; ``rule_cost`` the candidate's bits.
    ``improved``/``regressed`` count the words whose *residual bits* (the objective's own
    metric, not phone distance) fell/rose; ``moved`` counts every word the candidate changed.
    """

    delta_l: float
    delta_fit: float
    rule_cost: float
    improved: int
    regressed: int
    moved: int


class IntervalState:
    """Cached per-word derivations for one interval's current rule cascade.

    Holds the mini-project, the ordered induced-rule list, and the baseline derivations (with
    each word's residual bits) so a candidate can be scored by re-applying just that one rule
    to each word's cached running form. Rebuild — or call :meth:`accept` — when the cascade
    changes.
    """

    def __init__(self, project: Project, rules: list[Rule] | None = None) -> None:
        """Derive the baseline for *project* under *rules* (list order = application order)."""
        self.project = project
        self.rules: list[Rule] = list(rules or [])
        self.model: BitsModel = bits_model(project)
        self._phones: PhoneCache = {}
        ingest_words(project)  # segment the attested forms once; the shared words carry it forward
        self.baseline: list[Derivation] = self._derive_baseline()
        self.baseline_distances: list[DistanceToTarget | None] = [
            distance_to_target(d, project) for d in self.baseline
        ]
        # Per-word frequency-weighted residual bits, kept so a candidate that moves only a few
        # words re-scores just those (plan §5) — the running fit is a subtract/add, not a resum.
        self.baseline_residuals: list[float] = [
            self._residual(dtt) for dtt in self.baseline_distances
        ]
        self.baseline_fit: float = sum(self.baseline_residuals)

    # ---- baseline ----------------------------------------------------------------------

    def _derive_baseline(self) -> list[Derivation]:
        """Derive the mini-lexicon under the current induced rules (index-timed)."""
        return derive_all(replace(self.project, rules=timed_inventory(self.rules)))

    def _residual(self, dtt: DistanceToTarget | None) -> float:
        """One word's frequency-weighted residual bits (0 when it has no target)."""
        if dtt is None:
            return 0.0
        return dtt.frequency * residual_bits(dtt, self.project, self.model, self._phones)

    # ---- the append fast path ----------------------------------------------------------

    def _resolved(self, candidate: Rule) -> Rule:
        """The candidate with its letter runs resolved and its time set past every current rule."""
        placed = replace(candidate, time=len(self.rules))
        return _resolve_rule(placed, self.project)

    def append_derivation(self, base: Derivation, rule: Rule) -> Derivation:
        """The derivation that results from applying *rule* once after *base*'s cascade.

        *rule* must already be letter-resolved and timed past the cascade (see
        :meth:`_resolved`). Mirrors ``derive``'s per-rule tail — fire check, ``_maintain_tiers``,
        then the final surface ``cleanup_tiers`` — so the assessed surface is byte-identical to a
        real ``derive`` with *rule* genuinely appended. Returns *base* unchanged when the rule
        does not fire on this word (the common case, pruned cheaply by ``apply_rule``).
        """
        project = self.project
        pre = base.steps[-1].after if base.steps else base.input
        after = apply_rule(
            rule, pre, project.letters, project.features,
            project.sonorities, project.syllable_parts, project.tiers,
        )
        if after is pre or not _fired(lower_tiers(pre), lower_tiers(after)):
            return base  # no locus, or a vacuous match — surface unchanged
        after = _maintain_tiers(
            after, project.sonorities, project.syllable_parts, rule.time, project.letters,
            project.tiers,
        )
        step = DerivationStep(
            before=pre,
            rule=rule,
            after=after,
            before_boundaries=_display_boundaries(
                pre.bundles(), project.sonorities, project.syllable_parts, rule.time,
                project.letters,
            ),
            after_boundaries=_display_boundaries(
                after.bundles(), project.sonorities, project.syllable_parts, rule.time,
                project.letters,
            ),
        )
        # Mirror derive's tail: stray-erase floating autosegs, then display boundaries at the
        # latest rule-time (the appended rule's, which is the largest).
        surface = cleanup_tiers(after.copy(), project.tiers, surface=True)
        surface_boundaries = _display_boundaries(
            surface.bundles(), project.sonorities, project.syllable_parts, rule.time,
            project.letters,
        )
        return Derivation(
            word=base.word,
            input=base.input,
            steps=(*base.steps, step),
            surface=surface,
            surface_boundaries=surface_boundaries,
        )

    def score_append(self, candidate: Rule) -> AppendScore:
        """Score *candidate* at the append placement, returning the exact MDL change ``ΔL``.

        One ``apply_rule`` per word against the cached derivations; only moved words are
        re-assessed. The returned ``delta_l`` is exact for *this* placement (plan §2.3).
        """
        resolved = self._resolved(candidate)
        delta_fit = 0.0
        improved = regressed = moved = 0
        # A non-moved word contributes 0 to Δfit (its residual is already in baseline_fit), so
        # only the moved words are re-assessed — the incremental scoring the fast path exists for.
        # "improved"/"regressed" count a word by whether its *residual bits* fell or rose — the
        # objective's own metric, not phone distance. This matters: a feature-shift toward the
        # target (ɛ→e when the target is i) lowers residual bits with the phone distance
        # unchanged (objective §1.1), so a phone-distance gate would reject the very candidates
        # the objective rewards, and the loop would converge early on the hard, gradient-shaped
        # steps. The count still serves the anti-overfitting floor: a candidate must genuinely
        # help ``min_improved_words`` words to be accepted.
        for index, base in enumerate(self.baseline):
            new_deriv = self.append_derivation(base, resolved)
            if new_deriv is base:
                continue
            moved += 1
            old_residual = self.baseline_residuals[index]
            new_residual = self._residual(distance_to_target(new_deriv, self.project))
            delta_fit += new_residual - old_residual
            if new_residual < old_residual:
                improved += 1
            elif new_residual > old_residual:
                regressed += 1
        rule_cost = rule_bits(candidate, self.project, self.model)
        return AppendScore(
            delta_l=rule_cost + delta_fit,
            delta_fit=delta_fit,
            rule_cost=rule_cost,
            improved=improved,
            regressed=regressed,
            moved=moved,
        )

    def score_at(self, candidate: Rule, index: int) -> AppendScore:
        """Score *candidate* spliced in at position *index* (not just appended).

        Feeding/bleeding means the append slot is not always the right one (plan §2.3). This
        splices the candidate into the rule list at *index* and re-derives the whole
        mini-lexicon — the same ``timed_inventory`` → ``derive_all`` path the append fast path
        is proven byte-identical to, so it is correct by construction (the reindex *is* the
        splice). Slower than :meth:`score_append` (a full mini-run), so the caller reserves it
        for the top append-ranked finalists. ``index == len(rules)`` reduces to an append.
        """
        if index == len(self.rules):
            return self.score_append(candidate)
        spliced = self.rules[:index] + [candidate] + self.rules[index:]
        derivations = derive_all(replace(self.project, rules=timed_inventory(spliced)))
        new_fit = 0.0
        improved = regressed = moved = 0
        for base, base_residual, derivation in zip(
            self.baseline, self.baseline_residuals, derivations, strict=True
        ):
            new_grade = distance_to_target(derivation, self.project)
            new_residual = self._residual(new_grade)
            new_fit += new_residual
            if base.surface != derivation.surface:
                moved += 1
            if new_residual < base_residual:
                improved += 1
            elif new_residual > base_residual:
                regressed += 1
        rule_cost = rule_bits(candidate, self.project, self.model)
        return AppendScore(
            delta_l=rule_cost + (new_fit - self.baseline_fit),
            delta_fit=new_fit - self.baseline_fit,
            rule_cost=rule_cost,
            improved=improved,
            regressed=regressed,
            moved=moved,
        )

    def accept(self, candidate: Rule) -> None:
        """Commit *candidate* to the end of the cascade and refresh the cached baseline.

        Advances the cached derivations by the proven fast path rather than re-deriving from
        scratch — byte-identical (see the equivalence test), and O(one sweep) instead of a full
        mini-run per acceptance.
        """
        resolved = self._resolved(candidate)
        self.rules.append(candidate)
        self.baseline = [self.append_derivation(base, resolved) for base in self.baseline]
        self.baseline_distances = [distance_to_target(d, self.project) for d in self.baseline]
        self.baseline_residuals = [self._residual(dtt) for dtt in self.baseline_distances]
        self.baseline_fit = sum(self.baseline_residuals)

    def accept_at(self, candidate: Rule, index: int) -> None:
        """Commit *candidate* at position *index*, refreshing the cached baseline.

        An append (``index == len(rules)``) uses the fast path; a genuine insert rebuilds the
        cascade with one full mini-run — correct and cheap, since acceptance is rare (only the
        winner). Preserving the fast path through an arbitrary insert is where a bug would hide.
        """
        if index == len(self.rules):
            self.accept(candidate)
            return
        self.rules.insert(index, candidate)
        self.baseline = self._derive_baseline()
        self.baseline_distances = [distance_to_target(d, self.project) for d in self.baseline]
        self.baseline_residuals = [self._residual(dtt) for dtt in self.baseline_distances]
        self.baseline_fit = sum(self.baseline_residuals)
