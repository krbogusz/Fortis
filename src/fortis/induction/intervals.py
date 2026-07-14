"""Stage-aware decomposition: interval bucketing, mini-projects, and the synthetic benchmark.

The attested stage times partition the cascade into intervals ``(input → t₁), (t₁ → t₂), …,
(tₙ → final)``. Per interval the training set is the words attesting **both** endpoints, and
the interval's input is the *attested* earlier form, not a derived one — teacher forcing. This
buys three things (plan §3.1): intervals are fully independent (inducible in parallel, no
upstream contamination), the ordering search shrinks from one global problem to n+1 local
ones, and an attested stage can expose an environment the final form has since erased.

An interval problem is literally a :class:`Project`: the words become ``{source_form:
Word(ipa=source, final=target, frequency=…)}``, the rules start empty, and everything else
(features, letters, tiers, settings, syllabification) is shared with the parent — so every
downstream tool (``derive_all``, ``measure_accuracy``, ``confusions``, ``blame``) runs on it
unchanged.

The synthetic generator (:func:`synthetic_project`) derives the real cascade and snapshots
``form_at_time`` at each attested stage, emitting a machine-generated, perfectly self-consistent
lexicon — the learnability floor of §6.1: on it the hand cascade must score ``fit_bits`` 0.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

from src.fortis.application.deriving import derive_all, form_at_time
from src.fortis.application.rendering import render_syllabified
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.derivation import Derivation
from src.fortis.models.inventories import Word, WordInventory
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory

# Sentinels for the two open interval endpoints: the proto input (earliest interval's start)
# and the final surface (latest interval's end). An interior boundary is a plain stage time.
INPUT = None
FINAL = None


@dataclass(frozen=True)
class Interval:
    """One time interval of the cascade, as a self-contained mini-:class:`Project`.

    ``start`` is the earlier endpoint's stage time, or ``None`` for the proto input; ``end`` is
    the later endpoint's stage time, or ``None`` for the final surface. ``project`` is the
    mini-project (words = attested source → attested target, rules empty). ``excluded`` names
    the source forms dropped because they would not segment under the project's letters — never
    silently lost, always counted for the report. ``collisions`` counts distinct parent words
    whose source form duplicated another's (last wins in the mini-lexicon).
    """

    start: int | None
    end: int | None
    project: Project
    excluded: tuple[str, ...] = ()
    collisions: int = 0

    @property
    def label(self) -> str:
        """A human-readable interval name, e.g. ``input→-100`` or ``1400→final``."""
        start = "input" if self.start is None else str(self.start)
        end = "final" if self.end is None else str(self.end)
        return f"{start}→{end}"

    @property
    def size(self) -> int:
        """Number of training words in the mini-lexicon."""
        return len(self.project.words)


def stage_times(project: Project) -> list[int]:
    """The sorted distinct attested stage times across the lexicon."""
    return sorted({time for word in project.words.values() for time in word.stages})


def _boundaries(project: Project) -> list[tuple[int | None, int | None]]:
    """The (start, end) endpoint pairs partitioning the cascade at the attested stage times."""
    times = stage_times(project)
    checkpoints: list[int | None] = [INPUT, *times, FINAL]
    # Consecutive pairs; the trailing input/final are unpaired by design (unequal lengths).
    return list(zip(checkpoints, checkpoints[1:], strict=False))


def _source_form(word: Word, start: int | None) -> str | None:
    """The attested form at an interval's earlier endpoint: the input, or a stage form."""
    return word.ipa if start is INPUT else word.stages.get(start)  # type: ignore[arg-type]


def _target_form(word: Word, end: int | None) -> str | None:
    """The attested form at an interval's later endpoint: a stage form, or the final."""
    return word.final if end is FINAL else word.stages.get(end)  # type: ignore[arg-type]


def _segments(form: str, project: Project) -> bool:
    """Whether *form* segments under the project's letters/diacritics (the interval gate)."""
    try:
        string_to_sequence(form, project)
    except ValueError:
        return False
    return True


def build_interval(project: Project, start: int | None, end: int | None) -> Interval:
    """Build one interval's mini-project from the words attesting both its endpoints.

    A word enters only if it carries a form at *both* endpoints and its source form segments
    under the project's letters. The source form keys the mini-lexicon (as the engine keys a
    ``Word`` by its ipa); on the rare collision the later word wins and the count is recorded.
    """
    mini: dict[str, Word] = {}
    excluded: list[str] = []
    collisions = 0
    for word in project.words.values():
        source = _source_form(word, start)
        target = _target_form(word, end)
        if source is None or target is None:
            continue
        if not _segments(source, project):
            excluded.append(source)
            continue
        if source in mini:
            collisions += 1
        mini[source] = Word.from_series(
            id=source, seed=source, gloss=word.gloss, final=target, frequency=word.frequency
        )
    mini_project = replace(project, words=WordInventory(mini), rules=RuleInventory())
    return Interval(
        start=start,
        end=end,
        project=mini_project,
        excluded=tuple(excluded),
        collisions=collisions,
    )


def build_intervals(project: Project) -> list[Interval]:
    """Partition the cascade into its intervals, one mini-project each (plan §3.1–3.2).

    With no attested stages this yields a single ``input → final`` interval — the graceful
    degradation of §3.5, where Phase A and B collapse into one loop.
    """
    return [build_interval(project, start, end) for start, end in _boundaries(project)]


# --- Synthetic benchmark (the learnability floor, §6.1) ---------------------------------


def _render_at(derivation: Derivation, time: int | None, project: Project) -> str:
    """Render the derived snapshot at *time* (a stage time, or the final surface)."""
    if time is None:
        form, boundaries = derivation.surface, derivation.surface_boundaries
    else:
        form, boundaries = form_at_time(derivation, time)
    return render_syllabified(lower_tiers(form), boundaries, project)


def synthetic_words(project: Project) -> WordInventory:
    """A machine-generated lexicon: the same inputs, with derived stages/finals substituted.

    Derives the real cascade and, per word, snapshots ``form_at_time`` at each stage time the
    word originally attested (keeping the supervision density identical) plus the final
    surface. The result is perfectly self-consistent — the hand cascade regenerates it with
    zero residual — so it isolates the inducer's own learnability from notation noise.
    """
    derivations = derive_all(project)
    words: dict[str, Word] = {}
    for derivation, (key, word) in zip(derivations, project.words.items(), strict=True):
        stages = {
            time: _render_at(derivation, time, project) for time in sorted(word.stages)
        }
        words[key] = Word.from_series(
            id=word.id,
            seed=word.ipa,
            seed_time=word.seed_time,
            gloss=word.gloss,
            final=_render_at(derivation, None, project),
            stages=stages,
            frequency=word.frequency,
        )
    return WordInventory(words)


def synthetic_project(project: Project) -> Project:
    """A copy of *project* with its lexicon replaced by the synthetic one (rules unchanged).

    On this project the hand cascade scores ``fit_bits`` ≈ 0 (the targets are its own output),
    the exact benchmark the M0 scoreboard checks and every later milestone is assessed against.
    """
    return replace(project, words=synthetic_words(project))
