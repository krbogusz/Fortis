# Acknowledgements and data sources

Fortis is a general engine and ships no built-in phonology. The engine code is original; the
`projects/latin_to_french` example and its accuracy dataset draw on external work, recorded
here for attribution. Per-project provenance also lives beside the data:
[`projects/latin_to_french/SOURCE.md`](../projects/latin_to_french/SOURCE.md).

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

## Licensing note

Fortis (engine + original docs) is **CC BY-NC 4.0** ([`LICENSE`](../LICENSE)).

| Material                                                                             | Licence                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------ |
| Fortis engine + docs                                                                 | CC BY-NC 4.0                                     |
| Derived Latin→French `rules.toml` + lexicon (from DiaSim's DiaCLEF2025 / FLLAPS / FLLexPlus) | GPL-3.0 (derivative of GPL-3.0 sources) |
| French frequency list                                                                | MIT (hermitdave/FrequencyWords)                  |

Descriptive, not a legal instrument — consult each upstream project's own licence.
