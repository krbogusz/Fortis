"""Tests for project assembly (loaders/project.py)."""

from pathlib import Path

import pytest

from src.fortis.loaders.project import load_project

# A project dir with a lexicon: the PIE example has 'mother' (gloss) / 'meħˈteːr' (ipa).
_PIE = Path(__file__).resolve().parent.parent.parent / "projects" / "pie_to_germanic"


def test_word_scope_unknown_word_warns(tmp_path):
    # A `words` entry matching no word (by ipa or gloss) is a likely typo → warning,
    # not an error: the project still loads.
    rules = tmp_path / "rules.toml"
    rules.write_text('[r]\nwords = ["snu"]\ndefinition = "a → e"\n', encoding="utf-8")
    with pytest.warns(UserWarning, match="word-scope 'snu' matches no word"):
        result = load_project(_PIE, rules_path=rules)
    assert result.is_ok()


def test_word_scope_known_word_does_not_warn(tmp_path, recwarn):
    # Matching by gloss ('mother') or by ipa ('meħˈteːr') is fine — no word-scope warning.
    rules = tmp_path / "rules.toml"
    rules.write_text('[r]\nwords = ["mother", "meħˈteːr"]\ndefinition = "a → e"\n', encoding="utf-8")
    load_project(_PIE, rules_path=rules)
    assert not [w for w in recwarn if "word-scope" in str(w.message)]
