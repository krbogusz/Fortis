# Fortis — web app

A browser front-end for the Fortis phonology engine. It runs the same Python
engine as the CLI (`../src/fortis`), compiled to WebAssembly and executed
in-browser via [Pyodide](https://pyodide.org), rather than a separate
JavaScript reimplementation. Edit the inventories on the left, and the
derivations re-run on the right.

## How it reflects the engine

There is no JavaScript copy of the engine to keep in sync. At `predev`/`prebuild`,
`scripts/build-engine.mjs` tars the repo's live `src/` and `projects/default/` into
`public/engine.tgz` and copies the version-locked Pyodide runtime into
`public/pyodide/` (both are gitignored — built fresh). The browser unpacks that
bundle, puts it on `sys.path`, imports `src.fortis`, and calls the engine directly
(`src/lib/engine.js`). So any change to the engine or the shipped inventories is
reflected on the next build — the glue only calls stable public functions
(`derive`, `render_syllabified`, `describe_change`, and `main.py`'s
`_build_report` / `_build_csv_report` for the two generated reports below).

## Using it

- **Left panel**, titled by the loaded project's name (`default` until you load one).
  Mirrors the CLI's project/fallback model with two directories in the browser: a
  pristine shipped `default` and a user overlay — editing or loading a file always
  writes into the overlay, never the pristine copy. The 8 editable files split into
  rows accordingly:
  - **Default** — files still falling back to the shipped default. Disappears once
    every file is overridden.
  - **Project** — files the current project supplies; each has a **×** to revert it
    to default.
  - **Reports** — two read-only, regenerated-on-every-run files: `output.md` (the
    same report the CLI's `--output` writes) and `derivation_table.csv` (one row per
    word, one column per rule, holding the resulting form wherever that rule fired).
    Both get the same table view as `letters.csv`.

  **Example project…** (a picker, shown when any example is bundled) loads a
  built-in project — currently *Latin → French* — straight from the app's static
  assets, no local files needed. Selecting one replaces the overlay with that
  project's inventory files; the rest fall back to default (per-file, like the
  CLI). Picking the blank option reverts to the pristine default.
  **Load file** / **Load project** write into the overlay from *local* files
  (loading a project *replaces* it, not merges); **Save** downloads the active
  file's current content. `letters.csv` and `derivation_table.csv` have a table view.

  Example projects are built by `scripts/build-engine.mjs` into
  `public/projects/<dir>/` (only the inventory files each one overrides) plus a
  `public/projects/index.json` manifest the picker reads — all gitignored,
  rebuilt on every `predev`/`prebuild`, so they never go stale against
  `../projects/`. Add a project by appending one row to `EXAMPLE_PROJECTS` in
  that script; nothing else changes. The picker fetches these relative to
  `document.baseURI`, so they resolve under a GitHub Pages project subpath.
- **Results** (right) — the sound-change trace: each firing rule grouped under its
  `time:` heading, with `before → after (change)` per step and the surface form.
  **Definition** toggles the rule bodies. A progress bar in the header fills as the
  words derive (the run is driven in batches so the bar can update between them).

## Typography

All type lives on CSS custom properties in `src/app.css`, so every rule below
picks its role from the same handful of variables rather than a literal value.

**Size** (`--fs-*`, 4 tiers):

| Variable | Value | Used for |
|---|---|---|
| `--fs-emphasis` | 18px | The computed IPA forms: word headword, surface, each step's `before → after`, and its `(change)` annotation |
| `--fs-header` | 16px | Section/card titles: brand wordmark, panel `h2`, card `h3`, per-rule heading |
| `--fs-body` | 14px (also the page default) | Everything else: buttons, tabs, the editor/CSV-table content, and all **meta** text (see Color) |
| `--fs-label` | 10px | Uppercase group captions only: `DEFAULT`/`PROJECT`/`REPORTS` row labels |

**Family** (`--sans` / `--mono` / `--ipa`):

| Variable | Stack | Used for |
|---|---|---|
| `--sans` | system-ui, Segoe UI, Roboto | Default UI chrome (inherited by most elements) |
| `--mono` | ui-monospace, SF Mono, Consolas | Tabs, the editor, CSV tables, rule ids/definitions, time headers |
| `--ipa` | Gentium Plus, Charis SIL, Doulos SIL | Anything holding IPA text (`.ipa` utility class — the editor, results, CSV symbol column) |

**Weight**: 400 (default) for body text; 600 for headers/emphasis-adjacent labels
(`h2`, `h3`, rule-heading, CSV table headers); 700 for the two
heaviest-emphasis spots (word-ipa/surface, time-header).

**Color** (text only — `--text-h` / `--muted` / `--accent` / `--error`; see
`app.css` for the full background/border palette):

| Variable | Role | Used for |
|---|---|---|
| `--text-h` | Primary/heading strength | Headings, editor content, step forms, surface form |
| `--muted` | **Meta** — secondary/annotation text at `--fs-body` size, not a separate size tier | Tag, engine status, gloss, change annotation, time header, the uppercase group labels |
| `--accent` | Highlight (monochrome: near-black in light mode, near-white in dark) | Active/primary buttons app-wide; the progress-bar fill |
| `--error` | Errors only | Fatal banner, error card, remove-button hover |

Both palettes (light default in `:root`, dark under `prefers-color-scheme` or
an explicit `data-theme` from the Light/Dark/System toggle) remap the same
variable names, so no component-level CSS needs to know which theme is active.

## Develop

```
npm install
npm run dev        # predev rebuilds the engine bundle, then starts Vite
npm run build      # prebuild rebuilds the bundle, then builds to dist/
npm run smoke      # headless check that the engine loads and derives
```

`npm run build-engine` rebuilds `public/engine.tgz` on its own — run it after
changing `../src` or `../projects/default` if the dev server is already up.
