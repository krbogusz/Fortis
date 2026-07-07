"""Tests for the what-if rule preview (src/fortis/analysis/whatif.py).

Runs on the small default project (fast) — it has firing rules, assessed words, and
unassessed words, which is all the diff needs to exercise. Loads its *own* copy rather
than the shared ``project`` fixture, whose ``word.final`` values other tests mutate.
"""

import pytest

from src.fortis.analysis.whatif import render_whatif, try_rule, whatif_summary_line
from src.fortis.loaders.project import load_project


@pytest.fixture(scope="module")
def project():
    """A pristine default project, insulated from other tests' fixture mutations."""
    return load_project().unwrap()


class TestTryRule:
    def test_noop_candidate_touches_nothing(self, project):
        # No /q/ anywhere in the lexicon → the rule can never fire → zero delta.
        whatif = try_rule(project, "q → ʔ / _ #").unwrap()
        assert whatif.touched == 0
        assert whatif.net_exact_delta == 0
        assert whatif.improved == () and whatif.regressed == ()

    def test_parse_error_is_err(self, project):
        assert try_rule(project, "this is not a rule").is_err()

    def test_regression_is_detected(self, project):
        # a → e breaks words whose target keeps an /a/ they derived correctly.
        whatif = try_rule(project, "a → e").unwrap()
        assert whatif.regressed
        assert whatif.net_exact_delta < 0
        for change in whatif.regressed:
            assert change.candidate_distance is not None
            assert change.baseline_distance is not None
            assert change.candidate_distance > change.baseline_distance
            delta = change.delta
            assert delta is not None and delta > 0

    def test_unassessed_changes_bucketed_separately(self, project):
        # Words with no target that the rule moves land in `unassessed`, never in the
        # assessed buckets.
        whatif = try_rule(project, "a → e").unwrap()
        assert whatif.unassessed  # the default lexicon has bare (target-less) words
        for change in whatif.unassessed:
            assert change.target is None
        assessed = set(whatif.improved) | set(whatif.regressed) | set(whatif.lateral)
        assert assessed.isdisjoint(set(whatif.unassessed))

    def test_project_rules_are_not_mutated(self, project):
        before = {time: len(rules) for time, rules in project.rules.items()}
        try_rule(project, "a → e").unwrap()
        after = {time: len(rules) for time, rules in project.rules.items()}
        assert before == after


class TestRendering:
    def test_placement_time_is_surfaced(self, project):
        md = render_whatif(try_rule(project, "q → ʔ / _ #", time=500).unwrap(), "`proj`")
        assert "t=500" in md

    def test_untimed_placement_is_named(self, project):
        md = render_whatif(try_rule(project, "q → ʔ / _ #").unwrap(), "`proj`")
        assert "untimed" in md

    def test_noop_report_says_so(self, project):
        md = render_whatif(try_rule(project, "q → ʔ / _ #").unwrap(), "`proj`")
        assert "changed no word" in md

    def test_summary_line(self, project):
        line = whatif_summary_line(try_rule(project, "a → e").unwrap())
        assert "improved" in line and "regressed" in line
