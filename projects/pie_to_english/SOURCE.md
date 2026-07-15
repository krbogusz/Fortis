# Source of the PIE → English project

Proto-Indo-European to Present-Day English, scored at four checkpoints.

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
>   Minkova, Jones (*A History of English Phonology*), McMahon, Steponavičius, Plotkin. A sound
>   law is a fact, and facts are not copyrightable: they are **read and cited in the rule that
>   uses them, never redistributed** — `.gitignore` keeps the books out, and no book text belongs
>   in the tree. Because nothing here is redistributed, none of this appears in
>   `docs/acknowledgements.md` (which lists only the CC BY-SA lexicon we do redistribute).

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
(`kaikki/{pie,pgmc,oe,me}.jsonl`).

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
the PIE seed at **−2000** and the attested forms at **200** (Proto-Germanic), **900** (Old
English), **1400** (Middle English) and the modern **final** surface. A form that is not attested
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

What survives is nouns, adjectives and numerals: **249 rows**, the same order as the FLLAPS gold
that `latin_to_french` scores against.

### The residue is untuned, and should stay that way

Of the 240 rows scorable at Proto-Germanic, **126 are new** and have never been curated. They
land **56/128 exact (44%) with no `PREFORM_FIXES` entry at all**, which is the useful number:
the rules were fitted against the old 114, so a coin-flip hit-rate on words they have never seen
says the cascade generalises rather than having been tuned to the gold.

The misses among them are mostly the wrong-preform problem this file opens with — Wiktionary
citing `*h₂ébōl` against a Proto-Germanic `*apaliją` that no cascade can reach from it. They are
*not* evidence the rules are wrong, and the temptation to `PREFORM_FIXES` them until the number
goes back up should be resisted: their whole value is that they are untuned. Curating them is a
separate, deliberate pass, held to the same discipline as the rest of that table — read the
preform off the **attested** form (its consonant voicing, its vowel, its gender ending), never
invent the one feature that would make the cascade land.

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

For anything **reconstructed**, the order is:

> **Ringe** > **Kroonen** > **Wiktionary**

Wiktionary's Proto-Germanic and PIE are anonymous, unrefereed reconstructions of uneven quality.
Ringe (*From Proto-Indo-European to Proto-Germanic*) and Kroonen (*Etymological Dictionary of
Proto-Germanic*) are the standard reference works. **Where they disagree with Wiktionary, they
win** — and that is the normal case, not an exception to be argued for each time.

This applies to *reconstructions only*, and the distinction is the whole point:

| column | status | who wins |
| --- | --- | --- |
| the PIE **input** | reconstruction | Ringe/Kroonen → `PREFORM_FIXES` |
| **200** (Proto-Germanic) | reconstruction | Ringe/Kroonen → `ATTESTED_FIXES` |
| **900 / 1400 / final** | **attestation** — a real recorded form | nobody. Never touched. |

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
origin", \*wintru- has "no certain etymology". Those are honest misses, not failures of the rules,
and should be left alone rather than curated into a number.

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

1. **Only the 200 column.** The 900 / 1400 / final columns are *attested* — real recorded Old
   English, Middle English and modern forms. They are never touched, whatever they cost us.
2. **Only with an explicit citation** from Kroonen or Ringe, quoted in the comment. Never from our
   own inference, and never because a word would otherwise miss.
3. **The entry must be defensible with the derivation switched off.** If the only argument for it
   is "the cascade would then land", it does not go in.

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

  Some rows are not recoverable and remain a permanent ceiling — the ordinals (*seventh*,
  *sixth*, *eighth*) are built on a different suffix in Germanic than in the cited PIE form.
- **The Proto-Germanic column is a reconstruction, not an attestation.** Some of its distance
  from the derived form is transcription convention rather than phonology (see `CONVENTIONS`
  in the builder), so a miss there is a question to investigate, not automatically a rule bug.
- Attested IPA is normalised to what the inventory can segment (script `ɡ`, tie bars, the
  raising/lowering diacritics). A form that still will not segment is left **blank** rather
  than guessed at.

## Rules (`rules.toml`)

Two legs, from two sources:

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

## Where it stands

553 words.

| checkpoint | assessed | exact | within 1 phone |
|---|---|---|---|
| 200 Proto-Germanic | 528 | 449 (85.0%) | 465 |
| 900 Old English | 333 | 250 (75.1%) | 279 |
| 1400 Middle English | 226 | 147 (65.0%) | 176 |
| final Modern (RP) | 177 | 103 (58.2%) | 128 |

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
are not regular.

This keeps the two figures legible: the regular cascade's accuracy is what it derives with no
word-scoped help, and the sporadic layer is a labelled, auditable list of the morphological and
lexical facts on top. The provenance of every gold word travels with it in `words.toml`; the
sporadic *decisions* live in `rules.toml`, where the change itself is.

The 900 denominator is 333, not 337, because the descendant-picker now drops four words whose only
Old English reflex is a COMPOUND — *fetą survives solely in sīþfæt ('journey-vat'), *skaibaz in
sċāffōt — of which just the second element descends from our Proto-Germanic word. Scoring a simplex
derivation against the whole compound is a category error, and `root_nodes` in build_chains keeps
only the Old English node that is not itself descended from another (the compound is a child of the
simplex), leaving those four to score at Proto-Germanic alone. No derived form changed and no hit
moved — the correction is entirely in the denominator, removing rows that never belonged in the
Old English column.

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
  Saxon feature the later columns visibly reject;
* Anglian **rules**, each scoped to a cluster where the gold is uniformly Anglian: smoothing and
  raising before *ht* (`niht`, `riht`, `miht`), and the collapse of our derivation's i-mutated *æe*
  to Anglian *e* (`sċell`, `erfe`) — the derivation-side twin of the gold step above.

This is slow because it must be done cluster by cluster — *ht*, then the *æe* class, then the next —
never in bulk. But it is honest and it moves the number: 900 went 173 → 200 doing it. What it cannot
do is close the whole gap, because much of the residue is not dialect at all but the second thing:

**2. Some misses are a CITATION FORM, not a sound.** OE *þynne*, *swēte*, *ange* end in an `-e` we
correctly do not derive: their Proto-Germanic is *þunnuz, *swōtuz, *anguz — u-stem adjectives that
Old English cites as i-stems. The `-e` is a morphological reanalysis (u-stem → i-stem), and the
attested i-mutation in *þynne* proves the *i* was there. No sound change adds a morpheme; this is the
line `KEEP_WEAK_PRESENTS = False` draws for the verbs, drawn again. A handful more are compounds the
descendant-picker took for a simplex (*fetą* → `sīþfæt`, *trumaz* → `wyrttruma`) — the simplex has no
separate OE reflex in the tree, so they are simply unscoreable at 900.

Together these cap what regular sound-laws can reach: pushing 900 toward 75% would mean either
reconstructing Anglian targets wholesale (inventing forms, i.e. circularity) or adding morphology
rules to hit the citation forms (fitting). **The dialect normalisation is the honest lever, and it
is real but incremental; the rest of the gap is a property of the gold, not the rules.**

Proto-Germanic is **449/528 (85.0%)** exact. Report the **count and the denominator**, never the
percentage alone: an earlier expansion took it from 222/260 (85.4%) to 310/425 — **+88 exact**
while the rate *fell 12 points*, because 165 new and entirely untuned words entered the
denominator. The old 260 still scored exactly 222; nothing regressed.

The split is the number that means anything:

| | exact | |
|---|---|---|
| the 260 curated words | 222 / 260 (85%) | tuned against, `PREFORM_FIXES` applied |
| the 165 new words | 88 / 165 (53%) | **untuned** — not one `PREFORM_FIXES` entry |

A coin-flip hit rate on words the rules have never seen is the evidence that the cascade
generalises rather than having been fitted to the gold. **Do not curate them to pull the rate back
up.** Their value is that they are untuned.

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

**Still open:** `*penkʷrós` derives `**fimbraz` against an attested `*fingraz` — the labiovelar is
coming out labial and dragging the nasal with it. Logged, not chased.

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

Next, in yield order: OE breaking (*eald*, *heorte*), the palatalisation and affrication of
velars (§4.3 — *ċinn* > *chin*, *heċġ* > *hedge*), then the Middle English leg (§7.3–7.5) and
the long-vowel shifting (ch. 8).

## Transliteration (`tools/pie_ipa.py`)

Wiktionary writes PIE in Indo-Europeanist orthography (`*wĺ̥kʷos`); the engine reads IPA
(`ˈwl̩kʷos`). Validated against the 13 hand-written inputs of the old `pie_to_germanic` project:
11 reproduce exactly, and both differences are that project's own errors (the moved accent on
*mother*, and `ˈbʰreħteːr` writing PIE's breathy `bʱ` with the voiceless-aspirate diacritic `ʰ`).
