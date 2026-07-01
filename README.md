# Fortis

A diachronic phonology engine. Everything is user-supplied in `projects/default/`
(feature system, letters, diacritics, sonority scale, syllable parameters,
autosegmental tiers, lexicon, sound-change rules); the engine segments each word
into feature bundles, runs it through the rules in chronological order, and prints
a step-by-step derivation with syllable structure. Suprasegmental features (tone,
stress) live on autosegmental tiers, so rules can spread, dock, and delink them,
and a tone survives its vowel's deletion. The reference data models the
development from Proto-Indo-European to Modern English.

Run the derivations — the shipped default is a **feature showcase**, one word-scoped rule per
feature (voicing assimilation, i-umlaut, devoicing, deletion, epenthesis, degemination, tone spread):

```
python -m src.fortis.main
```

Or point it at your own data. `--words FILE` and `--rules FILE` override just the lexicon and
the sound changes (the feature system, letters, sonority, tiers, etc. stay the shipped
defaults); `--project DIR` runs a **project** — a directory whose own files override the
defaults, with any it omits falling back to them, so a project holds only what differs:

```
python -m src.fortis.main --words my_words.toml --rules my_rules.toml
python -m src.fortis.main --project projects/pie_to_english   # PIE → Modern English
```

`--output` writes the run to a Markdown file instead of printing it — the firing-rule trace
plus, for tier operations, an association-change diagram (`│` kept · `╎` added · `╪` delinked).
With no path it lands at `<project>/output.md`:

```
python -m src.fortis.main --project projects/old_chinese --output
```

## How rule matching works

The heart of the engine is deciding _where_ a rule applies in a word. This lives
in `application/matching.py`; `find_matches(rule, segments)` returns one
`Match(start, end, bindings)` for every place the rule fires.

### What a rule looks like, and what a "match" is

A parsed rule (`StructuralDescription`) is `A → B / C _ D // E _ F`:

- **target** `A` — the span that gets rewritten (`segments[start:end]`),
- **result** `B` — what it becomes (used by the _applier_, not during matching),
- **left / right context** `C` / `D` — what must sit immediately before / after the target,
- **left / right exception** `E` / `F` — an environment in which the rule must _not_ fire.

Each part is a sequence of **elements** (`models/elements.py`): a feature bundle
`[+syll]`, a letter, a disjunction `(X|Y)`, a quantified element `X{2}` / `X*`, a
group `(X Y)`, a word/syllable boundary `#` / `$`, a binding `1=X`, a recall `@1`,
a negation `!X`, the wildcard `[]`, or the null segment `∅`.

A **locus** (a match) is a target span where the left context matches _immediately
to its left_, the right context _immediately to its right_, and the exception
environment does _not_ hold around it.

### Three layers

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

### The bindings environment

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

### A worked example

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

## Autosegmental tiers

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
  `docs/change_notation_rules.md` §1.8 and §2.12.
- **Optional** — with no `tiers.toml` the tier machinery never runs; the engine behaves
  exactly as before, so a project that doesn't need tones pays nothing.

Internally a word is a `Form` (`models/form.py`): a list of `Segment`s (a feature bundle plus
a stable id) alongside the tiers. The matcher and renderer read suprasegmentals back through a
transient "lowered" view, so they keep working on plain bundles; `application/tiers.py` holds
the tier operations (associate at construction, prune/OCP cleanup, redock, and the
spread/dock/delink writes).

## Layout

A strict downward dependency DAG — each layer imports only from those above it
(`models` ← `parsing` ← `loaders` ← `application`); `models` is inert data.

```
fortis/
├── projects/
│   ├── default/                 # shipped project — user-authored data, fallback base for all others
│   │   ├── features.toml  letters.csv  diacritics.toml
│   │   ├── sonorities.toml  syllable_parts.toml  tiers.toml
│   │   └── words.toml  rules.toml
│   └── ...                      # other projects, e.g. old_chinese, pie_to_english
├── docs/                        # user_guide, notation reference, feature/rule docs
├── tests/
└── src/fortis/
    ├── config.py                # paths, value symbols, greek alphabet, special symbols
    ├── result.py                # Result / Ok / Err
    ├── main.py                  # load → segment → derive → print the trace
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
    │   ├── project.py           #   Project (every inventory bundled together)
    │   ├── derivation.py        #   DerivationStep, Derivation
    │   ├── segment.py  form.py  #   Segment (bundle + stable id), Form (segments + tiers)
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
    │   ├── diacritics.py  sonorities.py  syllable_parts.py  tiers.py  words.py
    │   ├── rules.py             #   rules.toml (bodies parsed via parsing.notation)
    │   └── project.py           #   load everything    → Project
    │
    └── application/             # THE ENGINE            (depends on: models, parsing, loaders)
        ├── combining.py         #   bundle algebra: combine, merge (node-delink), compare
        ├── matching.py          #   pattern_matches; find_matches (sequence matcher); full_match
        ├── applying.py          #   apply_match: rewrite a matched locus
        ├── syllabifying.py      #   syllabify: sonority + onset/coda-pattern boundaries
        ├── segmentation.py      #   string_to_sequence: IPA → feature bundles
        ├── rendering.py         #   sequence_to_string, render_syllabified, describe_change
        ├── diagram.py           #   render_change/render_autosegmental: tier association diagrams
        ├── tiers.py             #   autosegmental tier ops: associate, cleanup/OCP, redock, spread/dock
        └── deriving.py          #   apply_rule per mode; derive a word → Derivation
```

## License

Licensed under [CC BY-NC 4.0](LICENSE) — free for private and scientific/research
use with attribution; commercial use is not permitted.
