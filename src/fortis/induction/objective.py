"""The objective function: a two-part minimum-description-length loss, in bits.

The loss of a cascade ``R`` over a lexicon ``W`` is ``L(R) = rule_bits(R) + fit_bits(R)``,
both sides measured in bits so the fit/cost exchange rate is fixed by the encoding, not a
per-dataset ``λ`` knob. A rule is worth adding exactly when writing it costs fewer bits than
the corrections it makes unnecessary.

- **Fit bits** (:func:`residual_bits`) price the corrections that turn a *derived* form into
  its *attested* one, read off the deterministic ``accuracy.align`` op list: a substitution
  costs a site tag plus the feature delta between the two phones, a deletion costs a site tag
  plus spelling the missing phone, a spurious insertion costs only a site tag. Encoding
  substitutions as feature deltas is deliberate — it makes the fit term a blend of phone-edit
  count and feature distance, so a rule that moves ``ɛ→e`` toward a target ``i`` lowers the
  loss even though the phone distance is unchanged.
- **Rule bits** (:func:`rule_bits`) price the structural description element by element:
  literals by ``log2(|letters|)``, feature bundles by a per-feature-pair cost, boundaries for
  free. Longer contexts and fatter bundles cost linearly more — the generalization pressure
  that makes a real sound law beat its over-specific fragments.

Every constant scales off the project (``|F|``, ``V̄``, ``L̄``, ``|letters|``) except the two
structural constants ``B_RULE`` and ``B_TAG``, which are part of the code's definition of the
objective — moving them is a research act, not project tuning (see the plan §1.5).
"""
from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass

from src.fortis.analysis.accuracy import (
    AccuracyReport,
    DistanceToTarget,
    accuracy_by_stage,
    align,
    feature_diff,
    form_phones,
    segment_form,
    specified_features,
    try_segment,
)
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation
from src.fortis.models.elements import (
    Bound,
    BundleElem,
    Disjunction,
    Element,
    FloatingAutoseg,
    Group,
    LetterBundle,
    LetterRef,
    ModifiedLetter,
    Negated,
    Quantified,
    RecallRef,
    ResultElem,
)
from src.fortis.models.project import Project
from src.fortis.models.rules import Rule

# --- Structural constants (part of the objective, NOT project settings) -----------------
#
# These set the fixed structural overhead of a rule and of naming an element kind. They are
# principled but not sacred: the synthetic benchmark (§6) is the calibration instrument — if
# the inducer under- or over-accepts on clean self-generated data, these are what move, never
# a per-dataset knob.
B_RULE = 10.0  # header: a rule's time slot, application mode, and arrow
B_TAG = 3.0  # log2(#element kinds): what kind of element follows


@dataclass(frozen=True)
class BitsModel:
    """The per-project bit costs, computed once from the project's inventories.

    ``b_site`` prices an edit *site* (op kind + position); ``b_feat`` prices naming one
    feature and one value; ``letter_bits`` prices one letter literal; ``mean_features`` is the
    average specified-feature count of a segment (the fallback when a phone will not segment).
    """

    b_site: float
    b_feat: float
    letter_bits: float
    mean_features: float


def _mean_attested_length(project: Project) -> float:
    """Mean phone length ``L̄`` across every attested form (finals and all stages).

    Falls back to a length of 1 when the lexicon carries no attested forms, so the site cost
    stays finite on a target-less project.
    """
    lengths: list[int] = []
    for word in project.words.values():
        strings = ([word.final] if word.final is not None else []) + list(word.stages.values())
        for string in strings:
            form = try_segment(string, project)
            if form is not None:  # skip an attested form the inventory cannot segment
                lengths.append(len(form_phones(form, project)))
    return sum(lengths) / len(lengths) if lengths else 1.0


def _mean_feature_count(project: Project) -> float:
    """Mean specified-feature count ``F̄`` across the letter inventory's segments.

    The average size of a real segment — used to spell a phone that will not segment, so
    unsegmentable notation degrades the bit estimate rather than crashing it.
    """
    counts = [len(specified_features(letter.bundle)) for letter in project.letters.values()]
    return sum(counts) / len(counts) if counts else 1.0


def bits_model(project: Project) -> BitsModel:
    """Compute the project's bit costs from its feature, value, length, and letter counts."""
    num_features = max(len(project.features), 1)
    mean_values = _mean_values_per_feature(project)
    num_letters = max(len(project.letters), 1)
    b_site = math.log2(3) + math.log2(_mean_attested_length(project) + 1)
    b_feat = math.log2(num_features) + math.log2(max(mean_values, 1.0))
    return BitsModel(
        b_site=b_site,
        b_feat=b_feat,
        letter_bits=math.log2(num_letters),
        mean_features=_mean_feature_count(project),
    )


def _mean_values_per_feature(project: Project) -> float:
    """Mean ``V̄`` — number of legal values per feature (a unary feature counts as 1)."""
    counts = [max(len(feature.values), 1) for feature in project.features.values()]
    return sum(counts) / len(counts) if counts else 1.0


# --- Fit bits (residual encoding) -------------------------------------------------------

# A phone → its featurised bundle (or None if it will not segment), memoised per call site:
# the same handful of phones recur millions of times across a lexicon.
PhoneCache = dict[str, FeatureBundle | None]


def _phone_bundle(phone: str, project: Project, cache: PhoneCache) -> FeatureBundle | None:
    """The single feature bundle a phone segments to, or ``None`` if it will not segment."""
    if phone not in cache:
        bundles = segment_form(phone, project)
        cache[phone] = bundles[0] if bundles and len(bundles) == 1 else None
    return cache[phone]


def _sub_bits(
    target: str, derived: str, project: Project, model: BitsModel, cache: PhoneCache
) -> float:
    """Bits to encode a substitution ``derived→target``: site + the feature delta between them."""
    a = _phone_bundle(target, project, cache)
    b = _phone_bundle(derived, project, cache)
    delta = feature_diff(a, b) if a is not None and b is not None else model.mean_features
    return model.b_site + model.b_feat * delta


def _spell_bits(phone: str, project: Project, model: BitsModel, cache: PhoneCache) -> float:
    """Bits to encode a deletion: site + spelling the missing target phone in full."""
    bundle = _phone_bundle(phone, project, cache)
    count = len(specified_features(bundle)) if bundle is not None else model.mean_features
    return model.b_site + model.b_feat * count


def residual_bits(
    dtt: DistanceToTarget,
    project: Project,
    model: BitsModel | None = None,
    cache: PhoneCache | None = None,
) -> float:
    """Bits to encode the corrections turning ``dtt.derived`` into ``dtt.target``.

    Reads the same deterministic target→derived alignment ``diagnosis`` uses. An exact word
    costs 0. Pass a shared *model* and *cache* when scoring many distances (they are rebuilt on
    every call otherwise); a one-off caller may omit both.
    """
    if model is None:
        model = bits_model(project)
    if cache is None:
        cache = {}
    total = 0.0
    for op in align(dtt.target_phones, dtt.derived_phones):
        if op.kind == "match":
            continue
        if op.kind == "sub":
            assert op.target is not None and op.derived is not None
            total += _sub_bits(op.target, op.derived, project, model, cache)
        elif op.kind == "delete":  # target phone the derivation never produced
            assert op.target is not None
            total += _spell_bits(op.target, project, model, cache)
        else:  # insert — a spurious derived phone, site only
            total += model.b_site
    return total


# --- Rule bits (structural description encoding) ----------------------------------------


def _content_bits(element: Element, model: BitsModel) -> float:
    """The content cost of one element (its own kind tag is charged by :func:`element_bits`)."""
    match element:
        case LetterRef() | LetterBundle():
            return model.letter_bits
        case ModifiedLetter(_symbol, delta):
            return model.letter_bits + model.b_feat * len(delta)
        case BundleElem(bundle):
            return model.b_feat * len(bundle)
        case ResultElem(bundle):
            return model.b_feat * len(bundle)
        case FloatingAutoseg(pattern):
            return model.b_feat * len(pattern)
        case Group(inner):
            return sum(element_bits(e, model) for e in inner)
        case Disjunction(branches):
            return sum(element_bits(e, model) for branch in branches for e in branch)
        case Negated(inner):
            # A modifier adds no content beyond its inner element; its own tag is enough.
            return _content_bits(inner, model)
        case Quantified(inner, _quant):
            return _content_bits(inner, model)
        case Bound(_ref, inner):
            return _content_bits(inner, model)
        case RecallRef():
            return 0.0
        case _:
            # Boundaries (#, $, morpheme -), the null segment, and the wildcard: free content,
            # their presence is covered by the element tag.
            return 0.0


def element_bits(element: Element, model: BitsModel) -> float:
    """Bits to encode one structural-description element: its kind tag plus its content."""
    return B_TAG + _content_bits(element, model)


def rule_bits(rule: Rule, project: Project, model: BitsModel | None = None) -> float:
    """Bits to encode a rule's structural description: header + every element, tag and content.

    Prices the *unresolved* description (as loaded), so a letter run counts as its literal
    element, not the segments it later expands to.
    """
    if model is None:
        model = bits_model(project)
    sd = rule.sd
    sides = (
        sd.target,
        sd.result,
        sd.left_context,
        sd.right_context,
        sd.left_exception,
        sd.right_exception,
    )
    return B_RULE + sum(element_bits(e, model) for side in sides for e in side)


def cascade_rule_bits(project: Project, model: BitsModel | None = None) -> float:
    """Total rule bits over every rule in the project's inventory."""
    if model is None:
        model = bits_model(project)
    return sum(
        rule_bits(rule, project, model)
        for rules in project.rules.values()
        for rule in rules
    )


# --- The whole-cascade snapshot ---------------------------------------------------------


@dataclass(frozen=True)
class CascadeScore:
    """One snapshot of a cascade's loss: the fit and rule bits, plus headline accuracy.

    ``fit_bits`` sums the residual bits over every attested checkpoint (each ``Word.stages``
    form and the ``final``), frequency-weighted, with the final checkpoint scaled by the
    project's ``final_weight``. ``rule_bits`` is the total structural cost of the cascade.
    ``exact``/``assessed``/``mean_distance`` describe the *final* checkpoint alone — the
    human-readable accuracy comparable to the grader's headline.
    """

    fit_bits: float
    rule_bits: float
    exact: int
    assessed: int
    mean_distance: float

    @property
    def total(self) -> float:
        """The full MDL loss ``L = fit_bits + rule_bits``."""
        return self.fit_bits + self.rule_bits

    @property
    def accuracy(self) -> float:
        """Final-checkpoint exact-match fraction (0.0 if nothing assessed)."""
        return self.exact / self.assessed if self.assessed else 0.0


def fit_bits_of_report(
    report: AccuracyReport,
    project: Project,
    model: BitsModel,
    cache: PhoneCache,
    weight: float = 1.0,
) -> float:
    """Frequency-weighted residual bits summed over one checkpoint's distances, times *weight*."""
    return weight * sum(
        dtt.frequency * residual_bits(dtt, project, model, cache)
        for dtt in report.distances
    )


def cascade_score(derivations: Sequence[Derivation], project: Project) -> CascadeScore:
    """Score a whole derived cascade: fit bits over every checkpoint, plus the rule bits.

    ``fit_bits`` is the multi-checkpoint objective of §1 — every attested ``Word.stages`` form
    (assessed against the derived snapshot at its rule-time) and the ``final`` (against the
    surface), frequency-weighted, the final scaled by the project's ``final_weight``. The
    headline accuracy fields read the final checkpoint. The rule bits come straight from the
    project's inventory, so this is ``L(R)`` for the project *as derived*.
    """
    model = bits_model(project)
    cache: PhoneCache = {}
    final_weight = project.settings.induction.final_weight
    stages = accuracy_by_stage(derivations, project)
    fit = 0.0
    final_report: AccuracyReport | None = None
    for stage in stages:
        weight = final_weight if stage.time is None else 1.0
        fit += fit_bits_of_report(stage.report, project, model, cache, weight)
        if stage.time is None:
            final_report = stage.report
    assert final_report is not None  # accuracy_by_stage always appends the final step
    return CascadeScore(
        fit_bits=fit,
        rule_bits=cascade_rule_bits(project, model),
        exact=final_report.exact,
        assessed=final_report.assessed,
        mean_distance=final_report.mean_distance,
    )
