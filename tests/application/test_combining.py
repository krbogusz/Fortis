"""Tests for the bundle algebra (application/combining.py)."""

from src.fortis.application.combining import combine, differing, matches_exactly, merge
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec


def _fb(**features: object) -> FeatureBundle:
    """Build a realized FeatureBundle from feature=value kwargs."""
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


class TestCombine:
    def test_disjoint_union(self):
        result = combine(_fb(voice=1), _fb(nasal=0))
        assert result["voice"].value == 1
        assert result["nasal"].value == 0

    def test_other_overrides(self):
        result = combine(_fb(voice=1), _fb(voice=0))
        assert result["voice"].value == 0

    def test_does_not_mutate_base(self):
        base = _fb(voice=1)
        combine(base, _fb(voice=0))
        assert base["voice"].value == 1

    def test_form_contour(self):
        result = combine(_fb(tone=1), _fb(tone=2), form_contours=True)
        assert result["tone"].value == (1, 2)

    def test_form_contour_extends_existing_contour(self):
        result = combine(_fb(tone=(1, 2)), _fb(tone=3), form_contours=True)
        assert result["tone"].value == (1, 2, 3)


class TestMatchesExactlyAndDiffering:
    def test_exact_match(self):
        assert matches_exactly(_fb(voice=1, nasal=0), _fb(voice=1, nasal=0))

    def test_value_mismatch(self):
        assert not matches_exactly(_fb(voice=1), _fb(voice=0))

    def test_extra_feature_breaks_exact(self):
        assert not matches_exactly(_fb(voice=1, nasal=0), _fb(voice=1))

    def test_differing_lists_value_and_presence_diffs(self):
        diffs = set(differing(_fb(voice=1, nasal=0), _fb(voice=0, high=1)))
        assert diffs == {"voice", "nasal", "high"}

    def test_differing_empty_when_equal(self):
        assert differing(_fb(voice=1), _fb(voice=1)) == []


def _delta(**features: object) -> FeatureBundle:
    """Build a delta bundle; a value of None marks an unlink."""
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


class TestMerge:
    def test_merge_is_combine_when_no_unlinks(self, features):
        result = merge(_fb(voice=1), _delta(nasal=0), features)
        assert result["voice"].value == 1
        assert result["nasal"].value == 0

    def test_unlink_drops_the_feature(self, features):
        result = merge(_fb(voice=1, nasal=0), _delta(nasal=None), features)
        assert "nasal" not in result
        assert result["voice"].value == 1

    def test_unlink_node_drops_descendants(self, features):
        # `manner` dominates continuant/sonorant/nasal/lateral; unlinking it
        # unspecifies the whole subtree even though they carry concrete values.
        base = _fb(manner=1, nasal=1, lateral=0, continuant=1, voice=1)
        result = merge(base, _delta(manner=None), features)
        assert "manner" not in result
        for child in ("continuant", "sonorant", "nasal", "lateral"):
            assert child not in result
        # A feature outside the subtree is untouched.
        assert result["voice"].value == 1

    def test_set_daughter_adds_its_ancestor_nodes(self, features):
        # The mirror of the delink: a delta that sets a daughter (nasal) pulls in its
        # mother node (manner), so the merged segment is geometrically well-formed.
        result = merge(_fb(voice=1), _delta(nasal=1), features)
        assert result["nasal"].value == 1
        assert result["manner"].value == 1  # nasal's parent, completed by the upward pass

    def test_upward_completion_is_scoped_to_the_delta(self, features):
        # Only what the delta sets is completed. A base feature missing its ancestor
        # is left alone, so the pass cannot mask a pre-existing orphan.
        base = _fb(nasal=1)  # nasal without its parent manner — an incomplete base
        result = merge(base, _delta(voice=0), features)
        assert "manner" not in result  # not added: nasal came from the base, not the delta

    def test_does_not_mutate_base(self, features):
        base = _fb(nasal=1)
        merge(base, _delta(nasal=None), features)
        assert base["nasal"].value == 1
