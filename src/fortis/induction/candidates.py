"""Candidate rule generation: the proposal lattice (plan §2.2).

For each residual correspondence the proposer emits candidate rules as **notation strings** and
parses each through the existing ``load_rule`` — anything that fails to parse or validate is
silently dropped, so the generator can be aggressive and the parser stays the single source of
truth for what a legal rule is. The v1 language is a deliberate subset of Fortis notation:
literals, single-feature bracketed elements, one- or two-element contexts, and ``#``.

The lattice per correspondence (rewrite the derived phone toward the target):

1. **Unconditioned** — ``got → expected`` (substitutions only; an indel needs a context).
2. **Single predictor** — the top derived-side predictors, each as a left or right context:
   ``got → expected / p _``, ``got → expected / _ [+nasal]``, ``got → expected / _ #``.
3. **Predictor pairs** — a top-left and a top-right predictor together: ``got → expected / L _ R``.

Indels follow the same shape with a required context (plan §2.2 tier 5): a **deletion**
``got → ∅`` (delete a spurious derived phone) needs a context by policy — an unconditioned
deletion is too blunt to price fairly — and an **insertion** ``∅ → expected`` needs one by the
notation itself. Natural-class targets (tier 4) and self-conditioning arrive in M2/M4.

Everything is capped at ``contexts_per_confusion``; ``words = [...]`` restrictions are never
emitted (per-word suppletion is the human's tool, not the search's — plan §1.3).
"""
from __future__ import annotations

from dataclasses import dataclass

from src.fortis.application.segmentation import string_to_sequence
from src.fortis.induction.correspond import ContextPredictor, Correspondence
from src.fortis.induction.notation import render_feature_map
from src.fortis.loaders.rules import load_rule
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule
from src.fortis.result import Ok

# The null symbol the notation parser reads for insertion/deletion.
_NULL = "∅"


def _segments(phone: str, project: Project) -> bool:
    """Whether a phone literal segments under the project's letters (the null is always fine).

    A phone that does not segment as a lone literal cannot be a rule literal — the resolver
    would reject it — so a rewrite that needs it is not proposed.
    """
    if phone == _NULL:
        return True
    try:
        string_to_sequence(phone, project)
    except ValueError:
        return False
    return True


@dataclass(frozen=True)
class Candidate:
    """One proposed rule: its notation, the parsed rule(s), and where it came from.

    ``definition`` is the notation string; ``rules`` the parsed result of ``load_rule`` (a
    single rule for the v1 lattice). ``correspondence`` and ``predictors`` are the provenance —
    the residual it targets and the derived-side environment(s) it conditions on — carried into
    the report and the composed rule's description.
    """

    definition: str
    rules: list[Rule]
    correspondence: Correspondence
    predictors: tuple[ContextPredictor, ...]


def _context(predictor: ContextPredictor) -> str:
    """The ``/ …`` context fragment for one predictor (its element on the named side)."""
    return f"{predictor.element} _" if predictor.side == "left" else f"_ {predictor.element}"


def _pair_context(left: ContextPredictor, right: ContextPredictor) -> str:
    """The ``/ L _ R`` context fragment for a left/right predictor pair."""
    return f"{left.element} _ {right.element}"


def _rewrite(correspondence: Correspondence) -> tuple[str, str] | None:
    """The (target, result) notation for a correspondence, or ``None`` if it has no phone anchor.

    A substitution rewrites ``got → expected``; a deletion rewrites the spurious ``got → ∅``; an
    insertion rewrites ``∅ → expected``.
    """
    expected, got = correspondence.expected, correspondence.got
    if correspondence.kind == "substitution":
        return got, expected  # type: ignore[return-value]
    if correspondence.kind == "insertion":  # spurious derived phone → delete it
        return got, _NULL  # type: ignore[return-value]
    if correspondence.kind == "deletion":  # missing target phone → insert it
        return _NULL, expected  # type: ignore[return-value]
    return None


def propose(correspondence: Correspondence, project: Project) -> list[Candidate]:
    """Generate the candidate rules for one correspondence, parse-validated and capped.

    Emits the lattice above as notation strings, keeps each that ``load_rule`` accepts, dedupes
    by definition, and truncates to ``contexts_per_confusion``. Order is priority order —
    unconditioned first, then single predictors, then pairs — so the cap keeps the cheapest,
    most general forms.
    """
    rewrite = _rewrite(correspondence)
    if rewrite is None:
        return []
    target, result = rewrite
    if not _segments(target, project) or not _segments(result, project):
        return []  # an unsegmentable phone literal — the resolver would reject every candidate
    needs_context = correspondence.kind != "substitution"
    settings = project.settings.induction

    definitions: list[tuple[str, tuple[ContextPredictor, ...]]] = []
    if not needs_context:
        definitions.append((f"{target} → {result}", ()))

    predictors = correspondence.predictors
    lefts = [p for p in predictors if p.side == "left"]
    rights = [p for p in predictors if p.side == "right"]

    # Tier 2 — each predictor as a single-sided context, in phi order.
    for predictor in predictors:
        definitions.append((f"{target} → {result} / {_context(predictor)}", (predictor,)))

    # Tier 3 — a top-left with a top-right predictor (both consistent sides).
    for left in lefts[:3]:
        for right in rights[:3]:
            definitions.append(
                (f"{target} → {result} / {_pair_context(left, right)}", (left, right))
            )

    candidates: list[Candidate] = []
    seen: set[str] = set()
    for definition, used in definitions:
        if definition in seen:
            continue
        seen.add(definition)
        match load_rule("candidate", {"definition": definition, "time": 0}, project.features):
            case Ok(rules):
                candidates.append(
                    Candidate(
                        definition=definition, rules=rules,
                        correspondence=correspondence, predictors=used,
                    )
                )
            case _:  # unparseable / invalid — the parser is the gate, drop it silently
                pass
        if len(candidates) >= settings.contexts_per_confusion:
            break
    return candidates


def _shared_source(members: list[Correspondence]) -> list[tuple[str, object]]:
    """The feature/value pairs common to every member's derived phone — the natural class.

    A feature enters the source class only if every ``got`` phone in the group carries it with
    the *same* value, so the class matches exactly the phones that share the change.
    """
    maps = [dict(member.got_features) for member in members]
    if not maps or not all(maps):
        return []
    first = maps[0]
    return sorted(
        (feature, value)
        for feature, value in first.items()
        if all(other.get(feature) == value for other in maps[1:])
    )


def class_candidates(correspondences: list[Correspondence], project: Project) -> list[Candidate]:
    """Tier-4 natural-class candidates: fuse substitutions that share one structured delta.

    Correspondences that move the *same* features to the *same* values (``delta_key``) are
    grouped; a group of ≥2 proposes one class rule ``[shared source features] → [delta]`` — the
    natural-class generalization of its literal members. One class rule is cheaper in bits than
    its fragments, so MDL prefers the real sound law over its instances where it fits (plan
    §2.2 tier 4). The class rule is attached to its highest-count member for provenance.
    """
    groups: dict[tuple[tuple[str, object], ...], list[Correspondence]] = {}
    for correspondence in correspondences:
        if correspondence.kind != "substitution" or not correspondence.feature_delta:
            continue
        groups.setdefault(correspondence.delta_key, []).append(correspondence)

    candidates: list[Candidate] = []
    for delta, members in groups.items():
        if len(members) < 2:
            continue
        source = _shared_source(members)
        source_element = render_feature_map(source, project.features)
        result_element = render_feature_map(delta, project.features)
        if source_element is None or result_element is None:
            continue
        definition = f"{source_element} → {result_element}"
        match load_rule("candidate", {"definition": definition, "time": 0}, project.features):
            case Ok(rules):
                anchor = max(members, key=lambda m: m.count)
                candidates.append(
                    Candidate(
                        definition=definition, rules=rules,
                        correspondence=anchor, predictors=(),
                    )
                )
            case _:
                pass
    return candidates
