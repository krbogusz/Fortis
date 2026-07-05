"""Per-project tunable parameters (``settings.toml``).

Everything here is a knob a project may set to tune the *analysis* layer without
touching the engine — grading and error diagnosis. The field defaults on these
dataclasses are the single source of truth: a project that ships no ``settings.toml``
(or omits a key) gets exactly these values, and ``projects/default/settings.toml`` is
just a documented mirror of them (a test pins the two together).
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class GradingSettings:
    """Knobs for the edit-distance grader (:mod:`src.fortis.analysis.grading`)."""

    # Cost of swapping two adjacent segments (a metathesis) in the Damerau–Levenshtein
    # distance. 1 charges a reorder as one edit; raise it (e.g. 2) to score a metathesis
    # as two substitutions instead.
    transposition_cost: int = 1


@dataclass(frozen=True)
class DiagnosisSettings:
    """Knobs for the error diagnosis (:mod:`src.fortis.analysis.diagnosis`)."""

    # A context predictor is trusted in the autopsy only if present in at least this many
    # of the focus phone's positions (phi is near ±1 at a two-or-three-count cell).
    min_support: int = 3
    # A focus phone is autopsied only if it came out wrong at least this many times.
    min_errors: int = 2
    # How many predictors to show per phone in the report (the most error-associated).
    report_top: int = 8
    # How many of the top confusions' focus phones to run a context autopsy on.
    focus_count: int = 5


@dataclass(frozen=True)
class Settings:
    """A project's tunable parameters, grouped by the layer they steer."""

    grading: GradingSettings = field(default_factory=GradingSettings)
    diagnosis: DiagnosisSettings = field(default_factory=DiagnosisSettings)
