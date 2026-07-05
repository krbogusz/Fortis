"""Restrict the analysis to the words whose target form matches a phoneme pattern.

DiaSim's Suite scopes its diagnostics by a *filter sequence* — the etyma matching a
phoneme pattern. This is that filter, at the word (etymon) level: a Fortis sequence
pattern (feature bundles, letters, quantifiers, boundaries — the same notation a rule's
target uses) selects the words whose **attested target** form contains a match, and only
those feed grading, diagnosis, timeline, and blame.

Matching is on the target form (a documented choice — not the input or derived surface),
with stress marks stripped so it lives in the same space as the comparison. A word with
no target is not counted; a word whose target will not segment is counted but excluded
(and reported). A pattern that does not parse, or names an unresolvable symbol, is an
error — never a silent empty result.
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.analysis.grading import _segment
from src.fortis.application.deriving import resolve_rule_letters
from src.fortis.application.matching import find_matches
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule, RuleInventory, StructuralDescription
from src.fortis.parsing.notation import parse_sequence
from src.fortis.result import Err, Ok, Result


@dataclass(frozen=True)
class FilterResult:
    """The words a filter selected, with what it skipped.

    ``considered`` is the words carrying a target (the filter's denominator);
    ``unsegmentable`` is how many of those were excluded because their target would
    not segment.
    """

    pattern: str
    matched: tuple[Derivation, ...]
    considered: int
    unsegmentable: int


def _resolve_pattern(elements, pattern: str, project: Project) -> StructuralDescription:
    """Resolve a parsed pattern's letter runs into per-segment bundles.

    Reuses the rule path (``resolve_rule_letters``), so a complex/multi-segment symbol
    is expanded exactly as it would be in a rule; raises ``ValueError`` on an unknown
    symbol — the case that must error rather than silently match nothing.
    """
    sd = StructuralDescription(target=tuple(elements), result=())
    inventory = RuleInventory({None: (Rule(id="filter", time=None, raw_definition=pattern, sd=sd),)})
    return resolve_rule_letters(inventory, project)[None][0].sd


def filter_by_target(
    derivations: list[Derivation], pattern: str, project: Project
) -> Result[FilterResult, list[str]]:
    """Select the derivations whose attested target matches *pattern*.

    Returns an ``Err`` if the pattern does not parse or names an unresolvable symbol.
    """
    match parse_sequence(pattern, project.features):
        case Err(errs):
            return Err(errs)
        case Ok(elements):
            pass
    if not elements:
        return Err(["filter pattern is empty"])
    try:
        sd = _resolve_pattern(elements, pattern, project)
    except ValueError as error:
        return Err([str(error)])

    matched: list[Derivation] = []
    considered = 0
    unsegmentable = 0
    for derivation in derivations:
        target = derivation.word.final
        if target is None:
            continue  # a word with no target can't be matched (or graded)
        considered += 1
        bundles = _segment(target, project)
        if bundles is None:
            unsegmentable += 1
            continue
        if find_matches(sd, bundles, project.letters):
            matched.append(derivation)
    return Ok(
        FilterResult(
            pattern=pattern, matched=tuple(matched),
            considered=considered, unsegmentable=unsegmentable,
        )
    )


def filter_note(result: FilterResult) -> str:
    """A one-line description of what the filter selected, for report headers/stderr."""
    note = f"filter `{result.pattern}`: {len(result.matched)}/{result.considered} words"
    if result.unsegmentable:
        note += f" ({result.unsegmentable} unsegmentable excluded)"
    return note
