"""``letter^[Δ]`` — a letter shorthand with a concrete feature override.

The base letter's full specification with Δ combined on top: a wholesale replacement
(like a bare letter) but with the named features changed, or delinked for a ``none``
value. It resolves to a ``LetterBundle``, so on the target it constrains the match (the
segment must be the letter *and* satisfy Δ) and in the result it replaces-with-Δ. The ``^``
binds the last letter of a run. Δ may set or delink a suprasegmental (`stress: none`),
which — because the write replaces — overrides the value that would otherwise persist.
"""

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project


def _surface(tmp_path, definition, word='"ˌteˈte" = "x"\n'):
    (tmp_path / "rules.toml").write_text(f'[r]\ndefinition = "{definition}"\n', encoding="utf-8")
    (tmp_path / "words.toml").write_text(word, encoding="utf-8")
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    ipa, w = next(iter(proj.words.items()))
    d = derive(
        w, string_to_sequence(ipa, proj), rules, proj.letters, proj.features,
        proj.sonorities, proj.syllable_parts, proj.tiers,
    )
    return render_syllabified(lower_tiers(d.surface), d.surface_boundaries, proj)


def test_modifier_destresses_while_changing_melody(tmp_path):
    # ˈe → a^[stress: none]: change the vowel AND delink stress. The delink replaces, so the
    # matched syllable ends unstressed (`ta`), not inheriting the primary it had.
    assert _surface(tmp_path, "ˈe → a^[stress: none]") == "ˌte.ta"


def test_modifier_sets_stress(tmp_path):
    # ^[stress: primary] writes primary onto the changed segment's syllable.
    assert _surface(tmp_path, "ˌe → a^[stress: primary]") == "ˈtaˈte"


def test_modifier_tweaks_a_segmental_feature(tmp_path):
    # A purely segmental Δ (length) lengthens both e's; stress is untouched and persists.
    assert _surface(tmp_path, "e → e^[length: long]") == "ˌteːˈteː"


def test_modifier_constrains_the_match(tmp_path):
    # In the target, e^[length: long] matches only a LONG e — a short e is left alone,
    # a long e is caught. Identity match on the letter's features plus Δ.
    assert _surface(tmp_path, "e^[length: long] → i") == "ˌteˈte"
    assert _surface(tmp_path, "e^[length: long] → i", '"ˈteːt" = "y"\n') == "ˈtit"


def test_caret_binds_the_last_letter_of_a_run(tmp_path):
    # In at^[length: long] the ^ modifies only the last letter (t → tː); the a stays plain.
    assert _surface(tmp_path, "at → at^[length: long]", '"ˈkat" = "z"\n') == "ˈkatː"


def test_node_delink_yields_a_schwa(tmp_path):
    # `oral: none` delinks the whole oral subtree (place/quality), geometry-aware — a vowel
    # with no oral node is a featureless schwa. This is the segmental counterpart of destress.
    assert _surface(tmp_path, "e → e^[oral: none]") == "ˌtəˈtə"


def test_none_on_an_absent_feature_is_a_noop(tmp_path):
    # e carries no nasal specification, so delinking nasal changes nothing.
    assert _surface(tmp_path, "e → e^[nasal: none]") == "ˌteˈte"


def test_match_side_stress_constraint_is_symmetric(tmp_path):
    # In a target, absent ≡ none: e^[stress: none] matches an unstressed e (and e^[stress:
    # primary] a primary-stressed one) — symmetric, each matching exactly its stress level.
    assert _surface(tmp_path, "e^[stress: none] → i", '"teˈta" = "y"\n') == "tiˈta"
    assert _surface(tmp_path, "e^[stress: primary] → i", '"ˈtet" = "y"\n') == "ˈtit"
    assert _surface(tmp_path, "e^[stress: none] → i", '"ˈtet" = "y"\n') == "ˈtet"  # primary ≠ none
