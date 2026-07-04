# Source of the Latin → French rules

`rules.toml` in this project is a hand-translation of the **DiaCLEF2025** sound-change
cascade from **DiaSim**, saved here verbatim as `DiaCLEF2025.source.txt` for reference.

- **Upstream:** <https://github.com/clmarr/DiaSim> (branch `gamma`), file `DiaCLEF2025`.
- **License:** DiaSim is GPL-3.0. `DiaCLEF2025.source.txt` is an unmodified copy.
- **Provenance:** DiaCLEF encodes Mildred Katherine Pope's _From Latin to Modern
  French_ (1934); rule comments cite Pope section numbers (`s220`, `p130 s308-9`, …).
- **Lexicon:** `words.toml` (448 words) is a base of ~200 FLLexPlus2024 entries plus
  the **full FLLAPS** set (`reference/FLLAPS.source.txt`, DiaSim's multi-stage dataset;
  all active, derivable words ingested — see `tools/ingest_fllaps.py`; the irregular
  _août_ is excluded and homophone-input doublets deduped). Attested Modern French IPA
  is the accuracy target in `correctness.md`.

## FLLAPS — the multi-stage attested dataset (`reference/FLLAPS.source.txt`)

FLLAPS (same repo/branch as DiaCLEF) gives, per word, **six attested forms** — Classical
Latin, Late-Latin/Gallo-Romance, early Old French, later Old French, Middle French,
Modern French — comma-separated, space-tokenized phonemes, `$gloss` + notes; `$`-leading
lines are disabled entries. Because the intermediate columns are _attested_ (not computed),
they localize which historical **period** a derivation first diverges — the tool for
improving the rule translation, not just the final score. `tools/stagediff.py` aligns
Fortis's per-period output to these columns (empirically: FLLAPS c1↔time 300, c2↔600/750,
c3↔1000, c4↔1200, c5↔1400) and reports the first real divergence per word.

## Reading the source notation (for comparing against the Fortis port)

- Stages are marked by `=`/`~` header lines (Classical Latin → Late Latin → Early/
  Middle/Later Gallo-Roman → Early/Later Old French → Old French II → Middle French).
- `A > B / C __ D` is a rule; `$` begins a comment; `{a;b}` is an alternation;
  `@` is a word boundary in a context; feature bundles are `[+hi,-cont,…]`.
- A **bare vowel literal means _unstressed_** in DiaSim; in Fortis a bare literal
  matches any stress (stress is a separate tier) — mind this when porting deletions.
- Translation conventions and the known divergences are documented in
  [`../../docs/latin_to_french_review.md`](../../docs/latin_to_french_review.md).
