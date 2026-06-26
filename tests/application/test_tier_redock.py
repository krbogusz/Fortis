"""Tests for syllable-aware re-docking (application/tiers.redock_to_nuclei)."""

from src.fortis.application.tiers import redock_to_nuclei
from src.fortis.models.autosegment import Autoseg, AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.form import Form
from src.fortis.models.segment import Segment
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.bundles import parse_pattern_bundle


def _b(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_moves_a_non_nucleus_link_to_the_nucleus(project):
    nucleus = parse_pattern_bundle("+syllabic", project.features).unwrap()
    # one syllable [u, l]: u (pos 0) is the nucleus, l (pos 1) a coda carrying the stress
    form = Form([Segment(_b(syllabic=1), 0), Segment(_b(consonantal=1), 1)])
    form.tiers["stress"] = AutosegmentalTier(
        autosegs=[Autoseg(_b(stress=2), 100)], links={(100, 1)}
    )
    redock_to_nuclei(form, frozenset(), nucleus)
    assert form.tiers["stress"].links == {(100, 0)}  # followed the syllable to its nucleus


def test_leaves_a_nucleus_link_alone(project):
    nucleus = parse_pattern_bundle("+syllabic", project.features).unwrap()
    form = Form([Segment(_b(syllabic=1), 0), Segment(_b(consonantal=1), 1)])
    form.tiers["stress"] = AutosegmentalTier(
        autosegs=[Autoseg(_b(stress=2), 100)], links={(100, 0)}
    )
    redock_to_nuclei(form, frozenset(), nucleus)
    assert form.tiers["stress"].links == {(100, 0)}  # already on the nucleus
