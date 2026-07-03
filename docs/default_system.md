# The Default System

This describes `projects/default` — the feature system, letter inventory,
diacritics, sonority scale, and syllable structure shipped with the engine.
It is a single worked example of how to model a phonological system in
Fortis, not a fixed part of the engine: every field here lives in ordinary
TOML/CSV files under `projects/default/`, and any project can override some
or all of it (see the main [README](../README.md#design-philosophy)). For
how to author your own feature system from scratch, see
[`user_guide.md`](user_guide.md) §3–§4.

## Feature geometry

The segmental tree, from `features.toml` (a `root` node parenting the
top-level features is synthesised automatically and never written out):

```
ROOT
├── syllabic       (binary)
├── consonantal    (binary)
├── sonorant       (binary)
├── click          (unary)
├── length         (scalar: 1 short, 2 long, 3 overlong)
├── manner         (unary)
│   ├── continuant (binary)
│   ├── strident   (unary)
│   ├── lateral    (unary)
│   ├── tap        (unary)
│   └── trill      (unary)
├── nasal          (unary)
├── oral           (unary)
│   ├── labial     (unary)
│   │   ├── rounded    (unary)
│   │   └── compressed (unary)
│   ├── dental     (unary)   — the passive articulator (at the teeth): combines
│   │                          with labial (f, v, ɱ) or with lingual (t̪, n̪)
│   └── lingual    (unary)
│       ├── apical    (unary)
│       ├── retroflex  (unary)
│       ├── front     (unary)
│       │   ├── anterior (unary)
│       │   └── posterior (unary)
│       ├── back      (unary)
│       ├── aperture  (scalar: -1 low, 0 mid, 1 high)
│       └── advancement (scalar: -1 rtr, 0 neutral, 1 atr)
└── glottal        (unary)
    ├── voice            (binary)
    ├── glottal_aperture (scalar: -1 constricted, 0 neutral, 1 spread)
    ├── tension          (scalar: -1 slack, 0 neutral, 1 stiff)
    └── larynx_height    (scalar: -1 lowered, 0 neutral, 1 raised)
```

Two suprasegmental features live on tiers instead (`tiers.toml`, not the
segment bundle — see `user_guide.md` §4.3 and §5.12): `tone` (scalar,
extra-low…extra-high) and `stress` (scalar, secondary/primary).

Most nodes are unary (present/absent), reserving binary for the handful of
features that need a genuine positive/negative opposition (`syllabic`,
`consonantal`, `sonorant`, `continuant`, `voice`) and scalar for features
with more than two contrastive levels (`length`, `aperture`, `advancement`, tone,
stress, and the three laryngeal dimensions). Setting a parent node — `[oral: none]`,
`[lingual: none]` — unspecifies every child simultaneously; this is the mechanism
behind debuccalisation (a placeless, glottal segment) and behind vowel reduction
(clearing `oral` turns any vowel into the featureless ə).

## Vowels and consonants share one feature space

There is no separate "vowel feature system." A segment's status as a vowel
or a consonant comes from `syllabic` and `consonantal` (plus `sonorant` and
`manner`), not from a different set of place features — vowel quality and
consonant place of articulation are expressed through the _same_ `oral` /
`lingual` / `labial` nodes. Pulled directly from `letters.csv`:

| Segment                         | Active features                                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `/k/` (voiceless velar stop)    | `-syllabic, +consonantal, -continuant, +lingual, +back, aperture: high`                                      |
| `/u/` (high back rounded vowel) | `+syllabic, -consonantal, +continuant, +labial, +rounded, +lingual, +back, aperture: high, advancement: atr` |
| `/i/` (high front vowel)        | `+syllabic, -consonantal, +continuant, +lingual, +front, aperture: high, advancement: atr`                   |
| `/e/` (mid front vowel)         | `+syllabic, -consonantal, +continuant, +lingual, +front, aperture: mid`                                      |
| `/t/` (voiceless alveolar stop) | `-syllabic, +consonantal, -continuant, +lingual, +front, +anterior`                                          |
| `/a/` (low vowel)               | `+syllabic, -consonantal, +continuant, +lingual, +front, aperture: low, advancement: rtr`                    |

`/k/` and `/u/` both carry `lingual, back, aperture: high` — the identical
dorsal place specification. What makes `/u/` a rounded back **vowel** rather
than a velar **consonant** is `+syllabic, -consonantal` plus the added
`labial, rounded` (rounding is the same `labial` node a consonant like `/p/`
uses for bilabial place); what makes `/k/` a stop rather than a vowel is
`-syllabic, +consonantal, -continuant`. Likewise `/i/` and `/k/` share
`lingual, aperture: high`, differing in `front` vs. `back` and in the
syllabic/consonantal/continuant features that set the vowel/consonant and
manner distinctions. `/t/`'s coronal place (`lingual, front, anterior`) uses
the same `front` node a front vowel like `/i/` or `/a/` sets, just with the
`anterior`/`posterior` children (relevant only to consonantal place)
additionally specified.

This is a deliberate design choice — a single place hierarchy that both
segment classes draw from — not a requirement of the engine; a project is
free to give vowels and consonants entirely separate feature sets if that
suits its data better.

### Natural classes

A quick reference to the feature(s) that pick out each common class in
`letters.csv` (and so the bundle you write to match it in a rule). The place
rows assume a consonant (`+consonantal, -syllabic`); the manner rows cut across
places. Back consonants share the vowel-height scale: velar is `aperture: high`,
uvular is `aperture: mid`, pharyngeal is `aperture: low` (uvular and pharyngeal
additionally carry `advancement: rtr`) — the same high/mid/low contrast as vowels.

| Class                   | Marked by                                                  | e.g.                 |
| ----------------------- | ---------------------------------------------------------- | -------------------- |
| **vowel**               | `+syllabic, -consonantal`                                  | i, e, a, o, u        |
| **reduced vowel**       | `+syllabic, aperture: none` — featureless, no `oral` node  | ə                    |
| **semivowel**           | `-syllabic, -consonantal`                                  | i̯, u̯                 |
| **glide**               | `+consonantal, +sonorant, +continuant, aperture: !none`    | j, w (ʕ̞: low)        |
| **labial**              | `+labial`                                                  | p, b, m, f           |
| — labiodental           | `+labial, +dental` (no `lingual`)                          | f, v, ɱ              |
| **rounded** (V/glide)   | `+labial, +rounded`                                        | u, o, y, w           |
| **coronal**             | `+lingual, +front`                                         | t, s, n, ʃ, r, l     |
| — dental                | `+lingual, +front, +anterior, +dental`                     | t̪, n̪                 |
| — (post)alveolar        | `+lingual, +front, +anterior` / `+posterior`               | t, s / ʃ, ʒ          |
| — palatal               | `+lingual, +front, aperture: high` (no anterior/posterior) | c, ɟ, ɲ, ʎ, j        |
| **retroflex**           | `+lingual, +front, +retroflex`                             | ʈ, ɖ, ʂ, ɭ           |
| **dorsal / velar**      | `+lingual, +back, aperture: high`                          | k, g, ŋ, x, w        |
| **uvular**              | `+lingual, +back, aperture: mid, advancement: rtr`         | q, ɢ, χ, ʁ           |
| **pharyngeal**          | `+lingual, +back, aperture: low, advancement: rtr`         | ħ, ʕ                 |
| **glottal** (placeless) | `+glottal` only, no `oral`                                 | ʔ, h                 |
| **nasal**               | `+nasal` (and `+sonorant`)                                 | m, n, ɲ, ŋ           |
| **lateral**             | `+lateral`                                                 | l, ɭ, ʎ              |
| **rhotic**              | `+consonantal, +sonorant, nasal: none, lateral: none`      | r, ɾ, ɹ              |
| **stop**                | `-continuant`                                              | p, t, k              |
| **fricative**           | `+continuant, -sonorant`                                   | f, s, x              |
| **affricate**           | `continuant: ->+` (a closure-to-release contour)           | t͡s, t͡ʃ, d͡ʒ           |
| **sonorant**            | `+sonorant`                                                | vowels, glides, m, l |
| **obstruent**           | `-sonorant`                                                | stops, fricatives    |

### Reference tables

**Coronal place** (`front`, its `anterior`/`posterior` children, and
`retroflex`), by consonant:

|             | `anterior`      | `posterior`          | `aperture: high` |
| ----------- | --------------- | -------------------- | ---------------- |
| _unmarked_  | lamino-alveolar | palato-alveolar      | palatal          |
| `apical`    | apico-alveolar  | apico-postalveolar   | -                |
| `retroflex` | -               | sub-apical retroflex | -                |

**Vowel space** (`aperture` `high`/`mid`/`low` × `front`/_unmarked_/`back`
backness, each cell unrounded • rounded via `labial`/`rounded`). `mid` is the
scalar's middle value `aperture: mid` (0), not an absent feature:

| `aperture` |       | `front` | _unmarked_ | `back` |
| ---------- | ----- | ------- | ---------- | ------ |
| `high`     | `ATR` | i • y   | ɨ • ʉ      | ɯ • u  |
| `high`     | `RTR` | ɪ • ʏ   | -          | - • ʊ  |
| `mid`      | `ATR` | e • ø   | ɘ • ɵ      | ɤ • o  |
| `mid`      | `RTR` | ɛ • œ   | ɜ • ɞ      | ʌ • ɔ  |
| `low`      | `ATR` | æ • -   | ɐ          | -      |
| `low`      | `RTR` | a • ɶ   | -          | ɑ • ɒ  |

**ə sits outside the grid**: the reduction vowel is *featureless* — no `oral`
node at all, so no backness, aperture, advancement, or rounding (the vowel
counterpart of the placeless glottals ʔ/h). Match it with `[+syllabic,
aperture: none]`; derive it by clearing (`[oral: none]`) or by writing the
letter `ə`. Deliberate consequence: ə is *not* in the `aperture: mid` class,
so mid-vowel rules skip the reduction vowel unless they say otherwise.

The same `front`/`back`/`aperture` features, read as consonant place instead
of vowel quality. Back consonants split by height exactly as back vowels do:
`aperture: high` is velar, `aperture: mid` (with `advancement: rtr`) is uvular,
`aperture: low` is pharyngeal:

|                        | `front` | _unmarked_ | `back`  |
| ---------------------- | ------- | ---------- | ------- |
| `aperture: high`       | i, j, c | -          | u, w, k |
| `aperture: mid`, `RTR` | -       | -          | ʌ, ʁ, q |
| `aperture: low`, `RTR` | -       | -          | ɑ, ʕ, ʡ |

**Laryngeal settings** (`voice`, `glottal_aperture`, `tension`,
`larynx_height`) for the common phonation types:

|                                 | `voice` | `glottal_aperture` | `tension` | `larynx_height` |
| ------------------------------- | ------- | ------------------ | --------- | --------------- |
| /p/ plain voiceless             | -       | 0                  | 0         | 0               |
| /b/ plain voiced                | +       | 0                  | 0         | 0               |
| /pʰ/ voiceless aspirated        | -       | +1 spread          | 0         | 0               |
| /bʱ/ voiced aspirated / breathy | +       | +1 spread          | -1 slack  | 0               |
| /p͈/ Korean "tense"              | -       | 0                  | +1 stiff  | 0               |
| /pʼ/ ejective                   | -       | -1 constricted     | +1 stiff  | +1 raised       |
| /ɓ/ implosive                   | +       | 0                  | -1 slack  | -1 lowered      |
| /ʔ/ glottal stop                | -       | -1 constricted     | +1 stiff  | 0               |
| /h/ voiceless glottal fricative | -       | +1 spread          | 0         | 0               |
| /ɦ/ breathy glottal             | +       | +1 spread          | -1 slack  | 0               |

## How this differs from standard (SPE) feature theory

The inventory is closer to Feature Geometry and Dependency/Government
Phonology than to the flat binary matrix of _The Sound Pattern of English_.
The concrete departures from an SPE-style baseline:

- **Privative, not binary, by default.** SPE gives (almost) every feature a
  `+`/`−` opposition; here most features are **unary** — present or absent,
  with no negative value (`nasal`, `labial`, `lingual`, `front`, `back`,
  `rounded`, `lateral`, `strident`, `anterior`, …). Only five
  are binary (`syllabic`, `consonantal`, `sonorant`, `continuant`, `voice`)
  and the rest scalar. A pattern rule matches the absence of a unary feature
  with `[feature: none]`, and a binary's negative pole with `[-feature]` —
  these are **not** interchangeable (a binary feature like `syllabic` is
  always present with value `+` or `-`, never absent, so `[syllabic: none]`
  matches nothing).

- **Vowels, semivowels, and glides are three distinct classes**, separated by
  `consonantal` and `syllabic`:

  | class         | example  | `consonantal` | `syllabic` |
  | ------------- | -------- | ------------- | ---------- |
  | vowel         | `i`, `u` | `-`           | `+`        |
  | **semivowel** | `i̯`, `u̯` | `-`           | `-`        |
  | **glide**     | `j`, `w` | `+`           | `-`        |

  SPE treats glides as `[-consonantal]` and draws no semivowel/glide line. Here
  a **semivowel** (`i̯`/`u̯`, the non-syllabic member of a diphthong, made with
  the `̯` diacritic that adds `-syllabic` to a vowel) stays `[-consonantal]` —
  a vocalic off-glide — while a **glide** (`j`/`w`) is a genuine
  `[+consonantal]` approximant. So `au̯` is a vowel + semivowel diphthong,
  whereas `aw` is a vowel followed by a consonantal glide; the two behave
  differently under rules keyed on `[-consonantal]` (e.g. intervocalic
  voicing, which sees through a semivowel but not a glide).

- **Vowel height is one scalar `aperture`** (`-1 low`, `0 mid`, `1 high`), not
  two features `[±high]`/`[±low]`. SPE mid vowels are `[-high, -low]`; here a mid
  vowel (`e`, `ɛ`, `o`, `ɔ`) carries the explicit middle value `aperture: mid`.
  A segment has at most one aperture value, so — as with `advancement` — the
  height opposition can't be self-contradictory (`+hi +lo`) and there is no
  "empty height node" to leave behind. Rules write `aperture: high` /
  `aperture: mid` / `aperture: low`; to derive a mid vowel from a high or low
  one, write `[aperture: mid]`. (Back consonants use the same scale: `aperture:
high` velar, `aperture: mid` uvular, `aperture: low` pharyngeal — see the place
  tables above.) Dropping height entirely — say, when a palatalized consonant
  depalatalizes — is `[aperture: none]`, which unspecifies the feature; on a
  vowel you almost always want `aperture: mid` instead, since every full vowel
  carries a height (the sole exception is the featureless ə, next bullet).

- **ə is the featureless vowel.** The reduction vowel carries no `oral` node at
  all — no backness, aperture, advancement, or rounding — making it the vowel
  counterpart of the placeless glottals (ʔ, h). Absence is safe here because a
  single letter *owns* it: `[+syllabic, aperture: none]` matches exactly ə, and a
  reduction that clears a vowel's quality (`[oral: none]`) lands on ə as an exact
  hit rather than a closest-match guess. Deliberate consequence: ə is not a
  member of the `aperture: mid` class, so rules on true mid vowels skip the
  reduction vowel by construction.

- **Tongue root is one scalar `advancement`** (`-1 rtr`, `0 neutral`, `1 atr`),
  not two features `[±ATR]`/`[±RTR]`. A segment has at most one advancement
  value, so the ATR/RTR opposition can't be self-contradictory. Rules write
  `advancement: atr` / `advancement: rtr` (the `ATR`/`RTR` labels in the vowel
  tables above are these two poles). Consonants carry `advancement` only where
  it is class-defining: the gutturals (uvulars, pharyngeals, epiglottals) are
  `advancement: rtr` — the retracted tongue root is what unites them, and what
  lets lax vowels and gutturals interact in one rule (emphatic lowering as an
  rtr spread). Palatals and coronals carry no `advancement`: they don't contrast
  root position, and the palatal class is already exactly `+front, aperture:
  high`. The criterion: **a scalar is specified where it contrasts or defines a
  class, and absent where the dimension is inapplicable.**

- **Length and the laryngeal dimensions are scalar**, not several binary
  features: `length` (short/long/overlong) instead of `[±long]`, and
  `glottal_aperture`, `tension`, `larynx_height` (each `-1`/`0`/`+1`) instead
  of separate `[±spread glottis]`, `[±constricted glottis]`, `[±stiff/slack
vocal folds]`.

- **Affricates are a `continuant` contour, not a `[delayed release]`
  feature.** `t͡s`, `t͡ʃ`, `d͡z`, `d͡ʒ` are single letters whose `continuant`
  value is the contour `->+` — a `-continuant` closure moving to a
  `+continuant` release — where SPE would write `[-continuant, +delayed
release]`. There is no separate affricate/`delrel` feature. So the SPE
  deaffrication `[+delrel] > [-delrel]` is written by collapsing the contour to
  plain `[+continuant]`: `[continuant: ->+] → [+continuant]` turns every
  affricate into its matching fricative (`t͡s→s`, `d͡ʒ→ʒ`, …), place, voicing,
  and any palatalization preserved.

- **No `[coronal]` articulator feature.** Coronal place is `[+lingual, +front]`
  — the same `front` node a front vowel uses — rather than a dedicated
  `[coronal]` node as in Feature Geometry.

- **One place hierarchy for vowels and consonants** (see the section above):
  vowel quality and consonant place share the `oral`/`lingual`/`labial` nodes,
  rather than the separate vowel features (`[±high, ±low, ±back, ±round]`) and
  consonant place features SPE keeps largely apart.

- **`tone` and `stress` live on autosegmental tiers**, not in the segment
  bundle (see the note under _Feature geometry_). Keeping them off the melody is
  what lets a stress/tone diacritic on a rule literal be handled apart from the
  vowel — constraining the match in the target, writing the syllable's value in
  the result. That is engine notation, not a modelling choice; see §5.1 of the
  user guide.

None of this is baked into the engine — it is the modelling style of
`projects/default`. A project may adopt an SPE-style all-binary inventory, or
any other, by writing its own `features.toml`.

## Letters, diacritics, sonority, and syllable structure

- **`letters.csv`** maps each IPA symbol to a full feature bundle — one row
  per segment, one column per feature (every feature the system declares,
  segmental and syllabic alike; a blank cell is unspecified).

- **`diacritics.toml`** maps a combining mark or spacing diacritic to a
  partial bundle that modifies whatever base segment it attaches to,
  tagged with the tier it targets (`segment` or `syllable`) and its `kind`:
  `before`/`after` (a spacing mark adjacent to the base) or `combining` (a
  true Unicode combining diacritic). Stress marks (`ˈ`, `ˌ`) additionally
  set `marks_boundary = true`; the tone diacritics and tone letters are
  `read_only` or `contour`-aware where relevant, since tone is rendered
  back out rather than re-parsed the same way it was written.

- **`sonorities.toml`** assigns each segment a sonority level by first-match
  against an ordered list of feature-bundle predicates. The default scale
  has eight levels — vowel, semivowel, glide, rhotic, lateral, nasal,
  fricative, stop — each a one-line bundle (e.g. a rhotic is `consonantal: +,
sonorant: +, nasal: none, lateral: none`; a glide adds `aperture: !none` to
  that, ranking j/w above rhotics). A glide is defined by *having* a
  tongue-body place, not by being high: j/w pair with i/u, and a pharyngeal
  ʕ̞ or uvular ʁ̞ approximant (the consonantal counterparts of ɑ and ʌ) would
  classify as glides too, while the coronal/labial approximants ɹ, ʋ (no
  `aperture`) stay rhotic-level. Sonority is *intrinsic to the segment
  type*; syllabicity is positional and lives in `syllable_parts.toml`. So a
  syllabic consonant (PIE r̩, l̩, n̩, m̩) keeps its consonantal sonority and is a
  nucleus anyway — nuclei are found by the `+syllabic` pattern, and a nucleus's
  own sonority level is never consulted (levels drive only the split of the
  clusters *between* nuclei). Ranking r̩ with the vowels would erase the very
  fact that makes vowels better nuclei than sonorants.

- **`syllable_parts.toml`** is time-keyed, like rules: the nucleus
  (`+syllabic`) is defined from the start, but the shipped default only
  switches on explicit onset/coda _patterns_ at `t = 500` — a Latin-style
  grammar (_s_+stop+liquid, _s_+stop, obstruent+liquid, or any single
  consonant). Before that time, syllabification falls back to sonority and
  the Maximal Onset Principle, which is also what a project with no
  `syllable_parts.toml` onset/coda entries at all gets throughout. See
  `user_guide.md` §7 for the general mechanism.
