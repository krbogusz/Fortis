"""Tests for autosegmental tier construction (application/tiers.py)."""

from src.fortis.application.segmentation import string_to_sequence


def test_construction_links_the_stress_autoseg_to_the_nucleus(project):
    form = string_to_sequence("ˈta", project)  # stress on the nucleus a
    stress = form.tiers["stress"]
    assert len(stress.autosegs) == 1 and len(stress.links) == 1
    autoseg_id, segment_id = next(iter(stress.links))
    nucleus = next(s for s in form.segments if s.id == segment_id)
    assert nucleus.bundle["syllabic"].value == 1  # the anchor is the syllabic segment
    assert stress.autosegs[0].id == autoseg_id


def test_onset_gets_no_autoseg(project):
    form = string_to_sequence("ˈta", project)
    onset = form.segments[0]  # t — not a syllabic anchor
    linked_segments = {segment_id for (_autoseg_id, segment_id) in form.tiers["stress"].links}
    assert onset.id not in linked_segments


def test_tier_with_no_carried_feature_is_empty(project):
    form = string_to_sequence("ˈta", project)  # no tone here
    assert form.tiers["tone"].autosegs == []


def test_in_bundle_copy_is_stripped(project):
    # The dual-representation phase is over: stress now lives only on the tier and is
    # stripped from the nucleus' segment bundle.
    form = string_to_sequence("ˈta", project)
    nucleus = next(s for s in form.segments if s.bundle["syllabic"].value == 1)
    assert "stress" not in nucleus.bundle  # no longer kept in the bundle
    linked = {seg_id for (_autoseg, seg_id) in form.tiers["stress"].links}
    assert nucleus.id in linked  # stress is on the stress tier, linked to the nucleus
