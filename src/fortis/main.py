"""Main entry point for the Fortis phonology engine.

Loads every inventory, then for each word: segments the IPA into feature
bundles, runs it through all rules in time order, and prints a step-by-step
derivation showing only the rules that changed the form, with syllable
structure (``.`` between syllables) on the surface. Every run also writes a
Markdown report (``<project>/output.md`` by default; ``--output`` overrides
the path) and ``derivation_table.csv`` alongside it (one row per word, one
column per rule, holding the word's resulting form wherever that rule fired).
When the lexicon carries attested forms (``final`` and/or intermediate
``stages``), a ``distances.md`` summary grading the derivation against them is
written too.
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

from src.fortis.analysis.blame import blame_all, blame_summary_line, render_blame
from src.fortis.analysis.diagnosis import (
    confusions,
    diagnose_stages,
    diagnosis_summary_line,
    errors_by_time,
    render_diagnosis,
    render_timeline,
    timeline_summary_line,
)
from src.fortis.analysis.filtering import MatchedWord, FilterResult, filter_by_pattern, filter_summary_line
from src.fortis.analysis.grading import grade, grade_derivation, grade_stages
from src.fortis.analysis.reporting import distance_summary_line, render_distance_summary
from src.fortis.analysis.warnings import (
    render_warnings,
    syllabification_warnings,
    warnings_summary_line,
)
from src.fortis.application.deriving import derive_all, resolve_rule_letters
from src.fortis.application.rendering import describe_change, render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.config import config
from src.fortis.loaders.project import load_project
from src.fortis.models.derivation import Derivation, DerivationStep
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory
from src.fortis.result import Err, Ok

# Sentinel: no ``--output`` path given (the default) ⇒ write to ``<project>/output.md``.
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
            "path for the Markdown report — the firing-rule trace per word. Always "
            "written, alongside the printed trace and a derivation_table.csv report (one "
            "row per word, one column per rule) (default path: <project>/output.md)"
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
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Load inventories, derive every word, print the traces, and write the reports.

    With no arguments, runs every shipped rule over every shipped word. ``--words`` and
    ``--rules`` override just the lexicon and the sound-change file; the feature system,
    letters, sonority, tiers, etc. stay the shipped defaults unless ``--project`` points to
    a project directory (whose own files override the defaults, the rest falling back).
    Every run writes ``output.md`` (the trace, ``--output`` overrides the path) and
    ``derivation_table.csv`` (one row per word, one column per rule) into the same
    directory; if the lexicon has attested forms, a ``distances.md`` summary too.
    Ends with a run summary on stderr: words derived, rules applied, per-phase
    timing (init, apply, print), and the files saved.
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
    try:
        derivations = derive_all(project, on_progress=_progress_bar)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    derive_done = time.perf_counter()

    # Phase 3 — printing: write the reports and print the traces.
    output_dir = args.project or config.paths.default
    path = output_dir / "output.md" if args.output is _AUTO_OUTPUT else args.output
    path.write_text(_build_report(derivations, project, args.project), encoding="utf-8")
    print(f"wrote {path}", file=sys.stderr)
    saved = [path]

    csv_path = path.parent / "derivation_table.csv"
    csv_path.write_text(_build_csv_report(derivations, rules, project), encoding="utf-8")
    print(f"wrote {csv_path}", file=sys.stderr)
    saved.append(csv_path)
    write_done = time.perf_counter()

    where = f"`{args.project}`" if args.project is not None else "the shipped `projects/default`"

    # Phase 4 — grading: if the lexicon carries attested forms (final and/or
    # intermediate stages), grade the derivation against them and write a summary.
    graded = any(word.final is not None or word.stages for word in project.words.values())
    grade_split = write_done  # split point between grading and the (costlier) analysis
    if graded:
        stages = grade_stages(derivations, project)
        dist_path = path.parent / "distances.md"
        dist_path.write_text(render_distance_summary(stages, where), encoding="utf-8")
        print(f"wrote {dist_path}", file=sys.stderr)
        saved.append(dist_path)
        print(distance_summary_line(stages))
        grade_split = time.perf_counter()  # grading done; what follows is analysis

        # Diagnose where the final derivation goes wrong (confusions + context autopsy).
        grades = next(s for s in stages if s.time is None).report.grades
        diag_path = path.parent / "diagnosis.md"
        diag_path.write_text(render_diagnosis(grades, project, where), encoding="utf-8")
        print(f"wrote {diag_path}", file=sys.stderr)
        saved.append(diag_path)
        print(diagnosis_summary_line(grades))

        # Blame + the temporal views share the per-word blames (computed once).
        blames = blame_all(derivations, project)
        buckets = errors_by_time(blames)
        stage_diag = diagnose_stages(derivations, project)
        timeline_path = path.parent / "timeline.md"
        timeline_path.write_text(
            render_timeline(buckets, stage_diag, project, where), encoding="utf-8"
        )
        print(f"wrote {timeline_path}", file=sys.stderr)
        saved.append(timeline_path)
        print(timeline_summary_line(buckets))

        # Attribute each wrong word to the rule that produced it (blame.md).
        blame_path = path.parent / "blame.md"
        blame_path.write_text(render_blame(blames, where), encoding="utf-8")
        print(f"wrote {blame_path}", file=sys.stderr)
        saved.append(blame_path)
        print(blame_summary_line(blames))
    grade_done = time.perf_counter()

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
                    _build_csv_report([m.derivation for m in result.matched], rules, project),
                    encoding="utf-8",
                )
                foutput_path = path.parent / "filtered_output.md"
                foutput_path.write_text(_build_filtered_report(result, project, where), encoding="utf-8")
                for report_path in (ftable_path, foutput_path):
                    print(f"wrote {report_path}", file=sys.stderr)
                    saved.append(report_path)
                print(filter_summary_line(result))

    # Phase 5 — printing: print the per-word traces.
    for derivation in derivations:
        _print_derivation(derivation, project)
        print()
    print_done = time.perf_counter()

    phases = {"init": init_done - start, "apply": derive_done - init_done}
    if graded:  # grade = grading + distances.md; analysis = diagnosis + timeline + blame
        phases["grade"] = grade_split - write_done
        phases["analysis"] = grade_done - grade_split
    phases["print"] = (write_done - derive_done) + (print_done - grade_done)
    _print_run_summary(derivations, rules, saved, phases, print_done - start)


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

    ``phases`` maps each phase name (init, apply, grade, analysis, print — grade and
    analysis only when the run graded) to its elapsed seconds; ``total`` is the whole
    run's seconds. Analysis (diagnosis + timeline + blame) is split from grade because
    it is the costlier half — notably ``diagnose_stages``, which re-runs the diagnosis
    at each attested stage.
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


def _print_derivation(derivation: Derivation, project: Project) -> None:
    """Print one word's derivation: headword, each firing rule, then the surface.

    Each firing rule is shown as ``<time>: <rule name>``, with the before → after
    forms and a change summary on the indented line below. Consecutive steps from
    one list-``definition`` rule (sub-rules sharing a ``name#1``/``#2`` id) are
    grouped under a single heading, one change line per sub-step.
    """
    word = derivation.word
    gloss = f' – "{word.gloss}"' if word.gloss else ""
    print("")
    print(f"{word.ipa}{gloss}")  # echo the input verbatim (no render round-trip)

    for line in _trace_lines(derivation.steps, project):
        print(f"    {line}")

    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    print(f"    Surface: {surface}")
    print("")


def _build_report(derivations: list[Derivation], project: Project, project_dir: Path | None) -> str:
    """The whole run as one Markdown document (the ``output.md`` report)."""
    where = f"`{project_dir}`" if project_dir is not None else "the shipped `projects/default`"
    lines = [
        f"# Output — {where}",
        "",
        "Engine-generated run output. For each word: the surface form and the",
        "firing-rule trace (only the rules that changed the form).",
        "",
    ]
    for derivation in derivations:
        lines += _render_derivation_md(derivation, project)
    return "\n".join(lines).rstrip() + "\n"


def _render_derivation_md(derivation: Derivation, project: Project) -> list[str]:
    """One word's derivation as Markdown: surface form and firing-rule trace."""
    word = derivation.word
    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    lines = [f"## {word.gloss or word.ipa}", "", f"`{word.ipa}` → `{surface}`", ""]

    trace = _trace_lines(derivation.steps, project)
    if trace:
        lines += ["```", *trace, "```", ""]

    return lines


def _filtered_word_md(matched: MatchedWord, project: Project) -> list[str]:
    """One matched word for filtered_output.md: its grade, where it matched, and trace."""
    derivation = matched.derivation
    surface = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    lines = [f"### {derivation.word.gloss or derivation.word.ipa}", "", f"`{derivation.word.ipa}` → `{surface}`", ""]
    graded = grade_derivation(derivation, project)
    if graded is not None:
        verdict = "exact" if graded.exact else f"distance {graded.distance}"
        lines.append(f"target `{graded.target}` — {verdict}.")
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
    grading + confusion header, then every matched word's derivation.
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
        lines.append(f"| {matched.derivation.word.gloss or matched.derivation.word.ipa} | {labels} |")
    lines.append("")

    report = grade([matched.derivation for matched in result.matched], project)
    if report.graded:
        lines += [
            "## Subset grading",
            "",
            f"{report.exact}/{report.graded} exact ({report.accuracy:.1%}), mean phone "
            f"{report.mean_distance:.3f}, mean feature {report.mean_feature_distance:.3f}.",
            "",
        ]
        table = confusions(report.grades)
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
    for time in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[time]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in columns:
                label = rule.name or base
                columns[base] = f"{time}: {label}" if time is not None else label
    return list(columns.items())


def _build_csv_report(derivations: list[Derivation], rules: RuleInventory, project: Project) -> str:
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
