"""A word enters the cascade at its seed: rules dated before its earliest form do not apply."""

from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project

WORDS = """
[[words]]
id = "from-the-start"
forms = [
  { time = 0, ipa = "ata" },
]

[[words]]
id = "from-later"
forms = [
  { time = 150, ipa = "ata" },
]
"""

RULES = """
[early]
time = 100
definition = "t → d"

[late]
time = 200
definition = "a → e / _ #"
"""


def _surfaces(tmp_path):
    (tmp_path / "words.toml").write_text(WORDS, encoding="utf-8")
    (tmp_path / "rules.toml").write_text(RULES, encoding="utf-8")
    project = load_project(tmp_path).unwrap()
    return {
        d.word.id: render_syllabified(
            lower_tiers(d.surface), d.surface_boundaries, project
        ).replace(".", "")
        for d in derive_all(project)
    }


class TestSeedTime:
    def test_a_word_seeded_at_the_start_takes_every_rule(self, tmp_path):
        assert _surfaces(tmp_path)["from-the-start"] == "ade"

    def test_a_word_seeded_later_skips_the_earlier_rules(self, tmp_path):
        assert _surfaces(tmp_path)["from-later"] == "ate"
