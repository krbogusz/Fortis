"""The morpheme-boundary token ``-``.

A ``-`` in a word is a real, deletable segment that forces a syllable break and is
matched only by a ``-`` rule element. These tests exercise the whole pipeline on the
shipped default project: lexing, parsing, segmentation, syllabification, matching,
deletion, insertion, rendering, and accuracy.
"""

import pytest

from src.fortis.analysis.accuracy import (
    comparable_bundles,
    edit_distance,
    feature_edit_distance,
    form_phones,
    try_segment,
)
from src.fortis.application.deriving import apply_rule
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.syllabifying import syllabify
from src.fortis.models.bundles import is_morpheme_boundary
from src.fortis.models.elements import MorphemeBoundary, Null
from src.fortis.models.rules import ApplicationMode, Rule
from src.fortis.parsing.lexer import Token, lex
from src.fortis.parsing.notation import parse_definition


def _boundaries(form, project):
    return syllabify(
        form.bundles(), project.sonorities, project.syllable_parts, project.time, project.letters
    )


def _render(form, project):
    return render_syllabified(form.bundles(), _boundaries(form, project), project)


def _rule(definition: str, project, mode: ApplicationMode = ApplicationMode.simultaneous) -> Rule:
    sd = parse_definition(definition, project.features)
    assert sd.is_ok(), sd.unwrap_err()
    return Rule(
        id=definition, raw_definition=definition, sd=sd.unwrap(), application=mode, time=0, name=""
    )


def _apply(rule: Rule, word: str, project):
    form = string_to_sequence(word, project)
    out = apply_rule(
        rule, form, project.letters, project.features, project.sonorities,
        project.syllable_parts, project.tiers,
    )
    return form, out


# -- lexing / parsing ------------------------------------------------------------------


def test_lone_dash_lexes_as_a_boundary_token():
    kinds = [(t.kind, t.text) for t in lex("- -> ∅")]
    assert kinds[0] == (Token.BOUNDARY, "-")
    assert kinds[1][0] is Token.ARROW  # the '->' still wins when a '>' follows


def test_dash_parses_to_a_morpheme_boundary_element(project):
    sd = parse_definition("- -> ∅", project.features).unwrap()
    assert sd.target == (MorphemeBoundary(),)
    assert sd.result == (Null(),)


def test_value_dash_inside_a_bundle_is_untouched(project):
    # '-' as a negative value lives inside opaque brackets, so it never lexes as a boundary.
    sd = parse_definition("[-voice] -> [+voice]", project.features)
    assert sd.is_ok(), sd.unwrap_err()


# -- segmentation ----------------------------------------------------------------------


def test_dash_segments_to_a_boundary_segment(project):
    form = string_to_sequence("at-a", project)
    assert len(form.segments) == 4
    assert [is_morpheme_boundary(s.bundle) for s in form.segments] == [False, False, True, False]


# -- syllabification -------------------------------------------------------------------


def test_boundary_forces_a_syllable_break(project):
    # Without the boundary, MOP puts t in the onset (a.ta); the boundary forces it into
    # the coda of the first syllable (at.a), rendered at-a.
    assert _render(string_to_sequence("ata", project), project) == "a.ta"
    assert _render(string_to_sequence("at-a", project), project) == "at-a"


def test_boundary_splits_a_cluster(project):
    assert _render(string_to_sequence("at-pa", project), project) == "at-pa"


def test_boundary_renders_without_a_doubled_dot(project):
    assert "." not in _render(string_to_sequence("at-a", project), project)


# -- matching / rewriting --------------------------------------------------------------


def test_rule_deletes_the_boundary_and_form_resyllabifies(project):
    _, out = _apply(_rule("- -> ∅", project), "at-a", project)
    assert _render(out, project) == "a.ta"  # boundary gone → t re-syllabifies into the onset


def test_deletion_rule_leaves_a_boundary_free_word_untouched(project):
    form, out = _apply(_rule("- -> ∅", project), "ata", project)
    assert out is form  # no locus ⇒ the same object back (identity contract)


def test_boundary_is_matchable_in_context(project):
    _, out = _apply(_rule("t -> d / _ -", project), "at-a", project)
    assert _render(out, project) == "ad-a"


def test_context_boundary_blocks_when_absent(project):
    form, out = _apply(_rule("t -> d / _ -", project), "ata", project)
    assert out is form


def test_ordinary_pattern_does_not_match_a_boundary(project):
    # A wildcard-deletion after 'a' removes the 't', not the boundary sitting between them.
    _, out = _apply(_rule("[] -> ∅ / a _", project), "a-ta", project)
    assert _render(out, project) == "a-ta"  # 'a' then boundary: nothing deletable right after 'a'


def test_rule_can_insert_a_boundary(project):
    _, out = _apply(_rule("∅ -> - / a _ t", project), "ata", project)
    assert _render(out, project) == "a-ta"


@pytest.mark.parametrize("mode", [ApplicationMode.left_to_right, ApplicationMode.right_to_left])
def test_boundary_deletion_works_in_a_directional_scan(project, mode):
    _, out = _apply(_rule("- -> ∅", project, mode), "at-a", project)
    assert _render(out, project) == "a.ta"


@pytest.mark.parametrize(("word", "rendered"), [("-ata", "-a.ta"), ("ata-", "a.ta-")])
def test_word_edge_boundary_renders(project, word, rendered):
    assert _render(string_to_sequence(word, project), project) == rendered


# -- accuracy ---------------------------------------------------------------------------


def test_grader_treats_a_boundary_as_structural(project):
    with_boundary, without = try_segment("at-a", project), try_segment("ata", project)
    assert with_boundary is not None and without is not None  # both are well-formed IPA
    assert form_phones(with_boundary, project) == ["a", "t", "a"]  # the boundary is not a phone
    swap = project.settings.accuracy.transposition_cost
    assert (
        edit_distance(form_phones(with_boundary, project), form_phones(without, project), swap)
        == 0
    )
    assert (
        feature_edit_distance(
            comparable_bundles(with_boundary), comparable_bundles(without), swap
        )
        == 0
    )
