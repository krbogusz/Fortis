"""Extract PIE → Proto-Germanic pairs from Ringe, *From Proto-Indo-European to Proto-Germanic*.

Ringe sits at the TOP of this project's source hierarchy (Ringe > Kroonen > Wiktionary), so a pair
taken from him is better gold than anything the Wiktionary extracts can give — and it shows: the
words this yields land at ~60% exact with no curation at all, against ~50% for the Wiktionary
pool. He also states his derivations in a fixed citation format, which is what makes them
harvestable:

    PIE *dr̥ḱtós 'visible' (cf. Skt dr̥ṣṭás 'seen') > PGmc *turhtaz 'bright' (cf. OE torht);

Writes `ringe.json` into the cache, for `build_chains` to fold in beside the Wiktionary chains.

    PYTHONPATH=. python projects/pie_to_english/tools/ringe.py

The book is NOT in the repo (copyrighted; `sources/` is gitignored). Drop the PDF there and this
reads it; sound laws are facts and are encoded as rules, but no book text belongs in the tree.

THE PDF FIGHTS BACK, and every repair below is for damage that silently corrupts the pair:

* it splits digraphs from their diacritic — `*h₂stér-` comes out `*h 2stér-`, `ḱ` as `k ´`, `kʷ`
  as `k w`, and `*fadēr` as `*fad ēr`. Matching on whitespace therefore truncates a form at its
  first diacritic, which is how an earlier pass produced "PGmc *fad" and "PGmc *hund".
* Ringe separates examples with `;`. An unfenced match happily pairs the PIE of one example with
  the PGmc of the NEXT — it produced `*pah₂ > *wrōt` ('protect' > 'root'), 127 such phantoms in
  all. The span is fenced at `;`.
* a trailing `-` marks a STEM or ROOT (`*deḱs-`, `*hleuman-`). Stripping it as punctuation — which
  is the obvious thing to do — silently promotes every root to a word. It is kept, and it is what
  the root filter reads.
"""

import json
import os
import re
import sys
import unicodedata as ud
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, str(Path(__file__).parent))

CACHE = Path(os.environ.get("FORTIS_PIE_CACHE") or Path(__file__).parent.parent / ".cache")
PDF = (
    Path(__file__).parent.parent
    / "sources"
    / "From Proto-Indo-European to Proto-Germanic (Don Ringe).pdf"
)
OUT = CACHE / "ringe.json"

# Ringe's citation format. The `!` before PGmc is his own mark for a step that is NOT a sound
# change, and it is the most valuable thing in the file: he is telling us the pair is unreachable.
PAIR = re.compile(
    r"PIE \*([^‘’(,;~]{2,45}?)\s*[‘(]"   # the PIE form, up to its gloss
    r"([^;]{0,260}?)"                    # ...the gloss and cognates, NOT crossing a ';'
    r">\s*(!?)\s*PGmc \*([^‘’(,;~.]{1,30})"
)


def repair(text: str) -> str:
    """Undo the PDF's split digraphs, before any matching is done."""
    text = ud.normalize("NFC", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    text = re.sub(r"([kg])\s*wh", lambda m: m.group(1) + "ʷʰ", text)
    text = re.sub(r"([kg])\s*w(?=[aeiouāēīōūéóáíúḗṓ₁₂₃ʰ])", lambda m: m.group(1) + "ʷ", text)
    text = re.sub(r"([kg])\s*´", lambda m: {"k": "ḱ", "g": "ǵ"}[m.group(1)], text)
    text = re.sub(r"h\s*([123])", lambda m: "h" + "₁₂₃"[int(m.group(1)) - 1], text)
    return ud.normalize("NFC", text)


def form(s: str) -> str:
    """One cited form, with the PDF's stray spaces closed up. The trailing `-` is KEPT."""
    return ud.normalize("NFC", re.sub(r"\s+", "", s)).strip("*~ ")


def main() -> None:
    if not PDF.exists():
        sys.exit(f"{PDF} not found — the book is not redistributed; drop the PDF in sources/")
    import pypdf

    text = repair("\n".join(p.extract_text() or "" for p in pypdf.PdfReader(PDF).pages))

    seen: dict[tuple[str, str], dict] = {}
    for pie, _, bang, pgmc in PAIR.findall(text):
        pie, pgmc = form(pie), form(pgmc)
        if not pie or not pgmc:
            continue
        seen[(pie, pgmc)] = {
            "pie": pie,
            "pgmc": pgmc,
            # Ringe's `!`: a step that is NOT regular sound change (analogy, a morphological
            # rebuild, a semantic shift). Such a pair can never be derived, so it is not gold —
            # it is a WARNING, and it is kept in the file precisely so nobody hunts a rule for it.
            "analogical": bool(bang),
            "root": pie.endswith("-") or pgmc.endswith("-") or pie.startswith("-"),
            # A PGmc infinitive against a PIE finite form or root is the wrong-cell trap the verbs
            # already taught us: no sound change turns one cell of a paradigm into another.
            "infinitive": pgmc.endswith(("aną", "janą")),
            # The weak present. Ringe derives *bidiþi from *bedjidi with an explicit `>!` — its
            # *-iþi is levelled, not derived — so every *-þi present is out on his own authority,
            # even where he cites one in passing while illustrating some other change.
            "weak_present": pgmc.endswith("þi"),
        }
    pairs = list(seen.values())
    CACHE.mkdir(parents=True, exist_ok=True)
    json.dump(pairs, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    usable = [
        p for p in pairs
        if not (p["analogical"] or p["root"] or p["infinitive"] or p["weak_present"])
    ]
    print(f"""wrote {OUT}
  {len(pairs):4} distinct PIE -> PGmc derivations
  {sum(p['analogical'] for p in pairs):4} marked '>!' — NOT a sound change (analogy / rebuild)
  {sum(p['root'] for p in pairs):4} a stem or root, not a word
  {sum(p['infinitive'] for p in pairs):4} a PGmc infinitive (the wrong-cell trap)
  {sum(p['weak_present'] for p in pairs):4} a weak present (*-iþi is levelled — see build_chains)
  {len(usable):4} USABLE word-to-word pairs""", file=sys.stderr)


if __name__ == "__main__":
    main()
