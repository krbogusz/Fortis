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
`_build_derivations_csv` / `_build_csv_report` for the two generated reports below).

## Using it

- **Left panel**, headed by the **project switcher** — a dropdown (the title, with a
  ▾) of every project you can load: the built-in `default`, the bundled examples
  (e.g. *Latin → French*), and any folder you import. Mirrors the CLI's
  project/fallback model with two directories in the browser: a pristine shipped
  `default` and a user overlay — editing or loading a file always writes into the
  overlay, never the pristine copy. The 9 editable files (the eight inventories
  plus `settings.toml`) split into rows accordingly:
  - **Default** — files still falling back to the shipped default. Disappears once
    every file is overridden.
  - **Project** — files the current project supplies; each has a **×** to revert it
    to default.

  Switching projects replaces the overlay with that project's files (bundled
  examples are fetched from the app's static assets; the rest fall back to default,
  per-file, like the CLI). **Load file** overrides a single inventory file in the
  current project; **Load project** imports a local folder as a new project and adds
  it to the switcher; **Save** downloads the active file. `letters.csv` has a table
  view. The generated reports are in the right pane, not here.

- **Right panel** shows the results, with a view switcher: **Derivations** (the
  firing-rule trace, each word a card with per-card **Definition** and **Graph** toggles),
  **Rules** (`rule_firings.csv` — one row per rule with its fire count), **Tree** (the
  rule-feeding graph), **Matrix** (`derivation_table.csv` — one row per word, one column
  per rule), and, when the lexicon carries attested forms, **Accuracy** (the
  distance-to-target summary), **Errors** (which segments came out wrong, per stage),
  **Context** (the attested-form environments most associated with each error, per stage),
  and **Blame** (each wrong word attributed to the rule that produced it). A **Save** button
  downloads the active view's report (`derivations.csv` / `rule_firings.csv` /
  `derivation_table.csv` / `accuracy.csv` / `errors.csv` / `error_context.csv` / `blame.md`).
  Small projects re-run automatically on every edit; a
  large one (over 500 words or 100 rules) waits for a **Run project** button instead.

  Example projects are built by `scripts/build-engine.mjs` into
  `public/projects/<dir>/` (only the inventory files each one overrides) plus a
  `public/projects/index.json` manifest the picker reads — all gitignored,
  rebuilt on every `predev`/`prebuild`, so they never go stale against
  `../projects/`. Add a project by appending one row to `EXAMPLE_PROJECTS` in
  that script; nothing else changes. The picker fetches these relative to
  `document.baseURI`, so they resolve under a GitHub Pages project subpath.
- **Results** (right) — the sound-change trace: each firing rule grouped under its
  `time:` heading, with `before → after (change)` per step and the surface form.
  **Definition** toggles the rule bodies; **Graph** reveals, under each step whose rule
  spreads a tier or geometry node, its canonical autosegmental diagram. A progress bar in the header fills as the
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
