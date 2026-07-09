# Source of the Latin → French project

`rules.toml` here is a hand re-authoring, in Fortis notation, of the **DiaCLEF2025**
sound-change cascade from **DiaSim** — a re-expression of the same ordered changes, not a
mechanical copy.

- **Upstream:** <https://github.com/clmarr/DiaSim> (branch `gamma`), the `DiaCLEF2025` cascade.
  Authors: Clayton Marr & David R. Mortensen.
- **Licence:** DiaSim is **GPL-3.0**; the port is a derivative work and carries that licence.
- **Source text:** the verbatim DiaCLEF cascade is not redistributed in the committed repo —
  fetch it from the upstream repository above.

See [`../../docs/acknowledgements.md`](../../docs/acknowledgements.md) for the project's overall
provenance and licensing.

## Lexicon and accuracy targets (`words.csv`)

`words.csv` holds **304 words**. Columns: `word` (the Classical-Latin IPA input), `gloss`,
`frequency` (see below), then the attested forms at **300, 1000, 1200, 1500** and the modern
**final** surface. These attested forms come from DiaSim's companion **FLLAPS** dataset (with
additional entries from **FLLexPlus2024**), also part of DiaSim and GPL-3.0.

FLLAPS gives, per word, **six attested forms** across the timeline — Classical Latin, Late
Latin/Gallo-Romance, early and later Old French, Middle French, and Modern French. Because the
intermediate columns are *attested*, not computed, they let the engine measure accuracy at each
historical checkpoint — and localise which period a derivation first diverges — rather than
only scoring the modern surface.

## Word frequency (`words.csv` `frequency` column)

Per-word token weights come from **hermitdave/FrequencyWords**, the modern French 2018
top-50k list.

- **Upstream:** <https://github.com/hermitdave/FrequencyWords> — `content/2018/fr/fr_50k.txt`
  (`word count`, one per line, descending). **MIT**-licensed.
- **Underlying corpus:** OpenSubtitles 2018 token counts via the OPUS project
  (<https://opus.nlpl.eu/>) — spoken-register frequencies.
- **Method:** joined to each row's `gloss` (NFC-normalised, lower-cased). **282 / 304 matched**;
  the rare/archaic misses (`git`, `aulx`, `effriter`, `moyeu`, …) default to weight **1**.
  Raw subtitle counts. Fetched 2026-07-09.
- **Use:** token-frequency-weighted accuracy, and prioritising sporadic/lexical-change
  candidates (high-frequency words erode off the regular sound laws — e.g. the auxiliary
  _ai_ < habeō → /e/, not the regular affricate reflex).

## Reading the DiaCLEF notation (for comparing against the Fortis port)

- Stages are marked by `=`/`~` header lines (Classical Latin → Late Latin → Early/Middle/Later
  Gallo-Roman → Early/Later Old French → Old French II → Middle French).
- `A > B / C __ D` is a rule; `$` begins a comment; `{a;b}` is an alternation; `@` is a word
  boundary in a context; feature bundles are `[+hi,-cont,…]`.
- A **bare vowel literal means _unstressed_** in DiaSim; in Fortis a bare literal matches any
  stress (stress is a separate tier) — mind this when porting deletions.
- Translation conventions and known divergences from the DiaCLEF source are recorded inline in
  `rules.toml`'s per-rule `description` fields.
