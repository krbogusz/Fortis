"""CLI for the rule inducer: recover a rule cascade from a project's attested targets.

Loads a project, induces each stage interval's rules under teacher forcing (Phase A), composes
them into one real-time cascade, and writes ``induced_rules.toml`` (a loadable rules file) and
``induction.md`` (the per-interval trace). It then reports the *composed* accuracy — the induced
cascade run from the true inputs over the whole lexicon — against the identity and hand
baselines. Run::

    python -m src.fortis.induction.main --project projects/latin_to_french

``--ignore-stages`` induces a single ``input→final`` interval instead (the ablation, §3.5);
``--interval T1:T2`` runs one span (``T1``/``T2`` may be ``input``/``final`` or a stage time).
"""
from __future__ import annotations

import argparse
import sys
import time
from dataclasses import replace
from pathlib import Path

from src.fortis.analysis.accuracy import ingest_targets, measure_accuracy
from src.fortis.application.deriving import derive_all_parallel
from src.fortis.config import config
from src.fortis.induction.refine import induce_project, refine, refine_localized
from src.fortis.induction.report import (
    induction_summary_line,
    render_induced_rules,
    render_induction,
)
from src.fortis.loaders.project import load_project
from src.fortis.models.rules import RuleInventory


def _parse_endpoint(token: str) -> int | None:
    """One side of ``--interval``: ``input``/``final`` → ``None``, else a stage time."""
    if token in ("input", "final", ""):
        return None
    return int(token)


def _parse_interval(spec: str) -> tuple[int | None, int | None]:
    """Parse ``T1:T2`` into an interval endpoint pair."""
    start, _, end = spec.partition(":")
    return _parse_endpoint(start), _parse_endpoint(end)


def _accuracy(
    project, inventory: RuleInventory, *, serial: bool, workers: int | None
) -> tuple[int, int, float]:
    """Composed accuracy: derive the whole lexicon from true inputs under *inventory* and measure.

    Returns ``(exact, assessed, mean_distance)`` against each word's attested ``final``.
    """
    runnable = replace(project, rules=inventory)
    derivations = derive_all_parallel(runnable, workers=1 if serial else workers)
    ingest_targets(derivations, runnable)  # parallel returns word copies; ingest those
    report = measure_accuracy(derivations, runnable)
    return report.exact, report.assessed, report.mean_distance


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fortis-induce",
        description="Induce a sound-change cascade from a project's attested targets.",
    )
    parser.add_argument("--project", type=Path, metavar="DIR", help="a project directory")
    parser.add_argument(
        "--out", type=Path, metavar="FILE",
        help="path for the induced rules (default: <project>/induced_rules.toml)",
    )
    parser.add_argument(
        "--report", type=Path, metavar="FILE",
        help="path for the trace report (default: <project>/induction.md)",
    )
    parser.add_argument(
        "--ignore-stages", action="store_true",
        help="induce a single input→final interval, ignoring intermediate stages (ablation)",
    )
    parser.add_argument(
        "--interval", metavar="T1:T2",
        help="induce only this interval (T1/T2 may be 'input'/'final' or a stage time)",
    )
    parser.add_argument(
        "--max-rules", type=int, metavar="N", help="override max_rules_per_interval",
    )
    parser.add_argument(
        "--refine", action="store_true",
        help="run Phase-B global refinement (shrink + final-residual boosting) — slower",
    )
    parser.add_argument(
        "--refine-localized", action="store_true",
        help="run Phase-B localized refinement (correct each attested stage in place) — slowest",
    )
    parser.add_argument("--serial", action="store_true", help="derive in a single process")
    parser.add_argument("--workers", type=int, default=None, metavar="N", help="worker count")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Induce a project's cascade, write the outputs, and report composed accuracy."""
    args = _parse_args(argv)
    result = load_project(args.project)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()
    if args.max_rules is not None:
        induction = replace(project.settings.induction, max_rules_per_interval=args.max_rules)
        project = replace(project, settings=replace(project.settings, induction=induction))

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"
    only = _parse_interval(args.interval) if args.interval else None

    start = time.perf_counter()
    induction = induce_project(project, ignore_stages=args.ignore_stages, only_interval=only)
    inventory = induction.inventory
    trace = None
    workers = 1 if args.serial else args.workers
    if args.refine_localized:
        inventory, trace = refine_localized(project, inventory, workers=workers)
        print(f"Phase B (localized): added {len(trace.added)} rule(s)", file=sys.stderr)
    elif args.refine:
        inventory, trace = refine(project, inventory, workers=workers)
        print(
            f"Phase B: removed {len(trace.removed)}, added {len(trace.added)} rule(s)",
            file=sys.stderr,
        )
    elapsed = time.perf_counter() - start

    output_dir = args.project or config.paths.default
    out_path = args.out or output_dir / "induced_rules.toml"
    out_path.write_text(render_induced_rules(inventory), encoding="utf-8")
    report_path = args.report or output_dir / "induction.md"
    report_path.write_text(render_induction(induction.intervals, where, trace), encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)
    print(f"wrote {report_path}", file=sys.stderr)
    print(induction_summary_line(induction.intervals))

    # Composed accuracy from the true inputs over the whole lexicon.
    exact, assessed, mean = _accuracy(
        project, inventory, serial=args.serial, workers=args.workers
    )
    rules = sum(len(rs) for rs in inventory.values())
    print(
        f"composed cascade: {exact}/{assessed} exact (mean phone dist {mean:.3f}) "
        f"with {rules} induced rules · induced in {elapsed:.0f}s",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
