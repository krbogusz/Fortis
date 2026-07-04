"""Grade derived surface forms against the lexicon's target annotations.

The engine derives a surface form from each word's IPA; a word may also carry an
attested target in ``Word.final`` (a *target* annotation, native to ``words.toml``).
This module measures the distance between the two — per word and in aggregate —
so a rule set's accuracy can be tracked as it is developed.

Two distances are reported per word:

- **Phone distance** — the Damerau–Levenshtein distance over *phones*, where a
  phone is a base segment plus the marks that attach to it (nasalization ``ɑ̃``,
  dental ``t̪``, length ``ː`` all count as one phone, not several codepoints).
  This is the headline metric: distance 0 is an exact match.
- **Feature distance** — a *feature-weighted* edit distance over the same forms
  re-segmented into feature bundles: substituting one segment for another costs
  the number of features on which they disagree, so ``ɑ̃`` is one edit from ``ɑ``
  (nasal) but eleven from ``t``. This is the finer diagnostic — it distinguishes
  a near-miss from a gross one, which a phone distance flattens to 1 either way.

Both distances count a swap of two adjacent segments (a metathesis) as one edit,
not two substitutions — the Damerau–Levenshtein extension.

Both operate on the *rendered* forms (derived surface and target string), so a
feature distance of 0 coincides exactly with a phone distance of 0. Syllable
dots are structural, not segmental, and are dropped before comparison — the
engine renders them (``a.vɑ̃``) but the target forms do not (``avɑ̃``).

Only ``Word.final`` is graded here. Per-stage grading against ``Word.stages``
needs the derived form *at each stage time* (a different intermediate form per
stage), which is a separate tool.
"""
from __future__ import annotations

import unicodedata
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from src.fortis.application.deriving import form_at_time
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project

# Unicode categories whose characters attach to the preceding base to form one
# phone: nonspacing/spacing combining marks (Mn/Mc) and modifier letters/symbols
# (Lm/Sk — length ``ː``, palatalization ``ʲ``, superscripts, tone letters).
_ATTACHING = frozenset({"Mn", "Mc", "Lm", "Sk"})


def split_phones(form: str) -> list[str]:
    """Split a rendered form into phones for edit-distance comparison.

    A phone is a base character plus any following attaching marks. Syllable
    dots and whitespace are dropped (structural, not segmental), so ``a.vɑ̃`` and
    ``avɑ̃`` both split to ``['a', 'v', 'ɑ̃']``.
    """
    phones: list[str] = []
    for char in form:
        if char == "." or char.isspace():
            continue
        if phones and unicodedata.category(char) in _ATTACHING:
            phones[-1] += char
        else:
            phones.append(char)
    return phones


def edit_distance(a: Sequence[str], b: Sequence[str], transposition_cost: int = 1) -> int:
    """The Damerau–Levenshtein distance between two phone sequences (unit costs).

    Insert/delete/substitute each cost 1; swapping two *adjacent* phones costs
    ``transposition_cost`` (default 1), so a metathesis reads as one edit rather
    than two substitutions. This is the restricted (optimal string alignment)
    variant: a phone participates in at most one transposition.
    """
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i
    for j in range(1, m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(
                d[i - 1][j] + 1,  # deletion
                d[i][j - 1] + 1,  # insertion
                d[i - 1][j - 1] + (a[i - 1] != b[j - 1]),  # match/substitution
            )
            # Fires on any exact adjacent reversal in the optimal alignment — not
            # necessarily a linguistic metathesis; a future op-trace must not label it one.
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + transposition_cost)  # transposition
    return d[n][m]


def compare(derived: str, target: str) -> int:
    """The phone edit distance between a derived form and a target form."""
    return edit_distance(split_phones(derived), split_phones(target))


# Sentinel for a feature absent from a bundle, distinct from any real value so
# that present-vs-absent reads as a difference.
_ABSENT = object()


def _specified(bundle: FeatureBundle) -> dict[str, object]:
    """The bundle's features that carry a value, as ``{feature: value}``."""
    return {feature: spec.value for feature, spec in bundle.items() if spec.value is not None}


def feature_diff(a: FeatureBundle, b: FeatureBundle) -> int:
    """Number of features on which two segments disagree.

    A feature present on one segment and absent on the other counts as one
    difference, as does a feature present on both with different values. So
    ``ɑ̃`` and ``ɑ`` differ by one (nasal), ``ɑ̃`` and ``t`` by many.
    """
    left, right = _specified(a), _specified(b)
    return sum(left.get(f, _ABSENT) != right.get(f, _ABSENT) for f in left.keys() | right.keys())


def feature_edit_distance(
    a: Sequence[FeatureBundle], b: Sequence[FeatureBundle], transposition_cost: int = 1
) -> int:
    """Feature-weighted Damerau–Levenshtein over two segment sequences.

    Substituting one segment for another costs :func:`feature_diff`; inserting or
    deleting a segment costs its own feature count — its distance from nothing,
    ``feature_diff(x, ∅)``. Because a segment shares some features with any other
    (both are ``[consonantal …]``), a substitution never costs more than the
    delete-plus-insert alternative, so segments align by feature similarity and
    an indel falls out only on a genuine length mismatch.

    Swapping two *adjacent* segments costs ``transposition_cost`` (default 1) —
    but only when the swapped pair is featurally identical (each
    :func:`feature_diff` is 0), i.e. a true metathesis that reorders segments
    without changing any features. That one reordering event would otherwise be
    charged as two substitutions (up to ``2 × feature_diff``). This is the
    restricted (optimal string alignment) variant.
    """
    n, m = len(a), len(b)
    a_sizes = [len(_specified(bundle)) for bundle in a]
    b_sizes = [len(_specified(bundle)) for bundle in b]
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = d[i - 1][0] + a_sizes[i - 1]
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + b_sizes[j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(
                d[i - 1][j] + a_sizes[i - 1],  # delete a[i-1]
                d[i][j - 1] + b_sizes[j - 1],  # insert b[j-1]
                d[i - 1][j - 1] + feature_diff(a[i - 1], b[j - 1]),  # substitute
            )
            # Fires on any exact adjacent reversal in the optimal alignment — not
            # necessarily a linguistic metathesis; a future op-trace must not label it one.
            if (
                i > 1
                and j > 1
                and feature_diff(a[i - 1], b[j - 2]) == 0
                and feature_diff(a[i - 2], b[j - 1]) == 0
            ):
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + transposition_cost)  # transposition
    return d[n][m]


def _segment(form: str, project: Project) -> list[FeatureBundle] | None:
    """Segment a rendered form into feature bundles for the feature comparison.

    Syllable dots and whitespace (structural, not segmental) are stripped first,
    matching :func:`split_phones`. Returns ``None`` if the form uses a symbol the
    project cannot segment.
    """
    cleaned = "".join(form.replace(".", "").split())
    try:
        return lower_tiers(string_to_sequence(cleaned, project))
    except ValueError:
        return None


def feature_compare(derived: str, target: str, project: Project) -> int | None:
    """The feature edit distance between a derived and a target form.

    Both strings go through the same segmentation, so this is 0 exactly when the
    phone distance is 0. Returns ``None`` if either form cannot be segmented.
    """
    a, b = _segment(derived, project), _segment(target, project)
    if a is None or b is None:
        return None
    return feature_edit_distance(a, b)


@dataclass(frozen=True)
class Grade:
    """One word graded: its derived surface against the attested target form.

    ``derived`` and ``target`` are kept as rendered (dots and all) for display.
    ``distance`` is the phone edit distance (the headline). ``feature_distance``
    is the finer feature-weighted distance, or ``None`` when a form could not be
    segmented into features.
    """

    gloss: str
    ipa: str
    derived: str
    target: str
    distance: int
    feature_distance: int | None = None

    @property
    def exact(self) -> bool:
        """Whether the derived form matches the target exactly (distance 0)."""
        return self.distance == 0


@dataclass(frozen=True)
class GradeReport:
    """A set of per-word grades with the aggregate accuracy statistics.

    ``graded`` is the denominator throughout: words that carry a target ``final``.
    ``skipped`` counts words with no target to compare against.
    """

    grades: tuple[Grade, ...]
    skipped: int = 0

    @property
    def graded(self) -> int:
        """Number of words graded (those with a target ``final``)."""
        return len(self.grades)

    @property
    def exact(self) -> int:
        """Number of words derived exactly (distance 0)."""
        return sum(grade.exact for grade in self.grades)

    @property
    def within_one(self) -> int:
        """Number of words within one phone of the target (distance ≤ 1)."""
        return sum(grade.distance <= 1 for grade in self.grades)

    @property
    def total_distance(self) -> int:
        """Summed phone edit distance across all graded words."""
        return sum(grade.distance for grade in self.grades)

    @property
    def accuracy(self) -> float:
        """Fraction derived exactly, ``exact / graded`` (0.0 if none graded)."""
        return self.exact / self.graded if self.grades else 0.0

    @property
    def mean_distance(self) -> float:
        """Mean phone edit distance per graded word (0.0 if none graded)."""
        return self.total_distance / self.graded if self.grades else 0.0

    @property
    def feature_graded(self) -> int:
        """Number of graded words that also have a feature distance."""
        return sum(grade.feature_distance is not None for grade in self.grades)

    @property
    def unsegmentable(self) -> int:
        """Graded words whose forms could not be segmented (no feature distance)."""
        return sum(grade.feature_distance is None for grade in self.grades)

    @property
    def total_feature_distance(self) -> int:
        """Summed feature edit distance across words that have one."""
        return sum(g.feature_distance for g in self.grades if g.feature_distance is not None)

    @property
    def mean_feature_distance(self) -> float:
        """Mean feature edit distance per word that has one (0.0 if none)."""
        return self.total_feature_distance / self.feature_graded if self.feature_graded else 0.0


def grade_derivation(derivation: Derivation, project: Project) -> Grade | None:
    """Grade one derivation against its word's target ``final``.

    Returns ``None`` when the word carries no target form to compare against.
    """
    target = derivation.word.final
    if target is None:
        return None
    derived = render_syllabified(
        lower_tiers(derivation.surface), derivation.surface_boundaries, project
    )
    return _grade(derivation.word.gloss, derivation.word.ipa, derived, target, project)


def _grade(gloss: str, ipa: str, derived: str, target: str, project: Project) -> Grade:
    """Build a :class:`Grade` from a rendered derived form and a target form."""
    return Grade(
        gloss=gloss,
        ipa=ipa,
        derived=derived,
        target=target,
        distance=compare(derived, target),
        feature_distance=feature_compare(derived, target, project),
    )


def grade(derivations: Iterable[Derivation], project: Project) -> GradeReport:
    """Grade every derivation that has a target ``final``, in input order."""
    grades: list[Grade] = []
    skipped = 0
    for derivation in derivations:
        result = grade_derivation(derivation, project)
        if result is None:
            skipped += 1
        else:
            grades.append(result)
    return GradeReport(grades=tuple(grades), skipped=skipped)


@dataclass(frozen=True)
class StageGrades:
    """A :class:`GradeReport` for one grading step — an intermediate stage or the final.

    ``time`` is the stage time (``None`` for the final surface). ``label`` names
    the step in a report (the time as a string, or ``"final"``).
    """

    label: str
    time: int | None
    report: GradeReport


def grade_stages(derivations: Iterable[Derivation], project: Project) -> list[StageGrades]:
    """Grade each attested stage form, then the final, across the lexicon.

    For every stage time present in any word's ``Word.stages``, the derived
    snapshot *as of that rule-time* (see :func:`form_at_time`) is graded against
    the attested stage form — over just the words that carry a form for that
    stage. A trailing ``final`` step grades the surface against ``Word.final``.

    Note that a stage's derived form is taken at the matching *rule-time*; this is
    only meaningful if the rule times are calibrated to whatever timescale the
    attested stages use. The ``final`` step does not depend on that alignment.
    """
    derivations = list(derivations)
    stage_times = sorted({time for d in derivations for time in d.word.stages})
    stages: list[StageGrades] = []
    for time in stage_times:
        grades: list[Grade] = []
        for derivation in derivations:
            target = derivation.word.stages.get(time)
            if target is None:
                continue
            form, boundaries = form_at_time(derivation, time)
            derived = render_syllabified(lower_tiers(form), boundaries, project)
            grades.append(_grade(derivation.word.gloss, derivation.word.ipa, derived, target, project))
        stages.append(StageGrades(str(time), time, GradeReport(tuple(grades))))
    stages.append(StageGrades("final", None, grade(derivations, project)))
    return stages
