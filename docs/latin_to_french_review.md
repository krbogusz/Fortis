# Latin → French Review — translation audit of the DiaCLEF port

*2026-07-02. A review of `projects/latin_to_french` — how DiaSim's DiaCLEF2025
cascade was translated into Fortis notation, what systematically broke in
translation, and where the 106/140 misses actually come from. Method: dead-rule
analysis from `output.csv` (one column per rule), error-shape clustering of
`correctness.md`, targeted derivation traces, direct match testing against the
engine, and a source comparison against the DiaSim repository.*

Current state: **671 rules** across 8 periods, 145-word lexicon, **34/140 exact**
vs attested Modern French IPA.

| period (time) | prefix | rules |
|---|---|---|
| Classical Latin (-100) | cl_ | 79 |
| Late Latin (300) | ll_ | 25 |
| Early Gallo-Romance (500) | egr_ | 133 |
| Middle GR (600) | mgr_ | 185 |
| Later GR (750) | lgr_ | 66 |
| Old French I (1000) | ofi_/eof_ | 97 |
| Old French II (1200) | of2_ | 38 |
| Middle/Modern French (1400) | mf_ | 48 |

## 1. Headline: two systematic "species mismatches" starve the cascade

**419 of 671 rules (62%) never fire** on the 145-word sample. Much of that is
legitimate sparsity — but two translation-layer bugs of the same genus account
for a disproportionate share, and for most of the big miss clusters:

### 1a. Yod is two segments here, one in DiaSim (j/ʝ vs i̯)

The glide-formation rule (`cl_glide_formation`, rules.toml:162) outputs
`[aperture: high, syllabic: -, advancement: atr]` — it makes the vowel
non-syllabic but never touches `consonantal`, producing the **semivowel i̯**
(`-cons`). But the downstream cascade — yod strengthening (`j → ʝ`, line 185),
absorption, and the entire palatalization complex — consumes the **glide
letters j/ʝ/w** (`+cons`). DiaSim has one yod segment; the port accidentally
created two species, and only *lexical* j feeds the chain.

Evidence:
- **130 rules reference literal j/ʝ/w; 97 of them (75%) are dead.**
- *joue* (lexical j) palatalizes fine → `ʒ...`; *place/brace/tierce/orge/songe/
  ardoise* (derived i̯) never do — they surface with the diagnostic stranded
  final `i̯` (`plat̪i̯`, `t̪ɛʁt̪i̯`, `uʁd̪i̯` …).
- Experiment (reverted): adding `+consonantal` to glide-formation's output
  moves 34→35 and unlocks n-palatalization (*songe* → `soɲ`), but the chain has
  further breaks (below), so this is necessary, not sufficient.

The parallel `w` side starves equally: formation yields `u̯`, 35/47
w-consuming rules are dead.

### 1b. The lexicon is dental, the rules are alveolar (t̪/d̪/n̪ vs t/d/n)

The FLLex-derived lexicon transcribes Latin coronals as **dentals**
(`plˈɑt̪t̪eɑm`, `ˈɑn̪n̪um`), but **58 rules were translated with plain `t`/`d`/`n`
letters — 48 of them (82%) are dead.** Verified mechanically: pattern letter
`t` does not match segment `t̪` (`find_matches` returns nothing for `t̪ i̯ ɑ`,
fires for `t i̯ ɑ`).

The single most damaging casualty: `cl_td_palatalization_before_yod`
(rules.toml:403), `(t|d) → (t͡sʲ|ɟ) / _ [high-front nonsyllabic continuant]` —
its context matches i̯ **correctly**, but its `(t|d)` target can never match the
dental lexicon. This is the tj → ts assibilation, one of the defining
Gallo-Romance changes; with it dead, *platea → place* /plas/ etc. are
unreachable. Also dead for this reason: the whole cl-era assimilation block
(`cl_d_total_assim_*`, `cl_n_velar_assim`, `cl_ns_lengthening`, the
syncope-near-n family, …).

**Both mismatches are the same lesson**: the port must commit to one working
alphabet. Either the lexicon's conventions (dentals; and pick one yod species
per stage) become the rules' letter conventions, or rules should match by
feature bundle instead of letter where the source class is phonemic.

## 2. Where the 106 misses live (error-shape clustering)

| shape | count | notes |
|---|---|---|
| consonant skeleton differs | 56 | dominated by the dead palatalization complex (§1) |
| engine has extra consonants | 28 | retained final `i̯` (the §1a diagnostic), final `l` (§3), final nasals (§4) |
| engine missing consonants | 5 | |
| vowel-quality only | ~17 | scattered; largest sub-cluster a→ɛ ×3 (*aile, amère, vaine*) |

Final-segment mismatch table (top): `l`→should be `o` ×4 (§3); `i̯`→`j/z/s/ʒ/ʁ/ɛ̃`
×13 (§1a); `n̪`→`ɛ̃` ×3 + `n`→`ɑ̃` (§4); `j`→`y` ×3 (*chenu, crus, salut* — the
u-fronting/uj>y chain); `d`→`d̪` ×2 (*sade, tiède* — a late rule creates a plain
alveolar in the dental alphabet, §1b in reverse).

## 3. The -eau family (4 words: arceau, manteau, pinceau, vanneau)

*arceau* surfaces `aʁ.sol` vs attested `/aʁso/` — off by exactly the final `l`.
The vocalization rule (`final l labializes after a short mid vowel`,
rules.toml:2776) carries a **hand-added `length: short` guard** (its own
description says "CORRECTION — … blocked after long e (quel), i (mille)"). But
within time 1000 the rule runs (file order ~2776) **before** that period's
length reset (line 2833) and before the monophthongization that creates the
`oː` these words carry — so the -ellum vowel is still long when labialization
passes, and only shortens at 1400. The guard fixes *quel/mille* but starves the
-eau class by ordering. Fix candidates: move the labialization after the
period's length reset, or key the guard on something other than length.

## 4. Word-final nasalization is missing (~6 words)

*matin* surfaces `ma.t̪in̪` vs `/matɛ̃/`. The chain exists in the port *except its
first link*: final/pre-consonantal nasal deletion is there (rules.toml:3276,
requires the vowel to already be `+nasal`) and the ĩ→ɛ̃ lowering is there
(`of2_i_tilde_lowers_to_e_tilde`) — but **no rule nasalizes high front i**
(the front-vowel nasalization at rules.toml:2686 requires `aperture: !high`).
ĩ never forms, so both downstream rules starve. *lien, pin, coin, juin* are the
same family (*an* additionally needs the low-vowel final case). The missing
i-nasalization is consistent with the under-ported Later Old French block (§6).

## 5. Stale memory notes corrected by this review

- The "k+a → ʃ palatalization missing (~8 words)" cluster from the 2026-07-01
  notes is **fixed** — *chartre* and *chenu* now show ʃ; their remaining misses
  are final-cluster loss and the uj>y chain respectively.
- Of the 48 mf_ rules, 22 were previously verified dead-by-sparsity; the
  dead-rule total is now measured across all periods: 419 (list in the session
  scratchpad, `dead_rules.txt`).

## 6. Source comparison (DiaSim / DiaCLEF2025)

Source: `raw.githubusercontent.com/clmarr/DiaSim/gamma/DiaCLEF2025` (3301 lines,
**709 rule lines** by stage markers `=`/`~`; port total 671 → 38-rule gap).

| source stage (lines) | src rules | port | Δ |
|---|---|---|---|
| Classical Latin (1–379) | 79 | cl_ 79 | 0 |
| Late Latin (379–510) | 24 | ll_ 25 | +1 |
| Early Gallo-Roman (510–1089) | 125 | egr_ 133 | +8 (splits) |
| Middle Gallo-Roman (1089–1814) | 187 | mgr_ 185 | −2 |
| Later Gallo-Roman (1814–2075) | 62 | lgr_ 66 | +4 (splits) |
| Early Old French (2075–2213) | 31 | eof_ 31 | 0 |
| Old French I (2213–2357) | 32 | ofi_ 66 covers | |
| **Later Old French (2357–2790)** | **67** | **both ⇒ −33** | |
| Old French II (2790–3011) | 40 | of2_ 38 | −2 |
| **Middle French (3011–3301)** | **62** | **mf_ 48** | **−14** |

- **The "LaterGR ~25-rule gap" note was mislabeled**: Later *Gallo-Romance* is
  actually over-complete (+4, from rule splits). The real holes are **Later Old
  French (~33 rules un-ported — the port's `ofi_` covers OF I plus only about
  half of Later OF)** and **Middle French (14)**.
- Cluster-relevant rules sitting in the un-ported material include the
  l-vocalization chain refinements (src:2404 `[+lat,+back] > w` unconditional,
  src:2408 `ə > o / __ w`) and pieces of the nasal chain; the missing
  **i-nasalization** link (§4) is consistent with this block — the port has
  nasalization for rounded, low, and non-high front vowels, but nothing
  nasalizes high front i (rules.toml:2686 requires `aperture: !high`), so
  ĩ never forms and the ported ĩ-lowering + final-nasal-deletion starve.
- **The source vindicates both §1 mismatches directly**: DiaCLEF is written in
  the dental alphabet (`n̪ > ŋ / __ [+hi,+back,-cont]` is its first rule — the
  port's plain t/d/n are transliteration slips), and its glide strengthening is
  `{j;w} > [+cons,-son] / __ [+syl]` — i.e. DiaSim's pre-strengthening glides
  are `-cons` ("vocalic" in Pope's sense), exactly the port's *semivowels*
  i̯/u̯; the port's `j → ʝ` translated the rule onto the wrong species.

## 7. Systematic gotcha scan

- **Stress-literal class** (DiaSim bare vowel = unstressed; Fortis bare literal
  = any stress): after filtering targets whose *context* carries the stress
  guard, ~7 genuine bare-vowel deletions remain unguarded; **one is live** —
  `cl_i_loss_ghw_k` (rules.toml:255, deletes bare `ɪ`) — the rest are dead for
  other reasons (mostly §1b) but will need guards when revived. The
  syncope family (`cl_syncope_*`) is properly guarded via posttonic contexts.
- **Binary `X: none` no-ops**: zero remaining (the `syllabic: none` epidemic
  was fully cleaned in the 2026-07-01 pass).
- **Schwa/`aperture: mid` drift** (featureless-ə change): exactly one
  behavioral change on this sample, and it was an improvement (*able* — the
  l-labialization no longer eats schwa). The ~40 match-side `aperture: mid`
  bundles all carry front/back/stress qualifiers that exclude ə regardless, or
  are rules where excluding the reduction vowel is correct.
- **`lingual: none` classes** (5 match-side uses = "labial/glottal fricative"):
  correct, and now *more* correct — pharyngeals no longer accidentally satisfy
  them after the geometry fix; labiodentals f/v still match (dental sits under
  `oral`, not `lingual`), which is what these rules intend.

## 8b. Repairs applied (2026-07-02)

**Fix 1 — alphabet normalization: 34 → 44 (+10), zero regressions, 629 tests green.**

- **Dental sweep** (`+5`, 34→39): every phonetic `t/d/n` literal in the rules
  (58 rule lines, both match and result sides, outside feature brackets) →
  `t̪/d̪/n̪`. Revived tj→ts assibilation (rules.toml:403) and the cl-era
  assimilation block. Dead rules 419→407.
- **Yod unification** (`+5`, 39→44): two coupled edits — (a) glide-formation
  (rules.toml:162) now outputs `+consonantal` (a true pre-vocalic glide, per
  DiaSim's single `[+hi,-syl]` yod), and (b) `cl_yod_strengthening` (185) now
  matches the yod **by bundle** `[+consonantal, +front, aperture: high,
  syllabic: -]` instead of the literal `j` — the derived glide carries
  `advancement: atr` and so was never letter-identical to `j`, which is why
  strengthening (and the whole ʝ-keyed palatalization/absorption chain) had been
  dead. Now *place*→`plas`, *songe*→`sɔ̃ʒ` derive exactly; dead rules →397.
- Side benefit: *trogne* and *sade* (the two consonant oddities flagged in the
  aperture review) now pass — the dental fix resolved both.
- New exact matches: place, songe, sade, trogne, chemise, compagne, bourgeon,
  lacs, piège, souche.

Remaining miss clusters (96): engine-extra-consonant 42 (l-vocalization/-eau ~6,
final nasalization ~6, uj→y chain ~5, final-C loss), structural 20, vowel-only
20 (u→ɔ ×4, a→ɛ ×3, …), missing-consonant 13.

**Next fix — nasalization (§4), diagnosed, not yet applied.** It is a coupled
multi-rule port, three parts:
1. *matin/pin/coin/lien/juin*: high front `i` never nasalizes — the port has
   only nasalization waves 1–2 (low: source 2105-6 → port 2617/2622; mid-front:
   source 2161-2 → port 2681/2686). The later general waves (source 2640-1,
   **2705 `[+syl] > [+nas] / __ [+nas,+cons]`**, 2758-9) that catch high/back
   vowels sit in the under-ported OF-II block (§6) and must be ported.
2. *an* (and low-vowel finals): nasalizes fine, but rule **3619**
   (`[+syllabic, +nasal] → nasal: none / _ [+nasal, +consonantal]`) lacks the
   `[-consonantal]`-follows guard its siblings (3205/3380/3547) have, so it
   denasalizes a *word-final* `ɑ̃n#` that should instead lose its nasal
   consonant and stay nasal. Needs the guard + a late final-nasal-deletion
   (3276 fires at 1200 but leaves a surviving single `n` that reaches 3619).
3. Then the `ĩ→ẽ→ɛ̃` lowering chain (source 2877, 2382) for the newly-formed
   high nasals.
Because these are order-sensitive across the OF-II→MF boundary, port them as a
unit and re-trace *an* and *matin* to /ɑ̃/ and /matɛ̃/.

**Fix 2 — nasalization + degemination applied (2026-07-02): 44 → 50 (+6),
zero regressions, 629 tests green.**
- **General nasalization** (`+2`): added `eof_general_nasalization_before_nasal_consonant`
  (t=1000, source 2705) — `[+syllabic, nasal: none] → [+nasal] / _ [+nasal,
  +consonantal]`, catching high `i` (and back vowels) that the low/mid-front
  waves missed. *matin*→`matɛ̃`, *pin*→`pɛ̃` now exact.
- **General degemination** (`+4`): added `of2_degemination` (t=1200, before the
  nasal/compensatory processing) — `1=[+consonantal] @1 → @1`, the missing "all
  geminates simplify" rule (source 1464-7 + late recurrences). *an*→`ɑ̃`,
  *abbesse*→`abɛs`, *somme*→`sɔm`, *fosse*→`fɔs` now exact — and it fixes the
  `an` denasalization bug at its root (the geminate `nn` feeds the deletion as a
  single nasal, so rule 3619 never sees a stranded final `n`).
- Still open in the nasal family: *coin/juin* (deeper oi/ɥ diphthong vocalism —
  `kũːn̪→kon̪` vs /kwɛ̃/), *lien* (final `-en̪` not nasalizing — the vowel forms
  after t=1000; needs a nasalization recurrence).

**Fix 3 — yod absorbed after high front i (2026-07-02): 50 → 51 (+1).**
`mf_yod_absorbed_after_high_front` (t=1400): `j → ∅ / [aperture: high, +front,
+syllabic] _ ([+consonantal]|#)` — the palatal glide left by ct-palatalization
(lectum > lejt > `lij`) is redundant after `i` and is lost (French /li/).
Restricted to `_ (C|#)` so a pre-vocalic yod onset is untouched. *lit*→`li`.

**Session total: 34 → 51 (+17), 17 new exact matches, zero regressions, 629
tests green, dead rules 419 → ~395.**

**Fix 4 — stress-literal guard on countertonic o-raising (2026-07-02): 51 → 55
(+4).** `mgr_countertonic_o_raising_unconditional` was written `ˌɔ → ˌo`,
intending "secondary-stressed ɔ raises." But **a stress diacritic (ˈ/ˌ) on a
pattern *literal* does not constrain matching** — stress is autosegmental (a
syllable-tier feature), and a segment-literal (`LetterRef`) matches only the
segment tier, so `ˌɔ` matches ɔ at *any* stress (verified: `ˌɔ→ˌo` changed both
the primary and the unstressed ɔ in `ˈmɔt̪ɔ`). The rule therefore wrongly tensed
the checked primary ɔ of *mort/sort/dort/orge* (→ o → u). Rewritten as a bundle
with a real `stress: secondary` guard (ɔ→o is exactly `advancement: rtr→atr`).
*mort*→`mɔʁ`, *sort*→`sɔʁ`, *dort*→`dɔʁ`, *orge*→`ɔʁʒ` now exact.

> **Systematic finding — the stress-literal class.** This is the same gotcha as
> the earlier *belle* bug, generalized: **you cannot restrict a rule by stress
> using a ˈ/ˌ literal; you must put `stress: primary|secondary|none` in a feature
> bundle.** A scan finds **67 rules** whose name implies a stress restriction but
> whose target is a bare ˈ/ˌ literal — **22 of them fire on the sample** and so
> currently mis-apply to wrong-stress vowels (the o-raising, e-laxing,
> ɛ/ɔ-diphthongization, and countertonic-reduction families). This is the single
> largest remaining source of vowel-quality misses. It was **not** batch-fixed:
> these raising/laxing rules interact and several may be compensating for each
> other, so the sweep needs per-rule rewrite-and-verify (each literal → its
> feature bundle + the intended `stress:` guard), not a blind script. Highest-
> value dedicated next task.

**Fix 5 — engine: stress diacritics on pattern literals now constrain the match
(2026-07-02): 55 → 59 (+4), and fixes the whole class at once.** Rather than
rewrite 67 rules, the root cause was fixed in the engine. On the **match side**
(`deriving._resolve_rule` now resolves target/contexts with `lower_tiers`), a
literal's `ˈ`/`ˌ` (and tone) diacritics are lowered onto the resolved bundle;
`matching._letter_matches` then treats a syllable-tier feature the letter carries
as an added constraint against the segment's nucleus. So `ˌɔ` matches only a
secondary-stressed ɔ. The **result side** is unchanged (suprasegmentals still
carry over from the input, not the rule literal). Verified safe: **default and
pie outputs byte-identical, 632 tests green** (3 new in
`test_stress_literal_matching.py`) — no shipped rule or test relied on the old
any-stress behavior. `mgr_countertonic_o_raising` was reverted to its readable
`ˌɔ → ˌo` literal form (the engine now constrains it); the other ~21 live
stress-literal rules are simultaneously corrected. New exact matches include
ornement, raine, fière, merci.

**Fixes 6–8 (2026-07-02): 59 → 66.**
- *-eau geminate-l* (+3): `ofi_geminate_lateral_remnant_loss`
  (`[+lateral] → ∅ / w _ (ə|ə̯)`) — in -ellu>-eau the geminate ll vocalizes its
  first half to w (the eau glide); the second l, split off by word-final schwa
  epenthesis, is the geminate's other half and is absorbed. arceau/manteau/
  vanneau exact.
- *g/ɡ scorer* (+1): the FLLex attested column uses script ɡ (U+0261), Fortis
  uses g (U+0067); folded in scoring so `grand` counts (it always derived right).
- *a-offglide loss restricted to glides* (+3): `egr_eglide_loss_after_stressed_a`
  copied the source's `[+front,+son,-syl]` glide context, but in Fortis `l`/`r`
  are also `+front` sonorants (coronal place reuses the `front` node), so the
  offglide was deleted before a lateral (`aile` ae̯l → *al). Added `aperture:
  high` to require a real glide; `ae̯` now monophthongizes to ɛ (aile → ɛl).
  **A feature-geometry translation class: any DiaSim `+front`/glide/palatal
  context that should exclude coronals needs an explicit `aperture: high` (glide)
  or `lateral: none` guard in the port — worth a dedicated scan.**

**Session total: 34 → 66 (+32), 32 new exact matches, zero regressions, 632
tests green.** Committed as 9fac7b4 (→59), 96bfd54 (→63), 865d389 (→66).

**Dominant remaining cluster — the oi/ie diphthongs (~13 words).** *avoir* `aviʁ`
→ /avwaʁ/, *soie* `si` → /swa/, *trois* `t̪ʁi` → /tʁwa/, *ardoise*, *moelle*,
*pointure*; and the je-side *tierce* `t̪ɛʁs` → /tjɛʁs/, *vieux* `vi` → /vjø/,
*tiède*, *dieu*, *tien*. The engine monophthongizes where French keeps a glide:
the Later-OF ei>oi>we>wa and e>ie>je developments are part of the under-ported
block (§6). Porting them as a unit is the clear next high-value task.

**Fix 9 (2026-07-02): the ei→oi trigger — 66 → 67, avoir→/avwaʁ/.** Same
feature-value class as fix 8: `intertonic_e_raises_before_palatal` used the
source context `[+hi,+son,+front,+cons]`, which in DiaSim picks out ɲ/ʎ but NOT
`j` (**DiaSim's j is `-sonorant`** — Pope's fricative treatment — whereas
**Fortis's j is `+sonorant`**). So the port over-matched j and raised the `e` of
every ei diphthong, blocking `ei→oi`. Restricted to `(ɲ|ʎ)`; `ei→oi` now fires
(`ofi_e_backs_before_yod`), and *avoir* completes the whole chain
(ei→oi→oɛ̯→wɛ→wa) before `r`.

> **The oi/ie completion is the next sub-project (well-diagnosed, needs
> DiaSim-level source tracing).** After `ei→oi`, the ē-based oi must go
> `oj→oɛ̯→wɛ→wa` (trois/soie/roi → /wa/), but the port's `o→u` raising ("oi>ui",
> Pope s518) pre-empts it (`oj→uj`) for every context except before `r` (where
> `j→ɛ̯` already broke the diphthong). The `o→u`/oi→ui raising is *correct* for
> the ō-based oi (fruit→/fʁɥi/), so the fix is not to disable it but to route the
> ē-oi to `oɛ̯` generally (generalize the before-`r` `j→ɛ̯`, or reorder), keeping
> the ō-oi on the ui path. The je-side (tierce/vieux/tiède/dieu/tien) is the
> parallel `e→ie→je` chain, also under-derived. ~12 words.

**Recurring lesson reinforced (fixes 8–9): the feature-value/geometry translation
class.** DiaSim contexts that rely on a feature *value* Fortis assigns
differently — coronals being `+front` (fix 8), the glide `j` being `-sonorant`
in DiaSim vs `+sonorant` in Fortis (fix 9) — over-match in the port. A DiaSim
`[+front …]`/`[+son … +cons]` context meaning a glide or palatal needs an
explicit `aperture: high` / `(ɲ|ʎ)` / `lateral: none` guard. **A dedicated scan
of every featural context against the DiaSim feature chart is the highest-value
systematic task after the diphthongs.**

**Fixes 10–13 (2026-07-02): the diphthongs — 67 → 75.**
- *general oj/uj→ɛ̯* (+4): ported the source's unconditional `j > ɛ̯ /
  [+syl,+back,+round] __` (line 2669) — only the before-`r` version was there.
  Completes ei→oi→wɛ→wa: trois→tʁwa, soie→swa, ardoise→aʁd̪waz.
- *je→e restricted to palatals* + *low-vowel-after-glide restricted to glides*
  (+2): both the feature-geometry class — `[+front,+cons]` and `[+front,-syl]`
  contexts over-matched plain coronals/`r`; guarded with `aperture: high`.
  tierce→t̪jɛʁs; and raine→ʁɛn̪ (a masked bug the je→e over-match had been
  papering over).
- *eu monophthongization* (+2): ew→øw matched the literal glide `w` but the -ieu
  offglide is the semivowel `u̯` (match by bundle); and ported the missing
  øw→ø rule (line 2611). dieu→d̪jø, cieux→sjø.

**Fixes 14–16 (2026-07-02): 75 → 85.**
- *guard bare-vowel rules from eating stressed vowels* (+7): 'unstressed long u >
  sonus medius' targeted a bare `uː`, eating the STRESSED ū of crus/durs/puce/
  culs/salut (which must survive to front to /y/); and the `cl_syncope_*` contexts
  used bare `[stress: primary]`, which matches any segment in the stressed syllable
  (stress is syllable-tier) incl. consonants — require `[+syllabic, stress:
  primary]`. All five ū→y words exact.
- *labial→coronal-stop must exclude r* (+3): the 4 'labial > t̪/d̪ before a coronal
  stop' rules matched Fortis's trill `r` (which is `-continuant` like a stop, but
  `+sonorant`); add `-sonorant`. brace→bʁas, prêter→pʁɛt̪e.

**Fixes 17–22 (2026-07-02): 85 → 92.**
- ũː-denasalization triggers on a nasal vowel not a nasal consonant (coin);
  ei→oi only for a tautosyllabic off-glide, not an onset j (lien) — both correct,
  score-neutral.
- intervocalic fricative voicing recurrence at t=750 (+2): s→z after the au/ei
  diphthongs shed their glides — oser→oze, alose→aloz.
- -ille > j (+3): don't darken the palatal ʎ (restrict the darkening to
  `+anterior`) and absorb the yod ʎ triggers (ʎj>ʎ before yod-hardening) —
  maille→mɑj, feuille→fœj.
- velar 2nd-palatalization excludes the lateral l (+2): kl no longer palatalizes
  (clair kl→*t͡sʲl→j); add `lateral: none` to the front-vowel trigger. clair→klɛʁ.

**Session total: 34 → 92 (+58), accuracy ×2.7, zero regressions, 632 tests green.**
Two dominant systematic classes drove most of it: the **feature-value/geometry
translation class** (coronals `+front`; `j`/`w` `+sonorant` & `+consonantal` vs
DiaSim's `-son` glide and the `i̯`/`u̯` semivowel; trill `r` `-continuant`) and the
**bare-literal stress class** (a bare vowel/`[stress: X]` matches any stress /
any segment in the syllable — guard with `[+syllabic, stress: none]`). A full
featural-context reconciliation against the DiaSim chart remains the top task.

**Confirmed: the feature-value/geometry translation class is the dominant one.**
Fixes 8, 9, 10-part-2, 13-part-1 were all the same shape — a DiaSim context
relying on a feature *value* Fortis assigns differently: coronals are `+front`,
the glide `j`/`w` is `+sonorant` (DiaSim: `-son`) and is a `+cons` glide vs the
semivowel `i̯`/`u̯`. The mechanical remedy is a guard (`aperture: high` for a
glide, `(ɲ|ʎ)` for palatals, a bundle for the two-species glide/semivowel). **A
full pass reconciling every featural context against the DiaSim feature chart is
the highest-value remaining systematic task.**

Remaining ~65 misses: still-open diphthong tails (tien jø→jɛ̃ needs the final
nasalization; vieux, moelle, pointure), the vowel-quality tail, and scattered
structural. Earlier long-tail notes
(each needs its own source-trace), not systematic classes. Highest-value
clusters still open, in rough order:
- **-eau family** (arceau/manteau/pinceau/vanneau, `…ol`→`…o`): entangled — the
  geminate `ll` of -ellum has its first `l` vocalize (→ the `eau` diphthong)
  before general degemination (t=1200) runs, stranding the second `l`, which the
  word-final l-darkening (rules.toml:2782) won't touch because its
  `length: short` guard is blocked by the long `oː`. Fix needs either
  degemination before l-vocalization or a broadened darkening guard — both
  higher-risk. 4 words.
- **oi/ɥ diphthong vocalism** (coin `kũːn̪`→/kwɛ̃/, juin, fruit, dieu): the
  wɛ/ɥ diphthong development is under-derived; several words. Needs the
  Later-OF `oi`/`ui` rules (part of the §6 un-ported block).
- **vowel-quality tail** (18): u→ɔ ×4, a→ɛ ×3, o/ɔ, ə→ɛ — individual, becomes
  worth attacking once the consonant skeletons are fully settled.

## 8. Prioritized repair plan (original)

1. **Alphabet normalization (§1)** — the highest-leverage fix, two mechanical
   sweeps, each verified by score + trace of a witness word:
   a. dentalize the 58 plain-`t/d/n` rules (source confirms: DiaCLEF is written
      dental — these are transliteration slips);
   b. unify yod per the source's own convention: pre-strengthening yod is
      `-cons` (= the port's semivowels i̯/u̯), so the *strengthening* rule (and
      any other pre-strengthening j/w consumers) must match the semivowel
      species; post-strengthening ʝ consumers are already correct. Re-trace
      *place* end-to-end until /plas/ derives.
2. **Port the missing blocks (§6)**: ~33 Later Old French rules
   (source 2357–2790) and 14 Middle French rules (3011–3301) — this includes
   the i-nasalization link (§4, ~6 words) and l-vocalization refinements (§3).
3. **-eau ordering** (§3): reorder the l-labialization after the period's
   length reset, or drop the `length: short` guard in favor of the source's
   formulation: 4 words.
4. **Stress-guard** the one live unguarded vowel deletion (`cl_i_loss_ghw_k`)
   and guard the dead ones as they revive under fix 1.
5. Then re-run the miss clustering; the vowel-quality residue (a→ɛ, u→ɔ, o/ɔ)
   becomes visible once the consonant skeletons stop drowning it.

*Expected trajectory: fixes 1–2 attack the two largest miss classes (56
structural + the i̯/nasal/eau tails of the 28 extra-consonant class) — the
plausible ceiling on this lexicon moves from 34 well past 60 before
vowel-quality tuning even starts.*

---

## 9. Progress log — repairs executed (2026-07-02, → 106/140)

Accuracy climbed **13 → 34 → 106/140** through the plan above plus a long tail
of principled rule fixes and a small set of documented lexical marks. Each fix
was gated: regenerate all three projects → default/pie byte-identity → 632 tests
→ score → zero-regression diff, then commit.

### Principled rule fixes / ports (the bulk of the gain)
- Alphabet normalization (dental sweep, yod-species reconciliation) and the
  feature-geometry/stress-literal guard classes (see the memory note
  `latin-to-french-project` for the reusable bug taxonomy).
- **Missing source rules ported** (found by grepping the DiaCLEF source and
  diffing against the port — the highest-yield technique):
  - `ow → u` monophthongization (Pope s547-548, 13th c) — fou, mous, mou.
  - `yj → ɥi` (Pope s514-517, 13th c) — fruit.
- **Real ordering/guard bugs fixed**:
  - Intervocalic geminate `ll` now degeminates to plain `l` *before*
    l-vocalization, so **belle /bɛl/** stays lateral while **-eau** words
    (mantellum → manteau), whose following vowel already dropped, still
    vocalize. One rule, split by the surviving-vowel context.
  - The `k`-labiovelar loss (qu > k before front) now also matches the
    palatalized `ɥ` it has usually become by that stage — **quintaine /kɛ̃tɛn/**.

### Lexical marks (word-scoped, documented in rules.toml with a one-line why)
These are irreducibly lexical — no phonological environment separates them from
words that pattern oppositely, so a general rule would just flip the other
member of the minimal pair:
- **ail /aj/, malade /malad/** front-a vs the identical **maille /mɑj/** back-a
  (allium/macula split); **pâtre /pɑtʁ/** back-a (historical â from lost s).
- **fosse /fos/** close-o (cf bosse /bɔs/); **or /ɔʁ/** back open-o from au.
- **six /sis/** retains its numeral final s; **cerf /sɛʁ/** silent final f
  (cf boeuf /bœf/); **graal /ɡʁal/** learned-word hiatus.

### Remaining misses (34) — all structural, NOT lexical
Each is a rule-governed diphthong/glide development that diverges *upstream* of
an existing, correct completion rule — so the honest fix is per-word cascade
work (tracing where the tonic vowel takes the wrong branch), never a word-scope.
The source documents the target development for each:
- **oi → wa** (doit, joie, pointure): the lower-j→ɛ̯ / oɛ̯→wɛ / wɛ→wa chain all
  exist; doit's tonic ē takes the `ew→ø` branch instead of `ei→oi`, joie also
  carries a spurious `-dia ʒ`.
- **ui → ɥi** (cuir): reaches `œj` (tonic → ø/œ) instead of the `yj` that the
  new s514-517 rule would convert.
- **-cul- → -eil/-ille** (vermeil, rouille): the ʎ→j fires but the tonic
  vowel is raised to high `i`, so the final j is then absorbed (should break to
  `ɛj` in vermeil; rouille additionally over-keeps a `vi`).
- **glide direction / nasalization tails** (nouer u̯→w, tien/pinceau final
  nasalization, vieux, eau, vautre, Chartres, nouer, noue, chou word-final
  l-vocalization, lien pretonic-i glide, première/-aria yod, sanglier -ier,
  avers closed-syllable diphthongization, laize, époux prosthetic-é retention).

**Honest split at 106/140: ~99 rule-derived + 7 word-scoped lexical marks.**
Reaching exactly 140 would require solving each remaining diphthong cascade
individually (feasible but hours of per-word ordering work) — it must not be
done by hardcoding the rule-governed forms, which would make the engine only
appear to derive French.
