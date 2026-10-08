# Source of the PIE → English project

Proto-Indo-European to Present-Day English, scored at nine checkpoints.

> **Licensing — this directory is not all under one licence.**
>
> - **`words.toml` is CC BY-SA 4.0.** It is derived from **Wiktionary**, whose text is CC BY-SA
>   4.0, and that licence is *share-alike*: the derived lexicon carries it too, and so must any
>   redistribution of it. Attribution: **[Wiktionary](https://www.wiktionary.org/) contributors**,
>   via the [kaikki.org](https://kaikki.org/) extracts.
> - **`rules.toml`, `tools/`, `SOURCE.md`** are original work and carry the repo's own
>   **PolyForm Noncommercial 1.0.0**, like the rest of Fortis.
> - **`sources/` is NOT in the repo and must never be.** It holds copyrighted reference books —
>   for PIE/PGmc: Ringe (*From PIE to Proto-Germanic*), Kroonen (*Etymological Dictionary of
>   Proto-Germanic*), Ringe & Taylor (*The Development of Old English*); for the English legs:
>   Minkova, Jones (*A History of English Phonology*), McMahon, Steponavičius, Plotkin, Pyles &
>   Algeo (*The Origins and Development of the English Language*), and the etymological
>   dictionaries of Hoad, Klein and Liberman. A sound
>   law is a fact, and facts are not copyrightable: they are **read and cited in the rule that
>   uses them, never redistributed** — `.gitignore` keeps the books out, and no book text belongs
>   in the tree. Because nothing here is redistributed, none of this appears in
>   `docs/acknowledgements.md` (which lists only the data we do redistribute).
> - **The final targets in `words.toml` come from CUBE** (seas3.elte.hu/cube), whose pages say
>   "© Geoff Lindsey & Péter Szigetvári" and state no licence. Each note names the source. The
>   project owner judged CUBE free to use, so the targets are published with credit in
>   `docs/acknowledgements.md` (DECISIONS.md, 2026-10-07, "Publish the CUBE targets with credit").

## Lexicon (`words.toml`) — CC BY-SA 4.0

**`words.toml` is the canonical, hand-maintained lexicon.** To correct a word — a wrong preform,
a transcription slip in a target, a stem-class fix — **edit `words.toml` directly** and record the
reason in that form's (or the word's) `note`. There is no "regenerate the gold" step.

It was *bootstrapped* once from the [kaikki.org](https://kaikki.org/) Wiktionary extracts (produced
by [wiktextract](https://github.com/tatuylonen/wiktextract), MIT; the *data* is Wiktionary's, CC
BY-SA 4.0) by `tools/build_chains.py` (kaikki → `chains.json`) and `tools/build_gold.py`
(`chains.json` → `words.toml`). Those tools, and the `PREFORM_FIXES` / `ATTESTED_FIXES` / `OE_FIXES`
tables inside `build_gold.py`, are kept as the **record of how the bootstrap was built and why each
early correction was made** — but they are NOT re-run over the committed `words.toml`, because that
would overwrite the hand corrections. New corrections go straight into `words.toml`.

**The kaikki extracts are not versioned** (~280 MB). Both tools read them from
`projects/pie_to_english/.cache/` — override with `FORTIS_PIE_CACHE` — and that directory is
gitignored. `tools/` being in the repo does not make the pipeline self-contained: with an empty
cache the extracts must be re-fetched from [kaikki.org](https://kaikki.org/) first
(`kaikki/{pie,pgmc,oe,me,pwgmc}.jsonl`), and then the derived files built in order:
`tools/ringe.py` (needs the Ringe PDF in `sources/`), `tools/build_chains.py`, then
`tools/pde_sounds.py`.

The spine is the **Proto-Germanic** extract. Each record carries its PIE parent (an `inh`
etymology template) and, usually, a `descendants` tree running down through Old English →
Middle English → English, so one record yields a whole chain and the OE/ME/English entries
supply the IPA for each checkpoint. Word frequencies come from
[hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) (`2018/en/en_50k`,
MIT; OpenSubtitles token counts), as in `latin_to_french`.

**The descendants tree is optional, and that is what makes the lexicon the size it is.** The
chain-builder used to skip any etymon with no attested Old English descendant, which quietly
threw away more than half the usable Proto-Germanic gold — every word that died before Old
English, or simply is not linked to one. But the 200 checkpoint is scored against the
*Proto-Germanic* form and needs a PIE parent and a Proto-Germanic IPA, nothing more. A chain
that stops at Proto-Germanic is a *complete* chain for that column. Lifting the requirement took
the lexicon from 114 rows (111 scorable at 200) to **249 rows, 240 scorable at 200**.

Each word is a `[[words]]` table with an `id`, a `gloss`, a `frequency`, and a `forms` array —
the PIE seed at **−2000** and the attested forms at **200** (Proto-Germanic), **403**
(Proto-West Germanic), **900** (Old English), **1400** (Middle English), **1570**, **1580**, **1621**
and **1687** (Early Modern English) and the modern **final** surface. A form that is not attested
is simply absent from the array — the engine scores each word at whichever checkpoints it has.
`gloss` is the modern reflex where there is one and the Proto-Germanic headword (`hurnaz`) where
the word died before Modern English; it is a label and a `--single` lookup key, not necessarily
an English word.

**Provenance travels with the data.** Every word carries a `note` — its source (Wiktionary, or
Ringe, who outranks it) and any correction made to its input (`PREFORM_FIXES`) or its 200 target
(`ATTESTED_FIXES`). Each form may carry its own `note`: the PIE seed records the form as *cited*
by Wiktionary and whether hyphens were stripped, and a corrected 200 form says so. The engine
never reads `note` — it is documentation that round-trips through the loader, so the lexicon
explains its own evidence rather than leaving it in a separate `provenance.csv`. The word-scoped
SPORADIC decisions (reanalysis, leveling, the lexically-diffused sound changes) live in
`rules.toml`, where the change itself is; the lexicon's notes are about the *data*, the rules'
about the *changes*.

### What the builder throws away, and why

Coverage was traded for honesty. Wiktionary's `inh` link points at a PIE *root-representative
or inflected cell*, not necessarily at the ancestor of the citation form — it cites the 3sg
`*bʰéreti` against the Proto-Germanic infinitive `*beraną`. No correct cascade turns one into
the other, so such a row would score as a miss however good the rules were, and the accuracy
figure would stop measuring the rules. The builder therefore keeps only rows whose PIE form is
a true preform:

- **verbs are dropped** — the PIE form is a finite 3sg, the Germanic form an infinitive;
- **bare roots are dropped** (`*bʰer-`), being roots and not words;
- **affixes and inflected-cell glosses are dropped**;
- **pronouns, particles and other function words are dropped** — their PIE forms look clean,
  but they erode irregularly (the reflex of `*óynos` is the article *a*, not the regular
  *one*), so they belong in word-scoped `lex_*` rules rather than in the gold;
- the modern IPA is joined **by spelling *and* part of speech**, because an archaic noun can
  be spelled like a common word — *were* 'man' (the *werewolf* one, /wɪə/) would otherwise take
  the verb *were*'s /wɜː/.

### What is blanked rather than dropped

Three conditions say only that the **modern column** cannot be trusted — not that the word is
bad. They used to drop the whole row, throwing the Proto-Germanic and Old English columns out
with the English one. Since a word is scored at whichever checkpoints it has, the untrustworthy
`final` is now blanked and the row kept:

- **no surviving modern reflex** (98 rows) — the word died, but `*hurnaz` is still attested;
- **several modern reflexes** (38 rows: *of*/*off*, *thine*/*thy*) — the sound laws produce one
  output and nothing in the data says which reflex is the regular one, so the final is unusable;
  the Proto-Germanic form, however, is not in the least ambiguous;
- **the modern IPA will not segment** (13 rows).

A row with no segmentable target at *any* checkpoint is still dropped — it scores nothing.

### Finals filled on 2026-10-06

Most of the "several modern reflexes" rows listed the standard word beside dialect spellings or
proper nouns: *God*/*god*, *mither*/*mother*, *snaw*/*snow*, *neet*/*night*/*nite*. A final
was added to such a row, and to single-reflex rows that had none, when all of these hold:

1. Exactly one listed reflex is a standard English word. An entry counts as standard when it is
   not a proper noun and has a sense that is not an alternative or inflected form and is not
   tagged dialectal, obsolete, archaic, rare or regional.
2. That entry's Wiktionary etymology names the word's own Old English form, or its
   Proto-Germanic form when there is no Old English one. This rejects homographs: *near*
   'kidney' and *near* 'close' both go back to ME *nere*.
3. Its transcription is RP: tagged Received Pronunciation, else UK, else untagged. An American
   transcription is never used.
4. A reviewer confirmed the pick. Review rejected compounds and new formations (*hangnail*,
   *behest*, *golden*, *inkling*), obsolete reflexes (*near* 'kidney'), an uncertain etymology
   (*mound*) and transcriptions that are not RP (*two* /tu/, *haulm* /hɒm/). Where two
   reflexes passed, the reviewer chose the standard continuant: *father* over Scots *faeder*,
   *worm* over *wyrm*, *arse* over *ass*, *clout* over *cloud*, *mould* over *mold*, *tithe*
   over *tenth*.

This added 49 finals. Each one's `note` names the reflex and, for a reviewer's choice, the reason.
Genuine doublets stay blank, for example *shade*/*shadow* and *whit*/*wight*.

The same refresh found Wiktionary IPA, missing at the bootstrap, for three Old English forms
(*nigoða*, *anga*, *cynn*) and four Middle English ones (*gol*, *lowe*, *ange*, *kyn*). They are
normalised as the bootstrap normalises its own, and each note quotes the source IPA. Two were
left out. ME *widwe* /ˈwidwə/ would lose its only syllable nucleus to the column's dropped final
-e. OE *sīen* would pass through `anglianise()`, which wrongly turns the īe from *īo into ē.

### The modern column (final)

Since 2026-10-07 the final targets are CUBE's transcriptions of current Standard Southern British
(Lindsey & Szigetvári, seas3.elte.hu/cube), in CUBE's default symbols: ɪj ɛj ɑj oj əw ʉw aw for
FLEECE, FACE, PRICE, CHOICE, GOAT, GOOSE, MOUTH; ɪː ɛː ɑː əː oː ɵː for NEAR, SQUARE, PALM, NURSE,
THOUGHT, CURE; ɪ ɛ a ʌ ɔ ɵ ə for KIT, DRESS, TRAP, STRUT, LOT, FOOT, commA. CUBE's r is written ɹ,
its ʧ ʤ as t͡ʃ d͡ʒ, and its stress accent as ˈ. Ten words CUBE lacks keep their Wiktionary RP
form in CUBE's symbols. The choice, and what it replaced, is in DECISIONS.md (2026-10-07). The
section "Finals filled on 2026-10-06" describes how the words were chosen; the transcriptions
themselves are now CUBE's.

### The Proto-West Germanic column (403)

Added on 2026-10-06 (DECISIONS.md). The column splits the long leg from Proto-Germanic to Old
English, where most of the 900 errors arise.

- **Source.** Wiktionary's Proto-West Germanic entries, joined to the lexicon through their
  `inh` link to the Proto-Germanic headword. Where one headword has several PWGmc entries, the
  one whose descendants list the word's own Old English form is used. 312 words have a form.
- **Transcription.** `tools/pwgmc_ipa.py`. Wiktionary gives IPA for only 8 of its 5578 PWGmc
  entries, so the headword is transcribed, as the 200 column is. The letters follow Ringe &
  Taylor's PWGmc phonology (§4.1, PDF 120–121): *d* is a stop everywhere, *f* is labiodental,
  the labiovelars are clusters, *ʀ* is still *z*, and *ē* is ē₂ because stressed ē₁ had
  become *ā*.
- **Year.** 403: after the West Germanic loss of final *-z (400) and apocope (402), and before
  the first Old English rules (404). No rule has this date.
- **Status.** A reconstruction, like the 200 column, so Ringe & Taylor outrank it.

At its introduction the column scored 117/270 exact. Most misses came from rules dated on the
wrong side of the checkpoint, and re-dating them to Ringe & Taylor's chronology took it to
202/270 with no loss at 900, 1400 or final:

- moved after 403, as northern West Germanic or later: the nasal-spirant law and *lþ > *ld
  (§5.1.1, §5.1.3), β > f and the raising of ō (§4.1);
- moved before 403, as PNWGmc or PWGmc: final *-ō > *-u (§2.1.1), the older final *-ī shortening,
  the labiovelars (§3.1.3), and the vocalisation of final *j and *w (§3.1.2);
- added: PWGmc *ē₁ > *ā (§4.1) with its Anglo-Frisian fronting or rounding (§5.1.2), and the
  PWGmc final *-ō and *-ā of the n- and ōn-stems (§3.1.4).

The earlier vocalisation of *j and *w made several Old English forms analogical, as Ringe & Taylor
describe them: the ja-stem geminates (bedd, cynn), fealu, feoh, cwic and eoh. Each has a
word-scoped rule citing the page.

Still open at 403:

- anadô: Kroonen reconstructs *anad- and Ringe *anud-, and neither matches the preform.
- sōl: the cascade's *sōul is one step from the target *sōl.

Closed on 2026-10-07: the West Germanic gemination of a medial *Cj now keeps the *j, which Old
English loses later, so hedge (*haggju) is exact. The lowering of *i to *e, which Ringe & Taylor
find in only two words (§2.3.1), is now word-scoped to them, so lid and meed are exact. The targets
of fox and yoke follow Ringe & Taylor's a-umlaut, and the lowering in ford is dated after PWGmc. *w
is lost before an unstressed *u after a consonant (§2.1.1) and after a stressed vowel (§3.1.5), so
ahwō, roo and þrawō are exact. ear restores its s-stem *z after the loss of final *-z, so its 403
form keeps the *z that rhotacism turns into *r later. Later that night thick took the feminine
stem *þikkwī before 403, with its velar geminated before *w (Ringe & Taylor PDF 64). On 2026-10-08
midge took Kroonen's *muwī and the West Germanic velarization (DECISIONS.md), flunþrą's target kept
the *u that Ringe & Taylor leave unlowered before a nasal, and skuwwô took Kroonen's pretonic *ww
with Ringe & Taylor's PWGmc *uww > *ūw.

### The Early Modern checkpoints (1570, 1580, 1621, 1687)

Added on 2026-10-06 (DECISIONS.md). The forms are the pronunciations that 16th- and 17th-century
orthoepists record for words in the lexicon, as Jones reads them (*A History of English
Phonology*, ch. 4). Minkova and Pyles & Algeo name no orthoepist for any of these words, so they
served only for dating. 46 forms for 43 words. Each note names the orthoepist, his date and
spelling, Jones's page, and any doubt about the reading.

- **Years.** The evidence falls into four groups, each scored at its main orthoepist's date:
  Hart 1551 and 1570 at 1570 (7 forms); Bullokar 1580 and Mulcaster 1582 at 1580 (11); Gil 1619
  and 1621 at 1621 (14); Coles 1674 and Cooper 1687 at 1687 (14). No rule shares these years.
- **Conventions.** The IPA follows the final column, except where the source does not decide.
  The sources say nothing about the quality of r, so it is written r before the cascade's
  change to ɹ (1620) and ɹ after it. Gil's palatal fricative is written x, as in the 1400 column.
- **Less certain.** might and bright are attested only in almighty and brightness. Seven
  Bullokar forms (warm, harm, corn, thorn, worm, helm, elm) carry the inserted vowel of Jones's
  reading ([θɔrən]), where a syllabic consonant is also possible.

At their introduction the four stages scored 1/7, 0/11, 2/14 and 4/14. The misses point at the
cascade's Early Modern dates: `me_x_loss` (1450) is too early, since Hart and Gil still have the
fricative of night; the one-step Vowel Shift (1600) gives [aɪ] where Gil has [əɪ]; the laxing of
short i and u (1900) is too late for Gil's kin [ɪ]; STRUT reaches flood too early, and TRAP heart
and last too late.

On 2026-10-07 these dates were revised from the sources: the short high vowels are written lax
from 1569, TRAP is [æ] from 1575, the Vowel Shift of the high and mid vowels is at 1560 and that
of ME ā at 1600, the shift goes through [əɪ], [əʊ] before [aɪ], [aʊ] at 1690, the PRICE-r schwa
is at 1610, the FOOT–STRUT split and the loss of the fricative are at 1640, the MEAT–MEET merger
is at 1680, and ME ō before r stays [oː] until the FORCE lowering at 1700 (DECISIONS.md,
2026-10-07). The four stages then scored 4/7, 0/11, 10/14 and 11/14. Bullokar's inserted vowels
and the diphthong notation ([oʊ] where the cascade writes [ɔw]) account for most of what remains.

### Words added on 2026-10-06

The refreshed extracts were run through the unchanged bootstrap (`build_gold.py`, with its output
redirected so that `words.toml` was not overwritten), and the words it produced that the lexicon
lacked were appended as generated. The bootstrap's `pde_sounds.json` is built by
`tools/pde_sounds.py` from kaikki's per-word English pages. It keeps only transcriptions tagged RP
or UK, or untagged, so that `modern_ipa` cannot fall back to General American.

Of 23 new rows, 4 were left out: *gold* (Wiktionary now links *gelwaz 'yellow' to it), *ēbanþs*
(the word *even* already in the lexicon), *swēgraz* (the same PIE form as *swēguraz*) and
*humelaz* (the word *bumblebee*). 19 were added: *mark, deep, green, tongue, bitter, moth,
sooth, hrīsą, thill, theal, gamalaz, tehswô, ētijaz, lingwidi, lingwō, wazrą, līką, dankwaz,
tēlō*. The bootstrap drops most other chains for its stated reasons: 116 verbs or affixes, 113
bare PIE roots, 14 PIE forms it cannot transliterate.

### Old English transcriptions

Six Old English spellings without Wiktionary IPA were transcribed by `tools/oe_ipa.py` on
2026-10-06: *mynd, snōd, drōs, lungor, wiþe, eġeþe*. The tool follows Wiktionary's conventions
and agrees with its IPA on 435 of 450 lemmas (`python tools/oe_ipa.py` runs the check); the 15
disagreements are long vowels that a descendants tree leaves unmarked and compound stress. Four
other spellings were a different formation and were not used: *sīþfæt* (fetą), *wæstling*
(wastijō), *ġeēan* (aunaz), *scēaffōt* (skaibaz). Starred spellings are reconstructions, not
attestations, and were skipped.

### Bare-root words added on 2026-10-06

The bootstrap drops a chain whose PIE form Wiktionary cites only as a bare root. For the 111 such
chains, the standard references were searched for the full preform of the exact word:
Kroonen, with Ringe where he has the word. 60 were found. The 51 that the book states without
doubt were added by running the unchanged bootstrap with those preforms (`PREFORM_FIXES`,
supplied for the run only), and each entry's note names the book, headword and page. Left out:
the seven the book itself doubts (*aigin, miltiją, hugiz, līþu, knawaz, hehlǭ, miuzijō*), the
chains with no preform in either book (Germanic-only, substrate or unexplained words), the
duplicates *gold, ēbanþs, swēgraz, humelaz*, and *betwixt*, a be- formation. The finals of
*sole, riff, sullow, leam* were dropped as an obsolete, dialect or different word.

### Words added on 2026-10-07, scored at first contact

Since the rules and the words shape each other, the accuracy table measures fit, so a fresh batch
was added and scored before any change was made for it (DECISIONS.md, 2026-10-07, rule 5). The
bootstrap yields no new word: every chain it keeps is already in the lexicon. The batch comes from
the chains it drops because Wiktionary cites only a bare PIE root (58) or a form it cannot
transliterate (2). Under "Start a word at its earliest secure reconstruction" (DECISIONS.md,
2026-10-07) these words start at their Proto-Germanic form, so a doubtful preform no longer keeps
a word out: *miltiją, hugiz, līþu* and *hehlǭ* are back. Of the 60, 22 were already in the lexicon
under another name. Four were left out: *twiskaz* (ME bitwiks carries the prefix be-), *raskuz*
(OE ræsċettan is a verb), *miuzijō* (no Old or Middle English target) and *dungz* (its targets are
those of *dung*). The modern target of *razną* is blank, since barn is the compound bere-ærn. That
leaves 34 words, short of the 50 that were asked for. The 403 forms come from Wiktionary's PWGmc
entries (13 words). The modern targets come from CUBE (13 words) and, for *swith*, from
Wiktionary's RP in CUBE's symbols.

First contact, with no rule or target changed for them:

| checkpoint | exact | within 1 phone |
|---|---|---|
| 403 | 12 / 13 | 13 |
| 900 | 20 / 34 | 27 |
| 1400 | 9 / 20 | 13 |
| final | 8 / 14 | 9 |
| all | 49 / 81 (60%) | 62 |

The misses point to gaps in the rules. OE flǣsċ comes out as **flæːst͡ʃ**, so the palatalisation
of *sk leaves an s. OE nēah loses its final h. ME udder and swith need a shortening of the long
vowel that the rules lack.

The first two gaps are now closed. *sk palatalises in Ringe & Taylor's three positions, and
breaking keeps the length of a long vowel, so flesh and nigh are exact at every checkpoint. No
source at hand names the cause of the shortening in udder and swith, so both still miss. Two ME
targets turned out to belong to other words and were removed (*kīþą*, *aihtiz*). The score above
stays as the batch's first-contact record.

### Words added from Kroonen's headwords on 2026-10-07, scored at first contact

The bootstrap keeps only Proto-Germanic records with an inherited PIE parent, so it never reached
the many Wiktionary records that have none. The second batch comes from them (DECISIONS.md,
2026-10-07, "Draw the next batch from Kroonen's headwords, starting at Proto-Germanic"). Of 3345
Proto-Germanic nouns, adjectives and numerals, 422 are not in the lexicon, have a stem that is a
headword in Kroonen, and reach an attested Old English word. 418 of them have no PIE parent in
Wiktionary. 167 have an Old English, a Middle English and a single modern reflex. The fifty most
frequent of these were taken. Five records among them were passed over: four whose modern word
is a homograph (*more* from *murhǭ* and *murhō* 'wild carrot', *side* from an adjective, *blow*
from *blēwaz* 'blue') and one duplicate (*flugiz* 'flight', beside *fleugǭ* 'fly'). The batch is
core vocabulary: *back, way, thing, life, day, year, hand, stone, bread, sword* and forty more.

The targets come from the same sources as before. The 403 forms are Wiktionary's PWGmc entries (42
words). The Old English forms are Wiktionary's IPA, except *wiċe* 'week', transcribed by
`tools/oe_ipa.py`. A Middle English target is kept only when the Middle English entry's etymology
names the word's Old English form. That check dropped six targets taken from homographs, such as
ME *here* 'here' for *year*. The modern targets are CUBE's. All fifty start at Proto-Germanic, so
the batch does not test the 200 column.

First contact, with no rule or target changed for them:

| checkpoint | exact | within 1 phone |
|---|---|---|
| 403 | 40 / 42 | 41 |
| 900 | 36 / 50 | 47 |
| 1400 | 31 / 45 | 36 |
| final | 31 / 50 | 35 |
| all | 138 / 187 (74%) | 159 |

The misses pointed to rule gaps, and most have since been closed from the books. A final *j is now
lost only after *i, so OE dæġ and weġ keep their ġ. ME æ before j no longer merges with a. *gʷ
resolves into *g + *w. *w is lost before an unstressed *i (sǣ 'sea'). [uː] shortens before a final
[k] (book). Breaking acts only on stressed vowels (īsern). Word rules with a named cause gave bread
and dead their pre-shift shortening, tree and few their levelled *w, and grave the long vowel of its
inflected forms. Later the same night the batch reached 183 of 187 exact. Among the changes were
general syncope and the epenthesis before l (soul), the ME palatal glide (fly), a lengthening
before final ŋg that ME undid again (song), the lengthening before -nd limited to high vowels (hand,
land), and the ME open-syllable lengthening of a high vowel, word-scoped as Northern (week). On
2026-10-08 melu took the levelled form that Ringe & Taylor call the commoner one, and fly the ME
variant flie from OE flyge (Klein). That brings the batch to 185 of 187 and leaves OE ġēar and
sumor open. The score above stays as
the batch's first-contact record.

### A third batch from Kroonen's headwords on 2026-10-08, scored at first contact

The third batch takes fifty more words by the second batch's criteria (DECISIONS.md, 2026-10-08,
"Draw a third batch from Kroonen's headwords by the same criteria"). After the second batch and
the night's changes, 369 Proto-Germanic records qualify, and 115 of them have an Old English, a
Middle English and a single modern reflex. The fifty most frequent were taken. Ten records were
passed over. Eight have a modern spelling that is mostly another word: *more* (*murhǭ*, *murhō*),
*side* (*sīdaz*), *blow* (*blēwaz*), *halt* (*haltaz* 'lame'), *neat* (*nautą* 'cattle'), *wong*
(*wangaz*) and *wont* (*wanduz* 'mole'). Two are duplicates: *saltaz* beside *saltą*, and *fuldō*
beside *faludaz*. The batch is again core vocabulary: *edge, apple, salt, sand, grass, sheep,
hammer, liver, goat, net* and forty more.

The targets come from the same sources as the second batch. The 403 forms are Wiktionary's PWGmc
entries (36 words). The Old English forms are Wiktionary's IPA, except *drit* and *barc*,
transcribed by `tools/oe_ipa.py`. The Middle English check dropped the targets of *narrow*, *hawk*
and *bark*, whose Middle English entries do not name the Old English form. The modern targets are
CUBE's. *sand* and *herd* have a PIE form in a book (Ringe PDF 132; Kroonen PDF 261), but start at
Proto-Germanic like the rest of the batch.

First contact, with no rule or target changed for them:

| checkpoint | exact | within 1 phone |
|---|---|---|
| 403 | 33 / 36 | 35 |
| 900 | 29 / 50 | 42 |
| 1400 | 26 / 47 | 34 |
| final | 28 / 50 | 31 |
| all | 116 / 183 (63%) | 142 |

The misses point to these gaps:
- *net* and *web* lack the geminate of OE *nett* and *webb*, and *apple* that of *æppel*.
- *arrow* and *sorrow* end in a velar in Middle English (arx, sɔrg), where the targets have
  *arwe* and *sorwe*.
- *salt*, *sheep* and *swallow* have West Saxon 900 targets (*sealt*, *sċēap*, *swealwe*). The
  cascade derives the Anglian forms, which Middle English continues.
- *edge* has a Middle English target written dʒ without the tie bar, which the scorer reads as two
  segments.

### Middle English transcriptions

Where Wiktionary gives a Middle English spelling without IPA, the 1400 target may be transcribed
from the spelling (DECISIONS.md, 2026-10-06). Middle English spelling rarely marks vowel length:
*god* is both [gɔd] 'God' and [goːd] 'good' (Minkova §6.2, PDF 154). So only spellings whose
reading these rules fix are transcribed:

1. A stressed vowel is short before a doubled consonant letter or before two consonants
   (Minkova §7.5.3, PDF 225–226).
2. Rule 1 does not apply before the lengthening clusters *ld*, *nd*, *mb*, *ng*, *rd*, *rn*
   and *rð* (Minkova §6.4, PDF 168–169; Jones §2.2.5, PDF 41–42), nor before *st*, where
   shortening is lexical (Minkova §7.5.1.1, PDF 212–213).
3. A vowel digraph, a vowel in an open syllable, and a vowel before a single final consonant are
   not transcribed: their length or quality is ambiguous (Minkova §2.4, PDF 46; §6.2, PDF 154;
   §7.2, PDF 188–191). A macron in the edited headword marks a long vowel.
4. The column's conventions apply: short *e* is ɛ and short *o* is ɔ, *sch* is ʃ, *gh* and *h*
   before *t* are x, and a final *-e* is dropped, as in 78 of the 80 targets whose spelling ends
   in *-e*.

This added 15 targets: *harm*, *schelle*, *ribbe*, *midde*, *hals*, *morth*, *ridder*,
*drosse*, *briht*, *frosk*, *wedde*, *thank*, *inke*, *wrihte*, *gūth*. Each one's note says it
is a transcription. The other 53 spellings without IPA stay blank.

What survived the first build was nouns, adjectives and numerals: **249 rows**, the same order as
the FLLAPS gold that `latin_to_french` scores against.

### The residue at first contact

Of the 240 rows then scorable at Proto-Germanic, **126 were new** and had never been curated. They
landed **56/128 exact (44%) with no `PREFORM_FIXES` entry at all**, which is the useful number:
the rules had been fitted against the old 114, so a coin-flip hit-rate on words they had never seen
says the cascade generalises rather than having been tuned to the gold.

The misses among them are mostly the wrong-preform problem this file opens with — Wiktionary
citing `*h₂ébōl` against a Proto-Germanic `*apaliją` that no cascade can reach from it. They are
*not* evidence the rules are wrong. Since 2026-10-07 their preforms may be revised to fit the
rules, under rule 2 of "Correcting the gold itself" below. The figure above stays as this batch's
first-contact score.

### A vocalised laryngeal can be syllabic — and can carry the accent

`pie_ipa.py` accepts the **ring** (`◌̥`) on a laryngeal as well as on `l r m n`: `*h₂̥` is a
syllabic laryngeal, and like any other nucleus it can take the **acute**.

This is not a notational nicety — without it a whole class of words cannot be got right at any
price. Kroonen's `*nh₂-s-eh₂-` 'nose' is a zero grade: its first syllable has **no vowel at all**.
The `a` of the attested `*nasō` does not exist in the input; a rule *creates* it later, when the
laryngeal vocalises. But the accent binds to a vowel *segment*, not to a syllable slot — so with no
vowel to mark, the acute was forced onto the suffix, Verner then dutifully voiced the `*s`, and we
derived `**nazō` against an attested `*nasō` with a voiceless `*s`. The word was unreachable.

Write the ring and the acute on the laryngeal and it simply works: the laryngeal is a nucleus, it
bears the stress, it vocalises to a *stressed* `ə`, Verner correctly declines to fire, and the `*s`
stays voiceless.

Two consequences worth knowing:

- **`u_epenthesis` is restricted to `+son`.** It exists for the syllabic *sonorants* (`*l̥ r̥ m̥ n̥`
  > `ul ur um un`). A syllabic laryngeal is also `[+cons, +syll]` and was being swept up by it —
  but a laryngeal does not take an epenthetic `*u`, it vocalises to `*ə`. Unrestricted, Kroonen's
  `*n̥h₂-s-eh₂-` came out `**unsō`.
- Do **not** reach for the ring on the neighbouring sonorant instead. Writing `*ń̥h₂seh₂` makes the
  `*n` syllabic, u-epenthesis fires, and you get `**unsō` — the wrong segment made the nucleus.

### The source hierarchy — Wiktionary is the *weakest* source, not the truth

For anything **reconstructed**, the books outrank Wiktionary:

> **Ringe**, **Kroonen** > **Wiktionary**

Where Ringe and Kroonen disagree, each case is decided on its evidence and recorded in DECISIONS.md
("Decide each Ringe–Kroonen conflict on its evidence", 2026-10-06).

Wiktionary's Proto-Germanic and PIE are anonymous, unrefereed reconstructions of uneven quality.
Ringe (*From Proto-Indo-European to Proto-Germanic*) and Kroonen (*Etymological Dictionary of
Proto-Germanic*) are the standard reference works. **Where they disagree with Wiktionary, they
win** — and that is the normal case, not an exception to be argued for each time.

This applies to *reconstructions only*, and the distinction is the whole point:

| column | status | who wins |
| --- | --- | --- |
| the PIE **input** | reconstruction | Ringe/Kroonen, or the rules (rule 2 below) |
| **200** (Proto-Germanic) | reconstruction | Ringe/Kroonen, or the rules (rule 2 below) |
| **403** (Proto-West Germanic) | reconstruction | Ringe & Taylor, or the rules (rule 2 below) |
| **900 / 1400 / final** | **attestation** — a real recorded form | any cited source, in four cases only (rule 1 below) |
| **1570 / 1580 / 1621 / 1687** | an orthoepist's description, as Jones reads it | nobody |

Old English *nest*, *fisc*, *wer* are things people actually wrote down. Proto-Germanic `*nestą`
is somebody's guess. The two are not the same kind of object and must not be given the same
authority — which is exactly the mistake of treating the Wiktionary gold as ground truth.

**The books do not merely confirm; they overturn.** Three worked examples, each of which no amount
of staring at the attested form could have produced:

- Ringe: "PIE \*swéḱs 'six' **!** \*séḱs (**by lexical analogy** with \*septḿ̥ 'seven')". The
  missing \*w is *analogy*, not a sound change — so no rule should ever have been hunted for it.
- Kroonen on \*hōfa-: "the difference between Gm. \*ḱoHp-o- and Indo-Iranian \*ḱopH-o- implies
  that **laryngeal metathesis** occurred". Wiktionary cites the Indo-Iranian order, whose laryngeal
  cannot lengthen the \*o. The Germanic order gives the attested \*hōfaz outright.
- Kroonen has \*nista-, \*fiska- and \*wira- **all with /i/**, where Wiktionary gives \*nestą and
  \*weraz with /e/. That moved a *rule* (`pgmc_i_lowering`, out of Proto-Germanic), not just a
  preform.

Kroonen is equally useful when he says he *doesn't* know: \*steura- is "a word of uncertain
origin", \*wintru- has "no certain etymology". Those are honest misses, not failures of the rules.
Since 2026-10-07 their preforms may be revised to fit the rules, under rule 2 below.

### Correcting the gold itself — `ATTESTED_FIXES`, and the fence around it

There is a second table in `build_gold.py`, and it does a **categorically more dangerous** thing
than `PREFORM_FIXES`. The line between them must not blur:

- **`PREFORM_FIXES` corrects the INPUT** (the PIE preform), using the attested Germanic form as
  *independent evidence*. That is precisely what keeps it out of circularity: the evidence comes
  from outside the cascade.
- **`ATTESTED_FIXES` corrects the TARGET** — the thing the engine is scored against. Edit that to
  make a word pass and the accuracy figure stops measuring anything at all.

It is admissible for exactly one reason: **the 200 column is a RECONSTRUCTION, not an
attestation.** Wiktionary's Proto-Germanic is one scholar's reconstruction and it can simply be
wrong. Where the standard reference work says so in as many words, the reference work wins.

**The rules, which are not negotiable:**

1. **The 200 and 403 columns freely; the attested columns in four cases only.** The 900 / 1400 /
   final columns are *attested* — real recorded Old English, Middle English and modern forms —
   and a form that was really recorded is never replaced to make a word land. Since 2026-10-06
   (DECISIONS.md) an attested target may be corrected, with a citation, when the source shows one
   of four things: the target breaks the column's transcription convention (a General American
   form in the RP column); it records a dialect variant the later columns do not continue (South-
   Western ME *frøː*); it belongs to a different word (*twēġen* is *twain*, not *two*); or the
   modern target is a loan or a new formation, not the word's reflex, and is removed (*sister* is
   Old Norse *systir*). Each correction keeps the old value in its note. Since 2026-10-07 any
   source may support such a correction, and where the spelling leaves a sound open, such as vowel
   length, the rules may choose the reading.
2. **A reconstruction may answer to the rules.** Since 2026-10-07 (DECISIONS.md) a PIE input, or a
   200 or 403 target, may be revised when the rules predict a different form and the attested forms
   allow it. The note keeps the old value and says that the rules prompted the change.
3. **An attested target must be defensible with the derivation switched off.** If the only
   argument for it is "the cascade would then land", it does not go in, unless the spelling leaves
   that sound open (rule 1).

The entries so far are all one finding. Kroonen reconstructs `*nista-` 'nest' (< \*ni-zd-o-),
`*fiska-` (< \*pisk-o-, cf. Lat. *piscis*) and `*wira-` 'man' (cf. Skt *vīrá-*) — **all three with
an /i/**, where Wiktionary gives `*nestą` and `*weraz` with an /e/. Ringe's bibliography cites
Lloyd, *"Is there an a-umlaut of i in Germanic?"* So the lowering of \*i is doubtful **at
Proto-Germanic** — and `pgmc_i_lowering` has been re-dated out of it accordingly (t=50 → 300).

The change itself is not in doubt: Old English really does have *nest* with an /e/ while *fisc*
keeps its /i/, and those are attestations. Kroonen's claim is about **timing**, not existence. So
the rule moved rather than went, the two reconstructions were corrected, and the attested columns
were left exactly as they are.

### Verbs: the 3sg present, and only where sound change can reach it

Verbs were absent from this lexicon for a long time, and the reason was **morphological, not
phonological**. Wiktionary lemmatises a PIE verb at the **3sg present** (`*bʰéreti`) but a
Proto-Germanic verb at the **infinitive** (`*beraną`). The pair therefore names two different
cells of the paradigm, and no sound change connects them — `*bʰéreti` can never yield `*beraną`,
because the ending is not the same morpheme. Feeding that pair to the engine would score the
cascade on a mismatch it cannot possibly derive, which is the same trap the ablaut rows set.

Both ends do exist in the same cell, though. The PIE lemma already *is* a 3sg, and the Germanic
3sg sits in the record's inflection table (`*biridi`), so `build_chains` reads the pair from
there. Input and target are then the same morphological cell, exactly as a noun's accusative is.
The 3sg has no attested IPA — the inflection table gives romanisation only — so
`tools/pgmc_ipa.py` transcribes it, and is checked against the 4843 lemma pronunciations
Wiktionary *does* give (92.7% segment-exact; the residue is Wiktionary's own inconsistency).

Two filters keep the pair honest, and between them they reject more verbs than they keep:

- the **PIE** end must be a finite 3sg present, the primary ending `*-ti`. Wiktionary very often
  links the bare **root** (`*nem-`, `*gʰeldʰ-`) or a different tense (`*wóyde` is a perfect,
  `*bʰúHt` an aorist). Building a present out of those means reconstructing the input ourselves.
- the **Germanic** end must carry a present ending too. The preterite-presents (`*wait`, `*kann`,
  `*þarf`) continue PIE perfects and take perfect endings, so `*ǵn̥néh₃ti > *kann` is the same
  wrong-cell pairing one tense over.

#### The 1sg gets the weak verbs back

A verb is scored in **two** cells, the 3sg and the 1sg, and they are not duplicates of each other.

The 3sg has to exclude the 30 weak presents (below): Ringe reaches their `*-iþi` by an explicit
**analogy**, and no sound change produces it. **The 1sg has no such problem, and the reason is
structural — its ending has no consonant.** Ringe's own paradigm gives 1sg `*līhwō`, `*werþō`,
`*kwemō`, `*bidjō`, `*lētō` — and `*bidjō` sits right beside the `*bidiþi` he marks analogical.
Verner's Law needs a fricative to voice; `*-ō` offers none. The cell the analogy ruined in the 3sg
is untouched in the 1sg, so the weak verbs are scorable again — `*satjō`, `*bidjō`, `*ligjō`.

It is also a genuine second test of the roots, not a repeat of them:

| | | |
|---|---|---|
| 3sg | \*b**i**ridi | \*e RAISED to \*i before the following \*i |
| 1sg | \*b**e**rō | no following \*i, so the raising must NOT fire |

A minimal pair, with the 1sg as the negative control.

The filters mirror the 3sg's, one cell over: the PIE end must be a **thematic** present 1sg
(`*-oh₂`), which rejects the perfect (`*wóydh₂e`) and the athematic (`*h₁édmi`); and the Germanic
end must carry the present `*-ō`, which rejects the preterite-presents (`*wait`, `*kann`, `*þarf`),
whose 1sg is a perfect. **37 verbs, 23 exact (62%), untuned.**

#### The weak presents are excluded, because Ringe reaches them by analogy

The surviving 49 verbs split cleanly in two on their **Germanic ending**:

| Germanic ending | | count |
|---|---|---|
| `*-di` | **Verner fired** — the regular outcome | 19 |
| `*-þi` | **Verner did not** — the weak presents | 30 |

That looks like a conditioning the cascade is missing. It is not. Ringe derives the weak class 1
present with an explicit **analogical** step, which he marks with his `!` — the same mark he puts
on `*h₂stér- >! *sternan-`:

> PIE \*gʷʰédʰyeti '(s)he is asking for' … > \*bedjidi, \*bedjondi **>!** PGmc \*bidiþi, \*bidjanþi

Read the middle column. The **regular** outcome is `*bedjidi`, with the Verner-**voiced** `*d`,
because the vowel before the ending is unaccented — exactly as in the strong verbs. The attested
`*-iþi`, with its voiceless `*þ`, is levelled in from elsewhere in the paradigm afterwards. Our
cascade duly derives `*satiði`, `*sōkiði`, `*bidiði`: the ending Ringe says the phonology gives.

So `*satiþi` and its 29 fellows are targets that a **correct** sound-change cascade cannot hit,
and scoring against them would do damage twice over. It would hold 30 rows permanently wrong for
being right (dragging Proto-Germanic down by nine points), and it would stand as a permanent
invitation to "fix" Verner's Law — which would break the 16/19 strong verbs that derive perfectly
today, since they need the very voicing the weak verbs appear to refuse. A target must be
reachable by rule, or it is not evidence about rules. `KEEP_WEAK_PRESENTS` in `build_chains.py`
flips them back on.

The classifier keys on the **Germanic ending**, not the PIE suffix, and the difference is not
academic. `*h₂wḗh₁ti` has a laryngeal suffix and *looks* weak, but Germanic `*wēidi` ends in a
Verner-voiced `*-di`: it is a regular, reachable target. Matching on the PIE suffix filed it under
"analogy", where its miss — Verner failing to fire — could never be read as the rule signal it is.

This is the same line DiaSim draws. Its Latin→French cascade has no morphology at all — a flat
string of phones per stage, the etymon chosen once (the accusative `spīnam`, not `spīna`) — and
every mention of analogy in its 716 rules is in a *comment*, never a rule. Where Pope reaches for
analogy, DiaSim goes looking for the regular conditioning instead, and eats the miss when it
cannot find one. Modelling the levelling would be a different project from modelling sound change.

#### SIEVERS' LAW — found by the weak presents, fixed by the 1sg

The weak verbs showed the cascade had no Sievers' Law, and the **1sg** stated it as a minimal pair
sharp enough to implement. The cascade had it exactly **inverted** — it was faithfully passing
through whichever suffix PIE happened to write, where Germanic redistributes the two by the weight
of the preceding syllable:

| | derived | attested |
|---|---|---|
| `*sodéyoh₂` → light stem `*sat-` | `*sat**ij**ō` | `*sat**j**ō` |
| `*séh₂gyoh₂` → heavy stem `*sōk-` | `*sōk**j**ō` | `*sōk**ij**ō` |

**Heavy** is a long vowel plus a consonant (`*sōk-`), or any vowel plus **two** (`*wurk-`,
`*hauz-`); **light** is a short vowel plus exactly one (`*sat-`, `*lag-`, `*straw-`). The diphthong
stems need no special case: `*hauz-` is `*a` + `*w` + `*z` — two consonants before the `*j`, so
heavy — while `*straw-` is `*a` + `*w`, one consonant, so light. Exactly as attested.

`sievers_law` (t = −900) is dated after `unstressed_e_to_i`, which is what makes the `*i` of the
`*-éye-` suffix in the first place; Sievers then takes it away again where the stem is light.

**+13 exact at 200, zero regressions at any checkpoint.** The 1sg verbs went 23/37 → **34/37
(92%)**. Two nouns came along for free.

#### (superseded) What the weak presents first exposed

Before they were switched off, the weak verbs showed a second and genuinely **phonological** gap,
independent of the analogy — the length of the suffix vowel is inverted:

| | derived | attested |
|---|---|---|
| `*satiþi` (light stem `*sat-`) | `*sat**iː**ði` | `*sat**i**þi` |
| `*sōkīþi` (heavy stem `*sōk-`) | `*sōk**i**ði` | `*sōk**iː**þi` |

That is **Sievers' Law** — `*-y-` after a light syllable, `*-iy-` after a heavy one — and the
cascade does not implement it (nothing in any project mentions it). A noun-only lexicon could
never have found this: the law lives in the verbal suffix. It is a real target for the rules, and
the weak verbs are the only evidence for it in the lexicon, which is the reason they are excluded
by a flag rather than deleted.

### Known limits

- **Middle English is the weakest column.** Its Wiktionary IPA is an editorial reconstruction
  (a single dialect, Chaucerian London), not an attestation, and it covers under half of ME
  lemmas. Old English is safer: OE spelling is near-phonemic and the IPA is derived from it
  mechanically.
- **Ablaut: the PIE lemma is not always the preform, and the fix is in `ABLAUT_FIXES`.**
  Wiktionary's `inh` link records a PIE *lemma*, cited in the e-grade, but the Germanic word
  often continues the ZERO grade of the same root — and no rule can bridge them (`*ǵéwstus`
  will never yield `*kustuz`). Where the true preform is recoverable, the builder substitutes
  it: *mind* (`*mn̥tís`) and *cost* (`*ǵústus`) are now both **exact**. The accent has to be set
  by the attested Germanic consonant, since Verner's Law reads it — `*mundiz` has a voiced *d*
  (accent follows the root), `*kunþiz` a voiceless *þ* (accent on it).

  A poisoned row can also make a *correct* rule look broken: OE palatalisation dutifully
  palatalised the front vowel that *cost* should never have had. Fix the word, not the rule.

  The ordinals (*seventh*, *sixth*, *eighth*) were once such rows, built on a different suffix
  in Germanic than in the cited PIE form. Their 200 forms are now exact, and *sixth* is exact
  throughout. *seventh*, *eighth* and *ninth* still miss in Old English, whose targets have the
  -þ- variant of the suffix (*seofoþa*, *eahtoþa*, *nigoþa*) where the cascade derives -d-.
- **The Proto-Germanic column is a reconstruction, not an attestation.** Some of its distance
  from the derived form is transcription convention rather than phonology (see `CONVENTIONS`
  in the builder), so a miss there is a question to investigate, not automatically a rule bug.
- Attested IPA is normalised to what the inventory can segment (script `ɡ`, tie bars, the
  raising/lowering diacritics). A form that still will not segment is left **blank** rather
  than guessed at.

## Rules (`rules.toml`)

Two legs, which began from two sources:

- **PIE → Proto-Germanic** — originally the cascade of a separate `pie_to_germanic` sample
  project, now folded in here and that project deleted (this one supersedes it: same rules, plus
  a gold to score them against). That project carried *no targets* — its rules had never been
  scored until this lexicon — and its hand-written PIE inputs turned out to have been fitted to
  the rules rather than to the sources (it wrote `meħˈteːr` for *mother*, whose PIE accent is
  initial — `*méh₂tēr` — with the accent evidently moved to make Verner's Law fire). Here the PIE
  input is transliterated faithfully from the reconstruction, so *mother*'s /d/ shows up for what
  it is: **analogical**
  (levelled in from *father*), not a regular sound law, and therefore a word-scoped rule.
- **Proto-Germanic → Old English → Middle English → Modern** — from Minkova, *A Historical
  Phonology of English* (Edinburgh, 2014): §3.4 (Grimm, Verner, the pre-OE changes, West
  Germanic gemination), §4.3 (palatalisation and affrication of velars), §6.3 (i-mutation),
  §6.4 (homorganic-cluster lengthening), §7.3–7.5 (the ME qualitative, diphthongal and
  quantity changes), ch. 8 (the long-vowel shifting), ch. 5 (h-, r- and cluster histories).
  Ringe & Taylor, *A Linguistic History of English* vols 1–2, is the reference for the
  relative chronology of the PGmc→OE leg, which Minkova organises topically rather than
  chronologically.

Neither book is redistributed here: the sound laws are facts and are encoded as rules, but no
book text or extract belongs in the repo.

Rules added since also cite the other books listed at the top of this file: Ringe and Kroonen on
the first leg, and Jones, Pyles & Algeo, Hoad and Klein on the English legs. The rules dated 1980
cite CUBE's accent page, which lists how current Standard Southern British differs from classic RP.

Since 2026-10-07 a rule may also be inferred from the lexicon (DECISIONS.md). Its description then
says so and names the words it came from.

## Where it stands

On 2026-10-08, 737 words. A run of the cascade writes the current figures to
`reports/accuracy.csv`.

| checkpoint | assessed | exact | within 1 phone |
|---|---|---|---|
| 200 Proto-Germanic | 575 | 571 (99.3%) | 571 |
| 403 Proto-West Germanic | 390 | 385 (98.7%) | 389 |
| 900 Old English | 516 | 480 (93.0%) | 500 |
| 1400 Middle English | 379 | 357 (94.2%) | 365 |
| 1570 Hart | 7 | 6 | 6 |
| 1580 Bullokar, Mulcaster | 11 | 10 | 11 |
| 1621 Gil | 14 | 12 | 13 |
| 1687 Coles, Cooper | 14 | 13 | 13 |
| final current SSB (CUBE) | 343 | 314 (91.5%) | 320 |

### Sporadic changes — how the regular cascade and the word-scoped ones divide the work

A sound-law cascade cannot reach everything, and the honest thing is to say why, not to bend a
regular rule until it fits. **Reanalysis, leveling, rebracketing, compounding, and the lexically
diffused sound changes are SPORADIC** — they act on individual words, not on every word in an
environment — so they are written as **word-scoped rules** (`words = [...]`), named `sporadic_*`,
and kept apart from the regular cascade. Each is licensed by the *attested* form, which is the
evidence the word underwent the change, exactly as a Verner-voiced consonant is the evidence for a
PIE accent: `*þunnuz > þynne` (u-stem → i-stem, the ending and the i-mutation both attest it),
`*kustuz > cost` (the lexically diffused *u > *o), DEATH / FLOOD / BROAD (the famous English
splits), `*sehs > six` (numeral), the Anglian close *ē*, the `-ow` vocalisation. A blanket rule for
any of these was *measured* to regress — the geminate-blocked a-umlaut, the general *u > *o, the
final velar vocalisation each broke more than they fixed — which is the empirical case that they
are not regular. Since 2026-10-07 a word-scoped rule also names its cause, such as analogy with a
named word, Norse influence or a dialect form, or says that the cause is unknown (DECISIONS.md).

This keeps the sporadic layer a labelled, auditable list of the morphological and lexical facts on
top of the regular cascade. The reports give one accuracy figure, which includes the word-scoped
rules; no report scores the regular cascade alone. The provenance of every gold word travels with it
in `words.toml`; the sporadic *decisions* live in `rules.toml`, where the change itself is.

When this was written, the 900 denominator was 333, not 337, because the descendant-picker drops
four words whose only Old English reflex is a COMPOUND — *fetą survives solely in sīþfæt
('journey-vat'), *skaibaz in sċāffōt — of which just the second element descends from our
Proto-Germanic word. Scoring a simplex derivation against the whole compound is a category error,
and `root_nodes` in build_chains keeps only the Old English node that is not itself descended from
another (the compound is a child of the simplex), leaving those four to score at Proto-Germanic
alone. No derived form changed and no hit moved — the correction is entirely in the denominator,
removing rows that never belonged in the Old English column.

### The later legs were not broken — they were UNBUILT

The single most useful thing to know about this cascade's shape. For a long time the four legs had
**67 / 33 / 7 / 3** rules, and the accuracy fell off a cliff after Old English (1400 at 39/225,
RP at 9/175). That reads like a hard problem and it was not one: Middle English had seven rules
standing in for the open-syllable lengthening, the æ/ɑ merger, the diphthong smoothings, the
short-vowel openings and the quantity changes, and the modern leg had *three* for the whole of
Early Modern English. The misses were not wrong rules. They were absent ones.

Building them out (**23** and **21**) moved 1400 from 39 to 99 and RP from 9 to 71, and — this is
the part worth generalising — **most of the gain was ORDERING, not new phonology**:

* the OE diphthongs were smoothing *after* the homorganic lengthening, so *heard*, *ċeald*, *eald*
  had their second element lengthened and rounded before the diphthong could collapse;
* `eme_th_voicing` was written for the DENTAL θ, which the engine does not have until 1900 — so it
  named a segment that did not exist at its date and **never fired at all**;
* every pre-/r/ vowel rule (START, NURSE, NEAR, SQUARE) was written with the approximant `ɹ`, which
  `eme_rhotic_approximant` does not create until 1900, long after they run — same trap, four more
  rules, none of them matching anything;
* the Vowel Shift's last step is a SEPARATE step: ME *ɛː* reaches /eː/ in the shift and goes on to
  /iː/ a century later, but written as another clause of the same rule the two fire in one pass and
  *drēm* stops at **/dreːm/. **A chain of raisings needs one date per link.**

If a rule looks right and buys nothing, check the two dates around it before you touch what it says.

### What is left at 900, and why it is not a rule gap

Old English is the leg that gates everything below it — 1400 and RP are scored only on words that
reached them. Two things in the gold, neither a missing sound change, shape the residue.

**1. The Old English column MIXES DIALECTS, and this is the crux.** Wiktionary lemmatises at
whatever spelling is best attested, and that is not one dialect. *rehtaz* and *nahts* come out
Anglian (`riht`, `niht` — smoothed), while *sċiell* and *ġiest* come out West Saxon (with the `ie`
diphthong only West Saxon has). **No single set of breaking-and-smoothing rules fits both**: every
Anglian clause the cascade gains trades a West-Saxon-gold word for an Anglian-gold one, so a blanket
change nets *zero* and the accuracy stops measuring phonology and starts measuring which dialect
Wiktionary happened to lemmatise.

The resolution — carried out in stages, and it is the model for the rest — is that **Present-Day
English descends from the Anglian dialects, not West Saxon, and the gold's own later columns prove
it**: West Saxon *ġiest*, *nīewe*, *tīen* carry the `ie` diphthong, but their Middle English reflexes
are already monophthongs (ME `niw`, `tɛn`) and stay so today. The later columns *continue* the
Anglian form. So Anglian is not a preference imposed from outside; it is what the column ought to be
to agree with the columns that descend from it. Two coordinated moves, each pinned to where the gold
is *already* Anglian so the mixed words are never corrupted:

* `anglianise()` in `build_gold` maps the West Saxon `īe/ie` in the OE **targets** to the Anglian
  monophthong — a regular correspondence (Campbell §200-1), fired on the shape, and the one West
  Saxon feature the later columns visibly reject. Since 2026-10-07 a long *īe from the umlaut of
  *īo (PGmc *iu) becomes ēo instead, because Anglian kept that diphthong: WS dīere, Merc. dēore;
* Anglian **rules**, each scoped to a cluster where the gold is uniformly Anglian: smoothing and
  raising before *ht* (`niht`, `riht`, `miht`), and the collapse of our derivation's i-mutated *æe*
  to Anglian *e* (`sċell`, `erfe`) — the derivation-side twin of the gold step above.

Since 2026-10-07 a third move goes the other way. Where the gold is uniformly West Saxon but the
later columns continue the Anglian form, the target is corrected under the dialect case. Anglian
retraction before *lC* (`oe_anglian_retraction`) replaces breaking there, and *eald*, *ċeald*,
*healm* and four others become *ald*, *cald*, *halm* (DECISIONS.md).

This is slow because it must be done cluster by cluster — *ht*, then the *æe* class, then the next —
never in bulk. But it is honest and it moves the number: 900 went 173 → 200 doing it. What it cannot
do is close the whole gap, because much of the residue is not dialect at all but the second thing:

**2. Some misses are a CITATION FORM, not a sound.** OE *þynne*, *swēte*, *ange* end in an `-e` that
no sound change derives: their Proto-Germanic is *þunnuz, *swōtuz, *anguz — u-stem adjectives that
Old English cites as i-stems. The `-e` is a morphological reanalysis (u-stem → i-stem), and the
attested i-mutation in *þynne* proves the *i* was there. No sound change adds a morpheme; this is
the line `KEEP_WEAK_PRESENTS = False` draws for the verbs, drawn again. Word-scoped rules now supply
these endings: `sporadic_wg_adjective_ja_stem` gives thin and sweet the West Germanic ja-stem *-ī
(Ringe & Taylor, PDF 36), and `sporadic_weak_reanalysis_final_e` gives ange its -e. All three are
exact at 900. A handful more are compounds the descendant-picker took for a simplex (*fetą* →
`sīþfæt`, *trumaz* → `wyrttruma`) — the simplex has no separate OE reflex in the tree, so they are
simply unscoreable at 900.

When 900 stood near 200 exact, these two looked like a cap on what regular sound laws could
reach: pushing 900 toward 75% seemed to need either reconstructed Anglian targets (inventing forms)
or morphology rules for the citation forms (fitting). Since then 900 has passed 80% (the table
above), partly through word-scoped rules for citation forms, which DECISIONS.md allows since
2026-10-07 ("Let the rules and the words shape each other").

Report the **count and the denominator**, never the percentage alone: an earlier expansion took
Proto-Germanic from 222/260 (85.4%) to 310/425 — **+88 exact**
while the rate *fell 12 points*, because 165 new and entirely untuned words entered the
denominator. The old 260 still scored exactly 222; nothing regressed.

The split is the number that means anything:

| | exact | |
|---|---|---|
| the 260 curated words | 222 / 260 (85%) | tuned against, `PREFORM_FIXES` applied |
| the 165 new words | 88 / 165 (53%) | **untuned** — not one `PREFORM_FIXES` entry |

A coin-flip hit rate on words the rules have never seen is the evidence that the cascade
generalises rather than having been fitted to the gold. Since 2026-10-07 the rules and the words
shape each other (DECISIONS.md), so the accuracy table measures fit. New words are therefore scored
before any change is made for them, and the section that adds them records that first-contact
score, as this split records it for the 165.

### Where the 165 new words came from: two filters that were too blunt

Neither pool needed new data — both were already in the extracts, being thrown away.

**A hyphen in the middle of a PIE form is not a bare root.** The builder dropped every hyphenated
form as "a root", but Wiktionary writes morpheme boundaries inside forms that are perfectly
complete: `*gʷʰon-yeh₂` 'wound', `*kort-ús` 'hard', `*mn̥-tó-s` 'mouth', `*ǵnéw-o-m` 'knee'. A root
is *truncated* — it ends (or begins) with the hyphen (`*nem-`, `*gʰeldʰ-`). Only those are dropped
now; the rest have their hyphens stripped. **142 forms, 86 usable.**

**An unaccented form gets initial stress, and that is not a guess.** Proto-Germanic fixes the
stress on the first syllable, so the PIE accent reaches the output through exactly one door:
**Verner's Law**. Where a word has no Verner-eligible fricative the accent cannot affect the 200
form *at all* — and that is measurable, not assumed. Of the 49 unaccented nouns and adjectives,
**40 give a byte-identical Proto-Germanic form under every possible placement of the accent**.
Initial is simply one of them, and it is where Germanic puts the stress anyway.

For the other 9 the accent does change the outcome. Those were admitted as honest untuned misses,
and then corrected in a **separate, deliberate curation pass** — because admission is not curation
and the two must not blur. See below.

### Unstressed \*e lowers to \*a before \*r — and the same passage settles a bad target

The biggest remaining cluster was six words where we derived `*e` and the attestation wanted `*a`,
all of them before `*r`: `*undar`, `*ubar`, `*anþaraz`, `*hwaþaraz`. The cascade already knew that
the raising of unstressed `*e` to `*i` is **blocked** before `*r` (Ringe §5.3.2 (iii)) — but it had
the `*e` simply *staying*, and that is only half of what he says. The `*e` then **lowers**:

> "The regular Gothic and ON reflex is **a**. The OS and OHG spellings are variable, but *a* is a
> frequent variant. Only in northern WGmc ('Anglo-Frisian') do we typically find *e* — and that is
> precisely the area in which PGmc \*a was fronted and typically appears as *e* when unstressed.
> **It is reasonable to infer from this pattern of evidence that unstressed \*e was lowered to \*a
> before \*r already in PGmc.**"

`unstressed_e_to_a_before_r` (t = −950) is dated after the raising, whose exception is what leaves
the `*e` standing for it to find. **+4 exact at 200.**

#### The rule and a bad target, from one paragraph

Adding it broke exactly one word — `other` — and that turned out to be the point. The lexicon
holds the same word twice, from two sources, and they disagree:

| | PIE | Proto-Germanic | |
|---|---|---|---|
| Wiktionary | `*h₂énteros` | `*anþ**e**raz` | now a miss |
| **Ringe** | `*ánteros` | `*anþ**a**raz` | **exact** |

Ringe's paragraph *is* the argument that Wiktionary's `*e` is the **Anglo-Frisian innovation read
back into the protoform** — it is the one form that would refute a rule the rest of the daughters
support. So `ATTESTED_FIXES` corrects the target, which is precisely the case that table is fenced
to allow: a cited reference work correcting a **reconstruction**, never an attestation.

And the same sentence pays a third time. Ringe's aside — PGmc `*a` "typically appears as *e* when
unstressed" in Anglo-Frisian — is the missing Old English rule (`oe_unstressed_ae_to_e`, t = 410):
the brightened `*æ` does not survive unstressed. `*anþaraz` > `*anþæraz` > OE `ōþer`, **exact at
900 as well**.

### Ringe as a SOURCE, not just a reference

`tools/ringe.py` harvests Ringe's own cited derivations straight out of the book. He states them
in a fixed format, which is what makes them machine-readable at all:

> PIE \*dr̥ḱtós 'visible' (cf. Skt dr̥ṣṭás 'seen') **>** PGmc \*turhtaz 'bright' (cf. OE torht);

**247 distinct pairs**, of which **142 are usable word-to-word**; 35 were words we did not already
have, and those are now in the lexicon. They are scored at **200 only** — Ringe gives the Germanic
form, not an Old English chain, so there is nothing to score the later columns against.

**And they are better gold, measurably.** Ringe sits at the top of the source hierarchy, and it
shows in the one number that is not tunable:

| | exact, untuned |
|---|---|
| Wiktionary-sourced words | **~50%** |
| **Ringe-sourced words** | **60%** (21/35) |

Four filters throw away more than half of what he offers, and each one is a trap we have already
been caught by:

- **40 pairs he marks `>!`** — his own notation for a step that is *not* a sound change. They can
  never be derived, so they are not gold. They are kept in `ringe.json` as a **warning**, so that
  nobody hunts a rule for a change that never happened.
- **68 are a stem or a root**, not a word (`*deḱs-`, `*hleuman-`).
- **27 are a Proto-Germanic infinitive** — the wrong-cell trap the verbs already taught us.
- **10 are a weak present** (`*-iþi`), which is levelled and not derived (see above).

#### The PDF fights back, and every repair is load-bearing

The extractor is mostly a list of defences against the PDF's own damage, and each one silently
corrupts the data if you skip it:

- it **splits a diacritic off its base** — `*h₂stér-` renders as `*h 2stér-`, `ḱ` as `k ´`,
  `*fadēr` as `*fad ēr`. Matching on whitespace truncates a form at its first diacritic, which is
  how an early pass produced "PGmc \*fad" and "PGmc \*hund".
- Ringe separates examples with `;`, and an **unfenced match pairs the PIE of one example with the
  PGmc of the next** — it produced `*pah₂ > *wrōt` ('protect' > 'root'). **127 such phantoms**,
  every one of which would have entered the gold as an underivable miss.
- a **trailing `-` marks a stem**, and stripping it as punctuation — the obvious thing to do —
  silently promotes every root to a word. It is kept, and it is what the root filter reads.

#### Kroonen cannot be harvested, and the reason is the scan

Kroonen has far more material (≈3,700 headwords, ≈990 with an explicit PIE preform), but it is a
**scanned** book, and its OCR destroys precisely the diacritics the derivation runs on:

| Kroonen prints | the OCR gives | what is lost |
|---|---|---|
| `*ḱeuk-` | `*keuk-` | the palatovelar — **centumization** |
| `*pr̥d-u-` | `*prd-u-` | the syllabic ring — **u-epenthesis** |
| `*h₂elḱ-` | `*h₂el{H-` | the laryngeal — **colouring** |
| `*flauja-` | `*Jlauja-` | the Germanic headword itself |

Only about a third of its captured PIE forms survive as valid orthography, and the losses are not
random — they are concentrated in exactly the features our rules key on. Bulk-importing it would
poison the gold with inputs whose critical features had been erased, **silently**. It stays a
**lookup** source, hand-consulted one word at a time, which is how every `PREFORM_FIXES` citation
in this project was made.

### The Verner pass

Six words whose Germanic consonant flatly contradicts the accent their input carried. **All six
land, with no regressions**, and they carry downstream (+2 at 900, +3 at 1400, +1 at the surface).

| word | attested | so Verner… | ⇒ the accent | the fix |
|---|---|---|---|---|
| `*braidaz` | voiced `*ð` | fired | oxytone | `*bʰroytós` |
| `*sēdiz` | voiced `*ð` | fired | oxytone | `*seh₁tís` |
| `*þrēduz` | voiced `*ð` | fired | oxytone | `*treh₁tús` |
| `*hreubaz` | voiced `*β` | fired | oxytone | `*krewpós` |
| `*hulþaz` | **voiceless** `*þ` | did not | root | `*ḱĺ̥tos` |
| `*munþaz` | **voiceless** `*þ` | did not | root | `*mń̥tos` |

Four of them had **no cited accent at all** — they came in on the initial-stress default, which is
exactly the case that default was documented as not settling. Two had a *cited* oxytone that the
attested voiceless `*þ` refutes.

**This is inference, not fitting, and the difference is where the evidence comes from.** Verner's
Law is independently established; a voiced fricative therefore *proves* the preceding syllable was
unaccented, and a voiceless one proves it was not. Nothing is read off our derivation — the
consonant would say the same thing if the cascade did not exist. That the reasoning predicted all
six correctly, rather than some of them, is itself the check.

Set `*munþaz` 'mouth' beside `*mundiz` 'hand', which the table already carried:

| | attested | accent |
|---|---|---|
| `*mundiz` | `*mun**d**iz` — voiced | oxytone `*mn̥tís` |
| `*munþaz` | `*mun**þ**az` — voiceless | root `*mń̥tos` |

The same root shape with the opposite accent, and it is the consonant that tells them apart. That
is the whole doctrine in one pair.

**Three lookalikes were deliberately NOT touched.** `*harduz`, `*wurdą` and `*skaudō` also show a
`d`/`ð` mismatch, but theirs is not Verner: it is Wiktionary's own inconsistency about the
Proto-Germanic `*d` allophony (a fricative `[ð]` medially, but written `[d]` after `*r` in some
entries and `[ð]` in others). Bending an accent to chase a notation would be exactly the fitting
this pass is careful not to be.

### A gloss collision is no longer a reason to lose a word

`*angô` is TWO etyma — `*h₂énk-ō` 'a bend, crook' and `*h₂én(h₁)ǵʰō` 'smell'. Neither has a modern
reflex to be named after, so both fall back to the Proto-Germanic headword and collide. They are
not the same word, they have different preforms, and each is a real test of the cascade; dropping
one to keep the name unique threw away evidence to satisfy a naming constraint. They are now told
apart by their Wiktionary sense (`angô-bend`, `angô-smell`) — the job the `id` was introduced to do.

A **word-key** collision is different and still fatal: two etyma that transliterate to the *same*
PIE input are one input to the engine. It derives one form, and no id can make that two answers.

### What the expansion found in the rules

The point of an untuned expansion is that it exercises environments the old lexicon never had, and
it paid immediately.

**Kluge's law was firing on word-initial onset clusters.** Kroonen §2.2.5.2 states it as a voiced
stop geminated by the assimilation of a following `*n` in a stressed syllable — and written that
way it also fires on a `*Cn-` that *begins* the word, where the `*n` is part of the root and no
suffix is in sight. `*ǵnéwom` came out as `**kkewą`, against an attested `*knewą` 'knee' whose
`*kn` is intact.

The law assimilates a **suffixal** `*n` to a **root-final** stop (`*bʰudʰ-nós` > `*buttaz`), and a
root-final stop always has the root's vowel before it. Requiring a preceding vowel fixes it:
`*knewą` now derives exactly and `*buttaz` — the law's own example — still does.

Note what this cost on the old gold: **nothing**. Not one of the 260 curated words has a `*Cn-`
onset, so the bug was completely invisible until 165 new words walked into it. That is the case for
expanding a gold lexicon, in one line.

**Once open:** `*penkʷrós` derived `**fimbraz` against an attested `*fingraz`, with the labiovelar
coming out labial and dragging the nasal with it. On 2026-10-07 finger is exact at every
checkpoint.

### What the gold found in the inherited PIE→PGmc rules

Those rules had never been scored. Against the gold they turned out to have three real faults,
and fixing them took Proto-Germanic from 41 to 61 exact (token-weighted 47% → 76%):

- **Grimm's Law was wrong twice over — in its output and in its clause order.** (a) PIE
  *bʰ dʰ gʰ give voiced FRICATIVES *β ð ɣ (*beβruz, *lɑɣuz, *ɣarðaz); [b d g] are their
  allophones word-initially and after a nasal. Deriving stops outright made every medial one
  wrong and left the West Germanic hardening with nothing to do — worth 14 exact matches alone.
  (b) The clauses must run: aspirates→fricatives, THEN voiceless-stops→fricatives (blocked
  after any obstruent, voiced ones included), THEN voiced-stops→voiceless-stops. *mógʰtis needs
  the first order (its *ɣ shields the *t, giving *mɑxtiz); *h₂éyǵs needs the last (its new /k/
  must not fricativise in turn, giving *aiks not **aixs). Each other order breaks the other word.
- **The low vowel never backed.** PGmc *a is [ɑ], including the *a that laryngeal colouring
  made from *e — so *h₂érmos is *armaz with [ɑ], not a front [a].
- **Final *-n was lost after ANY unstressed vowel.** Only after a non-high one: *-am > *-ą,
  but the numerals *tehun, *newun, *sebun keep their /n/.
- **The laryngeal rules were ordered wrong, and missing a stress condition.** Loss *without*
  lengthening has to precede the post-vocalic loss that lengthens, or the latter eats the
  cases first (*kéh₂ilos > *hailaz, a diphthong, not **hālaz). And whether the vowel lengthens
  depends on STRESS: barytone *dʰóh₁mos lengthens (> *dōmaz) while oxytone *suHnús does not
  (> *sunuz, short). Miss that and doom comes out **damaz.

Two things the gold caught that are worth keeping in mind when reading it:

- The `/xʷ/` cluster of misses was **a real rule, not sporadic noise** — `pgmc_labial_jump`
  (*artikulatorischer Sprung*) derives *five*, *wolf* and *four* together, while *wheel*, the
  control, correctly does not fire. It replaced two word-scoped `lex_*` hacks.
- Two "conventions" turned out to be **sound changes in disguise**. Normalising the gold's
  ɔː/ɛː away would have hidden the raising of the Proto-Germanic long mids (`pgmc_long_mid_
  lowering` + `wg_long_mid_raising`); writing them as rules instead was worth 7 exact matches
  at Proto-Germanic. The lesson: prefer a rule to a normalisation, and let the score decide.

The next steps were then, in yield order: OE breaking (*eald*, *heorte*), the palatalisation and
affrication of velars (§4.3: *ċinn* > *chin*, *heċġ* > *hedge*), the Middle English leg
(§7.3–7.5) and the long-vowel shifting (ch. 8). All four have since been built.

## Transliteration (`tools/pie_ipa.py`)

Wiktionary writes PIE in Indo-Europeanist orthography (`*wĺ̥kʷos`); the engine reads IPA
(`ˈwl̩kʷos`). Validated against the 13 hand-written inputs of the old `pie_to_germanic` project:
11 reproduce exactly, and both differences are that project's own errors (the moved accent on
*mother*, and `ˈbʰreħteːr` writing PIE's breathy `bʱ` with the voiceless-aspirate diacritic `ʰ`).
