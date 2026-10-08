#!/usr/bin/env bash
# Run the Python CLI and the Rust binaries on the shipped projects and diff everything they write:
# every report of a full run (also with --autosegmental and --single), the induction scoreboard,
# and the inducer's rules and trace.
# usage: rust/parity.sh [project ...]        (default: all five projects)
# The inducer takes Python about 90 minutes on latin_to_french and pie_to_english, so it runs on
# those two only with PARITY_INDUCE_ALL=1.
# Exits non-zero if any file differs. Output lands in rust/target/parity/{py,rs}/.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${PARITY_OUT:-$ROOT/rust/target/parity}"
PROJECTS=("$@")
[ ${#PROJECTS[@]} -eq 0 ] && PROJECTS=(default halle_vaux_wolfe latin_to_french pie_to_english spe)
command -v cargo >/dev/null || . "$HOME/.cargo/env"
cargo build --release --quiet --manifest-path "$ROOT/rust/Cargo.toml" || exit 1
BIN="$ROOT/rust/target/release/fortis"
PY="$ROOT/.venv/bin/python"

# rule_dependencies.html lists its edges in Python set-iteration order, which varies with the hash
# seed, so that file is compared with its edges sorted.
normalize_html() {
  "$PY" -I - "$1" <<'EOF'
import json, re, sys
text = open(sys.argv[1], encoding="utf-8").read()
m = re.search(r"const D=(.*), bands=", text)
data = json.loads(m.group(1))
data["edges"].sort(key=lambda e: (e["from"], e["to"]))
sys.stdout.write(text[: m.start(1)] + json.dumps(data) + text[m.end(1):])
EOF
}

compare_dirs() {  # compare_dirs <label> <python dir> <rust dir>
  local label=$1 a=$2 b=$3 bad=0
  for f in $( (ls "$a"; ls "$b") | sort -u ); do
    if [ ! -f "$a/$f" ] || [ ! -f "$b/$f" ]; then
      echo "  $label: $f written by only one side"; bad=1; continue
    fi
    if [ "$f" = rule_dependencies.html ]; then
      cmp -s <(normalize_html "$a/$f") <(normalize_html "$b/$f") || { echo "  $label: $f differs"; bad=1; }
    else
      cmp -s "$a/$f" "$b/$f" || { echo "  $label: $f differs"; bad=1; }
    fi
  done
  [ $bad -eq 0 ] && echo "  $label: $(ls "$a" | wc -l | tr -d ' ') reports identical"
  return $bad
}

fail=0
cd "$ROOT"
for p in "${PROJECTS[@]}"; do
  for flags in "" "--autosegmental"; do
    tag="$p${flags:+ $flags}"
    dir="$p${flags//-/_}"
    rm -rf "$OUT/py/$dir" "$OUT/rs/$dir"
    mkdir -p "$OUT/py/$dir" "$OUT/rs/$dir"
    "$PY" -m src.fortis.main --project "projects/$p" $flags --output "$OUT/py/$dir/derivations.csv" 2>/dev/null
    "$BIN" --project "projects/$p" $flags --output "$OUT/rs/$dir/derivations.csv" 2>/dev/null
    compare_dirs "$tag" "$OUT/py/$dir" "$OUT/rs/$dir" || fail=1
  done
  # --single: the first three words, the last one, and a doubled seed that is in no lexicon.
  words=$("$PY" -c "
import sys
from pathlib import Path
from src.fortis.loaders.project import load_project
words = list(load_project(Path('projects/$p')).unwrap().words.values())
for w in (*words[:3], words[-1]):
    print(w.id)
print(words[0].seed.ipa * 2)
")
  i=0
  while IFS= read -r word; do
    i=$((i + 1))
    dir="${p}_single_$i"
    rm -rf "$OUT/py/$dir" "$OUT/rs/$dir"
    mkdir -p "$OUT/py/$dir" "$OUT/rs/$dir"
    "$PY" -m src.fortis.main --project "projects/$p" --single "$word" --output "$OUT/py/$dir/derivations.csv" 2>/dev/null
    "$BIN" --project "projects/$p" --single "$word" --output "$OUT/rs/$dir/derivations.csv" 2>/dev/null
    compare_dirs "$p --single $word" "$OUT/py/$dir" "$OUT/rs/$dir" || fail=1
  done <<< "$words"
  # The induction scoreboard, and the inducer itself.
  dir="${p}_induction"
  rm -rf "$OUT/py/$dir" "$OUT/rs/$dir"
  mkdir -p "$OUT/py/$dir" "$OUT/rs/$dir"
  "$PY" -m src.fortis.induction.scoreboard --project "projects/$p" --output "$OUT/py/$dir/scoreboard.md" > "$OUT/py/$dir/scoreboard.stdout" 2>/dev/null
  "$ROOT/rust/target/release/fortis-scoreboard" --project "projects/$p" --output "$OUT/rs/$dir/scoreboard.md" > "$OUT/rs/$dir/scoreboard.stdout" 2>/dev/null
  if [ "${PARITY_INDUCE_ALL:-0}" = 1 ] || { [ "$p" != latin_to_french ] && [ "$p" != pie_to_english ]; }; then
    "$PY" -m src.fortis.induction.main --project "projects/$p" --out "$OUT/py/$dir/induced_rules.toml" --report "$OUT/py/$dir/induction.md" > "$OUT/py/$dir/induce.stdout" 2>/dev/null
    "$ROOT/rust/target/release/fortis-induce" --project "projects/$p" --out "$OUT/rs/$dir/induced_rules.toml" --report "$OUT/rs/$dir/induction.md" > "$OUT/rs/$dir/induce.stdout" 2>/dev/null
  fi
  compare_dirs "$p induction" "$OUT/py/$dir" "$OUT/rs/$dir" || fail=1
done
exit $fail
