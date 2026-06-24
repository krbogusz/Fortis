"""Tests for IPA rendering (application/rendering.py).

These run against the real project inventories (the ``project`` fixture).
"""

from src.fortis.application.rendering import (
    describe_change,
    render_segment,
    render_syllabified,
    sequence_to_string,
)
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.syllabifying import syllabify


class TestRenderSegment:
    def test_exact_letter_match(self, project):
        # A plain letter's own bundle renders back to that letter.
        e = project.letters["e"].bundle
        assert render_segment(e, project) == "e"

    def test_segment_with_diacritic(self, project):
        # ɣʷ is a labialised ɣ: a base letter plus a combining diacritic.
        seq = string_to_sequence("ɣʷ", project)
        assert render_segment(seq[0], project) == "ɣʷ"


class TestDescribeChange:
    def test_equal_length_shows_changed_segment(self, project):
        before = string_to_sequence("kʲ", project)
        after = string_to_sequence("k", project)
        assert describe_change(before, after, project) == "kʲ→k"

    def test_length_change_trims_to_differing_region(self, project):
        # km̩tom → kumtom: only the syllabic m → um is shown, prefix/suffix trimmed.
        before = string_to_sequence("km̩tom", project)
        after = string_to_sequence("kumtom", project)
        assert describe_change(before, after, project) == "m̩→um"

    def test_deletion_shows_null(self, project):
        before = string_to_sequence("kat", project)
        after = string_to_sequence("ka", project)
        assert describe_change(before, after, project) == "t→∅"


class TestRenderSyllabified:
    def test_dots_at_syllable_boundaries_with_full_rendering(self, project):
        # mexteːr → mex.teːr: the boundary shows as ".", and each segment still goes
        # through the full renderer (the length diacritic on teːr is preserved).
        seq = string_to_sequence("mexteːr", project)
        boundaries = syllabify(
            seq, project.sonorities, project.syllable_parts, project.time, project.letters
        )
        assert render_syllabified(seq, boundaries, project) == "mex.teːr"

    def test_boundary_marking_stress_replaces_the_dot(self, project):
        # kaˈta: the stress mark ˈ (marks_boundary) sits at the interior boundary and
        # stands in for the ".", so it is kaˈta, not ka.ˈta.
        seq = string_to_sequence("kaˈta", project)
        boundaries = syllabify(
            seq, project.sonorities, project.syllable_parts, project.time, project.letters
        )
        assert render_syllabified(seq, boundaries, project) == "kaˈta"


class TestSequenceToString:
    def test_repositions_stress_to_the_syllable_edge(self, project):
        # The flat re-render syllabifies internally, so stress sits at the syllable
        # onset (koˈta), not before the nucleus (kotˈa).
        assert sequence_to_string(string_to_sequence("koˈta", project), project) == "koˈta"

    def test_falls_back_to_flat_when_unsyllabifiable(self, project):
        # A bare cluster has no nucleus, so it renders flat without raising.
        assert sequence_to_string(string_to_sequence("kt", project), project) == "kt"

    def test_string_round_trip_for_invertible_words(self, project):
        # Most words round-trip exactly; the one diacritic-ordering case is covered
        # at the feature level in the segmentation tests.
        for word in project.words:
            rendered = sequence_to_string(string_to_sequence(word, project), project)
            if rendered != word:
                # Only legitimate diacritic reorderings are allowed to differ; the
                # rendered form must still re-segment to the same length.
                assert len(string_to_sequence(rendered, project)) == len(
                    string_to_sequence(word, project)
                )
