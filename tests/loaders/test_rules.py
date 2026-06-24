"""Tests for the rules loader."""


from src.fortis.loaders.rules import (
    load_application,
    load_rule,
    load_rule_inventory,
    load_time,
)
from src.fortis.models.rules import ApplicationMode


class TestLoadTime:
    def test_valid(self):
        result = load_time("test_rule", {"time": -2000})
        assert result.is_ok()
        assert result.unwrap() == -2000

    def test_zero(self):
        result = load_time("test_rule", {"time": 0})
        assert result.is_ok()
        assert result.unwrap() == 0

    def test_missing(self):
        result = load_time("test_rule", {})
        assert result.is_err()

    def test_non_integer(self):
        result = load_time("test_rule", {"time": "not_a_number"})
        assert result.is_err()


class TestLoadApplication:
    def test_simultaneous(self):
        result = load_application("test_rule", {"application": "simultaneous"})
        assert result.is_ok()
        assert result.unwrap() == ApplicationMode.simultaneous

    def test_left_to_right(self):
        result = load_application("test_rule", {"application": "left_to_right"})
        assert result.is_ok()
        assert result.unwrap() == ApplicationMode.left_to_right

    def test_right_to_left(self):
        result = load_application("test_rule", {"application": "right_to_left"})
        assert result.is_ok()
        assert result.unwrap() == ApplicationMode.right_to_left

    def test_missing_defaults_to_simultaneous(self):
        result = load_application("test_rule", {})
        assert result.is_ok()
        assert result.unwrap() == ApplicationMode.simultaneous

    def test_invalid(self):
        result = load_application("test_rule", {"application": "diagonal"})
        assert result.is_err()

    def test_non_string(self):
        result = load_application("test_rule", {"application": 42})
        assert result.is_err()


class TestLoadRule:
    def test_minimal_rule(self, features):
        result = load_rule(
            "test_rule",
            {"time": -2000, "definition": "a → b"},
            features,
        )
        assert result.is_ok(), f"Errors: {result.unwrap_err() if result.is_err() else None}"
        [rule] = result.unwrap()  # a string definition yields exactly one rule
        assert rule.id == "test_rule"
        assert rule.time == -2000
        assert rule.application == ApplicationMode.simultaneous
        assert rule.name is None
        assert rule.description is None

    def test_full_rule(self, features):
        result = load_rule(
            "backness_harmony",
            {
                "time": 1300,
                "name": "Backness harmony",
                "description": "Backness spreads rightward",
                "definition": "[+syll] → [-syll]",
                "application": "left_to_right",
            },
            features,
        )
        assert result.is_ok()
        [rule] = result.unwrap()
        assert rule.id == "backness_harmony"
        assert rule.time == 1300
        assert rule.name == "Backness harmony"
        assert rule.description == "Backness spreads rightward"
        assert rule.application == ApplicationMode.left_to_right

    def test_list_definition_yields_ordered_subrules(self, features):
        # A list 'definition' becomes one sub-rule per entry — same time/name, in
        # order, with id-suffixed ids — so a multi-step change reads as one rule.
        result = load_rule(
            "final_loss",
            {
                "time": -1500,
                "name": "Final vowel loss",
                "definition": ["a → b", "c → d"],
            },
            features,
        )
        assert result.is_ok(), result.unwrap_err() if result.is_err() else None
        rules = result.unwrap()
        assert [r.id for r in rules] == ["final_loss#1", "final_loss#2"]
        assert all(r.time == -1500 and r.name == "Final vowel loss" for r in rules)
        assert [r.raw_definition for r in rules] == ["a → b", "c → d"]

    def test_empty_definition_list_is_an_error(self, features):
        assert load_rule("bad", {"time": 0, "definition": []}, features).is_err()

    def test_one_bad_definition_fails_the_whole_rule(self, features):
        result = load_rule("bad", {"time": 0, "definition": ["a → b", "→ → →"]}, features)
        assert result.is_err()

    def test_missing_time(self, features):
        result = load_rule("bad", {"definition": "a → b"}, features)
        assert result.is_err()

    def test_missing_definition(self, features):
        result = load_rule("bad", {"time": 0}, features)
        assert result.is_err()

    def test_invalid_definition(self, features):
        result = load_rule(
            "bad", {"time": 0, "definition": "→ → →"}, features
        )
        assert result.is_err()


class TestLoadRuleInventory:
    def test_from_file(self, tmp_path, features):
        toml_content = """\
[laryngeal_coloring]
time = -2000
name = "Laryngeal coloring"
definition = "m → n"

[voicing_assimilation]
time = -2000
definition = "[+cons, -voice] → [-voice]"
"""
        path = tmp_path / "rules.toml"
        path.write_text(toml_content)
        result = load_rule_inventory(path, features)
        assert result.is_ok(), f"Errors: {result.unwrap_err() if result.is_err() else None}"
        inv = result.unwrap()
        assert -2000 in inv
        assert len(inv[-2000]) == 2
        assert inv[-2000][0].id == "laryngeal_coloring"
        assert inv[-2000][1].id == "voicing_assimilation"

    def test_rules_at_different_times(self, tmp_path, features):
        toml_content = """\
[early_rule]
time = -2000
definition = "m → n"

[late_rule]
time = 1000
definition = "a → b"
"""
        path = tmp_path / "rules.toml"
        path.write_text(toml_content)
        result = load_rule_inventory(path, features)
        assert result.is_ok()
        inv = result.unwrap()
        assert -2000 in inv
        assert 1000 in inv
        assert len(inv[-2000]) == 1
        assert len(inv[1000]) == 1

    def test_missing_file(self, tmp_path, features):
        path = tmp_path / "nonexistent.toml"
        result = load_rule_inventory(path, features)
        assert result.is_err()

    def test_null_insertion_rule(self, tmp_path, features):
        """Rule with ∅ (null) in definition."""
        toml_content = """\
[epenthesis]
time = -1000
definition = "∅ [+cons] → u"
"""
        path = tmp_path / "rules.toml"
        path.write_text(toml_content)
        result = load_rule_inventory(path, features)
        assert result.is_ok(), f"Errors: {result.unwrap_err() if result.is_err() else None}"

    def test_duplicate_rule_id_is_an_error(self, tmp_path, features):
        # A list definition mints foo#1/foo#2; an explicit "foo#1" table collides.
        toml_content = """\
[foo]
time = 0
definition = ["a → b", "c → d"]

["foo#1"]
time = 0
definition = "e → f"
"""
        path = tmp_path / "rules.toml"
        path.write_text(toml_content)
        result = load_rule_inventory(path, features)
        assert result.is_err()
        assert any("duplicate rule id 'foo#1'" in e for e in result.unwrap_err())
