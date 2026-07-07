"""Tests for composition and Phase-B refinement (src/fortis/induction/refine.py)."""

from dataclasses import replace

from src.fortis.application.deriving import derive_all
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.induction.boost import InducedInterval
from src.fortis.induction.intervals import synthetic_project
from src.fortis.induction.refine import (
    _flat,
    _global_shrink,
    _inventory,
    _localized_bounds,
    _stage_residual_interval,
    compose,
    induce_project,
)
from src.fortis.induction.report import render_induced_rules
from src.fortis.loaders.rules import load_rule, load_rule_inventory


def _induced(label: str, definitions: list[str], synth) -> InducedInterval:
    rules = [
        load_rule("r", {"definition": d, "time": 0}, synth.features).unwrap()[0]
        for d in definitions
    ]
    return InducedInterval(
        label=label, rules=rules, steps=[], stopped="converged",
        start_fit=0.0, final_fit=0.0, start_exact=0, final_exact=0, assessed=0,
    )


class TestCompose:
    def test_times_land_strictly_inside_the_interval(self, synth):
        interval = _induced("-100→750", ["o → u", "k → t", "eː → e"], synth)
        inventory = compose([interval], synth)
        times = sorted(t for t in inventory if t is not None)
        assert all(-100 < t < 750 for t in times)
        assert len(set(times)) == 3  # distinct

    def test_ids_and_names_are_minted(self, synth):
        inventory = compose([_induced("750→1000", ["o → u"], synth)], synth)
        rule = next(iter(inventory.values()))[0]
        assert rule.id.startswith("ind_750_1000")
        assert rule.name is not None and "induced" in rule.name
        assert rule.raw_definition == "o → u"

    def test_interval_order_is_preserved_across_the_cascade(self, synth):
        early = _induced("-100→750", ["o → u"], synth)
        late = _induced("1000→1200", ["k → t"], synth)
        inventory = compose([early, late], synth)
        times = {r.raw_definition: t for t, rs in inventory.items() for r in rs}
        early_t, late_t = times["o → u"], times["k → t"]
        assert early_t is not None and late_t is not None
        assert early_t < late_t

    def test_empty_interval_contributes_nothing(self, synth):
        inventory = compose([_induced("-100→750", [], synth)], synth)
        assert len(inventory) == 0


class TestRoundTrip:
    def test_induce_serialize_reload_derives_identically(self, synth, tmp_path):
        # A tiny composed cascade must serialize to a rules.toml that reloads and derives the
        # same surfaces — the induce → load → measure round trip (plan §4.4).
        synth = synthetic_project(synth)
        result = induce_project(
            synth, only_interval=(750, 1000),
            escape=False, shrink=False, placement=False,
        )
        path = tmp_path / "induced_rules.toml"
        path.write_text(render_induced_rules(result.inventory), encoding="utf-8")
        reloaded = load_rule_inventory(path, synth.features).unwrap()

        def surfaces(inventory):
            project = replace(synth, rules=inventory)
            return [
                render_syllabified(lower_tiers(d.surface), d.surface_boundaries, project)
                for d in derive_all(project)
            ]

        assert surfaces(result.inventory) == surfaces(reloaded)


class TestFlatInventory:
    def test_flat_then_inventory_round_trips(self, synth):
        inventory = compose(
            [_induced("-100→750", ["o → u", "k → t"], synth),
             _induced("1000→1200", ["eː → e"], synth)],
            synth,
        )
        rebuilt = _inventory(_flat(inventory))
        assert {r.id for rs in rebuilt.values() for r in rs} == {
            r.id for rs in inventory.values() for r in rs
        }


class TestGlobalShrink:
    def test_removes_a_dominated_duplicate(self, synth):
        # Two identical rules over the whole lexicon: one is dead weight, dropped by global L.
        synth = synthetic_project(synth)
        r1 = load_rule("a", {"definition": "o → u", "time": 100}, synth.features).unwrap()[0]
        r2 = load_rule("b", {"definition": "o → u", "time": 200}, synth.features).unwrap()[0]
        kept, log = _global_shrink(synth, [r1, r2])
        assert len(kept) == 1
        assert len(log) == 1


class TestLocalizedHelpers:
    def test_bounds_use_stage_times_and_open_span(self, synth):
        times = [-200, -100, 750, 1000, 1200, 1400]
        assert _localized_bounds(-100, 750, times) == (-100, 750)  # bounded interval
        assert _localized_bounds(None, -200, times)[1] == -200  # input interval ends at first
        assert _localized_bounds(1400, None, times)[0] == 1400  # final interval starts at last

    def test_stage_residual_targets_are_the_attested_stage(self, synth):
        # The mini-project maps the composed *derived* form at a stage to the *attested* one:
        # every target is an attested form at that stage, so boosting corrects toward it.
        from src.fortis.models.rules import RuleInventory

        interval = _stage_residual_interval(synth, RuleInventory(), None, -100, workers=1)
        assert interval.project.words
        attested_minus_100 = {w.stages[-100] for w in synth.words.values() if -100 in w.stages}
        for word in interval.project.words.values():
            assert word.final in attested_minus_100
