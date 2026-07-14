"""Tests for the words loader."""

import pytest

from src.fortis.loaders.words import load_word_inventory


def _toml(tmp_path, text):
    (tmp_path / "words.toml").write_text(text, encoding="utf-8")
    return load_word_inventory(tmp_path / "words.toml")


def _csv(tmp_path, text):
    (tmp_path / "words.csv").write_text(text, encoding="utf-8")
    return load_word_inventory(tmp_path / "words.csv")


class TestConciseForm:
    """``"<ipa>" = "<gloss>"`` — a word that is only a seed, with no targets."""

    def test_valid(self, tmp_path):
        inventory = _toml(tmp_path, '"anpa" = "before"\n"atta" = "eight"\n').unwrap()
        assert list(inventory) == ["anpa", "atta"]
        assert inventory["anpa"].seed.ipa == "anpa"
        assert inventory["anpa"].gloss == "before"
        assert inventory["anpa"].targets == {}  # a seed is not something to score against

    def test_empty_gloss(self, tmp_path):
        assert _toml(tmp_path, '"anpa" = ""\n').unwrap()["anpa"].gloss == ""

    def test_a_table_value_is_rejected(self, tmp_path):
        # The old ipa-keyed table form. A word with targets now goes in a [[words]] table.
        errors = _toml(tmp_path, '"anpa" = {gloss = "x", final = "y"}\n').unwrap_err()
        assert "must be a gloss string" in errors[0]

    def test_missing_file(self, tmp_path):
        assert load_word_inventory(tmp_path / "nope.toml").is_err()


class TestWordsArray:
    """``[[words]]`` — id, gloss, frequency, and a series of forms through time."""

    LEXICON = """
[[words]]
id = "bear-v"
gloss = "to bear"
frequency = 1200
forms = [
  { time = -2000,   ipa = "bʱereti", category = "verb.pres.3sg" },
  { time = 200,     ipa = "biriði",  category = "verb.pres.3sg.strong" },
  { time = "final", ipa = "beəz" },
]
"""

    def test_full_word(self, tmp_path):
        word = _toml(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert word.id == "bear-v"
        assert word.gloss == "to bear"
        assert word.frequency == 1200
        assert word.seed_time == -2000
        assert word.seed.ipa == "bʱereti"

    def test_the_earliest_form_is_the_seed_and_is_not_a_target(self, tmp_path):
        word = _toml(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert word.ipa == "bʱereti"             # the derivation input
        assert set(word.targets) == {200, None}  # scored against — the seed is not among them
        assert word.stages == {200: "biriði"}
        assert word.final == "beəz"

    def test_final_is_the_untimed_slot(self, tmp_path):
        # "final" is not a year: an untimed rule runs after every timed one, so the form after
        # it cannot be dated. It keys as None, and sorts last.
        word = _toml(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert None in word.forms
        assert word.forms[None].ipa == "beəz"

    def test_category_is_read_per_form(self, tmp_path):
        word = _toml(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert word.forms[-2000].category == "verb.pres.3sg"
        assert word.forms[200].category == "verb.pres.3sg.strong"
        assert word.forms[None].category == ""  # omitted ⇒ empty, never guessed

    def test_category_in_force_is_the_latest_at_or_before(self, tmp_path):
        # This is what a category-scoped rule reads, and it is why a category given at a LATER
        # time expresses a reanalysis: every rule from that time on sees the new one.
        word = _toml(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert word.category_at(-2000) == "verb.pres.3sg"
        assert word.category_at(-500) == "verb.pres.3sg"         # still the seed's
        assert word.category_at(200) == "verb.pres.3sg.strong"   # the 200 entry takes effect
        assert word.category_at(900) == "verb.pres.3sg.strong"   # and stays in force
        assert word.category_at(-9999) == "verb.pres.3sg"        # before everything ⇒ the seed's

    def test_defaults(self, tmp_path):
        word = _toml(
            tmp_path, '[[words]]\nid = "a"\nforms = [{ time = 0, ipa = "a" }]\n'
        ).unwrap()["a"]
        assert word.gloss == "" and word.frequency == 1 and word.seed.category == ""

    def test_coexists_with_the_concise_form(self, tmp_path):
        # ABOVE the array: TOML binds a bare key/value to the table header above it, so a
        # concise entry written below [[words]] would become a key of that word.
        inventory = _toml(tmp_path, '"atta" = "eight"\n' + self.LEXICON).unwrap()
        assert set(inventory) == {"bear-v", "atta"}

    def test_concise_entry_below_the_array_says_why(self, tmp_path):
        errors = _toml(tmp_path, self.LEXICON + '\n"atta" = "eight"\n').unwrap_err()
        assert "must go ABOVE every [[words]] table" in errors[0]

    @pytest.mark.parametrize(
        "table, expected",
        [
            ('[[words]]\nforms = [{time=0, ipa="a"}]', "has no 'id'"),
            ('[[words]]\nid = "a"', "has no 'forms'"),
            ('[[words]]\nid = "a"\nforms = []', "has no 'forms'"),
            ('[[words]]\nid = "a"\nforms = [{time=0}]', "no 'ipa'"),
            ('[[words]]\nid = "a"\nforms = [{ipa="a"}]', "'time'"),
            ('[[words]]\nid = "a"\nforms = [{time="soon", ipa="a"}]', "neither an integer"),
            ('[[words]]\nid = "a"\nforms = [{time=0, ipa="a", category=7}]', "not a string"),
            ('[[words]]\nid = "a"\nfrequency = 0\nforms = [{time=0, ipa="a"}]', "positive integer"),
            ('[[words]]\nid = "a"\nfrequency = true\nforms = [{time=0, ipa="a"}]', "positive"),
            ('[[words]]\nid = "a"\nnope = 1\nforms = [{time=0, ipa="a"}]', "unknown key"),
        ],
    )
    def test_errors(self, tmp_path, table, expected):
        assert expected in _toml(tmp_path, table).unwrap_err()[0]

    def test_duplicate_id_errors(self, tmp_path):
        text = '[[words]]\nid = "a"\nforms = [{time=0, ipa="a"}]\n' * 2
        assert "already defined" in _toml(tmp_path, text).unwrap_err()[0]

    def test_two_forms_at_one_time_errors(self, tmp_path):
        text = '[[words]]\nid = "a"\nforms = [{time=0, ipa="a"}, {time=0, ipa="b"}]\n'
        assert "two forms at 0" in _toml(tmp_path, text).unwrap_err()[0]


class TestCsv:
    """One row per attested form — the long shape, so a category can vary with time."""

    LEXICON = (
        "id,time,ipa,category,gloss,frequency\n"
        "bear-v,-2000,bʱereti,verb.pres.3sg,to bear,1200\n"
        "bear-v,200,biriði,verb.pres.3sg.strong,,\n"
        "bear-v,final,beəz,,,\n"
    )

    def test_rows_sharing_an_id_are_one_word(self, tmp_path):
        inventory = _csv(tmp_path, self.LEXICON).unwrap()
        assert list(inventory) == ["bear-v"]
        word = inventory["bear-v"]
        assert word.seed.ipa == "bʱereti"
        assert word.stages == {200: "biriði"}
        assert word.final == "beəz"
        assert word.gloss == "to bear" and word.frequency == 1200

    def test_category_per_row(self, tmp_path):
        word = _csv(tmp_path, self.LEXICON).unwrap()["bear-v"]
        assert word.category_at(200) == "verb.pres.3sg.strong"

    def test_row_order_does_not_matter(self, tmp_path):
        rows = self.LEXICON.splitlines()
        shuffled = "\n".join([rows[0], rows[3], rows[1], rows[2]]) + "\n"
        assert _csv(tmp_path, shuffled).unwrap()["bear-v"].seed.ipa == "bʱereti"

    def test_quoted_comma_gloss(self, tmp_path):
        text = 'id,time,ipa,gloss\na,0,a,"amère, bitter"\n'
        assert _csv(tmp_path, text).unwrap()["a"].gloss == "amère, bitter"

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("time,ipa\n0,a\n", "missing required column"),
            ("id,time,ipa,wat\na,0,a,x\n", "unknown column"),
            ("id,time,ipa\n,0,a\n", "empty 'id'"),
            ("id,time,ipa\na,0,\n", "empty 'ipa'"),
            ("id,time,ipa\na,soon,a\n", "neither an integer"),
            ("id,time,ipa\na,0,a\na,0,b\n", "already has a form at 0"),
            ("id,time,ipa,frequency\na,0,a,0\n", "positive integer"),
            ("id,time,ipa,gloss\na,0,a,x\na,1,b,y\n", "two different glosses"),
        ],
    )
    def test_errors(self, tmp_path, text, expected):
        assert expected in _csv(tmp_path, text).unwrap_err()[0]


class TestCsvTomlEquivalence:
    def test_same_inventory(self, tmp_path):
        """The two serialisations are two spellings of one model."""
        from_toml = _toml(tmp_path, TestWordsArray.LEXICON).unwrap()
        from_csv = _csv(tmp_path, TestCsv.LEXICON).unwrap()
        assert from_toml.keys() == from_csv.keys()
        for key in from_toml:
            assert from_toml[key] == from_csv[key]
