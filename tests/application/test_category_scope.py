"""A rule scoped to a grammatical CATEGORY — the class-wide counterpart of ``words``.

The category is *given*, not derived: it is an annotation the analyst supplies at each time, like
the seed IPA, and the engine never predicts it. That is what keeps it out of circularity — the
engine still predicts only the IPA, and the category conditions the sound laws the way "this is a
weak class-1 verb" conditions them in a handbook. Giving a DIFFERENT category at a later time is
therefore how a reanalysis is expressed, and the last test here is the one that shows it.
"""

from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project

WORDS = """
[[words]]
id = "the-verb"
forms = [
  { time = 0, ipa = "ata", category = "verb" },
]

[[words]]
id = "the-noun"
forms = [
  { time = 0, ipa = "ata", category = "noun" },
]

[[words]]
id = "the-uncategorised"
forms = [
  { time = 0, ipa = "ata" },
]
"""

RULES = """
[verbs_only]
time = 100
categories = "verb"
definition = "t → d"

[everything]
time = 200
definition = "a → e / _ #"
"""


def _surfaces(tmp_path, words=WORDS, rules=RULES):
    (tmp_path / "words.toml").write_text(words, encoding="utf-8")
    (tmp_path / "rules.toml").write_text(rules, encoding="utf-8")
    project = load_project(tmp_path).unwrap()
    return {
        d.word.id: render_syllabified(
            lower_tiers(d.surface), d.surface_boundaries, project
        ).replace(".", "")
        for d in derive_all(project)
    }


class TestCategoryScope:
    def test_a_scoped_rule_fires_only_on_its_category(self, tmp_path):
        surfaces = _surfaces(tmp_path)
        assert surfaces["the-verb"] == "ade"   # t → d fired, then the unscoped a → e
        assert surfaces["the-noun"] == "ate"   # only the unscoped rule

    def test_an_unscoped_rule_still_fires_on_everything(self, tmp_path):
        # The category restricts the rules that NAME it; it does not opt a word out of the rest.
        assert all(s.endswith("e") for s in _surfaces(tmp_path).values())

    def test_a_word_with_no_category_is_not_swept_into_a_scoped_rule(self, tmp_path):
        # "" is not "any" — an unannotated word simply is not in the class.
        assert _surfaces(tmp_path)["the-uncategorised"] == "ate"

    def test_a_list_of_categories_matches_any_of_them(self, tmp_path):
        rules = RULES.replace('categories = "verb"', 'categories = ["verb", "noun"]')
        surfaces = _surfaces(tmp_path, rules=rules)
        assert surfaces["the-verb"] == surfaces["the-noun"] == "ade"
        assert surfaces["the-uncategorised"] == "ate"  # still out — it is in neither class

    def test_the_category_is_matched_literally(self, tmp_path):
        # The engine has no vocabulary of categories and never parses one, so a project's scheme
        # is its own business — "verb.pres.3sg" is not a sub-class of "verb" to the engine.
        words = WORDS.replace('category = "verb"', 'category = "verb.pres.3sg"')
        assert _surfaces(tmp_path, words=words)["the-verb"] == "ate"  # did NOT fire


class TestReanalysis:
    """A category given at a LATER time takes effect for every rule from that time on."""

    WORDS = """
[[words]]
id = "reanalysed"
forms = [
  { time = 0,   ipa = "ata", category = "verb" },
  { time = 500, ipa = "ada", category = "noun" },
]

[[words]]
id = "always-a-noun"
forms = [
  { time = 0, ipa = "ata", category = "noun" },
]
"""

    RULES = """
[verbs_only]
time = 100
categories = "verb"
definition = "t → d"

[nouns_only]
time = 600
categories = "noun"
definition = "a → e / _ #"
"""

    def test_a_word_can_change_class_mid_cascade(self, tmp_path):
        surfaces = _surfaces(tmp_path, words=self.WORDS, rules=self.RULES)
        # It was a verb at t=100 (so t → d fired) and a noun by t=600 (so a → e fired too).
        # No single category could have produced this form; the change of class is what did.
        assert surfaces["reanalysed"] == "ade"
        # The control never was a verb, so it only ever took the noun rule.
        assert surfaces["always-a-noun"] == "ate"

    def test_the_category_in_force_is_the_latest_at_or_before_the_rule(self, tmp_path):
        (tmp_path / "words.toml").write_text(self.WORDS, encoding="utf-8")
        (tmp_path / "rules.toml").write_text(self.RULES, encoding="utf-8")
        word = load_project(tmp_path).unwrap().words["reanalysed"]
        assert word.category_at(100) == "verb"   # before the reanalysis
        assert word.category_at(499) == "verb"
        assert word.category_at(500) == "noun"   # from the moment it is given
        assert word.category_at(600) == "noun"
        assert word.category_at(None) == "noun"  # the untimed rules run last of all
