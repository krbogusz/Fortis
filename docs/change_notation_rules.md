# Fortis Sound Change Notation Rules

**Notation conventions.** In this document, `A`, `B`, `C`, `D`, `E`, `F` stand for rule positions (target, result, left context, right context, etc.). `[F]` stands for any feature bundle. Feature names and values are illustrative.

## 1. Symbols

### 1.0. Rule notation

`A → B / C_D // E_F` — element `A` turns into `B` with context `C_D`, except `E_F`

### 1.1. Letters and features

- `p` — Letter shorthand
- `[-syll]` — Segment
- `[+syll]`, `[syll: 1]`, `[2 height]`, `[hgt: high]` — Different ways of specifying features and values

### 1.2. Other signs

- `[]` — Wildcard, any segment
- `#` — Word boundary
- `$` — Syllable boundary
- `∅` — Null segment (insertion/deletion marker)

### 1.3. Quantifiers

Quantifiers may be applied to any element — feature bundles, wildcards, groups, and letter shorthands.

- `[+cons]{3}` — Exactly 3 elements
- `[+cons]{0,3}` — Between 0 and 3 elements
- `[+cons]{2,}` — 2 or more elements
- `[+cons]{,3}` — Up to 3 elements
- `[+cons]?` — 0 or 1 element (={0,1})
- `[+cons]*` — 0 or more elements (={0,})
- `[+cons]+` — 1 or more elements (={1,})
- `[]{3}` — Exactly 3 of any segment
- `([+syll][+cons]){3}` — The two-element group pattern repeats 3 times

### 1.4. Control elements

- `!p`, `![+syll]` — Not this letter or element
- `[!+syll]` — An element without a positive syllabic specification
- `([+syll][+cons])` — Group
- `([height: 3] | [height: 2])` — Disjunction
- `[α high]` — Alpha notation
- `[!α high]` — Alpha notation, not the previously bound feature value
- `[<1: +high>]` — Conditional feature (valid in target, result, and context positions)
- `1=[+syll]` — Saving a reference to an element
- `@1` — Reference to an element

### 1.5. Contour specification

- `[cont: 1>2>3]` — Contour feature and values
- `[cont: +@any]` — F is + at any position in the contour (default, explicit)
- `[cont: +@initial]` — F is + at the start of the contour
- `[cont: -@initial]` — F is – at the start of the contour
- `[cont: +@final]` — F is + at the end of the contour
- `[tone: 5@2]` — Tone is 5 at the second place in the contour
- `[tone: 5@2;3]` — Tone is 5 at the second and third place in the contour
- `[tone: 5@all]` — Tone is 5 at every place in the contour

Positional modifiers (`@any`, `@initial`, `@final`, `@all`, `@n`) are suffixes on the value after a colon. The pattern is `[feature: value@position]` — sign or scalar value comes first, then the position.

### 1.6. Application modes

Rules may specify how they apply when multiple loci match. The `application` TOML key takes one of:

- `simultaneous` (default) — find every locus against the original input, rewrite all at once
- `left_to_right` — scan left to right, apply at each locus, changed segments visible to later applications
- `right_to_left` — scan right to left, mirror of left-to-right

### 1.7. Time ordering

Each rule is a TOML table headed by its id, `[<id>]` (e.g. `[laryngeal_coloring]`, `[backness_harmony]`), with the chronology supplied by a separate required `time` field inside the table. Lower time values are applied earlier. Rules sharing a time are applied in the order of declaration.

## 2. Rules

### 2.1. Structural rules

1. A rule must be **unambiguous** about how the target maps to the result. A result **bundle** merges into a corresponding target (preserving that target's other features, per 2.1.5), so it needs exactly one source — bundle results therefore require target and result to have the same number of elements (`∅` counts; boundaries do not). A **letter shorthand** replaces wholesale and fully specifies the output, so a result made entirely of letter shorthands may have a different count from the target: the matched span **collapses into** or **expands to** those letters. A count mismatch with any result bundle is ambiguous (which target does the bundle merge with, and which is gone?) and is invalid.
   - Valid: `au → e`, `e → au`, `∅ [+cons] → u` (full-replacement results).
   - Invalid: `[+cons][-cons] → [nas]`, `[+syll] → [+lo][+hi]` (a count mismatch onto merge bundles).
2. A result **bundle** lines up one-to-one with its corresponding target (it merges), so it must carry the same quantifier as that target. A full-replacement **letter** result is unconstrained by the target's quantifier — e.g. `a{2} → b` is valid (two a's collapse into b), while `[+cons]{2} → [+nas]` is not (the merge-bundle's quantifier must match).
3. The only exception to rule 2.1.2 is `∅`, which carries no quantifier.
4. A quantified target element paired with `∅` in the result deletes all matched segments.
5. Letter shorthands and bundles behave identically in target position (both match the segment's features). In result position they differ:
   - A **bundle** merges into the target — features not specified in the bundle are preserved. Example: `[+cons] → [-vc]` changes only the voice feature; all other features of the consonant remain.
   - A **letter shorthand** replaces the target entirely — the letter's full feature bundle takes over, discarding all of the target's features. Example: `x → a` replaces whatever matched `x` with the full specification of `a`.

### 2.2. Placement rules

1. `∅` is not valid in context or exception positions.
2. Boundaries (`#`, `$`) are positional assertions — they do not count toward cardinality on either side.
3. Boundaries are valid in target, context, exception, and optionally result positions, where they are redundant
   markers.
4. Boundaries may not be the sole element on either side of a rule — `# → x` and `x → #` are validation errors.
5. Boundaries are valid inside disjunctions in all positions (target, context, exception, and result).

### 2.3. Reference rules

1. Every `@n` recall must have a corresponding `n=` binding somewhere in the rule. Binding and recall are
   scope-based, not order-based: the position of the binding relative to the recall does not matter (e.g.
   `1=a → b / @1 _` binds in the target and recalls in the left context). The target is ref-bound first at
   match time, so no left-to-right ordering across positions is imposed.
2. Every `n=` binding must be recalled at least once.
3. `n=` is not valid in result position.
4. Group bindings follow the same rules as single-element bindings.
5. `@n` recall of a group binding is valid in all positions.

### 2.4. Alpha variable rules

1. Distinct Greek letters (α, β, γ, …) are distinct alpha variables. Each must be bound by at least one occurrence
   in target or context position. An alpha variable that appears only in result or exception position is unbound and
   is a validation error.
2. Example: `[+syll] → [α cor, β gut] / [+syll, α cor, β gut] [-syll]* _` — α and β are bound in the context and
   recalled in the result.

### 2.5. Null segment rules

1. `∅` in target position within a sequence marks an insertion point; the corresponding result element is what gets
   inserted.
2. `∅` as the entire target means unconditional insertion at a position defined by the context.
3. `∅` as the entire result means unconditional deletion of the entire matched target.
4. `∅` as the entire target is invalid without a context.
5. `∅` paired with a single target element in a multi-element result deletes that element while other result elements
   apply normally. Example: `[+cons][+syll] → ∅[-syll]` deletes the consonant and modifies the vowel.

### 2.6. Exception clause rules

1. An exception clause `//` may appear with or without a context clause `/`.
2. Exceptions may contain any elements valid in context position: boundaries, bundles, letter shorthands,
   quantifiers, groups, disjunctions, negation, references, alpha variables, and conditional features. Exception
   positions follow the same validation rules as context positions (e.g. `∅` is not valid in exception position,
   per §2.2.1).

### 2.7. Disjunction rules

1. A disjunction in result position must have a corresponding disjunction in target position with the same number
   of branches.
2. A disjunction in result position without a corresponding disjunction in the target is a validation error (there
   is no branch to pair with).
3. Branches are paired positionally — if branch k of the target matched, branch k of the result is applied.
4. A non-disjunction result applies uniformly regardless of which branch of a target disjunction matched.

### 2.8. Negation rules

1. `!` is valid in target and context positions only — not in result position.
2. `!` is not valid if applied to `∅` or `[]`.
3. `!` applied to a boundary is valid in target, context, and exception positions, meaning "not at this boundary."
4. `!` applies to whatever immediately follows it:
   - `!(a | b)` — negation of a disjunction: none of these branches match.
   - `!(ab)` — negation of a group: this sequence does not match.

### 2.9. Conditional feature rules

1. Conditional features `[<n: F>]` are valid in target, result, and context positions.
2. Each label `n` must appear **at least once as a condition** — in the target *or* the context — **and at least once
   in the result**. A label may repeat on either side: several result features may share a label (a single condition
   driving a multi-feature change, e.g. "become *a*"), and several conditions may share a label (combined, per rule 5).
3. A conditional label used in the result with **no** condition (in target or context) is a validation error — the
   feature would apply unconditionally.
4. A conditional label that is a condition but drives **no** result feature is a validation error — it gates nothing.
5. A label's conditions are **AND**ed across every position they appear in (target and/or context): the paired result
   feature(s) apply only when *all* of them hold. So a label may be conditioned purely on the context — assimilation
   from a neighbour, e.g. laryngeal colouring (`[<1: +low>]` on the adjacent laryngeal colours *e* → *a*) — or on the
   target itself (`[<1: +high>]` in the target → height-conditioned), or both.
6. The condition may be negated: `<n: !F>` means apply the paired result feature only if the condition is not
   satisfied.
7. Conditional features may reference alpha variables: `<n: αF>` means the condition is satisfied if the feature
   value equals the bound value of `α`. The alpha variable must be bound somewhere in the target or context of the same
   rule.

### 2.10. Child and parent feature rules

1. If a parent feature is set to unspecified, its child features are also unspecified.
2. Alpha variable binding to a parent feature automatically binds to all child features.
3. A parent node name in feature bundle position with no value (`[place]`) matches any segment that has that node
   specified, regardless of children.
4. `[node: ∅]` denotes a delinked node; all children are simultaneously unspecified by §2.10.1. This is the
   canonical debuccalization/placeless representation. The `∅` here is a feature value meaning "unspecified/delinked"
   — distinct from the `∅` null segment defined in §1.2.

### 2.11. Contour rules

1. A feature value of the form `v1>v2>...>vN` (N ≥ 2) is a contour. A single value is equivalent to a contour of
   length 1.
2. By default, `[+F]` matches if F is + at any position in its contour.
3. Positional modifiers (`@initial`, `@final`, `@any`, `@all`, `@n`) override the default existential matching. `@any`
   is the explicit form of the default (existential). They are suffixes on the value:
   `[feature: value@position]` (e.g. `[cont: +@initial]`, `[tone: 5@2]`). They are valid in target and context positions
   only. In result position, the contour must be specified explicitly with concrete
   values (e.g. `[F: v1>v2]`). Contour values themselves are valid in result position.
4. Contour reduction is 1:1 and uses normal cardinality. `[F: v1>v2] → [F: v1>∅]` keeps the initial limb;
   `[F: v1>v2] → [F: ∅>v2]` keeps the final. The `∅` in these contour values means "unspecified at that position" —
   distinct from the `∅` null segment defined in §1.2.
5. Alpha binding interacts with contours as follows: `[αF]` against a contour binds α to the full tuple;
   `[αF: @final]` binds α to the scalar at the named edge. `[!αF]` then means "any value other than the bound
   tuple/scalar," respectively.
