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
    form.tiers["tone"].links |= {(h, 1), (h, 3)}  # one tone, two syllables
    out = render_autosegmental(form, project)
    assert "└" in out and "┘" in out and "┬" in out  # the fork (tier below, opening up)


def test_contour_stacks_its_levels(project):
    form = string_to_sequence("ta", project)
    hi, mid = form.fresh_id(), form.fresh_id()
    form.tiers["tone"].autosegs += [_tone(5, hi), _tone(3, mid)]
    form.tiers["tone"].links |= {(hi, 1), (mid, 1)}  # two tones on one syllable
    out = render_autosegmental(form, project)
    # two tones on one TBU stack below it, each with its own label and association line
    assert "tone: extra-high" in out and "tone: mid" in out and "│" in out


def test_floating_tone_is_drawn_without_a_line(project):
    # A floating (unlinked) tone is shown at its lexical position, parenthesised, with no line.
    form = string_to_sequence("kata⟨◌́⟩", project)  # a floating high suffix, unanchored
    out = render_autosegmental(form, project)
    assert "(tone: high)" in out  # the float is drawn…
    assert "│" not in out and "┬" not in out  # …but with no association line — nothing anchors it


def test_change_added_association_is_dotted(project):
    # A newly added association (a spread / dock) renders dotted.
    before = string_to_sequence("taka", project)
    after = before.copy()
    h = after.fresh_id()
    after.tiers["tone"].autosegs.append(_tone(4, h))
    after.tiers["tone"].links.add((h, 1))  # H newly on the first vowel
    out = render_autosegmental_change(before, after, project)
    assert "tone: high" in out and "┊" in out  # dotted = added


def test_spread_change_renders_as_a_fork(project):
    # A tone spreading to a second vowel renders as a fork, so it reads as one autosegment
    # on both anchors — the kept link solid (│), the new one dotted (┊).
    before = string_to_sequence("taka", project)
    t = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, t))
    before.tiers["tone"].links.add((t, 1))  # H on the first vowel
    after = before.copy()
    after.tiers["tone"].links.add((t, 3))  # spreads to the second vowel
    out = render_autosegmental_change(before, after, project)
    assert "└" in out and "┘" in out  # the fork ties the one tone to both syllables
    assert "│" in out and "┊" in out  # first link kept (solid), the new one dotted


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
    sublabel, diagram = diagrams[0]
    assert sublabel == ""  # a tier change carries no spread-node sublabel
    assert "└" in diagram and "┊" in diagram  # the spread fork, dotted new link


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
    # An unchanged association stays a solid bar — neither dotted nor delinked.
    before = string_to_sequence("taka", project)
    h = before.fresh_id()
    before.tiers["tone"].autosegs.append(_tone(4, h))
    before.tiers["tone"].links.add((h, 1))
    after = before.copy()
    out = render_autosegmental_change(before, after, project)
    assert "│" in out and "┊" not in out and "╪" not in out


def _change_diagrams(project, ipa):
    """Every render_change diagram across a word's derivation — the rule of each step drives it."""
    rules = resolve_rule_letters(project.rules, project)
    word = next(w for w in project.words.values() if w.seed.ipa == ipa)
    derivation = derive(
        word, string_to_sequence(ipa, project), rules, project.letters, project.features,
        project.sonorities, project.syllable_parts, project.tiers,
    )
    return [
        diagram
        for step in derivation.steps
        for _sublabel, diagram in render_change(step.before, step.after, step.rule, project)
    ]


def test_render_change_reads_segmental_spreads_from_the_rule(project):
    # Rule-driven: a segmental spread is detected from the rule's ~n operations, not guessed from
    # which features changed. Place assimilation (anka) draws the two feature-geometry trees with
    # the oral node spreading (◀ the dashed arrow) and the nasal's old place delinked (⧧).
    place = _change_diagrams(project, "anka")
    assert len(place) == 1  # exactly the one assimilated consonant
    assert "◀" in place[0] and "⧧" in place[0]  # the spreading arrow and the delink mark


def test_node_spread_shows_both_geometry_trees(project):
    # The rule exchanges the ``oral`` node ([oral: ~1]); the diagram is the target's and trigger's
    # geometry trees side by side, so the coronal that delinks (``front``) and the velar that
    # spreads in (``back``) both appear, hung under their ``oral`` nodes with tree branches (┌┴┐).
    (place,) = _change_diagrams(project, "anka")
    assert "oral" in place and "┌" in place  # geometry nodes drawn as a top-down tree
    assert "back" in place  # the trigger's velar place (its tree)
    assert "front" in place  # the target's coronal place (its tree)


def test_harmony_spread_is_read_from_the_rule_but_agreement_is_not(project):
    # The two harmony rules reach the same surface, but only the *spreading* one (utine) performs
    # a ~n operation, so only it draws a spreading arrow; the *agreement* one (otine) draws nothing
    # — the honest autosegmental difference between the two formulations.
    harmony = _change_diagrams(project, "utine")
    assert any("back" in d and "◀" in d for d in harmony)  # the [back] spread, as an arrow
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
