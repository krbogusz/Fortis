"""Tests for config defaults."""

from src.fortis.config import Config, Paths, ValueSymbols, config


class TestPaths:
    def test_default_root(self):
        paths = Paths()
        assert paths.root.exists()

    def test_default_dir(self):
        paths = Paths()
        assert paths.default == paths.root / "projects" / "default"

    def test_letters_path(self):
        paths = Paths()
        assert paths.letters == paths.default / "letters.csv"


class TestValueSymbols:
    def test_present(self):
        vs = ValueSymbols()
        assert "+" in vs.present
        assert "1" in vs.present
        assert "present" in vs.present

    def test_absent(self):
        vs = ValueSymbols()
        assert "-" in vs.absent
        assert "0" in vs.absent
        assert "absent" in vs.absent

    def test_unspecified(self):
        vs = ValueSymbols()
        assert "∅" in vs.unspecified
        assert "none" in vs.unspecified
        assert "unspecified" in vs.unspecified


class TestConfig:
    def test_singleton(self):
        assert isinstance(config, Config)
        assert config.paths.default.exists()

    def test_greek_alphabet(self):
        assert "α" in config.greek_alphabet
        assert "β" in config.greek_alphabet
        assert len(config.greek_alphabet) >= 24

    def test_special_symbols(self):
        assert "." in config.special_symbols

    def test_reserved_symbols(self):
        assert "#" in config.reserved_symbols
        assert "[" in config.reserved_symbols
