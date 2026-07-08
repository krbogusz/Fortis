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


def test_spread_copies_a_childless_leaf_for_vowel_harmony(tmp_path):
    # A childless leaf (`back`, `rounded`, `labial`) spreads by node-copy too — the feature
    # itself, with no subtree. Turkish-style harmony: every vowel takes the preceding vowel's
    # backness, and a high vowel additionally takes its rounding (gated by <1: aperture: high>). The
    # cascade across `[-syllabic]*` also guards that node captures survive backtracking.
    (tmp_path / "words.toml").write_text('"utine" = "harmony"\n')
    (tmp_path / "rules.toml").write_text(
        '[harmony]\nwords = ["harmony"]\napplication = "left_to_right"\n'
        'definition = "[+syllabic, <1: aperture: high>] -> '
        "[back: ~1, front: none, <1: rounded: ~2>, <1: labial: ~3>] / "
        '[+syllabic, back: ~1, rounded: ~2, labial: ~3] [-syllabic]* _"\n'
    )
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    surface = {word.gloss: _surface(proj, ipa, word, rules) for ipa, word in proj.words.items()}
    # After back, round /u/: high /i/ takes backness + rounding (→ u); non-high /e/ takes only
    # backness (→ ɤ), the conditional gating its rounding off. The second vowel harmonising to
    # the first (already-changed) one is the cascade that needs the captured node to persist.
    assert surface["harmony"] == "u.tu.nɤ"
