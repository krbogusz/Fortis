"""Proto-Germanic romanisation → IPA, in Wiktionary's transcription conventions.

Needed because Wiktionary gives IPA for the *lemma* only (`sounds[]`), while the inflected cells
we want live in `forms[]` as bare romanisation: the 3sg present of *beraną is written `biridi` and
no pronunciation is attached to it. To score a verb at Proto-Germanic we have to transcribe that
cell ourselves.

The output deliberately targets **Wiktionary's** conventions, not the engine's, so that it can be
checked against the 4843 lemma pronunciations that Wiktionary does give (see `_selftest`). The
caller then puts the result through the same `normalise(..., reconstructed=True)` that every other
reconstructed column already goes through, which is what converts it to engine notation. Any other
arrangement would leave the verb targets spelled differently from the noun targets and the miss
would look like phonology.

The allophony is the part that cannot be guessed, and it is read off the attested data:

  b   [b] word-initially, after a nasal, and geminate;  [β] elsewhere   (ab /ˈɑβ/)
  d   [d] word-initially, after a nasal, and geminate;  [ð] elsewhere   (gudą /ˈɣu.ðɑ̃/)
  g   [ɣ] EVERYWHERE except after a nasal and geminate, where it is [ɡ] — including
      word-initially, which is where it differs from b and d (gans /ɣɑns/, not */ɡɑns/)
  f   [ɸ] throughout;  þ [θ];  h [x] throughout, including word-initially (hinder /ˈxin.der/)

So the 3sg of *beraną is *biridi /ˈbi.ri.ði/ — with a fricative, because the *d is intervocalic.
"""

import re
import unicodedata as ud

# Longest-first: the digraphs must be consumed before their parts.
DIGRAPHS = [
    ("ē₂", "eː"), ("ē2", "eː"),
    ("ai", "ɑi̯"), ("au", "ɑu̯"), ("eu", "eu̯"), ("iu", "iu̯"),
    ("hw", "xʷ"), ("kw", "kʷ"), ("gw", "ɣʷ"),
]

VOWELS = {
    "a": "ɑ", "e": "e", "i": "i", "o": "o", "u": "u",
    "ā": "ɑː", "ē": "ɛː", "ī": "iː", "ō": "ɔː", "ū": "uː",
    "ą": "ɑ̃", "į": "ĩ", "ų": "ũ", "ǫ": "ɔ̃",
    "ą̄": "ɑ̃ː", "į̄": "ĩː", "ų̄": "ũː", "ǭ": "ɔ̃ː",
    "ē₂": "eː",
}

CONSONANTS = {
    "p": "p", "t": "t", "k": "k",
    "f": "ɸ", "þ": "θ", "s": "s", "h": "x",
    "z": "z", "m": "m", "n": "n", "l": "l", "r": "r", "w": "w", "j": "j",
}

NASALS = {"m", "n"}
IPA_VOWELS = set("ɑeiouɛɔ")


# What hardens each voiced obstruent to a stop, counted over every unambiguous occurrence in the
# 4843 lemmas rather than assumed. A geminate always hardens; beyond that they differ:
#
#   b   after a nasal (m 23:1) and word-initially (340:0)
#   d   after a nasal (159:4), after l (57:3), after z (14:0), and word-initially (184:0)
#   g   after a nasal (105:3) ONLY — a fricative even word-initially (ɣ 246:6), which is why
#       *gans is /ɣɑns/ and not */ɡɑns/
#
# Note what the count refutes: d after r is the FRICATIVE (ð 47 : d 13). The /ˈxɑrduz/ that
# prompted this check is Wiktionary's own minority spelling, not the pattern.
HARDENS_AFTER = {"b": NASALS, "d": NASALS | {"l", "z"}, "g": NASALS}
HARD_INITIAL = {"b", "d"}
FRICATIVE = {"b": "β", "d": "ð", "g": "ɣ"}
STOP = {"b": "b", "d": "d", "g": "ɡ"}


def _plosive_or_fricative(letter: str, prev: str | None, nxt: str | None) -> str:
    """The b/d/g allophony. `prev`/`nxt` are the ROMANISED neighbours."""
    hard = (
        prev == letter
        or nxt == letter
        or (prev is None and letter in HARD_INITIAL)
        or (prev in HARDENS_AFTER[letter] if prev else False)
    )
    return STOP[letter] if hard else FRICATIVE[letter]


def transcribe(word: str) -> str | None:
    """`biridi` -> `ˈbiriði`. None if a character is not in the inventory."""
    w = ud.normalize("NFC", word.strip().lstrip("*").lower())
    if not w or not re.fullmatch(r"[a-zþāēīōūąįųǭǫē₂2-]+", w):
        return None

    # Split into romanised units, digraphs first.
    units: list[str] = []
    i = 0
    while i < len(w):
        for src, _ in DIGRAPHS:
            if w.startswith(src, i):
                units.append(src)
                i += len(src)
                break
        else:
            units.append(w[i])
            i += 1

    digraph = dict(DIGRAPHS)
    out: list[str] = []
    for n, u in enumerate(units):
        if u in digraph:
            out.append(digraph[u])
        elif u in VOWELS:
            out.append(VOWELS[u])
        elif u in CONSONANTS:
            out.append(CONSONANTS[u])
        elif u in ("b", "d", "g"):
            prev = units[n - 1] if n else None
            nxt = units[n + 1] if n + 1 < len(units) else None
            out.append(_plosive_or_fricative(u, prev, nxt))
        else:
            return None

    # A nasal before *h is lost, and the vowel before it nasalises and lengthens:
    # fanhaną /ˈɸɑ̃ːxɑnɑ̃/, þinhaną /ˈθĩːxɑnɑ̃/. This is the Germanic nasal loss before a
    # fricative, and it must run BEFORE the velar assimilation below or the n becomes an ŋ and
    # survives.
    for n in range(len(out) - 2, 0, -1):
        if out[n] in ("n", "m") and out[n + 1] in ("x", "xʷ") and out[n - 1] in IPA_VOWELS:
            out[n - 1] = ud.normalize("NFC", out[n - 1] + "̃") + "ː"
            del out[n]

    # A nasal assimilates to a following velar: bringaną /ˈbriŋgɑnɑ̃/, þankijaną /ˈθɑŋkijɑnɑ̃/.
    for n, seg in enumerate(out):
        if seg == "n" and n + 1 < len(out) and out[n + 1] in ("k", "ɡ", "ɣ", "kʷ", "xʷ", "x"):
            out[n] = "ŋ"

    # *w is non-syllabic u̯ when it closes a syllable — that is, before a consonant:
    # niwjaz /ˈniu̯jɑz/, awjō /ˈɑu̯jɔː/. It stays a glide before a vowel (strawiþi) and in the
    # geminate, whose second half is the onset of the next syllable (blewwaną /ˈblew.wɑ.nɑ̃/).
    for n, seg in enumerate(out):
        if seg == "w" and n and out[n - 1][0] in IPA_VOWELS:
            nxt = out[n + 1] if n + 1 < len(out) else None
            if nxt != "w" and (nxt is None or nxt[0] not in IPA_VOWELS):
                out[n] = "u̯"

    # A geminate is written doubled between vowels (gawissaz /ɣɑˈwis.sɑz/) but as length
    # word-finally, where there is no syllable break to carry the second half (inn /ˈinː/).
    if len(out) >= 2 and out[-1] == out[-2] and out[-1] in CONSONANTS.values():
        out[-2:] = [out[-1] + "ː"]

    ipa = "".join(out)
    # Proto-Germanic stress is fixed on the first syllable. Wiktionary writes it only where there
    # is more than one syllable to choose between, so a monosyllable gets no mark. A diphthong is
    # one syllable: its second half is written non-syllabic (ɑi̯), so it must not be counted.
    nfd = ud.normalize("NFD", ipa)
    syllables = sum(
        1
        for n, c in enumerate(nfd)
        if c in IPA_VOWELS and not (n + 1 < len(nfd) and nfd[n + 1] == "̯")
    )
    if syllables > 1:
        ipa = "ˈ" + ipa
    return ipa
