"""Per-project tunable parameters (``settings.toml``).

Everything here is a knob a project may set to tune the *analysis* layer without
touching the engine — accuracy and error diagnosis. The field defaults on these
dataclasses are the single source of truth: a project that ships no ``settings.toml``
(or omits a key) gets exactly these values, and ``projects/default/settings.toml`` is
just a documented mirror of them (a test pins the two together).
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AccuracySettings:
    """Knobs for the edit-distance grader (:mod:`src.fortis.analysis.accuracy`)."""

    # Cost of swapping two adjacent segments (a metathesis) in the Damerau–Levenshtein
    # distance. 1 charges a reorder as one edit; raise it (e.g. 2) to score a metathesis
    # as two substitutions instead.
    transposition_cost: int = 1


@dataclass(frozen=True)
class DiagnosisSettings:
    """Knobs for the error diagnosis (:mod:`src.fortis.analysis.diagnosis`)."""

    # A context predictor is trusted in the autopsy only if it clears the support floor:
    # present in at least ``max(min_support, ceil(min_support_percent% of the focus phone's
    # occurrences))`` positions. ``min_support`` is the absolute floor (phi is near ±1 at a
    # two-or-three-count cell); ``min_support_percent`` scales the floor with the word base,
    # so a predictor covering a trivial fraction of a common phone is dropped as noise.
    min_support: int = 3
    min_support_percent: int = 10
    # A focus phone is autopsied only if it came out wrong at least this many times.
    min_errors: int = 2
    # How many predictors to show per phone in the report (the most error-associated).
    report_top: int = 8
    # How many of the top confusions' focus phones to run a context autopsy on.
    focus_count: int = 5


@dataclass(frozen=True)
class InductionSettings:
    """Knobs for supervised rule induction (:mod:`src.fortis.induction`).

    These steer the *search*, not the objective: the MDL bits constants that price fit
    against rule cost (``B_rule``, ``b_tag``) are module constants in
    :mod:`src.fortis.induction.objective`, deliberately *not* settings — moving
    them changes the objective itself, a research act rather than per-project tuning.
    """

    # A candidate must strictly improve at least this many words to be accepted, on top of
    # the MDL criterion — a floor against a rule that only helps one incidental word.
    min_improved_words: int = 2
    # How many of the top residual confusions to expand into candidates per iteration.
    top_confusions: int = 5
    # Candidate cap per confusion (contexts × class/indel variants).
    contexts_per_confusion: int = 25
    # Candidates (ranked by append-ΔL) that get the full placement search.
    placement_candidates: int = 5
    # Iteration cap per interval, a runaway-loop backstop.
    max_rules_per_interval: int = 60
    # Words beyond this alignment distance don't feed the correspondence tallies (their
    # alignments are unreliable); they still count in the loss.
    alignment_distance_cap: int = 4
    # Weight on the final checkpoint relative to intermediate stages; lower it for a project
    # whose intermediate notation is only loosely comparable to the engine's output.
    final_weight: float = 1.0


@dataclass(frozen=True)
class Settings:
    """A project's tunable parameters, grouped by the layer they steer."""

    accuracy: AccuracySettings = field(default_factory=AccuracySettings)
    diagnosis: DiagnosisSettings = field(default_factory=DiagnosisSettings)
    induction: InductionSettings = field(default_factory=InductionSettings)
