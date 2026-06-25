"""Regression tests for bugs found in the bug hunt — each reproduces a fixed defect.

Self-contained (load the real inventories where a bug depends on real data) so a
reintroduced bug fails loudly here rather than silently returning a wrong result.
"""

import pytest

from src.fortis.application.applying import apply_match
from src.fortis.application.combining import merge
from src.fortis.application.matching import find_matches
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.loaders.features import load_feature_inventory, load_short
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.specs import FeatureSpec
from src.fortis.parsing.bundles import determine_contour_position, parse_feature_spec
from src.fortis.parsing.notation import parse_definition


def _fb(**features):
    return FeatureBundle({f: FeatureSpec(feature=f, value=v) for f, v in features.items()})


def test_bare_feature_matches_any_value(project):
    # `[cons]` means "consonantal present with any value" — it must match both
    # +cons and -cons segments, not silently match nothing.
    sd = parse_definition("[cons] -> [+voice]", project.features).unwrap()
    spans = [(m.start, m.end) for m in find_matches(sd, [_fb(consonantal=1), _fb(consonantal=0)])]
    assert spans == [(0, 1), (1, 2)]


def test_value_label_matching_a_feature_name(project):
    # `tone: high` must resolve to feature `tone`, not the feature `high` that the
    # value label `high` happens to spell.
    spec = parse_feature_spec("tone: high", project.features)
    assert spec.is_ok() and spec.unwrap().feature == "tone"


def test_blank_short_field_defaults_to_feature_name():
    # A whitespace-only `short` defaults to the feature name (was: silently "").
    assert load_short("nasal", {"short": "   "}).unwrap() == "nasal"


def test_leading_diacritic_raises_cleanly(project):
    # A diacritic with no preceding segment/nucleus is a clean ValueError, not an
    # uncaught IndexError or a silent misattachment to the wrong segment.
    with pytest.raises(ValueError):
        string_to_sequence("ʰa", project)  # segment-tier diacritic, no base
    with pytest.raises(ValueError):
        string_to_sequence("t˥a", project)  # tone before any nucleus


def test_contour_position_zero_rejected():
    # Contour positions are 1-based; the single-index path must reject 0.
    assert determine_contour_position("0").is_err()


def test_variable_count_with_a_multi_segment_bound(project):
    # A bound multi-segment group consumes >1 segment; the variable quantifier's
    # repetition count must subtract its real width, not assume width 1.
    sd = parse_definition("1=([+cons][+cons]) [-syll]* -> @1 a*", project.features).unwrap()
    segs = [_fb(consonantal=1), _fb(consonantal=1),
            _fb(consonantal=1, syllabic=0), _fb(consonantal=1, syllabic=0)]
    match = next(m for m in find_matches(sd, segs, project.letters) if (m.start, m.end) == (0, 4))
    out = apply_match(sd, match, segs, project.letters, project.features)
    assert len(out) == 4  # @1 replays 2 + a* repeats 2; was 5 (count inflated by 1)


def test_upward_geometry_skips_a_non_unary_ancestor(tmp_path):
    # Setting a daughter pulls in unary class nodes, but a scalar/binary ancestor
    # carries a value that can't be inferred — so it must NOT be fabricated.
    toml = tmp_path / "features.toml"
    toml.write_text(
        'place = { tier = "segment", kind = "scalar", short = "pl", '
        'values = { 1 = "labial" }, children = ["anterior"] }\n'
        'anterior = { tier = "segment", kind = "binary", short = "ant" }\n'
    )
    inv = load_feature_inventory(toml).unwrap()
    out = merge(FeatureBundle(), _fb(anterior=1), inv)
    assert "anterior" in out and "place" not in out
