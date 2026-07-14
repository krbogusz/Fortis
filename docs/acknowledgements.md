# Acknowledgements and data sources

Fortis is a general engine and ships no built-in phonology. The engine code is original; the
`projects/latin_to_french` and `projects/pie_to_english` examples and their accuracy datasets
draw on external work (data with its own licence), and `projects/halle_vaux_wolfe` and
`projects/spe` follow published feature systems (academic citations) — all recorded here for
attribution. Per-project provenance also lives beside the data:
[`projects/latin_to_french/SOURCE.md`](../projects/latin_to_french/SOURCE.md),
[`projects/pie_to_english/SOURCE.md`](../projects/pie_to_english/SOURCE.md),
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

## Wiktionary — the PIE → English lexicon

- **Source:** [Wiktionary](https://www.wiktionary.org/) contributors, via the
  [kaikki.org](https://kaikki.org/) machine-readable extracts (produced by
  [wiktextract](https://github.com/tatuylonen/wiktextract), MIT — the *tool* is MIT; the *data*
  is Wiktionary's).
- **Use:** `projects/pie_to_english/words.csv` — the reconstructed Proto-Indo-European inputs and
  the attested Proto-Germanic / Old English / Middle English / Modern English forms it is scored
  against. Built by `projects/pie_to_english/tools/`.
- **Licence:** **CC BY-SA 4.0**, and it is *share-alike*: the derived lexicon carries the same
  licence, and so must any redistribution of it. The project's `rules.toml` and `tools/` are
  original work and stay under the repo's own licence.
- English word frequencies from [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords)
  (`2018/en/en_50k`, MIT; OpenSubtitles token counts).

### The four reference books are NOT redistributed

The PIE → English rules are checked against Minkova, *A Historical Phonology of English*; Ringe,
*From Proto-Indo-European to Proto-Germanic*; Ringe & Taylor, *The Development of Old English*;
and Kroonen, *Etymological Dictionary of Proto-Germanic*. These are copyrighted books. They are
**read and cited, never redistributed** — `.gitignore` keeps `projects/pie_to_english/sources/`
out of the repo. A sound law is a fact and is encoded as a rule, with the citation in a comment;
no book text belongs in the repository.

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
| PIE→English lexicon `projects/pie_to_english/words.csv` (from Wiktionary)                    | CC BY-SA 4.0 (share-alike)              |
| PIE→English `rules.toml` + `tools/` (original)                                               | PolyForm Noncommercial 1.0.0            |
| French / English frequency lists                                                             | MIT (hermitdave/FrequencyWords)         |

Descriptive, not a legal instrument — consult each upstream project's own licence.
