"""Emit a per-word PROVENANCE table: every word, and where each part of it came from.

The lexicon is built from several sources of very different authority, and a row can carry a
correction from any of them. `words.csv` shows only the result; this shows the paper trail:

  * the PIE input as **cited** by Wiktionary, and the input actually **used** — they differ
    whenever a correction fired;
  * WHICH correction fired, and why: `PREFORM_FIXES` (the input, from Ringe/Kroonen or from the
    attested Germanic read as independent evidence) or `ATTESTED_FIXES` (the Proto-Germanic
    TARGET, only ever with a citation);
  * the two admissions that are not corrections and must not be confused with them — a morpheme
    hyphen stripped from a complete form, and an accent **defaulted** to the initial syllable
    because the source gave none;
  * the attested Old English / Middle English / Modern English forms behind the later columns.

Run:  PYTHONPATH=. python projects/pie_to_english/tools/provenance.py
"""

import csv
import json
import os
import sys
import unicodedata as ud
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, str(Path(__file__).parent))

import build_gold as BG  # noqa: E402
from pie_ipa import has_accent  # noqa: E402

CACHE = Path(os.environ.get("FORTIS_PIE_CACHE") or Path(__file__).parent.parent / ".cache")
OUT = Path(__file__).parent.parent / "sources" / "provenance.csv"

# Where each column of the lexicon comes from when nothing has corrected it.
WIKTIONARY = "Wiktionary (kaikki)"


def ident(row: dict) -> str:
    """The word's id, recomputed exactly as build_gold mints it (a slug of the gloss)."""
    import re
    s = re.sub(r"[^\w\s-]", "", ud.normalize("NFC", row["gloss"]).strip().lower())
    return re.sub(r"[\s_-]+", "-", s).strip("-") or row["word"]


def pie_provenance(row: dict) -> tuple[str, str]:
    """(source, note) for the PIE input — the one column that several authorities can touch."""
    pgmc = row["_pgmc"]
    if pgmc in BG.PREFORM_FIXES:
        return (
            "PREFORM_FIXES (Ringe / Kroonen, or the attested Germanic as independent evidence)",
            f"input replaced: *{row['_cited']} -> *{BG.PREFORM_FIXES[pgmc]}",
        )
    notes = []
    if "-" in row["_cited"]:
        notes.append("morpheme hyphens stripped (a complete form, not a bare root)")
    if not has_accent(row["_cited"].replace("-", "")):
        notes.append(
            "ACCENT DEFAULTED to the initial syllable — the source gives none. Proto-Germanic "
            "fixes the stress initially, so the PIE accent reaches the 200 form only through "
            "Verner's Law; where no Verner-eligible fricative exists it cannot matter"
        )
    return WIKTIONARY, "; ".join(notes)


def main() -> None:
    rows = json.load(open(CACHE / "gold_rows.json", encoding="utf-8"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([
            "id", "gloss", "category", "frequency", "frequency_source",
            "pie_cited", "pie_used", "pie_source", "pie_note",
            "pgmc_headword", "target_200", "target_200_source", "target_200_note",
            "oe_form", "target_900", "me_form", "target_1400", "modern", "target_final",
            "targets_source",
        ])
        for r in rows:
            src, note = pie_provenance(r)
            fixed = r["_pgmc"] in BG.ATTESTED_FIXES
            w.writerow([
                ident(r), r["gloss"],
                (f"verb.pres.{r['_cell']}" if r["_pos"] == "verb" else r["_pos"]),
                r["frequency"],
                "hermitdave/FrequencyWords en_50k (MIT; OpenSubtitles)"
                if r["frequency"] > 1 else "no match — defaulted to 1",
                f"*{r['_cited']}", f"*{r['_pie']}", src, note,
                f"*{r['_pgmc']}", r["200"],
                "ATTESTED_FIXES (a cited reconstruction beats Wiktionary's)" if fixed
                else WIKTIONARY,
                f"target corrected to {BG.ATTESTED_FIXES[r['_pgmc']]}" if fixed else "",
                r["_oe"], r["900"], r["_me"], r["1400"],
                " ".join(r["_variants"].split()) or "", r["final"],
                WIKTIONARY,
            ])
    print(f"wrote {OUT} — {len(rows)} words", file=sys.stderr)


if __name__ == "__main__":
    main()
