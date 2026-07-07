"""The M0 scoreboard: ``L`` of the identity cascade vs the hand cascade, real and synthetic.

This is the number §8's M0 milestone delivers and every later milestone reads — the fixed
reference the inducer's output is assessed against. For a project it reports four cascade scores:

- **identity** (no rules) and **hand** (the project's own rules) on the **real** lexicon, and
- the same two on the **synthetic** lexicon (the hand cascade's own output — the learnability
  floor where the hand cascade must score ``fit_bits`` 0).

The gap ``L(identity) − L(hand)`` is the loss the rules buy; an inducer is doing well when its
own cascade closes a large fraction of it. Run::

    python -m src.fortis.induction.scoreboard --project projects/latin_to_french
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, replace
from pathlib import Path

from src.fortis.application.deriving import derive_all_parallel
from src.fortis.induction.intervals import synthetic_project
from src.fortis.induction.objective import CascadeScore, cascade_score
from src.fortis.loaders.project import load_project
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory


@dataclass(frozen=True)
class Scoreboard:
    """The four reference scores for a project: {identity, hand} × {real, synthetic}."""

    real_identity: CascadeScore
    real_hand: CascadeScore
    synthetic_identity: CascadeScore
    synthetic_hand: CascadeScore

    @property
    def real_gap(self) -> float:
        """Loss the hand rules buy on the real lexicon: ``L(identity) − L(hand)``."""
        return self.real_identity.total - self.real_hand.total


def _score(project: Project, *, workers: int | None, serial: bool) -> CascadeScore:
    """Derive *project* (serial or fanned across processes) and score the whole cascade."""
    derivations = derive_all_parallel(project, workers=1 if serial else workers)
    return cascade_score(derivations, project)


def compute_scoreboard(
    project: Project, *, workers: int | None = None, serial: bool = False
) -> Scoreboard:
    """Compute the identity/hand scores on both the real and the synthetic lexicon."""
    identity = replace(project, rules=RuleInventory())
    synth = synthetic_project(project)
    synth_identity = replace(synth, rules=RuleInventory())
    return Scoreboard(
        real_identity=_score(identity, workers=workers, serial=serial),
        real_hand=_score(project, workers=workers, serial=serial),
        synthetic_identity=_score(synth_identity, workers=workers, serial=serial),
        synthetic_hand=_score(synth, workers=workers, serial=serial),
    )


def _row(label: str, score: CascadeScore) -> str:
    return (
        f"| {label:<20} | {score.fit_bits:12,.0f} | {score.rule_bits:10,.0f} "
        f"| {score.total:12,.0f} | {score.exact:>4}/{score.assessed:<4} "
        f"| {score.mean_distance:6.3f} |"
    )


def render_scoreboard(board: Scoreboard, where: str) -> str:
    """A Markdown table of the four reference scores, plus the loss the rules buy."""
    lines = [
        f"# Induction scoreboard — {where}",
        "",
        "The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the",
        "hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own",
        "output — the learnability floor, where its residual is zero). Every later induction",
        "milestone is assessed against these numbers.",
        "",
        "| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        _row("real · identity", board.real_identity),
        _row("real · hand", board.real_hand),
        _row("synthetic · identity", board.synthetic_identity),
        _row("synthetic · hand", board.synthetic_hand),
        "",
        f"**Loss the hand rules buy on real data:** L(identity) − L(hand) = "
        f"{board.real_gap:,.0f} bits.",
        "",
        f"**Learnability floor:** the hand cascade's synthetic `fit_bits` is "
        f"{board.synthetic_hand.fit_bits:.3g} (target 0).",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def scoreboard_summary_line(board: Scoreboard) -> str:
    """A one-line headline for stderr."""
    return (
        f"real: L(identity)={board.real_identity.total:,.0f} → "
        f"L(hand)={board.real_hand.total:,.0f} "
        f"(rules buy {board.real_gap:,.0f} bits); "
        f"synthetic hand fit={board.synthetic_hand.fit_bits:.3g}"
    )


def main(argv: list[str] | None = None) -> None:
    """Load a project, compute the scoreboard, and write ``induction_scoreboard.md``."""
    parser = argparse.ArgumentParser(
        prog="fortis-induction-scoreboard",
        description="Report L of the identity vs hand cascade, on real and synthetic data.",
    )
    parser.add_argument("--project", type=Path, metavar="DIR", help="a project directory")
    parser.add_argument(
        "--output", type=Path, metavar="FILE",
        help="path for the report (default: <project>/induction_scoreboard.md)",
    )
    parser.add_argument("--serial", action="store_true", help="derive in a single process")
    parser.add_argument("--workers", type=int, default=None, metavar="N", help="worker count")
    args = parser.parse_args(argv)

    result = load_project(args.project)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()

    board = compute_scoreboard(project, workers=args.workers, serial=args.serial)
    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"
    from src.fortis.config import config

    output_dir = args.project or config.paths.default
    path = args.output or output_dir / "induction_scoreboard.md"
    path.write_text(render_scoreboard(board, where), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    print(scoreboard_summary_line(board))


if __name__ == "__main__":
    main()
