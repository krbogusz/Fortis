"""Tests for the M0 scoreboard (src/fortis/induction/scoreboard.py)."""

import pytest

from src.fortis.induction.objective import CascadeScore
from src.fortis.induction.scoreboard import (
    Scoreboard,
    compute_scoreboard,
    render_scoreboard,
    scoreboard_summary_line,
)


def _fake(fit: float, rule: float, exact: int) -> CascadeScore:
    return CascadeScore(fit_bits=fit, rule_bits=rule, exact=exact, assessed=100, mean_distance=0.0)


class TestRender:
    def test_reports_the_gap_and_floor(self):
        board = Scoreboard(
            real_identity=_fake(200.0, 0.0, 0),
            real_hand=_fake(30.0, 45.0, 88),
            synthetic_identity=_fake(190.0, 0.0, 0),
            synthetic_hand=_fake(0.0, 45.0, 100),
        )
        assert board.real_gap == pytest.approx(200.0 - 75.0)
        text = render_scoreboard(board, "`x`")
        assert "L(identity) − L(hand) = 125 bits" in text
        assert "learnability floor" in text.lower()
        assert "real · hand" in text
        assert "L(identity)" in scoreboard_summary_line(board)


class TestIntegration:
    def test_scoreboard_invariants(self, synth):
        board = compute_scoreboard(synth, serial=True)
        # Hand cascade fits far better and wins on total loss despite its rule cost.
        assert board.real_hand.total < board.real_identity.total
        assert board.real_gap > 0
        # The learnability floor: the hand cascade regenerates its own synthetic lexicon.
        assert board.synthetic_hand.fit_bits == pytest.approx(0.0)
        assert board.synthetic_hand.exact == board.synthetic_hand.assessed
        # Identity fits nothing.
        assert board.real_identity.exact == 0
        assert board.real_identity.rule_bits == 0.0
