# Fortis Reference Manual

Fortis is a sound change engine for diachronic and synchronic phonology. It takes a lexicon and an ordered set of phonological rules, applies those rules to every word in the lexicon, and produces a derivation trace showing each intermediate form and the rule responsible for each change.

Everything Fortis works with is **user-defined and imported from plain-text TOML and CSV files**: the feature vocabulary, the IPA letters, the diacritics, the sonority scale, the syllable parameters, the lexicon, and the rules. Fortis ships no built-in phonology; it is an engine that runs whatever inventories and rules you supply.

---

## Table of Contents

1. [Overview](#1-overview)
2. [The Pipeline](#2-the-pipeline)
3. [The Feature System](#3-the-feature-system)
4. [Configuration Files](#4-configuration-files)
5. [Rule Notation Reference](#5-rule-notation-reference)
6. [Rule Application Semantics](#6-rule-application-semantics)
7. [Syllabification](#7-syllabification)
8. [Derivation and Output](#8-derivation-and-output)
9. [Validation](#9-validation)

---

## 1. Overview

Fortis models sound change as an ordered sequence of rewrite rules applied to phonological representations. The core abstraction is a **sequence** — an ordered list of segments, each represented as a bundle of phonological features. Rules pattern-match against sequences and rewrite matched portions according to a structural change.

The engine supports both **diachronic** use (historical sound change, where rules are ordered by time and applied in chronological order) and **synchronic** use (phonological derivations, where rules interact via feeding and bleeding). The distinction is one of how you organise your rule file, not a difference in how the engine works.

---

## 2. The Pipeline

A word passes through the following stages in order:

```
IPA string
    │
    ▼
Segmentation & parsing  (IPA → sequence of feature bundles)
    │
    ▼
Rule application  (rules in time order)
    │
    ▼
Rendering  (sequence → IPA string)
    │
    ▼
Derivation trace
```

### 2.1 Segmentation and parsing

The parser consumes an IPA string left to right using greedy longest-match tokenisation against the user-defined inventories. At each position it first consumes any **preposed** diacritics (those declared `kind = "before"` in `diacritics.toml`, e.g. the stress marks `ˈ`/`ˌ`), buffering them for the base to come; then it takes the longest substring that matches a letter in `letters.csv`; then it consumes any following (`"after"`/`"combining"`) diacritics, buffering all of them onto that base and applying their feature modifications. The result is a `Form` — an ordered list of `Segment` objects, each carrying a complete `FeatureBundle`, alongside any autosegmental tiers (§5.12).

The letter and diacritic tables are the sole authority on how a string is divided. There is no Unicode normalisation step: Fortis matches the code points exactly as written, against the entries exactly as the user authored them. If a string contains a substring that matches no letter (and no diacritic on a preceding base), that is a parse error, surfaced to the user rather than silently repaired — so the inventory and the lexicon must be written in the same form.

Round-trip identity (IPA → features → IPA) is not guaranteed and should not be assumed. The correct invariant is round-trip **stability**: parsing and re-rendering a form twice yields the same string both times.

### 2.2 Rule application

Rules are applied in time order. Rules sharing a time fire in the order they appear in the file. See §6 for full semantics.

### 2.3 Rendering

The final sequence is converted back to an IPA string by looking up each segment's feature bundle against the letter inventory and emitting the canonical IPA symbol plus whatever diacritics are needed to recover the full specification.

---

## 3. The Feature System

The feature vocabulary and its geometry are defined entirely by the user in `features.toml`. Fortis imposes no fixed feature set.

### 3.1 Feature bundles

The basic building block of the whole engine is the feature bundle — a set of feature–value pairs. Features may be defined as unary, binary and scalar.

Below is the table displaying which values different types of features can take, with `+` meaning the feature type can take this value, and `-` not.

| Value\Feature | Unary | Binary | Scalar |
| ------------- | ----- | ------ | ------ |
| Undefined     | +     | +      | +      |
| Present       | +     | +      | -      |
| Absent        | -     | +      | -      |
| Level         | -     | -      | +      |

**Undefined applies to every feature, not only unary ones.** Any feature — binary, unary, or scalar — can be marked unspecified with the value `none`. For example, `[cor: none]` removes the coronal specification entirely; this is distinct from `[−cor]`, which specifies a negative value. Both differ from a feature simply being absent from a bundle: in a concrete segment an absent feature is unspecified (equivalent to none), but in a pattern an absent feature is unconstrained — it places no condition on the segment, whereas [cor: none] requires the segment to be unspecified for coronal. Within a single bundle, each feature may be specified at most once — a repeat (`[aperture: high, aperture: low]`) is a parse error, not a silent last-wins.

### 3.2 Feature specification

A feature specification is a single feature-value pairing. It can be simple, or it can be contour. A contour is an ordered list of single values.

A contour for a feature can be of any length and can take any type of value that is correct for its feature type. Contours are specified using the notation for the appropriate value/feature type, separated by `>`.

Values in rules and inventories can be specified in a number of ways, depending on their type.

| Value     | Notation                   | Internal representation |
| --------- | -------------------------- | ----------------------- |
| Undefined | `∅`, `none`, `unspecified` | `None`                  |
| Present   | `+`, `1`, `present`        | 1                       |
| Absent    | `-`, `0`, `absent`         | 0                       |
| Level     | `n`, `label`               | n                       |

### 3.3 Feature geometry

Features may be organised hierarchically. A **parent node** dominates a set of child features. Setting a parent to `none` simultaneously unspecifies all of its children. Binding an alpha variable to a parent (see §5.6) binds all of its children simultaneously.

Referencing a parent node with no value — e.g. `[place]` — matches any segment that has that node specified, regardless of which children are set.

`[node: none]` denotes a **delinked node**: the node and all its children become unspecified at once. This is the canonical representation of debuccalisation (a placeless, glottal segment).

### 3.4 Sonority

The sonority scale is user-defined in `sonorities.toml` (or `sonorities.csv` — columns `name, level, bundle`, in first-match row order), both in the number of levels and in the feature predicates that assign segments to them. Levels are assigned by first-match against an ordered list of predicates. A typical scale might look like:

| Level | Class      |
| ----- | ---------- |
| 7     | Vowels     |
| 6     | Glides     |
| 5     | Rhotics    |
| 4     | Laterals   |
| 3     | Nasals     |
| 2     | Fricatives |
| 1     | Stops      |

but the number of levels, their ordering, and the predicates are all yours to define. Sonority feeds syllabification (§7): it drives the default onset/coda division by the Maximal Onset Principle.

---

## 4. Configuration Files

Every inventory Fortis uses is loaded from a file. All of them are user-authored.

| File                  | Contents                                            |
| --------------------- | --------------------------------------------------- |
| `features.toml`       | The feature vocabulary and geometry                 |
| `letters.csv`         | IPA symbol → feature bundle mappings                |
| `diacritics.toml`     | Diacritic modifications to base segment bundles     |
| `sonorities.toml`     | Sonority levels and the predicates that assign them |
| `syllable_parts.toml` | Onset/nucleus/coda constraints, keyed by time       |
| `tiers.toml`          | Autosegmental tier declarations (e.g. tone, stress; §4.3)|
| `words.toml`          | The lexicon                                         |
| `rules.toml`          | Phonological rules                                  |
| `settings.toml`       | Tunable analysis thresholds (optional; §8.3)        |

**TOML and CSV are equally valid.** Four of these inventories — the lexicon (`words`), the
rules (`rules`), the diacritics (`diacritics`), and the sonority scale (`sonorities`) — may be
supplied in **either** format, chosen by the file's extension; the CSV form carries the exact
same schema as the TOML form (§4.1–§4.2 give the two lexicon/rule schemas; the diacritic and
sonority CSVs simply put each TOML field in a named column). The letter inventory is CSV
(`letters.csv`); the feature system, tiers, and syllable parameters are TOML, since they nest.
If a project carries both formats of the same inventory, the TOML is used.

`syllable_parts.toml` supplies the **nucleus** definition (a feature pattern that
identifies syllable peaks) and, optionally, **onset**/**coda** patterns that
constrain the division (§7). Each part's `definition` is the relevant notation:
a single-segment bundle for the nucleus, an element sequence for an onset or coda
(e.g. `definition = "[+cons][-syll, -cons]?"`).

### 4.1 The lexicon — `words.toml` / `words.csv`

The lexicon is given in TOML or CSV (equally valid — see the **CSV form** at the end of this
section). In the TOML form, each entry's key is an IPA string; its value is either a **gloss string** or a
**table**. The table form adds optional *target* annotations — attested forms the
derivation is measured against (§8.3): `final`, the attested surface form, and any
number of integer-keyed `stages`, the attested form at that derivation `time`.

```toml
# Words for testing phonological derivation.
"xenti"     = "in front"                        # gloss only
"mexteːr"   = "mother"
"bʱleɣʷmoː" = "flower"
"ˈɑmɑt"     = {gloss = "loves", final = "ɛm",   # gloss + attested targets
               600 = "ˈãj̃məθ", 1400 = "ɛm"}
```

Only the IPA key feeds derivation; `final` and `stages` are ignored by the engine
and read only by the accuracy analysis.

A word may also carry a **floating lexical autosegment** — a melody-tier value with
no host segment of its own (the classic case: a grammatical floating H tone) —
written `⟨◌́⟩`: a suprasegmental diacritic on a
dotted-circle placeholder (◌, U+25CC), in float brackets. Its position in the
string matters: `kata⟨◌́⟩` places a floating high _after_ the final segment (a
suffixal tone that docks leftward onto it); `⟨◌́⟩kata` places one _before_ the
first. A dock rule (§5.12) then binds it wherever it sits.

**CSV form (`words.csv`).** The lexicon may equally be written as a CSV table — the same
schema, one word per row — chosen by the file's extension (`load_word_inventory` dispatches on
`.csv` vs TOML). A header row names the columns, read **by name** so any order works; the
canonical order follows the derivation timeline:

```
word, gloss, frequency, <intermediate stage times, ascending>, final
```

e.g. `word, gloss, frequency, -200, -100, 750, 1000, 1200, 1400, final`. `word` is the IPA key
(required); `gloss`/`final`/`frequency` are the reserved columns (all optional except `word`);
every other column
whose name is an **integer** is a stage time, its cell the attested form then. An empty
cell means "not present". Fields are read with the `csv` module, so a value containing a
comma must be quoted (`"amère, bitter"`). A project may carry either form; if both
`words.toml` and `words.csv` are present, TOML wins.

### 4.2 Rules — `rules.toml` / `rules.csv`

Rules are given in TOML or CSV (equally valid — see the **CSV form** at the end of this
section). In the TOML form, each rule is a table whose header is the rule's **id** (a slug). Chronology is carried by a separate `time` field, not by the header.

```toml
[laryngeal_coloring]
time        = -2000
name        = "Laryngeal coloring"
description = "Allophonic colouring of /e/ adjacent to laryngeal consonants"
definition  = "xe → xa"

[centumization]
time        = -2000
name        = "Centumization"
description = "Merging of PIE 'palatovelar' and 'velar' plosives"
definition  = "[+cons, +guttural, +coronal] → [cor: none]"

[u_epenthesis]
time        = -2000
name        = "'u' epenthesis"
description = "Epenthesis of /u/ before the syllabic sonorants"
definition  = "∅ [+cons, +syll] → u [-syll]"
```

**Fields:**

- `definition` _(required)_ — the rule in Fortis notation (§5).
- `time` _(optional)_ — an integer giving relative chronology. Lower values apply earlier; the value is a sort key, not a calendar date, and may be negative. Omit it for an **undated** rule, which applies _after_ every timed rule (not at `0`) — useful for a single synchronic derivation where chronology is irrelevant.
- `name` _(optional)_ — a short human-readable label.
- `description` _(optional)_ — a one-sentence description.
- `application` _(optional, default `"simultaneous"`)_ — one of `"simultaneous"`, `"left_to_right"`, `"right_to_left"`. See §6.2.
- `words` _(optional)_ — a word, or list of words, the rule is restricted to (matched against each word's IPA **or** gloss). With it set, the rule fires only on those words and is skipped for all others — a **sporadic** / lexically-restricted change, or a rule staged to demonstrate a synchronic mechanism on one word. Omit it (the default) and the rule applies to every word. A listed name that matches no word (by IPA or gloss) raises a load-time warning, since the rule could then never fire — a guard against typos.

**Ordering:** rules are sorted by `time` ascending — undated rules (no `time`) last — then by order of appearance in the file for rules that share a time. Leaving gaps between `time` values (e.g. −2000, −1000, 0) lets you insert later rules without renumbering.

The three rules above also illustrate the result-position distinction of §5.1: in `laryngeal_coloring`, `a` is a **letter** and replaces the matched segment entirely; in `u_epenthesis`, the inserted `u` is a letter (full segment) while `[+cons, +syll] → [-syll]` is a **bundle** that merges, changing only syllabicity and leaving the rest of the consonant intact.

**CSV form (`rules.csv`).** The rule list may equally be written as a CSV table — one rule
per row, chosen by extension. Columns are read by name; the canonical order mirrors a rule
table top-to-bottom:

```
id, time, name, description, definition, application, words
```

`id` and `definition` are required; the rest are the optional fields above (an empty cell
is "absent", so an empty `time` is an undated rule). Two fields that are lists in TOML are
written `;`-separated in their one cell: a multi-part `definition` (its sub-steps share the
row's time/name and mint `id#1`, `id#2`, …) and a multi-word `words` scope. `;` is used
because `|` is reserved by alternation inside a definition (e.g. `(j|w)`); a gloss used as a
word-scope therefore cannot itself contain `;`. As with the lexicon, a project may carry
either form, and `rules.toml` wins if both are present.

### 4.3 tiers.toml

Declares the autosegmental tiers (§5.12). Each top-level table **is** one
suprasegmental feature: the table name is the feature (and tier) name, and that
one feature is lifted onto its own tier as autosegments linked to an anchor,
rather than stored in the segment bundle. So each table both **defines the
feature** (`kind`/`values`/`short`, exactly as a `features.toml` entry, §3.2) and
sets its **association policy** (`anchor`, `melody`, …). The file is **optional** —
omit it and the engine runs with no tiers.

```toml
[tone]
kind        = "scalar"      # feature definition, as in features.toml (§3.2)
short       = "tn"
values      = { 1 = "extra-low", 2 = "low", 3 = "mid", 4 = "high", 5 = "extra-high" }
anchor      = "+syllabic"   # a segment matching this pattern can bear an autosegment
melody      = true          # melody (tone): floats and re-docks under stability
ocp         = true          # merge adjacent identical autosegments (the OCP)
stray_erase = true          # remove a still-floating autosegment at the surface

[stress]
kind   = "scalar"
short  = "str"
values = { 1 = "secondary", 2 = "primary" }
anchor = "+syllabic"
melody = false              # metrical (stress): stays put under deletion
ocp    = false
```

**Fields:**

- `kind`, `values`, `short` — the feature definition, exactly as a `features.toml` entry (§3.2); `kind` is required (and `values` for a `scalar`). The tier carries this single feature, named for the table.
- `anchor` _(required)_ — a feature pattern; a segment matching it can bear an autosegment (typically the syllable nucleus, `+syllabic`).
- `melody` _(required)_ — `true` for a melody tier (tone): an autosegment stranded by deletion floats and is carried to a neighbour (stability, §5.12). `false` for a metrical tier (stress): it stays put.
- `ocp` _(optional, default `true`)_ — merge adjacent identical autosegments.
- `stray_erase` _(optional, default `true`)_ — delete a still-floating autosegment at the surface.
- `stability` _(optional, default `"left"`)_ — for a melody tier, which neighbour an autosegment stranded by deletion carries to: `"left"` (the preceding syllable) or `"right"` (the following).

---

## 5. Rule Notation Reference

The general form of a rule is:

```
A → B / C _ D // E _ F
```

where `A` is the **target**, `B` is the **result**, `C` is the **left context**, `D` is the **right context**, `E` is the **left exception**, and `F` is the **right exception**. A rule requires at minimum a target and a result. The context (`/`) and the exception (`//`) are optional.

The underscore `_` marks the position of the target within the context and within the exception.

### 5.1 Letters and feature bundles

_Valid in all positions._

```
p                letter shorthand
[+syll]          feature bundle
[−voice]
[syll: 1]
[height: 3]      scalar value
[hgt: high]      named scalar value
[cor: none]      explicitly absent / unspecified
[nasal]          bare feature name — see below
```

A **bare feature name** with no sign or value (`[nasal]`, `[place]`) resolves
differently by kind: for a **unary** feature it means present, same as
`[+nasal]`; for a **binary** or **scalar** feature it means the feature is
specified with _any_ value, which is a pattern-only wildcard — it is a
validation error to write a bare non-unary feature in a **result**, since a
concrete output segment needs an explicit value.

In **target** position, letters and feature bundles both match by features. In **result** position they differ:

- A **feature bundle** merges into the matched segment — features it does not mention are preserved.
- A **letter shorthand** replaces the matched segment entirely with the letter's full specification.

**Suprasegmental diacritics on a literal** — any diacritic whose bundle sets a feature declared on a tier (§4.3; in the shipped inventory, the stress marks `ˈ`/`ˌ` and the tone marks) — live on their own tier (§5.12), apart from the segment's melody, so a literal that carries one does a different job on each side:

- In the **target** (and contexts/exceptions) it _constrains_ the match to that value: `ˌɔ` matches only a secondary-stressed ɔ, whereas a bare `ɔ` matches at any stress. To constrain by a suprasegmental without spelling the vowel, put it in a bundle: `[+syllabic, stress: secondary]`.
- In the **result** it _writes_, replacing the suprasegmental of the changed segment's syllable: `e → ˈa` stresses that syllable, `ˌa → ˈa` promotes secondary to primary, `ˈe → ˌe` demotes. A **bare** result literal writes nothing, so the syllable's stress persists from the input. The mark must land on a **nucleus** — on a non-nucleus result literal (`d → ˈt`) it has nowhere to attach and is dropped; write it on the syllable's nucleus, or use a bundle (`[stress: primary]`).

A **letter with a feature override** — `letter^[Δ]` — is a letter shorthand _modified_ by a concrete bundle Δ: the letter's full specification with Δ combined on top. It is a replacement (like a bare letter), not a merge, so Δ overrides only the features it names (a `none` value _delinks_). Δ is a **realized** bundle — concrete values only, no negation/alpha/conditional.

```
e^[stress: none]   e, unstressed          — the one way to remove stress while also changing the melody
a^[stress: primary] a, primary-stressed
t^[+voice]         t's spec, voiced
e^[length: long]   a long e
```

The `^` binds the **last** letter of a run: `au^[length: long]` lengthens only the `u`. It is valid in every position: in the **result** it replaces-with-Δ (and a suprasegmental in Δ writes the syllable, overriding what would persist — so `ˈe → a^[stress: none]` genuinely destresses); in the **target** it is an identity match against the letter _plus_ Δ (`e^[length: long]` matches only a long e). Contrast the plain bundle `[Δ]`, which _merges_ onto — and keeps the melody of — the matched segment.

A `none` value **delinks**. For a segmental feature it is geometry-aware — delinking a node drops its whole subtree, so `e^[oral: none]` (no place/quality) is a featureless schwa; it is a no-op only where the feature is already absent (`e^[nasal: none]`, since `e` carries no nasal). For a suprasegmental it delinks the tier (`e^[stress: none]` unstresses in the result). In the **target**, an absent value counts as `none`: an unstressed nucleus carries no stress feature, so `e^[stress: none]` matches an unstressed e — symmetric with `e^[stress: primary]`, which matches only a primary-stressed one.

#### Letter–tier interactions

A letter's _segmental_ content sits in the bundle; a tier feature (e.g. stress or tone) sits on the nucleus's tier. How a literal touches that tier depends on the side. Taking `e` and stress as the example:

| Form                  | Target — matches           | Result — produces                          |
| --------------------- | -------------------------- | ------------------------------------------ |
| `e`                   | an `e` at **any** stress   | an `e`; **stress persists** from the input |
| `ˈe`                  | a **primary**-stressed `e` | an `e`, **writes** primary stress          |
| `e^[stress: none]`    | an **unstressed** `e`      | an `e`, **delinks** stress (unstressed)    |
| `e^[stress: primary]` | a **primary**-stressed `e` | an `e`, **writes** primary stress          |

Three things follow. **`ˈe` is exactly `e^[stress: primary]`** (and `ˌe` is `e^[stress: secondary]`) — the stress diacritic is shorthand for that override, on both sides. **Bare `e` is the only form that leaves the tier alone** — it matches at any stress and lets the input's stress persist on output; every marked or overridden form pins one value. And **`e^[stress: none]` has no diacritic equivalent** (there is no "unstressed" mark), so it is the only way to _match_ an unstressed vowel or to _remove_ stress in the result — the suprasegmental mirror of `e^[oral: none]` → schwa on the segmental side.

### 5.2 Special symbols

```
[]     wildcard — matches any segment   (target, context, exception)
#      word boundary                    (target, context, exception)
$      syllable boundary                (target, context, exception)
-      morpheme boundary                (any position — a real segment)
∅      null segment                     (target, result only)
```

Boundaries (`#`, `$`) are positional assertions and do not count toward cardinality on either side. A boundary may not be the sole element on either side of a rule (`# → x` and `x → #` are both errors), but is otherwise valid in result position too, where it is a redundant marker, and inside a disjunction in any position. `∅` is **not** valid in context or exception positions.

The **morpheme boundary `-`** is different from `#`/`$`: it is a real, one-wide segment (written directly in a word, e.g. `at-a`), not a zero-width assertion. It forces a syllable break at its position (see §7) and is opaque to phonology — no bundle, letter, wildcard, or negation matches it, so it breaks up adjacency; only a `-` element matches it. Being a real segment it **does** count toward cardinality, so `- → ∅` deletes a boundary and `∅ → - / a _ t` inserts one, exactly like any segment. Because the form re-syllabifies before every rule, deleting a `-` ends its influence from the next rule on. (`-` is only ever the arrow head in `->`, so a `-` meant as a boundary right before an arrow needs a space: `ab- ->`; a `-` value inside a bundle, `[-voice]`, is untouched.)

### 5.3 Quantifiers

_Valid on any element, in any position._

```
[+cons]{3}            exactly 3
[+cons]{0,3}          between 0 and 3
[+cons]{2,}           2 or more
[+cons]{,3}           up to 3
[+cons]?              0 or 1
[+cons]*              0 or more
[+cons]+              1 or more
[]{3}                 exactly 3 of any segment
([+syll][+cons]){3}   group repeated 3 times
```

A **merge-bundle** result element must carry the **same quantifier** as its target. Full-replacement results are exempt: a letter-shorthand result may freely collapse or expand a span (`a{2} → b`), and `∅` (which carries no quantifier) pairs with a quantified target to delete all matched segments.

### 5.4 Negation

```
!p           not this letter
![+syll]     not this bundle
[!+syll]     a segment without a positive syllabic specification
!(a | b)     none of these branches match
!(ab)        this sequence does not match
!#           not at this boundary   (target, context, exception)
```

`!` is **not** valid in result position, and may not be applied to `∅` or `[]`. It applies to whatever immediately follows it.

At the feature level, negation is a complement over the whole value space **including** `none`: `!feature` matches `none` (equivalent to `[feature: none]`); `![+F]` matches `−F` or `none`; `[feature: !1]` matches every other value or `none`. This is why `!F` is never redundant with a specific negative value — it also covers the segment simply not having that feature specified at all.

### 5.5 Groups and disjunctions

_Valid in all positions._

```
([+syll][+cons])              group
([height: 3] | [height: 2])   disjunction
```

A disjunction in **result** position must correspond to a disjunction in **target** position with the same number of branches; otherwise it is a validation error. Branches pair positionally — if branch _k_ of the target matched, branch _k_ of the result applies. A non-disjunction result applies uniformly regardless of which target branch matched.

### 5.6 Alpha (Greek-letter variable) notation

```
[α high]     bind or recall the value of feature 'high' as α
[−α high]    the opposite of the bound value   (binary and unary features only)
[!α high]    any value other than the bound value, the unspecified case (none) included
```

Each Greek letter is an independent variable ranging over the legal values of its feature. A variable **binds** at its first occurrence during left-to-right evaluation of the structural description, evaluated in the order left context → target → right context → exception. Later occurrences recall the bound value.

Position rules:

- **Binding** may occur in target, context, or exception position. A variable that appears _only_ in the exception clause binds locally within that clause.
- **Recall** is valid in all positions. In result position, `[αF]` assigns the bound value to the output segment; result position is recall-only and never binds.
- A variable that appears only in result position, with no binding occurrence anywhere, is a validation error.
- `[−α F]` is valid only for binary and unary features.

`[!α F]` — "any value other than the bound one" — depends on the feature's kind: for a **unary** feature the only other value is `none` (so `!α` is exactly `none`, the sole reason it's never redundant with `−α`); for a **binary** feature it's `{−α, none}`; for a **scalar** feature it's any other level or `none`.

Binding a variable to a parent node binds all of its child features simultaneously. Against a contour, `[αF]` binds α to the full contour tuple, while `[αF: @final]` binds α to the scalar at the named edge.

Example — backness harmony:

```
[+syll] → [α back] / [α back] [−syll]* _
```

α binds on the left-context vowel; the same value is assigned to the target.

### 5.7 References

```
1=[+syll]    bind element reference 1     (target, context, exception)
@1           recall element reference 1   (all positions)
```

Every `@n` recall needs a corresponding `n=` binding somewhere in the rule (position doesn't matter — e.g. you can bind in the target and recall in the context), and every `n=` binding must be recalled at least once. `n=` is **not** valid in result position. Group bindings follow the same rules, and a group recall `@n` is valid in all positions.

Example — metathesis:

```
1=[+son, −syll] 2=[−son] → @2 @1 / V _ V
```

### 5.8 Conditional features

_Valid in target, result, and context positions._

```
[<1: +high>]    conditional feature with label 1
[<1: !+high>]   negated condition
[<1: α high>]   condition references an alpha variable
```

A conditional feature applies its result feature(s) only when its condition holds. Each label must be a condition **somewhere** — in the target _or_ the context — and must drive at least one feature in the result; a result label with no condition, or a condition that drives nothing, is a validation error. A label may repeat: several result features can share a label (one condition driving a multi-feature change, e.g. colouring _e_ to _a_), and a condition may sit purely in the context (assimilation from a neighbour — this is how laryngeal colouring works) or in the target itself. When a label has conditions in more than one position, **all** of them must hold. An alpha variable referenced in a condition must be bound in the target or context of the same rule.

Example — ATR harmony conditioned on height:

```
[+syll, <1: +high>] → [<1: +ATR>] / [+syll, +ATR] [−syll]* _
```

The target gains ATR only if it is high.

### 5.9 Contour features

```
[tone: 3>1]          contour: falling from 3 to 1
[tone: +@initial]    + at the start of the contour
[tone: +@final]      + at the end of the contour
[tone: +@any]        + at any position (the default, made explicit)
[tone: +@all]        + at every position
[tone: 5@2]          tone is 5 at position 2
[tone: 5@2;3]        tone is 5 at positions 2 and 3
```

By default `[+F]` matches if F is `+` at any position in its contour. That `@any` default holds for a single value or single limb. A multi-limb contour pattern (e.g. [tone: 1>2]) instead defaults to @all — it matches only a target contour of the same arity, limb for limb — so to match it as a sub-sequence of a longer contour you must give `@initial`, `@final`, `@any` (the contour anywhere), or per-limb positions (`@2;3`, one index per limb) explicitly. A bare `@n` is for single values only; on a multi-limb contour the positions must be an edge or a same-length list. The positional modifiers (`@initial`, `@final`, `@any`, `@all`, `@n`, `@n;m`) override the default and are **valid in target and context positions only**. In **result** position, a contour must be given with explicit concrete values.

The default position depends on the shape of the value, not on any per-rule setting:

| Value                            | Default position | Effect                                                                                                                                     |
| -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| single value (`tone: 1`)         | `@any`           | matches at some limb                                                                                                                       |
| multi-limb contour (`tone: 1>2`) | `@all`           | must be the whole contour, exact arity                                                                                                     |
| whole-contour alpha (`tone: α`)  | —                | binds the entire contour, any length; a position suffix narrows it to the limb(s) there (`tone: α@initial` binds α to just the first limb) |

An alpha variable can bind **per limb** or to the **whole contour**, and the two read differently: `tone: α>β` binds one variable to each of exactly two limbs (the multi-limb default `@all` applies, so the target contour must have exactly that arity), while `tone: α` (no `>`) binds a single variable to the entire contour regardless of its length. Note that `tone: α>α` is **not** a two-limb pattern: a run of identical adjacent limbs folds at parse time (like `5>5` → `5`), so `α>α` collapses to a single whole-contour `α`, identical to `tone: α`.

Contour reduction is 1:1:

```
[F: v1>v2] → [F: v1>none]   keep the initial limb
[F: v1>v2] → [F: none>v2]   keep the final limb
```

Here `none` is a feature value meaning "unspecified at that position," distinct from the null segment `∅`.

### 5.10 Null segment: insertion and deletion

_`∅` is valid in target and result positions only._

```
∅ [+cons, +syll] → u [-syll]      insertion: insert /u/ before a syllabic consonant, which desyllabifies
[+nas] → ∅ / _ #                   deletion: delete a word-final nasal
[+cons][+syll] → ∅[−syll]          paired: delete the consonant, modify the vowel
```

`∅` as the entire target requires a context. `∅` as the entire result deletes the whole matched target. A `∅` paired with one element of a multi-element result deletes that element while the other result elements apply normally.

### 5.11 Delinked nodes

```
[place: none]    delinked place node — the segment becomes placeless / glottal
```

This is a feature value, distinct from the null segment `∅`. All children of the delinked node become unspecified at once.

### 5.12 Autosegmental tier operations

A feature declared on a tier in `tiers.toml` (e.g. `tone`, `stress`) is an _autosegment_ linked to its anchor segment, not a value in the segment's bundle. Rules manipulate those links:

```
[tone: ~1=high]    bind: record the tone autosegment (value high) under reference 1
[tone: ~1]         recall: link that SAME autosegment to this anchor (spread)
[tone: none]       delink: remove this anchor's association on the tone tier
⟨tone: ~1=high⟩    a floating autosegment (no anchor); zero-width, bound for docking
```

- **Spread** — `[+syll, tone: none] → [+syll, tone: ~1] / [+syll, tone: ~1=high] [-syll]* _` gives a toneless vowel the tone of a preceding vowel with high tone (one autosegment, now two anchors — not a copy). Adjacent elements match adjacent _segments_, so the `[-syll]*` is what spans the consonants between the two syllables — without it the two `[+syll]` would have to be a vowel hiatus. Under a directional mode (§6.2) the H spreads across a whole toneless run.
- **Dock** — `⟨tone: ~1=high⟩ [+syll, tone: none] → [+syll, tone: ~1]` matches a floating H and links it onto the toneless syllable. The `⟨…⟩` is zero-width (it consumes no segment, so it does not count toward cardinality). A lexical floating autosegment (§4.1) is _positioned_ — it docks only where it sits in the string — while one stranded by a deletion (below) is position-blind and docks at any matching site, so a directional application mode or a narrowing context is usually needed to dock it exactly once.
- **Delink** — `[+syll] → [tone: none]` removes the association.
- **Stability** — _automatic_: when a rule deletes a segment carrying a **melody** tier autosegment (`melody = true`, e.g. tone), it is carried onto the surviving neighbour (the tier's `stability` direction — `"left"` by default, or `"right"`) and re-docked to its nucleus, so a tone outlives its vowel. **Metrical** tiers (`melody = false`, e.g. stress) stay put. A word-initial deletion with no left neighbour leaves the autosegment floating; a still-floating autosegment is stray-erased at the surface.

A `tiers.toml` entry declares one suprasegmental feature (its `kind`/`values`, §4.3), the `anchor` it links to, whether it is a `melody` (vs metrical), and its `ocp` / `stray_erase` policies. With no `tiers.toml`, none of this runs.

`~` is used (not `@`, which already marks contour positions). A `~n=` binding and `~n` recall follow the same validation as ordinary references (§5.7): every recall needs a binding and every binding must be recalled. A floating element `⟨…⟩` is pattern-only — valid in target and context positions, but a validation error in the result.

**Segmental node-spread.** `~n` on a _segmental_ geometry node copies that node's whole subtree from the source to the target — `[+nasal] → [oral: ~1] / _ [+consonantal, oral: ~1]` is place assimilation (the nasal takes the following consonant's whole place). Plain `~n` is the canonical spread: it matches only a source that _has_ the node (a nasal before a placeless `h`, no `oral`, does not assimilate). A trailing `?` — **`node: ~n?`** — is a _presence-optional_ node-spread: it matches whether the source has the node or not, and an absent source **clears** the node on the target (the node analogue of a unary α's absent pole). Use it where mutually-exclusive privative siblings spread as a set: `[back: ~1?, front: ~2?]` copies backness from the preceding vowel both ways — a back source (no `front`) clears the target's `front`, a front source clears its `back`. A value on a segmental recall — **`node: ~n=value`** — is a _bind-and-match_: it binds only a source whose node carries that value, so a transparent `[]*` gap steps over nearer non-matching segments to reach it. Sibe uvularization spreads `high` onto a dorsal from a preceding `[-high]` vowel with `high: ~1=-`, the intervening `[+high]` vowels transparent (a plain `high: ~1` would bind whichever vowel is nearest). These segmental changes render — alongside tier changes — as one canonical autosegmental diagram per rule in the `--autosegmental` report and the web app's **Graph** view (a feature-geometry tree for a node-spread, Goldsmith's tonal notation for a tier change); a rule that only rewrites a feature in place is not drawn.

---

## 6. Rule Application Semantics

### 6.1 The inner loop: does a locus fire?

At each candidate position the engine checks, in order:

1. **Target match** — does the segment or span at this position satisfy the target description?
2. **Context match** — do the left and right contexts hold around the target?
3. **Exception check** — if an exception clause is present, does it match? If it does, the rule does **not** fire here.

The rule rewrites the target when the target and context match and the exception does not.

### 6.2 The outer loop: application mode

The `application` field controls how the engine sweeps the form when multiple loci could match.

**`simultaneous`** (default): every locus is found against the original input, then all rewrites are applied at once. No application sees another's output. This is correct for most rules — assimilation, lenition, deletion.

**`left_to_right`**: the engine scans left to right, and each rewrite is immediately visible to later applications in the same pass. This is required for self-feeding rules such as progressive harmony, where a changed segment must itself become a trigger. Scan resumption follows obligatory-rewrite semantics (Kaplan & Kay 1994): the cursor advances past the rewritten **output** only, the context remains available for matching, and target spans are matched greedily, leftmost-longest.

**`right_to_left`**: the mirror of `left_to_right`, scanning right to left — for regressive (anticipatory) harmony or spreading.

### 6.3 Time ordering, feeding, and bleeding

Rules fire in `time` order, and within a single time in file order. Rules interact through standard feeding and bleeding relations purely as a consequence of this ordering; counterfeeding and counterbleeding need no special mechanism. Because the derivation is recorded step by step, opacity can be read directly off the trace.

Ordering is fully determined: rules are sorted by `time`, and within a single time by their order in the file. So when two rules share a `time`, the one earlier in the file applies first and can feed or bleed the later one exactly as a lower `time` would — change the relation by reordering them within the time or by giving them distinct `time` values.

---

## 7. Syllabification

Syllabification places syllable boundaries on a form without inserting or deleting segments. It runs on the input and is refreshed before every rule, so `$` always reflects current structure. A word's two edges count as syllable boundaries; a word with no nucleus is unsyllabifiable and gets none.

**Nuclei** are the segments matching the `nucleus` definition (§4). Between each adjacent pair of nuclei, the intervening consonants are divided into the preceding syllable's coda and the following syllable's onset:

- By default the division follows the **Maximal Onset Principle** under sonority sequencing (§3.4): the onset is the longest run whose sonority rises toward the nucleus; the rest is coda.
- If an `onset` and/or `coda` **pattern** is defined in `syllable_parts.toml`, that pattern _defines_ legality instead: every split point is considered and the longest onset whose onset and coda each fully match their patterns wins — so a pattern may license a non-sonority-rising onset (e.g. _s_+stop). The patterns are ordinary element sequences (`[nasal]` is a mandatory single-nasal coda; `[nasal]?` an optional one; `[+cons][-syll, -cons]?` a consonant plus optional glide). A cluster the patterns cannot legally divide **falls back to the sonority Maximal Onset division** (rather than leaving the word unsyllabified), and the fallback is recorded as a warning: the CLI writes a `warnings.md` listing each such word and cluster, and the web app shows a **Warnings** tab. So the patterns are a preference that always yields *some* structure — loosen them to cover a flagged cluster, or accept the sonority split.

Onset/coda patterns constrain only the interior division where there is a choice; word-edge onsets and codas are forced and not checked.

A **morpheme boundary** `-` (§5.2) in an interior cluster overrides all of the above: it forces the syllable split at its own position — everything before it is the preceding syllable's coda, everything after it the following syllable's onset — so `at-a` is `at.a` (coda _t_), where `ata` is `a.ta` (onset _t_). Deleting the `-` with a rule restores ordinary syllabification on the next pass.

The `$` assertion matches at any syllable boundary (interior or word edge). Syllable-tier diacritics attach to the nucleus of their syllable during segmentation, and render back to IPA in `render_syllabified` positioned by their attachment `kind` (§4): a `before` mark at the syllable's left edge (the shipped stress marks `ˈ`/`ˌ`), a `combining` mark on the nucleus itself, and an `after` mark at the syllable's right edge (the shipped Chao tone letters; a contour renders as a tone-letter sequence).

---

## 8. Derivation and Output

### 8.1 Derivation trace

For each word, Fortis records the sequence of forms from the input through every rule that **fired**, to the surface form. Each recorded step includes the form before the rule, the rule that fired, what changed, and the form after. Rules that did not fire for a given word are omitted from that word's trace.

### 8.2 Output format

The terminal shows only summary and general information — the files written, a `words derived / rules applied` count, per-phase timing, and (when the lexicon carries targets) the accuracy, errors, and blame headlines. The full per-word derivation trace is written to **`derivations.csv`** (long-format: one row per word × firing rule), not printed.

The same trace renders in human-readable block form in the web app — each word's headword and gloss (`ipa – "gloss"`), then a block per rule that fired: a heading line with the rule's `time:` and name, and beneath it one indented `before → after   (change)` line per locus the rule changed (with `.` between syllables), ending in a `Surface:` line:

```
meħˈteːr – "mother"
    -2000: Laryngeal colouring before a laryngeal
        meħˈteːr → maħˈteːr   (e→a)
    -2000: Loss of laryngeals after vowels
        maħˈteːr → maːˈteːr   (aħ→aː)
    …
    1950: */θ̠ ð̠/ > */θ ð/
        ˈmʌ.ð̠ə˞ → ˈmʌ.ðə˞   (ð̠→ð)
    Surface: ˈmʌ.ðə˞
```

The change summary shows the segments that changed as `old→new` (e.g. `kʲ→k`); for a length change it trims the shared prefix/suffix and shows just the differing region (`m̩→um`, with `∅` for a fully inserted or deleted side).

### 8.3 Written reports and accuracy

Every CLI run writes into a `reports/` subfolder of the project directory:

- **`derivations.csv`** — the main report: the firing-rule trace in long format, one
  row per word × firing rule (columns `word, rule, t, before, after, change`). Each
  word is bookended by two synthetic rules — **`input`** (`before` = the raw IPA as
  written in the lexicon, `after` = the form the engine ingested it as: syllabified,
  diacritics normalised) and **`output`** (`after` = the surface form). A word on which
  no rule fired is just its `input` and `output` rows.
- **`derivation_matrix.csv`** — the same run in wide format: one row per word, one column
  per rule (each titled `<time>: <name>`), holding the word's form right after that rule
  fired (empty where it did not).
- **`rule_firings.csv`** — the run inverted to one row per rule (`rule, t, sporadic, count,
  changes, matched`): its `words` scope in `sporadic` (blank for a general rule), the
  distinct segment-level changes it made (e.g. `d→t`), and the words it matched as
  `before → after`. A rule that never fired shows `count` 0 with empty cells.
- **`rule_dependencies.html`** — the rule feeding graph, read off the actual firings:
  which rule's output segment feeds which rule's input. A scrollable view with time on the
  x-axis (period blocks, +1 sub-column per same-time dependency); hover a rule to see the
  segments it consumes/produces and the rules it is fed by / feeds. The webapp's **Tree**
  tab renders the same graph.
- **`accuracy.csv`** and **`distance_to_target.csv`** — the **accuracy**
  analysis, written only when the lexicon carries attested forms (`final`/`stages`,
  §4.1). It measures each derived form's distance to its target with two edit
  distances: a **phone** distance (a base segment plus its combining marks is one
  phone; an exact match is 0) and a finer **feature** distance (a substitution costs
  the number of features that differ, so `ɑ̃` is one edit from `ɑ` but eleven from
  `t`; an adjacent-segment swap counts as one). `accuracy.csv` is the
  per-stage summary (columns `stage, assessed, exact, within 1, mean phone dist, mean
  feature dist` — plus `token-wt exact/phone/feature` when the lexicon carries word
  `frequency` weights, counting each word by its frequency); `distance_to_target.csv` is
  the per-word long table (columns `stage,
  gloss, derived, target, d, fd, matches at, closest at` — the last two scan the derived form
  against the word's *other* attested stages, flagging a form that matches, or comes closest to,
  a stage other than its own). Both cover each stage and the final surface.
- **`errors.csv`** — the **errors** analysis, when there are wrong words: per attested
  stage (and the final), a ranked tally of the phone confusions — `stage, expected, got,
  count, kind, examples (gloss: derived vs. attested)`. `∅` marks the absent side (an
  insertion has no *expected*, a deletion no *got*).
- **`error_context.csv`** — the **error context** analysis: per stage and per erroring
  segment, the attested-form environments most associated with getting it wrong —
  `stage, segment, environment, assoc. (φ), F₁, err/ok · with, err/ok · without`
  (positive-φ predictors that clear the support floor; complete, no display cap).
- **`blame.csv`** — every assessed word's per-step distance trajectory, worst first
  (columns `gloss, step, regression, t, form, target, d, fd`); exact words are included as short
  `d=0` paths. The interactive Blame tab additionally shows each wrong phone's culprit rule.

The thresholds these analyses use are tunable per project in an optional
`settings.toml` (the autopsy's support floor and how many phones to autopsy, the
edit distance's metathesis cost); an absent file, or key, uses the built-in defaults.

A run ends with a one-line summary on stderr — words derived, rules applied,
per-phase timing, and the files saved.

### 8.4 Single-word derivation

`--single WORD` derives one word instead of the whole project. The word is looked up in
the lexicon by its IPA key or gloss — so it carries any attested targets — and is
otherwise derived bare. It prints a compact summary and writes the same reports
prefixed `single_` into the project's `reports/` subfolder: `single_derivations.csv`
always, and — when the word carries a target — `single_accuracy.csv`,
`single_distance_to_target.csv`, `single_errors.csv`, `single_error_context.csv`, and
`single_blame.csv`. The web app's **Single** tab is the same feature, interactive.

### 8.5 Parallel derivation

Because deriving one word never affects another, the CLI (`python -m src.fortis.main`)
fans a large lexicon across worker processes **automatically**, giving a ~4–6× speedup
on a multi-core machine. The result is
byte-identical to a serial run and in the same order. A small lexicon (below a couple
hundred words) stays in a single process, since the pool's start-up cost — spawning
processes and handing each the project — would outweigh the gain. `--serial` forces a
single process (useful for profiling or a reproducible baseline); `--workers N` pins the
pool size (default: about two below the CPU count). The browser app derives serially:
Pyodide (CPython on WebAssembly) has no multiprocessing, so this applies to the CLIs only.

---

## 9. Validation

Rule definitions are validated at load time. Errors are collected rather than failing on the first one, so every problem in a file is reported together. The following are validation errors.

**Structural**

- Target and result have different numbers of elements **when the result contains a feature bundle** (`∅` counts; a full-replacement letter/recall result may collapse or expand the span, so it need not match — see §5.1).
- A result **bundle** carries a different quantifier from its corresponding target (a full-replacement letter result is unconstrained by the target's quantifier; `∅` carries none).
- A boundary (`#`, `$`) is the sole element on either side of a rule (`# → x`, `x → #`).
- A feature specified more than once within a single bundle (e.g. [+high, −high]).
- A bare non-unary feature name (`value == "any"`, §5.1) in result position — it's pattern-only, and a concrete output segment needs an explicit value.

**Null segment**

- `∅` in context or exception position.
- `∅` as the entire target with no context.

**References**

- An `@n` recall with no corresponding earlier `n=` binding.
- An `n=` binding that is never recalled.
- `n=` in result position.

**Alpha variables**

- A variable appearing only in result position (unbound).
- `[−α F]` on a non-binary, non-unary feature.

**Conditional features**

- A conditional label applied in the result with no condition for it in the target or context.
- A conditional label that is a condition (in target or context) but drives no result feature.
- An alpha variable referenced in a condition but not bound in the target or context.

**Disjunctions**

- A disjunction in the result with no corresponding target disjunction.
- A result disjunction whose branch count differs from its target disjunction.
- More than one top-level disjunction on a single side.
- A nested disjunction coexisting with a top-level disjunction on the same side.

**Negation**

- `!` applied to `∅` or `[]`.
- `!` in result position.

**Contours**

- A positional modifier (`@initial`, etc.) in result position (result contours must use explicit values).

**Autosegmental tiers**

- A `~n` recall with no corresponding `~n=` binding, or a `~n=` binding never recalled (same rule as ordinary references, §5.7).
- A floating element `⟨…⟩` in result position (pattern-only — valid in target and context).

---

_Fortis — a diachronic and synchronic phonology engine._
