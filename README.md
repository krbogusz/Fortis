# Fortis

A featural, autosegmental phonology engine for diachronic and synchronic use.

The engine is **feature-system agnostic**: the features, their geometry, the segment
inventory and its signs, the lexicon, and the rules are all user-provided data, not built
in. Fortis ships no phonology of its own — the example projects are just sample data.

You can use it in your browser, on desktop and mobile: <https://krbogusz.github.io/Fortis/>.

## What it is

Fortis takes a lexicon and an ordered set of phonological rules and derives,
word by word, every intermediate form from input to surface — recording
exactly which rule fired, what it changed, and why. Words aren't strings that
get pattern-matched character by character; they're sequences of **feature
bundles**, so a rule like "voiceless stops become voiced between vowels" is
written once, over features, and fires on every segment it describes,
regardless of how any particular inventory happens to spell it.

Suprasegmental features (tone, stress) live on **autosegmental tiers**,
linked to their anchor segment by identity rather than baked into it — so a
tone can spread across several vowels, dock onto one after floating free, or
survive the deletion of the vowel that used to carry it, the same way these
processes are described in the phonological literature. Syllable structure is
computed too, not annotated by hand: a sonority scale and (optionally)
onset/coda constraints decide where the boundaries fall, and rules can refer
to them directly.

When the lexicon records the forms a word is *meant* to reach — its attested
final reflex, and optionally its form at intermediate historical stages — Fortis
measures its own output's distance to them: a phone-level and a finer feature-weighted
edit distance, per stage and for the final surface, so a rule set's accuracy can
be tracked as it is built.

Fortis makes no distinction between "historical sound change" and
"synchronic phonology" — both are an ordered set of rules applied over
time; whether that time span is three millennia or a single derivation is
determined entirely by what you put in `rules.toml`. The repository
includes five example projects: a **feature showcase** (one rule per
mechanism), **Proto-Indo-European → Proto-Germanic**, **Latin → Modern
French**, the **Halle-Vaux-Wolfe feature geometry** (autosegmental
spreading phenomena), and a flat **SPE** feature matrix (demonstrating
that the engine requires no feature geometry at all).

## Design philosophy

- Every inventory — the feature vocabulary and its geometry, the IPA letters,
  the diacritics, the sonority scale, the syllable structure, the
  autosegmental tiers, the lexicon, and the rules — is user-authored data
  loaded at run time; none of it is hardcoded. The engine itself only
  implements the general mechanisms (feature bundles, structural rule
  matching, autosegmental association, syllabification) that such a system
  needs, not a specific language or phonological theory.

- `projects/default` (the shipped feature showcase) is treated as an
  ordinary project rather than a special case, which is why it lives under
  `projects/` instead of at the repo root. A project supplies only the
  files that differ from the default; whatever it omits falls back, so the
  same mechanism that runs the shipped showcase runs a project that
  overrides one file or a project that overrides all of them. That default
  project does ship with its own feature system, letter inventory,
  diacritics, sonority scale, and syllable structure, described in detail
  in [`docs/default_system.md`](docs/default_system.md) — a starting point
  to build from or override, not a fixed part of the engine.

- The codebase is organized as a one-way dependency DAG — `models` (inert
  data) ← `parsing` ← `loaders` ← `application` (the engine) — and each
  layer may only import from those before it. That constraint is enforced
  by what's importable, not just documented (see [Layout](#layout)).

- Rule notation is validated at load time, and every problem in a file is
  collected and reported together rather than stopping at the first one
  found. A rule whose result feature-bundle has no unambiguous target to
  merge with (§5.1 of the user guide) is surfaced as an error rather than
  resolved silently; an unsyllabifiable cluster, by contrast, is a
  *warning* — it falls back to a sonority-driven division and derivation
  continues (§7).

- Autosegmental tiers, onset/coda constraints, and a custom sonority scale
  are all optional. Without a `tiers.toml`, the tier machinery doesn't run
  at all, so a project with no tone or stress carries no runtime cost from
  the mechanism that would support them.

## Using it

### Command line

Run the derivations — the shipped default is a **feature showcase**, one word-scoped rule per
mechanism (voicing assimilation, i-umlaut, devoicing, deletion, epenthesis, degemination, tone spread):

```
python -m src.fortis.main
```

Or point it at your own data. `--words FILE` and `--rules FILE` override just the lexicon and
the sound changes (the feature system, letters, sonority, tiers, etc. stay the shipped
defaults); `--project DIR` runs a **project** — a directory whose own files override the
defaults, with any it omits falling back to them, so a project holds only what differs:

```
python -m src.fortis.main --words my_words.toml --rules my_rules.toml
python -m src.fortis.main --project projects/pie_to_english    # PIE → Present-Day English
```

The lexicon, the rule list, the diacritics, and the sonority scale may each be written in
**either TOML or CSV** — the two are equally valid encodings of the same schema, and the loader
dispatches on the file extension (so `--words my_words.csv` or a project carrying `rules.csv`
works exactly like the TOML form). If a project happens to carry both formats of a file, the
TOML is used. The feature system, tiers, and syllable parameters are TOML-only, since they nest.
See `docs/user_guide.md` §4.1–§4.2 for the CSV schemas.

Every run also writes reports into a `reports/` subfolder of the project: the
main one is `derivations.csv`, a long-format trace with one row per word × firing
rule (columns `word, rule, t, before, after, change`), each word bookended by two
synthetic rules — `input` (its raw IPA and how the engine ingested it: syllabified,
normalised) and `output` (the surface form). Alongside it, `derivation_matrix.csv`
gives the wide view (one row per word and one column per rule — each titled
`<time>: <rule>` — holding the word's resulting form wherever that rule fired,
empty otherwise), and `rule_firings.csv` inverts it (one row per rule: the distinct
segment changes it made, e.g. `d→t`, the words it matched as `before → after`, and a
`sporadic` column naming any word scope). `rule_dependencies.html` is the rule feeding
graph — which rule's output segment feeds which rule's input, read off the actual
firings — as a scrollable, time-columned view.
The optional `--autosegmental` flag additionally writes `autosegmental.md`, one
canonical rule diagram per rule that spreads, docks, or delinks — a feature-geometry
tree for a segmental node-spread (place assimilation) and Goldsmith's tonal notation
for a tier change — with the spreading association dashed (`┊`) and the delinked one
struck (`╪`/`⧧`). Rules that merely rewrite a feature in place are not drawn.
If the lexicon carries attested forms (`final` and/or
intermediate `stages`), four more analyses run over it: the **accuracy**
analysis writes `accuracy.csv` (per-stage exact-match accuracy + mean phone
and feature distance, plus token-weighted columns when the lexicon carries word
frequencies) and `distance_to_target.csv` (per-word); the **errors**
analysis writes `errors.csv` (which segments came out wrong, per stage) and the
**error context** analysis `error_context.csv` (the attested-form environments most
associated with each error, per stage and segment); and `blame.csv` records every
assessed word's per-step distance trajectory, worst first (see
[Diagnosing a rule set](#diagnosing-a-rule-set)). A run ends with a one-line
summary on stderr — words derived, rules applied, per-phase timing, files saved —
and shows a progress bar while deriving in a terminal. All reports land in
`<project>/reports/`; `--output` overrides the main report's path (the others
follow into the same directory):

```
python -m src.fortis.main --project projects/latin_to_french --output /tmp/run/derivations.csv
```

Deriving one word never touches another, so a large lexicon is fanned across worker
processes **automatically** — a ~4–6× speedup on a multi-core machine, with output
byte-identical to a serial run. Small lexica stay in a single process (the pool's
startup cost is not worth paying below a couple hundred words). Pass `--serial` to
force one process, or `--workers N` to pin the pool size.

The `--lint` flag runs a static check over the rules instead of deriving: it flags any
rule position whose feature bundle can never match a segment — a feature required present
under a geometry node required absent, e.g. `[front, oral: none]` (`front` sits under
`oral`, so no segment can satisfy both). It has no thresholds and no false positives, and
exits non-zero when it finds one, so it works as a CI gate. (The shipped feature showcase
deliberately carries one such rule — `contradictory_bundle` — as its demo of this check,
so `--lint` on the default project reports exactly that finding.)

```
python -m src.fortis.main --project projects/latin_to_french --lint
```

`--single WORD` derives just one word instead of the whole project — looked up in the
lexicon by its IPA key or gloss (so it carries any attested targets), or derived bare if
absent — printing a compact summary and writing the same reports prefixed `single_`
(`single_derivations.csv` always; `single_accuracy.csv`, `single_errors.csv`, … when the
word has a target).

### Web app

**Live: <https://krbogusz.github.io/Fortis/>** — no install; it runs entirely in your
browser.

`web/` is a browser front end that runs the same Python engine used by the CLI —
compiled to WebAssembly and executed in-browser via [Pyodide](https://pyodide.org),
rather than a separate JavaScript reimplementation. Every project in `projects/` is
auto-discovered into the picker (or load your own); edit any inventory file and the
derivations re-run in a trace view. Each derivation card carries a **Definitions**
toggle (the rule bodies) and — for a word touched by a rule that spreads, docks, or
delinks — a **Graph** toggle that draws the same autosegmental diagram as
`--autosegmental` inline. Result tabs (**Rules**, **Tree**, **Matrix**, **Accuracy**,
**Errors**, **Context**, **Blame**) score and analyse the run against the lexicon's
attested forms when it has them, and a **Single** tab derives one word on demand (the
web counterpart of the CLI's `--single`). A **Diagnostics** pane sits alongside results,
in three tabs: **Warnings** collects every finding from the last run — rule positions
whose bundle can never match (a feature required present under a node required absent),
never-firing rules, and syllabification fallbacks; **Classes** matches a feature bundle
with the engine's own matcher against the current inventory — so you can see the real
reach of a class (e.g. that `[+front]` also picks out every coronal); and **System**
draws the feature geometry as a tree, exactly as the engine loads it. The layout is
responsive down to a phone. See
[`web/README.md`](web/README.md) for the full picture, including the type scale and
theming. To run it locally:

```
cd web
npm install
npm run dev
```

### Accuracy against attested forms

A lexicon entry may record the form the engine should reproduce — its `final`
reflex, and optionally its form at intermediate historical `stages` keyed by rule
time. Both the table form (with targets) and the bare `word = "gloss"` form
(unassessed) are accepted:

```toml
"ˈɑmɑt" = {gloss = "aime", final = "ɛm", 600 = "ˈãj̃məθ", 1400 = "ɛm"}
"tag"   = "final devoicing"
```

Each derived form is compared to its target with two edit distances: a **phone**
distance (a base segment plus its combining marks is one phone; an exact match is
0) and a finer **feature** distance (a substitution costs the number of features
that differ, so `ɑ̃` is one edit from `ɑ` but eleven from `t`; an adjacent-swap
metathesis counts as one). Both are reported per word and in aggregate, per stage
and for the final surface, in `accuracy.csv` / `distance_to_target.csv` — written on
every run that has attested forms.

Intermediate `stages` are measured by matching the derived snapshot at rule-time T
against the attested form at stage T, so those rows are only meaningful when the
rule times are calibrated to the stage timescale — the `final` score never
depends on that alignment.

### Diagnosing a rule set

Accuracy says _how_ wrong a derivation is; three further analyses say _what_ and
_where_, all from the same attested targets and written on every run when the
lexicon has them:

- **`errors.csv`** — per attested stage (and the final), a ranked tally of the phone
  confusions (which target phone came out as which, with count, kind, and examples).
- **`error_context.csv`** — per stage and per erroring segment, a **context autopsy**:
  the attested-form environments most associated with getting that segment wrong (by
  phi coefficient), with F₁ and the raw err/ok counts with vs. without each environment.
- **`blame.csv`** — every assessed word's per-step distance trajectory (columns
  `gloss, step, regression, t, form, target, d, fd`), worst first, exact words included. The
  interactive Blame tab additionally attributes each wrong phone (by stable segment
  id) to the rule that last set it.

The thresholds these analyses use (the autopsy's support floor, how many phones
to autopsy, the edit distance's metathesis cost) are tunable per project in an
optional `settings.toml`; a project that omits it, or any key, gets the built-in
defaults.

## How it works

### Rule matching

The central problem the engine solves is deciding _where_ a rule applies in a
word. This lives in `application/matching.py`; `find_matches(rule, segments)` returns one
`Match(start, end, bindings)` for every place the rule fires.

#### What a rule looks like, and what a "match" is

A parsed rule (`StructuralDescription`) is `A → B / C _ D // E _ F`:

- **target** `A` — the span that gets rewritten (`segments[start:end]`),
- **result** `B` — what it becomes (used by the _applier_, not during matching),
- **left / right context** `C` / `D` — what must sit immediately before / after the target,
- **left / right exception** `E` / `F` — an environment in which the rule must _not_ fire.

Each part is a sequence of **elements** (`models/elements.py`): a feature bundle
`[+syll]`, a letter, a disjunction `(X|Y)`, a quantified element `X{2}` / `X*`, a
group `(X Y)`, a word/syllable boundary `#` / `$`, a binding `1=X`, a recall `@1`,
a negation `!X`, the wildcard `[]`, or the null segment `∅`. The full notation
reference lives in [`docs/user_guide.md`](docs/user_guide.md) §5.

A **locus** (a match) is a target span where the left context matches _immediately
to its left_, the right context _immediately to its right_, and the exception
environment does _not_ hold around it.

#### Three layers

**1. The leaf — does one pattern match one segment?** `pattern_matches(pattern,
segment)` walks the pattern's features. Each feature the pattern names must be
present in the segment with a compatible value; a feature it doesn't name is
unconstrained. The corner cases: `[F: none]` matches an _absent_ feature, `[F:
!val]` matches absence too, a bare concrete value fails against absence. A
**syllable-tier** feature (tone, stress) is tested against the segment's syllable
nucleus rather than the segment. A **conditional** feature `[<n: F>]` never
filters — it records whether its condition held, for the applier to gate the
paired result feature. **Alpha** features (`αF`) resolve against the bindings.

**2. The sequence matcher — does a run of elements match here?** `_match_element`
takes one element and is a _generator_: it yields every `(end_position, bindings)`
that element could produce, because one element can match in several ways.
`_match_sequence` chains them — match the first element, then from each resulting
position recurse on the rest. So matching is a **backtracking search**: a `[-syll]*`
may consume 0, 1, 2… segments and every alternative is explored until the whole
sequence fits. The element cases:

- a bundle / letter / `[]` consumes one segment if it matches;
- `(X|Y)` tries each branch (recording which one matched, so the applier can pick
  the paired result branch);
- `X{m,n}` is **greedy** — `_match_repeat` tries the most repetitions first;
- `(X Y)` splices its sub-sequence inline;
- `#` / `$` are **zero-width assertions** — they consume nothing and just check the
  position is a word edge / syllable boundary;
- `1=X` binds reference _1_ to the whole span `X` matched; `@1` replays it (the
  captured segments must re-match here, exactly);
- `!X` matches one segment that `X` does _not_ match;
- `∅` is a zero-width insertion point.

**3. The locus search — `find_matches`, in two passes.** Two passes are needed
because some bindings must be discovered before others can be checked:

- **Pass 1 — fix the span.** For each start position, match the **target alone**,
  _alpha-blind_ (alpha matches everything and binds nothing). This pins the
  candidate target spans and captures the target's reference bindings without
  committing alpha. The greediest fully-valid parse at each start wins.
- **Pass 2 — `_locate`, check the environment.** For a candidate `(start, end)`
  span: pre-seed the **right context's** references (so a recall to their left can
  resolve — references are scope-based, not left-to-right), then evaluate left
  context (matched _ending at_ `start`) → target (re-matched over exactly `[start,
end)`) → right context (matched _starting at_ `end`) → the deferred-`!α` check →
  the exception. If all hold, return the `Match`.

The contexts float against the target: the left context's right edge is anchored
at `start` while its left edge slides (`_match_ending_at`), the right context's
left edge is anchored at `end` (`_match_starting_at`). The exception uses the same
two anchored matches — if an exception-left _and_ an exception-right both match, the
locus is **blocked**.

#### The bindings environment

A `Bindings` (`models/bindings.py`) is threaded through the whole search:

- **references** (`n=` / `@n`) — _scope-based_: the target's bindings (pass 1) and
  the right context's (pre-seeded in pass 2) are captured first, so a recall
  resolves wherever it sits. A binding captures its whole matched span (one segment,
  or several for a group `1=([X][Y])`); a recall replays it segment-for-segment.
- **alpha** (`α`, `β`) — _order-independent value agreement_: each occurrence's op
  (`α` same, `-α` opposite, `!α` other) states how its position relates to `α`, and
  the rule fires under any consistent assignment.
- **conditions** — per-label truth of conditional features, AND-accumulated.
- plus the disjunction branch taken and any deferred `!α` constraints.

#### A worked example

Rule `[+syll] → [+nasal] / [+nasal] _` ("a vowel nasalises after a nasal"), word
`ana` = `[a, n, a]`:

1. Pass 1 scans start positions. The target `[+syll]` matches `a` at 0 → span
   `[0,1)`, and `a` at 2 → span `[2,3)`.
2. `_locate` on `[0,1)`: the left context `[+nasal]` must match _ending at_ 0 —
   there is nothing before position 0 → no match → rejected.
3. `_locate` on `[2,3)`: the left context `[+nasal]` ending at 2 is segment 1, `n`
   — a nasal → matches; the right context is empty; no exception → **locus at
   `[2,3)`**.

So `find_matches` returns one match, on the final `a`. The applier then rewrites
just that span; `deriving.py` splices the result back and moves to the next rule.

### Autosegmental tiers

A feature declared on a tier (`projects/default/tiers.toml`) — e.g. `tone` or `stress` — lives
not in the segment's feature bundle but as an **autosegment** on a separate tier, linked to
its anchor segment by identity. That identity link is what makes classic autosegmental
behaviour fall out:

- **Stability** — the link is to a segment _id_, so when a rule deletes that segment the
  autosegment survives as _floating_; a **melody** tier (`melody = true`, e.g. tone) carries
  it onto the surviving neighbour and re-docks it, so a tone outlives its vowel. A **metrical**
  tier (`melody = false`, e.g. stress) stays put.
- **Spread / dock / delink** — rules link one autosegment to many anchors (`~n`), dock a
  floating autosegment (`⟨…⟩`) onto an anchor, or remove an association (`tone: none`). See
  `docs/user_guide.md` §5.12.
- **Optional** — with no `tiers.toml` the tier machinery never runs; the engine behaves
  exactly as before, so a project that doesn't need tones pays nothing.

The same `~n` recall works on a **segmental geometry node**, where it copies that node's whole
subtree: `[+nasal] → [oral: ~1] / _ [+consonantal, oral: ~1]` is place assimilation (the nasal
takes the following consonant's whole place). Plain `~n` matches only a source that _has_ the
node; `~n?` is *presence-optional* (it also matches — and spreads — an absent node, so
`[back: ~1?, front: ~2?]` copies backness both ways); and `~n=value` is a *bind-and-match* that
binds only a source of that value (`high: ~1=-` binds a `[-high]` vowel, stepping over transparent
`[+high]` ones). Both kinds of change — tier and segmental — render as a single autosegmental rule
diagram in the CLI's `--autosegmental` report and the web app's **Graph** view. The
`projects/halle_vaux_wolfe` project is a showcase: the Halle-Vaux-Wolfe (2000) feature geometry
with place assimilation, Irish dorsal assimilation, Uyghur raising, Sibe uvularization, and more.
See `docs/user_guide.md` §5.12.

Internally a word is a `Form` (`models/form.py`): a list of `Segment`s (a feature bundle plus
a stable id) alongside the tiers. The matcher and renderer read suprasegmentals back through a
transient "lowered" view, so they keep working on plain bundles; `application/tiers.py` holds
the tier operations (associate at construction, prune/OCP cleanup, redock, and the
spread/dock/delink writes).

### Syllabification

Syllable boundaries are computed, not annotated — run on the input and refreshed before every
rule that uses the `$` assertion, so `$` always reflects the current structure. Nuclei are
identified from `syllable_parts.toml`; between each adjacent pair, the intervening consonants
default to a sonority-driven Maximal Onset division, or — if `syllable_parts.toml` defines
onset/coda patterns — the longest pattern-legal split wins instead, which can license clusters
sonority alone wouldn't (e.g. _s_+stop onsets). See §7 of
[`docs/user_guide.md`](docs/user_guide.md) for the full account.

## Layout

A strict downward dependency DAG — each layer imports only from those above it
(`models` ← `parsing` ← `loaders` ← `application`); `models` is inert data.

```
fortis/
├── projects/
│   ├── default/                 # shipped project — user-authored data, fallback base for all others
│   │   ├── features.toml  letters.csv  diacritics.toml   # words/rules/diacritics/sonorities may
│   │   ├── sonorities.toml  syllable_parts.toml  tiers.toml   # equally be given as .csv (TOML default)
│   │   └── words.toml  rules.toml  settings.toml   # settings.toml: tunable analysis params (optional)
│   └── ...                      # other projects, e.g. latin_to_french, pie_to_english
├── docs/                        # user_guide.md (full reference), default_system.md (the shipped inventory)
├── web/                         # browser playground (Pyodide) — see web/README.md
├── tests/
└── src/fortis/
    ├── config.py                # paths, value symbols, greek alphabet, special symbols
    ├── result.py                # Result / Ok / Err
    ├── main.py                  # load → derive → write reports (derivations + accuracy/errors/blame CSVs) → run summary
    │
    ├── general/                 # generic helpers, zero domain knowledge
    │   ├── file_handling.py     #   load_toml_file, load_csv_file
    │   ├── presenting.py        #   symbol presentation helpers
    │   └── utils.py             #   safe_int, ...
    │
    ├── models/                  # INERT DATA — imports only stdlib + within models
    │   ├── values.py            #   Value, AlphaRef, AlphaOp, ContourEdge, contours
    │   ├── tiers.py             #   Tier
    │   ├── specs.py             #   FeatureSpec, PatternSpec, ResultSpec
    │   ├── bundles.py           #   FeatureBundle, PatternBundle, ResultBundle
    │   ├── bindings.py          #   Bindings (alpha + element-ref state)
    │   ├── elements.py          #   Element union (LetterRef, Group, Quantified, $, …)
    │   ├── rules.py             #   ApplicationMode, StructuralDescription, Rule, RuleInventory
    │   ├── features.py          #   FeatureKind, Feature, FeatureInventory
    │   ├── inventories.py       #   Letter/Diacritic/Sonority/SyllablePart/Word + inventories
    │   ├── settings.py          #   Settings (tunable analysis parameters, from settings.toml)
    │   ├── project.py           #   Project (every inventory bundled together)
    │   ├── derivation.py        #   DerivationStep, Derivation
    │   ├── segment.py  form.py  #   Segment (bundle + stable id), Form (segments + tiers)
    │   ├── syllable.py          #   Syllable (computed onset/nucleus/coda view — never stored)
    │   ├── autosegment.py       #   Autoseg, AutosegmentalTier (the tier representation)
    │   └── tier_declaration.py  #   TierDeclaration, TierInventory (from tiers.toml)
    │
    ├── parsing/                 # STRING → models       (depends on: models)
    │   ├── lexer.py             #   tokenise rule notation
    │   ├── bundles.py           #   parse_value, parse_*_spec, parse_*_bundle
    │   ├── notation.py          #   parse_definition / parse_sequence → Elements
    │   └── rule_validation.py   #   structural validation of a parsed rule
    │
    ├── loaders/                 # FILE → models         (depends on: models, parsing)
    │   ├── features.py          #   features.toml      → FeatureInventory
    │   ├── letters.py           #   letters.csv        → LetterInventory
    │   ├── diacritics.py  sonorities.py  syllable_parts.py  tiers.py  words.py  settings.py
    │   ├── rules.py             #   rules.toml (bodies parsed via parsing.notation)
    │   └── project.py           #   load everything    → Project
    │
    ├── application/             # THE ENGINE            (depends on: models, parsing, loaders)
    │   ├── combining.py         #   bundle algebra: combine, merge (node-delink), compare
    │   ├── matching.py          #   pattern_matches; find_matches (sequence matcher); full_match
    │   ├── applying.py          #   apply_match: rewrite a matched locus
    │   ├── syllabifying.py      #   syllabify: sonority + onset/coda-pattern boundaries
    │   ├── segmentation.py      #   string_to_sequence: IPA → feature bundles
    │   ├── rendering.py         #   sequence_to_string, render_syllabified; render_residue → �
    │   ├── tiers.py             #   autosegmental tier ops: associate, cleanup/OCP, redock, spread/dock
    │   └── deriving.py          #   apply_rule per mode; derive_all → [Derivation]; form_at_time
    │
    └── analysis/                # OUTPUT ANALYSIS       (depends on: models, application)
        ├── accuracy.py          #   phone + feature edit distance vs attested targets (on BUNDLES)
        ├── diagnosis.py         #   per-stage confusions (errors) + per-segment context autopsy
        ├── dependencies.py      #   firing-based rule feeding graph → rule_dependencies.html
        ├── blame.py             #   attribute each wrong word to the rule that produced it
        ├── warnings.py          #   what the engine did silently: unspellable segments (�),
        │                        #   syllabification fallbacks → warnings.md
        └── reporting.py         #   render the accuracy CSVs (per-stage summary + per-word)
```

## Current limitations and future directions

- **Deterministic only.** A rule either fires everywhere its structural
  description matches, or is restricted to specific words via `words`;
  there's no notion of a rule applying only some of the time (sporadic or
  gradient change beyond that word-level restriction).
- **Limited morphological structure.** The lexicon is a flat list of
  IPA/gloss pairs. A morpheme boundary (`-`) *is* a first-class, rule-editable
  segment — it steers syllabification and blocks adjacency (§5.2 of the user
  guide) — but there's no affixation or reduplication machinery, so an
  affix-conditioned process or a reduplicative copy of a span isn't directly
  expressible.
- **Round-trip identity isn't guaranteed.** Only round-trip _stability_ is
  (parsing and re-rendering a form twice yields the same string both
  times) — an inventory's letters and diacritics may not spell a derived
  form back exactly as it was first typed.
- **No cross-project or typological validation.** Nothing checks a
  project's feature system against an external phonological inventory
  database, or against another project's; consistency across projects is
  the author's responsibility.
- **Rule-based, not constraint-based.** Fortis models sound change as
  ordered rewrite rules (SPE/autosegmental style); there's no
  Optimality-Theoretic ranking or violation-tableau mode.
- **The browser engine is slow relative to the CLI.** Pyodide runs real
  CPython compiled to WASM, which is meaningfully slower than native
  CPython — deriving a few dozen words can take tens of seconds in the
  browser versus a fraction of a second from the command line.
- **The web app has no persistence layer.** A loaded project lives only in
  that browser tab's memory; there's no save-to-cloud, sharing, or
  multi-user collaboration, only per-file download.

None of these are commitments, but plausible directions if the project
grows: richer (weighted or optional) rule application for gradient change,
richer morphological structure (beyond the morpheme boundary) to support
reduplication and affix-conditioned rules, metrical foot structure alongside the existing
tone/stress tiers, further accuracy work (attribution of errors to morphological
analogy rather than sound change — the segmental confusion diagnosis, per-stage
divergence, rule-level blame, and token-weighted accuracy under
[Diagnosing a rule set](#diagnosing-a-rule-set) are already in place), and
performance work on the browser build if it becomes more than a demo/playground.

## License

Licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE) — free for any
noncommercial purpose, including personal study, hobby projects, and use by educational
institutions, public research organizations, and other nonprofits (whatever their funding);
commercial use is not permitted. Keep the copyright notice with any copy you pass on.
Note that the Latin → French rule and lexicon data is derived from GPL-3.0 material
(see Acknowledgements) and carries that licence.

## Acknowledgements

The engine is original, but the `projects/latin_to_french` example and its accuracy dataset
draw on external work — full details, uses, and licences are in
[docs/acknowledgements.md](docs/acknowledgements.md). In brief:

- **Latin → French** — the rule cascade is a hand re-authoring, in Fortis notation, of the
  **DiaCLEF2025** cascade from [**DiaSim**](https://github.com/clmarr/DiaSim) (Marr &
  Mortensen; **GPL-3.0**); the per-stage accuracy targets in `words.csv` come from DiaSim's
  attested **FLLAPS**/FLLexPlus datasets (also GPL-3.0). See
  [`SOURCE.md`](projects/latin_to_french/SOURCE.md). Because it derives from GPL-3.0 data,
  treat the Latin → French rules/lexicon as GPL-3.0, separately from the engine's licence below.
- **Word frequencies** — [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords)
  (MIT), from OpenSubtitles 2018 via [OPUS](https://opus.nlpl.eu/).
- **Feature geometry (halle_vaux_wolfe project)** — the geometry and the phenomena it showcases
  are after Halle, Vaux & Wolfe (2000), _On Feature Spreading and the Representation of Place of
  Articulation_, *Linguistic Inquiry* 31:387–444. The inventory and rules are an original
  illustration, not the paper's data. See [`SOURCE.md`](projects/halle_vaux_wolfe/SOURCE.md).
- **SPE feature matrix (spe project)** — the flat binary feature system is after Chomsky &
  Halle (1968), *The Sound Pattern of English*. The inventory and rules are an original
  illustration, not the book's data. See [`SOURCE.md`](projects/spe/SOURCE.md).

## A note on generative AI

This project was developed with use of generative AI (Claude Code) as a coding assistant,
under the direction and review of the author.
