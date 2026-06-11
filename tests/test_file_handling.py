"""Tests for file handling utilities."""

import pytest

from src.fortis.general.file_handling import load_csv_file, load_toml_file
from src.fortis.result import Err, Ok


class TestLoadTomlFile:
    def test_valid_file(self, tmp_path):
        path = tmp_path / "test.toml"
        path.write_text('[section]\nkey = "value"\n')
        result = load_toml_file(path)
        assert result.is_ok()
        data = result.unwrap()
        assert data["section"]["key"] == "value"

    def test_missing_file(self, tmp_path):
        path = tmp_path / "missing.toml"
        result = load_toml_file(path)
        assert result.is_err()

    def test_wrong_extension(self, tmp_path):
        path = tmp_path / "test.json"
        path.write_text('{"key": "value"}')
        result = load_toml_file(path)
        assert result.is_err()

    def test_empty_file(self, tmp_path):
        path = tmp_path / "empty.toml"
        path.write_text("")
        result = load_toml_file(path)
        assert result.is_err()

    def test_non_dict_top_level(self, tmp_path):
        path = tmp_path / "list.toml"
        path.write_text("[1, 2, 3]\n")
        result = load_toml_file(path)
        assert result.is_err()


class TestLoadCsvFile:
    def test_valid_file(self, tmp_path):
        path = tmp_path / "test.csv"
        path.write_text("name,age\nAlice,30\nBob,25\n")
        result = load_csv_file(path)
        assert result.is_ok()
        rows = result.unwrap()
        assert len(rows) == 2
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "30"

    def test_missing_file(self, tmp_path):
        path = tmp_path / "missing.csv"
        result = load_csv_file(path)
        assert result.is_err()

    def test_wrong_extension(self, tmp_path):
        path = tmp_path / "test.json"
        path.write_text("name,age\n")
        result = load_csv_file(path)
        assert result.is_err()

    def test_empty_file(self, tmp_path):
        path = tmp_path / "empty.csv"
        path.write_text("")
        result = load_csv_file(path)
        assert result.is_err()

    def test_header_only(self, tmp_path):
        path = tmp_path / "header.csv"
        path.write_text("name,age\n")
        result = load_csv_file(path)
        assert result.is_err()