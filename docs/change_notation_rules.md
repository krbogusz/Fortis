# Fortis Sound Change Rule Notation

## 1. Symbols

### 0. Rule notation

`A → B / C_D // E_F` – element `A` turns into `B` with context `C_D`, except `E_F`

### 1.1. Letters and features

- `p` – Letter shorthand
- `[+syll]`, `[syll: 1]`, `[2 height]`, `[hgt: high]` – Different ways of specifying features and values
- `S[]` – syllable
- `M[]` – mora
- `[]` – segment (default)

### 1.2. Other signs

- `[]` – Wildcard, any segment
- `#` – Word boundary
- `$` – Syllable boundary
- `∅` – Null segment

### 1.3. Quantifiers

- `[+cons]{3}` – Exactly 3 elements
- `[+cons]{0,3}` – Between 0 and 3 elements
- `[+cons]{2,}` – 2 or more elements
- `[+cons]{,3}` – up to 3 elements
- `[+cons]?` – 0 or 1 element (={0,1})
- `[+cons]*` – 0 or more elements (={0,})
- `[+cons]+` – 1 or more elements (={1,})

### 1.4. Control elements

- `!p`, `![+syll]` – Not this letter or element
- `[!+syll]` – Not an element with a positive syllabic specification
- `([+syll][+cons])` – Group
- `([height: 3] | [height: 2])` – Disjunction
- `[α high]` – Alpha notation
- `[!α high]` – Alpha notation, not previously specified feature value
- `[<1: +high>]` – Conditional feature
- `V=[+syll]` – Saving a reference to an element
- `@V` – Reference to an element

### 1.5. Contour specification

- `[cont: 1>2>3]` – Contour feature and values
- `[cont: @initial]` – Edge match: F is + at the start of the contour
- `[cont: @final] ` – Edge match: F is + at the end of the contour
- `[cont: @2] ` – Existential: F is + at the second place in the contour
- `[cont: @2>3] ` – Existential: F is + at the second and third place in the contour
- `[cont: @all]` – Existential: F is + in every place in the contour

## 2. Rules

### 1. Structural rules

1. Target and result must have the same number of elements, where `∅` counts as an element.
2. Corresponding elements in target and result must carry identical quantifiers.
3. The only exception to rule 1.2. is `∅`, which carries no quantifier.
4. A quantified target element paired with `∅` in the result deletes all matched segments.

### 2. Placement rules

1. `∅` is not valid in context or exception positions.
2. Boundaries `#`, `$`, `%` are positional assertions — they do not count toward cardinality on either side.
3. Boundaries are valid in target, context, exception, and optionally result positions, where they are redundant
   markers.
4. Boundaries may not be the sole element on either side of a rule — `# → x` and `x → #` are validation errors.
5. Boundaries are valid inside disjunctions in context, target, and exception positions.

### 3. Reference rules

1. Every `@n` recall must have a corresponding `n=` binding earlier in the rule.
2. Every `n=` binding must be recalled at least once.
3. `n=` is not valid in result position.
4. Group bindings follow the same rules as single-element bindings.
5. `@n` recall of a group binding is valid in all positions.

### 4. Alpha variable rules

1. Every alpha variable must be bound by at least one occurrence in target or context position.
2. An alpha variable appearing only in result or exception position is a validation error.

### 5. Null segment rules

1. `∅` in target position within a sequence marks an insertion point; the corresponding result element is what gets
   inserted.
2. `∅` as the entire target means unconditional insertion at a position defined by the context.
3. `∅` as the entire result means unconditional deletion of the entire matched target.
4. `∅` as the entire target is invalid without a context.

### 6. Exception clause rules

1. An exception clause `//` may only appear if a context clause `/` is present.

### 7. Disjunction rules

1. A disjunction in result position must have a corresponding disjunction in target position with the same number
   of branches.
2. Branches are paired positionally — if branch k of the target matched, branch k of the result is applied.
3. A non-disjunction result applies uniformly regardless of which branch of a target disjunction matched.

### 8. Negation rules

1. `!` is valid in target and context positions only — not in result position.
2. `!` is not valid if applied to `∅` or `[]`.
3. `!` applied to a boundary is valid in target, context, and exception positions, meaning "not at this boundary."
4. `!` applied to a disjunction means "none of these branches match."
5. `!` applied to a group means "this sequence does not match."

### 9. Conditional feature rules

1. Conditional features are valid in target, result, and context positions.
2. Each label `n` must appear exactly once in the target and exactly once in the result.
3. A conditional label in the result without a matching label in the target is a validation error.
4. A conditional label in the target without a matching label in the result is a validation error.
5. A conditional feature sharing a label with a context conditional means both conditions must be satisfied for the
   paired result feature to apply.
6. The condition may be negated: `<n: !F>` means apply the paired result feature only if the condition is not
   satisfied.
7. Conditional features may reference alpha variables: `<n: αF>` means the condition is satisfied if the feature
   value equals the bound value of `α`. The alpha variable must be bound somewhere in the target or context of the same
   rule.

### 10. Child and parent feature rules

1. If a parent feature is set to unspecified, its child features are also unspecified.
2. Alpha variable binding to a parent feature automatically binds to all child features.
3. A parent node name in feature bundle position with no value (`[place]`) matches any segment that has that node
   specified, regardless of children.
4. `[node: ∅]` denotes a delinked node; all children are simultaneously unspecified by §10.1. This is the
   canonical debuccalization/placeless representation.

### 11. Contour rules

1. A feature value of the form `v1>v2>...>vN` (N ≥ 2) is a contour. A single value is equivalent to a contour of
   length 1.
2. By default, `[+F]` matches if F is + at any position in its contour.
3. The modifiers `@initial`, `@final`, `@all`, `@2`, `@2>3` like `[-cont@initial]` override the default. They are
   valid in target and context positions only — not in result, where the contour must be specified explicitly.
4. Contour reduction is 1:1 and uses normal cardinality. `[F: v1>v2] → [F: v1>∅]` keeps the initial limb;
   `[F: v1>v2]` → `[F: ∅>v2]` keeps the final.
5. Alpha binding interacts with contours as follows: `[αF]` against a contour binds α to the full tuple;
   `[αF@final]` binds α to the scalar at the named edge. `[!αF]` then means "any value other than the bound
   tuple/scalar," respectively.
