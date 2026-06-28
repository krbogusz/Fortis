"""Tests for the autosegmental text diagram (application/diagram.py)."""

from src.fortis.application.diagram import (
    render_autosegmental,
    render_autosegmental_change,
    render_geometry_tree,
    render_place_change,
)
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.models.autosegment import Autoseg
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec


def _tone(value, autoseg_id):
    return Autoseg(FeatureBundle({"tone": FeatureSpec("tone", value)}), autoseg_id)


def test_single_link_is_a_vertical_bar(project):
    form = string_to_sequence("ta", project)  # t a
    h = form.fresh_id()
    form.tiers["tone"].autosegs.append(_tone(4, h))
    form.tiers["tone"].links.add((h, 1))  # high on the vowel
    out = render_autosegmental(form, project)
    assert "˦" in out and "│" in out  # the tone letter + one association line


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
    assert "└┬┘" in out and "˥" in out and "˧" in out  # converging contour


def test_floating_tone_has_no_line(project):
    form = string_to_sequence("kata⟨◌́⟩", project)  # a floating high suffix, unanchored
    out = render_autosegmental(form, project)
    assert "˦" in out.split("\n")[0]  # the high appears on the tone row
    assert "│" not in out and "┬" not in out  # ...with no association line — it floats


def test_change_added_association_is_dashed(project):
    # A newly added association (a spread / dock) renders dashed.
    before = string_to_sequence("taka", project)
    after = before.copy()
    h = after.fresh_id()
    after.tiers["tone"].autosegs.append(_tone(4, h))
    after.tiers["tone"].links.add((h, 1))  # H newly on the first vowel
    out = render_autosegmental_change(before, after, project)
    assert "˦" in out and "╎" in out  # dashed = added


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


def test_place_change_shows_spread_and_delink(project):
    # Nasal place assimilation (n → m before p): the trigger's place spreads (dashed) and
    # the nasal's old place delinks (╪).
    n = string_to_sequence("n", project).segments[0].bundle  # coronal nasal
    m = string_to_sequence("m", project).segments[0].bundle  # its labial outcome
    p = string_to_sequence("p", project).segments[0].bundle  # the labial trigger
    out = render_place_change(n, m, p, project)
    assert "labial" in out and "lingual" in out  # new (shared) + old place, by their real nodes
    assert "╎" in out and "╪" in out  # the spread (dashed link) and the delink bar


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
