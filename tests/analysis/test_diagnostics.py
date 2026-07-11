"""Tests for the diagnostics tools (src/fortis/analysis/diagnostics.py).

Covers the match-set query and the unsatisfiable-bundle check.
"""

from pathlib import Path

from src.fortis.analysis.diagnostics import _contradiction, match_set, unsatisfiable_rules
from src.fortis.loaders.project import load_project
from src.fortis.parsing.bundles import parse_pattern_bundle


def _project():
    return load_project(Path("projects/default")).unwrap()


def test_match_set_returns_the_engines_denotation_of_a_bundle():
    # The whole point: the answer is the engine's own match, so a bundle's real reach is visible.
    proj = _project()
    result = match_set("+nasal", proj).unwrap()
    assert result.total == len(proj.letters)
    assert "m" in result.matched and "n" in result.matched and "ŋ" in result.matched
    assert "p" not in result.matched  # a plain oral stop is not nasal
    # inventory order is preserved (not sorted), so it reads like the letters file
    assert result.matched == [s for s in proj.letters if s in result.matched]


def test_coronal_front_overlap_is_surfaced_not_hidden():
    # The canonical feature-system surprise: [+front] is the coronal place node too, so a bundle
    # meaning "front glide/sonorant" also catches every coronal. The tool must show that.
    proj = _project()
    matched = match_set("+front, +sonorant, -syllabic", proj).unwrap().matched
    assert {"n", "l", "r", "j"} <= set(matched)  # coronals AND the palatal glide, together


def test_brackets_are_optional():
    proj = _project()
    bracketed = match_set("[+nasal]", proj).unwrap().matched
    assert bracketed == match_set("+nasal", proj).unwrap().matched


def test_empty_input_is_a_friendly_error():
    assert match_set("   ", _project()).unwrap_err().startswith("Enter a feature bundle")


def test_unknown_feature_surfaces_the_parse_error_as_a_string():
    err = match_set("+bogus", _project()).unwrap_err()
    assert isinstance(err, str) and "bogus" in err


def test_rule_only_specs_are_rejected_with_a_clear_message():
    # References, agreement variables, and conditionals silently match all-or-nothing without a
    # rule's bindings, so they are rejected up front rather than returning a misleading set.
    proj = _project()
    cases = [("oral: ~1", "oral"), ("αvoice", "voice"), ("<1: aperture: high>", "aperture")]
    for query, offender in cases:
        err = match_set(query, proj).unwrap_err()
        assert "inside a rule" in err and offender in err


# --- unsatisfiable-bundle check -------------------------------------------------------------


def _contradicts(raw):
    proj = _project()
    return _contradiction(parse_pattern_bundle(raw, proj.features).unwrap(), proj.features)


def test_child_present_under_absent_ancestor_is_unsatisfiable():
    # front → lingual → oral: requiring front present while removing an ancestor node can never
    # match, at any depth of the geometry chain.
    assert _contradicts("front, oral: none") is not None  # front under lingual under oral
    assert _contradicts("labial, oral: none") is not None
    assert _contradicts("front, lingual: none") is not None  # immediate parent
    assert _contradicts("+voice, glottal: none") is not None  # voice under glottal


def test_independent_node_absence_is_satisfiable():
    # nasal hangs off root, not oral, so removing oral does not contradict a present nasal.
    assert _contradicts("+nasal, oral: none") is None
    assert _contradicts("front, lingual") is None  # both present — consistent
    assert _contradicts("aperture: high") is None


def test_real_projects_have_no_unsatisfiable_rules():
    for name in ["default", "halle_vaux_wolfe", "spe", "latin_to_french"]:
        proj = load_project(Path(f"projects/{name}")).unwrap()
        assert unsatisfiable_rules(proj) == []


def test_unsatisfiable_rule_is_reported_with_rule_and_reason(tmp_path):
    (tmp_path / "words.toml").write_text('"anpa" = "w"\n')
    (tmp_path / "rules.toml").write_text(
        '[bad]\nwords = ["w"]\n'
        'definition = "[+nasal] -> [oral: ~1] / _ [+consonantal, front, oral: none]"\n'
    )
    proj = load_project(tmp_path).unwrap()
    findings = unsatisfiable_rules(proj)
    assert len(findings) == 1
    (f,) = findings
    assert f.rule == "bad" and f.role == "right context"
    assert "front is required present" in f.reason and "oral" in f.reason
