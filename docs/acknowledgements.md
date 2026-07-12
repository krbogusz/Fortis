# Acknowledgements and data sources

Fortis is a general engine and ships no built-in phonology. The engine code is original; the
`projects/latin_to_french` example and its accuracy dataset draw on external work (data with its
own licence), and `projects/halle_vaux_wolfe` and `projects/spe` follow published feature
systems (academic citations) — all recorded here for attribution. Per-project provenance also
lives beside the data: [`projects/latin_to_french/SOURCE.md`](../projects/latin_to_french/SOURCE.md),
[`projects/halle_vaux_wolfe/SOURCE.md`](../projects/halle_vaux_wolfe/SOURCE.md),
[`projects/spe/SOURCE.md`](../projects/spe/SOURCE.md).

## DiaSim / DiaCLEF2025 — the Latin → French rules

- **Upstream:** [DiaSim](https://github.com/clmarr/DiaSim), branch `gamma`, the `DiaCLEF2025`
  cascade. Authors: Clayton Marr & David R. Mortensen (Marr & Mortensen 2020, 2022).
- **Licence:** **GPL-3.0**.
- **Use:** `rules.toml` is a hand re-authoring of that cascade in Fortis notation — a
  re-expression of the same ordered changes, not a mechanical copy. The DiaCLEF source itself
  is not redistributed here; fetch it from the upstream repository above.

## FLLAPS / FLLexPlus2024 — attested per-stage data

- Part of DiaSim (same repo/branch); **GPL-3.0**.
- **FLLAPS** (→ `words.csv`): six attested forms per word across the timeline — the accuracy
  targets at each historical checkpoint, not just the modern surface. **FLLexPlus2024** adds
  lexical entries.

## Word frequencies — hermitdave/FrequencyWords

- **Upstream:** [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords),
  `content/2018/fr/fr_50k.txt`; **MIT**.
- **Corpus:** OpenSubtitles 2018 via [OPUS](https://opus.nlpl.eu/) (spoken-register counts).
- **Use:** the `frequency` column in `words.csv` (token-weighted accuracy; sporadic-change
  candidates). 282/304 matched; the rest default to weight 1.

## Halle, Vaux & Wolfe (2000) — the halle_vaux_wolfe feature geometry

- **Source:** Morris Halle, Bert Vaux & Andrew Wolfe (2000), _On Feature Spreading and the
  Representation of Place of Articulation_, **Linguistic Inquiry** 31(3): 387–444.
- **Use:** `projects/halle_vaux_wolfe/features.toml` encodes the paper's feature geometry
  (their structure (1)), and the rules illustrate phenomena it discusses — place assimilation,
  Irish dorsal assimilation, Uyghur raising, Sibe uvularization, Palestinian emphasis, Igbo
  rounding. The inventory, lexicon, and rules are an original illustration built to exercise the
  geometry, **not** the paper's data. Provenance beside the data:
  [`projects/halle_vaux_wolfe/SOURCE.md`](../projects/halle_vaux_wolfe/SOURCE.md). An academic
  citation, not a licensed dataset — it does not affect the engine's licence.

## Chomsky & Halle (1968) — the spe feature system

- **Source:** Noam Chomsky & Morris Halle (1968), _The Sound Pattern of English_. New York:
  Harper & Row.
- **Use:** `projects/spe/features.toml` encodes the book's flat binary distinctive-feature
  matrix (no feature geometry), demonstrating that the engine requires none. The inventory,
  lexicon, and rules are an original illustration, **not** the book's data. Provenance beside
  the data: [`projects/spe/SOURCE.md`](../projects/spe/SOURCE.md). An academic citation, not a
  licensed dataset — it does not affect the engine's licence.

## Licensing note

Fortis (engine + original docs) is **PolyForm Noncommercial 1.0.0** ([`LICENSE`](../LICENSE)) —
noncommercial use only, with the copyright notice kept on any copy passed on.

| Material                                                                                     | Licence                                 |
| -------------------------------------------------------------------------------------------- | --------------------------------------- |
| Fortis engine + docs                                                                         | PolyForm Noncommercial 1.0.0            |
| Derived Latin→French `rules.toml` + lexicon (from DiaSim's DiaCLEF2025 / FLLAPS / FLLexPlus) | GPL-3.0 (derivative of GPL-3.0 sources) |
| French frequency list                                                                        | MIT (hermitdave/FrequencyWords)         |

Descriptive, not a legal instrument — consult each upstream project's own licence.
