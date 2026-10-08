# Induction — `projects/latin_to_french`

Each interval's rule cascade, induced by greedy MDL boosting from the attested source
forms toward the attested targets. A rule is accepted only when it strictly lowers the
description length `L = fit_bits + rule_bits` — the bits it saves in the residual must
exceed the bits it costs to write. `ΔL` is that change (negative = a net saving), split
into its fit and rule-cost parts. `place` is where the rule was inserted in the
cascade (`append`, or `@i` when the placement search found an earlier slot fed a later
rule).

## Interval `input→300`

**1 → 26 / 304 exact** (9%), fit **1444423014 → 647117014** bits, **2 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `m → ∅ / _ #` | -671310537 | -671310563 | 26 | 208 | 1→6 | append |
| 2 | `u → o` | -125995406 | -125995437 | 31 | 113 | 6→26 | append |

## Interval `300→1000`

**0 → 5 / 304 exact** (2%), fit **1869530551 → 1626384187** bits, **2 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `ɑ → ə` | -177726205 | -177726236 | 31 | 190 | 0→4 | append |
| 2 | `ˈə → ˈeː` | -65420098 | -65420129 | 31 | 122 | 4→5 | append |

## Interval `1000→1200`

**52 → 50 / 303 exact** (17%), fit **700467720 → 482018004** bits, **2 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `ˈi → j / _ [advancement: atr]` | -52112167 | -52112207 | 40 | 35 | 52→52 | append |
| 2 | `j → ˈɛ / [+syllabic] _` | -166337469 | -166337509 | 40 | 44 | 52→50 | append |

## Interval `1200→1500`

**159 → 153 / 300 exact** (51%), fit **623688063 → 418051508** bits, **2 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `n̪ → ˈãː / [nasal] _` | -147223387 | -147223426 | 40 | 75 | 159→153 | append |
| 2 | `ˈãː → ˈũː / [aperture: high] _ #` | -58413086 | -58413128 | 43 | 15 | 153→153 | append |

## Interval `1500→final`

**0 → 0 / 300 exact** (0%), fit **1154751006 → 788263507** bits, **2 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `r → ʁ` | -325241873 | -325241904 | 31 | 133 | 0→0 | append |
| 2 | `ə → ∅ / _ #` | -41245568 | -41245595 | 26 | 95 | 0→0 | append |

## Phase B — global refinement

Composed cascade run from the true inputs over the whole lexicon: L **8844988175 → 6103954093**, final exact **0 → 0 / 304**.

**Final-residual boosting** appended 20 rule(s):

- `e → ɛ`
- `[back, -consonantal, +continuant, glottal, glottal_aperture: neutral, larynx_height: neutral, length: long, lingual, manner, oral, +sonorant, +syllabic, tension: neutral, +voice] → [length: short]`
- `ˈeː → ˈa / _ [glottal_aperture: neutral]`
- `m → ∅ / _ #`
- `ˈa → ˈe / _ [-continuant]`
- `t̪ → ∅ / [advancement: atr] _`
- `n̪ → ∅ / _ [+consonantal]`
- `l → ∅ / _ [+consonantal]`
- `o → ∅ / [advancement: rtr] _`
- `ɛ → ∅ / [back] _ [advancement: rtr]`
- `m → ∅ / _ #`
- `i → e`
- `ˈo → ˈu / _ [+sonorant]`
- `ˈa → ˈeː / [front] _`
- `l → ∅ / [advancement: atr] _`
- `ˈeː → ˈe`
- `n̪ → ∅ / [front] _`
- `ˈe → ∅ / [strident] _ [-sonorant]`
- `k → ∅ / _ [-sonorant]`
- `ɛ → e / [-sonorant] _`
