"""Tests for the Form/Segment scaffolding (autosegmental Phase 0)."""

from src.fortis.models.autosegment import AutosegmentalTier
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.form import Form
from src.fortis.models.segment import Segment
from src.fortis.models.specs import FeatureSpec


def _b(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_from_bundles_assigns_sequential_ids():
    b0, b1 = _b(a=1), _b(a=0)
    form = Form.from_bundles([b0, b1])
    assert [s.id for s in form.segments] == [0, 1]
    assert form.segments[0].bundle is b0 and form.segments[1].bundle is b1
    assert form.bundles() == [b0, b1]
    assert form.tiers == {}


def test_fresh_id_continues_after_initial_segments():
    form = Form.from_bundles([_b(a=1), _b(a=0)])
    assert [form.fresh_id(), form.fresh_id()] == [2, 3]


def test_splice_preserves_out_of_span_identity():
    # The whole point of ids: rewriting the middle leaves the neighbours' identity intact.
    form = Form.from_bundles([_b(a=1), _b(a=0), _b(a=1)])
    keep_left, keep_right = form.segments[0], form.segments[2]
    form.segments[1:2] = [Segment(_b(a=0), form.fresh_id())]
    assert form.segments[0] is keep_left
    assert form.segments[2] is keep_right
    assert form.segments[1].id == 3


def test_copy_is_independent():
    form = Form.from_bundles([_b(a=1)])
    clone = form.copy()
    clone.segments.append(Segment(_b(a=0), clone.fresh_id()))
    assert len(form.segments) == 1 and len(clone.segments) == 2


def test_copy_isolates_tier_float_hosts():
    form = Form.from_bundles([_b(a=1)])
    form.tiers["tone"] = AutosegmentalTier(float_hosts={5: (0, "before")})
    clone = form.copy()
    clone.tiers["tone"].float_hosts[6] = (0, "after")  # mutate the clone's tier
    assert 6 not in form.tiers["tone"].float_hosts  # the original is untouched
