"""A stress diacritic on a rule *literal* does one of two jobs, by side.

Stress is a syllable-tier feature, so a bare segment literal matches a vowel at any
stress and, in the result, leaves the syllable's stress untouched (it persists from the
input). A ``ˈ``/``ˌ`` mark is lowered onto the resolved bundle on every side; what it
then does depends on the side:

* **match side** (target/context/exception) — it *constrains* the match: ``ˌe`` matches
  only a secondary-stressed e.
* **result side** — it *writes*, replacing the suprasegmental of the changed segment's
  syllable: ``ˌe → ˈe`` promotes secondary to primary, ``ˈe → ˌe`` demotes. A bare result
  writes nothing, so the stress persists.
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
    word = next(iter(proj.words.values()))
    ipa = word.seed.ipa
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


def test_bare_result_leaves_stress_untouched(tmp_path):
    # A bare result writes no stress: the matched syllable keeps its secondary stress.
    assert _surface(tmp_path, "ˌe → i") == "ˌtiˈte"


def test_result_mark_promotes_secondary_to_primary(tmp_path):
    # The result ˈ replaces the changed syllable's suprasegmental: secondary → primary
    # (the other syllable's primary is untouched — the write is scoped to its syllable).
    assert _surface(tmp_path, "ˌe → ˈe") == "ˈteˈte"


def test_result_mark_demotes_primary_to_secondary(tmp_path):
    assert _surface(tmp_path, "ˈe → ˌe") == "ˌteˌte"


def test_result_mark_writes_stress_alongside_a_segment_change(tmp_path):
    # A segment shorthand replaces the segment; the suprasegmental shorthand replaces the
    # syllable's stress — both at once: e→i and secondary→primary.
    assert _surface(tmp_path, "ˌe → ˈi") == "ˈtiˈte"


def test_multisyllable_result_marks_are_authoritative_across_the_span(tmp_path):
    # ˈe → aˈna: the primary ˈe is replaced by two syllables — an unmarked ``a`` and a
    # primary ``ˈa``. The result's marks are authoritative for the whole span, so the
    # unmarked first syllable must NOT inherit the replaced nucleus's stress: it stays
    # unstressed (``.ta.``), not ``.ˈta.``.
    assert _surface(tmp_path, "ˈe → aˈna") == "ˌte.taˈna"
