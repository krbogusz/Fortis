"""The rule dependency (feeding) graph, read from the actual firings."""
from pathlib import Path

from src.fortis.analysis.dependencies import (
    _change,
    build_dependency_graph,
    render_dependency_html,
)
from src.fortis.application.deriving import derive_all
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project


def _segs(string, project):
    return lower_tiers(string_to_sequence(string, project))


class TestChange:
    def test_consumes_the_old_segment_and_produces_the_new(self):
        project = load_project(None).unwrap()
        consumed, produced = _change(_segs("n̪", project), _segs("ŋ", project), project)
        assert consumed == {"n̪"}
        assert produced == {"ŋ"}

    def test_no_change_yields_nothing(self):
        project = load_project(None).unwrap()
        consumed, produced = _change(_segs("t̪", project), _segs("t̪", project), project)
        assert consumed == set() and produced == set()


class TestBuildGraph:
    def _graph(self):
        project = load_project(Path("projects/latin_to_french")).unwrap()
        from src.fortis.application.deriving import resolve_rule_letters
        rules = resolve_rule_letters(project.rules, project)
        return build_dependency_graph(derive_all(project), rules, project), project

    def test_velar_assimilation_feeds_the_palatalization_of_that_velar(self):
        # The user's example: n → ŋ makes the ŋ that ŋ → ɲ then matches.
        graph, _ = self._graph()
        by_name = {n.name: n for n in graph.nodes}
        source = by_name["n assimilates to a following velar stop"]
        target = by_name["ŋ palatalizes to ɲ before a coronal"]
        assert source.index in target.deps

    def test_edges_are_backward_and_depth_is_consistent(self):
        graph, _ = self._graph()
        for edge in graph.edges:
            assert edge.target < edge.source  # a dependency fired earlier
        for node in graph.nodes:
            expected = 0 if not node.deps else 1 + max(graph.nodes[d].depth for d in node.deps)
            assert node.depth == expected
        assert any(not n.deps for n in graph.nodes)  # some unconnected roots

    def test_html_is_self_contained(self):
        graph, _ = self._graph()
        html = render_dependency_html(graph)
        assert html.startswith("<!doctype html>")
        assert "feeding edges" in html
        assert "http" not in html.split("</head>")[0]  # no external resources
