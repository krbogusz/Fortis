"""Tests for the Fortis rule engine: parsing, inventory loading, and application."""

from __future__ import annotations

import pytest

from src.fortis.inventories.feature_definition import FeatureDefinition
from src.fortis.inventories.feature_inventory import FeatureInventory
from src.fortis.inventories.rule_inventory import RuleInventory, _parse_key
from src.fortis.models.feature_bundle import FeatureBundle
from src.fortis.models.feature_spec import FeatureSpec
from src.fortis.models.feature_type import FeatureType
from src.fortis.models.sequence import Sequence
from src.fortis.models.tiers import Tier
from src.fortis.rules.apply import apply_rules, find_loci
from src.fortis.rules.elements import Application, Binding, Boundary, Bundle, Disjunction, Element, Group, Null, Quantifier, Ref, _ONE
from src.fortis.rules.match import match
from src.fortis.rules.parsing import parse_spe_definition
from src.fortis.rules.rule import Rule

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def inventory():
    """A small feature inventory for testing rules."""
    return FeatureInventory(
        {
            "consonantal": FeatureDefinition(
                name="consonantal",
                tier=Tier.segment,
                type=FeatureType.binary,
                short="cons",
                values={0: "absent", 1: "present"},
                children=None,
            ),
            "syllabic": FeatureDefinition(
                name="syllabic",
                tier=Tier.segment,
                type=FeatureType.binary,
                short="syll",
                values={0: "absent", 1: "present"},
                children=None,
            ),
            "nasal": FeatureDefinition(
                name="nasal",
                tier=Tier.segment,
                type=FeatureType.unary,
                short="nas",
                values={1: "present"},
                children=None,
            ),
            "voice": FeatureDefinition(
                name="voice",
                tier=Tier.segment,
                type=FeatureType.binary,
                short="vc",
                values={0: "absent", 1: "present"},
                children=None,
            ),
            "height": FeatureDefinition(
                name="height",
                tier=Tier.segment,
                type=FeatureType.scalar,
                short="ht",
                values={1: "low", 2: "mid", 3: "high"},
                children=None,
            ),
        }
    )


def _bundle(**specs: int | list[int | None] | None) -> FeatureBundle:
    """Helper to build a FeatureBundle from keyword arguments."""
    data: dict[str, FeatureSpec] = {f: FeatureSpec(f, v) for f, v in specs.items()}
    return FeatureBundle(data)


def _seq(*specs: dict[str, int | list[int | None] | None]) -> Sequence:
    """Helper to build a Sequence from feature-spec dicts."""
    bundles: list[FeatureBundle] = []
    for s in specs:
        data: dict[str, FeatureSpec] = {f: FeatureSpec(f, v) for f, v in s.items()}
        bundles.append(FeatureBundle(data))
    return Sequence(bundles)


# ---------------------------------------------------------------------------
# SPE Definition Parser
# ---------------------------------------------------------------------------


class TestParseSPEBasic:
    """Test basic SPE definition parsing."""

    def test_simple_rule_with_unicode_arrow(self, inventory):
        result = parse_spe_definition("[+cons, -syll] → [-vc] / _#", inventory)
        assert result.is_ok()
        target, result_elems, left_ctx, right_ctx, _, _ = result.unwrap()
        assert len(target) == 1
        assert isinstance(target[0], Bundle)
        assert len(result_elems) == 1
        assert isinstance(result_elems[0], Bundle)

    def test_simple_rule_with_ascii_arrow(self, inventory):
        result = parse_spe_definition("[+cons, -syll] -> [-vc] / _#", inventory)
        assert result.is_ok()

    def test_rule_without_context(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc]", inventory)
        assert result.is_ok()
        _, _, left_ctx, right_ctx, _, _ = result.unwrap()
        assert left_ctx is None
        assert right_ctx is None

    def test_missing_arrow_returns_error(self, inventory):
        result = parse_spe_definition("[+cons] [-vc]", inventory)
        assert result.is_err()

    def test_empty_target_returns_error(self, inventory):
        result = parse_spe_definition(" -> [-vc] / _#", inventory)
        assert result.is_err()

    def test_empty_result_returns_error(self, inventory):
        result = parse_spe_definition("[+cons] ->  / _#", inventory)
        assert result.is_err()


class TestParseSPEContext:
    """Test context parsing."""

    def test_right_boundary(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / _#", inventory)
        assert result.is_ok()
        _, _, left_ctx, right_ctx, _, _ = result.unwrap()
        assert left_ctx is None
        assert right_ctx is not None
        # Right context should end with a word boundary
        assert isinstance(right_ctx[-1], Boundary)
        assert right_ctx[-1].kind == "word"

    def test_left_boundary(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / #_", inventory)
        assert result.is_ok()
        _, _, left_ctx, right_ctx, _, _ = result.unwrap()
        assert left_ctx is not None
        assert right_ctx is None
        # Left context should end with a word boundary (outermost edge)
        assert isinstance(left_ctx[-1], Boundary)
        assert left_ctx[-1].kind == "word"

    def test_left_context_feature_bundle(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas]_", inventory)
        assert result.is_ok()
        _, _, left_ctx, _, _, _ = result.unwrap()
        assert left_ctx is not None
        assert len(left_ctx) == 1
        assert isinstance(left_ctx[0], Bundle)

    def test_right_context_feature_bundle(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / _[+nas]", inventory)
        assert result.is_ok()
        _, _, _, right_ctx, _, _ = result.unwrap()
        assert right_ctx is not None
        assert len(right_ctx) >= 1
        assert isinstance(right_ctx[0], Bundle)

    def test_both_contexts(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas]_[+syll]", inventory)
        assert result.is_ok()
        _, _, left_ctx, right_ctx, _, _ = result.unwrap()
        assert left_ctx is not None
        assert right_ctx is not None

    def test_both_boundaries(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / #[+nas]_[+syll]#", inventory)
        assert result.is_ok()

    def test_context_without_underscore_returns_error(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas]", inventory)
        assert result.is_err()

    def test_multi_segment_left_context(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas][+cons]_", inventory)
        assert result.is_ok()
        _, _, left_ctx, _, _, _ = result.unwrap()
        assert left_ctx is not None
        # Left context has 2 feature bundles (reversed to adjacent-first order)
        bundles = [el for el in left_ctx if isinstance(el, Bundle)]
        assert len(bundles) == 2

    def test_underscore_alone_means_no_context(self, inventory):
        result = parse_spe_definition("[+cons] -> [-vc] / _", inventory)
        assert result.is_ok()
        _, _, left_ctx, right_ctx, _, _ = result.unwrap()
        # Underscore alone means no context constraints
        assert left_ctx is None
        assert right_ctx is None


class TestParseSPEFeatureBundles:
    """Test that feature bundles in rules are parsed correctly."""

    def test_target_bundle_has_correct_features(self, inventory):
        result = parse_spe_definition("[+cons, -syll] → [-vc] / _#", inventory)
        assert result.is_ok()
        target, _, _, _, _, _ = result.unwrap()
        assert isinstance(target[0], Bundle)
        bundle = target[0].bundle
        assert "consonantal" in bundle
        assert bundle["consonantal"].value == 1
        assert "syllabic" in bundle
        assert bundle["syllabic"].value == 0

    def test_result_bundle_has_correct_features(self, inventory):
        result = parse_spe_definition("[+cons, -syll] → [-vc] / _#", inventory)
        assert result.is_ok()
        _, result_elems, _, _, _, _ = result.unwrap()
        assert isinstance(result_elems[0], Bundle)
        bundle = result_elems[0].bundle
        assert "voice" in bundle
        assert bundle["voice"].value == 0


# ---------------------------------------------------------------------------
# TOML Key Parsing
# ---------------------------------------------------------------------------


class TestParseKey:
    """Test TOML key parsing for time and ID."""

    def test_valid_key(self):
        time_val, rule_id = _parse_key("1200.final_devoicing")
        assert time_val == 1200
        assert rule_id == "final_devoicing"

    def test_zero_time(self):
        time_val, rule_id = _parse_key("0.first_rule")
        assert time_val == 0
        assert rule_id == "first_rule"

    def test_no_dot_returns_none(self):
        time_val, _ = _parse_key("no_dot_here")
        assert time_val is None

    def test_non_integer_time(self):
        time_val, _ = _parse_key("abc.rule_id")
        assert time_val is None


# ---------------------------------------------------------------------------
# RuleInventory Loading
# ---------------------------------------------------------------------------


class TestRuleInventoryLoad:
    """Test loading rules from TOML."""

    def test_load_real_rules_toml(self, inventory, tmp_path):
        toml_content = """
[1200.final_devoicing]
name = "Final devoicing"
description = "Devoices the final consonant in a sequence"
definition = "[+cons, -syll] → [-vc] / _#"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_ok()
        rules = result.unwrap()
        assert "final_devoicing" in rules
        rule = rules["final_devoicing"]
        assert rule.name == "Final devoicing"
        assert rule.time == 1200

    def test_load_multiple_rules(self, inventory, tmp_path):
        toml_content = """
[100.rule_a]
name = "Rule A"
description = "First rule"
definition = "[+cons] -> [-vc] / _#"

[200.rule_b]
name = "Rule B"
description = "Second rule"
definition = "[+nas] -> [+cons] / _#"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_ok()
        rules = result.unwrap()
        assert len(rules) == 2

    def test_sorted_rules_by_time(self, inventory, tmp_path):
        toml_content = """
[200.rule_b]
name = "Rule B"
description = "Second rule"
definition = "[+nas] -> [+cons] / _#"

[100.rule_a]
name = "Rule A"
description = "First rule"
definition = "[+cons] -> [-vc] / _#"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_ok()
        rules = result.unwrap()
        sorted_rules = rules.sorted_rules
        assert sorted_rules[0].rule_id == "rule_a"
        assert sorted_rules[0].time == 100
        assert sorted_rules[1].rule_id == "rule_b"
        assert sorted_rules[1].time == 200

    def test_invalid_key_format(self, inventory, tmp_path):
        toml_content = """
[invalid_key]
name = "Bad rule"
description = "No time"
definition = "[+cons] -> [-vc] / _#"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_err()

    def test_missing_definition(self, inventory, tmp_path):
        toml_content = """
[100.bad_rule]
name = "Bad rule"
description = "Missing definition"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_err()


# ---------------------------------------------------------------------------
# Match Generator
# ---------------------------------------------------------------------------


class TestMatchBundle:
    """Test matching Bundle elements against a Sequence."""

    def test_match_single_bundle(self, inventory):
        """A Bundle with quantifier (1,1) matches exactly one segment."""
        cons_bundle = _bundle(consonantal=1)
        elements: list[Element] = [Bundle(bundle=cons_bundle)]
        seq = _seq({"consonantal": 1, "voice": 1})
        results = list(match(elements, seq, 0))
        assert len(results) == 1
        assert results[0][0] == 1  # next_pos after consuming one segment

    def test_no_match(self, inventory):
        """A Bundle that doesn't match yields nothing."""
        cons_bundle = _bundle(consonantal=1)
        elements: list[Element] = [Bundle(bundle=cons_bundle)]
        seq = _seq({"consonantal": 0, "voice": 0})
        results = list(match(elements, seq, 0))
        assert len(results) == 0

    def test_match_beyond_sequence(self, inventory):
        """Matching beyond the end of the sequence yields nothing."""
        cons_bundle = _bundle(consonantal=1)
        elements: list[Element] = [Bundle(bundle=cons_bundle)]
        seq = _seq({"consonantal": 1})
        results = list(match(elements, seq, 1))  # pos=1 is beyond end
        assert len(results) == 0


class TestMatchBoundary:
    """Test matching Boundary elements."""

    def test_word_boundary_at_start(self, inventory):
        """# matches at position 0."""
        elements: list[Element] = [Boundary(kind="word")]
        seq = _seq({"consonantal": 1})
        results = list(match(elements, seq, 0))
        assert len(results) == 1
        assert results[0][0] == 0  # zero-width, doesn't consume

    def test_word_boundary_at_end(self, inventory):
        """# matches at the end of the sequence."""
        elements: list[Element] = [Boundary(kind="word")]
        seq = _seq({"consonantal": 1})
        results = list(match(elements, seq, 1))  # end position
        assert len(results) == 1
        assert results[0][0] == 1  # zero-width

    def test_word_boundary_in_middle_fails(self, inventory):
        """# does not match in the middle of the sequence."""
        elements: list[Element] = [Boundary(kind="word")]
        seq = _seq({"consonantal": 1}, {"consonantal": 0})
        results = list(match(elements, seq, 1))  # middle position
        assert len(results) == 0


class TestMatchSequence:
    """Test matching multiple elements in sequence."""

    def test_match_bundle_then_boundary(self, inventory):
        """Match a Bundle followed by a word boundary."""
        cons_bundle = _bundle(consonantal=1)
        elements: list[Element] = [Bundle(bundle=cons_bundle), Boundary(kind="word")]
        seq = _seq({"consonantal": 1})
        results = list(match(elements, seq, 0))
        assert len(results) == 1
        assert results[0][0] == 1  # consumed one segment, then at boundary

    def test_match_two_bundles(self, inventory):
        """Match two consecutive bundles."""
        cons_bundle = _bundle(consonantal=1)
        nas_bundle = _bundle(nasal=1)
        elements: list[Element] = [Bundle(bundle=cons_bundle), Bundle(bundle=nas_bundle)]
        seq = _seq(
            {"consonantal": 1, "nasal": 1},
            {"consonantal": 0, "nasal": 1},
        )
        # Should match starting at pos=0: first bundle matches seg 0, second matches seg 1
        results = list(match(elements, seq, 0))
        assert len(results) == 1
        assert results[0][0] == 2


# ---------------------------------------------------------------------------
# Rule Application — Locus Finding
# ---------------------------------------------------------------------------


class TestFindLoci:
    """Test finding loci where rules match."""

    def test_final_devoicing_locus(self, inventory):
        """Final devoicing rule matches at end of sequence."""
        rule = Rule(
            rule_id="final_devoicing",
            name="Final devoicing",
            description="",
            time=1200,
            target=[Bundle(bundle=_bundle(consonantal=1, syllabic=0))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=[Boundary(kind="word")],
        )
        # Sequence: /bad/ → [b, a, d] where d is [+cons, -syll, +vc]
        seq = _seq(
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # b
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # d
        )
        loci = find_loci(rule, seq)
        assert len(loci) == 1
        assert loci[0].start == 2  # d is at position 2
        assert loci[0].end == 3

    def test_no_locus_when_context_fails(self, inventory):
        """No locus when context doesn't match."""
        rule = Rule(
            rule_id="final_devoicing",
            name="Final devoicing",
            description="",
            time=1200,
            target=[Bundle(bundle=_bundle(consonantal=1, syllabic=0))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=[Boundary(kind="word")],
        )
        # Sequence: /badu/ → [b, a, d, u] where d is NOT at the end
        seq = _seq(
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # b
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # d
            {"consonantal": 0, "syllabic": 1},  # u
        )
        loci = find_loci(rule, seq)
        assert len(loci) == 0

    def test_unconditional_rule_matches_everywhere(self, inventory):
        """A rule without context matches every occurrence."""
        rule = Rule(
            rule_id="unconditional",
            name="Unconditional",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=None,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},  # b
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "voice": 1},  # d
        )
        loci = find_loci(rule, seq)
        assert len(loci) == 2  # matches at positions 0 and 2


# ---------------------------------------------------------------------------
# Rule Application — Apply Rules
# ---------------------------------------------------------------------------


class TestApplyRules:
    """Test the full rule application pipeline."""

    def test_final_devoicing(self, inventory):
        """Final devoicing: /bad/ → [b, a, t] (voiceless)."""
        rule = Rule(
            rule_id="final_devoicing",
            name="Final devoicing",
            description="",
            time=1200,
            target=[Bundle(bundle=_bundle(consonantal=1, syllabic=0))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=[Boundary(kind="word")],
        )
        seq = _seq(
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # b
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "syllabic": 0, "voice": 1},  # d → t
        )
        result = apply_rules(seq, [rule])
        # The final consonant should be devoiced
        assert result.data[2]["voice"].value == 0
        # But the initial consonant should still be voiced
        assert result.data[0]["voice"].value == 1

    def test_no_match_leaves_sequence_unchanged(self, inventory):
        """If no rule matches, the sequence is unchanged."""
        rule = Rule(
            rule_id="final_devoicing",
            name="Final devoicing",
            description="",
            time=1200,
            target=[Bundle(bundle=_bundle(consonantal=1, syllabic=0))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=[Boundary(kind="word")],
        )
        # /badu/ — d is not at the end
        seq = _seq(
            {"consonantal": 1, "syllabic": 0, "voice": 1},
            {"consonantal": 0, "syllabic": 1},
            {"consonantal": 1, "syllabic": 0, "voice": 1},
            {"consonantal": 0, "syllabic": 1},
        )
        result = apply_rules(seq, [rule])
        assert len(result.data) == 4
        # No changes should have been made
        assert result.data[0]["voice"].value == 1
        assert result.data[2]["voice"].value == 1

    def test_multiple_matches_simultaneous(self, inventory):
        """Multiple matches in one rule pass are applied simultaneously."""
        rule = Rule(
            rule_id="devoice_all_cons",
            name="Devoice all consonants",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=None,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},  # voiced → voiceless
            {"consonantal": 0, "syllabic": 1},  # vowel, unchanged
            {"consonantal": 1, "voice": 1},  # voiced → voiceless
        )
        result = apply_rules(seq, [rule])
        assert result.data[0]["voice"].value == 0
        assert result.data[1].get("voice") is None or result.data[1]["voice"].value != 0
        assert result.data[2]["voice"].value == 0

    def test_left_context_match(self, inventory):
        """Rule with left context: devoice after nasal."""
        rule = Rule(
            rule_id="post_nasal_voicing",
            name="Post-nasal voicing",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1, voice=0))],
            result=[Bundle(bundle=_bundle(voice=1))],
            left_context=[Bundle(bundle=_bundle(nasal=1))],
            right_context=None,
        )
        # /anpa/ → /amba/ — voiceless p after nasal n becomes voiced
        seq = _seq(
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "nasal": 1},  # n (nasal)
            {"consonantal": 1, "voice": 0, "nasal": 0},  # p → b
            {"consonantal": 0, "syllabic": 1},  # a
        )
        result = apply_rules(seq, [rule])
        # p (at position 2) should become voiced because it follows a nasal
        assert result.data[2]["voice"].value == 1

    def test_sequential_rules(self, inventory):
        """Rules are applied in time order."""
        rule1 = Rule(
            rule_id="devoice_all",
            name="Devoice all consonants",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=None,
        )
        rule2 = Rule(
            rule_id="voice_after_nasal",
            name="Voice after nasal",
            description="",
            time=200,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=1))],
            left_context=[Bundle(bundle=_bundle(nasal=1))],
            right_context=None,
        )
        seq = _seq(
            {"consonantal": 1, "nasal": 1, "voice": 1},  # n
            {"consonantal": 1, "voice": 1, "nasal": 0},  # d
        )
        # Rule 1 devoices all consonants → n(voice=0), d(voice=0)
        # Rule 2 voices consonant after nasal → d(voice=1)
        result = apply_rules(seq, [rule1, rule2])
        assert result.data[0]["voice"].value == 0  # n devoiced
        assert result.data[1]["voice"].value == 1  # d re-voiced after nasal

    def test_empty_sequence(self, inventory):
        """Rules on an empty sequence produce an empty sequence."""
        rule = Rule(
            rule_id="test",
            name="Test",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=None,
            right_context=None,
        )
        seq = Sequence([])
        result = apply_rules(seq, [rule])
        assert len(result.data) == 0

    def test_initial_devoicing(self, inventory):
        """Rule with left boundary: devoice at start of sequence."""
        rule = Rule(
            rule_id="initial_devoicing",
            name="Initial devoicing",
            description="",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1, voice=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            left_context=[Boundary(kind="word")],
            right_context=None,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},  # d at start → t
            {"consonantal": 0, "syllabic": 1},  # a
            {"consonantal": 1, "voice": 1},  # d at end, unchanged
        )
        result = apply_rules(seq, [rule])
        assert result.data[0]["voice"].value == 0  # initial d devoiced
        assert result.data[2]["voice"].value == 1  # final d unchanged


class TestApplicationMode:
    """Test the three application modes: simultaneous, left-to-right, right-to-left."""

    def test_simultaneous_is_default(self, inventory):
        """Default application mode is simultaneous."""
        rule = Rule(
            rule_id="test",
            name="Test",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
        )
        assert rule.application == Application.simultaneous

    def test_simultaneous_all_matches_at_once(self, inventory):
        """Simultaneous mode finds all loci first, then rewrites all at once.

        A rule that devoices consonants: with 3 voiced consonants, all 3
        are devoiced in one pass because loci are found against the original
        state before any changes are applied.
        """
        rule = Rule(
            rule_id="devoice",
            name="Devoice",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            application=Application.simultaneous,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},
            {"consonantal": 0, "syllabic": 1},
            {"consonantal": 1, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        assert result.data[0]["voice"].value == 0
        assert result.data[2]["voice"].value == 0

    def test_left_to_right_cascading(self, inventory):
        """Left-to-right mode applies changes that are visible to later matches.

        Rule: a consonant devoices, and the right context requires [+voice].
        With simultaneous, only the first match fires (the other consonant
        loses its right context).  With left-to-right, after the first
        application the changed segment is visible, so later positions may
        match differently.

        Simpler test: devoice all consonants, but left-to-right just confirms
        every position is visited left-to-right.
        """
        # Simple left-to-right: devoice all consonants
        rule = Rule(
            rule_id="devoice",
            name="Devoice",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            application=Application.left_to_right,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},
            {"consonantal": 0, "syllabic": 1},
            {"consonantal": 1, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        # All consonants should be devoiced
        assert result.data[0]["voice"].value == 0
        assert result.data[2]["voice"].value == 0

    def test_left_to_right_skips_rewritten_span(self, inventory):
        """Left-to-right: after rewriting at position i, resume at position end.

        A rule targeting two consecutive consonants should not re-match
        the second consonant of a rewritten pair if it was part of the
        first match's target span.
        """
        # Rule: devoice a consonant before another consonant (two-segment target)
        rule = Rule(
            rule_id="devoice_before_cons",
            name="Devoice before cons",
            time=100,
            target=[
                Bundle(bundle=_bundle(consonantal=1)),
                Bundle(bundle=_bundle(consonantal=1)),
            ],
            result=[
                Bundle(bundle=_bundle(voice=0)),
                Bundle(bundle=_bundle(voice=1)),  # keep second voiced
            ],
            application=Application.left_to_right,
        )
        # /ddd/ — three voiced consonants
        seq = _seq(
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        # First match: positions 0+1 → [devoiced, voiced]
        # Then resume at position 2: positions 2 alone can't match a 2-segment target
        assert result.data[0]["voice"].value == 0  # devoiced by rule
        assert result.data[1]["voice"].value == 1  # kept voiced by result
        assert result.data[2]["voice"].value == 1  # unchanged (no 2-segment match)

    def test_right_to_left_scans_backward(self, inventory):
        """Right-to-left mode matches from the right side first.

        Rule: devoice a consonant at the end of the word.
        With right-to-left, if there are two matches (e.g., word boundaries
        aren't involved), the rightmost is applied first.

        Simple test: devoice all consonants right-to-left still devoices all.
        """
        rule = Rule(
            rule_id="devoice",
            name="Devoice",
            time=100,
            target=[Bundle(bundle=_bundle(consonantal=1))],
            result=[Bundle(bundle=_bundle(voice=0))],
            application=Application.right_to_left,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 1},
            {"consonantal": 0, "syllabic": 1},
            {"consonantal": 1, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        assert result.data[0]["voice"].value == 0
        assert result.data[2]["voice"].value == 0

    def test_right_to_left_skips_rewritten_span(self, inventory):
        """Right-to-left: after rewriting, the consumed span can't overlap with new matches.

        With target [+cons][+cons] → [+voice][-voice], right-to-left scans
        from the right.  First match at positions 1+2 rewrites both.  Then
        scanning at position 0 would match [0, 2) but that overlaps with
        the consumed span [1, 3), so it's rejected.
        """
        rule = Rule(
            rule_id="devoice_before_cons",
            name="Devoice before cons",
            time=100,
            target=[
                Bundle(bundle=_bundle(consonantal=1)),
                Bundle(bundle=_bundle(consonantal=1)),
            ],
            result=[
                Bundle(bundle=_bundle(voice=1)),  # keep first voiced
                Bundle(bundle=_bundle(voice=0)),  # devoice second
            ],
            application=Application.right_to_left,
        )
        # /ddd/ — three voiced consonants
        seq = _seq(
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
            {"consonantal": 1, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        # R-L: first match at positions 1+2 → d₂ stays voiced, d₃ devoiced
        # Position 0 can't form a 2-segment target that doesn't overlap [1, 3)
        assert result.data[0]["voice"].value == 1  # unchanged
        assert result.data[1]["voice"].value == 1  # kept voiced by result
        assert result.data[2]["voice"].value == 0  # devoiced by rule

    def test_application_mode_from_toml(self, inventory, tmp_path):
        """Application mode is parsed from TOML rule entries."""
        from src.fortis.inventories.rule_inventory import RuleInventory

        toml_content = """
[100.left_to_right_rule]
name = "Left-to-right rule"
definition = "[+cons] → [-voice] / _#"
application = "left-to-right"

[200.default_rule]
name = "Default rule"
definition = "[+cons] → [-voice]"
"""
        toml_file = tmp_path / "rules.toml"
        toml_file.write_text(toml_content)

        result = RuleInventory.load(toml_file, inventory)
        assert result.is_ok()
        rules = result.unwrap()
        assert rules["left_to_right_rule"].application == Application.left_to_right
        assert rules["default_rule"].application == Application.simultaneous


# ---------------------------------------------------------------------------
# Quantifier and negation parsing
# ---------------------------------------------------------------------------


class TestQuantifierParsing:
    """Test that quantifier suffixes are parsed correctly on bundles."""

    def test_star_quantifier(self, inventory: FeatureInventory):
        """[*+cons] means zero or more consonant segments."""
        result = parse_spe_definition("[+cons]* -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Bundle)
        assert target[0].quantifier.min == 0
        assert target[0].quantifier.max is None
        assert target[0].negated is False

    def test_plus_quantifier(self, inventory: FeatureInventory):
        """[+cons]+ means one or more consonant segments."""
        result = parse_spe_definition("[+cons]+ -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].quantifier.min == 1
        assert target[0].quantifier.max is None

    def test_exact_quantifier(self, inventory: FeatureInventory):
        """[+cons]{3} means exactly 3 consonant segments."""
        result = parse_spe_definition("[+cons]{3} -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].quantifier.min == 3
        assert target[0].quantifier.max == 3

    def test_range_quantifier(self, inventory: FeatureInventory):
        """[+cons]{2,4} means 2 to 4 consonant segments."""
        result = parse_spe_definition("[+cons]{2,4} -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].quantifier.min == 2
        assert target[0].quantifier.max == 4

    def test_open_range_quantifier(self, inventory: FeatureInventory):
        """[+cons]{1,} means 1 or more (same as + but explicit)."""
        result = parse_spe_definition("[+cons]{1,} -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].quantifier.min == 1
        assert target[0].quantifier.max is None

    def test_default_quantifier_is_one(self, inventory: FeatureInventory):
        """[+cons] without suffix has quantifier (1, 1)."""
        result = parse_spe_definition("[+cons] -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].quantifier.min == 1
        assert target[0].quantifier.max == 1

    def test_quantifier_in_context(self, inventory: FeatureInventory):
        """Quantifiers work in context positions."""
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas]+_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert left_ctx[0].quantifier == Quantifier(min=1, max=None)

    def test_quantifier_in_result(self, inventory: FeatureInventory):
        """Quantifiers work in result positions."""
        result = parse_spe_definition("[+cons] -> [-vc]{2}", inventory)
        assert result.is_ok()
        result_elems = result.unwrap()[1]
        assert len(result_elems) == 1
        assert result_elems[0].quantifier.min == 2
        assert result_elems[0].quantifier.max == 2


class TestNegationParsing:
    """Test that negation prefix ! is parsed correctly on bundles."""

    def test_negated_bundle(self, inventory: FeatureInventory):
        """![+cons] matches any segment that is NOT [+cons]."""
        result = parse_spe_definition("![+cons] -> [+vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Bundle)
        assert target[0].negated is True
        assert target[0].quantifier == _ONE

    def test_negated_bundle_with_quantifier(self, inventory: FeatureInventory):
        """![+cons]+ means one or more segments that are NOT [+cons]."""
        result = parse_spe_definition("![+cons]+ -> [+vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert target[0].negated is True
        assert target[0].quantifier == Quantifier(min=1, max=None)

    def test_negated_bundle_in_context(self, inventory: FeatureInventory):
        """Negation works in context positions."""
        result = parse_spe_definition("[+cons] -> [-vc] / ![-syll]_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert left_ctx[0].negated is True

    def test_bang_without_bracket_is_error(self, inventory: FeatureInventory):
        """! without a following [ is a parse error."""
        result = parse_spe_definition("!+cons] -> [-vc]", inventory)
        assert result.is_err()

    def test_quantifier_match_and_apply(self, inventory: FeatureInventory):
        """Quantified bundles match multiple segments and rewrite them."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        voice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Bundle(bundle=cons, quantifier=Quantifier(min=2, max=2))],
            result=[Bundle(bundle=voice), Bundle(bundle=voice)],
            left_context=None,
            right_context=None,
        )
        # Two consonants
        seq = _seq({"consonantal": 1, "voice": 1}, {"consonantal": 1, "voice": 1}, {"consonantal": 0, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1
        assert loci[0].start == 0
        assert loci[0].end == 2
        result = apply_rules(seq, [rule])
        assert result.data[0]["voice"].value == 0
        assert result.data[1]["voice"].value == 0
        assert result.data[2]["voice"].value == 1  # vowel unchanged

    def test_negated_bundle_match(self, inventory: FeatureInventory):
        """![+cons] matches a segment that does NOT satisfy [+cons]."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Bundle(bundle=cons, negated=True)],
            result=[Bundle(bundle=devoice)],
            left_context=None,
            right_context=None,
        )
        # Vowel should match ![+cons]
        seq = _seq({"consonantal": 0, "syllabic": 1, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1


class TestFeatureNegationInRules:
    """Test that feature-level negation (! inside brackets) works in rules."""

    def test_feature_negation_parsed_in_bundle(self, inventory: FeatureInventory):
        """[+cons, !nasal] — ! applies to individual features inside brackets."""
        result = parse_spe_definition("[+cons, !nasal] -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert isinstance(target[0], Bundle)
        # consonantal is not negated
        assert target[0].bundle["consonantal"].negated is False
        # nasal IS negated
        assert target[0].bundle["nasal"].negated is True

    def test_feature_negation_match(self, inventory: FeatureInventory):
        """A rule with [+cons, !nasal] matches a non-nasal consonant."""
        cons_not_nasal = FeatureBundle({
            "consonantal": FeatureSpec("consonantal", 1),
            "nasal": FeatureSpec("nasal", 1, negated=True),
        })
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Bundle(bundle=cons_not_nasal)],
            result=[Bundle(bundle=devoice)],
            left_context=None,
            right_context=None,
        )
        # Non-nasal consonant should match [+cons, !nasal]
        seq = _seq({"consonantal": 1, "nasal": 0, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1

        # Nasal consonant should NOT match [+cons, !nasal]
        seq_nasal = _seq({"consonantal": 1, "nasal": 1, "voice": 1})
        loci_nasal = find_loci(rule, seq_nasal)
        assert len(loci_nasal) == 0


class TestNullParsing:
    """Test that ∅ and 0 are parsed as Null elements."""

    def test_unicode_null_in_target(self, inventory: FeatureInventory):
        """∅ in target marks an insertion point."""
        result = parse_spe_definition("∅ -> [+cons]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Null)

    def test_ascii_zero_in_target(self, inventory: FeatureInventory):
        """0 in target marks an insertion point (same as ∅)."""
        result = parse_spe_definition("0 -> [+cons]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Null)

    def test_null_in_result_deletion(self, inventory: FeatureInventory):
        """0 in result marks deletion of the corresponding target segment."""
        result = parse_spe_definition("[+cons] -> 0", inventory)
        assert result.is_ok()
        result_elems = result.unwrap()[1]
        assert len(result_elems) == 1
        assert isinstance(result_elems[0], Null)

    def test_null_in_context(self, inventory: FeatureInventory):
        """0 in context is a zero-width insertion point."""
        result = parse_spe_definition("[+cons] -> [-cons] / 0_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert isinstance(left_ctx[0], Null)

    def test_mixed_null_and_bundle(self, inventory: FeatureInventory):
        """Null and bundles can coexist in a rule."""
        result = parse_spe_definition("[+cons] -> 0 [+cons]", inventory)
        assert result.is_ok()
        result_elems = result.unwrap()[1]
        assert len(result_elems) == 2
        assert isinstance(result_elems[0], Null)
        assert isinstance(result_elems[1], Bundle)


class TestInsertionDeletion:
    """Test insertion and deletion via Null elements in rules."""

    def test_deletion(self, inventory: FeatureInventory):
        """A rule that deletes a segment: [+cons] -> 0."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        rule = Rule(
            rule_id="delete",
            name="delete consonant",
            time=100,
            target=[Bundle(bundle=cons)],
            result=[Null()],
            left_context=None,
            right_context=None,
        )
        seq = _seq({"consonantal": 0, "voice": 1}, {"consonantal": 1, "voice": 1}, {"consonantal": 0, "voice": 1})
        result = apply_rules(seq, [rule])
        # The consonant (index 1) should be deleted
        assert len(result.data) == 2
        assert result.data[0]["voice"].value == 1  # vowel unchanged
        assert result.data[1]["voice"].value == 1  # vowel unchanged

    def test_partial_deletion(self, inventory: FeatureInventory):
        """Delete one segment from a two-segment target."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        voice = FeatureBundle({"voice": FeatureSpec("voice", 1)})
        rule = Rule(
            rule_id="partial_del",
            name="delete first of two",
            time=100,
            target=[Bundle(bundle=cons), Bundle(bundle=cons)],
            result=[Null(), Bundle(bundle=voice)],
            left_context=None,
            right_context=None,
        )
        seq = _seq(
            {"consonantal": 1, "voice": 0},
            {"consonantal": 1, "voice": 0},
            {"consonantal": 0, "voice": 1},
        )
        result = apply_rules(seq, [rule])
        # First consonant deleted, second becomes voiced
        assert len(result.data) == 2
        assert result.data[0]["voice"].value == 1  # second consonant (now voiced)
        assert result.data[1]["voice"].value == 1  # vowel unchanged


class TestGroupParsing:
    """Test that parenthesised groups are parsed correctly."""

    def test_simple_group(self, inventory: FeatureInventory):
        """([+cons][+nas]) parses as a Group with two Bundle children."""
        result = parse_spe_definition("([+cons][+nas]) -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Group)
        assert len(target[0].elements) == 2
        assert target[0].quantifier == _ONE

    def test_group_with_quantifier(self, inventory: FeatureInventory):
        """([+cons][+nas])+ parses as a quantified Group."""
        result = parse_spe_definition("([+cons][+nas])+ -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert isinstance(target[0], Group)
        assert target[0].quantifier == Quantifier(min=1, max=None)

    def test_group_star_quantifier(self, inventory: FeatureInventory):
        """([+cons])* parses as a Group with * quantifier."""
        result = parse_spe_definition("([+cons])* -> [-vc]", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert isinstance(target[0], Group)
        assert target[0].quantifier == Quantifier(min=0, max=None)

    def test_nested_group(self, inventory: FeatureInventory):
        """Nested groups: ([+cons]([+nas])) parses with inner Group."""
        result = parse_spe_definition("([+cons]([+nas])) -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert isinstance(target[0], Group)
        assert len(target[0].elements) == 2
        assert isinstance(target[0].elements[1], Group)

    def test_unclosed_parenthesis_is_error(self, inventory: FeatureInventory):
        """Unclosed parenthesis produces an error."""
        result = parse_spe_definition("([+cons] -> [-vc]", inventory)
        assert result.is_err()

    def test_group_in_context(self, inventory: FeatureInventory):
        """Groups work in context positions."""
        result = parse_spe_definition("[+cons] -> [-vc] / ([+nas])+_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert isinstance(left_ctx[0], Group)
        assert left_ctx[0].quantifier == Quantifier(min=1, max=None)


class TestGroupMatching:
    """Test that groups match correctly in the match engine."""

    def test_group_matches_sequence(self, inventory: FeatureInventory):
        """A group matches the sequence of its inner elements."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        nas = FeatureBundle({"nasal": FeatureSpec("nasal", 1)})
        voice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Group(elements=[Bundle(bundle=cons), Bundle(bundle=nas)])],
            result=[Bundle(bundle=voice), Bundle(bundle=voice)],
            left_context=None,
            right_context=None,
        )
        # Consonant followed by nasal
        # All segments have explicit consonantal and nasal values to avoid
        # ignore_none wildcard matching
        seq = _seq(
            {"consonantal": 1, "nasal": 0, "voice": 1},  # consonant, non-nasal
            {"consonantal": 0, "nasal": 1, "voice": 1},  # nasal consonant
            {"consonantal": 0, "nasal": 0, "voice": 1},  # vowel
        )
        loci = find_loci(rule, seq)
        assert len(loci) == 1
        assert loci[0].start == 0
        assert loci[0].end == 2

    def test_quantified_group_match(self, inventory: FeatureInventory):
        """A quantified group matches repeated sequences."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        voice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Group(elements=[Bundle(bundle=cons)], quantifier=Quantifier(min=2, max=2))],
            result=[Bundle(bundle=voice), Bundle(bundle=voice)],
            left_context=None,
            right_context=None,
        )
        # Two consonants
        seq = _seq({"consonantal": 1, "voice": 1}, {"consonantal": 1, "voice": 1}, {"consonantal": 0, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1
        assert loci[0].start == 0
        assert loci[0].end == 2


class TestDisjunctionParsing:
    """Test that disjunction (|) is parsed correctly."""

    def test_simple_disjunction(self, inventory: FeatureInventory):
        """[+cons] | [+nas] parses as a Disjunction with two branches."""
        result = parse_spe_definition("[+cons] | [+nas] -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Disjunction)
        assert len(target[0].branches) == 2

    def test_three_way_disjunction(self, inventory: FeatureInventory):
        """[+cons] | [+nas] | [+voice] parses as three branches."""
        result = parse_spe_definition("[+cons] | [+nas] | [+voice] -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert isinstance(target[0], Disjunction)
        assert len(target[0].branches) == 3

    def test_disjunction_in_context(self, inventory: FeatureInventory):
        """Disjunction works in context positions."""
        result = parse_spe_definition("[+cons] -> [-vc] / [+nas] | [+vc]_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert isinstance(left_ctx[0], Disjunction)


class TestDisjunctionMatching:
    """Test that disjunction matches correctly in the match engine."""

    def test_disjunction_matches_first_branch(self, inventory: FeatureInventory):
        """A disjunction matches when the first branch matches."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        nas = FeatureBundle({"nasal": FeatureSpec("nasal", 1)})
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Disjunction(branches=[[Bundle(bundle=cons)], [Bundle(bundle=nas)]])],
            result=[Bundle(bundle=devoice)],
            left_context=None,
            right_context=None,
        )
        # Consonant should match the first branch
        seq = _seq({"consonantal": 1, "nasal": 0, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1

    def test_disjunction_matches_second_branch(self, inventory: FeatureInventory):
        """A disjunction matches when the second branch matches."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        nas = FeatureBundle({"nasal": FeatureSpec("nasal", 1)})
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Disjunction(branches=[[Bundle(bundle=cons)], [Bundle(bundle=nas)]])],
            result=[Bundle(bundle=devoice)],
            left_context=None,
            right_context=None,
        )
        # Nasal (not consonantal) should match the second branch
        seq = _seq({"consonantal": 0, "nasal": 1, "voice": 1})
        loci = find_loci(rule, seq)
        assert len(loci) == 1


class TestBindingRefParsing:
    """Test that Binding (V=...) and Ref (@V) are parsed correctly."""

    def test_binding_with_bundle(self, inventory: FeatureInventory):
        """V=[+cons] captures a consonant span."""
        result = parse_spe_definition("V=[+cons] -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Binding)
        assert target[0].name == "V"
        assert len(target[0].pattern) == 1
        assert isinstance(target[0].pattern[0], Bundle)

    def test_ref_in_result(self, inventory: FeatureInventory):
        """@V in result recalls a bound span."""
        result = parse_spe_definition("[+cons] -> @V", inventory)
        assert result.is_ok()
        result_elems = result.unwrap()[1]
        assert len(result_elems) == 1
        assert isinstance(result_elems[0], Ref)
        assert result_elems[0].name == "V"

    def test_binding_with_group(self, inventory: FeatureInventory):
        """V=([+cons][+nas]) captures a two-segment span."""
        result = parse_spe_definition("V=([+cons][+nas]) -> 0", inventory)
        assert result.is_ok()
        target = result.unwrap()[0]
        assert len(target) == 1
        assert isinstance(target[0], Binding)
        assert target[0].name == "V"
        assert len(target[0].pattern) == 1  # Group wraps the two bundles
        assert isinstance(target[0].pattern[0], Group)

    def test_binding_in_context(self, inventory: FeatureInventory):
        """Binding works in context positions."""
        result = parse_spe_definition("[+cons] -> [-vc] / V=[+nas]_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert isinstance(left_ctx[0], Binding)
        assert left_ctx[0].name == "V"

    def test_ref_in_context(self, inventory: FeatureInventory):
        """@V in context recalls a previously bound span."""
        result = parse_spe_definition("[+cons] -> 0 / V=[+nas]_@V", inventory)
        assert result.is_ok()
        # Right context should have a Ref
        right_ctx = result.unwrap()[3]
        assert right_ctx is not None
        assert isinstance(right_ctx[0], Ref)
        assert right_ctx[0].name == "V"


class TestSyllableBoundary:
    """Test that $ matches syllable boundaries stored in the Sequence."""

    def test_dollar_in_context(self, inventory: FeatureInventory):
        """$ is parsed as a syllable boundary in context."""
        result = parse_spe_definition("[+cons] -> [-vc] / $_", inventory)
        assert result.is_ok()
        left_ctx = result.unwrap()[2]
        assert left_ctx is not None
        assert any(isinstance(el, Boundary) and el.kind == "syllable" for el in left_ctx)

    def test_dollar_matches_syllable_boundary(self, inventory: FeatureInventory):
        """A rule with $ matches when there's a syllable boundary."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Bundle(bundle=cons)],
            result=[Bundle(bundle=devoice)],
            left_context=[Boundary(kind="syllable")],
            right_context=None,
        )
        # Sequence with a syllable boundary at position 1 (between seg 0 and 1)
        seq = _seq({"consonantal": 0, "voice": 1}, {"consonantal": 1, "voice": 1})
        seq.syllable_boundaries = {1}
        loci = find_loci(rule, seq)
        # The consonant at index 1 should match (boundary before it)
        assert len(loci) == 1
        assert loci[0].start == 1

    def test_dollar_no_match_without_boundary(self, inventory: FeatureInventory):
        """A rule with $ does NOT match when there's no syllable boundary."""
        cons = FeatureBundle({"consonantal": FeatureSpec("consonantal", 1)})
        devoice = FeatureBundle({"voice": FeatureSpec("voice", 0)})
        rule = Rule(
            rule_id="test",
            name="test",
            time=100,
            target=[Bundle(bundle=cons)],
            result=[Bundle(bundle=devoice)],
            left_context=[Boundary(kind="syllable")],
            right_context=None,
        )
        # Sequence WITHOUT any syllable boundaries
        seq = _seq({"consonantal": 0, "voice": 1}, {"consonantal": 1, "voice": 1})
        seq.syllable_boundaries = set()
        loci = find_loci(rule, seq)
        assert len(loci) == 0
