# Fortis — Feature-Spec Notation Reference

A feature spec names **one feature** and assigns it **one value**. _Simple_
features (unary/privative, binary, scalar) take a single value; _contour_
features take an ordered sequence of limbs joined by `>`. The pattern-vs-result
distinction is structural — which rule slot a `PatternSpec` / `ResultSpec`
fills — not written inside the spec.

- Limb separator: `>` — `1>2` is the two-limb contour _1 then 2_.
- Ordering is free: `tone: 1>2` ≡ `1>2 tone`. Canonical form below: `feature: value`.
- Position suffix attaches directly: `tone: α>2@initial`.

**Presence model.** Every feature node is in one of: a _specified value_, or
`none` (node absent / delinked). `!` is **complement** over _all values ∪ {none}_.

---

## Value atoms

Fill any scalar slot or any single limb of a contour.

| Token            | Meaning                                  | Notes                                                             |
| ---------------- | ---------------------------------------- | ----------------------------------------------------------------- |
| `1`, `2`, `-1`…  | concrete value                           | scalar features                                                   |
| `+` / `-`        | positive / negative (≈ present / absent) | unary & binary; sugar for the integer poles                       |
| `none`           | node absent / undefined (`None`)         | as a **result** = unlink                                          |
| _(bare feature)_ | any non-none value — `Wildcard.present`  | pattern-only; the complement of `none`                            |
| `α`              | alpha, same — bind or recall             | scalar; **whole contour** on a contour feature                    |
| `-α`             | alpha, opposite                          | binary / unary only (scalar has no single opposite)               |
| `!α`             | alpha, other                             | distinct from spec negation `!feature` (value `!` vs feature `!`) |

---

## Simple features — affirmative

| Notation     | Matches                                                            | Feature types         |
| ------------ | ------------------------------------------------------------------ | --------------------- |
| `nasal`      | node present (any value) — `value=Wildcard.present` (pattern-only) | all                   |
| `+nasal`     | positive / present                                                 | unary, binary         |
| `-nasal`     | negative / absent                                                  | unary, binary         |
| `tone: 1`    | value 1                                                            | scalar                |
| `tone: none` | node absent                                                        | all                   |
| `voice: α`   | bind / recall α                                                    | all                   |
| `voice: -α`  | opposite of α                                                      | unary, binary         |
| `voice: !α`  | other than α                                                       | all                   |

---

## Negation = value-space complement

`!` matches everything the affirmative spec does **not**, including `none`.

| Affirmative  | Matches           | `!…` matches               |
| ------------ | ----------------- | -------------------------- |
| `feature`    | any present value | `none` (≡ `feature: none`) |
| `+feature`   | positive          | `−`, `none`                |
| `-feature`   | negative          | `+`, `none`                |
| `feature: 1` | `1`               | every other value, `none`  |

Applies to unary, binary, scalar. The `+`/`-` forms are unary/binary only
(scalar uses explicit values). Contours negate the same way:
`!tone: 1>2` matches any contour other than `(1, 2)`, `none` included.

!α includes none. !α is the value-space complement of the bound value — any value other than what α matched, the unspecified case included — the alpha analogue of spec-level !. By feature type: scalar !α = any other level or none; binary !α = {−α, none}, distinct from −α (just the opposite pole); unary (privative) !α = none, the only value other than the bound +. This is what keeps !α from being redundant with −α.

---

## Contour features — limbs

Each limb is any value atom (`1`, `none`, `α`, `-α`, `!α`); limbs joined by `>`.

| Notation       | Meaning                                 |
| -------------- | --------------------------------------- |
| `tone: 1>2`    | limbs 1 then 2                          |
| `tone: none>1` | undefined limb, then 1                  |
| `tone: α>2`    | α then concrete 2                       |
| `tone: α>β`    | independent variables per limb          |
| `tone: α>α`    | limbs constrained equal                 |
| `tone: α`      | **whole** contour bound to one variable |

---

## Contour features — arity & position

The position suffix decides how the limb pattern aligns to the target contour.

| Form       | Behaviour                                                                             |
| ---------- | ------------------------------------------------------------------------------------- |
| `@any`     | pattern aligns at **some** position (subsequence / "some limb")                       |
| `@all`     | predicate holds at **every** limb — whole contour; a multi-limb pattern ⇒ exact arity |
| `@initial` | prefix — target starts with these limbs, any total length                             |
| `@final`   | suffix                                                                                |
| `@2`       | at limb index 2 (any total length covering it)                                        |
| `@2;3`     | at limbs 2 and 3                                                                      |

**Default position depends on value shape** — the parser sets it; the
`PatternSpec.contour_position = ContourEdge.any` field default is just a
hand-construction fallback:

| Value                                         | Default | Effect                                                                                     |
| --------------------------------------------- | ------- | ------------------------------------------------------------------------------------------ |
| scalar / single limb (`tone: 1`)              | `any`   | matches at some limb                                                                       |
| multi-limb contour (`tone: 1>2`, `tone: α>β`) | `all`   | must _be_ the whole contour (exact arity)                                                  |
| value-level `α` (`tone: α`)                   | —       | binds the entire contour at any length;                                                    |
|                                               |         | a position **narrows** it to the limb(s) at that position (`tone: α@initial` = first limb) |

`@all` on a single-limb predicate is universal: `tone: 1@all` matches a contour in which every limb is 1 (so 1, 1>1, 1>1>1, …). This is consistent with `@all` meaning "the whole contour" — the predicate must hold at every position.

---

## Whole-contour vs per-limb alpha

| Notation            | Binding                               | Arity / position                      |
| ------------------- | ------------------------------------- | ------------------------------------- |
| `tone: α`           | one variable binds the entire contour | any length (no position)              |
| `tone: α>β`         | one variable per limb                 | default `all` → **exactly two limbs** |
| `tone: α>β@initial` | α, β on the first two limbs           | any total length, α/β first           |

---

## Result-side specifics

A `ResultSpec` carries only a value — no position, no negation.

| Notation                 | Meaning                      |
| ------------------------ | ---------------------------- |
| `voice: +` / `tone: 1`   | set value                    |
| `tone: 1>2`              | set the contour              |
| `voice: none`            | **unlink**                   |
| `voice: α` / `voice: -α` | set to recalled / opposite α |

Role of `none`: pattern = "node absent"; **result scalar = unlink**; limb =
"undefined limb".

---

## Constraints to enforce in validation

- `@position` is contour-only and **pattern-side only** (`ResultSpec` has no `contour_position`).
- Negation is **pattern-side only** (`ResultSpec` has no `negated`).
- `-α` (opposite) restricted to binary / unary features (scalar has no single opposite).
- Value-level `α`: scalar on a simple feature, whole-contour on a contour feature.
- Default contour position is value-shape-driven: scalar/single-limb → `any`; multi-limb contour → `all` (exact arity).

# Fortis feature-spec notation — test cases

# One spec per line; lines starting with # are section labels.

# Strings double as pattern or result specs (the side is structural).

# --- simple: affirmative ---

nasal
+nasal
-nasal
voice: +
voice: -
tone: 1
tone: 2
tone: 0
tone: -1
tone: none
nasal: none

# --- simple: value-first ordering ---

1 tone
none continuant
α voice
none>1 continuant

# --- simple: alpha ---

voice: α
voice: -α
voice: !α
tone: α
tone: !α

# --- simple: negation (value-space complement) ---

!nasal
!+nasal
!-nasal
!tone: 1
!voice: +
!tone: none

# --- contour: concrete ---

tone: 1>2
tone: 2>1
tone: 1>2>3
tone: 1>none
continuant: none>1
height: 0>1>2
tone: -1>1

# --- contour: per-limb alpha ---

tone: α>2
tone: 2>α
tone: α>β
tone: α>α
tone: α>β>γ
tone: !α>2
tone: α>!β
tone: none>α

# --- contour: whole-contour alpha ---

tone: α
tone: !α

# --- position: single limb ---

tone: 1@initial
tone: 1@final
tone: 1@any
tone: 1@all
tone: 1@2
tone: 1@2;3

# --- position: sequence ---

tone: 1>2@initial
tone: 1>2@final
tone: 1>2@any
tone: 1>2@all
tone: 1>2@2
tone: 1>2@2;3
tone: α>β@initial
tone: α>β@final
tone: α>β@2;3

# --- whole-contour alpha + position (position narrows α to that limb) ---

tone: α@initial
tone: α@final
tone: α@2
tone: α@2;3

# --- contour negation (complement of the matched set) ---

!tone: 1>2
!tone: α>β
!tone: 1>2@initial

# --- combined: negation + position ---

!tone: 1@final
!tone: 1@all

# --- edge / expected-invalid (negative tests) ---

tone: -α
tone: 1>2>
tone: >1
tone: 1>2@0
voice: ++
@initial
tone:
1>2
