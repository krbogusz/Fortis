"""Proto-West Germanic romanisation → IPA, for the 400 checkpoint.

Wiktionary gives IPA for only 8 of its 5578 Proto-West Germanic entries, so the column is
transcribed from the headword, as the 200 column is (`pgmc_ipa.py`). The romanisation is the
Proto-Germanic one with three differences in what the letters stand for, all taken from Ringe &
Taylor's sketch of PWGmc phonology (§4.1, PDF 120–121), which outranks Wiktionary's own IPA:

  d   a stop in ALL positions ("*/d/ was a stop in all positions"). Wiktionary's IPA still
      writes [ð] (idisi /ˈi.ði.si/); Ringe & Taylor do not.
  f   labiodental [f] ("*/f/ may already have become labiodental"), not PGmc [ɸ].
  hw, kw, gw   clusters, not labiovelars ("PWGmc had eliminated the PGmc labiovelars").
  ʀ   still *z: rhotacism is post-PWGmc (Ringe & Taylor, PDF 401), and Wiktionary keeps the
      letter apart from r.
  ē   the close ē₂ [eː]: stressed PGmc *ē₁ had become *ā (PDF 120), which is spelled ā.

b and g keep their PGmc allophones ("much as they had been in PGmc"), so `pgmc_ipa` handles them.

One convention differs from the 200 column's: a word-final geminate is two consonants (*full
/ˈfull/), not a long one. PGmc has almost none — its words end in an ending — but PWGmc has many
after apocope (*fulla > *full), and the engine and the Old English column write them as two.
"""
import re

import pgmc_ipa


def transcribe(word: str) -> str | None:
    """`miʀdu` -> `ˈmizdu`. None if a character is not in the inventory."""
    w = word.strip().lstrip("*").replace("ʀ", "z").replace("ē", "ē₂")
    ipa = pgmc_ipa.transcribe(w)
    if ipa is None:
        return None
    ipa = ipa.replace("ð", "d").replace("ɸ", "f")
    ipa = re.sub(r"([^ɑeiouɛɔ̃ː])ː$", r"\1\1", ipa)
    return re.sub(r"([xkɣ])ʷ", r"\1w", ipa)
