"""Tests for syllabification-fallback warnings (analysis/warnings.py).

Each project is assembled by ``load_project`` over a tmp dir that supplies only its
``syllable_parts.toml`` and ``words.toml``; everything else (features, letters, the
sonority scale) falls back to the shipped default per-file.
"""

from src.fortis.analysis.warnings import (
    render_warnings,
    rendering_warnings,
    syllabification_warnings,
    warnings_summary_line,
)
from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import sequence_to_string
from src.fortis.application.tiers import lower_tiers
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
    assert astra.form == "astra"  # the exact (unsyllabified) form the warning fired on
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
    assert warnings_summary_line([]) == "no warnings"


def test_render_empty(tmp_path):
    md = render_warnings([], "the test project")
    assert "No syllabification fell back" in md


# ── Unspellable segments ────────────────────────────────────────────────────────────────
#
# The engine's one otherwise-invisible failure: a rule whose merge changes a segment's quality
# but leaves a feature of the old quality behind. A merge keeps every feature it does not
# mention, so the result is a segment that is ALMOST a letter — and the renderer used to spell
# it as that letter, dropping the difference. It then looked identical to the real letter in
# every report while matching no rule written against it, because letter patterns match by
# exact identity. Now it renders as � and warns, naming the near-miss letter and the culprit.


def _leaky_project(tmp_path, definition: str, words: str = '"o" = "oh"\n'):
    """A project whose one rule un-rounds /o/ — completely or otherwise.

    /o/ is [+rounded, +labial]; the letter ɤ is exactly /o/ without BOTH. So clearing only
    `rounded` lands one feature short of a real letter, and clearing both lands on it.
    """
    (tmp_path / "rules.toml").write_text(
        "[unround]\ntime = 0\nname = \"un-round o\"\n"
        f'definition = "{definition}"\n',
        encoding="utf-8",
    )
    (tmp_path / "words.toml").write_text(words, encoding="utf-8")
    result = load_project(tmp_path)
    assert result.is_ok(), result.unwrap_err()
    return result.unwrap()


def test_leaky_merge_renders_replacement_and_warns(tmp_path):
    # Clearing `rounded` but not `labial` leaves a segment that is the letter ɤ plus a stray
    # `labial` — it is NOT ɤ, and must not be spelt as one.
    project = _leaky_project(tmp_path, "[+syll, +rounded] → [rounded: none]")
    derivations = derive_all(project)
    warnings = rendering_warnings(derivations, project)
    assert len(warnings) == 1
    warning = warnings[0]
    assert warning.dropped == ("labial",)  # the feature no letter can express
    assert warning.nearest == "ɤ"  # what it will be MISTAKEN for
    assert warning.rule == "un-round o"  # and who to blame
    # The surface says so out loud rather than lying with a plausible ɑ.
    assert "�" in sequence_to_string(lower_tiers(derivations[0].surface), project)


def test_complete_merge_leaves_no_residue(tmp_path):
    # The same rule, clearing `labial` too: now the result really IS the letter ɤ.
    project = _leaky_project(tmp_path, "[+syll, +rounded] → [rounded: none, labial: none]")
    derivations = derive_all(project)
    assert rendering_warnings(derivations, project) == []
    assert sequence_to_string(lower_tiers(derivations[0].surface), project) == "ɤ"


def test_rendering_warning_reaches_the_report_and_summary(tmp_path):
    project = _leaky_project(tmp_path, "[+syll, +rounded] → [rounded: none]")
    warnings = rendering_warnings(derive_all(project), project)
    md = render_warnings([], "the test project", warnings)
    assert "Unspellable segments" in md
    assert "`ɤ`" in md and "`labial`" in md and "`un-round o`" in md
    line = warnings_summary_line([], warnings)
    assert "unspellable" in line and "labial" in line and "un-round o" in line


def test_blame_is_the_rule_that_produced_it_not_the_ones_that_carried_it(tmp_path):
    # A second rule that merely lengthens the already-broken segment must not be blamed for it:
    # the fix belongs in the merge that leaked the feature, not in every later rule that touches
    # the segment (changing any feature makes the bundle look "new").
    (tmp_path / "rules.toml").write_text(
        '[unround]\ntime = 0\nname = "un-round o"\n'
        'definition = "[+syll, +rounded] → [rounded: none]"\n'
        "\n"
        '[lengthen]\ntime = 100\nname = "lengthen it"\n'
        'definition = "[+syll] → [length: long]"\n',
        encoding="utf-8",
    )
    (tmp_path / "words.toml").write_text('"o" = "oh"\n', encoding="utf-8")
    project = load_project(tmp_path).unwrap()
    warnings = rendering_warnings(derive_all(project), project)
    assert {w.rule for w in warnings} == {"un-round o"}  # not "lengthen it"
