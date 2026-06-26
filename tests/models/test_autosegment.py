"""Tests for the autosegmental tier types (Autoseg, AutosegmentalTier)."""

from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec


def _b(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_tier_defaults_to_empty():
    tier = AutosegmentalTier()
    assert tier.autosegs == [] and tier.links == set()


def test_link_pairs_an_autoseg_to_a_segment():
    h = Autoseg(_b(tone=4), id=10)
    tier = AutosegmentalTier(autosegs=[h], links={(h.id, 0)})  # H linked to segment 0
    assert (10, 0) in tier.links


def test_floating_autoseg_is_one_with_no_link():
    # Stability in miniature: an autoseg whose anchor was deleted keeps no link → floating.
    h = Autoseg(_b(tone=4), id=10)
    tier = AutosegmentalTier(autosegs=[h], links=set())
    linked_ids = {autoseg_id for (autoseg_id, _segment_id) in tier.links}
    assert h.id not in linked_ids


def test_spread_is_one_autoseg_on_several_anchors():
    h = Autoseg(_b(tone=4), id=10)
    tier = AutosegmentalTier(autosegs=[h], links={(10, 0), (10, 1)})  # one H, two anchors
    anchors = {segment_id for (autoseg_id, segment_id) in tier.links if autoseg_id == 10}
    assert anchors == {0, 1}


def test_float_host_positions_a_floating_autoseg():
    # A positioned floating tone: H sits after segment 3, with no association line.
    h = Autoseg(_b(tone=4), id=10)
    tier = AutosegmentalTier(autosegs=[h], links=set(), float_hosts={10: (3, "after")})
    assert tier.float_hosts[10] == (3, "after")
    assert not any(autoseg_id == 10 for (autoseg_id, _seg) in tier.links)  # still floating
