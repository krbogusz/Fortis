"""Tests for tier-autosegment binding in the matcher (``tone: ~1=H`` records its position)."""

from src.fortis.application.matching import find_matches
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.notation import parse_definition


def _fb(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_bind_records_the_autoseg_position(project):
    sd = parse_definition("[+syllabic, tone: ~1=high] -> [+nasal]", project.features).unwrap()
    segs = [_fb(syllabic=1, tone=0), _fb(syllabic=1, tone=4)]  # toneless, then high
    matches = find_matches(sd, segs, project.letters)
    assert len(matches) == 1
    assert matches[0].start == 1  # only the high-toned nucleus matches
    assert matches[0].bindings.autoseg_reference == {1: 1}  # ref 1 bound to that position


def test_bind_requires_the_bound_value_to_match(project):
    sd = parse_definition("[+syllabic, tone: ~1=high] -> [+nasal]", project.features).unwrap()
    assert find_matches(sd, [_fb(syllabic=1, tone=2)], project.letters) == []  # mid, not high


def test_bind_needs_the_feature_present(project):
    sd = parse_definition("[+syllabic, tone: ~1=high] -> [+nasal]", project.features).unwrap()
    assert find_matches(sd, [_fb(syllabic=1)], project.letters) == []  # toneless → no bind
