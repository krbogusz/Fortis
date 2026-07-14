"""Build words.csv — the PIE→English gold lexicon — from the kaikki Wiktionary extracts.

The lexicon IS committed, but under its own licence: it is Wiktionary-derived and therefore
CC BY-SA 4.0 (share-alike), where the rest of the repo is PolyForm Noncommercial. See SOURCE.md.
Run this to regenerate it; the kaikki extracts it reads are not versioned (see CACHE below).

Stage two of two: `build_chains.py` walks the kaikki extracts into `chains.json`; this filters
and scores those chains into `words.csv`.

Three filters do the real work, and they are about honesty rather than coverage:

* Only rows whose PIE form is the true *preform* of the word are kept. Wiktionary links a
  lexeme to a PIE root-representative or an inflected cell, not necessarily to the ancestor of
  the citation form: it cites 3sg *bʰéreti against the PGmc infinitive *beraną, and no correct
  cascade turns one into the other. Verbs, affixes, bare roots and inflected-cell glosses are
  therefore dropped; nominative-singular nouns, numerals, pronouns and particles are kept.
* Attested IPA is normalised to what the inventory can segment (script ɡ, tie bars, the
  raising/lowering diacritics), and a form that still will not segment is left blank rather
  than guessed at — the engine scores a word at whichever checkpoints it has.
* A checkpoint the source cannot be trusted on is BLANKED, not made to condemn the whole row.
  A word with no modern reflex, or several of them, or an unsegmentable modern IPA, has an
  untrustworthy `final` — and a perfectly good Proto-Germanic form. Dropping it (as this once
  did) threw away more than half the Proto-Germanic gold to protect a column those rows were
  never going to be scored on. Only a row with no target at ANY checkpoint is dropped.
"""

import csv
import json
import os
import re
import sys
import unicodedata as ud
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, str(Path(__file__).parent))

from pie_ipa import (  # noqa: E402
    ACUTE,
    PieError,
    accent_first_nucleus,
    has_accent,
    to_ipa,
)

from fortis.analysis.accuracy import try_segment  # noqa: E402
from fortis.loaders.project import load_project  # noqa: E402

# The kaikki extracts and the intermediate chains.json. Big (~280 MB) and regenerable, so it
# is never committed — see SOURCE.md for how to populate it. Override with FORTIS_PIE_CACHE;
# the default is a .cache/ beside this project.
CACHE = Path(os.environ.get("FORTIS_PIE_CACHE") or Path(__file__).parent.parent / ".cache")
OUT = Path(__file__).parent.parent / "words.csv"

# Word classes whose Wiktionary PIE citation form is the preform of the attested word.
# Nouns, adjectives and numerals only. Pronouns, particles and the other function words are
# excluded even though their PIE forms look clean: they erode irregularly (the reflex of
# *óynos is the article "a", not the regular "one"), and their descendants trees carry
# spurious links (*wiHrós "man" → OE wer is listed as the ancestor of the homograph "were").
#
# Verbs are in, but only in the 3sg present, and only scored at Proto-Germanic: `build_chains`
# rewrites a verb chain into that one cell (PIE *bʰéreti → PGmc *biridi), because the two
# citation forms name different cells of the paradigm and nothing derives one from the other.
KEEP_POS = {"noun", "adj", "num", "verb"}

# Checkpoint times. The PIE→Proto-Germanic leg of the cascade runs to 160, so
# Proto-Germanic is read at 200.
PGMC, OE, ME = 200, 900, 1400
# The seed's time: the PIE form is the earliest attested form, and the earliest IS the input.
# At or before the first rule (the cascade opens at −2000), so the seed sees every rule.
SEED_TIME = -2000


def _bare(form: str) -> str:
    """*form* with its accents stripped, for testing what ending it has."""
    return ud.normalize("NFC", "".join(c for c in ud.normalize("NFD", form) if c != ACUTE))

# Preform corrections, keyed by the PROTO-GERMANIC headword.
#
# Keyed by the Germanic form, not the modern reflex, for three reasons. Most words in the lexicon
# no longer HAVE a modern reflex — they died before English — and keying by one made every one of
# them structurally impossible to correct. The modern key was also ambiguous: "lay" is the reflex
# of both *lagjaną and *laguz. And it is the Germanic form that carries the evidence, so the key
# now names the thing being read.
#
# Wiktionary's `inh` link records a PIE lemma, which is cited in the e-grade — but the Germanic
# word often continues the ZERO grade of the same root. The linked form is then not the preform,
# and no rule can bridge the two: *ǵéwstus can never yield *kustuz. Rather than let the row
# score as a permanent miss (or, worse, let it make a correct rule look broken — OE
# palatalisation dutifully palatalises the front vowel that *cost* should never have had), the
# input is replaced with the actual preform: the zero grade of the same root.
#
# The accent is not decoration. Verner's Law reads it, so it is set by the attested Germanic
# consonant: *mundiz has a VOICED d (Verner fired ⇒ the accent must follow the root), while
# *kunþiz keeps a voiceless þ (Verner did not fire ⇒ the accent sits on the root).
# The same table also carries STEM-CLASS corrections. Wiktionary cites the PIE lemma in one
# gender/stem class where Germanic continues another: *kʷékʷlos is masculine, but PGmc *hwehwlą
# is NEUTER, and a neuter *-om is what gives the attested nasal ending. That is the same
# wrong-preform problem as the ablaut, one level up in the morphology, and it has the same fix.
PREFORM_FIXES = {
    # ── ABLAUT: the attested VOWEL refutes the grade Wiktionary cites ────────────────────────
    "mundiz": "mn̥tís",     # *mundiz — zero grade of *men-; oxytone, so Verner voices *t > *d
    "kustuz": "ǵústus",     # *kustuz — zero grade of *ǵews-
    # NOT *kinþiz: its OE cynd (with i-mutated y) suggests a zero grade *ǵń̥h₁tis, but Wiktionary's
    # own Proto-Germanic is *kinþiz with an /i/ — which the e-grade *ǵénh₁tis gives directly, via
    # the raising of *e before a nasal. The inconsistency there is between Wiktionary's PGmc and
    # its OE, not between its PIE and its PGmc, so the input is left alone.

    # ── VERNER: the attested CONSONANT'S VOICING fixes the accent ────────────────────────────
    # A voiced fricative means Verner fired, so the accent followed the root (oxytone); a
    # voiceless one means it did not, so the accent sat on the root. The consonant is evidence
    # independent of our rules, which is what makes reading the accent off it legitimate.
    "dēdiz": "dʰeh₁tís",    # *dēdiz — voiced *ð; the long *ē keeps the e-grade *eh₁
    "stadiz": "sth₂tís",    # *stadiz — voiced *ð, and a SHORT *a: zero grade (cf. Gk stásis)
    "furduz": "pr̥tús",      # *furduz — voiced *ð, and *u from the zero-grade *r̥
    "laguz": "lokús",       # *laguz — a voiced *ɣ, so Verner fired and the accent is oxytone
    "kunþaz": "ǵń̥h₃tos",    # *kunþaz — root accent, so Verner leaves *þ voiceless
    "mōdēr": "meh₂tḗr",     # *mōdēr — VOICED *ð. The textbook pair: *bʰréh₂tēr keeps its voiceless
                            # *þ (*brōþēr) because it is root-accented, and *méh₂tēr does not.
    "fadiz": "potís",       # *fadiz — voiced *ð, so the cited barytone *pótis cannot be right
    "funsaz": "pń̥tstos",    # *funsaz — VOICELESS *s: Verner did NOT fire, so the cited oxytone
                            # *pn̥tstós is wrong and the accent belongs on the root
    "murþą": "mŕ̥tom",       # *murþą — voiceless *þ (root accent) AND a neuter *-ą; both wrong
    "agiþō": "h₂oḱéteh₂",   # *agiþō — the two consonants disagree, and that PLACES the accent:
                            # *ɣ is voiced (Verner fired ⇒ unstressed before it) but *þ is
                            # voiceless (it did not ⇒ stressed before it). Only a medial accent
                            # satisfies both. Feminine *-ō on top.
    "andō": "h₂enh₁téh₂",   # *andō — the *d is a hardened *ð, so Verner fired ⇒ oxytone; feminine
    "algiz": "h₁olḱís",     # *algiz — voiced *ɣ ⇒ oxytone, and the attested *a refutes the cited
                            # e-grade (PGmc *a is the regular reflex of PIE *o)

    # ── The Verner pass (2026-07-14) ─────────────────────────────────────────────────────────
    # Six words whose Germanic consonant flatly contradicts the accent the input carried. Four of
    # them (*braidaz, *sēdiz, *þrēduz, *hreubaz) had NO cited accent at all — they came in on the
    # initial-stress default, which is exactly the case that default was documented as not
    # settling. Two (*hulþaz, *munþaz) had a cited oxytone that the attested VOICELESS *þ refutes.
    #
    # In every case the reasoning runs the same way and it runs from the consonant, not from us:
    # Verner's Law is independently established, so a VOICED fricative proves it fired (the
    # preceding syllable was unaccented ⇒ oxytone) and a VOICELESS one proves it did not (that
    # syllable was accented ⇒ root accent). Nothing here is read off the derivation.
    "braidaz": "bʰroytós",  # *braidaz — VOICED *ð ⇒ Verner fired ⇒ oxytone
    "sēdiz": "seh₁tís",     # *sēdiz — VOICED *ð ⇒ oxytone. The same shape as *dēdiz : *dʰeh₁tís
                            # above, and it takes the same fix.
    "þrēduz": "treh₁tús",   # *þrēduz — VOICED *ð ⇒ oxytone; a u-stem, like *furduz : *pr̥tús
    "hreubaz": "krewpós",   # *hreubaz — VOICED *β ⇒ oxytone
    "hulþaz": "ḱĺ̥tos",      # *hulþaz — VOICELESS *þ ⇒ Verner did NOT fire ⇒ ROOT accent, against
                            # the cited oxytone *ḱl̥tós
    "munþaz": "mń̥tos",      # *munþaz 'mouth' — VOICELESS *þ ⇒ root accent, against the cited
                            # *mn̥tós. Set it beside *mundiz 'hand' : *mn̥tís above — the SAME root
                            # shape with the OPPOSITE accent, and it is the consonant that tells
                            # them apart: *mundiz has a voiced *d (Verner fired), *munþaz a
                            # voiceless *þ (it did not). That is the whole doctrine in one pair.

    # ── STEM CLASS: the attested ENDING names the declension ─────────────────────────────────
    # *-ą is neuter, *-ǭ / *-ō feminine, *-az a masculine a-stem, *-uz a u-stem, *-iz an i-stem.
    # Wiktionary cites each of these in a class its Germanic reflex does not continue; the ending
    # is the evidence. Same wrong-preform problem as the ablaut, one level up in the morphology.
    "hwehwlą": "kʷékʷlom",  # *hwehwlą — NEUTER. Keep the accent where the source has it:
                            # written oxytone, Verner voices the second *kʷ and gives **hweɣʷlą.
    "mazgą": "mosgʰóm",     # *mazgą — neuter
    "nestą": "nisdóm",      # *nestą — NEUTER, not the masculine *nisdós
    # The WEAK feminines. Their nominative is *-ǭ, with a NASAL vowel, and that nasal is the
    # last trace of a PIE *-ōn — the strong *-eh₂ gives the ORAL *-ō of *hagjō instead. The
    # tilde in the gold is therefore a declension, not a transcription slip, and writing *-ōn
    # is what produces it. (*hagjō above stays *-eh₂ precisely because it is oral.)
    "hōrǭ": "ḱéh₂rōn",      # *hōrǭ — weak ōn-stem, not the masculine *-os
    "abjǭ": "h₂epyṓn",      # *abjǭ — the *β also shows Verner fired, so the accent is late
    "kwenǭ": "gʷenṓn",      # *kwenǭ — and the attested SHORT *e refutes the cited *gʷḗn
    "widuwǭ": "h₁widʰewṓn",  # *widuwǭ — the ENDING only, which is all the nasal evidences. It
                            # still misses by one on the medial vowel (*i for the attested *u).
                            # Writing the zero grade *-uw- in fixes that and breaks the *w
                            # instead — still d=1, and now with an ablaut change nothing
                            # independent supports. The smaller, evidenced claim is the one kept.
    "sternǭ": "h₂sternṓn",  # *sternǭ — the *n is the n-stem suffix the weak ending is built on
    "hrīdrǭ": "kreydʰrṓn",  # *hrīdrǭ — cited as a NEUTER *-om, but the nasal *-ǭ is feminine
    "elhaz": "h₁élḱos",     # *elhaz — a masculine a-stem, not the cited i-stem *-is
    "meduz": "médʰus",      # *meduz — a u-stem WITH *-z, not the bare neuter *médʰu
    "hagjō": "kagʰyéh₂",    # *hagjō — feminine jō-stem, not a neuter *-om. The *-ō is ORAL, and
                            # that is not a slip for the *-ǭ of *hōrǭ/*abjǭ: those are weak ōn-
                            # stems and the nasal is their nominative. Two declensions, not one.
    "gudą": "ǵʰutóm",       # *gudą — neuter, not the masculine *-ós
    "tulguz": "dl̥h₁gʰús",   # *tulguz — u-stem
    "wurhtiz": "wr̥ǵtís",    # *wurhtiz — i-stem
    "niftiz": "néptis",     # *niftiz — i-stem, not the feminine *-ih₂
    "berkō": "bʰerh₁ǵéh₂",  # *berkō — feminine ō-stem
    "swegrō": "sweḱréh₂",   # *swegrō — feminine ō-stem, not the *-uh₂ the citation ends in
    "snuzō": "snuséh₂",     # *snuzō — feminine ō-stem (the *z already shows Verner fired)
    "siniz": "sénis",       # *siniz — i-stem; the *-is is also what raises the *e to the
                            # attested *i, so one correction answers both halves of the miss
    "kumþiz": "gʷḿ̥tis",     # *kumþiz — the attested *u is the zero grade, and the voiceless *þ
                            # puts the accent on the root. Still misses by one: it KEEPS its *m
                            # before the *þ where m_to_n_before_t_d makes it *n. The rule is not
                            # wrong — *ḱm̥tóm > *hundą needs it, and *tehundô and *seventy agree —
                            # so the *m here is lexical, almost certainly restored from the verb
                            # *kweman it is built on. Not something a preform can fix.
    "gunþiz": "gʷʰń̥tis",    # *gunþiz — same shape as *kunþaz: zero grade *u, voiceless *þ
    "kuruz": "gʷr̥h₂ús",     # *kuruz — the attested *ur is the zero-grade *r̥, and it is a u-stem
    "gumô": "ǵʰm̥ṓ",         # *gumô — the attested *um is a SYLLABIC *m̥; written non-syllabic it
                            # gives **ɣmɔːː, a word with no vowel in its first syllable
    # ── From KROONEN and RINGE, now that the reference works are in `sources/` ──────────────
    # These are citations, not inferences: the books give the preform outright.
    # Ringe §.. : "PIE *swéḱs 'six' ! *séḱs (by LEXICAL ANALOGY with *septḿ̥ 'seven'; cf. Lat.
    # sex) > PGmc *sehs". The lost *w is not a sound change at all — it is analogy with 'seven',
    # so it belongs here and not in a rule. (Ringe's ! marks exactly that.)
    "sehs": "séḱs",         # *sehs

    # ── The ORDINALS are n-stems, every one of them ──────────────────────────────────────────
    # PGmc *fedurþô, *fimftô, *sehtô, *sebundô, *ahtudô, *newundô, *tehundô — all *-ô. Wiktionary
    # cites all SEVEN as masculine *-ós. The attested ending is the evidence, exactly as with the
    # other n-stems (*uhsô, *nefô, *gumô) above; this is the same correction applied to a class.
    "sehtô": "séḱtō",       # …and built on the bare root: the gold has no *s before the *t
    "fedurþô": "kʷetwr̥tṓ",
    "fimftô": "penkʷtṓ",
    "sebundô": "septm̥mṓ",
    "ahtudô": "oḱtowṓ",
    "newundô": "h₁newn̥tṓ",   # the *d is a Verner-voiced *t, not an *n
    "tehundô": "déḱm̥tō",     # the consonants DISAGREE and so place the accent: *x is voiceless
                             # (Verner did not fire ⇒ stressed before it) but *d is voiced (it did
                             # ⇒ unstressed before it). Only a root accent satisfies both.
    "fōr": "ph₂uṓr",        # Ringe §..: the Germanic word continues the PIE amphikinetic
                            # COLLECTIVE — "PIE *páh₂wōr ~ *ph₂un-´ ! *ph₂uōŕ … > *puwōr > *pwōr >
                            # PGmc *fōr". Wiktionary cites *péh₂wr̥, whose syllabic *r̥ takes an
                            # epenthetic *u and gives **fōwur. The collective has no *r̥ at all.
    "kinnuz": "ǵénwus",     # Kroonen: *kinnu- f. 'cheek' <= *gen[H]-u — "an amphidynamic u-stem
                            # *gen[H]-u-s… THE STEM VARIANT *gen[H]w-" is what gives the attested
                            # geminate, by the *nw > *nn the cascade already has. The *H is bracketed
                            # in Kroonen (uncertain) and is left out: written in, it vocalises to a
                            # schwa between the *n and the *w and the assimilation never happens.
    "stallaz": "sth₂dʰlós",  # Kroonen: *stalla- M. <= *sth₂-dʰlo-, "formally identical to Lat.
                            # stabulum". Wiktionary cites a NEUTER *sth₂dʰlóm.
    "nadraz": "nh₂trós",    # Kroonen: *nadra- m. 'adder' <= *nh₂tr-ó-, a ZERO grade whose laryngeal
                            # vocalises to the *a of the attested *naðraz — and whose oxytone accent
                            # is what lets Verner voice the *þ to the *ð it shows. Wiktionary cites
                            # *(s)néHtr̥, a full grade with an *ē that gives **nēþur.
    "anadz": "h₂énh₂ets",   # Kroonen: *anad- f. 'duck' <= *h₂enh₂-ET-. Wiktionary's *h₂énh₂ts has
                            # no vowel there at all, and the attested *anadz plainly does. The
                            # root accent is what leaves the *t unstressed and lets Verner voice it
                            # to the *d the attested form shows.
    "mizdō": "misdʰéh₂",    # Kroonen: *mizdō(n)- f. 'reward' <= *misdʰ-EH₂-. A FEMININE, where
                            # Wiktionary cites the masculine *misdʰós.
    "kwernuz": "gʷerh₂nús",  # Kroonen's headword is *kwernu-, a U-STEM — this row is the one his
                             # preform is actually for. Same *-h₂n- giving the attested *rn*.
    "kwernō": "gʷerh₂néh₂",  # Kroonen: *kwernu- <= *gʷerh₂-nu-. The *-h₂n- is what gives the *rn*
                            # of the attested *kwernō; Wiktionary's *gʷréh₂wō has a *w instead.
    "nasō": "nh₂̥́seh₂",      # Kroonen: *nasō <= *nh₂-s-eh₂-, a zero grade. Wiktionary's *néh₂s is a
                            # full-grade root noun, whose *eh₂ gives a LONG *ā — but the attested
                            # *nasō has a SHORT *a. The accent goes on the LARYNGEAL, written with
                            # the ring (syllabic) and the acute: a vocalised laryngeal is a nucleus
                            # and can bear the beat like any other. That is what keeps the *s
                            # voiceless — Verner needs an UNstressed syllable before it — and the
                            # attested *nasō has a voiceless *s.
    "hōfaz": "ḱóh₂pos",     # Kroonen: *hōfa- <= *ḱoHp-o-, with the laryngeal BEFORE the *p, and
                            # he says so outright — "the difference between Gm. *ḱoHp-o- and
                            # Indo-Iranian *ḱopH-o- implies that LARYNGEAL METATHESIS occurred in
                            # one of the two forms". Wiktionary cites the Indo-Iranian order, whose
                            # laryngeal cannot lengthen the *o. The Germanic order gives *ḱōpos >
                            # *hōfaz — the long *ō the attested form has and we could not produce.
    "watōr": "wódōr",       # Kroonen: *watar- <= *uod-r/n-. Wiktionary cites *wédōr with an *e,
                            # but the attested Germanic *a is the regular reflex of PIE *o.
    "þahsuz": "táksus",     # Kroonen: *þahsu- <= *taks-. Not the thorn cluster *tótḱus Wiktionary
                            # cites — plain *ks, which gives *þɑxsuz straight off.
    "haihaz": "keh₂íkos",   # The attested *x is VOICELESS, so Verner did not fire and the accent
                            # must sit on the syllable before it. Kroonen's *keh₂i-ko- leaves the
                            # accent unmarked; the consonant places it, as everywhere in this table.
    "swestēr": "swéstēr",   # Ringe §.. : *swestēr's *-t- is "not a certain example" of PIE *sr >
                            # *str and "could owe its *-t- to lexical analogy with *duhtēr" — the
                            # word SHIFTED INTO THE *-ter- CLASS. That is morphology, not a sound
                            # law, so it belongs here rather than in a rule.
    "fiskaz": "pískos",     # *fiskaz — a-stem, and the attested SHORT *i refutes the cited
                            # diphthong *ey (Latin piscis has the same short i)

    # ── The n-stems: the attested *-ô is a nominative *-ō, not the cited *-n̥ / *-s ───────────
    # Proto-Germanic's *-ô is the n-stem nominative singular, and PIE spells that *-ō (*ǵʰmṓ,
    # *h₂éḱmō). Wiktionary cites several of these as neuter *-mn̥ collectives or as root nouns
    # instead, which no sound law turns into *-ô. The ending is again the evidence.
    "namô": "h₁nómō",       # *namô — n-stem nominative, not the neuter collective *-mn̥
    "sēmô": "séh₁mō",       # *sēmô
    "hleumô": "ḱléwmō",     # *hleumô
    "neurô": "negʷʰrṓ",     # *neurô
    "uhsô": "uksṓ",         # *uhsô — the *-ô is ORAL and overlong, so not the nasal *-ǭ of *-ēn
    "nefô": "népō",         # *nefô
    "hertô": "ḱérdō",       # *hertô — Germanic took the root noun *ḱḗrd into the n-stems

    # ── s-mobile ────────────────────────────────────────────────────────────────────────────
    # The transliterator drops an optional *(s)-, which is right for whale (PGmc *hwalaz, no s)
    # but wrong for share (PGmc *skarō, which has it). It is lexical, so it is settled here.
    "skarō": "skoréh₂",     # *skarō — keeps the s-mobile

    # ── DELIBERATELY NOT FIXED ──────────────────────────────────────────────────────────────
    # *warmaz is a BAD ETYMON in the source, and Ringe says so by name. Wiktionary derives it from
    # *gʷʰórmos, which would make it a counterexample to the word-initial *gʷʰ > *b that `gwh_to_w`
    # now implements. It is not one: in the footnote to that very passage Ringe writes "I connect
    # PGmc *warmaz 'warm' with Hitt. warnuzzi, not with Av. garəmō" — i.e. he rejects the
    # labiovelar etymology outright. The source hierarchy (Ringe > Wiktionary) says the rule wins
    # and the datum loses. He gives no PIE form to put here in its place, and inventing one is the
    # thing this table exists not to do, so *warmaz stays a miss ON PURPOSE. Do not "fix" the rule.
    #
    # *hlūdaz has a long *ū that the cited *ḱlutós cannot give, and a laryngeal-final root
    # (*ḱluh₁tós) would supply it exactly. But every cognate has a SHORT u — Greek klutós,
    # Sanskrit śrutá-, Latin inclutus — and Wiktionary says in as many words that "the origin of
    # the long vowel is unclear". Writing the laryngeal in would not be reading the preform off
    # the attested form, the way every entry above does; it would be inventing the one feature
    # needed to make the cascade land. It stays a miss, and so does *hūnaz (*ḱuh₁nós), whose long
    # *ū the corpus flatly contradicts: *suh₁nús gives *sunuz with a SHORT u, same environment.
    # *ansuz stays a miss too — see the note on m_to_n_before_t_d in rules.toml: *amsaz keeps its
    # *ms, so *ansuz's *n cannot be a sound change and we have no independent evidence for its
    # preform. *wapsō keeps a STOP *p that no accent or grade can produce from *wóbʰseh₂.
}


# Wiktionary and the engine spell the same reconstructed sounds differently. These are
# notational identities, not phonological claims: Wiktionary writes the glides as non-syllabic
# ɪ̯/u̯ and the long mid vowels of Proto-Germanic as ɔː/ɛː, where the engine writes j/w and
# oː/eː. Left unreconciled, every word would miss on spelling and the accuracy figure would
# measure transcription style instead of the rules.
#
# ɔː/ɛː are NOT in the list, though they were once: Proto-Germanic ō really is [ɔː] and Old
# English ō really is [oː], so the difference between the columns is a sound change (the
# raising in `wg_long_mid_raising`), not a spelling convention. Mapping it away would have
# hidden a real rule.
#
# θ/ð → θ̠/ð̠ is the same kind of identity, read the other way: both spell Germanic þ, but the
# engine's is non-dental because it inherits PIE *t's alveolar coding, while Wiktionary's plain
# θ is dental by IPA convention. One phoneme, two spellings.
#
# NOT a rule for ɑ→a, though the gold is full of ɑ: the engine derives both (ˈan.θ̠e.rɑz), so
# folding them together turns correct segments into wrong ones — it cost 8 exact matches when
# tried. Where the two really disagree on the low vowel, that is phonology, not spelling.
#
# Applied to the RECONSTRUCTED columns only. The modern column is left alone, where the same
# symbols are contrastive: RP's ɔː (four) is not oː.
# Corrections to the ATTESTED Proto-Germanic form itself, keyed by the Wiktionary headword.
#
# This is a different and far more dangerous thing than PREFORM_FIXES above, and the line between
# them must not blur. PREFORM_FIXES corrects the *input*, using the attested form as INDEPENDENT
# evidence — that is what keeps it out of circularity. This corrects the *target*: the thing the
# engine is scored against. Edit it to make a word pass and the accuracy figure stops measuring
# anything at all.
#
# It is admissible for exactly one reason: **the 200 column is a RECONSTRUCTION, not an
# attestation.** Wiktionary's Proto-Germanic is one scholar's reconstruction and it can simply be
# wrong; where the standard reference work says so in as many words, the reference work wins.
#
# THE RULES, and they are not negotiable:
#   1. ONLY the 200 (Proto-Germanic) column. The 900/1400/final columns are ATTESTED — real
#      recorded Old English, Middle English and modern forms. They are never touched, whatever
#      they cost us.
#   2. ONLY with an explicit citation from Kroonen or Ringe, quoted in the comment. Never from our
#      own inference, and never because a word would otherwise miss.
#   3. The entry must be defensible with the derivation switched off. If the only argument for it
#      is "the cascade would then land", it does not go in.
ATTESTED_FIXES = {
    # Ringe writes *anþaraz where Wiktionary writes *anþeraz, and he argues the point at length —
    # it is the very example he uses to establish that unstressed *e LOWERED to *a before *r in
    # Proto-Germanic (§5.3.2 (iii), and `unstressed_e_to_a_before_r` in rules.toml):
    #
    #   "The regular Gothic and ON reflex is a. The OS and OHG spellings are variable, but a is a
    #    frequent variant. Only in northern WGmc ('Anglo-Frisian') do we typically find e — and
    #    that is precisely the area in which PGmc *a was fronted and typically appears as e when
    #    unstressed. It is reasonable to infer from this pattern of evidence that unstressed *e
    #    was lowered to *a before *r already in PGmc."
    #
    # So Wiktionary's *e is the Anglo-Frisian INNOVATION read back into the protoform, and its
    # *anþeraz is the one form that would refute a rule the rest of the daughters support. The
    # source hierarchy (Ringe > Wiktionary) settles it, and this is exactly the case ATTESTED_FIXES
    # is fenced to allow: a cited reference work correcting a RECONSTRUCTION, never an attestation.
    "anþeraz": "ˈɑnθɑrɑz",
    # Kroonen's headword is *nista- 'nest' <= *ni-zd-o- — with an /i/, not the /e/ of Wiktionary's
    # *nestą. He also has *fiska- <= *pisk-o- (cf. Lat. piscis) with /i/, and Ringe's bibliography
    # cites Lloyd, "Is there an a-umlaut of i in Germanic?" — so the lowering of *i is doubtful AT
    # PROTO-GERMANIC. It plainly happens LATER (Old English has nest with an /e/ while fisc keeps
    # its /i/), which is where `pgmc_i_lowering` has been re-dated to. The 900 column, being a real
    # attestation, is untouched and still reads `nest`.
    "nestą": "ˈnistɑ̃",
    # And the same again, from the same page of the same book: Kroonen's headword for 'man' is
    # "*wira- m. 'man': Go. wair, ON verr, OE, OS, OHG wer, cf. Skt. vīra-" — an /i/, not the /e/
    # of Wiktionary's *weraz. That makes THREE (*nista-, *fiska-, *wira-), all with /i/ at
    # Proto-Germanic, all with /e/ or /i/ later exactly as Old English attests. The lowering is
    # uniformly post-Proto-Germanic, and *weraz was never counter-evidence to that — it was the
    # same error a second time. (Old English wer, with its /e/, is untouched: it is attested.)
    "weraz": "ˈwirɑz",
}


CONVENTIONS = [("ɪ̯", "j"), ("i̯", "j"), ("u̯", "w"), ("θ", "θ̠"), ("ð", "ð̠")]


def normalise(ipa: str, *, reconstructed: bool) -> str:
    """Strip a Wiktionary transcription down to what the inventory can segment."""
    s = ipa.split(",")[0].split("/")[1] if ipa.count("/") >= 2 else ipa
    s = s.strip("/[] ")
    s = s.replace("ɡ", "g")            # script g U+0261 → ascii g
    # The tie bar BELOW (U+035C) binds the OE diphthongs, e͜o — two vowel segments, so it goes.
    # The tie bar ABOVE (U+0361) binds the AFFRICATES, t͡ʃ and d͡ʒ — ONE segment, and the engine's
    # own letter carries it, so it must stay. Stripping both (as this did) split every affricate
    # into a /t/ plus a /ʃ/, and the gold for ċeald read as four segments where the engine
    # derives three. Palatalisation was scoring as a miss on words it had got exactly right.
    s = s.replace("͜", "")                    # U+035C, below: the OE diphthongs
    s = re.sub(r"\(.*?\)", "", s)      # optional segments: (i)janą
    s = s.replace(".", "")             # syllable dots
    s = ud.normalize("NFD", s)
    for mark in ("̝", "̞", "̥"):        # raised / lowered / voiceless
        s = s.replace(mark, "")
    s = ud.normalize("NFC", s)
    if reconstructed:
        for theirs, ours in CONVENTIONS:
            s = s.replace(theirs, ours)
    # Wiktionary leaves stress unwritten on a monosyllable (boːg, kɑmb, guːs) and marks it only
    # where there is a choice to record. The engine always marks it, and stress is a feature of
    # the vowel — so an unmarked target scores its stressed vowel wrong. Restoring the mark
    # states what the source assumes: a monosyllabic content word carries primary stress, and
    # in Germanic and Old English the stress is fixed on the first syllable anyway.
    if "ˈ" not in s and "ˌ" not in s:
        s = "ˈ" + s
    return s


def modern_ipa(sounds: dict, word: str, pos: str) -> str:
    """The RP transcription of *word* as a *pos*, from the kaikki English `sounds`.

    Two traps. Wiktionary tags regional variants — heart is /hɑːʔ/ under
    ("British", "Southern", "Standard") and /hɑːt/ under ("Received-Pronunciation") — so the
    exact RP tag is required, not a loose match on "British". And a homograph has one entry
    per part of speech: `were` the noun (/wɪə/, the werewolf one) is not `were` the verb
    (/wɜː/), so the entry is chosen by the part of speech the chain descends into.
    """
    entries = sounds.get(word, [])
    same_pos = [e for e in entries if e["pos"] == pos] or entries
    for wanted in ("Received-Pronunciation", "General-American"):
        for entry in same_pos:
            for sound in entry["sounds"]:
                if wanted in sound["tags"]:
                    return sound["ipa"]
    # No tagged transcription: take an untagged one before any regionally-marked variant.
    for entry in same_pos:
        for sound in entry["sounds"]:
            if not sound["tags"]:
                return sound["ipa"]
    return ""


def main() -> None:
    project = load_project(Path("projects/pie_to_english")).unwrap()
    chains = json.load(open(CACHE / "chains.json"))
    pde_sounds = json.load(open(CACHE / "pde_sounds.json"))
    freq = {}
    for line in open(CACHE / "en_50k.txt"):
        word, _, count = line.partition(" ")
        freq[word.strip()] = int(count)

    def segmentable(ipa: str, *, reconstructed: bool = True) -> str:
        """The normalised IPA, or "" if the inventory cannot segment it."""
        if not ipa:
            return ""
        s = normalise(ipa, reconstructed=reconstructed)
        return s if s and try_segment(s, project) is not None else ""

    rows, dropped, blanked = [], {}, {}

    def drop(why: str) -> None:
        """The whole row is discarded."""
        dropped[why] = dropped.get(why, 0) + 1

    def blank(why: str) -> None:
        """The row is kept; only its `final` column is unusable."""
        blanked[why] = blanked.get(why, 0) + 1

    for c in chains:

        # A Ringe pair carries no part of speech — he cites a form and a gloss, not a lexicon
        # entry — so the word-class filter, which exists to catch Wiktionary's wrong-cell links,
        # has nothing to read and nothing to catch. Ringe's own citation IS the guarantee.
        if c.get("source") != "Ringe" and c["pos"] not in KEEP_POS:
            drop("not a noun-like word class (verb/affix)")
            continue
        if not c["pgmc"] or c["pgmc"].startswith("-") or c["pgmc"].endswith("-"):
            drop("affix")
            continue
        if re.search(r"\bof\b.*\*", c["gloss"]):
            drop("PIE form is an inflected cell, not the preform")
            continue
        if not c["pie"] or " " in c["pie"]:
            drop("PIE form is a bare root, not a preform")
            continue
        # A ROOT is truncated — it ends (or begins) with a hyphen: *nem-, *gʰeldʰ-. A hyphen in
        # the MIDDLE is something else entirely: Wiktionary's morpheme boundaries inside a form
        # that is perfectly complete (*gʷʰon-yeh₂ 'wound', *kort-ús 'hard', *mn̥-tó-s 'mouth').
        # Dropping every hyphen alike threw away 142 whole words to catch the roots.
        pie_form = PREFORM_FIXES.get(c["pgmc"], c["pie"])
        if pie_form.startswith("-") or pie_form.endswith("-"):
            drop("PIE form is a bare root, not a preform")
            continue
        pie_form = pie_form.replace("-", "")
        # ...but a complete form can still be the WRONG CELL. Wiktionary links the 3sg present
        # *wénh₁-e-ti against the NOUN *wēniz; no sound change turns a finite verb into a noun,
        # so the row would be a permanent miss however good the rules were. Same trap the verbs
        # set, one word class over — and note it is a trap only for a NON-verb: a verb's PIE form
        # ends in *-eti because it IS the 3sg present, which is the whole point of the cell match
        # `build_chains` makes for it.
        if c["pos"] != "verb" and _bare(pie_form).endswith("eti"):
            drop("PIE form is an inflected cell, not the preform")
            continue
        # An unaccented form gets INITIAL stress — which is not a guess.
        #
        # Proto-Germanic fixes the stress on the first syllable (`stress_change`), so the PIE
        # accent reaches the output through exactly one door: VERNER'S LAW. Where a word has no
        # Verner-eligible fricative the accent cannot affect the 200 form at all — and that is
        # measurable, not assumed: of the 49 unaccented nouns/adjectives, 40 give a BYTE-IDENTICAL
        # Proto-Germanic form under every possible placement of the accent. Initial is simply one
        # of them, and it is where Germanic puts the stress anyway.
        #
        # For the other 9 the accent does change the outcome, and those become honest untuned
        # misses. Reading the accent off the attested Germanic consonant is legitimate — a voiced
        # fricative proves Verner fired — but that is the PREFORM_FIXES move, a separate and
        # deliberate curation pass. Admission is not curation, and the two must not blur.
        if not has_accent(pie_form):
            pie_form = accent_first_nucleus(pie_form)
        try:
            word = to_ipa(pie_form, project)
        except PieError as exc:
            drop(f"PIE not transliterable ({str(exc).split(' in ')[0]})")
            continue

        # The MODERN column is the fragile one, and the three conditions below say only that it
        # cannot be trusted — not that the word is bad. They used to drop the whole row, which
        # threw the Proto-Germanic and Old English columns out with it. A word is now scored at
        # whichever checkpoints it has, so an untrustworthy `final` is BLANKED and the row stays:
        #   * no surviving modern reflex — the word died, but *hurnaz is still attested;
        #   * several modern reflexes (of/off, thine/thy) — the sound laws produce one output and
        #     nothing in the data says which reflex is the regular one, so the final is unusable
        #     (but the Proto-Germanic form is not in the least ambiguous);
        #   * the modern IPA will not segment.
        reflexes = c["pde"]
        pde = reflexes[0] if len(reflexes) == 1 else ""
        if not reflexes:
            blank("no surviving modern reflex — scored at 200/900 only")
        elif len(reflexes) > 1:
            blank("several modern reflexes — cannot say which is the regular one")
        final = ""
        if pde:
            final = segmentable(modern_ipa(pde_sounds, pde, c["pos"]), reconstructed=False)
        if pde and not final:
            blank("no segmentable modern IPA")

        # The 200 column, with any cited correction to the RECONSTRUCTION applied (ATTESTED_FIXES).
        pgmc = segmentable(ATTESTED_FIXES.get(c["pgmc"], c["pgmc_ipa"]))
        oe, me = segmentable(c["oe_ipa"]), segmentable(c["me_ipa"])
        # A row with no target at ANY checkpoint scores nothing and is only noise in the reports.
        if not (pgmc or oe or me or final):
            drop("no segmentable target at any checkpoint")
            continue

        rows.append({
            # A word that died before Modern English has no reflex to be named after, so it is
            # keyed by its Proto-Germanic headword instead (*hurnaz). The gloss is a label and a
            # lookup key for --single; it is not required to be an English word.
            "word": word,
            "gloss": pde or c["pgmc"],
            "frequency": freq.get(pde.lower(), 1) if pde else 1,
            PGMC: pgmc,
            OE: oe,
            ME: me,
            "final": final,
            "_pie": pie_form, "_cited": c["pie"],  # _cited keeps the hyphens: see richness()
            "_sense": c["gloss"],                   # the Wiktionary sense: see sense()
            "_source": c.get("source", "Wiktionary"),
            "_cell": c.get("cell", ""),             # a verb's paradigm cell: 1sg / 3sg
            "_pgmc": c["pgmc"], "_oe": c["oe"], "_me": c["me"],
            "_variants": " ".join(reflexes[1:]), "_pos": c["pos"],
        })

    # One row per modern word AND one per IPA key — `word` is what the loader keys the
    # lexicon by, so two etyma transliterating alike would silently collide. Sorting by
    # frequency first means an attested high-frequency reflex always beats a collision with one
    # of the new frequency-1 words. The losers are listed, not just counted: a silent truncation
    # reads as "we covered everything" when we did not.
    # Frequency first, then the number of attested checkpoints. Frequency alone left the tie
    # between two etyma that transliterate alike to be settled by list order: *h₂ékʷeh₂ yields
    # both *ahwō (attested at 200/900/1400) and *āhwijaz (attested only as modern "eagre"), and
    # both are frequency 1. The richer row must win on purpose, not by accident — three
    # checkpoints test more of the cascade than one. Where a word is genuinely frequent, that
    # still dominates, so no common reflex is ever displaced by a new frequency-1 homophone.
    # The last key is the CITATION form, and it settles a tie the first two cannot. Two etyma can
    # land on one Germanic word: *angô is both *h₂énk-ō 'a crook' and *h₂én(h₁)ǵʰō 'smell', and
    # with no modern reflex both are frequency 1 with the same checkpoints. The one that survives
    # is the one Wiktionary writes as a plain lemma rather than as a morphological ANALYSIS (the
    # hyphens), so the winner is chosen rather than decided by list order.
    def richness(r) -> tuple:
        analysed = "-" in r["_cited"]
        return (
            -r["frequency"],
            -sum(bool(r[col]) for col in (PGMC, OE, ME, "final")),
            analysed,
        )

    # A GLOSS collision is no longer a reason to lose a word, and that is what ids are for.
    # *angô is TWO etyma — *h₂énk-ō 'a bend, crook' and *h₂én(h₁)ǵʰō 'smell' — and neither has a
    # modern reflex to be named after, so both fall back to the Proto-Germanic headword and
    # collide. They are not the same word, they have different preforms, and each is a real test
    # of the cascade; dropping one to keep the name unique threw away evidence to satisfy a
    # naming constraint. They are now told apart by their Wiktionary sense (*angô-crook,
    # *angô-smell), which is exactly the job the id was introduced to do.
    #
    # A WORD KEY collision is different and still fatal: two etyma that transliterate to the SAME
    # PIE input are one input to the engine. It will derive one form, and no id can make that two
    # answers — so the richer row wins and the other is reported, not silently dropped.
    def sense(r) -> str:
        """A short discriminator from the Wiktionary sense: 'a bend; crook' -> 'crook'."""
        words = re.findall(r"\w+", r["_sense"].split(";")[0].split(",")[0], re.UNICODE)
        skip = {"a", "an", "the", "to", "of"}
        pick = [w for w in words if w.lower() not in skip]
        return (pick[-1] if pick else "").lower()

    by_gloss: dict[str, list] = {}
    for row in rows:
        by_gloss.setdefault(row["gloss"], []).append(row)
    for gloss, group in by_gloss.items():
        if len(group) < 2:
            continue
        for row in group:
            tag = sense(row)
            if tag and tag != gloss:
                row["gloss"] = f"{gloss}-{tag}"

    seen_gloss, seen_word, unique, collisions = set(), set(), [], []
    for row in sorted(rows, key=richness):
        clash = ("word key " + row["word"] if row["word"] in seen_word
                 else "gloss " + row["gloss"] if row["gloss"] in seen_gloss else "")
        if clash:
            collisions.append(f"*{row['_pie']} (*{row['_pgmc']}) — collides on {clash}")
            drop("duplicate word key or gloss")
            continue
        seen_gloss.add(row["gloss"])
        seen_word.add(row["word"])
        unique.append(row)

    # The LONG shape — one row per attested form, not one per word. A word is a series of forms
    # through time, and its grammatical category can differ at each of them, which a wide
    # one-column-per-checkpoint table has nowhere to put. The seed is the PIE form at SEED_TIME;
    # every later row is a target.
    #
    # The category is what a rule can now be scoped to (`categories = [...]` in rules.toml). It
    # is carried straight through from the word class the chain was built from, so the verbs
    # announce themselves as verbs — which is what makes their 3sg present a class the cascade
    # can name, rather than something a build flag has to hold apart.
    def category_of(row) -> str:
        pos = row["_pos"]
        if pos != "verb":
            return pos          # "" for a Ringe pair: he gives no word class, so we claim none
        # The cell is part of what the word IS — the 1sg and the 3sg of one verb are two
        # different words here, with different preforms and different targets, and a rule that
        # wants one and not the other can now say so.
        return f"verb.pres.{row['_cell']}"

    # The id is derived from the gloss, not from the IPA. An IPA string is a poor identifier —
    # unreadable in a report, and two etyma can transliterate alike — and the rows above are
    # already deduplicated on the gloss, so a slug of it is unique by construction.
    def ident(row) -> str:
        s = re.sub(r"[^\w\s-]", "", ud.normalize("NFC", row["gloss"]).strip().lower())
        return re.sub(r"[\s_-]+", "-", s).strip("-") or row["word"]

    with open(OUT, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "time", "ipa", "category", "gloss", "frequency"])
        for row in unique:
            category, word_id = category_of(row), ident(row)
            writer.writerow(
                [word_id, SEED_TIME, row["word"], category, row["gloss"], row["frequency"]]
            )
            for time, column in ((PGMC, PGMC), (OE, OE), (ME, ME), ("final", "final")):
                if row[column]:
                    writer.writerow([word_id, time, row[column], category, "", ""])

    json.dump(unique, open(CACHE / "gold_rows.json", "w"), ensure_ascii=False, indent=1)
    print(f"wrote {OUT} — {len(unique)} words")
    for time in (PGMC, OE, ME):
        print(f"  attested at {time}: {sum(1 for r in unique if r[time])}")
    print(f"  attested final:  {sum(1 for r in unique if r['final'])}")
    print(f"  doublets to check: {sum(1 for r in unique if r['_variants'])}")
    print("\ndropped (row not written):")
    for why, n in sorted(dropped.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>4}  {why}")
    print("\nkept, but with a BLANK final column:")
    for why, n in sorted(blanked.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>4}  {why}")
    if collisions:
        print(f"\ncollisions dropped ({len(collisions)}):")
        for line in collisions:
            print(f"  {line}")


if __name__ == "__main__":
    main()
