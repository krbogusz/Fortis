"""Walk the kaikki Proto-Germanic extract into PIE → PGmc → OE → ME → English chains.

Stage one of two: this writes `chains.json`, which `build_gold.py` then filters and scores into
`words.csv`. `chains.json` is an intermediate and is not committed; `words.csv` is, under
CC BY-SA 4.0 — the data is Wiktionary's, and that licence is share-alike. See SOURCE.md.

The spine is the **Proto-Germanic** record: it carries its PIE parent (an `inh` template) and a
`descendants` tree running down through Old English → Middle English → English, so one record
yields a whole chain and the OE/ME/PDE entries supply the IPA for each checkpoint.

**Old English is optional, and that is the point.** This script used to `continue` on any etymon
with no attested OE descendant, which quietly threw away every word that died before Old English
or simply is not linked to one — more than half of the usable Proto-Germanic gold. But the 200
checkpoint is scored against the *Proto-Germanic* form, and needs a PIE parent and a PGmc IPA and
nothing else. A chain that stops at Proto-Germanic is a complete chain for that column; the engine
scores each word at whichever checkpoints it has. So the walk keeps every etymon with a PIE parent
and lets OE/ME/PDE be blank.

Join note: Wiktionary stores Old English page titles WITHOUT macrons (`fot`) while the descendants
trees cite the macronned form (`fōt`). The macronned form lives in forms[] under the `canonical`
tag, so every entry is indexed under BOTH keys.
"""

import collections
import json
import os
import sys
import unicodedata as ud

from pathlib import Path

import pgmc_ipa

# The kaikki extracts and the intermediate chains.json. Big (~280 MB) and regenerable, so it
# is never committed — see SOURCE.md for how to populate it. Override with FORTIS_PIE_CACHE;
# the default is a .cache/ beside this project.
CACHE = Path(os.environ.get("FORTIS_PIE_CACHE") or Path(__file__).parent.parent / ".cache")
K = CACHE / "kaikki"


def load_ipa(path: Path) -> dict[str, str]:
    """{page title AND canonical form} -> phonemic IPA."""
    out: dict[str, str] = {}
    for line in open(path, encoding="utf-8"):
        d = json.loads(line)
        slashed = [s["ipa"] for s in d.get("sounds", []) if (s.get("ipa") or "").startswith("/")]
        any_ipa = [s["ipa"] for s in d.get("sounds", []) if s.get("ipa")]
        ipa = slashed[0] if slashed else (any_ipa[0] if any_ipa else None)
        if not ipa:
            continue
        keys = {d.get("word")}
        for f in d.get("forms", []):
            if "canonical" in (f.get("tags") or []) and f.get("form"):
                keys.add(f["form"])
        for k in keys:
            out.setdefault(k, ipa)
    return out


def gloss_of(d: dict) -> str:
    """The record's first sense gloss ("" if it has none)."""
    for s in d.get("senses", []):
        for g in s.get("glosses", []) or []:
            return g
    return ""


def walk(nodes, want: str) -> list[dict]:
    """Every descendant node in *want*'s language, at any depth."""
    hits = []
    for n in nodes or []:
        if n.get("lang_code") == want and n.get("word"):
            hits.append(n)
        hits += walk(n.get("descendants"), want)
    return hits


def pie_parent(d: dict) -> str:
    """The PIE form this record inherits from, bare of its asterisk ("" if none)."""
    for t in d.get("etymology_templates", []):
        a = t.get("args", {})
        if t.get("name") in ("inh", "inh+") and a.get("2") == "ine-pro":
            # arg 3 is the linked form; when it is blank the form is in arg 4
            # ({{inh|gem-pro|ine-pro||*úd-s}} — the display-only convention).
            return (a.get("3") or a.get("4") or "").lstrip("*")
    return ""


# The weak presents are excluded, and the reason is not that they are hard — it is that no sound
# change reaches them. Ringe derives the weak class 1 present with an explicit ANALOGICAL step,
# which he marks with his "!" (the same mark he puts on *h₂stér- >! *sternan-):
#
#     PIE *gʷhédhyeti '(s)he is asking for' ... > *bedjidi, *bedjondi >! PGmc *bidiþi, *bidjanþi
#                                                                     ^
# Read the middle column: the REGULAR outcome is *bedjidi, with the Verner-VOICED *d — because the
# vowel before the ending is unaccented, exactly as in the strong verbs. The attested *-iþi, with
# its voiceless *þ, is levelled in from elsewhere in the paradigm afterwards. So *satiþi, *sōkīþi,
# *bidiþi and the other 28 are targets that a correct sound-change cascade CANNOT hit, and ours
# duly derives *satiði, *sōkiði, *bidiði — the ending Ringe says the phonology gives.
#
# Scoring against them would do real damage twice over. It would hold 30 rows permanently wrong
# for being right, dragging the Proto-Germanic figure down by nine points; and it would stand as a
# standing invitation to "fix" Verner's law — which would break the 16/19 strong verbs that
# currently derive perfectly, since they need the very voicing the weak verbs appear to refuse.
# This is the same line the lexicon already draws when it drops a PIE link that names the wrong
# cell: the target must be reachable by rule, or it is not evidence about rules.
#
# Flip this to True to score them anyway — they are otherwise regular, and they are the only
# evidence in the lexicon for the weak suffix's *i/*ī length (see SOURCE.md, Sievers' Law).
KEEP_WEAK_PRESENTS = False


def is_weak_present(third: str) -> bool:
    """Is this Germanic 3sg a weak present — the one Ringe reaches by analogy?

    Keyed on the GERMANIC ending, which is the thing Ringe's claim is actually about, and not on
    the PIE suffix, which is only a proxy for it. The proxy breaks: *h₂wḗh₁ti has a laryngeal
    suffix and so looks weak, but Germanic *wēidi ends in a Verner-VOICED *-di — it is a regular,
    reachable target, and suffix-matching quietly filed it under "analogy" where its miss could
    never be read as the rule signal it is.

    The ending sorts the 49 verbs with no exceptions: 30 end *-þi (weak — the analogical ending),
    19 end *-di (Verner fired regularly).
    """
    return third.endswith("þi")


def third_singular(d: dict) -> str:
    """The Proto-Germanic 3sg present active indicative, from the inflection table ("" if none)."""
    want = {"active", "indicative", "singular", "third-person"}
    for f in d.get("forms", []):
        if want <= set(f.get("tags") or []) and f.get("form") not in (None, "", "-"):
            return f["form"]
    return ""


def finite_verb(d: dict, pie: str) -> dict | None:
    """A verb chain, in the 3sg present — or None if the two ends are not the same cell.

    A verb cannot be scored on its citation forms the way a noun can. Wiktionary lemmatises a PIE
    verb at the 3sg present (*bʰéreti) but a Proto-Germanic verb at the INFINITIVE (*beraną), so
    the pair names two different cells of the paradigm and no sound change connects them: *bʰéreti
    can never yield *beraną, because the ending is not the same morpheme. That mismatch — not
    anything phonological — is why verbs were excluded from this lexicon.

    Both ends do exist in the 3sg, though: the PIE lemma already IS one, and the Germanic 3sg
    (*biridi) sits in the record's inflection table. Read the pair from there and input and target
    are the same morphological cell again, exactly as they are for a noun's accusative.

    Two filters keep the pair honest, and they drop rather more than they keep:

    - the PIE end must be a finite 3sg PRESENT — the primary ending *-ti. Wiktionary often links
      the bare ROOT (*nem-, *gʰeldʰ-) or a different tense (*wóyde is a perfect, *bʰúHt an
      aorist), and building a present out of those would mean reconstructing the input ourselves.
    - the Germanic end must carry a PRESENT ending too. The preterite-presents (*wait, *kann,
      *þarf) descend from PIE perfects and take perfect endings, so *ǵn̥néh₃ti > *kann is the
      same wrong-cell pairing one tense over.
    """
    third = third_singular(d)
    if not third or not third.endswith(("di", "þi", "ti")):
        return None
    if not pie.endswith("ti"):
        return None
    if pie.startswith("-") or third.startswith("-") or "-" in pie:
        return None                     # a suffix (*-eh₂yéti) or a hyphenated analysis, not a form
    if "(" in pie:
        # An optional segment — the s-mobile of *(s)méldeti. The transliterator drops it, so the
        # input would lack the s that *smiltidi plainly continues, and the row could never derive.
        # Deciding it belongs means reading the answer off the target, which is what PREFORM_FIXES
        # exists to do under citation; it is not something to infer here.
        return None
    if KEEP_WEAK_PRESENTS is False and is_weak_present(third):
        return None
    ipa = pgmc_ipa.transcribe(third)
    if not ipa:
        return None
    # Old English and later are left blank ON PURPOSE. The descendants tree hangs off the
    # INFINITIVE, so it cannot supply the 3sg; and the modern 3sg -s is Northumbrian analogy, not
    # the phonological continuation of -þ. A verb is scored at Proto-Germanic and nowhere else.
    return {
        "pie": pie, "pgmc": third, "pgmc_ipa": f"/{ipa}/", "cell": "3sg",
        "oe": "", "oe_ipa": "", "me": "", "me_ipa": "", "me_variants": 0, "pde": [],
        "pos": "verb", "gloss": gloss_of(d),
    }


def first_singular(d: dict) -> str:
    """The Proto-Germanic 1sg present active indicative, from the inflection table."""
    want = {"active", "indicative", "singular", "first-person"}
    for f in d.get("forms", []):
        if want <= set(f.get("tags") or []) and f.get("form") not in (None, "", "-"):
            return f["form"]
    return ""


def load_pie_first_singulars() -> dict[str, str]:
    """{PIE lemma -> its 1sg present}. The PIE record carries a full paradigm, same as the PGmc one.

    Needed because the chain only carries the PIE *lemma* (from the Germanic record's etymology
    template), and the lemma is the 3sg. The 1sg has to be read out of the PIE record itself.
    """
    want = {"first-person", "singular", "indicative"}
    out: dict[str, str] = {}
    for line in open(K / "pie.jsonl", encoding="utf-8"):
        d = json.loads(line)
        if d.get("pos") != "verb":
            continue
        for f in d.get("forms", []):
            if want <= set(f.get("tags") or []) and f.get("form") not in (None, "", "-"):
                out.setdefault(d["word"], f["form"])
                break
    return out


def finite_verb_1sg(d: dict, pie: str, pie_1sg: str) -> dict | None:
    """A verb chain in the 1sg present — the cell that gets the WEAK verbs back.

    The 3sg had to exclude the 30 weak presents because Ringe reaches their *-iþi by an explicit
    ANALOGY (see `is_weak_present`), which no sound change can produce. The 1sg has no such
    problem, and the reason is structural: **its ending has no consonant.** Ringe's own paradigm
    gives 1sg *līhwō, *werþō, *kwemō, *bidjō, *lētō — and *bidjō sits right beside the *bidiþi he
    marks as analogical. Verner's Law needs a fricative to voice; *-ō offers none, so the cell the
    analogy ruined in the 3sg is untouched in the 1sg, and the weak verbs are scorable again.

    It is also a genuine second test of the roots we already have, not a duplicate of them:

        3sg *b-i-ridi   — *e RAISED to *i before the following *i
        1sg *b-e-rō     — no following *i, so the raising must NOT fire

    A minimal pair, and the 1sg is the negative control.

    The filters mirror the 3sg's, one cell over: the PIE end must be a THEMATIC present 1sg
    (*-oh₂), which rejects the perfect (*wóydh₂e) and the athematic (*h₁édmi); and the Germanic
    end must carry the present *-ō, which rejects the preterite-presents (*wait, *kann, *þarf)
    whose 1sg is a perfect.
    """
    first = first_singular(d)
    if not first or not first.endswith("ō"):
        return None
    bare = "".join(c for c in ud.normalize("NFD", pie_1sg) if c not in "́̀")
    if not bare.endswith("oh₂"):
        return None
    if any(x in pie_1sg for x in "-(") or " " in pie_1sg:
        return None
    ipa = pgmc_ipa.transcribe(first)
    if not ipa:
        return None
    return {
        "pie": pie_1sg, "pgmc": first, "pgmc_ipa": f"/{ipa}/", "cell": "1sg",
        "oe": "", "oe_ipa": "", "me": "", "me_ipa": "", "me_variants": 0, "pde": [],
        "pos": "verb", "gloss": gloss_of(d),
    }


def rank(c: dict) -> tuple:
    """How complete a chain is. Two Wiktionary records can share an etymon key.

    *hwalaz is both "whale" (with an Old English descendant) and "sheatfish" (with none), and
    they collide on (pie, pgmc). The richer record must win: letting the OE-less homograph
    overwrite the other silently emptied the 900/1400/final columns of whale, lithe and eke.
    """
    return (bool(c["oe_ipa"]), bool(c["me_ipa"]), len(c["pde"]) == 1, bool(c["oe"]))


def main() -> None:
    """Walk every Proto-Germanic record into a chain and write chains.json."""
    oe_ipa = load_ipa(K / "oe.jsonl")
    me_ipa = load_ipa(K / "me.jsonl")
    pie_1sg = load_pie_first_singulars()
    print(f"OE IPA keys: {len(oe_ipa)}   ME IPA keys: {len(me_ipa)}   "
          f"PIE 1sg cells: {len(pie_1sg)}", file=sys.stderr)

    stats: collections.Counter[str] = collections.Counter()
    by_etymon: dict[tuple[str, str], dict] = {}
    for line in open(K / "pgmc.jsonl", encoding="utf-8"):
        d = json.loads(line)
        stats["pgmc_records"] += 1
        pie = pie_parent(d)
        if not pie:
            continue
        stats["has_pie_parent"] += 1

        if d.get("pos") == "verb":
            # A verb is scored in the finite cells where PIE and Germanic name the SAME one — the
            # 3sg and the 1sg. They are not duplicates of each other: the 1sg is a negative control
            # on the *e > *i raising (*berō vs *biridi), and it is the only cell in which the WEAK
            # verbs are scorable at all, their 3sg ending being analogical (see finite_verb_1sg).
            got = False
            for cell, chain in (
                ("3sg", finite_verb(d, pie)),
                ("1sg", finite_verb_1sg(d, pie, pie_1sg.get(pie, ""))),
            ):
                if chain:
                    stats[f"verb ({cell} present)"] += 1
                    by_etymon[(chain["pie"], chain["pgmc"])] = chain
                    got = True
            if not got:
                stats["verb rejected (wrong cell)"] += 1
            continue

        base = {
            "pie": pie, "pgmc": d["word"],
            "pgmc_ipa": (d.get("sounds") or [{}])[0].get("ipa", ""),
            "oe": "", "oe_ipa": "", "me": "", "me_ipa": "", "me_variants": 0, "pde": [],
            "pos": d.get("pos", ""), "gloss": gloss_of(d),
        }
        oe_nodes = walk(d.get("descendants"), "ang")
        if not oe_nodes:
            # Stops at Proto-Germanic. Still a complete chain for the 200 checkpoint.
            stats["pgmc_only (no OE descendant)"] += 1
            cand = base
        else:
            stats["has_oe"] += 1
            # Per PGmc etymon, keep the single best OE branch: one that has IPA, whose ME
            # descendants have IPA, and which yields exactly one Modern English reflex.
            best = None
            for oe in oe_nodes:
                me_nodes = [m["word"] for m in walk([oe], "enm")]
                pde = sorted({e["word"] for e in walk([oe], "en")})
                me_hit = [m for m in me_nodes if m in me_ipa]
                branch = base | {
                    "oe": oe["word"], "oe_ipa": oe_ipa.get(oe["word"], ""),
                    "me": me_hit[0] if me_hit else (me_nodes[0] if me_nodes else ""),
                    "me_ipa": me_ipa.get(me_hit[0], "") if me_hit else "",
                    "me_variants": len(me_nodes), "pde": pde,
                }
                score = sum(rank(branch)[:3])
                if best is None or score > best[0]:
                    best = (score, branch)
            assert best is not None
            cand = best[1]

        # `>=`, not `>`: among equally complete homographs the LAST record wins, as it always
        # has. What the guard forbids is a DOWNGRADE — a chain that stops at Proto-Germanic
        # displacing one that runs all the way to Modern English.
        prev = by_etymon.get((pie, d["word"]))
        if prev is None or rank(cand) >= rank(prev):
            by_etymon[(pie, d["word"])] = cand

    # RINGE, folded in beside the Wiktionary chains — and he outranks them (Ringe > Kroonen >
    # Wiktionary). Only words we do NOT already have are added, so nothing existing is disturbed:
    # using him to OVERRIDE a preform we already carry is a bigger and separate question.
    #
    # A Ringe pair is scored at 200 and nowhere else. He gives the Germanic form, not an OE/ME/PDE
    # chain, so there is nothing to score the later columns against — exactly like a word that
    # died before Old English.
    ringe_file = CACHE / "ringe.json"
    if ringe_file.exists():
        have = {c["pgmc"] for c in by_etymon.values()}
        for p in json.load(open(ringe_file, encoding="utf-8")):
            if p["analogical"] or p["root"] or p["infinitive"] or p["weak_present"]:
                continue
            if p["pgmc"] in have:
                continue
            ipa = pgmc_ipa.transcribe(p["pgmc"])
            if not ipa:
                continue
            have.add(p["pgmc"])
            stats["from Ringe (new word, scored at 200)"] += 1
            by_etymon[(p["pie"], p["pgmc"])] = {
                "pie": p["pie"], "pgmc": p["pgmc"], "pgmc_ipa": f"/{ipa}/", "cell": "",
                "oe": "", "oe_ipa": "", "me": "", "me_ipa": "", "me_variants": 0, "pde": [],
                "pos": "", "gloss": "", "source": "Ringe",
            }
    else:
        print("no ringe.json — run tools/ringe.py first (Ringe pairs skipped)", file=sys.stderr)

    chains = list(by_etymon.values())
    json.dump(chains, open(CACHE / "chains.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"""
PGmc records            {stats['pgmc_records']}
  with a PIE parent     {stats['has_pie_parent']}
  reaching Old English  {stats['has_oe']}
  stopping at PGmc      {stats['pgmc_only (no OE descendant)']}
unique etymon chains    {len(chains)}
  PGmc has IPA          {sum(1 for c in chains if c['pgmc_ipa'])}
  OE has IPA            {sum(1 for c in chains if c['oe_ipa'])}
  ME has IPA            {sum(1 for c in chains if c['me_ipa'])}
  single PDE reflex     {sum(1 for c in chains if len(c['pde']) == 1)}
""", file=sys.stderr)


if __name__ == "__main__":
    main()
