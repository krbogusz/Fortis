"""Node-level spread: `node: ~n` copies a whole geometry node's subtree (place assimilation)."""

from pathlib import Path

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
    surface = {w.gloss: _surface(proj, w.seed.ipa, w, rules) for w in proj.words.values()}
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
    surface = {w.gloss: _surface(proj, w.seed.ipa, w, rules) for w in proj.words.values()}
    # After back, round /u/: high /i/ takes backness + rounding (→ u); non-high /e/ takes only
    # backness (→ ɤ), the conditional gating its rounding off. The second vowel harmonising to
    # the first (already-changed) one is the cascade that needs the captured node to persist.
    assert surface["harmony"] == "u.tu.nɤ"


def test_presence_optional_spread_clears_the_target(tmp_path):
    # `~n?` is a presence-optional node-spread: it spreads the node's presence OR absence — the
    # node analogue of a unary alpha's absent pole. Backness harmony recalling both `back: ~1?`
    # and `front: ~2?` then works BOTH ways: a back trigger clears the target's `front`, a front
    # trigger clears its `back`. (Plain `~n` would require the node present and fail one direction.)
    (tmp_path / "words.toml").write_text('"uti" = "back-trigger"\n"itu" = "front-trigger"\n')
    (tmp_path / "rules.toml").write_text(
        '[harmony]\nwords = ["back-trigger", "front-trigger"]\napplication = "left_to_right"\n'
        'definition = "[+syllabic] -> [back: ~1?, front: ~2?] / '
        '[+syllabic, back: ~1?, front: ~2?] [-syllabic]* _"\n'
    )
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    surface = {w.gloss: _surface(proj, w.seed.ipa, w, rules) for w in proj.words.values()}
    assert surface["back-trigger"] == "u.tɯ"  # /i/ takes back, its front cleared → ɯ
    assert surface["front-trigger"] == "i.ty"  # /u/ takes front, its back cleared → y


def test_plain_recall_still_requires_the_node_present(tmp_path):
    # Without `?`, `node: ~n` keeps the canonical "spread only what's there" semantics: a nasal
    # before a PLACELESS consonant (glottal /h/, no oral node) does not match, so its place is not
    # touched — unlike `~n?`, which would delink it.
    (tmp_path / "words.toml").write_text('"anha" = "placeless"\n"anpa" = "labial"\n')
    (tmp_path / "rules.toml").write_text(
        '[place]\nwords = ["placeless", "labial"]\n'
        'definition = "[+nasal] -> [oral: ~1] / _ [+consonantal, oral: ~1]"\n'
    )
    proj = load_project(tmp_path).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    surface = {w.gloss: _surface(proj, w.seed.ipa, w, rules) for w in proj.words.values()}
    assert surface["placeless"] == "an.ha"  # h has no oral node → rule does not fire, n unchanged
    assert surface["labial"] == "am.pa"  # p has a place → the nasal assimilates as usual


def test_bind_and_match_recall_skips_non_matching_sources():
    # `node: ~n=value` is a bind-AND-match: it binds only a source whose node has that value, so a
    # transparent `[]*` gap steps over nearer non-matching segments to reach it. Sibe uvularization
    # spreads `high` onto a dorsal from a preceding [-high] vowel (`high: ~1=-`), the nearer [+high]
    # vowels transparent — a plain `high: ~1` would instead bind whichever vowel is nearest.
    proj = load_project(Path("projects/halle_vaux_wolfe")).unwrap()
    rules = resolve_rule_letters(proj.rules, proj)
    surface = {w.seed.ipa: _surface(proj, w.seed.ipa, w, rules) for w in proj.words.values()}
    assert surface["dʒalukun"] == "dʒa.lu.qun"  # a ([-high]) uvularizes k across the transparent u
    assert surface["bɔduxu"] == "bɔ.du.χu"  # ɔ ([-high]) uvularizes x across the transparent u
    assert surface["ulukun"] == "u.lu.kun"  # all [+high]: no [-high] to bind, so no uvularization
