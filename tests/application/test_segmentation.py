"""Tests for IPA segmentation (application/segmentation.py).

These run against the real project inventories (the ``project`` fixture).
"""

import pytest

from src.fortis.application.combining import matches_exactly
from src.fortis.application.rendering import sequence_to_string
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.tiers import Tier


def _feature_equal(a, b) -> bool:
    """Whether two segment sequences carry the same features, segment for segment."""
    return len(a) == len(b) and all(matches_exactly(x, y) for x, y in zip(a, b, strict=True))


class TestStringToSequence:
    def test_known_word_segments(self, project):
        # xenti is five segments: x e n t i.
        assert len(string_to_sequence("xenti", project).bundles()) == 5

    def test_diacritics_attach_to_their_base(self, project):
        # ɣʷeroː is four segments — the labialisation and length are diacritics on
        # their bases, not separate segments.
        assert len(string_to_sequence("ɣʷeroː", project).bundles()) == 4

    def test_unknown_character_raises(self, project):
        with pytest.raises(ValueError):
            string_to_sequence("xen§ti", project)  # a section sign is not in any inventory

    def test_syllable_tier_diacritic_attaches_to_nucleus(self, project):
        # A syllable-tier tone mark written after the coda must land on the syllable's
        # nucleus, not an earlier segment. ("̄" is tone 3.) Guards the last_nucleus_index
        # path, which no plain lexicon word exercises. Tone now lives on the tier, so
        # read it back per-segment via lower_tiers.
        seq = lower_tiers(string_to_sequence("tan" + "̄", project))
        assert [("tone" in s) for s in seq] == [False, True, False]  # tone on the a, not t/n

    def test_word_initial_nucleus_tier_diacritic(self, project):
        # The nucleus is segment 0 here; the tone must land on it (not index -1).
        seq = lower_tiers(string_to_sequence("an" + "̄", project))
        assert seq[0]["tone"].value == 3

    def test_stress_attaches_to_a_diacritic_made_nucleus(self, project):
        # ˈl̩ : the syllabic diacritic makes l a nucleus *after* the letter is read;
        # the pending stress must still attach to it (not get stranded / skipped).
        seq = lower_tiers(string_to_sequence("ˈl̩", project))
        assert "stress" in seq[0]

    def test_stress_not_stolen_by_a_later_plain_vowel(self, project):
        # ˈl̩a : stress belongs to the syllabic l̩, not the following plain vowel a.
        seq = lower_tiers(string_to_sequence("ˈl̩a", project))
        assert "stress" in seq[0] and "stress" not in seq[1]


class TestRoundTrip:
    def test_feature_level_round_trip_for_all_words(self, project):
        # Render-then-resegment recovers the same segments for every lexicon word.
        # (String equality can differ only by diacritic ordering, e.g. gʲʱ vs gʱʲ —
        # the same feature bundle written two ways — so the feature level is the
        # invariant that must hold.)
        for word in project.words:
            seq = string_to_sequence(word, project).bundles()
            reseg = string_to_sequence(sequence_to_string(seq, project), project).bundles()
            assert _feature_equal(seq, reseg), word


class TestFloatingTone:
    _FLOAT_HIGH = "⟨◌́⟩"  # a floating high tone (dotted circle + combining acute, in float brackets)

    def test_marker_creates_a_positioned_float(self, project):
        form = string_to_sequence("kata" + self._FLOAT_HIGH, project)
        assert len(form.segments) == 4  # the marker adds no segment
        tier = form.tiers["tone"]
        assert len(tier.autosegs) == 1
        autoseg = tier.autosegs[0]
        assert autoseg.bundle["tone"].value == 4  # high
        assert not any(a == autoseg.id for (a, _s) in tier.links)  # floating, no anchor
        assert tier.float_hosts[autoseg.id] == (3, "after")  # after the final segment

    def test_word_initial_float_is_before_the_first_segment(self, project):
        form = string_to_sequence(self._FLOAT_HIGH + "kata", project)
        autoseg = form.tiers["tone"].autosegs[0]
        assert form.tiers["tone"].float_hosts[autoseg.id] == (0, "before")

    def test_unterminated_float_marker_rejected(self, project):
        with pytest.raises(ValueError, match="unterminated floating tone"):
            string_to_sequence("ka⟨◌́", project)


def test_stress_survives_a_diacritic_that_unmakes_the_nucleus(project):
    """A ˈ is not lost when the syllable's first vowel is made non-syllabic by a diacritic.

    The mark is buffered and flushed onto the first segment that is a nucleus AT LETTER-APPEND
    time. In `ˈe̯a`, the letter `e` IS syllabic when appended and so claims the stress — and then
    the `̯` makes it non-syllabic, no tier can anchor the autoseg (`anchor: +syllabic`) and
    `stray_erase` deleted it. `ˈɲaws` kept its stress; `ˈɲe̯aws` silently lost it, in the
    lexicon's ATTESTED forms as much as in derived ones (targets are ingested through here).
    The suprasegmentals must be handed back so the syllable's real nucleus claims them.
    """
    syllable = frozenset(
        name for name, feature in project.features.items() if feature.tier == Tier.syllable
    )

    def carriers(text: str) -> list[dict]:
        form = string_to_sequence(text, project)
        return [
            {f: bundle[f].value for f in syllable & set(bundle.data)}
            for bundle in lower_tiers(form)
            if syllable & set(bundle.data)
        ]

    plain = carriers("ˈnaws")  # control: no unmaking diacritic
    assert plain == [{"stress": 2}]
    # The on-glide is made non-syllabic; the stress must move on to the real nucleus, not vanish.
    assert carriers("ˈne̯aws") == [{"stress": 2}]
    assert carriers("ˈe̯aws") == [{"stress": 2}]
