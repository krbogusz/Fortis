"""Tests for the words loader."""

from src.fortis.loaders.words import load_word_inventory


class TestLoadWordInventory:
    def test_valid(self, tmp_path):
        toml_content = '"xenti" = "in front"\n"mexteːr" = "mother"\n'
        path = tmp_path / "words.toml"
        path.write_text(toml_content)
        result = load_word_inventory(path)
        assert result.is_ok()
        inv = result.unwrap()
        assert "xenti" in inv
        assert inv["xenti"].gloss == "in front"
        assert inv["mexteːr"].gloss == "mother"

    def test_empty_gloss(self, tmp_path):
        toml_content = '"test" = ""\n'
        path = tmp_path / "words.toml"
        path.write_text(toml_content)
        result = load_word_inventory(path)
        assert result.is_ok()
        inv = result.unwrap()
        assert inv["test"].gloss == ""

    def test_missing_file(self, tmp_path):
        path = tmp_path / "nonexistent.toml"
        result = load_word_inventory(path)
        assert result.is_err()

    def test_wrong_extension(self, tmp_path):
        path = tmp_path / "words.json"
        path.write_text("{}")
        result = load_word_inventory(path)
        assert result.is_err()


class TestWordTableForm:
    """The richer table form: gloss/final + integer-keyed stage forms."""

    def _load(self, tmp_path, content):
        path = tmp_path / "words.toml"
        path.write_text(content, encoding="utf-8")
        return load_word_inventory(path)

    def test_full_table(self, tmp_path):
        content = (
            '"ˈɑmɑt̪" = {gloss = "aime – loves", final = "ɛm", '
            '100 = "ˈɑ.mɑt̪", 300 = " ˈɑ.mɑt̪", 600 = "ˈãj̃.məθ", '
            '1000 = "ˈɛ̃j̃.mə", 1400 = "ˈɛ̃.mə", 1700 = "ɛm"}\n'
        )
        result = self._load(tmp_path, content)
        assert result.is_ok(), result.unwrap_err() if result.is_err() else None
        w = result.unwrap()["ˈɑmɑt̪"]
        assert w.ipa == "ˈɑmɑt̪"
        assert w.gloss == "aime – loves"
        assert w.final == "ɛm"
        assert w.stages == {
            100: "ˈɑ.mɑt̪",
            300: "ˈɑ.mɑt̪",  # leading space stripped
            600: "ˈãj̃.məθ",
            1000: "ˈɛ̃j̃.mə",
            1400: "ˈɛ̃.mə",
            1700: "ɛm",
        }

    def test_both_forms_coexist(self, tmp_path):
        # The explicit requirement: the plain string form and the table form
        # must both work in one inventory.
        content = (
            '"ˌɑbˈɑnte" = "avant"\n'
            '"ˈɑmɑt̪" = {gloss = "aime", final = "ɛm", 600 = "ˈãj̃.məθ"}\n'
        )
        result = self._load(tmp_path, content)
        assert result.is_ok()
        inv = result.unwrap()
        assert inv["ˌɑbˈɑnte"].gloss == "avant"
        assert inv["ˌɑbˈɑnte"].final is None
        assert inv["ˌɑbˈɑnte"].stages == {}
        assert inv["ˈɑmɑt̪"].final == "ɛm"
        assert inv["ˈɑmɑt̪"].stages == {600: "ˈãj̃.məθ"}

    def test_table_optional_fields(self, tmp_path):
        # gloss/final both optional; a table with only stages is valid.
        result = self._load(tmp_path, '"a" = {500 = "b"}\n')
        assert result.is_ok()
        w = result.unwrap()["a"]
        assert w.gloss == ""
        assert w.final is None
        assert w.stages == {500: "b"}

    def test_negative_stage_time_allowed(self, tmp_path):
        # -100 is a real rule time; stage times aren't constrained to boundaries.
        result = self._load(tmp_path, '"a" = {gloss = "x", -100 = "y"}\n')
        assert result.is_ok()
        assert result.unwrap()["a"].stages == {-100: "y"}

    def test_non_integer_stage_key_errors(self, tmp_path):
        result = self._load(tmp_path, '"a" = {gloss = "x", latin = "y"}\n')
        assert result.is_err()
        assert any("latin" in e for e in result.unwrap_err())

    def test_non_string_stage_form_errors(self, tmp_path):
        result = self._load(tmp_path, '"a" = {100 = 42}\n')
        assert result.is_err()

    def test_non_string_final_errors(self, tmp_path):
        result = self._load(tmp_path, '"a" = {final = 42}\n')
        assert result.is_err()

    def test_non_string_non_table_value_errors(self, tmp_path):
        result = self._load(tmp_path, '"a" = 42\n')
        assert result.is_err()
        assert any("gloss string or a table" in e for e in result.unwrap_err())
