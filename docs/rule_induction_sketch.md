# Idea sketch: automated rule finding (supervised rule induction)

*A design sketch for discussion, and a request. Deliberately incomplete — the ask at the
end is for a full implementation document.*

## Context (for a reader who doesn't know the codebase)

**Fortis** is a general phonological derivation engine. Its normal job is **forward**:
given an input form and an *ordered, time-keyed cascade of context-sensitive sound-change
rules*, it derives the surface form step by step. Around that it already has an analysis
layer:

- **accuracy** (`analysis/accuracy.py`) — phone- and feature-level edit distance of a derived
  form against an attested target, per word and in aggregate.
- **diagnosis** (`analysis/diagnosis.py`) — a phone **confusion matrix** (which target phone
  came out as which) plus a **context autopsy** that finds, for the most-wrong phones, the
  environments most associated with the error (by phi coefficient).
- **blame** (`analysis/blame.py`) — attributes each wrong output to the specific rule (and
  position) that produced the wrong phone.
- **what-if** (`--try` on the accuracy CLI) — derive + measure a *candidate* rule against the
  whole lexicon and report the effect.

Inputs live in `words.toml`: each word carries its input IPA, an attested `final` target,
and optionally **intermediate attested `stages`** keyed by time (e.g. the Latin→French
project attests forms at times −100, 750, 1000, 1200, 1400). Fortis can already snapshot a
derivation at any time (`form_at_time`) and measure against a stage.

## The problem

Given a `words.toml` with **input proto-forms and attested targets** (final, and ideally
intermediate stages), **automatically find the rule cascade** that derives the targets from
the inputs. The ancestor and the outputs are fixed; only the *rules* are unknown. (This is
the supervised sub-problem of full reconstruction — ancestor given — and the right thing to
build first.)

## The reframing: gradient *boosting*, not gradient descent

Rules are discrete symbolic objects, so there is no continuous parameter vector to
differentiate a loss against — literal gradient descent doesn't apply. But the intuition of
iterative loss reduction does, in the form built for discrete weak learners:

**Stagewise additive modeling.** Start from the identity map (surface = input), compute the
residual error, then repeatedly **fit one new rule to the current residual** and append it
to the cascade — gradient boosting with sound-change rules as the weak learners. The cascade
is the ensemble; the "pseudo-residual" a new rule targets is the systematic error still
present.

This works because Fortis already computes every term of the boosting loop:

| boosting concept | existing Fortis machinery |
|---|---|
| loss `L(cascade)` | accuracy — total phone + feature edit distance over the lexicon |
| pseudo-residual ("which way is down") | diagnosis — the most systematic remaining error **and its conditioning environment** → the next rule to fit |
| which existing learner now hurts | blame — residual error attributed to a specific rule/position |
| line search (evaluate a candidate step) | what-if / `--try` — derive + measure a candidate rule, report the loss delta |
| cheap repeated evaluation | identity caches + parallel derivation |

So the loss, a genuine **gradient surrogate**, and the step evaluator all exist. The missing
piece is the outer search loop that *proposes* candidate rules and accepts the best.

## Using the intermediate attested stages (central to this idea)

The intermediate `stages` are not a nicety — they are the lever that makes the hard parts
tractable, and the inducer should be built around them from the start:

1. **Dense supervision.** Instead of one signal (input → final), each cognate contributes a
   *chain* of checkpoints (input → stage₁ → stage₂ → … → final). The loss becomes a sum of
   per-stage misfits, so a wrong rule is caught at the first stage it breaks rather than only
   at the end.
2. **Chronology localization — this tames the ordering problem.** Rule *order* (feeding/
   bleeding) is the combinatorial wall in cascade induction. But a rule whose effect first
   appears between stage *k* and stage *k+1* **belongs to that time interval**. The attested
   stages partition the cascade into time buckets, so instead of one global search over
   ordered rules you get several **smaller, independently-ordered sub-searches** — fit the
   rules for input→stage₁, then stage₁→stage₂, and so on — then compose. Fortis rules are
   already time-keyed, so each induced rule drops straight into its interval's slot.
3. **Opacity relief.** An intermediate stage can *expose* a conditioning environment that the
   final form has since erased — so opaque changes (the second wall below) that are invisible
   from the final form alone often become visible at an earlier stage.
4. **Per-interval decomposition = smaller weak learners.** Fitting proto→stage₁ is a far
   smaller, less-interacting problem than fitting proto→final; boosting within one short
   interval converges faster and to simpler rules.

Fortis already supports all of this: `form_at_time` snapshots the derivation at any stage,
accuracy measures per stage, `diagnose_stages` already reports errors *by stage*
(`errors.csv`), and `blame` attributes each error to its *producing rule-time* — the exact
signals a stage-aware inducer consumes.

## Sketch of a v1 algorithm

For each time interval (bounded by consecutive attested stages), and boosting within it:

1. Set the interval's input = the earlier stage's attested forms; target = the later stage's.
2. Loss = distance(current derived, target).
3. Run diagnosis on the residual → top systematic correspondence + its environment.
4. Propose that rule at a few context generalities and positions within the interval.
5. Evaluate each with what-if; take the steepest-descent candidate; insert it.
6. Repeat until the interval's loss plateaus or an **MDL penalty** (rule cost) outweighs the
   gain. Then move to the next interval.
7. Finally, relax the interval boundaries and do a global refinement pass (blame-guided:
   drop/edit rules that later rules made counterproductive; anneal or beam to escape local
   minima).

## Where it's genuinely hard

- **Rule ordering / relative chronology** — mitigated but not eliminated by stage bucketing
  (still an ordered search *within* each interval).
- **Opacity** — mitigated by intermediate stages, but not fully (a change opaque even at the
  nearest attested stage leaves no direct evidence).
- **Context discovery** — finding the *right* environment for a rule (the phi-autopsy is the
  main tool, but generalization vs overfitting is a real tension, hence the MDL penalty).

## Validation: a benchmark we already own

`projects/latin_to_french` is a turnkey test harness: hide its hand-built `rules.toml`, keep
`words.toml` (input + `final` + the intermediate `stages`), run the inducer, and measure
**(a)** whether induced accuracy approaches the hand-built baseline, **(b)** whether induced
rules resemble the documented sound laws, and **(c)** an ablation dropping the intermediate
stages, to quantify exactly how much the dense/chronological supervision buys.

## The differentiable alternative (back pocket)

One could instead relax rule application into a soft/weighted transducer with continuous
feature weights and a differentiable soft-edit-distance loss, and literally backprop. The
cost is losing the crisp, interpretable symbolic rules that are Fortis's whole point, then
having to discretize back into rules lossily. Worth noting, not worth leading with.

---

## Ask for Fable

Please turn this sketch into a **detailed implementation document** for the automated
rule-finding feature, targeting the existing Fortis codebase (the `analysis/` consumer layer,
which already depends on the engine but not vice versa). I'd like it concrete enough to build
from. Please cover:

1. **Objective function, stated precisely** — the exact per-stage, MDL-regularized loss over
   the lexicon (fit term from accuracy; rule-cost term; how the two are weighted without
   per-dataset hand-tuning).
2. **The search algorithm in full** — candidate-rule *generation* (how a diagnosis
   correspondence + its autopsied environment becomes a set of candidate rules at varying
   generality), scoring, acceptance, the within-interval ordering search, escape from local
   minima (annealing / beam / backtracking), and termination.
3. **Stage-aware decomposition** — how to consume the intermediate attested `stages`:
   interval bucketing, per-interval boosting, composition across intervals, the final global
   refinement pass, and graceful degradation when only `final` is present (no stages).
4. **Data + API** — any `words.toml` / loader changes; the new module(s) and their public
   functions; how they reuse `accuracy`, `diagnosis`, `blame`, `form_at_time`, and the
   parallel `derive_all`; CLI/report surface (by analogy to `--try` and the written reports).
5. **Complexity and performance** — how many derivations the search evaluates and how to keep
   it affordable (caching, parallelism, candidate pruning).
6. **Evaluation protocol** — the Latin→French ablation above, metrics, and what "good enough"
   looks like for a first milestone.
7. **Risks and honest limits** — opacity, overfitting vs generalization, mergers, ordering
   blow-up, and where a human-in-the-loop is expected rather than full automation.
8. **A staged milestone plan** — the smallest end-to-end slice that produces a *measurable*
   result (e.g. single unordered rewrites within one interval), then what each subsequent
   milestone adds.
