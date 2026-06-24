"""Tests for structural rule validation (the §2.x well-formedness checks)."""

from src.fortis.parsing.notation import parse_definition
from src.fortis.parsing.rule_validation import validate_structural_description


def check(definition, features):
    """Parse a definition and run structural validation on the result."""
    return validate_structural_description(parse_definition(definition, features).unwrap())


class TestValid:
    def test_simple_rule(self, features):
        assert check("a -> b / c _ d", features).is_ok()

    def test_alpha_bound_in_target(self, features):
        assert check("[αhigh] -> [αnasal] / c _", features).is_ok()

    def test_alpha_bound_in_context(self, features):
        # §2.4.2 — bound in context, recalled in result.
        assert check("a -> [αnasal] / [αhigh] _", features).is_ok()

    def test_reference_bind_and_recall(self, features):
        assert check("1=a -> b / @1 _", features).is_ok()

    def test_conditional_label_once_each(self, features):
        assert check("[<1:+high>] -> [<1:+nasal>] / a _", features).is_ok()

    def test_conditional_label_also_in_context(self, features):
        # §2.9.5 — a label may also appear in context (shared condition).
        assert check("[<1:+high>] -> [<1:+nasal>] / [<1:+voice>] _", features).is_ok()

    def test_conditional_label_context_only(self, features):
        # §2.9 — a label may be conditioned purely on the context (no target
        # condition): assimilation from a neighbour, e.g. laryngeal colouring.
        assert check("[+syll] -> [<1:+nasal>] / [<1:+voice>] _", features).is_ok()

    def test_conditional_label_multifeature_result(self, features):
        # §2.9 — one label may drive several result features (a conditional change
        # of more than one feature at once).
        assert check("[<1:+high>] -> [<1:+nasal>, <1:+voice>] / a _", features).is_ok()

    def test_collapse_to_letter(self, features):
        # §2.1.1 — many targets may coalesce into a full-replacement letter.
        assert check("a a -> b / c _", features).is_ok()

    def test_expand_to_letters(self, features):
        # §2.1.1 — one target may expand to several full-replacement letters.
        assert check("a -> b c / d _", features).is_ok()


class TestInvalid:
    def test_ambiguous_collapse_to_bundle(self, features):
        # §2.1.1 — collapsing two targets onto one merge-bundle is ambiguous.
        errors = check("[+cons][-cons] -> [+nasal] / a _", features).unwrap_err()
        assert any("Ambiguous" in e for e in errors)

    def test_ambiguous_expand_to_bundles(self, features):
        # §2.1.1 — one target expanding to several merge-bundles is ambiguous.
        errors = check("[+syllabic] -> [+nasal][+high] / a _", features).unwrap_err()
        assert any("Ambiguous" in e for e in errors)


class TestBatch2Valid:
    def test_null_target_with_context(self, features):
        assert check("∅ -> x / a _", features).is_ok()

    def test_boundary_in_context(self, features):
        assert check("a -> b / # _", features).is_ok()

    def test_matching_quantifiers(self, features):
        assert check("a{2} -> b{2} / c _", features).is_ok()

    def test_quantified_target_collapses_to_letter(self, features):
        # §2.1.2 — a quantified target may collapse onto a full-replacement letter.
        assert check("a{2} -> b / c _", features).is_ok()

    def test_exception_without_context(self, features):
        # §2.6.1 scrapped — an exception clause needs no context clause.
        assert check("a -> b // e _ f", features).is_ok()

    def test_paired_disjunction(self, features):
        assert check("(a|b) -> (c|d) / f _", features).is_ok()

    def test_disjunction_collapse_to_single_result(self, features):
        # §2.7 — a target disjunction may collapse to one (non-disjunction) result.
        assert check("(a|b|c) -> d / f _", features).is_ok()

    def test_negation_in_target(self, features):
        assert check("!a -> b / c _", features).is_ok()


class TestBatch2Invalid:
    def test_null_in_context(self, features):
        errors = check("a -> b / ∅ _", features).unwrap_err()
        assert any("not valid in left context" in e for e in errors)

    def test_boundary_sole_target(self, features):
        errors = check("# -> x", features).unwrap_err()
        assert any("only element in target" in e for e in errors)

    def test_boundary_sole_result(self, features):
        errors = check("x -> #", features).unwrap_err()
        assert any("only element in result" in e for e in errors)

    def test_null_entire_target_without_context(self, features):
        errors = check("∅ -> x", features).unwrap_err()
        assert any("entire target requires a context" in e for e in errors)

    def test_merge_bundle_quantifier_mismatch(self, features):
        # §2.1.2 — a merge-bundle result must match its target's quantifier.
        errors = check("[+consonantal]{2} -> [+nasal] / c _", features).unwrap_err()
        assert any("same quantifier" in e for e in errors)

    def test_disjunction_unpaired(self, features):
        errors = check("a -> (b|c) / d _", features).unwrap_err()
        assert any("corresponding target" in e for e in errors)

    def test_disjunction_branch_count_mismatch(self, features):
        errors = check("(a|b) -> (c|d|e) / f _", features).unwrap_err()
        assert any("same number of branches" in e for e in errors)

    def test_more_than_one_disjunction_per_side(self, features):
        # §2.7.1 — pairing is by the matched branch, so only one top-level per side.
        errors = check("(a|b) (e|f) -> (c|d) (g|h)", features).unwrap_err()
        assert any("at most one top-level disjunction" in e for e in errors)

    def test_nested_disjunction_with_a_top_level_one_rejected(self, features):
        # §2.7.1 — a nested disjunction may not coexist with a top-level one (it would
        # desync the recorded branch choice from how the result is resolved).
        errors = check("(a | (b|c)) -> (d|e)", features).unwrap_err()
        assert any("nested disjunction cannot coexist" in e for e in errors)

    def test_nested_only_disjunction_is_allowed(self, features):
        # A nested alternation with no top-level disjunction to pair is fine —
        # e.g. (a|b)? before a target, deleted wholesale.
        assert check("(a|b)? c -> ∅ / d _", features).is_ok()

    def test_negation_in_result(self, features):
        errors = check("a -> !b / c _", features).unwrap_err()
        assert any("not valid in result" in e for e in errors)

    def test_negation_on_null(self, features):
        errors = check("!∅ -> b / c _", features).unwrap_err()
        assert any("not be applied to ∅" in e for e in errors)

    def test_negation_on_wildcard(self, features):
        errors = check("![] -> b / c _", features).unwrap_err()
        assert any("not be applied to ∅" in e for e in errors)

    def test_dangling_recall(self, features):
        errors = check("@1 -> b / a _", features).unwrap_err()
        assert any("no matching binding" in e for e in errors)

    def test_binding_never_recalled(self, features):
        errors = check("1=a -> b / c _", features).unwrap_err()
        assert any("never recalled" in e for e in errors)

    def test_binding_in_result(self, features):
        errors = check("@1 -> 1=b / c _", features).unwrap_err()
        assert any("not allowed in result" in e for e in errors)

    def test_alpha_unbound_in_result(self, features):
        errors = check("a -> [αnasal] / c _", features).unwrap_err()
        assert any("never bound" in e for e in errors)

    def test_conditional_label_condition_without_result(self, features):
        # A label that conditions but applies nothing in the result is an orphan.
        errors = check("[<1:+high>] -> b / a _", features).unwrap_err()
        assert any("applies no result feature" in e for e in errors)

    def test_conditional_label_result_without_condition(self, features):
        # A result label with no condition anywhere (target or context) is an orphan.
        errors = check("a -> [<1:+nasal>] / b _", features).unwrap_err()
        assert any("has no condition" in e for e in errors)
