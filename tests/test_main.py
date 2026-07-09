"""Smoke test for the end-to-end pipeline (src/fortis/main.py)."""

from src.fortis.application.deriving import derive
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.loaders.rules import load_rule
from src.fortis.main import _trace_lines, main
from src.fortis.models.inventories import Word
from src.fortis.models.rules import RuleInventory


def test_main_derives_every_word(project, capsys, tmp_path):
    # shipped feature showcase, reports to tmp_path
    out_path = tmp_path / "derivations.csv"
    main(["--output", str(out_path)])
    captured = capsys.readouterr()
    # The per-word cascade is written to derivations.csv, not printed — stdout is empty; the
    # run summary (with the accuracy headline) is on stderr.
    assert captured.out == ""
    assert "exact" in captured.err  # the Accuracy headline in the run summary
    # A couple of the showcase derivations come through in the long-format trace.
    trace = out_path.read_text(encoding="utf-8")
    assert "ag.ba" in trace  # voicing assimilation: k → g before b
    assert "tak" in trace  # final devoicing: g → k word-finally
    assert "aŋ.ka" in trace  # place assimilation: n → ŋ (node spread copies the velar's place)


def test_main_writes_derivation_matrix_csv(tmp_path):
    # The rule×word matrix is written as derivation_matrix.csv, alongside the main report.
    main(["--output", str(tmp_path / "derivations.csv")])
    assert (tmp_path / "derivation_matrix.csv").exists()


def test_main_writes_rule_firings_csv(tmp_path):
    # One row per rule: the words it matched (before → after) and its distinct changes.
    import csv

    main(["--output", str(tmp_path / "derivations.csv")])
    text = (tmp_path / "rule_firings.csv").read_text(encoding="utf-8")
    rows = list(csv.reader(text.splitlines()))
    assert rows[0] == ["rule", "t", "sporadic", "count", "changes", "matched"]
    fired = [r for r in rows[1:] if int(r[3]) > 0]  # rules that changed at least one word
    assert fired
    for r in fired:
        assert r[4]  # changes (distinct segment deltas) are non-empty
        assert " → " in r[5]  # matched holds `before → after` entries
        assert len(r[5].split(", ")) == int(r[3])  # one matched entry per counted firing


def test_main_writes_derivations_csv_long_format(tmp_path):
    # The main report is derivations.csv: one row per word × rule, bookended by the
    # synthetic `input` (raw IPA → ingested form) and `output` (→ surface) rows.
    import csv

    out = tmp_path / "derivations.csv"
    main(["--output", str(out)])
    rows = list(csv.reader(out.read_text(encoding="utf-8").splitlines()))
    assert rows[0] == ["word", "rule", "t", "before", "after", "change"]
    body = rows[1:]
    assert body[0][1] == "input"  # first row of the first word is its input
    # input's `before` is the raw IPA; `change` is empty on both synthetic rows.
    inputs = [r for r in body if r[1] == "input"]
    outputs = [r for r in body if r[1] == "output"]
    assert inputs and len(inputs) == len(outputs)  # one of each per word
    assert all(r[3] and r[5] == "" for r in inputs)  # before set, change empty
    # after set, before/change empty
    assert all(r[3] == "" and r[4] and r[5] == "" for r in outputs)


def test_main_writes_reports_into_subfolder(project, tmp_path):
    # With --project (no --output), every report lands in <project>/reports/.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(f'"{ipa}" = "x"\n', encoding="utf-8")
    main(["--project", str(tmp_path)])
    assert (tmp_path / "reports" / "derivations.csv").exists()
    assert (tmp_path / "reports" / "derivation_matrix.csv").exists()
    assert not (tmp_path / "derivations.csv").exists()  # not at the project root


def test_main_single_word_writes_single_reports(project, tmp_path, capsys):
    # --single derives one word (found by IPA key) and writes single_*.csv, not the full run.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(
        f'"{ipa}" = {{gloss = "x", final = "zzz"}}\n', encoding="utf-8"
    )
    main(["--project", str(tmp_path), "--single", ipa])
    reports = tmp_path / "reports"
    assert (reports / "single_derivations.csv").exists()
    assert (reports / "single_accuracy.csv").exists()  # the word carries a target
    assert (reports / "single_blame.csv").exists()
    assert not (reports / "derivations.csv").exists()  # the whole-project run did not happen
    assert "Single" in capsys.readouterr().err


def test_main_single_word_by_gloss(project, tmp_path):
    # A word absent from the lexicon key but matched by gloss still derives (from its IPA).
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(f'"{ipa}" = "hello"\n', encoding="utf-8")
    main(["--project", str(tmp_path), "--single", "hello"])
    assert (tmp_path / "reports" / "single_derivations.csv").exists()


def test_main_single_word_not_in_lexicon_has_no_target_reports(project, tmp_path):
    # A word not in the lexicon derives bare: only single_derivations.csv, no target reports.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(
        f'"{ipa}" = {{gloss = "x", final = "zzz"}}\n', encoding="utf-8"
    )
    # First a found run writes the target reports, then an absent word must clear them.
    main(["--project", str(tmp_path), "--single", ipa])
    assert (tmp_path / "reports" / "single_accuracy.csv").exists()
    main(["--project", str(tmp_path), "--single", "ˈnot.a.word"])
    reports = tmp_path / "reports"
    assert (reports / "single_derivations.csv").exists()
    assert not (reports / "single_accuracy.csv").exists()  # stale target report cleared


def test_main_skips_accuracy_without_target(project, tmp_path):
    # A lexicon with no attested forms (bare `word = "gloss"`) gets no accuracy report.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(f'"{ipa}" = "x"\n', encoding="utf-8")
    main(["--project", str(tmp_path)])
    assert not (tmp_path / "reports" / "accuracy.csv").exists()


def test_main_writes_accuracy_with_target(project, tmp_path):
    # A minimal project (one word carrying a target `final`, everything else falling
    # back to the default inventory) triggers the accuracy CSVs, in reports/.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(
        f'"{ipa}" = {{gloss = "x", final = "zzz"}}\n', encoding="utf-8"
    )
    main(["--project", str(tmp_path)])
    reports = tmp_path / "reports"
    overall = reports / "accuracy.csv"
    assert overall.exists()
    assert overall.read_text(encoding="utf-8").startswith(
        "stage,assessed,exact,within 1,mean phone dist,mean feature dist"
    )
    assert (reports / "distance_to_target.csv").read_text(encoding="utf-8").startswith(
        "stage,gloss,derived,target,d,fd"
    )
    # No Markdown accuracy report is written.
    assert not (reports / "accuracy.md").exists()
    assert not (reports / "distances.md").exists()


def test_main_run_summary_splits_out_analysis(project, tmp_path, capsys):
    # The end-of-run timing reports `accuracy` and `analysis` (diagnosis + timeline +
    # blame) separately, so each cost is visible.
    ipa = next(iter(project.words))
    (tmp_path / "words.toml").write_text(
        f'"{ipa}" = {{gloss = "x", final = "zzz"}}\n', encoding="utf-8"
    )
    main(["--project", str(tmp_path)])
    err = capsys.readouterr().err
    assert "accuracy" in err and "analysis" in err


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


def test_list_definition_substeps_share_one_heading(project):
    # A list-definition rule's sub-steps (ids `name#1`, `#2`) render under a single
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
    derivation = _derive("koˈta", RuleInventory({-1000: tuple(sub)}), project)
    out = "\n".join(_trace_lines(derivation.steps, project))
    assert out.count("Stress change to first syllable") == 1  # one heading, not per sub-step
    assert out.count(" → ") == 2  # both sub-steps' before → after lines are shown
    assert "stress_change#1" not in out and "stress_change#2" not in out  # suffix hidden


def test_standalone_rule_keeps_its_own_heading(project):
    # A plain (non-list) rule is its own heading, with its id shown when unnamed.
    spec = {"time": 0, "definition": "[+cons] → [-voice]"}
    [rule] = load_rule("devoicing", spec, project.features).unwrap()
    derivation = _derive("ˈba", RuleInventory({0: (rule,)}), project)
    out = "\n".join(_trace_lines(derivation.steps, project))
    assert "0: devoicing" in out  # unnamed rule falls back to its id (no suffix to strip)
