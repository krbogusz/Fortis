"""Tests for notation rendering (src/fortis/induction/notation.py)."""

from src.fortis.induction.notation import (
    render_bundle,
    render_feature,
    render_feature_element,
)
from src.fortis.parsing.bundles import parse_pattern_bundle


class TestRenderFeature:
    def test_unary_present_is_the_bare_name(self, synth):
        # nasal is unary in the Latin project.
        assert render_feature("nasal", 1, synth.features) == "nasal"

    def test_binary_is_signed(self, synth):
        assert render_feature("voice", 1, synth.features) == "+voice"
        assert render_feature("voice", 0, synth.features) == "-voice"

    def test_scalar_is_colon_labelled(self, synth):
        # aperture is scalar {low, mid, high}; render the label, not the code.
        rendered = render_feature("aperture", 1, synth.features)
        assert rendered is not None and rendered.startswith("aperture: ")

    def test_unrenderable_value_is_none(self, synth):
        assert render_feature("voice", "any", synth.features) is None
        assert render_feature("not_a_feature", 1, synth.features) is None
        assert render_feature("voice", True, synth.features) is None  # bool is not a code


class TestRoundTrip:
    def _bundle_of(self, synth, source: str):
        from src.fortis.analysis.accuracy import segment_form

        bundles = segment_form(source, synth)
        assert bundles is not None
        return bundles[0]

    def test_rendered_element_parses_back(self, synth):
        # [aperture: high] must parse to the same feature/value it was rendered from.
        element = render_feature_element("aperture", 1, synth.features)
        assert element is not None
        parsed = parse_pattern_bundle(element.strip("[]"), synth.features).unwrap()
        assert parsed["aperture"].value == 1

    def test_bundle_round_trips_specified_features(self, synth):
        # Render a real segment's bundle, parse it back, and confirm every specified value
        # survives — the property the candidate generator relies on.
        bundle = self._bundle_of(synth, "t̪")
        rendered = render_bundle(bundle, synth.features)
        assert rendered is not None
        parsed = parse_pattern_bundle(rendered.strip("[]"), synth.features).unwrap()
        for feature, spec in bundle.items():
            if isinstance(spec.value, int) and not isinstance(spec.value, bool):
                assert parsed[feature].value == spec.value

    def test_empty_bundle_is_none_not_wildcard(self, synth):
        from src.fortis.models.bundles import FeatureBundle

        # An empty render would be "[]", which the parser reads as a wildcard — must be None.
        assert render_bundle(FeatureBundle(), synth.features) is None
