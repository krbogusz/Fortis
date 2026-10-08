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

## 2026-10-06: Score the Early Modern evidence at four checkpoints

**Choice:** The Early Modern forms are scored at four years, one per group of orthoepists: 1570
(Hart), 1580 (Bullokar, Mulcaster), 1621 (Gil) and 1687 (Coles, Cooper). This replaces the single
Early Modern checkpoint in "Gather more data for pie_to_english" (2026-10-06), item 2.

**Reason:** The attested forms run from 1551 to 1687 in four groups, with nothing between 1621 and
1674. One year would score Bullokar's and Cooper's forms against the same cascade state, across
most of the Great Vowel Shift.

**Rejected:**
- One checkpoint at 1621, the median of the evidence.
- One checkpoint per form's own year: eight stages, two of them with a single form.

## 2026-10-06: Add pypdf as a dev dependency

**Choice:** `pypdf` joins the `dev` dependency group in `pyproject.toml`.

**Reason:** `projects/pie_to_english/tools/ringe.py` imports it to read the Ringe PDF, but no
dependency declared it, so the tool failed in a fresh environment. The dev group is installed by
`uv sync` by default. The engine itself still has no runtime dependencies.

**Rejected:**
- A separate dependency group for the data tools, which `uv sync` would not install by default.
- Installing it ad hoc (`uv run --with pypdf`), which is what replaced it for one run.

## 2026-10-06: Transcribe Old English spellings by rule

**Choice:** Where Wiktionary gives an Old English spelling without IPA, the 900 target is
transcribed from the spelling by `projects/pie_to_english/tools/oe_ipa.py`. The tool refuses
spellings its rules cannot read. Reconstructed (starred) forms and spellings of a different
formation (a compound, a prefixed or derived word) are not transcribed.

**Reason:** Old English spelling with macrons and dotted palatals is close to phonemic. The tool
agrees with Wiktionary's own IPA on 435 of 450 lemmas, and every disagreement is information the
spelling lacks (an unmarked long vowel, compound stress). Asked for on 2026-10-06.

**Rejected:** Leaving the spellings without a target.

## 2026-10-07: Derive the *k of taikuraz by Kroonen's laryngeal velarization

**Choice:** `kroonen_laryngeal_velarization` (*-aiH- before *u or *w > *-aik-) derives
*taikuraz from the cited *dayh₂uros.

**Reason:** Both books take the *k from a laryngeal before a labial glide. Kroonen states it as a
sound law with a second example, *aikwernan- (s.v. *taikwer-, PDF 546; PDF 48–49). Ringe reaches it
through Cowgill's law, but needs a different preform with *h₂w and an analogy with *swehuraz for
the *-ur- (PDF 98, 181). Kroonen's route needs neither. Tested: taikuraz exact at 200 and 403, no
word worse.

**Rejected:** Ringe's route: Cowgill's law on a preform *dayh₂wēr, plus an analogical *-ur-.

## 2026-10-07: Derive PGmc *fōr 'fire' as Ringe does

**Choice:** `pgmc_initial_cuv` and `pgmc_w_loss_labial_round` (Ringe §3.2.5 (ii), §3.2.6 (i))
derive *fōr from the existing preform *ph₂uṓr: *pwōr, then loss of *w between a labial and a round
vowel.

**Reason:** It needs no new preform and makes fire exact at 200. Restricted to an initial obstruent,
which is what Ringe's examples have (*s, *p), it changes no other word.

**Rejected:** Kroonen's preform *péh₂ur with Mahlow's law (s.v. *fōr-, PDF 191). Mahlow's law is
decided on its own.

## 2026-10-07: Kluge's law after Verner for *ðn (white)

**Choice:** Adopt Kroonen's post-Verner Kluge's law for a Verner-voiced *ð before *n and the accent
(`kroonen_kluge_after_verner`), with his late shortening of a geminate after a long vowel
(`kroonen_late_geminate_shortening`), and his preform *ḱweytnós for white.

**Reason:** Ringe rejects Kluge's law and gives no derivation of *hwītaz. Kroonen derives it
(*ḱueit-nó- > *hwītta- > *hwīta-, s.v. *hwīta-, PDF 307), and his chronology puts the law after
Verner (§2.2.5.2, §2.2.6). Ringe's counterexample *swiknaz has *kn, which this restricted form does
not touch. Tested: white exact at all five checkpoints, no other word changed. The cascade's older
pre-Grimm `kluges_law` is left as it is.

**Rejected:** Following Ringe and leaving white without a derivation.

## 2026-10-07: Do not adopt Mahlow's law

**Choice:** The cascade has no rule for Mahlow's law (Kroonen's *ōu > *ō except before two
consonants or word-finally, §2.1.5, PDF 22–23).

**Reason:** Ringe derives *stauraz regularly from *steh₂-u-ro- (PDF 107), against Kroonen's *stōra-
from the same kind of preform. Tested with Kroonen's lengthening before *u and his Mahlow rule:
roo lost its exact match at 200 and 900 (OE rōw keeps the *w that Ringe's chronology preserves),
and stōraz did not become exact.

**Rejected:** Kroonen's Mahlow's law.

## 2026-10-07: Open-syllable lengthening only before a final schwa

**Choice:** `me_open_syllable_lengthening` applies only when the second syllable is a coda-less
final schwa. The four sonorant-peak words with long ME vowels (acre, navel, haven, beaver) are
lengthened by a word-scoped rule (`sporadic_osl_sonorant_coda`).

**Reason:** Minkova §7.5.2.1 (PDF 223) counts the outcomes. Words with a coda-less final schwa
lengthen in 95.8 per cent of cases. Of the disyllables whose second syllable survives, 84.8 per cent
resist the lengthening. Of those with a sonorant peak, about a quarter lengthen. A rule should
describe the majority, so the minority becomes the word list. Tested: any becomes exact at final,
navel and seventh move closer, and the exception rules for father, water and weather become
unnecessary.

**Rejected:** Lengthening every open syllable and listing the words that stay short. That was the
earlier design, and it needed a new exception for every word with a surviving second syllable.

## 2026-10-07: Date the loss of [x] by the orthoepists

**Choice:** `eme_x_loss` drops the velar and palatal fricative at 1640, between Gil (1621), who
still writes it in night, right and brightness, and Wallis (1653), who says it is "almost always
omitted" (Jones §4.3(1), PDF 251–252). The lengthening of the vowel before it stays at 1450.

**Reason:** The Early Modern targets are Jones's readings of the orthoepists. Hart (1570) and Gil
(1621) keep the fricative in might, night, right and daughter, so a cascade that loses it in the
15th century cannot match those columns. Jones says the loss was complete in Southern speech by the
late 17th century.

**Rejected:** The 15th-century dating in Minkova §5.1.4 (full-scale evidence in the 15th century),
Pyles & Algeo p. 176 ("as early as the fifteenth century in all England south of the Humber") and
Steponavičius §202 (early 15th century). Pyles & Algeo add that old-fashioned speakers kept the
sounds into the late 16th century, which is what the orthoepists record.

## 2026-10-07: Stage the shift of ME ī and ū through [əɪ] and [əʊ]

**Choice:** `emode_vowel_shift` (1600) gives [əɪ] and [əʊ], and `eme_price_mouth_lowering`
(1690) lowers them to [aɪ] and [aʊ].

**Reason:** Minkova gives [əɪ] and [əʊ] as the intermediate stage and as the Shakespearean value
(Fig. 8.6 and n. 18, PDF 257). Pyles & Algeo date [aɪ] and [aʊ] to "the course of the seventeenth
century" (p. 171, PDF 93). Jones reads Gil (1621) as [ei]- or [əi]-type and still writes Cooper's
(1687) reflex as [ei]/[əi] (PDF 225, 252–253), so the lowering comes after the 1687 checkpoint.
Tested: night and right become exact at 1621; no final row changes.

**Rejected:** A one-step shift to [aɪ], [aʊ] at 1600. Also rejected: Minkova p. 261, which says the
changes were "pretty much complete by the end of the sixteenth century"; that conflicts with her
own footnote 18 and with the orthoepists.

## 2026-10-07: Date the MEAT–MEET merger before Cooper

**Choice:** `pde_meat_merger` (ME ɛ̄, by then [eː], > [iː]) is dated 1680, before the 1687
checkpoint.

**Reason:** Jones reads Cooper's (1687) "e long" (bean, dream, eat) and "ee" (ear, fear, near) as
[iː] (Table 4.8, PDF 259), and those readings are the 1687 targets. Pyles & Algeo (p. 173, PDF 94)
say the [i] pronunciation of ME ē words had been an option since the beginning of the Modern
period. Tested: dream, ear and ausô become exact at 1687; no other row changes.

**Rejected:** The 18th-century date the rule had, which follows Pyles & Algeo's account of the
fashionable [e] that lasted "from about 1600 to the mid-eighteenth century". Jones notes the
controversy over Cooper's values, so this decision depends on his reading.

## 2026-10-07: Date the Vowel Shift at 1560, with ME ā at 1600

**Choice:** `emode_vowel_shift` (the high and mid vowels) is dated 1560, and the step ME ā > [ɛː]
is a separate rule, `emode_vowel_shift_low`, at 1600.

**Reason:** Minkova dates the shift c. 1400–1550 (Fig. 8.6, PDF 257). Hart (1570) already has [oː]
in ghost and still has [aː] in fāðr, and Cooper (1687) has [ɛː] in name. The 1400 targets follow
the traditional reconstruction with unshifted vowels, so the shift must come after 1400. The
shortenings dated 1550 must come before it. Tested: ghost becomes exact at 1570; might moves one
step away there (Hart's short [ɪ]); no final row changes.

**Rejected:** The single shift at 1600. Also rejected: Stenbrenden's 13th–14th-century start for
the high and upper-mid vowels (Minkova §8.2.2.1, PDF 253–254), which the 1400 targets do not show.

## 2026-10-07: Let the rules and the words shape each other

**Choice:** In `pie_to_english`, the rules and the lexicon are developed together:

1. A miss may start a rule. A regular rule applies to a class of sounds, not to listed words. It
   stays if, across all checkpoints, it makes more targets exact than it breaks. A rule without a
   source says in its description that it was inferred from the lexicon, and names the words it
   came from.
2. A word-scoped rule names its cause, such as analogy with a named word, Norse influence or a
   dialect form. If no cause is known, the rule says so.
3. The PIE input and the 200 and 403 targets may be revised to fit the rules when the attested
   forms allow it. The note keeps the old value and says that the rules prompted the change.
4. The 900, 1400 and final targets keep the four cases, but any source may support a correction,
   not only a printed book. Where the spelling leaves a sound open, such as vowel length, the rules
   may choose the reading.
5. New words are scored before any change is made for them, and SOURCE.md records that
   first-contact score.

The Early Modern targets stay as they are: no source corrects them.

Item 4 amends "Correct attested targets with a citation, in four cases" (2026-10-06). The entry
also replaces three passages of SOURCE.md: the ban on curating the untuned words, and rules 2 and
3 of "Correcting the gold itself".

**Reason:** The project exists to develop a set of rules, and a miss is the main evidence of a
missing rule or a wrong reconstruction. While every change needed a printed source, misses such as
father, water, dross, kind and cow stayed open because no source at hand explains them. A
reconstruction is itself inferred through sound laws, so it may answer to the rules. An attested
form is the data, so it keeps the four cases. Once the rules and the words shape each other, the
accuracy table measures fit. The first-contact score measures how well the rules predict words
they were not shaped on. Asked for on 2026-10-07.

**Rejected:**
- Requiring a printed source for every rule and every target change.
- Letting every column move, the attested ones included.
- Loosening the rules only, and keeping every target under the cited four cases.
- Two further checks: a count of the word-scoped rules beside each accuracy table, and a score
  with the word-scoped rules switched off.

## 2026-10-07: Model Anglian retraction before *lC

**Choice:** `oe_anglian_retraction` retracts *æ to *a before *l and a consonant, as the Anglian
dialects did (Ringe & Taylor §6.2.3, PDF 199 and 234). The seven West Saxon 900 targets of this
cluster (eald, ċeald, steall, sealf, healm, heals, mealt) are corrected to their Anglian forms
under the dialect case of the four cases.

**Reason:** The Middle English and modern forms continue the Anglian vowel: ME ōld, cōld with its
k, halm, hals and salve. So the West Saxon targets record a dialect variant that the later columns
do not continue. Wiktionary lists ald and cald as the Anglian forms, and halm, salf, stall and
malt as alternative forms. The rule makes the velar of cold regular, which a word-scoped rule
supplied before. Tested: every target in the cluster is exact before and after, and no other row
changes.

**Rejected:** Keeping the West Saxon targets and breaking, with word-scoped rules for the Anglian
outcomes. It scores the same but models a dialect that the later columns do not descend from.

## 2026-10-07: Take the modern targets from CUBE

**Choice:** The final targets are the transcriptions of CUBE, Current British English searchable
transcriptions (Geoff Lindsey and Péter Szigetvári, seas3.elte.hu/cube), in CUBE's default symbols
for current Standard Southern British. Three notational changes fit them to the project's
inventory: CUBE's r is written ɹ, its ʧ and ʤ are t͡ʃ and d͡ʒ, and its stress accent becomes ˈ
before the stressed syllable. Where a spelling has several CUBE entries, the one with the word's
part of speech is taken (wind is the noun /wɪ́nd/). Ten words that CUBE lacks (atter, dere, ell,
erf, lede, neve, nift, sweven, theed, wort) keep their Wiktionary RP form, written in CUBE's
symbols with the table on CUBE's symbols page. Each note keeps the old value. The cascade gets rules
for the changes that CUBE's accent page lists between classic RP and current Standard Southern
British.

**Reason:** Asked for on 2026-10-07. The Wiktionary targets use the symbols Gimson chose for classic
RP, an accent that CUBE's authors call "rarely heard in the 21st century". CUBE gives one
recommended pronunciation per entry for the standard accent heard today. CUBE's pages say
"© Geoff Lindsey & Péter Szigetvári" and state no licence; the transcriptions are used as facts
about pronunciation, with the source in each note, and publishing them needs a separate decision.

**Rejected:**
- Keeping the Wiktionary RP targets.
- Converting the RP targets symbol by symbol instead of taking CUBE's entries. That misses the words
  whose CUBE form differs in more than its symbols: dew /ʤʉ́w/, salve /sálv/.
- CUBE's optional Gimsonian display, which keeps the old symbols.

## 2026-10-07: Geminate *w from a laryngeal only before the accent

**Choice:** `w_gemination_before_laryngeal` turns *wH into *ww only when the accent follows. The
preforms of dew and bewwą move the accent to the ending. `velar_labialization` asks for an
obstruent, and the word-scoped `sporadic_glide_gemination` (dew, lawwō) is deleted.

**Reason:** Kroonen states Holtzmann's law as pretonic gemination (§2.2.5.7, PDF 36–37) and says of
*lawwō that "the geminate *-ww- points to original oxytony" (PDF 370). Of the *wH words in the set,
dew, lawwō and bewwą have *ww, and þrawō and awô, both root-accented, have a single *w. The
condition fits all of them. The gemination rule had never worked: `velar_labialization` matched
*w + *w and merged the geminate, and the word-scoped rule put it back for dew and lawwō. Tested:
bewwą becomes exact at 200, 403 and 900, dew and lawwō stay exact, and no other score changes.

**Rejected:**
- Kroonen's general pretonic gemination of *j and *w. It made twajjaz and wajjuz exact at 200 and
  broke 12 words, among them free, kin, thin, widow and gelwaz. Kroonen calls the counter-examples
  "numerous" (PDF 36). The *jj of ajją, twajjaz and wajjuz stays open.
- The laryngeal condition without the accent. It geminates þrawō and awô.

## 2026-10-07: Publish the CUBE targets with credit

**Choice:** The CUBE transcriptions in `projects/pie_to_english/words.toml` may be published with
the rest of the repository. Each note names CUBE, and `docs/acknowledgements.md` credits its
authors. This settles the question that "Take the modern targets from CUBE" (2026-10-07) left open.

**Reason:** Asked on 2026-10-07, the project owner judged CUBE free to use. CUBE's about page credits
its design and compilation to Péter Szigetvári and Geoff Lindsey, names its core database (Ádám
Nádasdy and Szigetvári, *Huron's English Pronouncing Dictionary*, 2000), and states no licence.

**Rejected:**
- Asking the authors for permission first.
- Keeping the targets local until a later decision.
- Replacing them with Wiktionary RP written in CUBE's symbols.

## 2026-10-07: Do not adopt Dybo's law

**Choice:** The cascade has no regular rule for Dybo's law, Kroonen's pretonic shortening of a long
vowel before a resonant (§2.1.2, PDF 17). delō, his example, joins the word-scoped
`lex_laryngeal_lost_without_lengthening` with his account as its cause.

**Reason:** Tested as a regular rule, the law made delō exact at 200 and broke dūnaz, glēmaz, hūnaz,
mēraz and sīmô at 200, and three of them again at 403 or 900. All five have oxytone preforms and
attested long vowels. Saving the law would mean moving five accents with no book behind them. Ringe
holds that "there was certainly no regular sound change that could have shortened these vowels"
(PDF 109).

**Rejected:**
- Kroonen's Dybo's law as a regular rule.
- Moving the accents of the five words to the root to fit the law.

## 2026-10-07: Geminate pretonic *j after a surviving vowel

**Choice:** `kroonen_holtzmann_j` doubles a *j that stands before the PIE accent, after *e, *o, *a
or the schwa of a first syllable. It does not apply after *i or after a schwa that is later lost.

**Reason:** Kroonen states Holtzmann's law as pretonic gemination (§2.2.5.7, PDF 36–37) and derives
*twajjan from *dwoi-óm and *wajju- from *wh₁̥i-u- (PDF 569, 608). His unrestricted law also doubled
the *j of free, frijō, sijǭ, kin and kunją, which have a single *j. In all five the *j follows *i
or a schwa that the cascade later deletes. Tested with the restriction: twajjaz and wajjuz become
exact at 200, and no other row changes. ajją stays open, since Kroonen's derivation of it also needs
Mahlow's and Dybo's laws.

**Rejected:**
- Kroonen's unrestricted pretonic gemination of *j.
- A laryngeal condition like the one for *w. It covers twajjaz (*dwoyHós) but not wajjuz.

## 2026-10-07: Adopt Kroonen's West Germanic velarization of *w

**Choice:** `wg_w_velarization` turns *w between two high vowels, one of them rounded, into *ɣ
between the 200 and 403 checkpoints. youth gets a word-scoped hiatus glide, an accent on the
syllabic *n̥, and Kroonen's PGmc *juwunþiz as its 200 target.

**Reason:** Kroonen derives the *g of PWGmc *jugunþi from *juwunþi- by this velarization (PDF 316),
and Ringe & Taylor give *jugunþi with no derivation (PDF 156). Tested alone, the rule changes no
word. With the youth changes, youth becomes exact at 200 and 403 and moves closer at 900 and final.
OE ġeoguþ still misses: its second vowel shows no i-umlaut, which Ringe & Taylor's double umlaut
(PDF 266–268) would predict, so the word was probably remodelled as an ō-stem, as gūþ was.

**Rejected:**
- midge by the same rule. Its short *u needs Dybo's law, which the cascade does not adopt.
- Replacing `sporadic_nine_nigun`. Kroonen's account needs a raising of *e before *u that OE
  seofon does not show.
- Lengthening unstressed vowels before a nasal and a voiceless fricative. It brought youth closer at
  900 but gave the wrong vowel in even, and it changed no exact count.

## 2026-10-07: Keep Mahlow's law out after a second test

**Choice:** The cascade still has no rule for Mahlow's law. "Do not adopt Mahlow's law" (2026-10-07)
stands.

**Reason:** Asked for a re-test on 2026-10-07. Kroonen's account has two steps: a laryngeal lost
before *u lengthens the vowel, and the long *ōu then loses its glide in an open syllable (§2.1.5,
PDF 22–23). As stated, the two steps broke young, youth, roo, grēwaz and stauraz-stake and gained
no exact row. Limited to a stressed non-high vowel, and to the glide after a back long vowel, they
still broke roo, whose *rōwō keeps its *w, and gained nothing. stōraz and bottle came closer but did
not become exact. cow does not fit either: Kroonen's rule shortens *ōu word-finally, which gives *au,
not the *ō of the 200 target.

**Rejected:**
- Kroonen's lengthening before *u with his glide loss, in both forms.

## 2026-10-07: Start a word at its earliest secure reconstruction

**Choice:** A word enters the cascade at its seed, its earliest form: the engine skips every timed
rule dated before the seed. In `pie_to_english`, a word whose PIE etymology no book supports starts
at its Proto-Germanic form. The PIE form that Wiktionary cites moves into the word's note. The
first such words are winter, steer, gaukaz, bladą and elmaz.

**Reason:** Asked for on 2026-10-07. These five words missed at every checkpoint because their PIE
inputs are guesses: Kroonen gives winter "no certain etymology", steer "uncertain origin", calls
the cuckoo word onomatopoeic and *blada- "created ... within Germanic itself", and has no entry
for elm. Started at Proto-Germanic, their Old English, Middle English and modern rows test the
later rules. Every word in the other projects is seeded at or before its project's earliest rule,
so their outputs do not change.

**Rejected:**
- Back-projected PIE inputs fitted to the Proto-Germanic targets. They would score at 200 without
  predicting anything.
- Leaving the five words as residue.

## 2026-10-07: Draw the next batch from Kroonen's headwords, starting at Proto-Germanic

**Choice:** In `pie_to_english`, the second first-contact batch comes from Wiktionary's
Proto-Germanic nouns, adjectives and numerals that the lexicon lacks, whose stem is a headword in
Kroonen, and that reach an attested Old English word. Fifty are taken: the most frequent, by their
modern reflex, of those with an Old English, a Middle English and a single modern reflex. They
start at their Proto-Germanic form. A Middle English target is kept only when the Middle English
entry's etymology names the word's Old English form.

**Reason:** Asked for on 2026-10-07. The bootstrap keeps only Proto-Germanic records with an
inherited PIE parent, and 418 of the 422 candidates have none in Wiktionary, so it never reached
them. Kroonen's headword confirms each reconstruction. The batch tests the rules after
Proto-Germanic. Its words have no PIE input in Wiktionary, and Kroonen's preforms would have to be
transcribed by hand from the scanned text. The Middle English check removes the fault that gave
kīþą and aihtiz the targets of other words.

**Rejected:**
- Transcribing Kroonen's PIE preforms for every word now, so that the batch also tests the 200
  column. That can follow as a separate step.
- Taking all 422 candidates. Fifty keeps the batch the size of the last one.
- Taking Middle English IPA by page title alone, as the bootstrap does.

## 2026-10-08: Derive midge by Kroonen's velarization after all

**Choice:** midge goes through `wg_w_velarization`, as youth does. It takes the same word-scoped
hiatus glide (*muH-íh₂ > *muwī), and a word rule levels the root *mug- onto the jō-stem of the
genitive. Its 200 target becomes Kroonen's *muwī. This replaces the rejection of midge in
"2026-10-07: Adopt Kroonen's West Germanic velarization of *w".

**Reason:** That entry rejected midge because its short *u seemed to need Dybo's law. It does not:
`loss_of_laryngeals_before_vowels` already drops the *H before a vowel without lengthening, so the
*u is short. Kroonen (PDF 420) gives the paradigm *muwī, gen. *mujjōz, the velarization of the
nominative's *w and the spread of *mug- to the genitive, and he gives bridge the same history (PDF
119). Tested: midge becomes exact at 200, 403, 900, 1400 and final, and no other row changes.

**Rejected:** Keeping Wiktionary's *mugjō as the 200 target. It writes the West Germanic *g into
Proto-Germanic.

## 2026-10-08: Explain ġeoguþ by the loss of a third-syllable *-i, without adding the rule

**Choice:** OE ġeoguþ has no i-umlaut in its second vowel because PWGmc *jugunþi lost its final
*-i, as Ringe & Taylor derive it (*jugunþi > *jugų̄þ, PDF 70–71, 156). This replaces the remark in
"2026-10-07: Adopt Kroonen's West Germanic velarization of *w" that the word was probably remodelled
as an ō-stem. The cascade does not add the loss as a rule, so youth still misses at 900.

**Reason:** Asked for on 2026-10-08: add the rule only if it gains more exact rows than it breaks.
Ringe & Taylor state the loss as a hypothesis. A final short high vowel was lost in the third or a
later syllable, unless a short high vowel and one consonant stood before it. Tested at 404 for *-i
alone, the rule breaks undern (ˈundorn) and does not fix youth. The *u it leaves before the *þ is
short in the cascade, so it falls to the OE o of ˈjugoθ. Ringe & Taylor's *ų̄ is long there, but
the cascade lengthens only stressed vowels before a nasal and a fricative, because the ordinals
keep a short vowel (seofoþa). The rule does not reach fergunją, whose *-uni keeps its *-i under the
hypothesis.

**Rejected:**
- The rule for *-i alone: 900 loses one exact row (undern).
- The rule for *-i and *-u: 900 loses two (undern, and soul, whose ending Ringe & Taylor say was
  restored, PDF 71).

## 2026-10-08: Draw a third batch from Kroonen's headwords by the same criteria

**Choice:** In `pie_to_english`, the third first-contact batch takes fifty more words by the
criteria of "2026-10-07: Draw the next batch from Kroonen's headwords, starting at Proto-Germanic":
the most frequent Proto-Germanic nouns, adjectives and numerals that the lexicon lacks, whose stem
is a Kroonen headword, and that have an Old English, a Middle English and a single modern reflex.
They start at their Proto-Germanic form. A record is passed over when its modern spelling is mostly
another word, or when another record in the batch has the same modern word.

**Reason:** Asked for on 2026-10-08, to test the rules added on 2026-10-07 and 2026-10-08 on words
they were not shaped on. The second batch's criteria and size keep the two first-contact scores
comparable.

**Rejected:**
- Adding words with only an Old English reflex, which test the Old English rules alone.
- Seeding the batch at PIE with Kroonen's preforms, transcribed by hand from the scanned text.
- Taking all 115 words that qualify.

## 2026-10-08: Port Fortis to Rust, checked by identical reports

**Choice:** Port the whole Python program to Rust, to see whether it runs faster. The port lives
in `rust/`, a Cargo crate named `fortis` built with the stable toolchain from rustup (Rust 1.99).
It covers the loaders, the rule parser, the engine, every report the CLI writes, and the induction
CLI. The web app keeps running the Python engine through Pyodide until a later WebAssembly step.
The port is correct when, on all five shipped projects, the Rust binary writes the same report
files as the Python CLI, byte for byte. `rust/parity.sh` runs both and diffs them. Rust gets unit
tests only where the reports cannot show a fault.

The crate uses these dependencies:
- `toml` with `preserve_order`: reads the TOML project files in file order (replaces `tomllib`).
- `indexmap`: maps that keep insertion order, as Python's `dict` does.
- `csv`: reads `letters.csv` and the CSV inventories (replaces `csv.DictReader`). The reports are
  written by hand, to match `csv.writer`'s quoting exactly.
- `rayon`: derives the words in parallel (replaces `multiprocessing`).
- `clap`: parses the command line (replaces `argparse`).
- `unicode-general-category`: tells a combining mark from a base character (replaces
  `unicodedata.category`).
- `caseless`: Unicode case folding for the blame report's sort (replaces `str.casefold`).

**Reason:** Asked for on 2026-10-08. A run of `pie_to_english` takes 9.4 s in Python: 2.0 s
deriving, 4.7 s of analysis and 2.6 s writing reports. A port of the engine alone could save at
most 2 s, so the whole program moves. Identical reports prove the port without porting the
9,500 lines of pytest tests.

**Rejected:**
- Porting only the engine and keeping the Python analysis.
- A Rust extension module called from Python (PyO3), which adds a build step to the Python
  install.
- Porting the pytest suite to Rust tests.

The Python CLI writes `rule_dependencies.html` with its edges in set-iteration order, which
changes with the hash seed for `latin_to_french` and `pie_to_english`. The Rust port writes them
in sorted order, and `rust/parity.sh` compares that file with its edges sorted on both sides.

## 2026-10-08: Make the dependency graph's edge order deterministic in Python

**Choice:** `build_dependency_graph` walks a firing's consumed segments in sorted order, so
`rule_dependencies.html` lists its edges in the same order on every run, and in the order the Rust
port writes them. `rust/parity.sh` now compares that file byte for byte. This replaces the note in
"2026-10-08: Port Fortis to Rust, checked by identical reports" that the parity script compares
the file with its edges sorted.

**Reason:** Asked for on 2026-10-08. The edge order followed set iteration, which varies with
Python's hash seed, so two runs of `latin_to_french` or `pie_to_english` wrote different files.

**Rejected:** Keeping the normalization in the parity script, which leaves the Python report
nondeterministic.

## 2026-10-08: Run the web app on the Rust engine, compiled to WebAssembly

**Choice:** The web app runs the Rust port in place of the Python engine under Pyodide. A second
crate, `rust/web` (`fortis-web`), wraps the `fortis` crate for the browser and builds with the
stable toolchain for the `wasm32-unknown-unknown` target. The engine runs in a Web Worker, so the
page stays responsive during a run. The project files stay on the main thread, so reading and
editing them stays synchronous. The worker gets a copy of the user's files with the first engine
call after an edit. The loaders read through a file source, so one loader reads the disk for the
CLI and a map of texts for the browser. This is the WebAssembly step that "2026-10-08: Port Fortis
to Rust, checked by identical reports" left for later.

The change is correct when the app shows what the Pyodide app showed. On all five shipped
projects, the new engine gave the same JSON as the old helper for a full run, three single words,
five class queries and the feature tree, and the same report texts. The old helper read the
reports back with `\n` line ends; the new one keeps the `\r\n` that the CLI writes.

The change adds these dependencies:
- `wasm-bindgen` (crate): the bindings between the WebAssembly module and JavaScript (replaces
  Pyodide's bridge between Python and JavaScript).
- `wasm-pack` (build tool, installed with `cargo install`): builds the crate, then runs
  `wasm-bindgen` and `wasm-opt` on it (replaces the `engine.tgz` tarball of `src/`).

It removes the `pyodide` npm package.

**Reason:** Asked for on 2026-10-08, after the Rust port ran about 30 times faster than Python.
In headless Chrome on the same machine, a full run of `pie_to_english` took 27.5 s with Pyodide
and 2.1 s with the WebAssembly engine. `latin_to_french` took 21.5 s and 1.6 s. The engine ships
as one 1.5 MB file. GitHub Pages serves `.wasm` files with the `application/wasm` type that
streaming compilation needs.

**Rejected:**
- Keeping Pyodide beside the WebAssembly engine.
- Running the engine on the page's main thread, as the Pyodide app did, which freezes the page
  during each batch.

## 2026-10-08: Run the web engine in one thread

**Choice:** The web engine runs in one thread. The `fortis` crate's rayon calls fall back to the
calling thread on `wasm32-unknown-unknown`. This replaces the plan, chosen earlier on 2026-10-08,
to run rayon's threads in the browser through `wasm-bindgen-rayon`, with `coi-serviceworker` to
make the GitHub Pages site cross-origin isolated.

**Reason:** Measured in headless Chrome on an 8-core machine, threads made the engine slower. A
full run of `pie_to_english` took 2.0 s with 1 thread, 2.3 s with 2, 3.7 s with 4 and 10.8 s with
8. Rust's WebAssembly allocator guards all memory with one global spin lock, and the engine
allocates constantly. That is the likely cause, but it was not profiled. Threads also needed a
pinned nightly toolchain that rebuilds the standard library, extra linker flags for a shared
memory, and a service worker that reloads the page on the first visit.

**Rejected:**
- Threads through `wasm-bindgen-rayon` and `coi-serviceworker`, as above.
- Keeping the threaded build but starting one thread, which keeps the nightly toolchain and the
  service worker for no gain.
- Looking for an allocator with per-thread caches, which adds a dependency and may still not beat
  one thread.

## 2026-10-08: Move the Rust crates into a Cargo workspace at the root

**Choice:** `Cargo.toml` at the repository root declares a workspace with two members:
`crates/fortis` (the library and the three commands) and `crates/fortis-web` (the WebAssembly
session). `default-members` holds only `crates/fortis`, so `cargo build` and `cargo test` skip the
web crate, which `web/scripts/build-engine.mjs` builds. The release profile lives in the root
manifest. A command finds `projects/default` two folders above its crate, or through `FORTIS_ROOT`.

**Reason:** With Python gone, a folder named `rust/` no longer marks one version among two. A root
workspace lets `cargo build` and `cargo test` run from the repository root.

**Rejected:** Keeping the crates in `rust/`.

## 2026-10-08: Match a feature name in a spec as a whole word

**Choice:** The parser accepts a feature name or short name in a spec only where no ASCII letter
or `_` touches it. It searches the spec with its spaces, so a space separates words. `+voice`,
`αback`, `tone@2` and `mid tone` still name their feature.

**Reason:** The parser searched for each name as a bare substring. In `+nonexistent` it found
`t`, the short name of `tone`, and reported "Could not identify value for 'tone'". It now reports
that it cannot identify the feature. The Python program had the same fault. No saved report
changes.

**Rejected:** Matching only at the end of the part before the colon, which would reject a
position suffix such as `tone@2`.
