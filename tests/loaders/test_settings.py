"""Tests for the settings loader (src/fortis/loaders/settings.py)."""

from src.fortis.config import config
from src.fortis.loaders.settings import load_settings
from src.fortis.models.settings import DiagnosisSettings, GradingSettings, Settings


def _write(tmp_path, text):
    path = tmp_path / "settings.toml"
    path.write_text(text, encoding="utf-8")
    return path


class TestDefaults:
    def test_missing_file_is_all_defaults(self, tmp_path):
        assert load_settings(tmp_path / "nope.toml").unwrap() == Settings()

    def test_empty_file_is_all_defaults(self, tmp_path):
        assert load_settings(_write(tmp_path, "")).unwrap() == Settings()

    def test_shipped_default_mirrors_code_defaults(self):
        # The invariant: projects/default/settings.toml must equal the built-in
        # defaults, so "file present" and "file absent" can never diverge.
        shipped = config.paths.default / "settings.toml"
        assert load_settings(shipped).unwrap() == Settings()


class TestOverrides:
    def test_single_key_overrides_rest_default(self, tmp_path):
        settings = load_settings(_write(tmp_path, "[diagnosis]\nmin_support = 5\n")).unwrap()
        assert settings.diagnosis.min_support == 5
        assert settings.diagnosis.min_errors == DiagnosisSettings().min_errors  # untouched
        assert settings.grading == GradingSettings()  # whole section defaults

    def test_all_keys(self, tmp_path):
        text = (
            "[grading]\ntransposition_cost = 2\n"
            "[diagnosis]\nmin_support = 4\nmin_errors = 1\nreport_top = 10\nfocus_count = 3\n"
        )
        settings = load_settings(_write(tmp_path, text)).unwrap()
        assert settings.grading.transposition_cost == 2
        assert settings.diagnosis == DiagnosisSettings(
            min_support=4, min_errors=1, report_top=10, focus_count=3
        )


class TestValidation:
    def test_unknown_section(self, tmp_path):
        err = load_settings(_write(tmp_path, "[nope]\nx = 1\n")).unwrap_err()
        assert any("unknown section" in e for e in err)

    def test_unknown_key(self, tmp_path):
        err = load_settings(_write(tmp_path, "[diagnosis]\nmadeup = 1\n")).unwrap_err()
        assert any("unknown key 'madeup'" in e for e in err)

    def test_bool_is_rejected_not_coerced_to_int(self, tmp_path):
        # bool is an int subclass; `true` must NOT silently become 1.
        err = load_settings(_write(tmp_path, "[diagnosis]\nmin_support = true\n")).unwrap_err()
        assert any("must be an integer" in e for e in err)

    def test_non_integer_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[grading]\ntransposition_cost = 1.5\n")).unwrap_err()
        assert any("must be an integer" in e for e in err)

    def test_below_minimum_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[diagnosis]\nmin_support = 0\n")).unwrap_err()
        assert any("must be ≥ 1" in e for e in err)

    def test_negative_transposition_cost_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[grading]\ntransposition_cost = -1\n")).unwrap_err()
        assert any("must be ≥ 0" in e for e in err)

    def test_errors_accumulate(self, tmp_path):
        err = load_settings(
            _write(tmp_path, "[diagnosis]\nmin_support = 0\nmadeup = 1\n")
        ).unwrap_err()
        assert len(err) == 2
