"""Tests for the top-level project loader (integration)."""


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

    def test_missing_features_file(self, tmp_path):
        # Don't write features.toml
        (tmp_path / "letters.csv").write_text(LETTERS_CSV)
        (tmp_path / "diacritics.toml").write_text(DIACRITICS_TOML)
        (tmp_path / "sonorities.toml").write_text(SONORITIES_TOML)
        (tmp_path / "syllable_parts.toml").write_text(SYLLABLE_PARTS_TOML)
        (tmp_path / "words.toml").write_text(WORDS_TOML)
        result = load_project(tmp_path)
        assert result.is_err()

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
