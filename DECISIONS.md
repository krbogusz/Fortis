# Decisions

Each entry records a choice, its date, its reason and the options rejected. Entries are only
appended. To reverse a choice, add an entry that names the one it replaces.

## 2026-10-06: Keep the source review out of git

**Choice:** The nine source reports on `pie_to_english` live in `docs/source_review/`, which
`.gitignore` excludes.

**Reason:** The reports quote the copyrighted reference books briefly. The other planning notes in
`docs/` are kept out of git for the same kind of reason.

**Rejected:** Leaving the reports in the session scratchpad, which is deleted after the session.

## 2026-10-06: Correct attested targets with a citation, in four cases

**Choice:** In `pie_to_english`, a 900, 1400 or final target may be corrected when a cited source
shows one of these:

1. Transcription convention: the target breaks the column's convention, for example a General
   American form in the RP column.
2. Dialect variant: the target records a dialect form that the later columns do not continue.
3. Wrong word: the target belongs to a different word.
4. No modern reflex: the modern target is a loan or a different formation. The target is removed.

SOURCE.md forbids this today. It is amended in the commit that makes the first such correction.

**Reason:** The source review found about 22 targets that the sources call wrong, for example
free and theed with a south-western /øː/, two with the form of twain, and tale with a non-RP
/eː/. Three earlier commits (finger, atter, tallow) already corrected the transcription
convention of final targets.

**Rejected:**
- Keeping the rule that attested targets are never touched.
- Allowing only the convention and dialect cases.

## 2026-10-06: Decide each Ringe–Kroonen conflict on its evidence

**Choice:** Where Ringe and Kroonen disagree about a sound law or a reconstruction, each case is
tested and decided on its own, and the decision is recorded here.

**Reason:** Kroonen's Mahlow's law, Kluge's law after Verner, and Holtzmann's law explain
several 200 errors that Ringe's account leaves open. A fixed ranking would discard them untested.

**Rejected:** The fixed ranking Ringe > Kroonen > Wiktionary, stated in
`projects/pie_to_english/tools/build_chains.py`.

## 2026-10-06: Gather more data for pie_to_english

**Choice:**
1. Fill missing targets at the existing checkpoints (900, 1400, final) for words already in the
   lexicon. Existing forms are not changed.
2. Add a Proto-West Germanic checkpoint near 400, and an Early Modern English checkpoint between
   1621 (Gil) and 1687 (Cooper). Each exact year is set so that no rule shares it.
3. Add new words from Wiktionary chains. Existing entries are not changed.
4. Keep the 900 and 1400 years. The rule dates are calibrated to them, and no new evidence asks
   for a move.

**Reason:** The cascade is scored at only four points, and two legs are long. Of the 73 errors
that arise inside the English legs, 30 arise between 200 and 900. More checkpoints show where
inside a leg a derivation goes wrong. More words test the rules on more data.

**Rejected:** Gathering only from the books in `sources/`, which would limit the work to the
Early Modern checkpoint and a few targets.

## 2026-10-06: Transcribe clear Middle English spellings

**Choice:** Where Wiktionary gives a Middle English spelling without IPA, the 1400 target may be
transcribed from the spelling when its reading is unambiguous. The transcription follows the
spelling conventions in Minkova and Jones, and each form's note says it is a transcription.

**Reason:** 69 words have a Middle English spelling but no 1400 target.

**Rejected:** Adding 1400 targets only where Wiktionary or a book gives the pronunciation.

## 2026-10-06: Rebuild the Wiktionary cache from kaikki.org

**Choice:** Download the kaikki.org extracts and the frequency list again into
`projects/pie_to_english/.cache/`, which git ignores.

**Reason:** The cache was not moved with the project. The bootstrap tools need it to fill gaps,
to add the 400 checkpoint and to add words. Wiktionary has changed since the bootstrap, so new
data may differ from the data the lexicon was built from.

**Rejected:** Working from the books only.
