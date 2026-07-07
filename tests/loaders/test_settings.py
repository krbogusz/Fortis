"""Tests for the settings loader (src/fortis/loaders/settings.py)."""

from src.fortis.config import config
from src.fortis.loaders.settings import load_settings
from src.fortis.models.settings import (
    AccuracySettings,
    DiagnosisSettings,
    InductionSettings,
    Settings,
)


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
        assert settings.accuracy == AccuracySettings()  # whole section defaults

    def test_all_keys(self, tmp_path):
        text = (
            "[accuracy]\ntransposition_cost = 2\n"
            "[diagnosis]\nmin_support = 4\nmin_support_percent = 25\n"
            "min_errors = 1\nreport_top = 10\nfocus_count = 3\n"
            "[induction]\nmin_improved_words = 3\ntop_confusions = 7\n"
            "contexts_per_confusion = 40\nplacement_candidates = 6\n"
            "max_rules_per_interval = 80\nalignment_distance_cap = 5\nfinal_weight = 0.5\n"
        )
        settings = load_settings(_write(tmp_path, text)).unwrap()
        assert settings.accuracy.transposition_cost == 2
        assert settings.diagnosis == DiagnosisSettings(
            min_support=4, min_support_percent=25, min_errors=1, report_top=10, focus_count=3
        )
        assert settings.induction == InductionSettings(
            min_improved_words=3, top_confusions=7, contexts_per_confusion=40,
            placement_candidates=6, max_rules_per_interval=80, alignment_distance_cap=5,
            final_weight=0.5,
        )

    def test_final_weight_accepts_int(self, tmp_path):
        # A bare integer is promoted to float for the one float-valued key.
        settings = load_settings(_write(tmp_path, "[induction]\nfinal_weight = 2\n")).unwrap()
        assert settings.induction.final_weight == 2.0
        assert isinstance(settings.induction.final_weight, float)


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
        err = load_settings(_write(tmp_path, "[accuracy]\ntransposition_cost = 1.5\n")).unwrap_err()
        assert any("must be an integer" in e for e in err)

    def test_below_minimum_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[diagnosis]\nmin_support = 0\n")).unwrap_err()
        assert any("must be ≥ 1" in e for e in err)

    def test_negative_transposition_cost_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[accuracy]\ntransposition_cost = -1\n")).unwrap_err()
        assert any("must be ≥ 0" in e for e in err)

    def test_final_weight_bool_rejected(self, tmp_path):
        # bool is an int subclass; `true` must NOT become 1.0 on a float-valued key.
        err = load_settings(_write(tmp_path, "[induction]\nfinal_weight = true\n")).unwrap_err()
        assert any("must be a number" in e for e in err)

    def test_induction_below_minimum_rejected(self, tmp_path):
        err = load_settings(_write(tmp_path, "[induction]\ntop_confusions = 0\n")).unwrap_err()
        assert any("must be ≥ 1" in e for e in err)

    def test_errors_accumulate(self, tmp_path):
        err = load_settings(
            _write(tmp_path, "[diagnosis]\nmin_support = 0\nmadeup = 1\n")
        ).unwrap_err()
        assert len(err) == 2
