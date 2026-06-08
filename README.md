# Fortis

A sound-change engine for diachronic and synchronic phonology. Fortis takes a
user-defined phonology — feature vocabulary, IPA inventory, diacritics, sonority
scale, lexicon, and an ordered set of rules — applies the rules to every word,
and produces a step-by-step derivation trace.

Fortis ships no built-in phonology. Everything is loaded from TOML; the engine
runs whatever inventories and rules you supply.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management

```bash
uv sync
```

## The pipeline

At load time the TOML inventories become a `Project` and each rule's
`definition` string is parsed into a `StructuralDescription`. Then every word
runs through:

```
IPA string
  → segmentation      (Segmenter:   IPA → Sequence)
  → rule application  (RuleMatcher + Applier, rules in time order)
  → rendering         (Renderer:    Sequence → IPA string)
  → derivation trace  (DerivationEngine records each rule that fired)
```

Segmentation is greedy longest-match against the letter and diacritic tables: no
Unicode normalisation, exact code-point matching, and parse errors are surfaced
rather than silently repaired. Round-trip _identity_ (IPA → features → IPA) is
not guaranteed; only round-trip _stability_ is (segmenting and re-rendering
twice yields the same string both times).

## The data model

`model.py` defines the domain types. The one idea to internalise before reading
it: **"feature bundle" is three different things**, kept as three separate types
because a matcher, a piece of data, and a rewrite are genuinely different
operations. All three are feature-keyed maps and differ only in what each
feature maps to:

| Type            | Maps feature →                               | Role                                                     |
| --------------- | -------------------------------------------- | -------------------------------------------------------- |
| `FeatureBundle` | `Value`                                      | concrete data (segments, letters, diacritics)            |
| `PatternBundle` | `PatternSpec` (`ValueSpec`/`AlphaSpec`/…)    | a _matcher_ (rule targets/contexts, sonority predicates) |
| `ResultBundle`  | `ResultSpec` (`ValueAssign`/`AlphaAssign`/…) | a _transform_ (rule results)                             |

The concrete side needs no spec wrapper: a segment has only one way to specify a
feature — a value — so there is no union and nothing to wrap. The pattern and
result sides are unions because a feature can be constrained or rewritten in
several distinct ways. The feature name is the map key, so it never appears
inside a spec.

Layers, top to bottom:

- **Values** — `SingleValue` (`int | None`, where `None` means unspecified),
  `ContourValue` (a tuple of single values), and their union `Value`.
  `make_value` collapses a length-1 contour to a scalar at construction.
- **Vocabulary** — `FeatureDef` and `FeatureSystem`. A feature's `kind` is
  `UNARY` / `BINARY` / `SCALAR`; being a _node_ is not a kind but a geometry
  fact (the feature has children). The only special node behaviour — `none` and
  `α` cascading to children — is handled at apply time from the geometry, not by
  a tag.
- **Segments** — `Segment` is exactly a `FeatureBundle` (no source spelling
  retained); `Sequence` is a frozen tuple of segments.
- **Inventories** — `Letter`, `Diacritic`, `SonorityLevel`, `LexicalEntry`.
- **Rule AST** — a `PatternBundle` maps each feature to a `PatternSpec`
  (`ValueSpec | AlphaSpec`); a `ResultBundle` maps each feature to a
  `ResultSpec` (`ValueAssign | AlphaAssign`); the `Element` union (letters,
  bundles, wildcards, boundaries, the null segment, groups, disjunctions,
  negation, quantifiers, element references); and `StructuralDescription` /
  `Rule`.
- **Output** — `DerivationStep`, `Derivation`, `ValidationError`, and `Project`
  (the loaded root bundling every inventory).

## Architecture

The model (`model.py`) is inert data and imports nothing else in the project.
All behaviour — parsing, matching, rewriting, rendering — lives in separate
stage classes that operate _over_ the model. Three reasons: each algorithm stays
readable in one place; new passes can be added without touching the AST; and the
data layer never depends on the engine. Parsing and matching also need outside
context (the `FeatureSystem`, and for matching a binding `Env`), which a method
on a frozen dataclass has nowhere to take.

Each stage is named for the transformation it performs, so no two share a verb:

| Stage        | Input → Output                                           | Class              | When      |
| ------------ | -------------------------------------------------------- | ------------------ | --------- |
| Segmentation | IPA `str` → `Sequence`                                   | `Segmenter`        | run time  |
| Rule parsing | `definition` str → `StructuralDescription`               | `RuleParser`       | load time |
| Matching     | `(StructuralDescription, Sequence)` → loci `(span, Env)` | `RuleMatcher`      | run time  |
| Application  | `(locus, ResultBundle, Sequence)` → `Sequence`           | `Applier`          | run time  |
| Rendering    | `Sequence` → IPA `str`                                   | `Renderer`         | run time  |
| Derivation   | `(LexicalEntry, rules)` → `Derivation`                   | `DerivationEngine` | run time  |

Only `RuleParser` keeps the word "parse"; the IPA side is _segmentation_, so the
two parse-like steps never get confused. Alongside the stages, **loaders** turn
the TOML files into a `Project` (invoking `RuleParser` at load time), and
**validation** runs as a single collect-all pass that returns every
`ValidationError` at once — the reason the AST is permissive enough to hold
invalid rules.

### The binding environment

Matching is not a plain yes/no test, because a pattern can _bind_. An alpha
variable like `[α back]` records a segment's value on first occurrence; a
reference like `1=[…]` captures the span it matched. `RuleMatcher` threads an
immutable `Env` carrying those bindings, so a single-segment match returns
`Env | None` — the `Env` is "yes, and here is what it learned" — while
element-level matching, nondeterministic because of quantifiers and
disjunctions, yields `(span, Env)` outcomes. `Applier` reads that `Env` whenever
a result recalls a variable (`AlphaAssign`) or a reference (`@1`, as in
metathesis).

## Configuration files

Every inventory is a user-authored TOML file:

| File              | Contents                                |
| ----------------- | --------------------------------------- |
| `features.toml`   | feature vocabulary and geometry         |
| `letters.toml`    | IPA symbol → feature bundle             |
| `diacritics.toml` | diacritic modifications to base bundles |
| `sonorities.toml` | sonority levels and their predicates    |
| `words.toml`      | the lexicon                             |
| `rules.toml`      | the rules                               |

`syllable.toml` is reserved for syllabification (not yet active).

### Value notation

In rules and inventories, a value can be written several ways:

| Value     | Notation                   | Internal |
| --------- | -------------------------- | -------- |
| undefined | `∅`, `none`, `unspecified` | `None`   |
| present   | `+`, `1`, `present`        | `1`      |
| absent    | `-`, `0`, `absent`         | `0`      |
| level     | `n`, label                 | `n`      |

### A rule

Each rule is a TOML table keyed by its id; chronology lives in `time`, not the
header:

```toml
[centumization]
time        = -2000
name        = "Centumization"
description = "Merger of palatovelar and velar plosives"
definition  = "[+cons, +guttural, +coronal] → [cor: none]"
```

Rules sort by `time` ascending, then by file order. The full rule notation
(quantifiers, alpha variables, conditionals, contours, references) lives in the
reference manual.

## Design notes

A few decisions that aren't obvious from the code:

- **The AST is permissive on purpose.** It can represent invalid rules, because
  validation runs as a single collect-all-errors pass (`ValidationError`) and
  needs to _see_ every problem to report it. Making invalid states
  unrepresentable would defeat that.
- **Contours are tuples, not lists** — so bundles stay hashable and a segment
  can't be mutated through an aliased contour.
- **No `ANY` or node sentinels.** A feature omitted from a pattern means "don't
  care"; `ValueSpec(f, None)` means "must be unspecified". Bare `[place]` (a
  unary node named with no value) is just its present value, so it needs no
  special case.
- **Segments carry no spelling.** Rendering reconstructs IPA from features, so
  there is no stored symbol to keep in sync.

## Status

The core data model is complete. Two notation features remain deferred in
`model.py`: conditional features (`ConditionalSpec` / `ConditionalAssign`) and
the presence spec (only needed if a binary or scalar node is ever named bare).
Contour positions are modelled — `ContourEdge` / `ContourPosition` via the
optional `at` field on `ValueSpec` and `AlphaSpec` (target/context only; result
contours must use explicit values).

None of the stage classes exist yet: `Segmenter`, `RuleParser`, `RuleMatcher`,
`Applier`, `Renderer`, `DerivationEngine`, and the TOML loaders are all still to
be written. Syllabification (the `$` boundary and sonority-driven boundary
placement) is designed but not implemented; until it lands, `$` has nothing to
match and rules should not rely on syllable structure.

## Layout

One module per stage; `model.py` is the only piece that exists today.

```
fortis/
  model.py        # domain types (data only)            — done
  loaders.py      # TOML → Project                      — planned
  notation.py     # RuleParser: definition → SD         — planned
  segmenter.py    # Segmenter: IPA → Sequence           — planned
  matcher.py      # RuleMatcher + Env                   — planned
  applier.py      # Applier: rewrite one locus          — planned
  renderer.py     # Renderer: Sequence → IPA            — planned
  engine.py       # DerivationEngine: derive a word     — planned
data/
  features.toml
  letters.toml
  diacritics.toml
  sonorities.toml
  words.toml
  rules.toml
docs/
  reference.md    # the Fortis reference manual
```
