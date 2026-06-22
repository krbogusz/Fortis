# Fortis Reference Manual

Fortis is a sound change engine for diachronic and synchronic phonology. It takes a lexicon and an ordered set of phonological rules, applies those rules to every word in the lexicon, and produces a derivation trace showing each intermediate form and the rule responsible for each change.

Everything Fortis works with is **user-defined and imported from TOML files**: the feature vocabulary, the IPA letters, the diacritics, the sonority scale, the syllable parameters, the lexicon, and the rules. Fortis ships no built-in phonology; it is an engine that runs whatever inventories and rules you supply.

---

## Table of Contents

1. [Overview](#1-overview)
2. [The Pipeline](#2-the-pipeline)
3. [The Feature System](#3-the-feature-system)
4. [The TOML Configuration Files](#4-the-toml-configuration-files)
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

The parser consumes an IPA string left to right using greedy longest-match tokenisation against the user-defined inventories. At each position it takes the longest substring that matches a letter in `letters.toml`, then consumes any following substrings that match diacritics in `diacritics.toml`, buffering them onto the preceding base and applying their feature modifications. The result is a `Sequence` — an ordered list of `Segment` objects, each carrying a complete `FeatureBundle`.

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
| Absent        | +     | +      | -      |
| Level         | -     | -      | +      |

**Undefined applies to every feature, not only unary ones.** Any feature — binary, unary, or scalar — can be marked unspecified with the value `none`. For example, `[cor: none]` removes the coronal specification entirely; this is distinct from `[−cor]`, which specifies a negative value. Both differ from a feature simply being absent from a bundle: in a concrete segment an absent feature is unspecified (equivalent to none), but in a pattern an absent feature is unconstrained — it places no condition on the segment, whereas [cor: none] requires the segment to be unspecified for coronal. Within a single bundle, each feature may be specified at most once.

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

The sonority scale is user-defined in `sonorities.toml`, both in the number of levels and in the feature predicates that assign segments to them. Levels are assigned by first-match against an ordered list of predicates. A typical scale might look like:

| Level | Class      |
| ----- | ---------- |
| 7     | Vowels     |
| 6     | Glides     |
| 5     | Rhotics    |
| 4     | Laterals   |
| 3     | Nasals     |
| 2     | Fricatives |
| 1     | Stops      |

but the number of levels, their ordering, and the predicates are all yours to define. Sonority feeds syllabification, which is not yet implemented (see §7).

---

## 4. The TOML Configuration Files

Every inventory Fortis uses is loaded from a TOML file. All of them are user-authored.

| File              | Contents                                            |
| ----------------- | --------------------------------------------------- |
| `features.toml`   | The feature vocabulary and geometry                 |
| `letters.toml`    | IPA symbol → feature bundle mappings                |
| `diacritics.toml` | Diacritic modifications to base segment bundles     |
| `sonorities.toml` | Sonority levels and the predicates that assign them |
| `words.toml`      | The lexicon                                         |
| `rules.toml`      | Phonological rules                                  |

A `syllable.toml` for syllabification parameters is planned but not yet active (§7).

### 4.1 words.toml

Each entry maps an IPA string directly to a gloss. The IPA string is the key; the gloss is the value.

```toml
# Words for testing phonological derivation.
# Format: IPA = "gloss"
"xenti"     = "in front"
"mexteːr"   = "mother"
"ɣʷeroː"    = "eagle"
"bʱleɣʷmoː" = "flower"
"kʲm̩tom"    = "hundred"
"n̩ter"      = "inside"
"wl̩kʷos"    = "wolf"
"xr̩tkʲos"   = "bear"
"wergʲom"   = "work"
"wr̩mis"     = "worm"
"gʲʱhjeti"   = "go"
"ketus"     = "fight"
```

### 4.2 rules.toml

Each rule is a TOML table whose header is the rule's **id** (a slug). Chronology is carried by a separate `time` field, not by the header.

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
- `time` _(required for ordering)_ — an integer giving relative chronology. Lower values apply earlier; the value is a sort key, not a calendar date, and may be negative.
- `name` _(optional)_ — a short human-readable label.
- `description` _(optional)_ — a one-sentence description.
- `application` _(optional, default `"simultaneous"`)_ — one of `"simultaneous"`, `"left_to_right"`, `"right_to_left"`. See §6.2.

**Ordering:** rules are sorted by `time` ascending, then by order of appearance in the file for rules that share a time. Leaving gaps between `time` values (e.g. −2000, −1000, 0) lets you insert later rules without renumbering.

The three rules above also illustrate the result-position distinction of §5.1: in `laryngeal_coloring`, `a` is a **letter** and replaces the matched segment entirely; in `u_epenthesis`, the inserted `u` is a letter (full segment) while `[+cons, +syll] → [-syll]` is a **bundle** that merges, changing only syllabicity and leaving the rest of the consonant intact.

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
```

In **target** position, letters and feature bundles both match by features. In **result** position they differ:

- A **feature bundle** merges into the matched segment — features it does not mention are preserved.
- A **letter shorthand** replaces the matched segment entirely with the letter's full specification.

### 5.2 Special symbols

```
[]     wildcard — matches any segment   (target, context, exception)
#      word boundary                    (target, context, exception)
$      syllable boundary                (target, context, exception)
∅      null segment                     (target, result only)
```

Boundaries (`#`, `$`) are positional assertions and do not count toward cardinality on either side. A boundary may not be the sole element in the target. `∅` is **not** valid in context or exception positions.

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

Corresponding target and result elements must carry **identical quantifiers** (the sole exception is `∅`, which carries none). A quantified target element paired with `∅` in the result deletes all matched segments.

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

Each Greek letter is an independent variable ranging over the legal values of its feature. A variable **binds** at its first occurrence during left-to-right evaluation of the structural description, evaluated in the order left context → target → right context. Later occurrences recall the bound value.

Position rules:

- **Binding** may occur in target, context, or exception position. A variable that appears _only_ in the exception clause binds locally within that clause.
- **Recall** is valid in all positions. In result position, `[αF]` assigns the bound value to the output segment; result position is recall-only and never binds.
- A variable that appears only in result position, with no binding occurrence anywhere, is a validation error.
- `[−α F]` is valid only for binary and unary features.

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

Every `@n` recall needs a corresponding `n=` binding earlier in the rule, and every `n=` binding must be recalled at least once. `n=` is **not** valid in result position. Group bindings follow the same rules, and a group recall `@n` is valid in all positions.

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

A conditional feature applies a result feature only when its condition holds. Each label must appear exactly once in the target and exactly once in the result; a label present in one without a match in the other is a validation error. A conditional in the context sharing a label with one in the target means **both** conditions must hold for the paired result feature to apply. An alpha variable referenced in a condition must be bound in the target or context of the same rule.

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

By default `[+F]` matches if F is `+` at any position in its contour. That `@any` default holds for a single value or single limb. A multi-limb contour pattern (e.g. [tone: 1>2]) instead defaults to @all — it matches only a target contour of the same arity, limb for limb — so to match it as a sub-sequence of a longer contour you must give @initial, @final, or @n explicitly. The positional modifiers (`@initial`, `@final`, `@any`, `@all`, `@n`) override this and are **valid in target and context positions only**. In **result** position, a contour must be given with explicit concrete values.

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

Two rules sharing both a `time` and an adjacent file position with overlapping loci have an undefined interaction; give them distinct `time` values or reorder them to make the intended feeding relation explicit.

---

## 7. Syllabification

**Not yet implemented — TODO.**

Syllabification is planned to sit between parsing and rule application, placing boundaries between pre-identified nuclei without inserting or deleting segments, driven by the user-defined sonority scale (§3.3) and a forthcoming `syllable.toml` parameter file. Until it lands, sequences are not syllabified, the `$` syllable-boundary assertion has nothing to match against, and rules should not rely on syllable structure.

---

## 8. Derivation and Output

### 8.1 Derivation trace

For each word, Fortis records the sequence of forms from the input through every rule that **fired**, to the surface form. Each recorded step includes the form before the rule, the rule that fired, what changed, and the form after. Rules that did not fire for a given word are omitted from that word's trace.

### 8.2 Output format

The report shows only the rules that actually changed the form:

```
ɣʷeroː  "eagle"
  →  [laryngeal_coloring]  ɣʷeroː       (no match)   ← omitted
  →  [centumization]       ɣweroː       gʷ: [cor: none]
Surface: ɣweroː
```

In practice the omitted line above does not appear; only steps that change the form are printed. A compact rendering of the same derivation:

```
ɣʷeroː  "eagle"
  →  [centumization]  ɣweroː   gʷ: [cor: none]
Surface: ɣweroː
```

---

## 9. Validation

Rule definitions are validated at load time. Errors are collected rather than failing on the first one, so every problem in a file is reported together. The following are validation errors.

**Structural**

- Target and result have different numbers of elements (`∅` counts as an element).
- Corresponding target and result elements carry different quantifiers (except `∅`, which carries none).
- A boundary (`#`, `$`) is the sole element in the target.
- A feature specified more than once within a single bundle (e.g. [+high, −high]).

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

- A conditional label in the result with no matching label in the target, or vice versa.
- An alpha variable referenced in a condition but not bound in the target or context.

**Disjunctions**

- A disjunction in the result with no corresponding target disjunction.
- A result disjunction whose branch count differs from its target disjunction.

**Negation**

- `!` applied to `∅` or `[]`.
- `!` in result position.

**Contours**

- A positional modifier (`@initial`, etc.) in result position (result contours must use explicit values).

---

_Fortis — a diachronic and synchronic phonology engine._
