"""Diagnostics: what an authored bundle denotes against the project's own inventory.

These are statements about the feature *system*, independent of any derivation — the
consumer-layer tools behind the web app's Diagnostics pane (and a future ``--lint`` CLI).

The match-set query answers the question that trips up every hand-authored feature system:
*which segments does this bundle actually pick out?* It matches the bundle with the engine's
own matcher (:func:`pattern_matches`), so the answer is the engine's denotation — the surprise
that ``[+front]`` also catches every coronal is visible rather than latent.

The rule check is intent-free and needs no inventory or run: it flags any rule position whose
bundle can *never* match a segment — a feature required present while one of its geometry-parent
nodes is required absent (``[front, oral: none]``). Unlike a reach heuristic, every finding is a
real bug, so there are no thresholds and no false positives.
"""

from __future__ import annotations

from dataclasses import dataclass

from src.fortis.application.matching import _has_alpha, pattern_matches
from src.fortis.models.bundles import FeatureBundle, PatternBundle
from src.fortis.models.elements import Bound, BundleElem, Element, Group, Quantified
from src.fortis.models.features import FeatureInventory
from src.fortis.models.project import Project
from src.fortis.models.specs import PatternSpec
from src.fortis.models.values import AutosegBind, AutosegRecall
from src.fortis.parsing.bundles import parse_pattern_bundle
from src.fortis.result import Err, Ok, Result


@dataclass(frozen=True)
class MatchSet:
    """The segments a feature bundle matches, in inventory order, plus the inventory size."""

    matched: list[str]
    total: int


def _needs_rule_context(spec: PatternSpec) -> bool:
    """Whether *spec* is meaningless in a standalone query.

    A conditional (``<n: F>``), an agreement variable (``αF``), or a reference (``F: ~n``) each
    needs a rule's binding environment. With none, they don't error — they silently match
    all-or-nothing (an unbound α holds everywhere, a conditional never filters, a recall binds
    nothing), which misleads more than a clear rejection.
    """
    return (
        spec.condition_label is not None
        or _has_alpha(spec.value)
        or isinstance(spec.value, AutosegBind | AutosegRecall)
    )


def match_set(raw_bundle: str, project: Project) -> Result[MatchSet, str]:
    """The inventory segments a feature bundle matches — the engine's own denotation of it.

    Parses *raw_bundle* as a pattern bundle (brackets optional) and tests it against every
    letter in *project*. Returns an error string for empty input, a parse failure, or a spec
    that needs a rule context — each surfaced to the author verbatim.
    """
    raw = (raw_bundle or "").strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1].strip()
    if not raw:
        return Err("Enter a feature bundle, e.g. +front, +sonorant, -syllabic")
    match parse_pattern_bundle(raw, project.features):
        case Err(error):
            return Err("; ".join(error) if isinstance(error, list) else error)
        case Ok(pattern):
            offenders = [f for f, spec in pattern.items() if _needs_rule_context(spec)]
            if offenders:
                return Err(
                    "References (~n), agreement variables (α), and conditionals (<n: …>) only "
                    f"mean something inside a rule — remove: {', '.join(offenders)}"
                )
            matched = [
                symbol
                for symbol, letter in project.letters.items()
                if pattern_matches(pattern, letter.bundle, None)
            ]
            return Ok(MatchSet(matched=matched, total=len(project.letters)))


# --- Rule checks: unsatisfiable bundles -----------------------------------------------------


@dataclass(frozen=True)
class Unsatisfiable:
    """A rule position whose bundle can never match any segment — always a bug, not a heuristic."""

    rule: str  # the rule's display name (or id)
    time: int | None  # its chronology key, for ordering and display
    role: str  # where in the rule: "target", "left context", etc.
    label: str  # the offending bundle rendered back to notation
    reason: str  # why it can never match, in plain language


def _feature_token(feature: str, value: object, features: FeatureInventory) -> str:
    """One feature/value pair rendered back to notation (``+voice``, ``aperture: high``)."""
    if feature not in features or not isinstance(value, int) or isinstance(value, bool):
        return feature if value is not None else f"{feature}: none"
    kind = features[feature].kind
    if kind == "binary":
        return f"+{feature}" if value == 1 else f"-{feature}"
    if kind == "scalar":
        label = features[feature].values.get(value)
        return f"{feature}: {label}" if label is not None else feature
    return feature  # unary present


def _bundle_label(bundle: PatternBundle | FeatureBundle, features: FeatureInventory) -> str:
    """A bracketed rendering of a bundle's specs — for locating the position in the rule."""
    tokens = [
        _feature_token(f, getattr(spec, "value", None), features) for f, spec in bundle.items()
    ]
    return f"[{', '.join(tokens)}]"


def _bundle_positions(elements: tuple[Element, ...]) -> list[PatternBundle]:
    """The pattern-bundle positions in a target/context/exception.

    Unwraps the structural wrappers (group, binding, quantifier). Only a feature bundle can carry
    a geometry contradiction; letters, wildcards, disjunctions, and boundaries are skipped.
    """
    out: list[PatternBundle] = []
    for element in elements:
        match element:
            case BundleElem(bundle):
                out.append(bundle)
            case Group(inner):
                out.extend(_bundle_positions(inner))
            case Bound(_, inner):
                out.extend(_bundle_positions((inner,)))
            case Quantified(inner, _):
                out.extend(_bundle_positions((inner,)))
            case _:
                pass  # letter, wildcard, negation, disjunction, boundary — no bundle here
    return out


def _ancestor_nodes(feature: str, features: FeatureInventory) -> list[str]:
    """The chain of geometry-parent nodes above *feature* (``front`` → lingual, oral, root)."""
    chain: list[str] = []
    seen: set[str] = set()
    current = features[feature].parent if feature in features else None
    while current and current not in seen and current in features:
        seen.add(current)
        chain.append(current)
        current = features[current].parent
    return chain


def _contradiction(bundle: PatternBundle, features: FeatureInventory) -> str | None:
    """Why *bundle* can never match, or ``None`` if it is satisfiable.

    A bundle is unsatisfiable when it requires a feature **present** while one of that feature's
    ancestor nodes is required **absent** (``node: none``): the feature's geometry needs the node,
    so no segment can satisfy both. Conditional specs (``<n: …>``) don't filter and are ignored.
    """
    absent = {
        feature
        for feature, spec in bundle.items()
        if spec.value is None and not spec.negated and spec.condition_label is None
    }
    if not absent:
        return None
    for feature, spec in bundle.items():
        if spec.condition_label is not None:
            continue
        requires_present = spec.value is not None or spec.negated  # a value, `!none`, or `!val`
        if not requires_present:
            continue
        for ancestor in _ancestor_nodes(feature, features):
            if ancestor in absent:
                return (
                    f"{feature} is required present, but its parent node {ancestor} "
                    f"is absent (`{ancestor}: none`)"
                )
    return None


def unsatisfiable_rules(project: Project) -> list[Unsatisfiable]:
    """Rule positions whose bundle can never match any segment — a geometry contradiction.

    Intent-free and inventory-free: it needs no derivation and has no threshold, so every finding
    is a real bug (a feature required present under a node required absent). Checks each rule's
    target, contexts, and exceptions; returns findings in rule-chronology order.
    """
    features = project.features
    findings: list[Unsatisfiable] = []
    for rule in (r for rules_at_time in project.rules.values() for r in rules_at_time):
        name = rule.name or rule.id
        roles = (
            ("target", rule.sd.target),
            ("left context", rule.sd.left_context),
            ("right context", rule.sd.right_context),
            ("left exception", rule.sd.left_exception),
            ("right exception", rule.sd.right_exception),
        )
        for role, elements in roles:
            for bundle in _bundle_positions(elements):
                reason = _contradiction(bundle, features)
                if reason is not None:
                    findings.append(
                        Unsatisfiable(
                            rule=name, time=rule.time, role=role,
                            label=_bundle_label(bundle, features), reason=reason,
                        )
                    )
    findings.sort(key=lambda f: f.time if f.time is not None else 1 << 30)
    return findings
