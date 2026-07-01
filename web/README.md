# Fortis — web app

A browser front-end for the Fortis phonology engine. It runs the **real Python
engine** (`../src/fortis`) in the browser via [Pyodide](https://pyodide.org) — no
server, no reimplementation. Edit the inventories on the left, and the derivations
re-run on the right.

## How it reflects the engine

There is no JavaScript copy of the engine to keep in sync. At `predev`/`prebuild`,
`scripts/build-engine.mjs` tars the repo's live `src/` and `projects/default/` into
`public/engine.tgz` and copies the version-locked Pyodide runtime into
`public/pyodide/` (both are gitignored — built fresh). The browser unpacks that
bundle, puts it on `sys.path`, imports `src.fortis`, and calls the engine directly
(`src/lib/engine.js`). So any change to the engine or the shipped inventories is
reflected on the next build — the glue only calls stable public functions
(`derive`, `render_syllabified`, `describe_change`, `render_autosegmental`,
`render_change`, `render_geometry_tree`, and `main.py`'s `_build_report` /
`_build_csv_report` for the two generated reports below).

## Using it

- **Inventories** (left): the eight editable files — `features.toml`, `letters.csv`,
  `diacritics.toml`, `sonorities.toml`, `syllable_parts.toml`, `tiers.toml`,
  `words.toml`, `rules.toml`. Edit in place, or **Load file** / **Load project** to
  swap in your own. `letters.csv` has a table view. After them, two read-only
  reports regenerate on every run: `output.md` (the same Markdown report the CLI's
  `--output` writes) and `output.csv` (one row per word, one column per rule, holding
  the resulting form wherever that rule fired) — `output.csv` gets the same table view
  as `letters.csv`.
- **Results** (right), two views:
  - **Historical** — the sound-change trace: each firing rule grouped under its
    `time:` heading, with `before → after (change)` per step and the surface form.
    **Definition** toggles the rule bodies.
  - **Autosegmental** — the tier/geometry picture: each rule as an association
    change (`│` kept · `╎` added — spread/dock · `╪` delinked), plus a per-segment
    feature-geometry tree for the input.

## Develop

```
npm install
npm run dev        # predev rebuilds the engine bundle, then starts Vite
npm run build      # prebuild rebuilds the bundle, then builds to dist/
npm run smoke      # headless check that the engine loads and derives
```

`npm run build-engine` rebuilds `public/engine.tgz` on its own — run it after
changing `../src` or `../projects/default` if the dev server is already up.
