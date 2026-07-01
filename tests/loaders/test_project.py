"""Tests for project assembly (loaders/project.py)."""

from pathlib import Path

import pytest

from src.fortis.loaders.project import load_project

# A project dir with a lexicon: the Old Chinese example has 'sun' (gloss) / 'ˈnjit' (ipa).
_OC = Path(__file__).resolve().parent.parent.parent / "projects" / "old_chinese"


def test_word_scope_unknown_word_warns(tmp_path):
    # A `words` entry matching no word (by ipa or gloss) is a likely typo → warning,
    # not an error: the project still loads.
    rules = tmp_path / "rules.toml"
    rules.write_text('[r]\nwords = ["snu"]\ndefinition = "a → e"\n', encoding="utf-8")
    with pytest.warns(UserWarning, match="word-scope 'snu' matches no word"):
        result = load_project(_OC, rules_path=rules)
    assert result.is_ok()


def test_word_scope_known_word_does_not_warn(tmp_path, recwarn):
    # Matching by gloss ('sun') or by ipa ('ˈnjit') is fine — no word-scope warning.
    rules = tmp_path / "rules.toml"
    rules.write_text('[r]\nwords = ["sun", "ˈnjit"]\ndefinition = "a → e"\n', encoding="utf-8")
    load_project(_OC, rules_path=rules)
    assert not [w for w in recwarn if "word-scope" in str(w.message)]
