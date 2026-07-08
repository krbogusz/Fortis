"""A stress diacritic on a rule *literal* constrains the match by stress.

Stress is a syllable-tier feature, so a bare segment literal historically matched a
vowel at any stress. When a literal carries a ``ˈ``/``ˌ`` mark, that mark is lowered
onto the resolved pattern bundle and becomes a match *constraint* — on the match side
only. The result side is unaffected (suprasegmentals carry over from the input).
"""

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project


def _surface(tmp_path, definition):
    (tmp_path / "rules.toml").write_text(
        f'[r]\ndefinition = "{definition}"\n', encoding="utf-8"
    )
    (tmp_path / "words.toml").write_text('"ˌteˈte" = "x"\n', encoding="utf-8")
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    ipa, word = next(iter(proj.words.items()))
    d = derive(
        word, string_to_sequence(ipa, proj), rules, proj.letters, proj.features,
        proj.sonorities, proj.syllable_parts, proj.tiers,
    )
    return render_syllabified(lower_tiers(d.surface), d.surface_boundaries, proj)


def test_secondary_literal_matches_only_secondary(tmp_path):
    # ˌe → i must raise only the secondary-stressed e of ˌte.ˈte, not the primary one.
    assert _surface(tmp_path, "ˌe → i") == "ˌtiˈte"


def test_primary_literal_matches_only_primary(tmp_path):
    assert _surface(tmp_path, "ˈe → i") == "ˌteˈti"


def test_bare_literal_still_matches_any_stress(tmp_path):
    # No stress mark on the literal ⇒ both stressed vowels match (unchanged behaviour).
    assert _surface(tmp_path, "e → i") == "ˌtiˈti"
