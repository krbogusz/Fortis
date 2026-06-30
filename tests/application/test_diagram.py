"""Tests for the autosegmental text diagram (application/diagram.py)."""

from dataclasses import replace

from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.diagram import (
    render_autosegmental,
    render_autosegmental_change,
    render_change,
    render_geometry_tree,
)
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.models.autosegment import Autoseg
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.features import FeatureInventory
from src.fortis.models.specs import FeatureSpec


def _tone(value, autoseg_id):
    return Autoseg(FeatureBundle({"tone": FeatureSpec("tone", value)}), autoseg_id)


def test_single_link_is_a_vertical_bar(project):
    form = string_to_sequence("ta", project)  # t a
    h = form.fresh_id()
    form.tiers["tone"].autosegs.append(_tone(4, h))
    form.tiers["tone"].links.add((h, 1))  # high on the vowel
    out = render_autosegmental(form, project)
    assert "tone: high" in out and "│" in out  # the feature label + one association line


def test_spread_is_a_fork(project):
    form = string_to_sequence("taka", project)
    h = form.fresh_id()
    form.tiers["tone"].autosegs.append(_tone(4, h))
    form.tiers["tone"].links |= {(h, 1), (h, 3)}  # one tone, two anchors
    out = render_autosegmental(form, project)
    assert "┌" in out and "┐" in out and "┴" in out  # the fork


def test_contour_converges(project):
    form = string_to_sequence("ta", project)
    hi, mid = form.fresh_id(), form.fresh_id()
    form.tiers["tone"].autosegs += [_tone(5, hi), _tone(3, mid)]
    form.tiers["tone"].links |= {(hi, 1), (mid, 1)}  # two tones on one vowel
    out = render_autosegmental(form, project)
    # converging contour: the join glyph plus both levels' feature labels (spaced, not overlapping)
    assert "└┬┘" in out and "tone: extra-high" in out and "tone: mid" in out


def test_floating_tone_has_no_line(project):
    form = string_to_sequence("kata⟨◌́⟩", project)  # a floating high suffix, unanchored
    out = render_autosegmental(form, project)
    assert "tone: high" in out.split("\n")[0]  # the high appears on the tone row
    assert "│" not in out and "┬" not in out  # ...with no association line — it floats


def test_change_added_association_is_dashed(project):
    # A newly added association (a spread / dock) renders dashed.
    before = string_to_sequence("taka", project)
    after = before.copy()
    h = after.fresh_id()
    after.tiers["tone"].autosegs.append(_tone(4, h))
    after.tiers["tone"].links.add((h, 1))  # H newly on the first vowel
    out = render_autosegmental_change(before, after, project)
    assert "tone: high" in out and "╎" in out  # dashed = added


def test_spread_change_renders_as_a_fork(project):
    # A tone spreading to a second vowel renders as a fork, so it reads as one autosegment
    # on both anchors — the kept link solid (│), the new one dashed (╎).
    before = string_to_sequence("taka", project)
    t = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, t))
    before.tiers["tone"].links.add((t, 1))  # H on the first vowel
    after = before.copy()
    after.tiers["tone"].links.add((t, 3))  # spreads to the second vowel
    out = render_autosegmental_change(before, after, project)
    assert "┌" in out and "┐" in out  # the fork ties the one tone to both anchors
    assert "│" in out and "╎" in out  # first link kept (solid), the new one dashed


def test_render_change_is_the_unified_entry_point(project):
    # render_change returns every autosegmental change for a rule; a tier spread comes back as
    # one fork diagram (segmental spreads, driven by the rule, would each add their own). A
    # tier change needs no rule, so None is passed here.
    before = string_to_sequence("taka", project)
    t = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, t))
    before.tiers["tone"].links.add((t, 1))
    after = before.copy()
    after.tiers["tone"].links.add((t, 3))  # the tone spreads
    diagrams = render_change(before, after, None, project)
    assert len(diagrams) == 1
    assert "┌" in diagrams[0] and "╎" in diagrams[0]  # the spread fork, dashed new link


def test_change_removed_association_is_delinked(project):
    # A removed association renders with the delink bar.
    before = string_to_sequence("taka", project)
    h = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, h))
    before.tiers["tone"].links.add((h, 1))
    after = before.copy()
    after.tiers["tone"].links.discard((h, 1))  # delink the H from the vowel
    out = render_autosegmental_change(before, after, project)
    assert "╪" in out  # the delink bar


def test_change_kept_association_is_solid(project):
    # An unchanged association stays a solid bar — neither dashed nor delinked.
    before = string_to_sequence("taka", project)
    h = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, h))
    before.tiers["tone"].links.add((h, 1))
    after = before.copy()
    out = render_autosegmental_change(before, after, project)
    assert "│" in out and "╎" not in out and "╪" not in out


def _change_diagrams(project, ipa):
    """Every render_change diagram across a word's derivation — the rule of each step drives it."""
    rules = resolve_rule_letters(project.rules, project)
    word = project.words[ipa]
    derivation = derive(
        word, string_to_sequence(ipa, project), rules, project.letters, project.features,
        project.sonorities, project.syllable_parts, project.tiers,
    )
    return [
        d
        for step in derivation.steps
        for d in render_change(step.before, step.after, step.rule, project)
    ]


def test_render_change_reads_segmental_spreads_from_the_rule(project):
    # Rule-driven: a segmental spread is detected from the rule's ~n operations, not guessed from
    # which features changed. Place assimilation (anka) spreads the oral node — one fork carrying
    # the new place (╎) with the nasal's old place delinked (╪) below.
    place = _change_diagrams(project, "anka")
    assert len(place) == 1  # exactly the one assimilated consonant
    assert "oral" in place[0]  # labelled by the spread node itself, not its whole subtree
    assert "╎" in place[0] and "╪" in place[0]  # the spread (dashed) and the delink bar


def test_harmony_spread_is_read_from_the_rule_but_agreement_is_not(project):
    # The two harmony rules reach the same surface, but only the *spreading* one (utine) performs
    # a ~n operation, so only it draws forks; the *agreement* one (otine) draws nothing — the
    # honest autosegmental difference between the two formulations.
    harmony = _change_diagrams(project, "utine")
    assert any("back" in d and "┌" in d and "╎" in d for d in harmony)  # the [back] spread fork
    assert _change_diagrams(project, "otine") == []  # α-agreement performs no ~n spread


def test_geometry_tree_nests_real_nodes_for_one_segment(project):
    # Single-segment inspection: the segment is the implicit root; present features hang
    # beneath it, nested by the real feature geometry and named by its own nodes.
    out = render_geometry_tree(string_to_sequence("k", project).segments[0].bundle, project)
    lines = out.splitlines()
    assert lines[0] == "k"  # the segment itself is the (implicit) root
    assert "+consonantal" in out  # a binary feature shows its sign
    assert "glottal_aperture: neutral" in out  # a scalar shows its value label
    # the velar place nests faithfully: oral → lingual → back, each indented deeper than the last
    oral = next(i for i, line in enumerate(lines) if line.endswith("oral"))
    lingual = next(i for i, line in enumerate(lines) if line.endswith("lingual"))
    back = next(i for i, line in enumerate(lines) if line.endswith("back"))
    assert oral < lingual < back
    assert lines[oral].index("oral") < lines[lingual].index("lingual") < lines[back].index("back")


def _with_tone4_label_as(project, label):
    """A copy of *project* whose tone value 4 is labelled *label* instead of 'high'."""
    tone = project.features["tone"]
    features = FeatureInventory(dict(project.features))
    features["tone"] = replace(tone, values={**tone.values, 4: label})
    return replace(project, features=features)


def test_label_follows_a_redefined_feature_value(project):
    # The diagram labels autosegs by feature, read from the inventory — not a hardcoded map:
    # relabel tone value 4 and the diagram's tone label follows it.
    custom = _with_tone4_label_as(project, "HIGH!")
    form = string_to_sequence("ta", custom)
    h = form.fresh_id()
    form.tiers["tone"].autosegs.append(_tone(4, h))
    form.tiers["tone"].links.add((h, 1))
    out = render_autosegmental(form, custom)
    assert "tone: HIGH!" in out
