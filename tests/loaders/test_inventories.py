"""Tests for the top-level project loader (integration)."""

import pytest

from src.fortis.loaders.project import load_project

FEATURES_TOML = """\
[consonantal]
tier = "segment"
kind = "binary"
short = "cons"

[sonorant]
tier = "segment"
kind = "binary"
short = "son"

[syllabic]
tier = "segment"
kind = "binary"
short = "syll"
"""

LETTERS_CSV = "symbol,consonantal,sonorant\nm,+,+\n"

DIACRITICS_TOML = '"̩" = { tier = "segment", kind = "combining", bundle = "+syll" }\n'

SONORITIES_TOML = (
    'vowel = { level = 7, bundle = "+syllabic" }\nstop = { level = 1, bundle = "-sonorant" }\n'
)

SYLLABLE_PARTS_TOML = '[-2000]\nnucleus = { definition = "+syll" }\n'

WORDS_TOML = '"xenti" = "in front"\n'

RULES_TOML = """\
[test_rule]
time = -2000
definition = "m → n"
"""


def _write_inventory_files(tmp_path):
    (tmp_path / "features.toml").write_text(FEATURES_TOML)
    (tmp_path / "letters.csv").write_text(LETTERS_CSV)
    (tmp_path / "diacritics.toml").write_text(DIACRITICS_TOML)
    (tmp_path / "sonorities.toml").write_text(SONORITIES_TOML)
    (tmp_path / "syllable_parts.toml").write_text(SYLLABLE_PARTS_TOML)
    (tmp_path / "words.toml").write_text(WORDS_TOML)
    (tmp_path / "rules.toml").write_text(RULES_TOML)
    # This fixture's minimal feature set has no tone/stress, so it declares its own (empty)
    # tiers rather than inheriting the shipped tone/stress tiers via fall-back.
    (tmp_path / "tiers.toml").write_text("# no autosegmental tiers\n")


class TestLoadProject:
    def test_full_load(self, tmp_path):
        _write_inventory_files(tmp_path)
        result = load_project(tmp_path)
        assert result.is_ok(), f"Errors: {result.unwrap_err() if result.is_err() else None}"
        project = result.unwrap()
        assert "consonantal" in project.features
        assert "m" in project.letters
        assert "̩" in project.diacritics
        assert "vowel" in project.sonorities
        assert -2000 in project.syllable_parts
        assert "xenti" in project.words

    # Falls back to the (word-scoped) default showcase rules, which don't match these test
    # words — that "rule will never fire" warning is correct here and not what we're testing.
    @pytest.mark.filterwarnings("ignore::UserWarning")
    def test_missing_files_fall_back_to_defaults(self, tmp_path):
        # A project that omits files (here, all but the lexicon) uses the shipped
        # defaults — so re-using the default feature system needs no features.toml.
        (tmp_path / "words.toml").write_text(WORDS_TOML)
        result = load_project(tmp_path)
        assert result.is_ok(), result.unwrap_err() if result.is_err() else None
        project = result.unwrap()
        assert "consonantal" in project.features  # the default feature system, via fallback
        assert "xenti" in project.words  # the project's own lexicon

    def test_invalid_features(self, tmp_path):
        # Write features with invalid content
        (tmp_path / "features.toml").write_text("[bad]\nkind = 'invalid'\n")
        (tmp_path / "letters.csv").write_text(LETTERS_CSV)
        (tmp_path / "diacritics.toml").write_text(DIACRITICS_TOML)
        (tmp_path / "sonorities.toml").write_text(SONORITIES_TOML)
        (tmp_path / "syllable_parts.toml").write_text(SYLLABLE_PARTS_TOML)
        (tmp_path / "words.toml").write_text(WORDS_TOML)
        result = load_project(tmp_path)
        assert result.is_err()
