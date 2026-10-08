"""Old English spelling → phonemic IPA, in Wiktionary's transcription conventions.

Wiktionary transcribes most Old English lemmas, but a few spellings that reach the lexicon through
a descendants tree have no transcription of their own. Old English spelling, as Wiktionary
normalises it, is close to phonemic: macrons mark long vowels and dots mark the palatals (ċ, ġ).
So those spellings can be transcribed by rule, and the rule can be checked against the lemmas
Wiktionary does transcribe (`_selftest`).

The output targets Wiktionary's conventions, so the caller puts it through the same
`normalise(...)` and `anglianise(...)` as every other Old English target:

  vowels       a ɑ, æ æ, e e, i i, o o, u u, y y; a macron adds ː
  diphthongs   ea æ͜ɑ, eo e͜o, ie i͜y, io i͜o; with a macron the length goes on the second half
  consonants   c k, ċ t͡ʃ, ċġ jj, cg ɡɡ, g ɡ, ġ j, h x, x ks, sċ ʃ, sc sk, þ ð θ, f f, s s
  stress       on the first syllable, or after the prefix ġe-

A spelling the rules cannot read is refused (None), not guessed. That covers an *e* written after
a palatal to mark it (sċeadu /ʃɑdu/, ġeoc /jok/), whose value varies word by word. Two things the
self-test cannot reach are left to the source: length a descendants tree leaves unmarked (*wom*
for wōm) and secondary stress in compounds.
"""

import re
import unicodedata as ud

# Longest first: the digraphs must be consumed before their parts.
UNITS = [
    ("ēa", "æ͜ɑː"), ("ēo", "e͜oː"), ("īe", "i͜yː"), ("īo", "i͜oː"),
    ("ea", "æ͜ɑ"), ("eo", "e͜o"), ("ie", "i͜y"), ("io", "i͜o"),
    ("ċġ", "jj"), ("cg", "ɡɡ"), ("sċ", "ʃ"), ("sc", "sk"),
    ("ā", "ɑː"), ("ǣ", "æː"), ("ē", "eː"), ("ī", "iː"), ("ō", "oː"), ("ū", "uː"), ("ȳ", "yː"),
    ("a", "ɑ"), ("æ", "æ"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u"), ("y", "y"),
    ("ċ", "t͡ʃ"), ("ġ", "j"), ("c", "k"), ("g", "ɡ"), ("h", "x"), ("x", "ks"),
    ("þ", "θ"), ("ð", "θ"), ("f", "f"), ("s", "s"),
    ("b", "b"), ("d", "d"), ("l", "l"), ("m", "m"), ("n", "n"), ("p", "p"), ("r", "r"),
    ("t", "t"), ("w", "w"),
]
VOWEL_START = set("ɑæeiouy")


def transcribe(word: str) -> str | None:
    """`snōd` -> `/snoːd/`. None if a letter is outside the inventory."""
    w = ud.normalize("NFC", word.strip().lower())
    if not w or not re.fullmatch(r"[a-zæþðāǣēīōūȳċġ]+", w):
        return None
    if re.search(r"(ċ|ġ|sċ)e[aoāō]", w):
        return None  # an *e* marking the palatal: its value varies word by word
    out: list[str] = []
    i = 0
    while i < len(w):
        for src, ipa in UNITS:
            if w.startswith(src, i):
                out.append(ipa)
                i += len(src)
                break
        else:
            return None
    nuclei = [n for n, seg in enumerate(out) if seg[0] in VOWEL_START]
    if len(nuclei) > 1:
        stressed = nuclei[1] if w.startswith("ġe") else nuclei[0]
        onset = stressed
        while onset > 0 and out[onset - 1][0] not in VOWEL_START:
            onset -= 1
        # The stress mark goes before the onset of the stressed syllable. A single consonant
        # between two vowels is the onset; of a cluster, only the last consonant is.
        if onset > 0 and stressed - onset > 1:
            onset = stressed - 1
        out.insert(onset, "ˈ")
    return "/" + "".join(out) + "/"


def _selftest() -> None:
    """Agreement with Wiktionary's own transcriptions, after the bootstrap's normalisation."""
    import json
    import sys
    from pathlib import Path

    sys.path[:0] = [str(Path(__file__).parent)]
    import build_gold as bg

    cache = Path(__file__).parent.parent / ".cache"
    chains = json.load(open(cache / "chains.json", encoding="utf-8"))
    pairs = sorted({(c["oe"], c["oe_ipa"]) for c in chains if c.get("oe") and c.get("oe_ipa")})
    same, differ = 0, []
    for oe, wikt in pairs:
        mine = transcribe(oe)
        if mine is None:
            continue
        a = bg.anglianise(bg.normalise(wikt, reconstructed=True))
        b = bg.anglianise(bg.normalise(mine, reconstructed=True))
        if a == b:
            same += 1
        else:
            differ.append(f"{oe}: wiktionary {a}, rule {b}")
    print(f"{same}/{same + len(differ)} agree")
    for line in differ:
        print("  ", line)


if __name__ == "__main__":
    _selftest()
