# Source of the PIE → English project

Proto-Indo-European to Present-Day English, scored at four checkpoints.

> **Licensing — this directory is not all under one licence.**
>
> - **`words.csv` is CC BY-SA 4.0.** It is derived from **Wiktionary**, whose text is CC BY-SA
>   4.0, and that licence is *share-alike*: the derived lexicon carries it too, and so must any
>   redistribution of it. Attribution: **[Wiktionary](https://www.wiktionary.org/) contributors**,
>   via the [kaikki.org](https://kaikki.org/) extracts.
> - **`rules.toml`, `tools/`, `SOURCE.md`** are original work and carry the repo's own
>   **PolyForm Noncommercial 1.0.0**, like the rest of Fortis.
> - **`sources/` is NOT in the repo and must never be.** It holds four copyrighted reference
>   books (Minkova; Ringe; Ringe & Taylor; Kroonen). They are read and cited, never
>   redistributed — `.gitignore` keeps them out. Sound laws are facts and are encoded as rules;
>   no book text belongs here.
>
> Recorded in [`docs/acknowledgements.md`](../../docs/acknowledgements.md), alongside the same
> arrangement for `latin_to_french` (GPL-3.0).

## Lexicon (`words.csv`) — CC BY-SA 4.0

Built in two stages from the [kaikki.org](https://kaikki.org/) machine-readable Wiktionary
extracts (produced by [wiktextract](https://github.com/tatuylonen/wiktextract), MIT; the *data*
is Wiktionary's, CC BY-SA 4.0). Neither stage's output is stored — run them to regenerate:

```
PYTHONPATH=. python projects/pie_to_english/tools/build_chains.py   # kaikki → chains.json
PYTHONPATH=. python projects/pie_to_english/tools/build_gold.py     # chains.json → words.csv
```

`PYTHONPATH=.` (the repo root), **not** `src`: `fortis.analysis.accuracy` imports
`from src.fortis...`, so the root must be on the path. The obvious invocations crash on
`ModuleNotFoundError: No module named 'src'` *before writing anything*, which leaves `words.csv`
untouched and makes a diff falsely read as "reproduced byte-identically". Check the exit status,
not just the diff.

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

Columns: `word` (the PIE input, in IPA), `gloss`, `frequency`, then the attested forms at
**200** (Proto-Germanic), **900** (Old English) and **1400** (Middle English), and the modern
**final** surface. An empty cell means "not attested here" — the engine scores each word at
whichever checkpoints it has. `gloss` is the modern reflex where there is one and the
Proto-Germanic headword (`hurnaz`) where the word died before Modern English; it is a label and
a `--single` lookup key, not necessarily an English word.

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

#### What the weak presents did expose: Sievers' Law is missing

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

448 words.

| checkpoint | assessed | exact | within 1 phone |
|---|---|---|---|
| 200 Proto-Germanic | 425 | 310 | 348 |
| 900 Old English | 335 | 121 | 190 |
| 1400 Middle English | 225 | 39 | 92 |
| final Modern (RP) | 175 | 9 | 40 |

Proto-Germanic is **310/425 (72.9%)** exact. Report the **count and the denominator**, never the
percentage alone: the last expansion took it from 222/260 (85.4%) to 310/425 — **+88 exact** while
the rate *fell 12 points*, because 165 new and entirely untuned words entered the denominator. The
old 260 still score exactly 222; nothing regressed.

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

For the other 9 the accent does change the outcome, and those are honest untuned misses. Reading
the accent off the attested Germanic consonant is legitimate — a voiced fricative proves Verner
fired — but that is the `PREFORM_FIXES` move, a separate and deliberate curation pass. **Admission
is not curation, and the two must not blur.**

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
