"""Tests for the induction.md report writer (src/fortis/induction/report.py)."""

from src.fortis.induction.boost import InducedInterval, InductionStep
from src.fortis.induction.report import (
    induction_summary_line,
    render_induced_rules,
    render_induction,
)
from src.fortis.loaders.rules import load_rule, load_rule_inventory


def _interval(synth) -> InducedInterval:
    rule = load_rule("r", {"definition": "o → u", "time": 0}, synth.features).unwrap()[0]
    step = InductionStep(
        definition="o → u", delta_l=-600.0, delta_fit=-640.0, rule_cost=40.0,
        improved=33, moved=33, fit_before=1000.0, fit_after=360.0,
        exact_before=53, exact_after=75, placement=-1,
    )
    return InducedInterval(
        label="750→1000", rules=[rule], steps=[step], stopped="converged",
        start_fit=1000.0, final_fit=360.0, start_exact=53, final_exact=75, assessed=299,
        shrink_log=["removed `x → y` (L 400 → 390, exact kept)"],
    )


class TestRender:
    def test_report_shows_the_iteration_and_shrink(self, synth):
        text = render_induction([_interval(synth)], "`synth`")
        assert "Interval `750→1000`" in text
        assert "`o → u`" in text
        assert "53 → 75 / 299 exact" in text
        assert "Shrink pass" in text
        assert "removed `x → y`" in text

    def test_summary_line_aggregates(self, synth):
        line = induction_summary_line([_interval(synth)])
        assert "induced 1 rule(s)" in line
        assert "53 → 75 / 299" in line

    def test_empty_interval_says_nothing_induced(self, synth):
        empty = InducedInterval(
            label="input→-200", rules=[], steps=[], stopped="fit_zero",
            start_fit=0.0, final_fit=0.0, start_exact=299, final_exact=299, assessed=299,
        )
        text = render_induction([empty], "`synth`")
        assert "nothing induced" in text.lower()


class TestSerialize:
    def test_induced_rules_toml_reloads(self, synth, tmp_path):
        from src.fortis.induction.refine import compose

        toml = render_induced_rules(compose([_interval(synth)], synth))
        path = tmp_path / "induced_rules.toml"
        path.write_text(toml, encoding="utf-8")
        reloaded = load_rule_inventory(path, synth.features)
        assert reloaded.is_ok()
        rules = [r for rs in reloaded.unwrap().values() for r in rs]
        assert rules[0].raw_definition == "o → u"

    def test_toml_escapes_quotes_and_backslashes(self, synth):
        from src.fortis.induction.report import _toml_string

        assert _toml_string('a "b" c') == '"a \\"b\\" c"'
        assert _toml_string("a\\b") == '"a\\\\b"'
