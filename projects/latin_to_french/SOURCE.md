# Source of the Latin → French rules

`rules.toml` in this project is a hand-translation of the **DiaCLEF2025** sound-change
cascade from **DiaSim**, saved here verbatim as `DiaCLEF2025.source.txt` for reference.

- **Upstream:** <https://github.com/clmarr/DiaSim> (branch `gamma`), file `DiaCLEF2025`.
- **License:** DiaSim is GPL-3.0. `DiaCLEF2025.source.txt` is an unmodified copy.
- **Provenance:** DiaCLEF encodes Mildred Katherine Pope's *From Latin to Modern
  French* (1934); rule comments cite Pope section numbers (`s220`, `p130 s308-9`, …).
- **Lexicon:** the sample in `words.toml` is drawn from FLLexPlus2024 (DiaSim's
  companion dataset), whose attested Modern French IPA is the accuracy target in
  `correctness.md`.

## Reading the source notation (for comparing against the Fortis port)

- Stages are marked by `=`/`~` header lines (Classical Latin → Late Latin → Early/
  Middle/Later Gallo-Roman → Early/Later Old French → Old French II → Middle French).
- `A > B / C __ D` is a rule; `$` begins a comment; `{a;b}` is an alternation;
  `@` is a word boundary in a context; feature bundles are `[+hi,-cont,…]`.
- A **bare vowel literal means *unstressed*** in DiaSim; in Fortis a bare literal
  matches any stress (stress is a separate tier) — mind this when porting deletions.
- Translation conventions and the known divergences are documented in
  [`../../docs/latin_to_french_review.md`](../../docs/latin_to_french_review.md).
