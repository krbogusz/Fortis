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
and the distinct segment changes it made) are written alongside it. When the lexicon
carries attested forms (``final`` and/or
intermediate ``stages``), the accuracy analysis measures the derivation's distance
to target and writes ``accuracy.csv`` (per-stage summary) and
``distance_to_target.csv`` (per-word) too.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import time
from collections.abc import Sequence
from pathlib import Path

from src.fortis.analysis.accuracy import (
    accuracy_by_stage,
    distance_to_target,
    ingest_targets,
    measure_accuracy,
)
from src.fortis.analysis.blame import blame_all, blame_summary_line, render_blame_csv
from src.fortis.analysis.diagnosis import (
    confusions,
    diagnose_stages,
    error_context_omissions,
    errors_summary_line,
    render_error_context_csv,
    render_errors_csv,
)
from src.fortis.analysis.filtering import (
    FilterResult,
    MatchedWord,
    filter_by_pattern,
    filter_summary_line,
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
    derive_all,
    derive_all_parallel,
    resolve_rule_letters,
)
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.config import config
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory
from src.fortis.result import Err, Ok

# Sentinel: no ``--output`` path given (the default) ⇒
# write to ``<project>/reports/derivations.csv``.
_AUTO_OUTPUT = object()


def _progress_bar(done: int, total: int) -> None:
    """Render an in-place derivation progress bar on stderr.

    A no-op when stderr is not a terminal (piped or captured output stays clean).
    Redraws on the same line via a carriage return; the final update emits a
    trailing newline so the ``wrote …`` messages that follow start fresh.
    """
    if total == 0 or not sys.stderr.isatty():
        return
    width = 28
    filled = round(width * done / total)
    bar = "█" * filled + "░" * (width - filled)
    end = "\n" if done == total else ""
    print(f"\rderiving [{bar}] {done}/{total}{end}", end="", file=sys.stderr, flush=True)


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
        "--filter",
        dest="filter",
        metavar="PATTERN",
        help="after the run, synthesise the words a sequence pattern touches in ANY form "
        "(input, intermediate, surface, target, stage) into filtered_output.md + "
        "filtered_table.csv, e.g. 't̪ [aperture: high]'",
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

    # Phase 3 — printing: write the reports and print the traces.
    output_dir = args.project or config.paths.default
    default_path = output_dir / "reports" / "derivations.csv"
    path = default_path if args.output is _AUTO_OUTPUT else args.output
    path.parent.mkdir(parents=True, exist_ok=True)  # the reports/ subfolder (or --output's dir)
    path.write_text(_build_derivations_csv(derivations, project), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    saved = [path]

    csv_path = path.parent / "derivation_matrix.csv"
    csv_path.write_text(_build_matrix_csv(derivations, rules, project), encoding="utf-8")
    print(f"wrote {csv_path}", file=sys.stderr)
    saved.append(csv_path)

    firings_path = path.parent / "rule_firings.csv"
    firings_path.write_text(_build_rule_firings_csv(derivations, rules, project), encoding="utf-8")
    print(f"wrote {firings_path}", file=sys.stderr)
    saved.append(firings_path)
    write_done = time.perf_counter()

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    # Phase 4 — accuracy: if the lexicon carries attested forms (final and/or
    # intermediate stages), measure the derivation's distance to target and write the
    # accuracy CSVs (per-stage summary + the per-word distance-to-target table).
    has_targets = any(word.final is not None or word.stages for word in project.words.values())
    accuracy_split = write_done  # split point between accuracy and the (costlier) analysis
    if has_targets:
        ingest_targets(derivations, project)  # segment attested forms once, in the main process
        stages = accuracy_by_stage(derivations, project)
        for name, render in (
            ("accuracy.csv", render_accuracy_csv),
            ("distance_to_target.csv", render_distance_to_target_csv),
        ):
            report_path = path.parent / name
            report_path.write_text(render(stages), encoding="utf-8")
            print(f"wrote {report_path}", file=sys.stderr)
            saved.append(report_path)
        print(accuracy_summary_line(stages))
        accuracy_split = time.perf_counter()  # accuracy done; what follows is analysis

        # Errors + Error context, per attested stage and the final: which segments came
        # out wrong, and the environments most associated with each.
        stage_diag = diagnose_stages(derivations, project)
        for name, render in (
            ("errors.csv", render_errors_csv),
            ("error_context.csv", render_error_context_csv),
        ):
            report_path = path.parent / name
            report_path.write_text(render(stage_diag), encoding="utf-8")
            print(f"wrote {report_path}", file=sys.stderr)
            saved.append(report_path)
        print(errors_summary_line(stage_diag))
        # Say plainly what error_context.csv left out — segments that erred but were too
        # sparse to autopsy (< min_errors) or had no error-associated environment.
        omitted = error_context_omissions(stage_diag)
        if omitted:
            shown = ", ".join(f"{seg} @ {label}" for label, seg in omitted[:10])
            more = f", +{len(omitted) - 10} more" if len(omitted) > 10 else ""
            print(
                f"note: {len(omitted)} erroring segment(s) omitted from error_context.csv "
                f"(too few errors or no error-associated environment): {shown}{more}",
                file=sys.stderr,
            )

        # Every assessed word's distance trajectory, worst first (blame.csv). Exact words are
        # included as short d=0 paths; the residuals + culprit rules live in the web Blame tab.
        blames = blame_all(derivations, project, include_exact=True)
        blame_path = path.parent / "blame.csv"
        blame_path.write_text(render_blame_csv(blames), encoding="utf-8")
        print(f"wrote {blame_path}", file=sys.stderr)
        saved.append(blame_path)
        print(blame_summary_line(blames))
    accuracy_done = time.perf_counter()

    # Phase 4b — syllabification warnings: words whose onset/coda patterns admitted no
    # legal split and fell back to sonority. Only written when there is something to report.
    warnings = syllabification_warnings(derivations, project)
    warn_path = path.parent / "warnings.md"
    if warnings:
        warn_path.write_text(render_warnings(warnings, where), encoding="utf-8")
        print(f"wrote {warn_path}", file=sys.stderr)
        saved.append(warn_path)
        print(warnings_summary_line(warnings), file=sys.stderr)
    elif warn_path.exists():
        warn_path.unlink()  # a prior run warned but this one doesn't — clear the stale report

    # Phase 4c — filter: a post-run pass. --filter synthesises the words a pattern touches
    # in ANY form (input → intermediate → surface → target → stage) into two extra files.
    if args.filter is not None:
        match filter_by_pattern(derivations, args.filter, project):
            case Err(errs):
                for error in errs:
                    print(f"error: --filter: {error}", file=sys.stderr)
                raise SystemExit(1)
            case Ok(result):
                ftable_path = path.parent / "filtered_table.csv"
                ftable_path.write_text(
                    _build_matrix_csv([m.derivation for m in result.matched], rules, project),
                    encoding="utf-8",
                )
                foutput_path = path.parent / "filtered_output.md"
                foutput_path.write_text(
                    _build_filtered_report(result, project, where), encoding="utf-8"
                )
                for report_path in (ftable_path, foutput_path):
                    print(f"wrote {report_path}", file=sys.stderr)
                    saved.append(report_path)
                print(filter_summary_line(result))

    # Phase 5 — summary: the full per-word trace lives in derivations.csv, not the
    # terminal; only the run summary and headlines are printed.
    done = time.perf_counter()
    phases = {"init": init_done - start, "apply": derive_done - init_done}
    if has_targets:  # accuracy = the distance CSVs; analysis = errors + error context + blame
        phases["accuracy"] = accuracy_split - write_done
        phases["analysis"] = accuracy_done - accuracy_split
    phases["write"] = (write_done - derive_done) + (done - accuracy_done)
    _print_run_summary(derivations, rules, saved, phases, done - start)


_SUBRULE_SUFFIX = re.compile(r"#\d+$")


def _applied_rule_count(derivations: list[Derivation]) -> int:
    """How many distinct rules fired at least once across the run.

    Sub-rules of one list-``definition`` (ids ``name#1``/``#2``) count once, to
    match the CSV's rule columns.
    """
    fired = {_SUBRULE_SUFFIX.sub("", step.rule.id) for d in derivations for step in d.steps}
    return len(fired)


def _print_run_summary(
    derivations: list[Derivation],
    rules: RuleInventory,
    saved: list[Path],
    phases: dict[str, float],
    total: float,
) -> None:
    """Print the end-of-run summary to stderr: counts, timing, and saved files.

    ``phases`` maps each phase name (init, apply, accuracy, analysis, write — accuracy and
    analysis only when the run assessed) to its elapsed seconds; ``total`` is the whole
    run's seconds. Analysis (errors + error context + blame) is split from accuracy because
    it is the costlier half — notably ``diagnose_stages``, which tallies confusions and
    autopsies every erroring segment at each attested stage.
    """
    words = len(derivations)
    applied = _applied_rule_count(derivations)
    total_rules = len(_rule_columns(rules))
    breakdown = ", ".join(f"{name} {secs:.2f}s" for name, secs in phases.items())
    names = ", ".join(path.name for path in saved)
    print(
        f"\n{words} words derived, {applied} of {total_rules} rules applied\n"
        f"elapsed {total:.2f}s ({breakdown})\n"
        f"saved {names}",
        file=sys.stderr,
    )


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


def _rule_rows(rules: RuleInventory) -> list[tuple[str, str, int | None]]:
    """Each rule as ``(base_id, name, time)``, sub-rules merged, in firing order.

    Like :func:`_rule_columns`, but keeping the name and time apart (the per-rule report
    wants them in separate columns).
    """
    seen: dict[str, tuple[str, int | None]] = {}
    for t in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[t]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in seen:
                seen[base] = (rule.name or base, t)
    return [(base, name, t) for base, (name, t) in seen.items()]


def _build_rule_firings_csv(
    derivations: list[Derivation], rules: RuleInventory, project: Project
) -> str:
    """Per-rule firing report: one row per rule, what it matched and how it changed it.

    Columns: ``rule, t, count, matched, changes``. ``count`` is how many words the rule
    changed; ``matched`` is each such word as ``before → after`` (comma-separated, in
    derivation order); ``changes`` is the *distinct* segment-level deltas it made (e.g.
    ``d→t``), comma-separated. Every rule gets a row in firing order — one that never fired
    shows ``count`` 0 with empty ``matched``/``changes``, so dead rules are visible. A
    list-``definition`` rule's sub-rules are merged into one row, matching the other tables.
    """
    matched: dict[str, list[str]] = {}
    changes: dict[str, dict[str, None]] = {}  # ordered set: first-seen order, deduped
    for derivation in derivations:
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            before_bundles = lower_tiers(step.before)
            after_bundles = lower_tiers(step.after)
            before = render_syllabified(before_bundles, step.before_boundaries, project)
            after = render_syllabified(after_bundles, step.after_boundaries, project)
            change = describe_change(before_bundles, after_bundles, project)
            matched.setdefault(base, []).append(f"{before} → {after}")
            changes.setdefault(base, {})[change] = None
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["rule", "t", "count", "matched", "changes"])
    for base, name, rule_time in _rule_rows(rules):
        firings = matched.get(base, [])
        writer.writerow([
            name,
            "" if rule_time is None else rule_time,
            len(firings),
            ", ".join(firings),
            ", ".join(changes.get(base, {})),
        ])
    return buffer.getvalue()


def _filtered_word_md(matched: MatchedWord, project: Project) -> list[str]:
    """One matched word for filtered_output.md: distance to target, match sites, and trace."""
    derivation = matched.derivation
    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    lines = [
        f"### {derivation.word.gloss or derivation.word.ipa}",
        "",
        f"`{derivation.word.ipa}` → `{surface}`",
        "",
    ]
    measured = distance_to_target(derivation, project)
    if measured is not None:
        verdict = "exact" if measured.exact else f"distance {measured.distance}"
        lines.append(f"target `{measured.target}` — {verdict}.")
    lines.append("matched at: " + ", ".join(f"`{loc.label}`" for loc in matched.locations))
    lines.append("")
    trace = _trace_lines(derivation.steps, project)
    if trace:
        lines += ["```", *trace, "```", ""]
    return lines


def _build_filtered_report(result: FilterResult, project: Project, where: str) -> str:
    """The ``filtered_output.md`` synthesis: where the pattern appears, then each trace.

    Trace-centric: a matched word usually derives correctly (the pattern arose and
    resolved), so the payload is *which* words pass through it and *where* — a subset
    accuracy + confusion header, then every matched word's derivation.
    """
    lines = [
        f"# Filtered — {where} · filter `{result.pattern}`",
        "",
        f"Matched **{len(result.matched)} of {result.considered}** words where `{result.pattern}`",
        "appears in some form — the input, an intermediate derived form, the surface, the",
        "attested target, or a stage. Most matched words derive correctly; this shows *which*",
        "words pass through the pattern and *where*, with each word's trace below.",
        "",
    ]
    if not result.matched:
        return "\n".join([*lines, "No word matched."]).rstrip() + "\n"

    lines += ["## Where matched", "", "| word | matched at |", "| --- | --- |"]
    for matched in result.matched:
        labels = ", ".join(f"`{loc.label}`" for loc in matched.locations)
        name = matched.derivation.word.gloss or matched.derivation.word.ipa
        lines.append(f"| {name} | {labels} |")
    lines.append("")

    report = measure_accuracy([matched.derivation for matched in result.matched], project)
    if report.assessed:
        lines += [
            "## Subset accuracy",
            "",
            f"{report.exact}/{report.assessed} exact ({report.accuracy:.1%}), mean phone "
            f"{report.mean_distance:.3f}, mean feature {report.mean_feature_distance:.3f}.",
            "",
        ]
        table = confusions(report.distances)
        if table:
            lines += [
                "Confusions among the matched words (counts only — the subset is too small",
                "for the phi autopsy):",
                "",
                "| expected | got | count | examples |",
                "| --- | --- | ---: | --- |",
            ]
            for c in table:
                exp = f"`{c.expected}`" if c.expected is not None else "`∅`"
                got = f"`{c.got}`" if c.got is not None else "`∅`"
                lines.append(f"| {exp} | {got} | {c.count} | {', '.join(c.examples)} |")
            lines.append("")

    lines += ["## Derivations", ""]
    for matched in result.matched:
        lines += _filtered_word_md(matched, project)
    return "\n".join(lines).rstrip() + "\n"


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
