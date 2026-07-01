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
│   └── lingual    (unary)
│       ├── apical    (unary)
│       ├── retroflex  (unary)
│       ├── front     (unary)
│       │   ├── anterior (unary)
│       │   └── posterior (unary)
│       ├── back      (unary)
│       ├── aperture  (unary)
│       │   ├── high (unary)
│       │   └── low  (unary)
│       └── advancement (unary)
│           ├── ATR (unary)
│           └── RTR (unary)
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
with more than two contrastive levels (`length`, tone, stress, and the three
laryngeal dimensions). Setting a parent node — `[oral: none]`, `[place:
none]` — unspecifies every child simultaneously; this is the mechanism
behind debuccalisation (a placeless, glottal segment).

## Vowels and consonants share one feature space

There is no separate "vowel feature system." A segment's status as a vowel
or a consonant comes from `syllabic` and `consonantal` (plus `sonorant` and
`manner`), not from a different set of place features — vowel quality and
consonant place of articulation are expressed through the _same_ `oral` /
`lingual` / `labial` nodes. Pulled directly from `letters.csv`:

| Segment                         | Active features                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| `/k/` (voiceless velar stop)    | `-syllabic, +consonantal, -continuant, +lingual, +back, +aperture, +high`                          |
| `/u/` (high back rounded vowel) | `+syllabic, -consonantal, +continuant, +labial, +rounded, +lingual, +back, +aperture, +high, +ATR` |
| `/i/` (high front vowel)        | `+syllabic, -consonantal, +continuant, +lingual, +front, +aperture, +high, +ATR`                   |
| `/t/` (voiceless alveolar stop) | `-syllabic, +consonantal, -continuant, +lingual, +front, +anterior`                                |
| `/a/` (low vowel)               | `+syllabic, -consonantal, +continuant, +lingual, +front, +low, +RTR`                               |

`/k/` and `/u/` both carry `lingual, back, aperture, high` — the identical
dorsal place specification. What makes `/u/` a rounded back **vowel** rather
than a velar **consonant** is `+syllabic, -consonantal` plus the added
`labial, rounded` (rounding is the same `labial` node a consonant like `/p/`
uses for bilabial place); what makes `/k/` a stop rather than a vowel is
`-syllabic, +consonantal, -continuant`. Likewise `/i/` and `/k/` share
`lingual, aperture, high`, differing in `front` vs. `back` and in the
syllabic/consonantal/continuant features that set the vowel/consonant and
manner distinctions. `/t/`'s coronal place (`lingual, front, anterior`) uses
the same `front` node a front vowel like `/i/` or `/a/` sets, just with the
`anterior`/`posterior` children (relevant only to consonantal place)
additionally specified.

This is a deliberate design choice — a single place hierarchy that both
segment classes draw from — not a requirement of the engine; a project is
free to give vowels and consonants entirely separate feature sets if that
suits its data better.

### Reference tables

**Coronal place** (`front`, its `anterior`/`posterior` children, and
`retroflex`), by consonant:

|             | `anterior`      | `posterior`          | `high` (no children) |
| ----------- | --------------- | -------------------- | -------------------- |
| _unmarked_  | lamino-alveolar | palato-alveolar      | palatal              |
| `apical`    | apico-alveolar  | apico-postalveolar   | -                    |
| `retroflex` | -               | sub-apical retroflex | -                    |

**Vowel space** (`front`/_unmarked_/`back` × `high`/_unmarked_/`low`, each
cell unrounded • rounded via `labial`/`rounded`):

|            |       | `front` | _unmarked_ | `back` |
| ---------- | ----- | ------- | ---------- | ------ |
| `high`     | `ATR` | i • y   | ɨ • ʉ      | ɯ • u  |
| `high`     | `RTR` | ɪ • ʏ   | -          | - • ʊ  |
| _unmarked_ | `ATR` | e • ø   | ɘ • ɵ      | ɤ • o  |
| _unmarked_ | -     |         | ə          |        |
| _unmarked_ | `RTR` | ɛ • œ   | ɜ • ɞ      | ʌ • ɔ  |
| `low`      | `ATR` | æ • -   | ɐ          | -      |
| `low`      | `RTR` | -       | a • ɶ      | ɑ • ɒ  |

The same `front`/`back`/`high` nodes, read as consonant place instead of
vowel quality (coronal and dorsal consonants aren't marked for
`advancement`):

|                   | `front` | _unmarked_ | `back`  |
| ----------------- | ------- | ---------- | ------- |
| `high`            | i, j, c | -          | u, w, k |
| _unmarked_, `RTR` | -       | -          | ʌ, ʁ, q |
| `low`, `RTR`      | -       | -          | ɑ, ʕ, ʡ |

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
  has seven levels — vowel, glide, rhotic, lateral, nasal, fricative, stop
  — each a one-line bundle (e.g. a rhotic is `consonantal: +, sonorant: +,
nasal: none, lateral: none`).

- **`syllable_parts.toml`** is time-keyed, like rules: the nucleus
  (`+syllabic`) is defined from the start, but the shipped default only
  switches on explicit onset/coda _patterns_ at `t = 500` — a Latin-style
  grammar (_s_+stop+liquid, _s_+stop, obstruent+liquid, or any single
  consonant). Before that time, syllabification falls back to sonority and
  the Maximal Onset Principle, which is also what a project with no
  `syllable_parts.toml` onset/coda entries at all gets throughout. See
  `user_guide.md` §7 for the general mechanism.
