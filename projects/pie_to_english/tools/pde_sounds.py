"""Build `pde_sounds.json`, the modern English pronunciations that `build_gold.py` reads.

For every modern reflex named in `chains.json`, this fetches the word's entries from kaikki.org's
per-word English pages and keeps, per entry, its part of speech and its transcriptions:

    {"father": [{"pos": "noun",
                 "sounds": [{"ipa": "/ˈfɑː.ðə/", "tags": ["Received-Pronunciation"]}]}]}

Only transcriptions tagged Received Pronunciation or UK, or untagged, are kept. `modern_ipa` in
`build_gold.py` falls back to a General American transcription when it finds no RP one, and that
fallback is how *tallow* once got GA /ˈtæloʊ/ in the RP column. Leaving the GA transcriptions out
of the file makes the fallback impossible without changing the bootstrap.

The pages are cached in `<cache>/en_pages/`, so a re-run fetches only what is missing.

Run:  python projects/pie_to_english/tools/pde_sounds.py
"""

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

CACHE = Path(os.environ.get("FORTIS_PIE_CACHE") or Path(__file__).parent.parent / ".cache")
PAGES = CACHE / "en_pages"
OUT = CACHE / "pde_sounds.json"
RP_TAGS = {"Received-Pronunciation", "UK"}


def fetch(word: str) -> list[dict]:
    """The kaikki entries for `word`, from the page cache or the network."""
    page = PAGES / f"{word}.jsonl"
    if not page.exists():
        q = urllib.parse.quote(word)
        url = f"https://kaikki.org/dictionary/English/meaning/{q[0]}/{q[:2]}/{q}.jsonl"
        try:
            data = urllib.request.urlopen(url, timeout=30).read()
        except OSError:
            data = b""  # no page: the word has no English entry, and that is cached too
        page.write_bytes(data)
        time.sleep(0.3)
    lines = page.read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


def main() -> None:
    """Write `pde_sounds.json` for every modern reflex in `chains.json`."""
    chains = json.load(open(CACHE / "chains.json", encoding="utf-8"))
    PAGES.mkdir(parents=True, exist_ok=True)
    words = sorted(
        {w for c in chains for w in (c.get("pde") or []) if w and " " not in w and w[0] != "-"}
    )
    sounds: dict[str, list[dict]] = {}
    for word in words:
        entries = []
        for entry in fetch(word):
            if entry.get("lang") != "English":
                continue
            kept = [
                {"ipa": s["ipa"], "tags": s.get("tags", [])}
                for s in entry.get("sounds", [])
                if s.get("ipa") and (not s.get("tags") or RP_TAGS & set(s["tags"]))
            ]
            entries.append({"pos": entry.get("pos"), "sounds": kept})
        if entries:
            sounds[word] = entries
    json.dump(sounds, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"wrote {OUT} — {len(sounds)} of {len(words)} reflex spellings have an English entry")


if __name__ == "__main__":
    main()
