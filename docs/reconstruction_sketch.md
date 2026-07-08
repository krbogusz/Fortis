# Idea sketch: automated reconstruction of a common ancestor from cognates

_A design sketch for discussion — deliberately incomplete, meant to be poked at._

## Context (for a reader who doesn't know the codebase)

**Fortis** is a general phonological derivation engine. Its normal job is **forward**:
given a proto-form and an _ordered cascade of context-sensitive sound-change rules_, it
derives the daughter forms, step by step, and can **measure** the result against attested
targets (phone- and feature-level edit distance), **diagnose** systematic errors (a phone
confusion matrix + a context autopsy that finds which environments an error correlates
with, by phi coefficient), and **blame** each wrong output on the specific rule that
produced it. It already ships a hand-ported Latin→French cascade (from DiaSim/DiaCLEF).

This sketch asks the **inverse** question: given only the _daughter_ forms (cognate sets
across related languages), can we recover **(a)** the common ancestor form for each
cognate set and **(b)** the rule cascades that derive each daughter from it?

## The reframing that matters

Reconstruction is **abduction, not deduction**, and it is **not invertible**: sound change
merges distinctions (if ancestral `t` and `d` both become `t` in a daughter, no data
recovers which was which). So we do not _compute_ the ancestor — we **search** for the
`⟨ancestor lexicon, rule cascades⟩` that best **regenerates** the observed daughters.

The key leverage: **Fortis is already the generator and the scorer for that search.** A
reconstruction hypothesis _is_ a Fortis project (proto-lexicon + rules); running it forward
and measuring against the daughters _is_ the objective. Reconstruction becomes a search loop
wrapped around machinery that already exists.

## The objective (the clean formulation)

Pick the hypothesis minimizing **total description length**:

```
cost = size(proto-lexicon) + Σ_daughter size(rule cascade_d) + Σ misfit(derive(proto, rules_d), attested_d)
```

subject to the rules regenerating the daughters. This is Occam's razor made computable
(equivalently, the Bayesian posterior: fit × a simplicity/naturalness prior). Fortis
supplies the last two terms directly — the rules _are_ the model, measuring _is_ the misfit.
The open design work is the first term's **prior** (what makes a rule set "small" or
"natural") and the **search** that explores hypotheses.

## Why Romance → Vulgar Latin is the right testbed

Most reconstruction is unfalsifiable — you can't check Proto-Indo-European. Romance is the
opposite, which makes it a **benchmark with an answer key**:

- **The ancestor is attested.** Reconstruct from the daughters, then measure edit distance
  of the reconstructed proto-form against _actual_ Classical/Vulgar Latin. A number, not an
  opinion.
- **Many witnesses**, which is what breaks the underdetermination that dooms two-language
  cases: Spanish, Italian, French, Portuguese, Romanian, Catalan, Occitan — and crucially
  **Sardinian**, the conservative outlier that often preserves the ancestral state and thus
  supplies _directionality_ (e.g. it keeps `/k/` in `kentu` where the others palatalized).
- **The sound laws are documented**, so induced rules can be checked against known changes
  (palatalization of `k` before front vowels, intervocalic lenition, final-vowel loss in
  French, `-ct- → it/tt/ch/pt`, etc.).
- **Fortis already has a Latin→French forward cascade**, usable as an _oracle_: one
  daughter's "correct" rules exist, to validate rule induction against.

Worked flavor of a single correspondence set (Latin `centum` 'hundred'):

| daughter   | form     | initial |
| ---------- | -------- | ------- |
| Sardinian  | `kɛntu`  | k       |
| Italian    | `tʃɛnto` | tʃ      |
| Spanish    | `θjento` | θ       |
| French     | `sɑ̃`     | s       |
| Portuguese | `sẽtu`   | s       |

The correspondence `{k, tʃ, θ, s, s}` before a front vowel, with Sardinian's `k` and the
front-vowel environment, points straight at ancestral `*k` + a conditioned palatalization —
exactly the reasoning to automate.

## The pipeline (with have / need against current Fortis)

1. **Cognate data model + loader** — a lexicon of _sets_: one gloss → a form per daughter.
   _Need_ (small): extend the `words.toml`-style loader to multi-daughter rows.
   `projects/romance/cognates.toml` already has the shape (gloss → {lang = form}), with
   attested Latin included as a held-out answer key.
2. **Alignment** — column-align the phones within each cognate set.
   _Have_ pairwise: `align()` (Damerau–Levenshtein op-trace) in `analysis/accuracy.py`.
   _Need_: multiple-sequence alignment for ≥3 daughters.
3. **Correspondence sets** — tabulate which daughter phones co-occur per column, **and in
   what environment**.
   _Have, almost for free_: `analysis/diagnosis.py`'s confusion matrix + phi-context
   autopsy is already a _conditioned-correspondence_ engine — it was built to ask "which
   phone became which, in which environment." Re-point it from target/derived to daughter-A/
   daughter-B.
4. **Proto-segment reconstruction** — posit one ancestral phoneme per correspondence set.
   _Need_: a **directionality / naturalness prior** (which changes are common and one-way:
   devoicing, lenition, laryngeal/final loss). This is the linguistic knowledge that breaks
   ties the data can't; feature-edit-distance is a crude proxy ("prefer small changes"),
   but real typological frequencies are better.
5. **Rule induction** — synthesize the minimal context-conditioned Fortis rules mapping
   proto → each daughter. **The hard, open part** (program synthesis over rule notation).
   _Have as the verifier/critic_: forward derive + measure (fitness), `--try`/whatif (test a
   candidate rule), and **`blame`** (localize exactly where a derivation diverges → tells
   the search _which_ rule to fix). Missing: the _proposer_ of candidate rules.
6. **Joint optimization** — co-optimize ancestor and rules under the description-length
   objective (they trade off).

## What's genuinely missing (ranked by difficulty)

1. **Rule-space search / synthesis** (stage 5) — the research problem. Candidate framings:
   constraint-solve each correspondence set into a rule, then a beam/genetic/MCMC search over
   rule _edits_ using blame-guided proposals; ordered cascades (feeding/bleeding) blow up the
   space and need taming.
2. **A directionality prior** (stage 4) — hand-built typological table vs learned; without
   it the answer is underdetermined even with perfect data.
3. **Multiple-sequence alignment** (stage 2) — well-trodden (bio-inspired), just not present.
4. **Proto-inventory hypothesis** — reconstruct sets _jointly_ under a shared inventory, not
   independently.

## Validation methodology (the payoff of a known answer)

- **Proto-form accuracy**: edit distance of reconstruction vs attested Latin (Fortis's accuracy analysis,
  unchanged).
- **Rule fidelity**: do induced rules match documented sound laws / the existing Latin→French
  oracle cascade?
- **Round-trip**: reconstructed ancestor + induced rules must forward-derive the daughters —
  Fortis does this natively, so it's a built-in consistency check.
- **Ablations**: drop daughters (esp. Sardinian) → watch accuracy degrade → quantifies how
  much each witness and the conservative outlier contribute.

## Questions I'd want Fable's take on

1. **Search strategy for stage 5**: constraint-solve-then-refine, evolutionary, MCMC over an
   MDL posterior, or neural sequence model? What's the right first cut that isn't a toy?
2. **Encoding the naturalness prior**: hand-authored typology of sound changes, feature-distance
   proxy, or learn it from the Romance forward cascades we can already run?
3. **Independent vs joint** reconstruction of proto-forms — how much does a shared-inventory
   constraint actually buy, and how hard is it to optimize?
4. **Ordered cascades**: is inducing a _relative chronology_ (rule order) tractable, or should
   v1 restrict to a single unordered rewrite per correspondence and accept the accuracy hit?
5. **Objective weighting**: how to set the fit-vs-simplicity trade-off in the description-length
   cost without hand-tuning per dataset?
6. **Robustness**: real cognate lists carry loans, analogy, and errors — how much does that
   break a naive MDL search, and what's the cheapest guard?
7. **Scope for a first milestone**: what's the smallest end-to-end slice (say, stages 1–3 +
   segment-wise reconstruction, no rule induction) that produces a _measurable_ result on
   Romance and proves the approach is worth the stage-5 investment?

```

```
