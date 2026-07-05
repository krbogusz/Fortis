"""Tests for syllabification-fallback warnings (analysis/warnings.py).

Each project is assembled by ``load_project`` over a tmp dir that supplies only its
``syllable_parts.toml`` and ``words.toml``; everything else (features, letters, the
sonority scale) falls back to the shipped default per-file.
"""

from src.fortis.analysis.warnings import (
    render_warnings,
    syllabification_warnings,
    warnings_summary_line,
)
from src.fortis.application.deriving import derive_all
from src.fortis.loaders.project import load_project

# onset and coda each exactly one consonant → any interior cluster must be exactly two.
_STRICT_PARTS = (
    "[0]\n"
    'nucleus = { definition = "+syll" }\n'
    'onset   = { definition = "[-syll]" }\n'
    'coda    = { definition = "[-syll]" }\n'
)


def _project(tmp_path, parts: str, words: str):
    (tmp_path / "syllable_parts.toml").write_text(parts, encoding="utf-8")
    (tmp_path / "words.toml").write_text(words, encoding="utf-8")
    result = load_project(tmp_path)
    assert result.is_ok(), result.unwrap_err()
    return result.unwrap()


def test_unpatternable_cluster_warns(tmp_path):
    project = _project(tmp_path, _STRICT_PARTS, '"apta" = "ok"\n"astra" = "three"\n')
    warnings = syllabification_warnings(derive_all(project), project)
    by_ipa = {w.ipa: w for w in warnings}
    assert "apta" not in by_ipa  # pt splits legally (one coda + one onset)
    assert "astra" in by_ipa  # str is three consonants → no 1+1 split → sonority fallback
    astra = by_ipa["astra"]
    assert astra.clusters == ("str",)
    assert astra.syllabified == "as.tra"


def test_render_and_summary(tmp_path):
    project = _project(tmp_path, _STRICT_PARTS, '"astra" = "three"\n')
    warnings = syllabification_warnings(derive_all(project), project)
    md = render_warnings(warnings, "the test project")
    assert "three" in md and "`str`" in md and "as.tra" in md  # gloss, cluster, syllabified
    assert "fell back" in warnings_summary_line(warnings)


def test_no_patterns_never_warns(tmp_path):
    # With only a nucleus and no onset/coda patterns, sonority is always used — there is
    # no pattern to fail, so nothing "falls back".
    parts = '[0]\nnucleus = { definition = "+syll" }\n'
    project = _project(tmp_path, parts, '"astra" = "three"\n')
    assert syllabification_warnings(derive_all(project), project) == []
    assert warnings_summary_line([]) == "no syllabification warnings"


def test_render_empty(tmp_path):
    md = render_warnings([], "the test project")
    assert "No syllabification fell back" in md
