"""Smoke test for the end-to-end pipeline (src/fortis/main.py)."""

from pathlib import Path

from src.fortis.application.deriving import derive
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.loaders.rules import load_rule
from src.fortis.main import _print_derivation, main
from src.fortis.models.inventories import Word
from src.fortis.models.rules import RuleInventory


def test_main_derives_every_word(project, capsys):
    main([])  # no CLI args → all shipped rules over all shipped words
    out = capsys.readouterr().out
    # One surface form per word, and known syllabified derivations come through.
    assert out.count("Surface:") == len(project.words)
    assert "ˈħan.ti" in out  # *h₂énti: a-coloured by h₂ (now ħ, [+low]), stress kept
    assert "wul.kʷos" in out  # centumization + u-epenthesis, then syllabified


def test_cli_overrides_words_and_rules(capsys):
    # --words / --rules run a different lexicon + rules with the *shipped* feature system,
    # letters, tiers, etc. (the tonal example needs tone, which the shipped inventories support).
    example = Path(__file__).resolve().parent.parent / "examples" / "tonal"
    main(["--words", str(example / "words.toml"), "--rules", str(example / "rules.toml")])
    out = capsys.readouterr().out
    assert "High-tone spread" in out  # the tonal rule fired on the tonal words
    assert "ˈħan.ti" not in out  # ...and the shipped PIE lexicon was not used


def _derive(word, rules, project):
    return derive(
        Word(ipa=word),
        string_to_sequence(word, project),
        rules,
        project.letters,
        project.features,
        project.sonorities,
        project.syllable_parts,
        project.tiers,
    )


def test_list_definition_substeps_share_one_heading(project, capsys):
    # A list-definition rule's sub-steps (ids `name#1`, `#2`) print under a single
    # heading, one change line each — not the rule name repeated per sub-step.
    sub = load_rule(
        "stress_change",
        {
            "time": -1000,
            "name": "Stress change to first syllable",
            "definition": [
                "[+syll] → [stress: primary] / # [-syll]* _ []* [+syll, stress: primary]",
                "[+syll] → [stress: none] / [+syll] []* _",
            ],
        },
        project.features,
    ).unwrap()
    _print_derivation(_derive("koˈta", RuleInventory({-1000: tuple(sub)}), project), project)
    out = capsys.readouterr().out
    assert out.count("Stress change to first syllable") == 1  # one heading, not per sub-step
    assert out.count(" → ") == 2  # both sub-steps' before → after lines are shown
    assert "stress_change#1" not in out and "stress_change#2" not in out  # suffix hidden


def test_standalone_rule_keeps_its_own_heading(project, capsys):
    # A plain (non-list) rule is its own heading, with its id shown when unnamed.
    spec = {"time": 0, "definition": "[+cons] → [-voice]"}
    [rule] = load_rule("devoicing", spec, project.features).unwrap()
    _print_derivation(_derive("ˈba", RuleInventory({0: (rule,)}), project), project)
    out = capsys.readouterr().out
    assert "0: devoicing" in out  # unnamed rule falls back to its id (no suffix to strip)
