"""Main entry point for the Fortis phonology engine.

Loads every inventory, then for each word segments the IPA into feature
bundles and runs it through all rules in time order. The full step-by-step
derivation is written to the reports, not printed: the terminal shows only
summary and general information (the files written, counts, per-phase timing,
and — when the lexicon carries targets — the accuracy/errors/blame headlines).
Every run writes its reports into a ``reports/`` subfolder of the project
(``--output`` overrides
the main file's path, and everything else follows alongside it). The main
report is ``derivations.csv``, a long-format trace: one row per word × firing
rule (columns ``word, rule, t, before, after, change``), each word bookended by
two synthetic rules — ``input`` (the raw IPA and how the engine ingested it)
and ``output`` (the surface form). A wide ``derivation_matrix.csv`` (one row per
word, one column per rule, holding the word's form wherever that rule fired) and a
``rule_firings.csv`` (one row per rule: the words it matched as ``before → after``
and the distinct segment changes it made) are written alongside it, plus a
``rule_dependencies.html`` — the rule feeding graph (which rule's target needs a
feature an earlier rule produced), as a scrollable timeline. When the lexicon
carries attested forms (``final`` and/or
intermediate ``stages``), the accuracy analysis measures the derivation's distance
to target and writes ``accuracy.csv`` (per-stage summary) and
``distance_to_target.csv`` (per-word) too.
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import sys
import textwrap
import time
from collections.abc import Sequence
from pathlib import Path

from src.fortis.analysis.accuracy import (
    accuracy_by_stage,
    ingest_targets,
)
from src.fortis.analysis.blame import blame_all, blame_summary_line, render_blame_csv
from src.fortis.analysis.dependencies import build_dependency_graph, render_dependency_html
from src.fortis.analysis.diagnosis import (
    diagnose_stages,
    error_context_omissions,
    errors_summary_line,
    render_error_context_csv,
    render_errors_csv,
)
from src.fortis.analysis.reporting import (
    accuracy_summary_line,
    render_accuracy_csv,
    render_distance_to_target_csv,
)
from src.fortis.analysis.warnings import (
    render_warnings,
    syllabification_warnings,
    warnings_summary_line,
)
from src.fortis.application.deriving import (
    derive,
    derive_all,
    derive_all_parallel,
    resolve_rule_letters,
)
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.config import config
from src.fortis.loaders.project import load_project, unfired_scoped_rules
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.inventories import Word
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory

# Sentinel: no ``--output`` path given (the default) ⇒
# write to ``<project>/reports/derivations.csv``.
_AUTO_OUTPUT = object()

# ANSI colour, on only for an interactive stderr (respecting NO_COLOR).
_COLOR = sys.stderr.isatty() and not os.environ.get("NO_COLOR")


def _sgr(text: str, *codes: str) -> str:
    """Wrap *text* in SGR codes, or return it unchanged when colour is off."""
    return f"\033[{';'.join(codes)}m{text}\033[0m" if _COLOR else text


def _label(text: str) -> str:
    return _sgr(text, "1", "36")  # bold cyan — the Accuracy/Errors/Blame column


def _key(text: str) -> str:
    return _sgr(text, "1")  # bold — the headline figures


def _dim(text: str) -> str:
    return _sgr(text, "2")  # faint — secondary detail and the report list


def _print_scoped_warnings(unfired: list[tuple[str, str]]) -> None:
    """Compactly report word-scoped rules that never fire (scoped to an absent word)."""
    if not unfired:
        return
    rules = list(dict.fromkeys(rule_id for rule_id, _ in unfired))  # distinct, first-seen order
    print(
        f"  {_sgr('⚠', '33')}  {_key(str(len(rules)))} rule(s) never fire — "
        "word-scoped to a word not in the lexicon:",
        file=sys.stderr,
    )
    body = textwrap.fill(
        ", ".join(rules), width=76, initial_indent="     ", subsequent_indent="     "
    )
    print(_dim(body), file=sys.stderr)


def _progress_bar(done: int, total: int, label: str = "deriving") -> None:
    """Render an in-place progress bar on stderr (``deriving``, ``analysing``, …).

    A no-op when stderr is not a terminal (piped or captured output stays clean).
    Redraws on the same line via a carriage return (clearing to end-of-line so a
    shorter redraw leaves no remnants); the final update emits a trailing newline so
    the messages that follow start fresh.
    """
    if total == 0 or not sys.stderr.isatty():
        return
    width = 28
    filled = round(width * done / total)
    bar = "█" * filled + "░" * (width - filled)
    end = "\n" if done == total else ""
    print(f"\r  {label} [{bar}] {done}/{total}\033[K{end}", end="", file=sys.stderr, flush=True)


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    """Parse the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="fortis",
        description=(
            "Run a phonological derivation: segment each word, apply the rules in time order, "
            "and print a step-by-step trace. With no arguments, runs every shipped rule over "
            "every shipped word."
        ),
    )
    parser.add_argument(
        "--project",
        type=Path,
        metavar="DIR",
        help=(
            "a project directory; its files override the shipped defaults and any it omits "
            "fall back to them (default: the shipped projects/default/)"
        ),
    )
    parser.add_argument(
        "--words",
        type=Path,
        metavar="FILE",
        help="lexicon file to run (default: the project's words.toml)",
    )
    parser.add_argument(
        "--rules",
        type=Path,
        metavar="FILE",
        help="sound-change file to apply (default: the project's rules.toml)",
    )
    parser.add_argument(
        "--output",
        nargs="?",
        const=_AUTO_OUTPUT,
        default=_AUTO_OUTPUT,
        type=Path,
        metavar="FILE",
        help=(
            "path for the main report — derivations.csv, the long-format firing-rule "
            "trace (one row per word × rule). The other reports (derivation_matrix.csv, "
            "accuracy.csv, …) are written alongside it (default: "
            "<project>/reports/derivations.csv)"
        ),
    )
    parser.add_argument(
        "--single",
        metavar="WORD",
        help="derive a single word instead of the whole project — looked up in the lexicon by "
        "its IPA key or gloss (so it carries any attested/target forms), else derived bare. "
        "Writes single_*.csv reports (single_derivations.csv, and — with a target — "
        "single_accuracy.csv, single_errors.csv, …) into the project's reports/ subfolder.",
    )
    parser.add_argument(
        "--serial",
        dest="serial",
        action="store_true",
        help="derive in a single process, disabling the automatic multiprocessing "
        "(which otherwise fans a big lexicon across worker processes).",
    )
    parser.add_argument(
        "--workers",
        dest="workers",
        type=int,
        default=None,
        metavar="N",
        help="pin the worker-process count for the parallel derivation "
        "(default: auto, ~CPU count − 2). Ignored with --serial.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load inventories, derive every word, and write the reports (the trace is not printed).

    With no arguments, runs every shipped rule over every shipped word. ``--words`` and
    ``--rules`` override just the lexicon and the sound-change file; the feature system,
    letters, sonority, tiers, etc. stay the shipped defaults unless ``--project`` points to
    a project directory (whose own files override the defaults, the rest falling back).
    Every run writes ``derivations.csv`` (the long-format trace, ``--output`` overrides the
    path) and ``derivation_matrix.csv`` (one row per word, one column per rule) into a
    ``reports/`` subfolder of the project; if the lexicon has attested forms, the
    accuracy CSVs (``accuracy.csv`` + ``distance_to_target.csv``) too.
    A big lexicon is derived across worker processes automatically (identical output);
    ``--serial`` forces a single process and ``--workers N`` pins the pool size.
    Ends with a run summary on stderr: words derived, rules applied, per-phase
    timing (init, apply, write), and the files saved.
    """
    args = _parse_args(argv)

    # Phase 1 — engine initiation: load the inventories and resolve rule letters.
    start = time.perf_counter()
    result = load_project(args.project, words_path=args.words, rules_path=args.rules)
    if result.is_err():
        for error in result.unwrap_err():
            print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
    project = result.unwrap()
    # Resolve the letter+diacritic runs a rule writes (e.g. ʁʷ, au) into segments.
    try:
        rules = resolve_rule_letters(project.rules, project)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    init_done = time.perf_counter()

    # Single-word mode: derive just one word and write single_*.csv, skipping the full run.
    if args.single is not None:
        output_dir = args.project or config.paths.default
        default_path = output_dir / "reports" / "derivations.csv"
        reports_dir = (default_path if args.output is _AUTO_OUTPUT else args.output).parent
        _run_single(project, rules, args.single, reports_dir, start)
        return

    # Phase 2 — rule application: derive every word (with a progress bar on a TTY).
    # Parallel by default — derive_all_parallel fans a big lexicon across worker
    # processes and quietly falls back to serial for small ones; --serial forces it off.
    try:
        if args.serial:
            derivations = derive_all(project, on_progress=_progress_bar)
        else:
            derivations = derive_all_parallel(
                project, workers=args.workers, on_progress=_progress_bar
            )
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    derive_done = time.perf_counter()

    # Phase 3 — write the core derivation reports (the full trace lives here, not the terminal).
    output_dir = args.project or config.paths.default
    default_path = output_dir / "reports" / "derivations.csv"
    path = default_path if args.output is _AUTO_OUTPUT else args.output
    path.parent.mkdir(parents=True, exist_ok=True)  # the reports/ subfolder (or --output's dir)
    path.write_text(_build_derivations_csv(derivations, project), encoding="utf-8")
    saved = [path]
    csv_path = path.parent / "derivation_matrix.csv"
    csv_path.write_text(_build_matrix_csv(derivations, rules, project), encoding="utf-8")
    saved.append(csv_path)
    firings_path = path.parent / "rule_firings.csv"
    firings_path.write_text(_build_rule_firings_csv(derivations, rules, project), encoding="utf-8")
    saved.append(firings_path)
    # The rule dependency (feeding) graph — a static analysis over the rules themselves.
    dep_path = path.parent / "rule_dependencies.html"
    dep_path.write_text(
        render_dependency_html(build_dependency_graph(derivations, rules, project)),
        encoding="utf-8",
    )
    saved.append(dep_path)
    write_done = time.perf_counter()

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    # Phase 4 — accuracy + errors + blame, when the lexicon carries attested forms. Each
    # analysis writes its CSV(s) and contributes a one-line headline to the run summary.
    has_targets = any(word.final is not None or word.stages for word in project.words.values())
    _ANALYSIS_STEPS = 4  # accuracy · errors · blame · warnings — for the progress bar
    summaries: list[tuple[str, str, list[str]]] = []  # (label, headline, sub-lines) rows
    if has_targets:
        _progress_bar(0, _ANALYSIS_STEPS, "analysing")  # accuracy is starting
        ingest_targets(derivations, project)  # segment attested forms once, in the main process
        stages = accuracy_by_stage(derivations, project)
        for name, render in (
            ("accuracy.csv", render_accuracy_csv),
            ("distance_to_target.csv", render_distance_to_target_csv),
        ):
            report_path = path.parent / name
            report_path.write_text(render(stages), encoding="utf-8")
            saved.append(report_path)
        acc = accuracy_summary_line(stages).removeprefix("final: ")
        acc_head, _, stage_tail = acc.partition(" · stages ")
        acc_subs = [f"also at stages {stage_tail}"] if stage_tail else []
        summaries.append(("Accuracy", acc_head, acc_subs))
        _progress_bar(1, _ANALYSIS_STEPS, "analysing")  # accuracy done; errors next

        # Errors + Error context, per attested stage and the final.
        stage_diag = diagnose_stages(derivations, project)
        for name, render in (
            ("errors.csv", render_errors_csv),
            ("error_context.csv", render_error_context_csv),
        ):
            report_path = path.parent / name
            report_path.write_text(render(stage_diag), encoding="utf-8")
            saved.append(report_path)
        err_subs: list[str] = []
        # Say plainly what error_context.csv left out — segments too sparse to autopsy.
        omitted = error_context_omissions(stage_diag)
        if omitted:
            shown = ", ".join(f"{seg} @ {label}" for label, seg in omitted[:10])
            more = f", +{len(omitted) - 10} more" if len(omitted) > 10 else ""
            err_subs.append(
                f"{len(omitted)} segment(s) too sparse to autopsy — omitted from "
                f"error_context.csv: {shown}{more}"
            )
        err_head = errors_summary_line(stage_diag).removeprefix("final: ").split(" — see")[0]
        summaries.append(("Errors", err_head, err_subs))
        _progress_bar(2, _ANALYSIS_STEPS, "analysing")  # errors done; blame next

        # Every assessed word's distance trajectory, worst first (blame.csv).
        blames = blame_all(derivations, project, include_exact=True)
        blame_path = path.parent / "blame.csv"
        blame_path.write_text(render_blame_csv(blames), encoding="utf-8")
        saved.append(blame_path)
        summaries.append(("Blame", blame_summary_line(blames).split(" — see")[0], []))
        _progress_bar(3, _ANALYSIS_STEPS, "analysing")  # blame done; warnings next
    accuracy_done = time.perf_counter()

    # Phase 4b — syllabification warnings: words whose onset/coda patterns admitted no
    # legal split and fell back to sonority. Only written when there is something to report.
    syllab_warnings = syllabification_warnings(derivations, project)
    warn_path = path.parent / "warnings.md"
    syllab_line = None
    if syllab_warnings:
        warn_path.write_text(render_warnings(syllab_warnings, where), encoding="utf-8")
        saved.append(warn_path)
        syllab_line = warnings_summary_line(syllab_warnings)
    elif warn_path.exists():
        warn_path.unlink()  # a prior run warned but this one doesn't — clear the stale report
    if has_targets:
        _progress_bar(_ANALYSIS_STEPS, _ANALYSIS_STEPS, "analysing")  # done — clears the bar line
    # Word-scoped rules that never fire — reported now, after the deriving/analysing bars.
    _print_scoped_warnings(unfired_scoped_rules(project.rules, project.words))

    # Phase 5 — the run summary block on stderr.
    done = time.perf_counter()
    phases = {"init": init_done - start, "apply": derive_done - init_done}
    if has_targets:  # analysis = accuracy + errors + error context + blame, timed as one phase
        phases["analysis"] = accuracy_done - write_done
    phases["write"] = (write_done - derive_done) + (done - accuracy_done)
    _print_summary(
        derivations, rules, saved, phases, done - start,
        summaries=summaries, syllab_line=syllab_line, reports_dir=path.parent,
    )


_SUBRULE_SUFFIX = re.compile(r"#\d+$")


def _applied_rule_count(derivations: list[Derivation]) -> int:
    """How many distinct rules fired at least once across the run.

    Sub-rules of one list-``definition`` (ids ``name#1``/``#2``) count once, to
    match the CSV's rule columns.
    """
    fired = {_SUBRULE_SUFFIX.sub("", step.rule.id) for d in derivations for step in d.steps}
    return len(fired)


def _print_summary(
    derivations: list[Derivation],
    rules: RuleInventory,
    saved: list[Path],
    phases: dict[str, float],
    total: float,
    *,
    summaries: list[tuple[str, str, list[str]]],
    syllab_line: str | None,
    reports_dir: Path,
) -> None:
    """Print the end-of-run summary to stderr: analysis headlines, run stats, and reports.

    ``summaries`` are ``(label, headline, sub-lines)`` rows (Accuracy/Errors/Blame), the
    sub-lines shown dimmed under the headline; ``syllab_line`` is the syllabification-fallback
    warning if any. ``phases`` maps each phase name (init, apply, analysis, write — analysis
    only when the run assessed) to its elapsed seconds; ``total`` is the
    whole run's seconds.
    """
    out = sys.stderr
    pad = max((len(label) for label, _, _ in summaries), default=0)
    if summaries:
        print("", file=out)
    for label, headline, subs in summaries:
        print(f"  {_label(label.ljust(pad))}  {headline}", file=out)
        for sub in subs:
            print(f"  {' ' * pad}  {_dim(sub)}", file=out)
    if syllab_line:
        print(f"  {_sgr('⚠', '33')}  {syllab_line}", file=out)

    words = len(derivations)
    applied = _applied_rule_count(derivations)
    total_rules = len(_rule_columns(rules))
    breakdown = " · ".join(f"{name} {secs:.2f}s" for name, secs in phases.items())
    print("", file=out)
    print(
        f"  {_key(str(words))} words · {_key(f'{applied}/{total_rules}')} rules applied · "
        f"{_key(f'{total:.2f}s')}",
        file=out,
    )
    print(f"  {_dim(breakdown)}", file=out)

    print("", file=out)
    print(f"  {_key(str(len(saved)))} reports {_dim('→ ' + str(reports_dir))}", file=out)
    listing = textwrap.fill(
        " · ".join(p.stem for p in saved), width=76, initial_indent="  ", subsequent_indent="  "
    )
    print(_dim(listing), file=out)


def _find_word(project: Project, word_str: str) -> tuple[str, Word, bool]:
    """Locate *word_str* in the lexicon by IPA key or gloss.

    Returns ``(ipa, word, found)``. A hit yields the lexicon entry (its IPA key drives
    derivation, so a gloss lookup still derives the right form, and its attested
    ``final``/``stages`` come along). A miss yields a bare ``Word(ipa=word_str)`` — derived
    with no target — and ``found`` False.
    """
    for ipa, word in project.words.items():
        if ipa == word_str or word.gloss == word_str:
            return ipa, word, True
    return word_str, Word(ipa=word_str), False


def _run_single(
    project: Project,
    rules: RuleInventory,
    word_str: str,
    reports_dir: Path,
    start: float,
) -> None:
    """Derive one word and write the ``single_*.csv`` reports, then print a compact summary.

    Only ``single_derivations.csv`` is unconditional; the target-based reports
    (``single_accuracy.csv``, ``single_distance_to_target.csv``, ``single_errors.csv``,
    ``single_error_context.csv``, ``single_blame.csv``) are written only when the word
    carries an attested form, and any stale copies from a prior run are cleared otherwise.
    """
    ipa, word, found = _find_word(project, word_str)
    derivation = derive(
        word, string_to_sequence(ipa, project), rules, project.letters, project.features,
        project.sonorities, project.syllable_parts, project.tiers,
    )
    derivations = [derivation]
    reports_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []

    def write(name: str, text: str) -> None:
        report_path = reports_dir / name
        report_path.write_text(text, encoding="utf-8")
        saved.append(report_path)

    def write_or_clear(name: str, text: str | None) -> None:
        report_path = reports_dir / name
        if text is not None:
            report_path.write_text(text, encoding="utf-8")
            saved.append(report_path)
        elif report_path.exists():
            report_path.unlink()  # a prior single run wrote it but this word has no target

    write("single_derivations.csv", _build_derivations_csv(derivations, project))
    has_target = word.final is not None or bool(word.stages)
    acc_line: str | None = None
    if has_target:
        ingest_targets(derivations, project)
        stages = accuracy_by_stage(derivations, project)
        write("single_accuracy.csv", render_accuracy_csv(stages))
        write("single_distance_to_target.csv", render_distance_to_target_csv(stages))
        stage_diag = diagnose_stages(derivations, project)
        write("single_errors.csv", render_errors_csv(stage_diag))
        write("single_error_context.csv", render_error_context_csv(stage_diag))
        blames = blame_all(derivations, project, include_exact=True)
        write("single_blame.csv", render_blame_csv(blames))
        acc_line = accuracy_summary_line(stages).removeprefix("final: ")
    else:
        for name in (
            "single_accuracy.csv", "single_distance_to_target.csv", "single_errors.csv",
            "single_error_context.csv", "single_blame.csv",
        ):
            write_or_clear(name, None)

    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    out = sys.stderr
    gloss = f" ‘{word.gloss}’" if word.gloss else ""
    print("", file=out)
    print(f"  {_label('Single'.ljust(8))}  {_key(ipa)}{gloss}  →  {_key(surface)}", file=out)
    tag = "in the lexicon" if found else "not in the lexicon — derived without a target"
    print(f"  {' ' * 8}  {_dim(tag)}", file=out)
    if acc_line is not None:
        print(f"  {_label('Accuracy')}  {acc_line}", file=out)
    print("", file=out)
    print(f"  {_key(f'{time.perf_counter() - start:.2f}s')}", file=out)
    print("", file=out)
    print(f"  {_key(str(len(saved)))} reports {_dim('→ ' + str(reports_dir))}", file=out)
    listing = textwrap.fill(
        " · ".join(p.stem for p in saved), width=76, initial_indent="  ", subsequent_indent="  "
    )
    print(_dim(listing), file=out)


def _trace_lines(steps: Sequence[DerivationStep], project: Project) -> list[str]:
    """The firing-rule trace, shared by the CLI and Markdown renders.

    A ``<time>: <name>`` head per rule group — consecutive sub-rules of one list-``definition``
    rule (``name#1``/``#2``) share a head — then an indented ``<before> → <after>   (<change>)``
    line per step. The CLI render prefixes each line with four more spaces.
    """
    lines: list[str] = []
    previous_base: str | None = None
    for step in steps:
        before = render_syllabified(lower_tiers(step.before), step.before_boundaries, project)
        after = render_syllabified(lower_tiers(step.after), step.after_boundaries, project)
        change = describe_change(lower_tiers(step.before), lower_tiers(step.after), project)
        base = _SUBRULE_SUFFIX.sub("", step.rule.id)
        if base != previous_base:
            label = step.rule.name or base
            lines.append(f"{step.rule.time}: {label}" if step.rule.time is not None else label)
            previous_base = base
        lines.append(f"    {before} → {after}   ({change})")
    return lines


def _build_derivations_csv(derivations: list[Derivation], project: Project) -> str:
    """Long-format derivation trace: one row per word × firing rule.

    Columns: ``word, rule, t, before, after, change``. Each word is bookended by
    two synthetic rules — ``input`` (``before`` = the raw IPA as given, ``after`` =
    the form the engine ingested it as: syllabified, diacritics normalised) and
    ``output`` (``after`` = the surface form). Between them, one row per firing rule
    with its ``before``/``after`` forms, the rule ``time`` in ``t``, and a change
    summary. A word on which no rule fired is just its ``input`` and ``output`` rows.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["word", "rule", "t", "before", "after", "change"])
    for derivation in derivations:
        word = derivation.word
        name = word.ipa  # the lexicon key — the one unambiguous per-word identifier
        # input.after — how the engine ingested the raw IPA. With no steps the input is
        # the surface, so its boundaries stand in (the same fallback the blame trace uses).
        input_boundaries = (
            derivation.steps[0].before_boundaries if derivation.steps
            else derivation.surface_boundaries
        )
        ingested = render_syllabified(lower_tiers(derivation.input), input_boundaries, project)
        writer.writerow([name, "input", "", word.ipa, ingested, ""])
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            before = render_syllabified(lower_tiers(step.before), step.before_boundaries, project)
            after = render_syllabified(lower_tiers(step.after), step.after_boundaries, project)
            change = describe_change(lower_tiers(step.before), lower_tiers(step.after), project)
            t = "" if step.rule.time is None else step.rule.time
            writer.writerow([name, step.rule.name or base, t, before, after, change])
        surface = render_syllabified(
            lower_tiers(derivation.surface), derivation.surface_boundaries, project
        )
        writer.writerow([name, "output", "", "", surface, ""])
    return buffer.getvalue()


def _rule_rows(rules: RuleInventory) -> list[tuple[str, str, int | None, tuple[str, ...]]]:
    """Each rule as ``(base_id, name, time, words)``, sub-rules merged, in firing order.

    Like :func:`_rule_columns`, but keeping the name, time, and word-scope apart (the
    per-rule report wants them in separate columns). ``words`` is the rule's ``words``
    scope — non-empty only for a sporadic/lexical, word-scoped rule.
    """
    seen: dict[str, tuple[str, int | None, tuple[str, ...]]] = {}
    for t in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[t]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in seen:
                seen[base] = (rule.name or base, t, rule.words)
    return [(base, name, t, words) for base, (name, t, words) in seen.items()]


def _build_rule_firings_csv(
    derivations: list[Derivation], rules: RuleInventory, project: Project
) -> str:
    """Per-rule firing report: one row per rule, what it matched and how it changed it.

    Columns: ``rule, t, sporadic, count, changes, matched``. ``sporadic`` is the rule's
    ``words`` scope (comma-separated) — non-empty only for a word-scoped, lexical/sporadic
    rule, empty for a general one. ``count`` is how many words the rule changed; ``changes``
    is the *distinct individual* segment-level deltas it made (e.g. ``d→t``), comma-separated
    and deduped per delta (so a word with two ``w→ɣʷ`` in one firing does not inflate the
    list); ``matched`` is each such word as ``before → after`` (comma-separated, in
    derivation order). Every rule gets a row in firing order — one that never fired shows
    ``count`` 0 with empty ``changes``/``matched``, so dead rules are visible. A
    list-``definition`` rule's sub-rules are merged into one row, matching the other tables.
    """
    matched: dict[str, list[str]] = {}
    changes: dict[str, dict[str, None]] = {}  # ordered set of individual deltas, deduped
    for derivation in derivations:
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            before_bundles = lower_tiers(step.before)
            after_bundles = lower_tiers(step.after)
            before = render_syllabified(before_bundles, step.before_boundaries, project)
            after = render_syllabified(after_bundles, step.after_boundaries, project)
            change = describe_change(before_bundles, after_bundles, project)
            matched.setdefault(base, []).append(f"{before} → {after}")
            # describe_change joins a firing's individual deltas with ", "; split them back
            # out so the distinct set is per delta, not per firing (dedupes repeats like a
            # two-w word's "w→ɣʷ, w→ɣʷ").
            for delta in change.split(", "):
                if delta:
                    changes.setdefault(base, {})[delta] = None
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["rule", "t", "sporadic", "count", "changes", "matched"])
    for base, name, rule_time, words in _rule_rows(rules):
        firings = matched.get(base, [])
        writer.writerow([
            name,
            "" if rule_time is None else rule_time,
            ", ".join(words),
            len(firings),
            ", ".join(changes.get(base, {})),
            ", ".join(firings),
        ])
    return buffer.getvalue()


def _rule_columns(rules: RuleInventory) -> list[tuple[str, str]]:
    """Ordered ``(base_id, title)`` pairs, one per rule, in firing order.

    The title is ``<time>: <name>`` (just the name for an untimed rule), matching
    the trace headings. A list-``definition`` rule's sub-rules (``name#1``,
    ``name#2``, ...) share one column, matching how the Markdown report groups
    them under one heading.
    """
    columns: dict[str, str] = {}
    for t in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[t]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in columns:
                label = rule.name or base
                columns[base] = f"{t}: {label}" if t is not None else label
    return list(columns.items())


def _build_matrix_csv(derivations: list[Derivation], rules: RuleInventory, project: Project) -> str:
    """One row per word, one column per rule.

    A cell holds the word's resulting form right after that rule fired (its last
    step, if it fired more than once), or stays empty if the rule never fired on
    that word.
    """
    columns = _rule_columns(rules)
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["ipa", "gloss", *(label for _base, label in columns)])
    for derivation in derivations:
        word = derivation.word
        after_by_base: dict[str, str] = {}
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            after_by_base[base] = render_syllabified(
                lower_tiers(step.after), step.after_boundaries, project
            )
        writer.writerow(
            [word.ipa, word.gloss or "", *(after_by_base.get(base, "") for base, _label in columns)]
        )
    return buffer.getvalue()


if __name__ == "__main__":
    main()
