"""Transliterate Wiktionary's PIE notation into the IPA the engine reads.

Wiktionary writes PIE in the traditional Indo-Europeanist orthography (*wĺ̥kʷos, *ph₂tḗr);
The cascade reads IPA with the default inventory's letters and diacritics
(ˈwl̩kʷos, pħˈteːr). This maps one to the other.

Two things make it more than a lookup table:

* The acute is ambiguous in NFD. `ḱ` (palatovelar) and `é` (accented vowel) both decompose
  to base + U+0301, so the mark is read by its base: on k/g it palatalises, everywhere else
  it marks the PIE accent.
* Wiktionary marks the accent on the *nucleus*; the engine wants `ˈ` before the accented
  syllable's *onset*. Where the onset starts is a phonotactic question (*oḱtṓw* is okʲ.ˈtoːw,
  not o.ˈkʲtoːw), so we hand the segmented form to the engine's own syllabifier rather than
  guessing at a maximal onset.
"""

import re
import unicodedata as ud

ACUTE, MACRON, RING = "́", "̄", "̥"

# Base letters, before any combining mark is applied.
CONSONANTS = {
    "p": "p", "b": "b", "t": "t", "d": "d", "k": "k", "g": "g",
    "s": "s", "m": "m", "n": "n", "l": "l", "r": "r",
    "w": "w", "y": "j", "j": "j",
    "h₁": "χ", "h₂": "ħ", "h₃": "ʁʷ",
    # H is the cover symbol for a laryngeal whose colour is unrecoverable (*suHnús). Read it
    # as h₁, the one that does not colour an adjacent *e — the choice that adds no claim the
    # source does not make.
    "H": "χ",
}
VOWELS = {"e": "e", "o": "o", "a": "a", "i": "i", "u": "u"}
# Under the ring. The LARYNGEALS belong here too: a vocalised laryngeal IS a nucleus — that is
# what "vocalised" means — and writing it as one lets it do what any nucleus does, including bear
# the accent. Without it, a zero-grade form like Kroonen's *nh₂-s-eh₂- 'nose' has no vowel at all
# in its first syllable, so there is nothing for the acute to sit on; the accent was forced onto
# the suffix, Verner then voiced the *s that the attested *nasō shows voiceless, and the word could
# not be got right at any price. The ring says which syllable carries the beat.
SYLLABIC = {
    "l": "l̩", "r": "r̩", "m": "m̩", "n": "n̩",
    "h₁": "χ̩", "h₂": "ħ̩", "h₃": "ʁʷ̩", "H": "χ̩",
}


class PieError(ValueError):
    """A PIE form this transliterator will not guess at."""


def _units(form: str):
    """Split an NFD PIE string into (base, marks, modifiers) units."""
    # An optional segment — *(s)ker- — is a claim about two variants, not one form. Take the
    # variant without it, which is the one the descendants tree is hung on.
    form = re.sub(r"[(⁽].*?[)⁾]", "", form)
    text = ud.normalize("NFD", form)
    i, out = 0, []
    while i < len(text):
        ch = text[i]
        i += 1
        if ch in "*-. ":
            continue
        # laryngeals: h + subscript digit
        if ch == "h" and i < len(text) and text[i] in "₁₂₃":
            ch, i = "h" + text[i], i + 1
        marks, mods = "", ""
        while i < len(text) and ud.combining(text[i]):
            marks += text[i]
            i += 1
        while i < len(text) and text[i] in "ʰʷ":
            mods += text[i]
            i += 1
            while i < len(text) and ud.combining(text[i]):
                marks += text[i]
                i += 1
        out.append((ch, marks, mods))
    return out


def has_accent(form: str) -> bool:
    """Does *form* carry a PIE accent?

    The acute is ambiguous in NFD: on `k`/`g` it makes the PALATOVELAR (ḱ, ǵ), and only elsewhere
    does it mark the accent — the same test :func:`to_tokens` makes.
    """
    return any(ACUTE in marks and base not in ("k", "g") for base, marks, _ in _units(form))


def accent_first_nucleus(form: str) -> str:
    """Put the acute on *form*'s first nucleus. Returns it unchanged if it has no nucleus.

    A nucleus is a vowel OR a ringed syllabic consonant (`l̥ r̥ m̥ n̥`, and a vocalised laryngeal) —
    the same set :func:`to_tokens` will read as one, so the accent lands where the engine will
    look for it. Written by re-emitting the parsed units rather than by patching the string,
    because a naive "insert after the first vowel letter" would put the acute on the `h` of a
    laryngeal, or miss a syllabic consonant entirely.
    """
    out, done = [], False
    for base, marks, mods in _units(form):
        nucleus = base in VOWELS or (RING in marks and base in SYLLABIC)
        if nucleus and not done:
            marks, done = marks + ACUTE, True
        out.append(base + marks + mods)
    return ud.normalize("NFC", "".join(out))


def to_tokens(form: str) -> tuple[list[str], int]:
    """Return (one IPA string per segment, index of the accented segment).

    Raises PieError on anything outside the notation — an unmapped letter, or a form with
    no accent at all (the accent is what places the stress, and Verner's Law reads it).
    """
    tokens: list[str] = []
    accent = -1
    for base, marks, mods in _units(form):
        stressed = ACUTE in marks and base not in ("k", "g")
        if base in VOWELS:
            tok = VOWELS[base] + ("ː" if MACRON in marks else "")
        elif base in CONSONANTS:
            tok = CONSONANTS[base]
            if RING in marks and base in SYLLABIC:
                tok = SYLLABIC[base]
            if ACUTE in marks and base in ("k", "g"):
                tok += "ʲ"
            if "ʷ" in mods:
                tok += "ʷ"
            if "ʰ" in mods:
                # PIE's voiced aspirates are breathy: bʰ dʰ gʰ → bʱ dʱ gʱ (ʱ, not ʰ).
                tok += "ʱ" if base in ("b", "d", "g") else "ʰ"
        else:
            raise PieError(f"unmapped letter {base!r} in {form!r}")
        if stressed:
            if accent >= 0:
                raise PieError(f"two accents in {form!r}")
            accent = len(tokens)
        tokens.append(tok)
    if accent < 0:
        raise PieError(f"no accent in {form!r}")
    return tokens, accent


def to_ipa(form: str, project) -> str:
    """Transliterate *form*, placing ˈ before the onset of its accented syllable."""
    from fortis.application.segmentation import string_to_sequence
    from fortis.application.syllabifying import syllabify

    tokens, accent = to_tokens(form)
    bare = "".join(tokens)
    word = string_to_sequence(bare, project)
    if len(word.segments) != len(tokens):
        raise PieError(f"{form!r} → {bare!r}: {len(tokens)} tokens vs "
                       f"{len(word.segments)} segments")
    bounds = syllabify(
        [segment.bundle for segment in word.segments],
        project.sonorities, project.syllable_parts, -2000, project.letters,
    )
    onset = max((b for b in bounds if b <= accent), default=0)
    return "".join(("ˈ" if i == onset else "") + t for i, t in enumerate(tokens))
