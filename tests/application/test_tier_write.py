"""Tests for the tier write path (application/tiers: split_carried, write_to_tier)."""

from src.fortis.application.tiers import split_carried, write_to_tier
from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.form import Form
from src.fortis.models.segment import Segment
from src.fortis.models.specs import FeatureSpec


def _b(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_split_separates_carried_features_from_the_segment(project):
    segment_bundle, by_tier = split_carried(_b(consonantal=1, stress=2, voice=1), project.tiers)
    assert "stress" not in segment_bundle  # carried → off the segment
    assert "consonantal" in segment_bundle and "voice" in segment_bundle  # segmental → stay
    assert by_tier["stress"]["stress"].value == 2


def test_write_creates_an_autoseg_and_links_it(project):
    form = Form([Segment(_b(syllabic=1), 0)])
    write_to_tier(form, 0, "stress", _b(stress=2))
    tier = form.tiers["stress"]
    assert len(tier.autosegs) == 1
    autoseg_id, anchor = next(iter(tier.links))
    assert anchor == 0 and tier.autosegs[0].bundle["stress"].value == 2


def test_write_with_a_none_value_just_delinks(project):
    form = Form([Segment(_b(syllabic=1), 0)])
    existing = Autoseg(_b(stress=2), 100)
    form.tiers["stress"] = AutosegmentalTier(autosegs=[existing], links={(100, 0)})
    write_to_tier(form, 0, "stress", _b(stress=None))  # `stress: none`
    assert form.tiers["stress"].links == set()  # delinked
    assert existing in form.tiers["stress"].autosegs  # old autoseg floats until stray-erase


def test_write_replaces_the_existing_link(project):
    form = Form([Segment(_b(syllabic=1), 0)])
    old = Autoseg(_b(stress=1), 100)
    form.tiers["stress"] = AutosegmentalTier(autosegs=[old], links={(100, 0)})
    write_to_tier(form, 0, "stress", _b(stress=2))
    linked_autosegs = {autoseg for (autoseg, _anchor) in form.tiers["stress"].links}
    assert 100 not in linked_autosegs and len(linked_autosegs) == 1  # old gone, new linked
