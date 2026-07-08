# Feature-System Review — robustness & structure audit

_2026-07-02. A structural audit of `projects/default/` (features.toml, letters.csv,
diacritics.toml, sonorities.toml) in the spirit of the aperture/advancement scalar
migrations: find the remaining encodings that invite the same bug classes, and the
places where the declared geometry and the data disagree._

Status: **implemented** (2026-07-02), with one amendment: C4 was replaced by
**C4′ — featureless schwa** (see below; ə owns quality-absence instead of
carrying explicit neutrals). Gate results: default and pie_to_germanic outputs
**byte-identical** throughout; latin_to_french changed on exactly one word
(*able*, a principled fix — the "final l labializes after a short mid vowel"
rule no longer over-applies to schwa) plus one resyllabified trace line
(*cervum* `ker.wum` → `ke.rwum`, glides now outranking rhotics); 629 tests
(626 + 3 new validator tests); latin score 34/140 held.

---

## What already holds

The three scalar migrations (advancement, the laryngeal trio, aperture) eliminated
two bug classes by construction: contradictory poles (`+hi +lo`, ATR+RTR) and the
dangling empty parent node (`aperture` with no child). The vowel grid is now fully
explicit in three dimensions — backness (privative front/back), aperture (scalar),
advancement (scalar) — with one exception (§A5).

## A. Concrete defects found

### A1. 41 parent-child geometry violations in letters.csv

Features set on a segment whose declared parent is empty. Three distinct causes:

| Segments            | Violation                                                  | Diagnosis                                                                                                                                                                                                                 |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ħ ʕ ʜ ʢ ʡ (+ ʡ͡ʜ ʡ͜ʢ) | `back`, `aperture`, `advancement` set, **`lingual` empty** | Pharyngeals/epiglottals use tongue-root features — all declared under `lingual` — without the parent. The tree says "tongue", the letters say "no tongue". They should carry `+lingual` (the root is part of the tongue). |
| ɱ f v ʋ ⱱ           | `dental` set, `lingual` empty                              | **Structural misfit, not a data bug**: `dental` means "at the teeth" (a passive articulator) but is declared under `lingual`. Labiodentals are labial+dental with no tongue involvement — see §C1.                        |
| k͡ʘ g͡ʘ q͡ʘ ɢ͡ʘ ŋ͡ʘ ɴ͡ʘ   | `back`+`aperture` set, `lingual` empty                     | Plain data bug — the bilabial-click series forgot `+lingual` for its velar/uvular rear closure.                                                                                                                           |

Not cosmetic: latin has a live natural class `[+continuant, +consonantal,
lingual: none]` ("s voices before a labial/glottal fricative" — rules.toml:2453,
2822, 3060, 3421) that **pharyngeals accidentally satisfy** because of the
violation. (Harmless today only because the latin lexicon contains none.)

### A2. Live dangling-child bug: pie delabialization

`pie_to_germanic/rules.toml:115` turns kʷ → k with `→ [rnd: none]`: it deletes
`rounded` but leaves the parent `labial` node dangling. The derived bundle — "a k
that still carries a labial node" — matches **no letter exactly** and renders as k
only because closest-match rendering is forgiving. Same family as the old empty
`aperture` node.

### A3. Data hygiene

- **ɠ** (velar implosive) carries `front=+` — velars aren't front; sibling ʄ
  (palatal implosive) legitimately is. Looks like a copy-paste slip.
- One symbol cell is literally `'q͡ǂ '` **with a trailing space** — unmatched by any
  typed input, and a silent near-duplicate of a correct-looking symbol.

### A4. Sonority classes contradict the vowel/semivowel/glide doctrine

`sonorities.toml` defines `glide = { consonantal: -, sonorant: + }` — that is the
**semivowel** class (i̯, u̯). True glides j/w are `+consonantal` (per the documented
three-way split), fall through to the next matching predicate — `rhotic` — and so
**j ranks exactly as sonorous as r** (level 5, below semivowels at 6).
Syllabification is sonority-driven wherever the time-keyed onset/coda patterns
don't apply, so a /rj/ or /jr/ cluster's parse is currently arbitrary.

### A5. ə is the last "neutral by absence" vowel

Every vowel carries an explicit `advancement` — i `1`, ɪ `-1`, e `1`, ɛ `-1`, ɘ `1`,
ɜ `-1` … — **except ə, whose advancement is absent** while the scalar declares
`0 = neutral`. No surviving rule matches or writes `advancement: none` (the only
writers were in the deleted post-Germanic tail), so the fix window was open.

**Resolution (amended): the hazard was never absence itself — it was *unowned*
absence.** Pre-migration, "no aperture" was ambiguously shared by every mid vowel
and consonant; a bundle landing there matched nothing exactly. The adopted fix
runs the other way from the original C4: instead of giving ə explicit neutrals,
ə was made the **featureless vowel** that *owns* quality-absence outright — a
class of one, exactly matchable. See C4′.

### A6. Doc/data contradictions in default_system.md

- The vowel-space table shows `a • ɶ` in the **central** column; letters.csv has
  both as `+front`. (The front/RTR/low cell shows "-", which is what should read
  `a • ɶ`.)
- The text cites `[place: none]` as a parent-clearing example — no `place` node
  exists in the geometry.

## B. The design questions

### B1. Should coronal/palatal consonants carry ATR? — Recommendation: no

- Consonantal `advancement: rtr` on uvulars/pharyngeals is **class-defining and
  load-bearing**: it _is_ the guttural class (pie's laryngeal rules match
  `[+cons, advancement: rtr]` seven times). It is also phonetically real — those
  places retract the tongue root.
- Palatals need nothing extra to be a class: `+front, aperture: high` with no
  anterior/posterior already picks out exactly c ç ɟ ʝ ɲ ʎ j ɥ ʄ ɕ ʑ t͡ɕ d͡ʑ c͡ç ɟ͡ʝ
  (all 15 audited, uniformly advancement-free).
- Every feature added to a letter class creates a **clearing burden** on every rule
  that destroys the class: if palatals were `atr`, every depalatalization (latin
  797, 3252, …) would have to also clear `advancement` — re-introducing the
  dangling-value family the scalar migrations eliminated, for no rule that
  currently needs it.
- The criterion, stated once: **a scalar is specified where it contrasts or defines
  a class, and absent where the dimension is inapplicable.** Vowels contrast
  tense/lax → all specified. Gutturals are defined by rtr → specified. Palatals and
  coronals don't contrast root position → absent.
- The rtr "double duty" (lax vowels and gutturals share a value) is a _feature_:
  it's what makes Arabic-style emphatic lowering a one-line rtr spread. A project
  needing palatalization→ATR interactions can write them as rules (match
  `aperture: high, +front`, emit `advancement` onto the vowel) with no letter
  change.

### B2. Should backness become a scalar like aperture? — No, and it's the instructive counter-case

`front`+`back` genuinely co-occur 32 times in letters.csv: the clicks' double
articulation (coronal/palatal front closure + dorsal rear closure), velarized ɫ,
and PIE palatovelars (kʲ via the ʲ diacritic; the centumization rule
`[+cons, -son, +back, +front] → [front: none]` depends on it). Aperture qualified
for scalarization because `+hi +lo` was never legal; backness fails that test.
**Criterion: scalar iff the poles are mutually exclusive.**

Same verdict, for now, on the other unary pairs: `anterior`/`posterior`,
`rounded`/`compressed`, `tap`/`trill` never co-occur today, but no middle value
exists, no bug class bites (all `anterior: none` uses are match-side), and the
validator (§C6) covers the risk more cheaply than three migrations.

## C. Proposed changes

In dependency order. All except §C7 are expected byte-identical and use the
standard gate: regenerate all three projects, diff outputs, 626 tests, latin ≥ 34.

### C1. Move `dental` from `lingual` to `oral` (features.toml, one line)

```toml
# now:  lingual = { ..., children = ["apical", "retroflex", "dental", "front", "back", "aperture", "advancement"] }
# new:  oral    = { ..., children = ["labial", "lingual", "dental"] }   # dental = passive articulator
```

`dental` becomes "articulated at the teeth", combinable with the lips (f) or the
tongue (t̪). letters.csv is untouched (columns are flat). One latin rule (797,
depalatalization to a dental) relies on `+dental` auto-implying `lingual` and gets
an explicit `+lingual` added.

### C2. Add `+lingual` to pharyngeals/epiglottals and the ʘ-clicks (letters.csv, ~13 cells)

Fixes the §A1 rows. Expected byte-identical: latin's lexicon has no pharyngeals;
pie matches ħ via `advancement: rtr`, not via lingual-absence.

### C3. Data hygiene (letters.csv, 2 cells)

Remove ɠ's stray `front`; strip the trailing space from `q͡ǂ `.

### C4′. ə is the featureless vowel (letters.csv; replaces the original C4)

The original proposal (ə → `advancement: 0`) was replaced, at the user's
suggestion, by its dual: **ə carries no `oral` node at all** — no backness,
aperture, advancement, or rounding — the vowel counterpart of the placeless
glottals ʔ/h. Schwa is genuinely unique (the targetless reduction vowel) and
now *owns* quality-absence: `[+syllabic, aperture: none]` matches exactly ə,
and reduction-by-clearing (`[oral: none]`) lands on it as an exact hit.

Consequences, all deliberate:
- ə is **not** in the `aperture: mid` class — mid-vowel rules skip the
  reduction vowel by construction. (This immediately fixed an over-application:
  latin's "final l labializes after a short mid vowel" had been catching the
  schwa of *able*.)
- pie's "Elimination of */ə/" now matches it as `[+syll, aperture: none]` —
  simpler than the old central-mid circumlocution.
- The explicit-neutral policy stands for everything else: the criterion is
  refined to *absence is safe when a unique letter owns it*.

### C5. Fix pie delabialization (rules.toml:115, one token)

`[rnd: none]` → `[labial: none]` — clears the node and its children, so the
derived bundle is exactly the letter k. Expected byte-identical.

### C6. Load-time geometry validator (engine, ~30 lines + tests)

After parsing each letters.csv row, verify every set feature's declared parent
is also set; fail the load with a message naming the row and features. Also
reject duplicate symbols and whitespace-padded symbols. **Diacritic bundles are
deliberately exempt**: they are deltas onto a base segment, and merging implies
the missing ancestors (`ʲ` = `+front, aperture: high` needn't carry `lingual`).
Zero behavior change for valid data; the entire §A1/§A3 class becomes impossible
to reintroduce. Shipped **after** C1–C3 (the old data would have failed it).
Implemented in `loaders/letters.py` with 3 tests in `tests/loaders/test_letters.py`.

### C7. Sonority: a true-glide level (sonorities.toml) ⚠️

Rename the current level-6 class `semivowel`; insert above `rhotic` (final
levels: vowel 8, semivowel 7, glide 6, rhotic 5, …, stop 1):

```toml
glide = { level = 6, bundle = "consonantal: +, sonorant: +, continuant: +, aperture: !none, nasal: none, lateral: none" }
```

The defining property is *having* a tongue-body (`aperture`) place — any value,
hence `!none` rather than `high` (user's amendment): j/w pair with i/u, but a
pharyngeal ʕ̞ or uvular ʁ̞ approximant (the counterparts of ɑ and ʌ) is a glide
too, while the coronal/labial approximants ɹ, ʋ (no `aperture`) stay
rhotic-level. **The one change that can legitimately move syllable boundaries**
— outcome: default/pie byte-identical; latin shows a single resyllabified trace
line (*cervum* `ker.wum` → `ke.rwum`: rw is now a rising-sonority onset under
bare sonority+MOP), zero surface changes. Note latin_to_french declares a
nucleus-only `syllable_parts.toml` — it **never** applies onset/coda patterns
(the default's t=500 Latin-style onset grammar is overridden by the per-file
fallback), so it syllabifies by sonority+MOP throughout. The *cervum* parse is
bounded not by patterns but by the derivation itself: the next rule (w → ɣʷ)
makes the cluster fall in sonority and MOP splits it again. Persistent
sonorant+glide clusters (rj, lj, lw …) now parse as rising onsets in latin —
consistent with French phonotactics (/ʁjɛ̃/ *rien*, /lwa/ *loi*).

Related decision (user question): the top class stays `syllabic: +,
consonantal: -`, **not** bare `syllabic: +`. Nucleus-hood comes from the
`+syllabic` nucleus pattern in syllable_parts.toml, not from the scale — PIE's
r̩ l̩ n̩ m̩ are already nuclei, and a nucleus's own level is never consulted
(levels drive only the clusters *between* nuclei). Sonority is intrinsic to
the segment type; ranking r̩ with vowels would erase the fact that vowels make
better nuclei than syllabic sonorants.

### C8. Doc updates (default_system.md)

- Vowel table: `a • ɶ` move from the central to the front column.
- Replace the `[place: none]` phantom with a real node (`[lingual: none]`).
- Pharyngeal row of the natural-classes table gains `+lingual` (after C2).
- Write down the two criteria from §B: _scalar iff poles mutually exclusive_;
  _scalars explicit on the class that contrasts them, absent where inapplicable_
  — with backness and the guttural/ATR decision as the worked examples.

## D. Explicitly not proposed

- **ATR on palatals/coronals** (§B1) — documented instead.
- **Backness, anterior/posterior, rounded/compressed, tap/trill as scalars**
  (§B2) — the exclusivity criterion fails or the migration buys nothing the
  validator doesn't.
- **A `place`/`coronal` articulator node** — the doc already records the
  deliberate choice to reuse `front` for coronality; nothing in the audit
  contradicts it.
