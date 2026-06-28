"""Node-level spread: `node: ~n` copies a whole geometry node's subtree (place assimilation)."""

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.loaders.project import load_project


def _surface(proj, ipa, word, rules):
    derivation = derive(
        word, string_to_sequence(ipa, proj), rules, proj.letters, proj.features,
        proj.sonorities, proj.syllable_parts, proj.tiers,
    )
    return render_syllabified(lower_tiers(derivation.surface), derivation.surface_boundaries, proj)


def test_place_assimilation_spreads_the_oral_node(tmp_path):
    # A nasal copies the whole place (oral) node of the following consonant — a node-level
    # `~n` spread that replaces the nasal's own place, be it labial, coronal, or velar.
    (tmp_path / "words.toml").write_text(
        '"anpa" = "labial"\n"anta" = "coronal"\n"anka" = "velar"\n'
    )
    (tmp_path / "rules.toml").write_text(
        '[place]\nwords = ["labial", "coronal", "velar"]\n'
        'definition = "[+nasal] -> [oral: ~1] / _ [+consonantal, oral: ~1]"\n'
    )
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    surface = {word.gloss: _surface(proj, ipa, word, rules) for ipa, word in proj.words.items()}
    assert surface["labial"] == "am.pa"  # n → m (copies the labial place)
    assert surface["coronal"] == "an.ta"  # n → n (already coronal; replace is a no-op)
    assert surface["velar"] == "aŋ.ka"  # n → ŋ (copies the velar/dorsal place)
