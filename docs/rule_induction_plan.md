# Rule induction: implementation plan

_The implementation document requested by `rule_induction_sketch.md`: automated
supervised rule finding — given `words.toml` inputs and attested targets (final and
intermediate stages), induce the rule cascade. This is the ancestor-given sub-problem of
full reconstruction (`reconstruction_sketch.md`); everything here lives in the
`analysis/` consumer layer and treats the engine as a fixed black box._

## 0. Design in one page

The inducer is stagewise additive modeling (gradient boosting) with sound-change rules
as weak learners, run **per time interval** between attested stages, under a **two-part
MDL objective** that prices both misfit and rule complexity in bits.

The loop, per interval:

1. Build a **mini-project**: the interval's words, with the _attested earlier-stage
   form_ as input and the _attested later-stage form_ as target (teacher forcing). The
   whole existing pipeline — `derive_all`, `measure_accuracy`, `align`, `confusions`, blame — runs
   on it unchanged.
2. Score the current cascade: `L = fit_bits + rule_bits` (§1).
3. Read the residual: the confusion tally, re-autopsied on the **derived side** (§2.1),
   names the most systematic remaining correspondence and its conditioning environment.
4. **Propose** a candidate set: the corrective rewrite at several context generalities,
   plus natural-class and insertion/deletion variants, written in Fortis notation and
   parse-validated (§2.2).
5. **Score** every candidate incrementally (append fast path: one `apply_rule` sweep per
   word, no re-derivation), then re-derive properly for the top few, at up to four
   insertion positions (§2.3).
6. **Accept** the best candidate iff it strictly lowers `L` — the bits it saves in the
   residual must exceed the bits it costs to write. Otherwise walk the escape ladder
   (§2.5); if that fails too, the interval is done.
7. After the interval converges, a **shrink pass** deletes any rule whose removal now
   lowers `L` (§2.6).

Then **compose**: assign real times inside each interval, run the full cascade from the
true inputs over the whole lexicon (including final-only words), and do a **global
refinement** boost whose residuals are localized to intervals via blame's
stage-divergence (§3.4). With no attested stages the same algorithm runs on the single
interval input→final (§3.5).

Everything maps onto existing machinery:

| component            | reuses                                             | new code                                                |
| -------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| loss                 | `accuracy_by_stage`, `align`, `feature_diff`            | the bits model (§1)                                     |
| residual → next rule | `confusions`, phi machinery from `diagnosis`       | derived-side contexts (§2.1), proposal generator (§2.2) |
| step evaluation      | `derive_all(_parallel)`, `apply_rule`, `load_rule` | incremental scorer (§2.3)                               |
| chronology           | `Word.stages`, `form_at_time`, `blame`             | interval bucketing, mini-projects (§3)                  |
| reporting            | report conventions of `whatif.md` etc.             | `induction.md`, `induced_rules.toml` (§4.4)             |

## 1. Objective function

The loss of a cascade `R` over lexicon `W` is a two-part description length, in bits:

```
L(R) = rule_bits(R) + fit_bits(R)

fit_bits(R)  = Σ_{w ∈ W} freq(w) · Σ_{s ∈ checkpoints(w)} residual_bits(derived_w(s), attested_w(s))
rule_bits(R) = Σ_{r ∈ R} bits(r)
```

`checkpoints(w)` is every attested form the word carries: each `Word.stages[T]` (measured
against the snapshot at rule-time `T`, exactly as `accuracy_by_stage` does) plus `final`.
During per-interval induction the sum collapses to the interval's single target; the
full sum is the Phase-B (composition/refinement) objective.

MDL answers the sketch's "how are fit and rule cost weighted without per-dataset
hand-tuning": both sides are bits, so the exchange rate is fixed by the encoding, not
by a λ knob. A rule is worth adding exactly when writing it costs fewer bits than the
corrections it makes unnecessary.

### 1.1 The fit term: residual bits

`residual_bits(derived, attested)` is the cost of encoding the corrections that turn
the derived form into the attested one, read off the existing `accuracy.align` op list
(the same deterministic alignment diagnosis uses):

| op                                | correction encoded     | cost                                   |
| --------------------------------- | ---------------------- | -------------------------------------- |
| `match`                           | none                   | 0                                      |
| `sub` (a→b)                       | site + feature delta   | `B_site + b_feat · feature_diff(a, b)` |
| `delete` (target phone missing)   | site + spell the phone | `B_site + b_feat · feature_count(a)`   |
| `insert` (spurious derived phone) | site only              | `B_site`                               |

with

```
B_site  = log2(3) + log2(L̄ + 1)          # op kind + position; L̄ = mean attested length
b_feat  = log2(|F|) + log2(V̄)            # name one feature + one value
```

`|F|` = feature names in the project's `FeatureInventory`, `V̄` = mean values per
feature, `L̄` measured once from the attested forms. All three are computed from the
project at startup — nothing is tuned per dataset.

Encoding substitutions as _feature deltas_ is deliberate: it makes `fit_bits` a linear
blend of phone-edit count and feature edit distance, so the objective has the gradient
the sketch wants — a rule that moves ɛ→e when the target is i lowers `fit_bits` even
though the phone distance is unchanged. `feature_diff` and the phone/feature machinery
come straight from `accuracy`; the private `_segment`/`_specified` helpers get promoted
to public (`segment_form`, `specified_features`) rather than re-implemented. A phone
that will not segment falls back to `b_feat · F̄` (spell it as an average-size segment),
so unsegmentable notation degrades the estimate, never crashes it.

Worked scale (Latin→French: |Σ| ≈ 60 phones, |F| ≈ 25 features, V̄ ≈ 3, L̄ ≈ 6):
`B_site ≈ 4.4` bits, `b_feat ≈ 6.2` bits — a one-feature near-miss costs ≈ 10.6 bits, a
gross substitution or indel ≈ 4.4 + 6.2·k for k specified features.

### 1.2 The rule-cost term

`bits(r)` encodes the structural description, element by element:

```
bits(r) = B_rule                            # header: time slot, application mode, arrow
        + Σ_{e ∈ target,result,contexts,exceptions} (b_tag + bits(e))

bits(letter literal)   = log2(|letters|)
bits(feature bundle)   = Σ_{f: v}  (log2(|F|) + log2(V̄))     # b_feat per specified pair
bits(boundary #, $)    = 0                                    # covered by b_tag
bits(letter^[Δ])       = log2(|letters|) + b_feat · |Δ|
b_tag                  = log2(#element kinds) ≈ 3             # what kind of element follows
B_rule                 ≈ 10
```

Longer contexts and fatter bundles cost linearly more — this is the generalization
pressure that resolves the context-discovery tension: an over-specific environment must
buy its keep in residual bits. Worked example: `b → a / _ #` ≈ 10 + (3+6) + (3+6) + 3 ≈
31 bits — it pays for itself once it fixes about three one-feature errors, or two
gross ones. A whole-word suppletion is priced accordingly steeply, which is most of the
anti-overfitting story (§7 has the rest).

### 1.3 Acceptance criterion

Candidate `r` at placement `p` is accepted iff

```
ΔL = bits(r) + fit_bits(R ⊕p r) − fit_bits(R) < 0
```

with ties (|ΔL| < ε) rejected. Two hard guards on top of MDL, both settings:
a candidate must strictly improve at least `min_improved_words` (default 2) words, and
the generator never emits `words = [...]`-restricted rules — per-word suppletion is the
human's tool, not the search's.

### 1.4 Frequency and stage weighting

`freq(w)` multiplies a word's residual bits (a token appears that many times in the
data being encoded) — frequency-weighted induction falls out for free. All attested
checkpoints weigh equally by default; a `final_weight` setting exists for projects
whose intermediate notation is only loosely comparable (§7), to keep noisy stages from
dominating.

### 1.5 Where the knobs live

A new frozen dataclass in `models/settings.py`, mirrored in
`projects/default/settings.toml`:

```toml
[induction]
min_improved_words   = 2      # §1.3
top_confusions       = 5      # confusions expanded per iteration (§2.2)
contexts_per_confusion = 25   # candidate cap per confusion (§2.2)
placement_candidates = 5      # candidates that get the full placement search (§2.3)
max_rules_per_interval = 60   # iteration cap (§2.7)
alignment_distance_cap = 4    # words beyond this distance don't feed correspondences (§2.1)
final_weight         = 1.0    # §1.4
```

The bits constants (`B_rule`, `b_tag`) are module constants, not settings — they are
part of the code's definition of the objective, and moving them is a research act, not
project tuning.

## 2. The search algorithm

### 2.1 Correspondences, read from the derived side

Diagnosis's autopsy conditions on the **attested**-form environment — the right
coordinate for a human reading a report, and the wrong one for a rule proposer: an
induced rule fires on the _derived_ form, so its context must hold there. The inducer
gets a derived-side variant (new module `induction/correspond.py`), built on the same
`align` output:

- For each confusion `(expected=a, got=b)`, every aligned site where derived `b` maps
  to target `a` is a **should-change** site; every site where derived `b` maps to
  target `b` is a **should-stay** site. (Sites where `b` maps to some third phone are
  excluded from both classes for this correspondence.)
- Each site yields predictors from the **derived** form at `op.derived_index`:
  neighbour identities (`left=p`, `right=#`), neighbour features (`left:voice=1`), and
  **self** features of the site's own phone beyond its base identity (`self:stress=primary`,
  `self:length=long`) — the handle for stress- and length-conditioned changes, which
  the Latin cascade is full of.
- phi over (predictor present/absent) × (should-change/should-stay), with the existing
  `phi_coefficient` and support-floor logic lifted from `diagnosis`.
- Deletion residuals (`got=None` — a phone the derivation never produced) read their
  environment from the derived-side _gap_: the nearest alignment neighbours that do
  have a `derived_index`. Insertion residuals (`expected=None`) read the spurious
  phone's own neighbours.

Words whose distance exceeds `alignment_distance_cap` are excluded from correspondence
extraction (their alignments are unreliable and poison the tallies); they still count
in the loss, so fixing the systematic words first eventually pulls them under the cap.

### 2.2 Candidate generation

For each of the `top_confusions` residual correspondences, the proposer emits
candidates as **notation strings**, then parses each through the existing
`load_rule` — anything that fails to parse or validate is silently dropped, so the
generator can be aggressive and the parser stays the single source of truth. A small
`induction/notation.py` renders `FeatureBundle`s back to bundle notation (the inverse
of `parse_definition` for the realized subset; property-tested by round-trip).

The lattice per correspondence `(a ← b)` (rule direction: rewrite derived `b` to `a`):

1. **Unconditioned**: `b → a`.
2. **Single predictor** (top ~8 by phi): `b → a / p _`, `b → a / _ [+nasal]`,
   `b → a / _ #`, and self-predictors folded into the target:
   `b^[stress: primary] → a`.
3. **Predictor pairs** (consistent sides, top pairs, capped): `b → a / [+syllabic] _ #`.
4. **Natural-class targets**: correspondences are grouped by identical feature delta
   `δ = diff(b→a)`; a group of ≥ 2 sharing δ proposes the class rule
   `[shared features of the sources] → [δ as a merge bundle]`, at the same context
   generalities. One class rule is cheaper in bits than three literal rules — MDL
   makes real sound laws win over their fragments, which is also what makes induced
   cascades _readable_.
5. **Deletions**: `b → ∅ / ...` (context required by policy). **Insertions**:
   `∅ → a / ...` (context required by the notation itself).

Everything is capped at `contexts_per_confusion`. The v1 language is deliberately a
subset of Fortis notation: literals, realized bundles, `^[Δ]` overrides, one- or
two-element contexts, `#`. No quantifiers, alphas, references, or tier operations — a
proposer for `([-syllabic])*`-style long-distance contexts is a later milestone (M4),
added as a targeted template (`/ _ C* V́` for stress-sensitive rules) rather than a
grammar-wide search.

### 2.3 Scoring and placement

Scoring is two-tier, because the candidate count times a full re-derivation is the
whole cost of the search (§5):

- **Append fast path** (every candidate). The boosting default places the candidate
  after all current interval rules, so its input is the _cached current derived form_
  of each mini-lexicon word. Scoring is then one `apply_rule` per word — no derivation:
  `cannot_match` prunes most words for free (the identity contract makes a non-firing
  sweep cheap), and only words whose form actually moves get re-measured. This yields an
  exact ΔL _for the append placement_.
- **Placement search** (top `placement_candidates` by append-ΔL). Feeding/bleeding means
  append is not always the right slot. Each finalist is also evaluated at: interval
  start; immediately before and after the interval rule that blame names most often on
  the correspondence's sites. Non-append placements re-derive only the words the
  candidate _could_ touch (pre-filtered by `cannot_match` against each cached
  intermediate snapshot of the word), resuming from the cached form at the insertion
  point — the `DerivationStep` list already stores every snapshot needed.

The winner is the (candidate, placement) with the lowest ΔL. Candidate scoring is
embarrassingly parallel and fans across processes exactly like `derive_all_parallel`
(same spawn-pool pattern, one initializer shipping the mini-project).

### 2.4 Ordering bookkeeping

Within an interval the inducer owns a plain ordered list of rules; `time` keys are
synthesized as the list index for evaluation runs and only mapped to real times at
composition (§3.3). Insertion anywhere is a list insert plus renumber — no fractional
time hacks, and `RuleInventory` stays untouched.

### 2.5 Escape ladder (when the best ΔL ≥ 0)

In order, each step only if the previous failed:

1. **Deeper residuals**: expand the next `top_confusions` down the tally (the top
   confusion may be irreducible noise while #7 is a clean rule).
2. **Pair lookahead**: for the top correspondence, propose _two-rule_ candidates —
   the corrective rewrite preceded by a bridging rewrite through each intermediate
   value one feature away (the classic chain-shift/opacity shape: `a → ə → ∅`). Scored
   as a unit; accepted only if the pair beats its summed bits.
3. **Stop** and record a _stuck report_: the top irreducible correspondences, their
   phi tables, and example words — the designed human-in-the-loop handoff (§7).

Beam search over cascades (keep the top B partial cascades per interval instead of one
greedy chain) is deliberately deferred to M4: greedy + shrink + global refinement has
to be measured first, and the evaluation harness (§6) is exactly the instrument for
deciding whether the beam is worth its cost.

### 2.6 Shrink pass

After an interval converges: for each induced rule, score the cascade without it (one
mini-run each, parallel across rules). Remove the rule whose deletion lowers `L` most;
repeat to fixpoint. This is the boosting-pruning analog: later rules routinely make an
early greedy step redundant, and MDL now charges it rent. The same pass runs globally
in Phase B (§3.4) with full-lexicon runs.

### 2.7 Termination

An interval stops when the escape ladder is exhausted, `max_rules_per_interval` is
hit, or `fit_bits` reaches 0. Global refinement stops when a full sweep (boost attempt

- shrink pass) accepts nothing.

## 3. Stage-aware decomposition

### 3.1 Intervals and teacher forcing

Sorted attested stage times `t₁ < … < tₙ` partition the cascade into intervals
`(input → t₁), (t₁ → t₂), …, (tₙ → final)`. Per interval, the training set is the words
attesting **both** endpoints, and the interval input is the **attested** earlier form,
not the derived one — teacher forcing. Consequences, all load-bearing:

- Intervals are **fully independent**: they can be induced in parallel, and an
  upstream interval's mistakes cannot contaminate a downstream one during Phase A.
- The ordering search shrinks from one global problem to n+1 local ones — the sketch's
  chronology-localization argument, realized.
- An attested stage can expose environments the final form erased (opacity relief) —
  the interval's residuals see them directly.

In Latin→French: 299 of 447 measured words carry stage chains (−200, −100, 750, 1000,
1200, 1400), so Phase A trains on ~299-word mini-lexicons per interval; the other 148
final-only words enter at Phase B.

### 3.2 Mini-projects

An interval problem is literally a `Project`: `words` = `{attested_source_ipa:
Word(ipa=source, final=attested_target, frequency=…)}`, `rules` = the induced list so
far (times = list indices), everything else (features, letters, tiers, settings)
shared with the parent. `induction/intervals.py` builds these; every downstream tool —
`derive_all`, `measure_accuracy`, `confusions`, `blame_all` — works on them without modification.
This is the single biggest reuse win in the design.

One gate: the attested source form must segment (`string_to_sequence`) under the
project's letters/diacritics. A word whose stage form does not segment is excluded
from that interval (counted and reported, never silently dropped). The stage forms in
`latin_to_french` were written to be engine-comparable, so exclusions there should be
rare; a project with reconstructive stage notation will see this number and know its
intervals are under-supervised.

### 3.3 Composition

Induced interval rules get real times evenly spaced strictly inside their interval
(e.g. interval (300, 500] with 12 rules → times 315, 330, …), leaving room for later
insertions and never colliding with the boundary stages. Rule ids are minted as
`ind_<interval>_<n>`; `name` carries the human-readable correspondence
(`"b → a / _ # (induced)"`), `description` the provenance (support, phi, iteration,
ΔL). The composed inventory serializes to `induced_rules.toml` via the normal loader
round-trip.

### 3.4 Global refinement (Phase B)

Run the composed cascade from the true inputs over **all** words; the objective is now
the full multi-checkpoint `L(R)` of §1. Loop until a full sweep changes nothing:

1. **Global shrink** (as §2.6, full-lexicon runs) — kills rules that only worked under
   teacher forcing.
2. **Localized boosting**: extract correspondences per checkpoint; a residual is
   assigned to the interval where it first appears — by blame's `stage_divergence`
   (ground truth where stages exist) with `errors_by_time` as the fallback — and the
   proposer/scorer run as in §2, except candidates are evaluated on the full composed
   cascade (append-within-interval keeps a fast path: resume each word from
   `form_at_time` at the interval's end).

Phase B is where teacher-forcing's one weakness — the composed input to interval k is
the _derived_ t_k form, not the attested one — gets repaired: any systematic gap
between the two is precisely a residual that Phase B's proposer sees.

### 3.5 Degradation without stages

No `stages` ⇒ one interval, input→final; Phase A and B collapse into one loop. Nothing
else changes. The ordering search burden that stages were absorbing comes back
(placement search does more work, the escape ladder fires more), which is exactly what
the ablation in §6 measures. `--ignore-stages` forces this mode on stage-bearing data
for that experiment.

## 4. Data and API

### 4.1 Modules

```
src/fortis/analysis/induction/
  __init__.py
  objective.py    # bits model: residual_bits, rule_bits, CascadeScore
  correspond.py   # derived-side correspondences + phi contexts (§2.1)
  notation.py     # FeatureBundle/rule → notation string (round-trip-tested)
  candidates.py   # the proposal lattice (§2.2), parse-validated via load_rule
  evaluate.py     # incremental scorer: append fast path + placement re-derive (§2.3)
  intervals.py    # stage bucketing, mini-project construction (§3.1–3.2)
  boost.py        # induce_interval: the greedy loop + escape ladder + shrink
  refine.py       # compose, Phase-B global refinement (§3.3–3.4)
  report.py       # induction.md + induced_rules.toml writers
  main.py         # CLI
```

Key public signatures:

```python
# objective.py
def residual_bits(distance: DistanceToTarget, project: Project) -> float
def rule_bits(rule: Rule, project: Project) -> float
@dataclass(frozen=True)
class CascadeScore:  # fit_bits, rule_bits, total, exact, mean_distance — one snapshot

# correspond.py
@dataclass(frozen=True)
class Correspondence:  # expected, got, count, delta (feature diff), sites
def correspondences(distances, project, cap: int) -> list[Correspondence]
def derived_contexts(corr, distances, project) -> FocusAutopsy   # derived-side phi table

# candidates.py
@dataclass(frozen=True)
class Candidate:  # definition str, parsed rules, provenance (corr, predictors, phi)
def propose(corr, contexts, project, settings) -> list[Candidate]

# evaluate.py
class IntervalState:  # cached per-word derivations for the current interval cascade
    def score_append(self, cand) -> float            # ΔL, apply_rule fast path
    def score_at(self, cand, index) -> float          # ΔL, partial re-derive
    def accept(self, cand, index) -> None             # commit + refresh caches

# boost.py / refine.py
def induce_interval(interval, project, settings) -> InducedInterval  # rules + trace
def compose(intervals, project) -> RuleInventory
def refine(project, inventory, settings) -> tuple[RuleInventory, RefineTrace]
```

### 4.2 Loader and settings changes

- `words.toml`: **no changes** — `stages`, `final`, `frequency` already carry
  everything the inducer consumes.
- `settings.py`: add `InductionSettings` (§1.5) to `Settings`, with the
  default-mirror test extended to the new section.
- `accuracy.py`: promote `_segment`/`_specified` to public names (used by the bits
  model); no behavior change.
- `diagnosis.py`: extract the phi/support-floor core into a shared helper so
  `correspond.py` does not duplicate it. Reports unchanged.

### 4.3 CLI

```
python -m src.fortis.analysis.induction.main --project DIR
    [--out FILE]           # induced_rules.toml   (default: <project>/induced_rules.toml)
    [--report FILE]        # induction.md         (default: <project>/induction.md)
    [--ignore-stages]      # ablation mode (§3.5)
    [--seed-rules FILE]    # induce around a fixed partial cascade (§7)
    [--interval T1:T2]     # run one interval only (development / debugging)
    [--max-rules N]        # override max_rules_per_interval
    [--serial | --workers N]
```

By analogy with the accuracy CLI: progress and one-line summaries to stderr, reports to
the project directory. The webapp gets an Induction tab reading `induction.md` in a
later milestone, not v1.

### 4.4 Reports

`induction.md`, per interval: an iteration table (accepted rule, ΔL split into fit/cost
bits, exact and mean-distance before→after, words touched, placement), rejected-best
lines when the escape ladder fired, the shrink log, and the stuck report (§2.5) when
induction stopped with residual structure left. Then the composition summary and the
Phase-B trace in the same shape. `induced_rules.toml` is a normal loadable rules file
(§3.3) — the round trip `induce → load → measure` is itself a test.

## 5. Complexity and performance

Let W = interval words (~300), C = candidates per iteration (≤ 5 confusions × 25 =
125), I = iterations per interval (≤ 60), K = intervals (7 for Latin→French).

- **Append scoring** dominates by count: `I × C × W` ≈ 2.3M `apply_rule` sweeps per
  interval — but a sweep is microseconds when `cannot_match` prunes (most words, most
  candidates), and the whole tier fans across processes. This is the designed-for
  regime: the fast path exists precisely so the candidate count never multiplies a
  full derivation.
- **Placement re-derives**: `I × placement_candidates × 3` partial mini-runs ≈ 900 per
  interval, each over only the pre-filtered affected words under a ≤ 60-rule cascade —
  small next to one full-project derivation (447 words × 704 rules, a few seconds
  wall-clock today).
- **Shrink**: ≤ rules² mini-runs per interval in the worst case (re-scored after each
  removal); in practice a handful of full passes.
- **Phase B**: each accepted global candidate costs ~1 full-lexicon derivation; the
  global shrink costs one per induced rule per pass. Bounded by the acceptance rate,
  which MDL keeps low.

Caching that makes this hold: `IntervalState` keeps every word's current derivation
(steps = snapshots at every rule, so any insertion point resumes for free);
`apply_rule`'s identity contract keeps the tier-lowering/syllabification caches warm
across the millions of non-firing sweeps; candidate scoring shares one immutable
mini-project across workers (the `derive_all_parallel` initializer pattern). No new
cache machinery is required — the engine's existing contracts were built for exactly
this access pattern.

## 6. Evaluation protocol

Three experiments, in order, all on `projects/latin_to_french`:

1. **Synthetic recovery (the learnability floor).** Derive the lexicon with the
   hand-built cascade; snapshot `form_at_time` at the attested stage times; emit a
   synthetic `words.toml` (same inputs, machine-generated stages/finals — perfectly
   consistent, zero notation noise). Hide the rules; run the inducer. Metrics:
   final `fit_bits` (target: 0), exact accuracy (target: 100% per interval), induced
   rule count vs the hand cascade's per interval, and **behavioral rule recovery** —
   an induced rule matches a hand rule if swapping one for the other changes no
   derivation over the lexicon. If the inducer can't learn from clean self-generated
   data, nothing downstream matters; this experiment gates every milestone.
2. **Real-data induction.** Hide `rules.toml`, keep the real attested forms. Baselines:
   identity cascade (no rules) and the hand-built cascade (currently 388/447 exact,
   mean phone distance 0.208). Report per-interval teacher-forced accuracy, composed
   final accuracy, `L(R)` of induced vs hand cascade, and a qualitative table mapping
   the top induced rules to documented sound laws (`rule_translation.md` is the key).
3. **Stage ablation.** Re-run experiment 2 with `--ignore-stages`. The gap between the
   two runs — in final accuracy, rule count, wall-clock, and stuck-report size — is
   the measured value of dense chronological supervision, the sketch's central claim.

Milestone bars (first pass; revised once experiment 1 lands):

- **M1 good-enough**: synthetic single-interval recovery — fit 0, ≤ 2× the hand rule
  count for that interval.
- **M3 good-enough**: real data, teacher-forced — on the worst interval (−100→750,
  where mean phone distance today is 1.224 even under the hand cascade), the inducer
  recovers ≥ 50% of the loss reduction the hand rules achieve; composed final accuracy
  clearly beats identity and lands within striking distance of a useful assistant
  (the target is _leads a human trusts_, not parity with 704 curated rules).

## 7. Risks and honest limits

- **Opacity.** A change opaque even at the nearest attested stage leaves no direct
  evidence; pair lookahead (§2.5) catches the two-step shapes, and nothing catches the
  rest. The stuck report is the designed handoff: it names the irreducible residual and
  its environments, and `--seed-rules` lets a human drop in the opaque rule and re-run.
  Expected mode of use: the inducer does the systematic 80%, the human does the opaque
  tail — that is already a large win over hand-building all 704.
- **Overfitting vs generalization.** MDL prices over-specific contexts; the
  `min_improved_words` floor and the ban on `words=` restrictions close the trivial
  routes. The residual risk is _systematic coincidence_ on a 300-word lexicon — a
  context that generalizes in the sample but not the language. No in-sample defense
  exists; the honest check is the qualitative comparison against documented laws
  (experiment 2) and, later, held-out words.
- **Mergers and splits.** Mergers (many→one) are easy forward. A _split_ whose
  conditioning environment was later destroyed — and is invisible at every attested
  stage — is unlearnable by construction; it surfaces as a stuck report where the
  same source phone needs two outcomes with no separating predictor.
- **Ordering blow-up.** Bounded by stages (7 small ordered searches, not one big one)
  and by the placement heuristic (4 positions, not all). The no-stage ablation
  quantifies what remains; beam search (M4) is the reserve if greedy+placement proves
  insufficient _within_ intervals.
- **Notation noise in attested stages.** A stage written in notation the engine never
  emits creates a constant loss floor and, worse, false correspondences. Mitigations:
  the segmentation gate (§3.2) reports exclusions, `alignment_distance_cap` keeps
  garbage alignments out of the proposer, `final_weight` can down-weight noisy stages.
  The -200 stage in Latin→French (137/299 exact under the _hand_ cascade, mostly
  stress-placement conventions) is the live example — its interval will need exactly
  these dials.
- **Expressivity gap.** The v1 proposer emits a small notation subset (§2.2). Changes
  that need quantified spans, alpha harmony, or tier operations will show up as
  residuals v1 cannot fix. Deliberate: each extension (M4+) is a new candidate
  template whose value the harness can measure, not a speculative grammar search.
- **MDL constant sensitivity.** The bits model's constants set the fit/cost exchange
  rate; they are principled but not sacred. The synthetic benchmark doubles as the
  calibration instrument: if the inducer under- or over-accepts on clean data, the
  constants are wrong, and that is where they get fixed — never per real dataset.

## 8. Milestones

Each milestone ends with a measurable number from the §6 harness.

- **M0 — Harness and objective.** `objective.py`, `intervals.py` (bucketing +
  mini-projects), `evaluate.py`'s append fast path, the synthetic-lexicon generator,
  and tests. _Measure:_ `L` of identity vs hand cascade on real and synthetic data —
  the scoreboard every later milestone reads.
- **M1 — Single-interval boosting, synthetic.** `correspond.py`, `candidates.py`
  (lattice tiers 1–3 + indels), `boost.py` greedy loop, append placement only.
  _Measure:_ synthetic recovery on one interval (bar in §6). This is the sketch's
  smallest end-to-end slice.
- **M2 — Real-data single interval.** Placement search, shrink pass, class-target
  candidates (tier 4), the escape ladder's step 1, `induction.md`. _Measure:_
  teacher-forced accuracy on −100→750 vs the hand rules for that interval.
- **M3 — Full pipeline.** All intervals, composition, Phase-B refinement,
  `--ignore-stages`, `induced_rules.toml` round-trip, CLI. _Measure:_ experiments 2
  and 3 in full — the headline result and the ablation.
- **M4 — Search strength.** Pair lookahead, beam option, quantified-span and
  stress-context templates, per-interval parallelism. _Measure:_ delta on the M3
  numbers per feature, so each buys its complexity or gets cut.
- **M5 — Assistant ergonomics.** `--seed-rules` workflows, stuck-report polish,
  webapp Induction tab, held-out-word evaluation. _Measure:_ end-to-end walkthrough —
  seed with the CL period's hand rules, induce the rest, human-patch the stuck
  report — written up as the workflow doc.
