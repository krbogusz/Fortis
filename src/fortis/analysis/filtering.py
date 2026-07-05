"""Find the words a phoneme pattern touches anywhere in their derivation.

DiaSim's Suite scopes its diagnostics by a *filter sequence* — the etyma matching a
phoneme pattern. This is the word-level equivalent, but matched against **every form a
word takes**: its input, each intermediate derived form, the surface, the attested
target, and each attested stage. A word is selected if the pattern (Fortis sequence
notation — feature bundles, letters, quantifiers, boundaries, the same a rule target
uses) matches in *any* of those, and each match records **where** it occurred.

Because the pattern may appear transiently — arising at one rule and resolving at a
later one — a matched word is usually *correctly* derived: the payload is *which* words
pass through the configuration and *where*, not an error analysis. Matching a derived
form uses the lowered segments the engine itself matches rules against; an attested
string is segmented (stress-stripped) and skipped if it will not segment (the word may
still match on another form). A pattern that fails to parse or names an unresolvable
symbol is an error, never a silent empty result.
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.analysis.grading import _segment
from src.fortis.application.deriving import resolve_rule_letters
from src.fortis.application.matching import find_matches
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.derivation import Derivation
from src.fortis.models.form import Form
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule, RuleInventory, StructuralDescription
from src.fortis.parsing.notation import parse_sequence
from src.fortis.result import Err, Ok, Result


@dataclass(frozen=True)
class Location:
    """One form of a word in which the pattern matched, and how it was rendered."""

    label: str  # "input", "t=750", "surface", "target", or "stage 1000"
    form: str


@dataclass(frozen=True)
class MatchedWord:
    """A word the filter selected, with every form the pattern matched in."""

    derivation: Derivation
    locations: tuple[Location, ...]


@dataclass(frozen=True)
class FilterResult:
    """The words a pattern touches. ``considered`` is every word (all have a derivation)."""

    pattern: str
    matched: tuple[MatchedWord, ...]
    considered: int


def _resolve_pattern(elements, pattern: str, project: Project) -> StructuralDescription:
    """Resolve a parsed pattern's letter runs, exactly as a rule target is resolved.

    Raises ``ValueError`` on an unknown symbol — the case that must error rather than
    silently match nothing.
    """
    sd = StructuralDescription(target=tuple(elements), result=())
    inventory = RuleInventory({None: (Rule(id="filter", time=None, raw_definition=pattern, sd=sd),)})
    return resolve_rule_letters(inventory, project)[None][0].sd


def _matches(sd: StructuralDescription, bundles, project: Project) -> bool:
    return bundles is not None and bool(find_matches(sd, bundles, project.letters))


def _locations(derivation: Derivation, sd: StructuralDescription, project: Project) -> list[Location]:
    """Every form of *derivation* the pattern matches in, one entry per distinct phase.

    Deduped by *label*, so a pattern that persists across several rules at one time
    collapses to a single ``t=600`` entry (the era it was present), not one per rule.
    """
    locations: list[Location] = []
    seen: set[str] = set()

    def consider(label: str, bundles, rendered: str) -> None:
        if label not in seen and _matches(sd, bundles, project):
            seen.add(label)
            locations.append(Location(label, rendered))

    def derived(label: str, form: Form, boundaries) -> None:
        bundles = lower_tiers(form)
        consider(label, bundles, render_syllabified(bundles, boundaries, project))

    input_boundaries = (
        derivation.steps[0].before_boundaries if derivation.steps else derivation.surface_boundaries
    )
    derived("input", derivation.input, input_boundaries)
    for step in derivation.steps:
        label = f"t={step.rule.time}" if step.rule.time is not None else step.rule.id
        derived(label, step.after, step.after_boundaries)
    derived("surface", derivation.surface, derivation.surface_boundaries)

    if derivation.word.final is not None:
        consider("target", _segment(derivation.word.final, project), derivation.word.final)
    for time, form in sorted(derivation.word.stages.items()):
        consider(f"stage {time}", _segment(form, project), form)
    return locations


def _parse_and_resolve(pattern: str, project: Project) -> Result[StructuralDescription, list[str]]:
    """Parse a pattern and resolve its letter runs, or ``Err`` — shared by both filters."""
    match parse_sequence(pattern, project.features):
        case Err(errs):
            return Err(errs)
        case Ok(elements):
            pass
    if not elements:
        return Err(["filter pattern is empty"])
    try:
        return Ok(_resolve_pattern(elements, pattern, project))
    except ValueError as error:
        return Err([str(error)])


def filter_by_pattern(
    derivations: list[Derivation], pattern: str, project: Project
) -> Result[FilterResult, list[str]]:
    """Select the words the pattern matches in any form; ``Err`` if it will not parse/resolve."""
    match _parse_and_resolve(pattern, project):
        case Err(errs):
            return Err(errs)
        case Ok(sd):
            pass
    matched: list[MatchedWord] = []
    for derivation in derivations:
        locations = _locations(derivation, sd, project)
        if locations:
            matched.append(MatchedWord(derivation, tuple(locations)))
    return Ok(FilterResult(pattern=pattern, matched=tuple(matched), considered=len(derivations)))


@dataclass(frozen=True)
class ScopeResult:
    """The words whose attested forms match a pattern (for scoping the error reports).

    ``considered`` is the words carrying any attested form (target or a stage) — the
    scope's denominator; words with none are neither scoped nor graded.
    """

    pattern: str
    matched: tuple[Derivation, ...]
    considered: int


def filter_attested(
    derivations: list[Derivation], pattern: str, project: Project
) -> Result[ScopeResult, list[str]]:
    """Select the words whose **attested** target or any attested stage matches *pattern*.

    Unlike :func:`filter_by_pattern` this looks only at the attested forms (not the derived
    ones), so its subset is the natural population to restrict grading/diagnosis/blame to.
    """
    match _parse_and_resolve(pattern, project):
        case Err(errs):
            return Err(errs)
        case Ok(sd):
            pass
    matched: list[Derivation] = []
    considered = 0
    for derivation in derivations:
        word = derivation.word
        forms = ([word.final] if word.final is not None else []) + list(word.stages.values())
        if not forms:
            continue
        considered += 1
        if any(_matches(sd, _segment(form, project), project) for form in forms):
            matched.append(derivation)
    return Ok(ScopeResult(pattern=pattern, matched=tuple(matched), considered=considered))


def scope_summary_line(result: ScopeResult) -> str:
    """A one-line headline for stderr."""
    return f"scope `{result.pattern}`: {len(result.matched)}/{result.considered} words match an attested form"


def filter_summary_line(result: FilterResult) -> str:
    """A one-line headline for stderr."""
    return f"filter `{result.pattern}`: matched {len(result.matched)}/{result.considered} words"
