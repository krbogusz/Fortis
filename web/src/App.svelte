<script>
  import { onMount } from "svelte";
  import {
    initEngine,
    listFiles,
    readFile,
    writeFile,
    removeFile,
    resetOverlay,
    fileStatus,
    prepareRun,
    deriveBatch,
    finalizeRun,
    analysisStep,
    runSingle,
    listExampleProjects,
    loadExampleProject,
  } from "./lib/engine.js";
  import CsvTable from "./lib/CsvTable.svelte";
  import DependencyTree from "./lib/DependencyTree.svelte";
  import { marked } from "marked";
  import userGuideMd from "../../docs/user_guide.md?raw";
  import defaultSystemMd from "../../docs/default_system.md?raw";
  import acknowledgementsMd from "../../docs/acknowledgements.md?raw";

  let ready = $state(false);
  let status = $state("Starting…");
  let initError = $state(null);

  let files = $state([]); // editable inventory filenames
  let fileSource = $state({}); // filename -> "default" | "project"
  let active = $state(null); // active inventory filename in the left pane
  let content = $state(""); // viewer content for the active file
  let busy = $state(false); // a derivation run is in flight
  let progress = $state(0); // derivation progress, 0..1 (only meaningful while busy)
  let progressText = $state(""); // "213 / 448" during a run
  let runToken = 0; // bumped for each new run/load; a run whose token is stale aborts (supersession)

  let openDefs = $state({}); // per-card: index → whether that card's rule definitions are shown
  let openAuto = $state({}); // per-card: index → whether that card's autosegmental diagrams are shown
  let result = $state(null); // { derivations } | { error }
  let accuracy = $state(null); // accuracy summary from the last run, or null when there's no target
  let errors = $state(null); // Errors analysis: per-stage confusions, or null when all exact
  let errorContext = $state(null); // Error-context analysis: per-stage per-segment autopsy, or null
  let blame = $state(null); // per-word blame, or null when all exact
  let warnings = $state([]); // syllabification-fallback warnings from the last run
  let unfiredRules = $state([]); // word-scoped rules naming a word absent from the lexicon: {rule, word}
  let timing = $state(null); // {words, rules, deriveMs, analysisMs} from the last run (accuracy folded into analysis)
  let matrixCsv = $state(""); // derivation_matrix.csv content, for the right-pane Matrix view
  let dependencies = $state(null); // rule feeding-graph layout, for the right-pane Tree view
  let rulesCsv = $state(""); // rule_firings.csv content, for the right-pane Rules view
  let resultView = $state("derivations"); // right-pane view: derivations | rules | matrix | accuracy | errors | errorContext | blame | warnings

  // A project with more than this many words OR rules is too costly to re-run on
  // every edit; it waits for the "Run project" button instead of auto-running.
  const AUTO_RUN_WORDS = 500;
  const AUTO_RUN_RULES = 100;
  let bigProject = $state(false); // project exceeds the auto-run limit — shows the manual Run button
  let dirty = $state(false); // overlay edited since the last committed run (a big project needs re-running)
  let pendingSize = $state(null); // { words, rules } of the project awaiting a run
  // The Run button is disabled when the shown results are current; the status dot goes amber
  // ("Modified — re-run") when a big project has been edited since its last run.
  const current = $derived(!dirty && result?.derivations != null);
  const modified = $derived(ready && bigProject && dirty && result?.derivations != null);
  let single = $state(null); // last single-word run: {found, ipa, gloss, derivations, accuracy, …} | {error} | null
  let singleInput = $state(""); // the Single tab's input-bar text
  let singleBusy = $state(false); // a single-word derivation is in flight
  let singleDefs = $state(false); // whether the single derivation card shows its rule definitions
  let singleAuto = $state(false); // whether the single derivation card shows its autosegmental diagrams

  let fileInput; // single-file <input>
  let projectInput; // multi-file (folder) <input>
  let examples = $state([]); // bundled example projects from the static manifest
  let imported = $state([]); // imported (local-folder) projects: { id, label, files }
  let picked = $state(""); // id of the selected project ("" = the built-in default)

  let docsOpen = $state(false); // the Docs floating window
  let docsTab = $state("guide"); // active docs tab: "guide" | "system"
  let docsBodyEl = $state(null); // the scrollable docs pane, for in-page ToC jumps

  // GitHub-style heading slug, matching the anchors the docs' Table of Contents links to.
  const slugify = (text) =>
    text.toLowerCase().trim().replace(/[^\w\s-]/g, "").replace(/\s+/g, "-");
  // marked doesn't emit heading ids, so the ToC's #anchors have no targets. Inject an id
  // (the slug of each heading's text) into every rendered <h1>…<h6> so the jumps resolve.
  const addHeadingIds = (html) =>
    html.replace(/<(h[1-6])>(.*?)<\/\1>/gs, (_m, tag, inner) => {
      const text = inner.replace(/<[^>]+>/g, ""); // plain text for the slug
      return `<${tag} id="${slugify(text)}">${inner}</${tag}>`;
    });
  const docsMd = { guide: userGuideMd, system: defaultSystemMd, acknowledgements: acknowledgementsMd };
  const docsHtml = $derived(addHeadingIds(marked.parse(docsMd[docsTab] ?? userGuideMd)));

  // Intercept ToC clicks: scroll the target heading into view within the docs pane (a plain
  // #hash would jump the whole SPA, not this scroll container).
  function docsAnchorClick(event) {
    const anchor = event.target.closest?.('a[href^="#"]');
    if (!anchor || !docsBodyEl) return;
    const id = decodeURIComponent(anchor.getAttribute("href").slice(1));
    const target = id && docsBodyEl.querySelector(`#${CSS.escape(id)}`);
    if (target) {
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  let debounceTimer = null;

  // "absent" files (in neither overlay nor default — e.g. words.csv when the project uses
  // words.toml) are hidden, so the two lexicon formats never both show a tab.
  const defaultFiles = $derived(files.filter((f) => fileSource[f] === "default"));
  const projectFiles = $derived(files.filter((f) => fileSource[f] === "project"));

  // Hover tooltips: what each inventory file is.
  const FILE_HELP = {
    "features.toml": "The feature system — every phonological feature, its tier and values",
    "letters.csv": "The letter/segment inventory — IPA symbols and their feature bundles",
    "diacritics.toml": "Diacritics — marks that modify a segment (nasalization, length, …)",
    "diacritics.csv": "Diacritics (CSV) — marks that modify a segment (nasalization, length, …)",
    "sonorities.toml": "The sonority scale used for syllabification",
    "sonorities.csv": "The sonority scale used for syllabification (CSV)",
    "syllable_parts.toml": "Onset / nucleus / coda constraints for syllabification",
    "tiers.toml": "Autosegmental tiers (tone, stress) and their behaviour",
    "words.toml": "The lexicon — input IPA plus attested target and stage forms",
    "words.csv": "The lexicon (CSV) — input IPA plus attested target and stage forms",
    "rules.toml": "The ordered, time-keyed sound-change rules",
    "rules.csv": "The ordered, time-keyed sound-change rules (CSV)",
    "settings.toml": "Tunable analysis parameters (accuracy, error analysis, induction)",
  };

  // Everything the project switcher lists: the built-in default, the bundled
  // examples, and any locally-imported folders (added by loadProject).
  const projects = $derived([
    { id: "", label: "default" },
    ...examples.map((e) => ({ id: e.dir, label: e.label || e.dir, kind: "example", entry: e })),
    ...imported.map((p) => ({ id: p.id, label: p.label, kind: "imported", files: p.files })),
  ]);

  let theme = $state(localStorage.getItem("theme") ?? "system"); // "light" | "dark" | "system"
  $effect(() => {
    if (theme === "system") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = theme;
    localStorage.setItem("theme", theme);
  });
  // A single button cycles the theme, like the psyguide switcher: system → dark → light → …
  const nextTheme = { system: "dark", dark: "light", light: "system" };
  const cycleTheme = () => (theme = nextTheme[theme] ?? "system");

  // Adjustable split between the left (inventories) and right (results) panes: the left pane's
  // width as a percent, dragged via the divider and clamped so neither pane collapses.
  let panelsEl; // the flex row that holds both panes, for the drag's coordinate frame
  let splitPct = $state(clampSplit(Number(localStorage.getItem("splitPct"))));
  $effect(() => localStorage.setItem("splitPct", String(splitPct)));
  // Mobile only: which stacked panel is collapsed to just its header so the other gets
  // full height. "" = split, "left" = editor collapsed, "right" = results collapsed.
  let collapsed = $state("");

  function clampSplit(pct) {
    return Number.isFinite(pct) && pct > 0 ? Math.min(80, Math.max(20, pct)) : 50;
  }

  function startResize(event) {
    if (window.matchMedia("(max-width: 960px)").matches) return; // stacked: no horizontal drag
    event.preventDefault();
    const rect = panelsEl.getBoundingClientRect();
    const onMove = (e) => {
      splitPct = clampSplit(((e.clientX - rect.left) / rect.width) * 100);
    };
    const onUp = () => {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
    };
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none"; // no text selection mid-drag
  }

  function keyResize(event) {
    if (event.key === "ArrowLeft") splitPct = clampSplit(splitPct - 2);
    else if (event.key === "ArrowRight") splitPct = clampSplit(splitPct + 2);
    else if (event.key === "Home") splitPct = 50;
    else return;
    event.preventDefault();
  }

  onMount(async () => {
    try {
      await initEngine((m) => (status = m));
      files = listFiles();
      examples = await listExampleProjects();
      ready = true;
      refreshStatus();
      selectFile(files[0]);
      await rerun();
    } catch (e) {
      initError = e?.message ?? String(e);
      status = "Failed to load engine";
    }
  });

  function refreshStatus() {
    fileSource = fileStatus();
  }

  function selectFile(name) {
    active = name;
    content = readFile(name);
  }

  // After a project switch, keep `active` on a visible file: if it went absent (e.g. the
  // project uses words.csv but `active` was words.toml), hop to the sibling format (words or
  // rules) if it is visible, else fall back to the first visible file.
  const DUAL_FORMAT = { // each file's sibling in the other (toml/csv) format
    "words.toml": "words.csv", "words.csv": "words.toml",
    "rules.toml": "rules.csv", "rules.csv": "rules.toml",
    "diacritics.toml": "diacritics.csv", "diacritics.csv": "diacritics.toml",
    "sonorities.toml": "sonorities.csv", "sonorities.csv": "sonorities.toml",
  };
  function visibleActive() {
    if (fileSource[active] && fileSource[active] !== "absent") return active;
    const sibling = DUAL_FORMAT[active];
    if (sibling && fileSource[sibling] && fileSource[sibling] !== "absent") return sibling;
    return files.find((f) => fileSource[f] && fileSource[f] !== "absent") ?? files[0];
  }

  // Yield to the browser so a state change (the progress bar) actually paints
  // before the next synchronous Pyodide batch blocks the main thread again.
  const paint = () => new Promise((r) => setTimeout(r, 0));

  async function rerun(force = false) {
    if (!ready) return;
    const myToken = ++runToken; // claim this run; a newer run bumps the token and supersedes us
    try {
      // Probe the project first (synchronous — no await yet, so an in-flight run can't slip in
      // between the token bump and this session reset). A too-large project bails here WITHOUT
      // touching the current results, so the pane keeps showing the last run.
      const prep = prepareRun();
      if (prep.error) {
        result = { error: prep.error };
        bigProject = false;
        dirty = false;
        return;
      }
      bigProject = prep.words > AUTO_RUN_WORDS || prep.rules > AUTO_RUN_RULES;
      if (bigProject && !force) {
        // Too large to auto-run: wait for the manual Run button. Leave the current results (and
        // the `dirty` flag the edit set) in place — the pane keeps showing the last run, the
        // top-bar button flags "modified" until the user re-runs.
        pendingSize = { words: prep.words, rules: prep.rules };
        if (!result) resultView = "single"; // opening a large project defaults to the Single tab
        return;
      }
      // Committing to a run: clear the previous output and paint the bar before the first batch.
      dirty = false; // the results about to appear are current
      busy = true;
      progress = 0;
      progressText = "";
      result = null; // clear the previous results so the pane doesn't show stale output under the bar
      accuracy = null; // and the previous accuracy summary
      warnings = []; // and the previous warnings
      unfiredRules = []; // and the previous never-fire flags
      matrixCsv = ""; // and the previous derivation table
    dependencies = null; // and the previous feeding graph
      rulesCsv = ""; // and the previous rule-firings table
      timing = null; // and the previous run's timing
      openDefs = {}; // reset per-card definition toggles (indices map to new words after a run)
      openAuto = {}; // and the per-card autosegmental toggles
      await paint(); // paint the (updated) left pane + cleared right pane before the first batch blocks
      if (myToken !== runToken) return; // superseded while painting — a newer run owns the session now
      const total = prep.words;
      const acc = [];
      // Drive the run in slices, painting the bar between them. Batch size is
      // adapted from the measured cost of the previous batch to keep each one a
      // short, roughly fixed slice of wall-clock time (so the bar stays smooth
      // and the thread never freezes for long, whatever the machine's speed).
      let batch = 4;
      const runStart = performance.now();
      for (let i = 0; i < total; ) {
        const t0 = performance.now();
        const slice = deriveBatch(i, batch);
        acc.push(...slice);
        i += slice.length || batch; // guard against an empty slice stalling the loop
        progress = total ? i / total : 1;
        progressText = `${Math.min(i, total)} / ${total}`;
        const perWord = (performance.now() - t0) / Math.max(1, slice.length);
        batch = Math.min(32, Math.max(1, Math.round(120 / Math.max(perWord, 1))));
        if (i < total) {
          await paint();
          // If a newer run started, stop before the next batch: it has reset the
          // Python session (prepare_run), so continuing would derive against it.
          if (myToken !== runToken) return;
        }
      }
      const deriveMs = performance.now() - runStart;
      // Analysis phase — a fresh progress bar, driven one step at a time so it repaints
      // between the (individually slow) report/analysis chunks.
      const plan = finalizeRun();
      let fin = plan.result;
      if (plan.steps?.length) {
        progress = 0; // the derivation bar empties; the analysis bar fills from scratch
        for (let k = 0; k < plan.steps.length; k++) {
          if (myToken !== runToken) return; // a newer run took over
          progress = k / plan.steps.length;
          progressText = `analysing… ${plan.steps[k]}`;
          await paint();
          const step = analysisStep();
          if (step?.result) fin = step.result;
        }
        progress = 1;
      }
      timing = { words: total, rules: prep.rules, deriveMs, analysisMs: fin?.analysisMs ?? 0 };
      accuracy = fin?.accuracy ?? null;
      if (!accuracy && resultView === "accuracy") resultView = "derivations"; // no target ⇒ leave the (now hidden) tab
      errors = fin?.errors ?? null;
      if (!errors && resultView === "errors") resultView = "derivations"; // all exact ⇒ leave the tab
      errorContext = fin?.errorContext ?? null;
      if (!errorContext && resultView === "errorContext") resultView = "derivations"; // none ⇒ leave the tab
      blame = fin?.blame ?? null;
      if (!blame && resultView === "blame") resultView = "derivations"; // all exact ⇒ leave the tab
      warnings = fin?.warnings ?? [];
      unfiredRules = fin?.unfiredRules ?? [];
      if (!warnings.length && !unfiredRules.length && resultView === "warnings")
        resultView = "derivations"; // none ⇒ leave the tab
      matrixCsv = readFile("reports/derivation_matrix.csv"); // for the Matrix view
      rulesCsv = readFile("reports/rule_firings.csv"); // for the Rules view
      dependencies = fin?.dependencies ?? null; // for the Tree view
      if (resultView === "single") resultView = "derivations"; // a full run shows the whole lexicon
      result = { derivations: acc };
    } catch (e) {
      if (myToken === runToken) result = { error: [e?.message ?? String(e)] };
    } finally {
      if (myToken === runToken) busy = false; // only the latest run clears the busy flag
    }
  }

  function onEdit() {
    writeFile(active, content);
    refreshStatus();
    dirty = true; // overlay changed — a big project now needs re-running (flags "modified" at once)
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => rerun(), 400); // auto-run only if under the size limit
  }

  // Comment-muting overlay for the .toml editor: a highlight <pre> mirrors the textarea's
  // text (comment lines dimmed) behind its transparent-text caret. The two are kept in
  // metric + scroll lock-step so the coloured mirror sits exactly under what you type.
  let taEl = $state(null); // the textarea
  let hlEl = $state(null); // the highlight mirror
  // Split a TOML line into its code and trailing-comment halves at the first `#` that is NOT
  // inside a string — TOML uses `#` as the word-boundary marker inside rule definitions
  // (e.g. `definition = "a -> e / _ #"`), which must not be dimmed as a comment.
  function splitComment(line) {
    let inString = null; // '"' or "'" while inside a string, else null
    for (let i = 0; i < line.length; i++) {
      const ch = line[i];
      if (inString) {
        if (ch === "\\" && inString === '"') i++; // skip an escaped char in a basic string
        else if (ch === inString) inString = null;
      } else if (ch === '"' || ch === "'") {
        inString = ch;
      } else if (ch === "#") {
        return { code: line.slice(0, i), comment: line.slice(i) };
      }
    }
    return { code: line, comment: "" };
  }
  const editorLines = $derived(content.split("\n").map(splitComment));

  // Render a confusion cell's examples. Spaces inside each label are made non-breaking so a
  // single example ("acheter: a.ʃa.t̪e/aʃ.t̪e") never wraps mid-way; the "  • " separator's
  // two leading spaces are non-breaking too, so a line break can fall only after a bullet —
  // between examples, never inside one.
  const NBSP = String.fromCharCode(0xA0); // non-breaking space
  const exampleList = (examples) =>
    examples.map((e) => e.replaceAll(" ", NBSP)).join(NBSP + NBSP + "• ");

  function syncScroll() {
    if (hlEl && taEl) {
      hlEl.scrollTop = taEl.scrollTop;
      hlEl.scrollLeft = taEl.scrollLeft;
    }
  }

  // The editable CSV table edits `.csv` inventories (letters.csv, a CSV words file) in place;
  // it hands back the whole re-serialized file, which we save and re-run like any text edit.
  function onCsvEdit(csv) {
    content = csv;
    onEdit();
  }

  function runProject() {
    rerun(true); // force a run regardless of size (the Run project button)
  }

  // Derive just the word in the input bar, independent of the full-run pipeline (it neither
  // reads nor writes the batched session, so it's safe to run without touching `result`).
  async function runSingleWord() {
    const word = singleInput.trim();
    if (!ready || singleBusy || !word) return;
    singleBusy = true;
    single = null; // clear the previous single result so the pane doesn't show stale output
    await paint(); // paint "deriving…" before the synchronous Pyodide call blocks the thread
    try {
      single = runSingle(word);
    } catch (e) {
      single = { error: [e?.message ?? String(e)] };
    } finally {
      singleBusy = false;
    }
  }

  async function removeFileTab(name, ev) {
    ev.stopPropagation();
    removeFile(name);
    refreshStatus();
    dirty = true; // removing a file mutates the overlay — a big project needs re-running
    if (active === name) content = readFile(name); // now shows the default content
    await rerun();
  }

  function download(filename, text) {
    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }

  function saveActiveFile() {
    download(active, content);
  }

  // The report file each right-pane view is generated from (basenames; the reports
  // live in the overlay's reports/ subfolder — saveResult() reads from there but keeps
  // the download named by the basename).
  const RESULT_FILE = {
    derivations: "derivations.csv",
    matrix: "derivation_matrix.csv",
    rules: "rule_firings.csv",
    accuracy: "accuracy.csv",
    errors: "errors.csv",
    errorContext: "error_context.csv",
    blame: "blame.csv",
    warnings: "warnings.md",
  };

  function saveResult() {
    const name = RESULT_FILE[resultView];
    if (name) download(name, readFile("reports/" + name)); // read from reports/, download by basename
  }

  function matchFile(name) {
    const base = name.split("/").pop().toLowerCase();
    return files.find((f) => f.toLowerCase() === base);
  }

  async function loadSingleFile(ev) {
    const file = ev.target.files?.[0];
    if (!file) return;
    const target = matchFile(file.name);
    if (!target) {
      alert(
        `"${file.name}" is not one of the inventory files:\n${files.join(", ")}`,
      );
      ev.target.value = "";
      return;
    }
    const text = await file.text();
    writeFile(target, text);
    refreshStatus();
    dirty = true; // importing a file mutates the overlay — a big project needs re-running
    selectFile(target);
    await rerun();
    ev.target.value = "";
  }

  // Switch to a project from the title switcher: the built-in default (id ""),
  // a bundled example (fetched from static assets), or a locally-imported folder
  // (its cached files re-written into the overlay). Replaces the overlay wholesale.
  async function selectProject(id) {
    const proj = projects.find((p) => p.id === id);
    if (!proj) return;
    picked = id;
    // Reflect the choice and clear the right pane at once, before any (network) load.
    const myToken = ++runToken; // a second pick supersedes this one
    busy = true;
    progress = 0;
    progressText = "";
    result = null;
    single = null; // a fresh project — drop the previous project's single-word result
    singleInput = "";
    warnings = []; // and its syllabification-fallback + never-fire warnings
    unfiredRules = [];
    dirty = false; // a freshly-loaded project hasn't been edited yet
    await paint();
    if (myToken !== runToken) return; // superseded while painting
    try {
      if (proj.kind === "example") {
        await loadExampleProject(proj.entry); // resets the overlay, then fetches its files
      } else {
        resetOverlay(); // default or imported: start from the pristine base
        if (proj.kind === "imported") {
          for (const [name, text] of Object.entries(proj.files)) writeFile(name, text);
        }
      }
      if (myToken !== runToken) return; // superseded during the fetch
      refreshStatus();
      selectFile(visibleActive());
      await rerun(); // bumps runToken and takes over the busy flag from here
    } catch (e) {
      if (myToken === runToken) {
        alert(`Could not load ${proj.label}: ${e?.message ?? e}`);
        picked = "";
        resetOverlay();
        refreshStatus();
        selectFile(visibleActive());
      }
    } finally {
      if (myToken === runToken) busy = false; // if rerun ran it owns busy; else clear on our error
    }
  }

  // Import a local folder as a project: cache its inventory files, add it to the
  // switcher (replacing an earlier import of the same folder), and select it.
  async function loadProject(ev) {
    const incoming = Array.from(ev.target.files ?? []);
    ev.target.value = "";
    const collected = {};
    const skipped = [];
    for (const file of incoming) {
      const target = matchFile(file.name);
      if (target) collected[target] = await file.text();
      else skipped.push(file.name);
    }
    if (!Object.keys(collected).length) {
      alert("No matching inventory files found in the selection.");
      return;
    }
    const folder = incoming[0]?.webkitRelativePath?.split("/")[0] || "imported";
    const id = `imported:${folder}`;
    imported = [...imported.filter((p) => p.id !== id), { id, label: folder, files: collected }];
    await selectProject(id);
    if (skipped.length) alert(`Ignored (not inventory files): ${skipped.join(", ")}`);
  }
</script>

<svelte:window onkeydown={(e) => e.key === "Escape" && (docsOpen = false)} />

<div class="app">
  <header class="bar">
    <div class="bar-left">
      <div class="brand">
        <strong>Fortis</strong>
        <span class="tag">phonology engine</span>
      </div>
      <button
        class="docs-btn"
        title="Open the notation and engine documentation"
        onclick={() => (docsOpen = true)}>Docs</button
      >
    </div>
    <div class="state">
      {#if initError}
        <span class="err-dot"></span> {status}
      {:else if !ready}
        <span class="spinner"></span> {status}
      {:else if modified}
        <span class="mod-dot"></span> <span class="mod-text">Modified</span>
      {:else}
        <span class="ok-dot"></span> Engine ready
      {/if}
      {#if ready && bigProject}
        <button
          class="run-top"
          disabled={busy || current}
          aria-label="Run project"
          title={current
            ? "Results are up to date"
            : "Run project — derive the whole lexicon and regenerate the reports"}
          onclick={runProject}
        >
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" aria-hidden="true">
            <path d="M8 5v14l11-7z" />
          </svg>
        </button>
      {/if}
      <button
        class="theme-toggle"
        onclick={cycleTheme}
        aria-label="Toggle theme"
        title={theme === "system"
          ? "Theme: system (click for dark)"
          : theme === "dark"
            ? "Theme: dark (click for light)"
            : "Theme: light (click for system)"}
      >
        {#if theme === "system"}
          <!-- Auto / system (eclipse) -->
          <svg viewBox="0 0 32 32" width="18" height="18" fill="currentColor" stroke="none" aria-hidden="true">
            <path d="M13,7c-0.6,0-1-0.4-1-1V5c0-0.6,0.4-1,1-1s1,0.4,1,1v1C14,6.6,13.6,7,13,7z" />
            <path d="M5.9,9.9c-0.3,0-0.5-0.1-0.7-0.3L3.1,7.5c-0.4-0.4-0.4-1,0-1.4s1-0.4,1.4,0l2.1,2.1c0.4,0.4,0.4,1,0,1.4C6.4,9.8,6.2,9.9,5.9,9.9z" />
            <path d="M3,17H2c-0.6,0-1-0.4-1-1s0.4-1,1-1h1c0.6,0,1,0.4,1,1S3.6,17,3,17z" />
            <path d="M3.8,26.2c-0.3,0-0.5-0.1-0.7-0.3c-0.4-0.4-0.4-1,0-1.4l2.1-2.1c0.4-0.4,1-0.4,1.4,0s0.4,1,0,1.4l-2.1,2.1C4.3,26.1,4.1,26.2,3.8,26.2z" />
            <path d="M13,28c-0.6,0-1-0.4-1-1v-1c0-0.6,0.4-1,1-1s1,0.4,1,1v1C14,27.6,13.6,28,13,28z" />
            <path d="M22,25c-5,0-9-4-9-9s4-9,9-9s9,4,9,9S27,25,22,25z" />
            <path d="M11,16c0-3.1,1.3-5.9,3.3-7.9C13.9,8,13.5,8,13,8c-4.4,0-8,3.6-8,8s3.6,8,8,8c0.5,0,0.9,0,1.3-0.1C12.3,21.9,11,19.1,11,16z" />
          </svg>
        {:else if theme === "dark"}
          <!-- Dark (moon) -->
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
          </svg>
        {:else}
          <!-- Light (sun) -->
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="12" cy="12" r="5" />
            <line x1="12" y1="1" x2="12" y2="3" />
            <line x1="12" y1="21" x2="12" y2="23" />
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
            <line x1="1" y1="12" x2="3" y2="12" />
            <line x1="21" y1="12" x2="23" y2="12" />
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
          </svg>
        {/if}
      </button>
    </div>
  </header>

  {#if initError}
    <div class="fatal">
      <h2>Could not load the engine</h2>
      <pre>{initError}</pre>
    </div>
  {/if}

  <main
    class="panels"
    class:disabled={!ready}
    bind:this={panelsEl}
    style="--split-left: {splitPct}%"
  >
    <!-- LEFT: inventories -->
    <section class="panel left" class:is-collapsed={collapsed === "left"}>
      <div class="panel-head">
        <div class="project-picker">
          <select
            class="project-select"
            disabled={!ready}
            bind:value={picked}
            onchange={() => selectProject(picked)}
            title="Switch or load a project"
          >
            {#each projects as p}
              <option value={p.id}>{p.label}</option>
            {/each}
          </select>
          <span class="caret" aria-hidden="true">▾</span>
        </div>
        <div class="actions">
          <button
            disabled={!ready}
            title="Override one inventory file in this project from a local file"
            onclick={() => fileInput.click()}>Load file</button
          >
          <button
            disabled={!ready}
            title="Import a local folder as a new project"
            onclick={() => projectInput.click()}>Load project</button
          >
          <button disabled={!ready} title="Download the active file" onclick={saveActiveFile}
            >Save</button
          >
        </div>
      </div>

      <div class="file-selection">
      {#if defaultFiles.length}
        <div class="file-group">
          <div class="file-group-label">Default</div>
          <div class="tabs">
            {#each defaultFiles as f}
              <button
                class="tab"
                class:active={f === active}
                disabled={!ready}
                title={FILE_HELP[f]}
                onclick={() => selectFile(f)}>{f}</button
              >
            {/each}
          </div>
        </div>
      {/if}

      {#if projectFiles.length}
        <div class="file-group">
          <div class="file-group-label">Project</div>
          <div class="tabs">
          {#each projectFiles as f}
            <span class="tab-wrap">
              <button
                class="tab"
                class:active={f === active}
                disabled={!ready}
                title={FILE_HELP[f]}
                onclick={() => selectFile(f)}>{f}</button
              >
              <button
                class="tab-remove"
                disabled={!ready}
                title="Revert to default"
                onclick={(ev) => removeFileTab(f, ev)}>×</button
              >
            </span>
          {/each}
          </div>
        </div>
      {/if}
      </div>

      <div class="editor-area">
      {#if active?.endsWith(".csv")}
        <CsvTable {content} onchange={onCsvEdit} />
      {:else if active?.endsWith(".toml")}
        <!-- Highlight overlay: the mirror colours comment lines; the textarea on top holds
             the caret and real text (rendered transparent so only the mirror shows). -->
        <div class="editor-wrap">
          <pre class="editor editor-hl ipa" aria-hidden="true" bind:this={hlEl}>{#each editorLines as l, i}{#if i > 0}{"\n"}{/if}{l.code}<span
                class="comment">{l.comment}</span>{/each}</pre>
          <textarea
            class="editor editor-input ipa"
            spellcheck="false"
            disabled={!ready}
            bind:value={content}
            oninput={onEdit}
            onscroll={syncScroll}
            bind:this={taEl}
          ></textarea>
        </div>
      {:else}
        <textarea
          class="editor ipa"
          spellcheck="false"
          disabled={!ready}
          bind:value={content}
          oninput={onEdit}
        ></textarea>
      {/if}
      </div>

      <input
        bind:this={fileInput}
        type="file"
        hidden
        onchange={loadSingleFile}
      />
      <input
        bind:this={projectInput}
        type="file"
        webkitdirectory
        multiple
        hidden
        onchange={loadProject}
      />
    </section>

    <!-- A focusable separator is a valid ARIA window-splitter widget; the lint rules
         treat `separator` as non-interactive, which does not fit this use. -->
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
    <div
      class="divider"
      role="separator"
      aria-orientation="vertical"
      aria-label="Resize panels — drag, or use arrow keys"
      aria-valuenow={Math.round(splitPct)}
      aria-valuemin="20"
      aria-valuemax="80"
      tabindex="0"
      onpointerdown={startResize}
      onkeydown={keyResize}
      ondblclick={() => (splitPct = 50)}
    >
      <!-- Mobile only (see the max-width: 960px block): collapse one stacked panel so the
           other fills the screen. ▴ = editor full, ▾ = results full; tap again to restore. -->
      <button
        type="button"
        class="collapse-btn"
        class:active={collapsed === "right"}
        title={collapsed === "right" ? "Restore split" : "Editor full height"}
        aria-label="Give the editor full height"
        onclick={(e) => (e.stopPropagation(), (collapsed = collapsed === "right" ? "" : "right"))}
        onpointerdown={(e) => e.stopPropagation()}>▴</button
      >
      <button
        type="button"
        class="collapse-btn"
        class:active={collapsed === "left"}
        title={collapsed === "left" ? "Restore split" : "Results full height"}
        aria-label="Give the results full height"
        onclick={(e) => (e.stopPropagation(), (collapsed = collapsed === "left" ? "" : "left"))}
        onpointerdown={(e) => e.stopPropagation()}>▾</button
      >
    </div>

    <!-- RIGHT: results -->
    <section class="panel right" class:is-collapsed={collapsed === "right"}>
      <div class="panel-head results-head">
        <div class="head-row">
          <div class="head-title">
            <h2>Results</h2>
            {#if warnings.length || unfiredRules.length}
              {@const warnTotal = warnings.length + unfiredRules.length}
              <button
                class="warn-tab"
                class:active={resultView === "warnings"}
                onclick={() => (resultView = "warnings")}
                title="Rules that never fire, and words that fell back to sonority syllabification"
                >⚠ {warnTotal} warning{warnTotal === 1 ? "" : "s"}</button
              >
            {/if}
          </div>
          <div class="actions">
            {#if result?.derivations}
              <div class="view-tabs">
                <button
                  class:active={resultView === "derivations"}
                  title="Each word's step-by-step derivation from input to surface form"
                  onclick={() => (resultView = "derivations")}>Derivations</button
                >
                <button
                  class:active={resultView === "rules"}
                  title="Each rule's firings: the words it matched (before → after) and the distinct segment changes it made (rule_firings.csv)"
                  onclick={() => (resultView = "rules")}>Rules</button
                >
                <button
                  class:active={resultView === "tree"}
                  title="dependence tree — which rule's output segment feeds which rule's input (rule_dependencies.html)"
                  onclick={() => (resultView = "tree")}>Tree</button
                >
                <button
                  class:active={resultView === "matrix"}
                  title="Every word's form at each stage, in one wide matrix (derivation_matrix.csv)"
                  onclick={() => (resultView = "matrix")}>Matrix</button
                >
                {#if accuracy}
                  <button
                    class:active={resultView === "accuracy"}
                    title="Exact-match accuracy and edit distance vs the attested targets"
                    onclick={() => (resultView = "accuracy")}>Accuracy</button
                  >
                {/if}
                {#if errors}
                  <button
                    class:active={resultView === "errors"}
                    onclick={() => (resultView = "errors")}
                    title="Which segments came out wrong, per attested stage and the final"
                    >Errors</button
                  >
                {/if}
                {#if errorContext}
                  <button
                    class:active={resultView === "errorContext"}
                    onclick={() => (resultView = "errorContext")}
                    title="The attested-form environments most associated with each error, per stage"
                    >Context</button
                  >
                {/if}
                {#if blame}
                  <button
                    class:active={resultView === "blame"}
                    onclick={() => (resultView = "blame")}
                    title="Each wrong word attributed to the rule that produced it"
                    >Blame</button
                  >
                {/if}
                <button
                  class:active={resultView === "single"}
                  onclick={() => (resultView = "single")}
                  title="Derive one word on demand — its full derivation, accuracy, errors, and blame"
                  >Single</button
                >
              </div>
              {#if resultView !== "single"}
                <button
                  class="save-result"
                  disabled={!ready}
                  title="Download this view's report file"
                  onclick={saveResult}>Save</button
                >
              {/if}
            {/if}
          </div>
        </div>
      </div>

      <!-- The last run's headline (words · rules · per-phase timing), shared by every result
           view including the Table tab. -->
      {#snippet timingLine()}
        {#if timing}
          <p class="muted timing-line">
            {timing.words} words · {timing.rules} rules · derivation
            {(timing.deriveMs / 1000).toFixed(1)}s · analysis
            {(timing.analysisMs / 1000).toFixed(1)}s
          </p>
        {/if}
      {/snippet}

      <div class="result-area">
      {#if busy}
        <div class="results">
          <div class="run-prompt">
            <span class="progress big" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow={Math.round(progress * 100)}>
              <span class="progress-fill" style="width:{Math.round(progress * 100)}%"></span>
            </span>
            <p class="muted progress-text">{progressText || "running…"}</p>
          </div>
        </div>
      {:else if resultView === "tree" && dependencies}
        <DependencyTree data={dependencies} />
      {:else if resultView === "matrix" && matrixCsv}
        <div class="table-timing">{@render timingLine()}</div>
        <CsvTable content={matrixCsv} />
      {:else if resultView === "rules" && rulesCsv}
        <div class="table-timing">{@render timingLine()}</div>
        <CsvTable content={rulesCsv} wideColumns={["changes", "matched"]} italicColumn="sporadic" />
      {:else}
      <div class="results">
        <!-- The firing-rule trace of one word, as a borderless table (rule · t · before → after
             · change) — used by the Derivation tab. `showDefs` reveals each rule's
             definition under its name (the Derivation tab's Definition toggle). -->
        {#snippet traceSteps(steps, showDefs, showAuto)}
          {@const hasTime = steps.some((s) => s.time != null)}
          <!-- The trace table hugs its content (nowrap form columns), so on a narrow
               screen it can exceed the card. Contain that overflow to a per-card scroll
               region: the card itself stays pane-width (no page-level scroll, no blank
               space beside narrower cards) and only the wide table scrolls within it. -->
          <div class="trace-scroll">
          <table class="report-misses blame-traj">
            <thead>
              <tr><th>rule</th>{#if hasTime}<th>t</th>{/if}<th>before</th><th>after</th><th>change</th></tr>
            </thead>
            <tbody>
              {#each steps as s}
                <tr>
                  <td class="st-rule" class:sporadic={s.sporadic}>{#if s.heading}{s.heading}{/if}</td>
                  {#if hasTime}<td class="st-time">{s.time ?? ""}</td>{/if}
                  <td class="form">{s.before}</td>
                  <td class="form">{s.after}</td>
                  <td class="form">{s.change ?? ""}</td>
                </tr>
                {#if showDefs && s.heading && s.definition}
                  <tr><td colspan={hasTime ? 5 : 4} class="def-cell">{s.definition}</td></tr>
                {/if}
                {#if showAuto && s.autosegmental?.length}
                  <tr><td colspan={hasTime ? 5 : 4} class="auto-cell">
                    {#each s.autosegmental as [, diagram]}
                      <pre class="diagram">{diagram}</pre>
                    {/each}
                  </td></tr>
                {/if}
              {/each}
            </tbody>
          </table>
          </div>
        {/snippet}
        <!-- Shared by the Errors and Error context views. -->
        {#snippet confusionTable(confs)}
          <table class="report-summary">
            <thead>
              <tr><th>expected</th><th>got</th><th>count</th><th>kind</th><th>examples (gloss: derived vs. attested)</th></tr>
            </thead>
            <tbody>
              {#each confs as c}
                <tr>
                  <td class="form">{c.expected ?? "∅"}</td>
                  <td class="form">{c.got ?? "∅"}</td>
                  <td>{c.count}</td>
                  <td>{c.kind}</td>
                  <td class="form">{exampleList(c.examples)}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        {/snippet}
        {#snippet autopsyBlock(autopsy)}
          {#each autopsy as a}
            <details class="report-detail">
              <summary>
                <span class="form tgt">{a.segment}</span>
                <span class="muted">wrong {a.errors}/{a.total} · support ≥{a.supportFloor}</span>
              </summary>
              {#if a.predictors.length}
                <table class="report-misses">
                  <thead>
                    <tr>
                      <th title="The attested-form environment tested as a predictor of this error (e.g. right=n)">environment</th>
                      <th title="Phi coefficient: chance-corrected association between the environment and the error (positive ⇒ it co-occurs with error). Predictors rank by this.">assoc. (φ)</th>
                      <th title="F₁ of treating the environment as a prediction of error (precision × recall). Shown alongside φ; not the ranking metric.">F₁</th>
                      <th title="Errors vs. correct outcomes in positions where the environment IS present">err/ok · with</th>
                      <th title="Errors vs. correct outcomes in positions where it is absent">err/ok · without</th>
                    </tr>
                  </thead>
                  <tbody>
                    {#each a.predictors as p}
                      <tr>
                        <td class="form">{p.predictor}</td>
                        <td>{p.phi >= 0 ? "+" : ""}{p.phi.toFixed(2)}</td>
                        <td>{p.fscore.toFixed(2)}</td>
                        <td>{p.errHere}/{p.okHere}</td>
                        <td>{p.errAway}/{p.okAway}</td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              {:else}
                <p class="muted">No environment predictor was positively associated with the error.</p>
              {/if}
            </details>
          {/each}
        {/snippet}
        <!-- The four analysis views, each as a snippet so the Single tab can stack the same
             renders the whole-lexicon tabs show. The parameter shadows the same-named state,
             so a body reads identically whether fed the full run's data or one word's. -->
        {#snippet accuracyBlock(accuracy)}
          <table class="report-summary">
            <thead>
              <tr>
                <th>stage</th><th>assessed</th><th>exact</th>
                <th title="Words within edit distance 1 of the target (an exact match, or one insertion/deletion/substitution away)">within 1</th>
                <th title="Mean phone edit distance: Levenshtein distance over segments, averaged across assessed words">mean phone dist</th>
                <th title="Mean feature distance: per-segment featural difference, averaged across assessed words">mean feature dist</th>
              </tr>
            </thead>
            <tbody>
              {#each accuracy.stages as s}
                <tr class:final={s.label === "final"}>
                  <td class="tgt">{s.label}</td>
                  <td>{s.assessed}</td>
                  <td>{s.exact}</td>
                  <td>{s.withinOne}</td>
                  <td>{s.meanPhone.toFixed(3)}</td>
                  <td>{s.meanFeature.toFixed(3)}</td>
                </tr>
              {/each}
            </tbody>
          </table>

          {#if accuracy.weighted}
            <p class="caveat">
              <strong>Token-weighted</strong> (by <code>frequency</code>, total weight
              {accuracy.weighted.weight}): final {(accuracy.weighted.accuracy * 100).toFixed(1)}%
              exact, mean phone dist {accuracy.weighted.meanPhone.toFixed(3)}, mean feature dist
              {accuracy.weighted.meanFeature.toFixed(3)}. Confusions and the autopsy stay
              unweighted token counts.
            </p>
          {/if}

          {#if accuracy.hasStages}
            <p class="caveat">
              Intermediate stages compare the derived snapshot at rule-time T against
              the target at stage-time T. If those timescales aren’t calibrated, the
              stage rows read low for an alignment reason, not a phonological one —
              only <strong>final</strong> is independent of that.
            </p>
          {/if}

          {#each accuracy.stages as s}
            <details class="report-detail" open={s.label === "final"}>
              <summary>
                <span class="tgt">{s.label}</span>
                <span class="muted">{s.assessed - s.exact} of {s.assessed} differ</span>
              </summary>
              {#if s.misses.length}
                <table class="report-misses">
                  <thead>
                    <tr>
                      <th>gloss</th><th>derived</th><th>target</th><th>d</th><th>fd</th>
                      <th title="Attested stages whose target this derived form reproduces exactly (feature distance 0)">matches at</th>
                      <th title="The attested stage whose target this derived form is closest to by feature distance">closest at</th>
                    </tr>
                  </thead>
                  <tbody>
                    {#each s.misses as m}
                      <tr>
                        <td>{m.gloss}</td>
                        <td class="form">{m.derived}</td>
                        <td class="form">{m.target}</td>
                        <td>{m.d}</td>
                        <td>{m.fd ?? "—"}</td>
                        <td>{m.matchesAt || "—"}</td>
                        <td>{m.closestAt || "—"}</td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              {:else}
                <p class="muted">All {s.assessed} assessed words exact.</p>
              {/if}
            </details>
          {/each}
        {/snippet}
        {#snippet errorsBlock(errors)}
          <p class="caveat">
            Which segments came out wrong at each attested stage (and the final): the phone
            confusions, most frequent first. <code>∅</code> on the <em>got</em> side is a
            dropped phone; on the <em>expected</em> side, a spurious inserted one. Trust an
            intermediate stage only where its attested forms are notationally comparable to
            the engine’s output.
          </p>
          {#each errors.stages as s}
            <details class="report-detail" open={s.label === "final"}>
              <summary>
                <span class="tgt">stage {s.label}</span>
                <span class="muted">{s.confusions.length} error(s)</span>
              </summary>
              {@render confusionTable(s.confusions)}
            </details>
          {/each}
        {/snippet}
        {#snippet contextBlock(errorContext)}
          <p class="caveat">
            For each erroring segment, the <strong>attested</strong>-form environments most
            associated with getting it wrong (by phi coefficient), per stage. A metathesis
            reads as an adjacent substitution pair.
          </p>
          {#each errorContext.stages as s}
            <details class="report-detail context-stage" open={s.label === "final"}>
              <summary>
                <span class="tgt">stage {s.label}</span>
                <span class="muted">{s.segments.length} segment(s)</span>
              </summary>
              {@render autopsyBlock(s.segments)}
            </details>
          {/each}
        {/snippet}
        {#snippet blameBlock(blame, open = false)}
          <p class="caveat">
            Every assessed word, worst first (exact ones last, with no residual). Each wrong
            phone is attributed to the rule that produced it (the last firing rule that set its
            segment). <strong>omission</strong> = no rule touched it; <strong>unattributed</strong>
            = the surface didn’t map one phone per segment. The stage line and trajectory are
            context — trust the stage only where the attested forms are notationally comparable
            to the engine’s output.
          </p>
          {#each blame.words as w}
            <details class="report-detail" {open}>
              <summary class="blame-summary">
                <span class="tgt blame-word">{w.word}</span>
                <span class="blame-meta">
                  <span class="form">{w.surface}</span>
                  <span class="muted">for</span>
                  <span class="form">{w.target}</span>
                  <span class="muted">· d{w.distance}</span>
                </span>
              </summary>
              {#if w.residuals.length}
                <ul class="residual-pills">
                  {#each w.residuals as r}
                    <li class="residual-pill">
                      <span class="form">{r.expected ?? "∅"}</span>→<span class="form"
                        >{r.got ?? "∅"}</span
                      >
                      <span class="muted"
                        >({r.culprit
                          ? r.culprit + (r.time != null ? ", t=" + r.time : "")
                          : r.attributed
                            ? r.kind
                            : "unattributed"})</span
                      >
                    </li>
                  {/each}
                </ul>
              {:else}
                <p class="muted">exact — matches the target.</p>
              {/if}
              {#if w.stage}
                <p class="muted stage-line">
                  first diverges at stage t={w.stage.time}: attested
                  <span class="form">{w.stage.attested}</span>, derived
                  <span class="form">{w.stage.derived}</span>
                </p>
              {/if}
              <div class="trace-scroll">
              <table class="report-misses blame-traj">
                <thead>
                  <tr><th>step</th><th>t</th><th>form</th><th>target</th><th>d</th><th>fd</th></tr>
                </thead>
                <tbody>
                  {#each w.trajectory as p}
                    <tr class:regressed={p.regressed}>
                      <td>{p.label}{p.regressed ? " ⤴" : ""}</td>
                      <td>{p.time ?? ""}</td>
                      <td class="form">{p.form}</td>
                      <td class="form">{p.target}</td>
                      <td>{p.distance}</td>
                      <td>{p.fd ?? "—"}</td>
                    </tr>
                  {/each}
                </tbody>
              </table>
              </div>
            </details>
          {/each}
        {/snippet}
        <!-- The Single tab: an input bar to derive one word on demand, then that word's own
             derivation, accuracy, errors, context, and blame — the same renders as the
             whole-lexicon tabs, over a one-word run. -->
        {#snippet singleView()}
          <div class="single-view">
            {#if bigProject && !result && pendingSize}
              <p class="muted">
                {pendingSize.words} words × {pendingSize.rules} rules — too large to run on every
                edit. Either run the whole project with the <strong>Run project</strong> button
                above, or derive one word at a time below. Running the full project through the CLI
                offers a 10× or greater speedup over in-browser derivation.
              </p>
            {/if}
            <form class="single-bar" onsubmit={(e) => { e.preventDefault(); runSingleWord(); }}>
              <input
                class="single-input"
                type="text"
                placeholder="a word to derive — its IPA, or a gloss from the lexicon"
                bind:value={singleInput}
                disabled={!ready || singleBusy}
              />
              <button
                class="run-single"
                disabled={!ready || singleBusy || !singleInput.trim()}
                onclick={runSingleWord}>Run single word</button
              >
            </form>
            {#if singleBusy}
              <p class="muted">deriving…</p>
            {:else if single?.error}
              <div class="card error">
                <h3>Error</h3>
                {#each single.error as line}<pre>{line}</pre>{/each}
              </div>
            {:else if single}
              {@const d = single.derivations[0]}
              <p class="muted single-meta">
                <span class="form tgt">{single.ipa}</span>{#if single.gloss}<span class="gloss"
                    >{" ‘" + single.gloss + "’"}</span
                  >{/if}{single.found
                  ? " — from the lexicon"
                  : " — not in the lexicon, derived without a target"}
              </p>
              <article class="card derivation">
                <header class="word-head">
                  <span class="word-ipa">{d.ipa}</span>
                  {#if d.gloss}<span class="gloss">‘{d.gloss}’</span>{/if}
                  <div class="card-toggles">
                    {#if d.steps.some((s) => s.autosegmental?.length)}
                      <button
                        class="card-toggle"
                        class:active={singleAuto}
                        title="Show the autosegmental diagram for each rule that spreads, docks, or delinks"
                        onclick={() => (singleAuto = !singleAuto)}>Autosegmental</button
                      >
                    {/if}
                    {#if d.steps.some((s) => s.definition)}
                      <button
                        class="card-toggle"
                        class:active={singleDefs}
                        title="Show the rule definitions for this word"
                        onclick={() => (singleDefs = !singleDefs)}>Definitions</button
                      >
                    {/if}
                  </div>
                </header>
                {@render traceSteps(d.steps, singleDefs, singleAuto)}
                <div class="surface">
                  <span class="muted" aria-hidden="true">→</span>
                  <span class="form">{d.surface}</span>
                </div>
              </article>
              {#if single.accuracy}
                <h3 class="single-section">Accuracy</h3>
                {@render accuracyBlock(single.accuracy)}
              {/if}
              {#if single.errors}
                <h3 class="single-section">Errors</h3>
                {@render errorsBlock(single.errors)}
              {/if}
              {#if single.errorContext}
                <h3 class="single-section">Error context</h3>
                {@render contextBlock(single.errorContext)}
              {/if}
              {#if single.blame}
                <h3 class="single-section">Blame</h3>
                {@render blameBlock(single.blame, true)}
              {/if}
            {/if}
          </div>
        {/snippet}
        {#if resultView === "single" || (bigProject && !result)}
          {@render singleView()}
        {:else}
        {@render timingLine()}
        {#if resultView === "accuracy" && accuracy}
          {@render accuracyBlock(accuracy)}
        {:else if resultView === "errors" && errors}
          {@render errorsBlock(errors)}
        {:else if resultView === "errorContext" && errorContext}
          {@render contextBlock(errorContext)}
        {:else if resultView === "blame" && blame}
          {@render blameBlock(blame)}
        {:else if resultView === "warnings" && (warnings.length || unfiredRules.length)}
          {#if unfiredRules.length}
            <p class="caveat">
              These rules are word-scoped to a word that isn’t in the lexicon, so they can never
              fire. Fix the word name, or drop the scope.
            </p>
            <table class="report-summary warnings-table">
              <thead>
                <tr><th>rule</th><th>scoped to missing word</th></tr>
              </thead>
              <tbody>
                {#each unfiredRules as u}
                  <tr>
                    <td class="form">{u.rule}</td>
                    <td class="tgt">{u.word}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          {/if}
          {#if warnings.length}
            <p class="caveat">
              These words’ onset/coda patterns admitted no legal split for the listed cluster, so
              syllabification fell back to the sonority Maximal Onset division. Loosen the patterns
              to cover these clusters, or accept the fallback.
            </p>
            <table class="report-summary warnings-table">
              <thead>
                <tr
                  ><th>word</th><th>gloss</th><th>form</th><th>cluster</th><th>syllabified as</th></tr
                >
              </thead>
              <tbody>
                {#each warnings as w}
                  <tr>
                    <td class="tgt">{w.word}</td>
                    <td class="gloss-cell">{w.gloss}</td>
                    <td class="form">{w.form}</td>
                    <td class="form">{w.clusters.join(", ")}</td>
                    <td class="form">{w.syllabified}</td>
                  </tr>
                {/each}
              </tbody>
            </table>
          {/if}
        {:else if !result}
          {#if !busy}<p class="muted">No results yet.</p>{/if}
        {:else if result.error}
          <div class="card error">
            <h3>Error</h3>
            {#each result.error as line}
              <pre>{line}</pre>
            {/each}
          </div>
        {:else if result.derivations.length === 0}
          <p class="muted">No words in the project.</p>
        {:else}
          {#each result.derivations as d, i}
            <article class="card derivation">
              <header class="word-head">
                <span class="word-ipa">{d.ipa}</span>
                {#if d.gloss}<span class="gloss">‘{d.gloss}’</span>{/if}
                <div class="card-toggles">
                  {#if d.steps.some((s) => s.autosegmental?.length)}
                    <button
                      class="card-toggle"
                      class:active={openAuto[i]}
                      title="Show the autosegmental diagram for each rule that spreads, docks, or delinks"
                      onclick={() => (openAuto[i] = !openAuto[i])}>Autosegmental</button
                    >
                  {/if}
                  {#if d.steps.some((s) => s.definition)}
                    <button
                      class="card-toggle"
                      class:active={openDefs[i]}
                      title="Show the rule definitions for this word"
                      onclick={() => (openDefs[i] = !openDefs[i])}>Definitions</button
                    >
                  {/if}
                </div>
              </header>
              {@render traceSteps(d.steps, openDefs[i], openAuto[i])}
              <div class="surface">
                <span class="muted" aria-hidden="true">→</span>
                <span class="form">{d.surface}</span>
              </div>
            </article>
          {/each}
        {/if}
        {/if}
      </div>
      {/if}
      </div>
    </section>
  </main>
</div>

{#if docsOpen}
  <!-- backdrop click closes (Esc and × also close) -->
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <div
    class="docs-overlay"
    role="presentation"
    onclick={(e) => e.target === e.currentTarget && (docsOpen = false)}
  >
    <div class="docs-window" role="dialog" aria-modal="true" aria-label="Documentation">
      <div class="docs-head">
        <div class="docs-tabs">
          <button
            class:active={docsTab === "guide"}
            onclick={() => (docsTab = "guide")}>User guide</button
          >
          <button
            class:active={docsTab === "system"}
            onclick={() => (docsTab = "system")}>Default system</button
          >
          <button
            class:active={docsTab === "acknowledgements"}
            onclick={() => (docsTab = "acknowledgements")}>Acknowledgements</button
          >
        </div>
        <button class="docs-close" title="Close (Esc)" onclick={() => (docsOpen = false)}
          >×</button
        >
      </div>
      <!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions -->
      <div class="docs-body" bind:this={docsBodyEl} onclick={docsAnchorClick}>{@html docsHtml}</div>
    </div>
  </div>
{/if}

<style>
  .app {
    display: flex;
    flex-direction: column;
    height: 100svh;
  }

  .bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 18px;
    border-bottom: 1px solid var(--border);
    background: var(--panel);
    flex: none;
  }
  .bar-left {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .docs-btn {
    font-size: var(--fs-body);
    padding: 4px 12px;
  }
  .brand strong {
    color: var(--text-h);
    font-size: var(--fs-header);
    font-weight: 600;
    letter-spacing: -0.3px;
  }
  .tag {
    margin-left: 8px;
    color: var(--muted);
    font-size: var(--fs-body);
  }
  .state {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: var(--fs-body);
    color: var(--muted);
  }
  /* Single cycling icon button (system → dark → light), styled after the psyguide switcher. */
  .theme-toggle {
    margin-left: 4px;
    width: 34px;
    height: 34px;
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--text);
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s, color 0.15s;
  }
  .theme-toggle:hover {
    color: var(--text-h);
    background: var(--accent-bg);
    border-color: var(--accent-border);
  }
  .theme-toggle svg {
    display: block;
    width: 18px;
    height: 18px;
  }

  .fatal {
    padding: 16px 18px;
    color: var(--error);
    background: var(--error-bg);
    border-bottom: 1px solid var(--border);
  }
  .fatal pre {
    white-space: pre-wrap;
    font-family: var(--mono);
    font-size: var(--fs-body);
  }

  .panels {
    display: flex;
    flex: 1;
    min-height: 0;
  }
  .panels.disabled {
    opacity: 0.8;
  }

  .panel {
    display: flex;
    flex-direction: column;
    min-width: 0;
    min-height: 0;
  }
  .left {
    flex: 0 0 var(--split-left, 50%);
  }
  .right {
    flex: 1 1 0;
  }
  /* The editor pane's body is: .panel-head, then .file-selection (the file tabs), then
     .editor-area (the active editor/CSV table, which fills the rest). The results pane's
     body is .panel-head then .result-area. Grouping the "one of" views under a single flex
     child keeps the collapse rule and the fill simple. */
  .file-selection {
    flex: none;
  }
  .editor-area,
  .result-area {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;
  }
  .divider {
    flex: none;
    position: relative;
    width: 9px; /* a wide, easy-to-grab hit area around a 1px visual line */
    background: transparent;
    cursor: col-resize;
    touch-action: none; /* a pointer drag resizes, never scrolls, on touch */
  }
  .divider::before {
    content: "";
    position: absolute;
    inset: 0 4px; /* the 1px line, centred in the 9px handle */
    background: var(--border);
    transition: background 0.12s;
  }
  .divider:hover::before,
  .divider:focus-visible::before {
    inset: 0 3px; /* thickens to 3px on hover/focus */
    background: var(--accent-border);
  }
  .divider:focus-visible {
    outline: none;
  }
  /* The panel-collapse buttons live in the divider but only appear on mobile (see the
     max-width: 960px block); on desktop the divider is a resize handle only. */
  .collapse-btn {
    display: none;
  }

  .panel-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px 16px 8px;
    flex: none;
  }
  .results-head {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }
  .head-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }
  .head-title {
    display: flex;
    align-items: center;
    gap: 10px;
    flex: none; /* keep the "Results" label + warning badge at content width — don't let
                   space-between squeeze it so the badge overflows into the wrapping tabs */
  }
  .warn-tab {
    font-size: var(--fs-body);
    padding: 2px 9px;
    border: 1px solid var(--warn-border);
    border-radius: 999px;
    background: var(--warn-bg);
    color: var(--warn-fg);
    white-space: nowrap;
    cursor: pointer;
  }
  .warn-tab:hover:not(:disabled) {
    background: var(--warn-bg-hover);
    border-color: var(--warn-fg);
  }
  .warn-tab.active {
    border-color: var(--warn-fg);
    font-weight: 600;
  }
  .panel-head h2 {
    margin: 0;
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
  }
  .actions {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .actions button {
    font-size: var(--fs-body);
    padding: 4px 10px;
  }
  .project-picker {
    position: relative;
    display: inline-flex;
    align-items: center;
    min-width: 0;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--panel);
    transition: border-color 0.15s, background 0.15s;
  }
  .project-picker:hover {
    border-color: var(--accent-border);
    background: var(--accent-bg);
  }
  .project-select {
    appearance: none;
    -webkit-appearance: none;
    font-family: var(--sans);
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
    background: transparent;
    border: none;
    margin: 0;
    padding: 3px 26px 3px 9px; /* room for the caret */
    max-width: 40ch;
    cursor: pointer;
  }
  .project-picker .caret {
    position: absolute;
    right: 9px;
    color: var(--muted);
    font-size: 15px;
    pointer-events: none; /* clicks fall through to the select */
  }
  .project-picker:hover .caret {
    color: var(--accent);
  }

  .file-group-label {
    padding: 4px 16px 2px;
    font-size: var(--fs-label);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--muted);
    flex: none;
  }
  .tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    padding: 0 16px 8px;
    flex: none;
  }
  .tab {
    font-family: var(--mono);
    font-size: var(--fs-body);
    padding: 3px 8px;
  }
  .tab-wrap {
    display: inline-flex;
    align-items: stretch;
  }
  .tab-wrap .tab {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
    border-right: none;
  }
  .tab-remove {
    font-family: var(--mono);
    font-size: var(--fs-body);
    padding: 3px 7px;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
    color: var(--muted);
  }
  .tab-remove:hover:not(:disabled) {
    color: var(--error);
    border-color: var(--error);
  }
  .editor {
    flex: 1;
    margin: 0 16px 16px;
    padding: 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--panel); /* match the derivation card background */
    color: var(--text-h);
    font-size: var(--fs-content);
    line-height: 1.55;
    resize: none;
    tab-size: 4;
    white-space: pre;
    overflow: auto;
  }
  /* Comment-highlight overlay (.toml editor). The wrap owns the frame; the textarea and its
     mirror <pre> stack inside it, sharing identical metrics so the coloured mirror lines up
     under the caret. */
  .editor-wrap {
    position: relative;
    flex: 1;
    margin: 0 16px 16px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--panel);
    overflow: hidden;
  }
  .editor-wrap .editor {
    position: absolute;
    inset: 0;
    flex: none;
    margin: 0;
    border: 0;
    border-radius: 0;
    background: transparent;
  }
  .editor-input {
    z-index: 1;
    color: transparent;
    caret-color: var(--text-h);
  }
  .editor-hl {
    z-index: 0;
    pointer-events: none;
    scrollbar-width: none; /* the textarea owns the visible scrollbar; the mirror is synced */
  }
  .editor-hl::-webkit-scrollbar {
    display: none;
  }
  .editor-hl .comment {
    color: var(--muted);
  }

  .progress {
    display: inline-block;
    width: 120px;
    height: 6px;
    border-radius: 3px;
    background: var(--border);
    overflow: hidden;
  }
  .progress.big {
    width: 280px;
    height: 12px;
    border-radius: 6px;
  }
  .progress-fill {
    display: block;
    height: 100%;
    background: var(--accent);
    border-radius: inherit;
    transition: width 120ms linear;
  }
  .progress-text {
    font-family: var(--mono);
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
  .run-prompt .progress-text {
    margin: 0;
    font-size: var(--fs-body);
  }

  .results {
    flex: 1;
    overflow: auto;
    padding: 4px 16px 24px;
  }
  /* IPA is opt-in: the results panel defaults to the Sans body face, and only the linguistic
     forms take the Charis (IPA) face — the computed forms (.form), the emphasised word/target
     cells (.word-ipa, .tgt), and code spans (which may carry an IPA pattern). This replaces the
     old "whole panel is IPA, then override back to Sans" model, so gloss/heading/label cells are
     Sans by default with no counter-override. */
  .results .form,
  .results .tgt,
  .results .word-ipa,
  .results code {
    font-family: var(--ipa);
  }
  .muted {
    color: var(--muted);
  }

  .run-prompt {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    padding: 56px 16px;
    text-align: center;
  }
  .run-top {
    width: 34px;
    height: 34px;
    padding: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--accent);
    background: var(--accent-bg);
    border-color: var(--accent-border);
  }
  .run-top svg {
    display: block;
  }
  .run-top:disabled {
    color: var(--muted);
    background: transparent;
    font-weight: 400;
  }
  .run-prompt .muted {
    max-width: 30ch;
  }

  .single-view {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .single-bar {
    display: flex;
    gap: 8px;
    align-items: center;
  }
  .single-input {
    flex: 1;
    min-width: 0;
    font-family: var(--ipa);
    font-size: var(--fs-emphasis);
    padding: 6px 10px;
    color: var(--text-h);
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
  }
  .single-input:focus {
    outline: none;
    border-color: var(--accent-border);
  }
  .run-single {
    font-size: var(--fs-body);
    padding: 6px 16px;
    font-weight: 600;
    white-space: nowrap;
    color: var(--accent);
    background: var(--accent-bg);
    border-color: var(--accent-border);
  }
  .single-meta {
    margin: 4px 0 0;
  }
  .single-section {
    margin: 18px 0 2px;
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
    border-top: 1px solid var(--border);
    padding-top: 12px;
  }

  /* One horizontally-scrollable row (like the file tabs) rather than wrapping to several
     rows — fills the actions row, with Save pinned after it. */
  .view-tabs {
    display: flex;
    flex: 1;
    flex-wrap: nowrap;
    gap: 4px;
    min-width: 0;
    overflow-x: auto;
    scrollbar-width: none;
  }
  .view-tabs::-webkit-scrollbar {
    display: none;
  }
  .view-tabs button {
    flex: 0 0 auto; /* keep each tab its natural width */
  }
  .head-row > .actions {
    flex: 1;
    min-width: 0;
  }
  .view-tabs button {
    font-size: var(--fs-body);
    padding: 4px 10px;
  }
  .save-result {
    margin-left: 8px;
    flex: none; /* pinned after the scrolling tabs — never shrinks */
  }

  .report-summary,
  .report-misses {
    border-collapse: collapse;
    width: 100%;
    font-size: var(--fs-body);
    font-variant-numeric: tabular-nums;
  }
  .report-summary {
    margin-bottom: 14px;
  }
  .report-summary th,
  .report-summary td,
  .report-misses th,
  .report-misses td {
    border: 1px solid var(--border);
    padding: 4px 9px;
    text-align: right;
  }
  .report-summary td.tgt,
  .report-misses th,
  .report-misses td:first-child {
    text-align: left;
  }
  /* Sporadic (word-scoped) rules read as italic in the derivation trace, like the Rules tab. */
  .st-rule.sporadic {
    font-style: italic;
  }
  /* Gloss is a translation, not IPA — muted (Sans is now the panel default, so no override). */
  .report-summary td.gloss-cell {
    color: var(--muted);
  }
  /* Warnings table: word/gloss/form/cluster (the first four columns) read left-to-right, so
     left-align their headers and cells (report-summary right-aligns by default). */
  .warnings-table th:nth-child(-n + 4),
  .warnings-table td:nth-child(-n + 4) {
    text-align: left;
  }
  .report-summary thead th,
  .report-misses thead th {
    color: var(--muted);
    font-weight: 600;
    text-align: right;
    background: var(--panel);
  }
  .report-summary tr.final td {
    font-weight: 600;
    color: var(--text-h);
    border-top-width: 2px;
  }
  .report-misses td.form {
    color: var(--text-h);
  }
  /* Wide traces (long IPA forms) scroll inside their own card rather than widening the
     whole results pane. On desktop the table fits, so this container never scrolls. */
  .trace-scroll {
    overflow-x: auto;
  }
  /* Blame trajectory: the t/form/target/d/fd columns hug their content; the first `step`
     column absorbs the remaining width and wraps long rule labels instead of forcing the
     table wide. A min-width keeps that label column readable when the table is starved for
     space (mobile) — without it, overflow-wrap: anywhere shreds the label to one letter
     per line. break-word (not anywhere) then only breaks words too long to fit. */
  .blame-traj td:not(:first-child),
  .blame-traj th:not(:first-child) {
    width: 1%;
    white-space: nowrap;
  }
  .blame-traj td:first-child,
  .blame-traj th:first-child {
    white-space: normal;
    overflow-wrap: break-word;
    min-width: 15ch;
  }

  .caveat {
    font-size: var(--fs-body);
    color: var(--muted);
    border-left: 3px solid var(--border);
    padding: 6px 12px;
    margin: 0 0 16px;
  }

  .report-detail {
    margin-bottom: 10px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
  }
  .report-detail summary {
    cursor: pointer;
    display: flex;
    flex-wrap: wrap;
    gap: 4px 10px;
    align-items: baseline;
    padding: 4px 0;
    font-weight: 600;
    color: var(--text-h);
  }
  .report-detail summary .muted {
    font-weight: 400;
  }
  /* Blame word row: the gloss/word label takes the available width; the derived-vs-target
     metadata stays together as one unit (never splitting "· dN" mid-token) and sits to the
     right, dropping to its own line only when the label leaves it no room. */
  .blame-word {
    flex: 1 1 auto;
    min-width: 0;
    overflow-wrap: anywhere;
  }
  .blame-meta {
    display: inline-flex;
    align-items: baseline;
    gap: 8px;
    margin-left: auto;
    white-space: nowrap;
  }
  .report-detail .report-misses {
    margin-top: 6px;
  }
  /* The Errors tab renders a .report-summary confusion table per stage <details>;
     give it a bit more breathing room below the stage heading. */
  .report-detail .report-summary {
    margin-top: 12px;
  }
  /* The Context tab nests each segment's autopsy (a .report-detail) inside a per-stage
     .report-detail. Distinguish the levels without a heavier stage rule (kept at the tabs'
     standard 1px solid): the stage header gets more room below it, and its segments sit
     indented under a left rule with a lighter dashed separator. */
  .context-stage > summary {
    padding-bottom: 10px;
  }
  .context-stage > .report-detail {
    margin-left: 16px;
    padding-left: 12px;
    border-left: 2px solid var(--border);
    border-bottom-style: dashed;
  }
  .context-stage > .report-detail:last-child {
    margin-bottom: 0;
    padding-bottom: 0;
    border-bottom: none;
  }

  /* Errors, Error context + Blame tabs (reuse the report-* tables above) */
  /* The blame residuals render as a wrapped list of static, button-styled pills — one per
     wrong phone → its culprit rule — below each word's summary header. */
  .residual-pills {
    list-style: none;
    margin: 8px 0 2px;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .residual-pill {
    display: inline-flex;
    align-items: baseline;
    gap: 4px;
    padding: 3px 10px;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--accent-bg);
    font-size: var(--fs-body);
  }
  .residual-pill .form {
    color: var(--text-h);
  }
  .stage-line {
    font-size: var(--fs-body);
    margin: 0 0 8px;
  }
  .report-misses tr.regressed td:first-child {
    font-weight: 600;
    color: var(--text-h);
  }

  .timing-line {
    font-size: var(--fs-body);
    margin: 0 0 12px;
    font-variant-numeric: tabular-nums;
  }
  /* The Table tab renders CsvTable (flex: 1) directly in the flex-column pane, so the timing
     line rides above it in a fixed-height, 16px-inset strip. Padding matches the .results
     container (4px top) plus the timing line's usual 12px gap to the content below. */
  .table-timing {
    flex: none;
    padding: 4px 16px 12px;
  }
  .table-timing .timing-line {
    margin-bottom: 0;
  }

  .card {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 14px;
    background: var(--panel);
    box-shadow: var(--shadow);
  }
  .card h3 {
    margin: 0 0 6px;
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
  }
  .card.error {
    color: var(--error);
    background: var(--error-bg);
    border-color: var(--error);
  }
  .card.error pre {
    white-space: pre-wrap;
    font-family: var(--mono);
    font-size: var(--fs-body);
    margin: 2px 0;
  }

  .word-head {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin-bottom: 10px;
  }
  .word-ipa {
    font-size: var(--fs-emphasis);
    font-weight: 600;
    color: var(--text-h);
  }
  .gloss {
    font-size: var(--fs-body);
    color: var(--muted);
    font-style: italic;
  }
  /* The card's toggle buttons (Autosegmental · Definitions) float to the right of the
     word/gloss as a group; Autosegmental sits left of Definitions. */
  .card-toggles {
    margin-left: auto;
    align-self: center;
    display: flex;
    gap: 8px;
  }
  .card-toggle {
    font-size: var(--fs-label);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 3px 8px;
  }

  /* The firing-rule trace reuses the Blame trajectory table look (report-misses blame-traj).
     Additions: a rule's definition revealed as a full-width merged row by the Definitions
     toggle, and a left-aligned first-column ("rule") header. */
  .blame-traj td.def-cell {
    font-family: var(--mono);
    font-size: var(--fs-body);
    font-weight: 400;
    color: var(--muted);
  }
  /* The autosegmental diagram(s) revealed as a full-width merged row under a rule that
     spreads/docks/delinks. One monospace diagram per spread (vowel harmony spreads several
     nodes ⇒ several, stacked). */
  .blame-traj td.auto-cell {
    padding: 10px 9px 12px;
  }
  /* Diagrams must be monospace for the box-drawing association lines to align. */
  .diagram {
    margin: 0;
    font-family: var(--mono);
    font-size: var(--fs-body);
    line-height: 1.35;
    color: var(--text-h);
    white-space: pre;
    overflow-x: auto;
  }
  .diagram + .diagram {
    margin-top: 10px;
  }
  .blame-traj thead th:first-child {
    text-align: left;
  }

  .surface {
    display: flex;
    align-items: baseline;
    gap: 8px;
    margin-top: 12px;
    font-size: var(--fs-emphasis);
  }
  .surface .form {
    color: var(--text-h);
  }

  .spinner {
    width: 12px;
    height: 12px;
    border: 2px solid var(--accent-border);
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
    display: inline-block;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  .ok-dot,
  .err-dot,
  .mod-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  .ok-dot {
    background: #2faa5b;
  }
  .mod-dot {
    background: var(--warn-fg);
  }
  .mod-text {
    color: var(--warn-fg);
    font-weight: 600;
  }
  .err-dot {
    background: var(--error);
  }

  @media (max-width: 960px) {
    .app {
      overflow-x: hidden; /* nothing should push the page wider than the screen */
    }
    .panels {
      flex-direction: column;
    }
    /* Stacked: the horizontal split no longer applies. Give the editor a little more of
       the height than the results, since editing is the cramped half on a phone. */
    .left {
      flex: 1 1 56%;
    }
    .right {
      flex: 1 1 44%;
    }
    /* Collapse a stacked panel to just its header so the other fills the screen. The
       remaining panel keeps flex-grow, so it expands into the freed space automatically. */
    .panel.is-collapsed {
      flex: 0 0 auto;
    }
    /* :global so this also hides child-component roots that don't carry App's scope class
       (CsvTable's .csv-wrap, DependencyTree's .tree-outer) — otherwise a collapsed pane
       showing a CSV/Matrix/Tree wouldn't actually collapse. */
    .panel.is-collapsed > :global(:not(.panel-head)) {
      display: none;
    }
    /* The divider stops being a drag handle and becomes the collapse control bar. */
    .divider {
      width: auto;
      height: auto;
      flex: none;
      cursor: default;
      touch-action: auto;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 5px 0;
      background: var(--panel);
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
    }
    .divider::before {
      display: none; /* no resize line on mobile */
    }
    .collapse-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 24px;
      padding: 0;
      font-size: 13px;
      line-height: 1;
      color: var(--muted);
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      cursor: pointer;
    }
    .collapse-btn.active {
      color: var(--text-h);
      border-color: var(--accent-border);
      background: var(--panel);
    }

    /* Compact single-line header: drop the tagline and the long "modified" note (the
       accented run icon already signals a pending re-run), and tighten the padding so
       brand + Docs + status + run + theme fit on one row. flex-wrap stays as a fallback. */
    .bar {
      flex-wrap: wrap;
      gap: 8px;
      padding: 8px 12px;
    }
    .tag {
      display: none;
    }

    /* Editor pane header: the project selector + load buttons scroll horizontally in one
       row, instead of colliding when a project's (folder-name) title is long. */
    .left .panel-head {
      flex-wrap: nowrap;
      justify-content: flex-start;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .left .panel-head::-webkit-scrollbar {
      display: none;
    }
    .left .panel-head > * {
      flex: 0 0 auto; /* the picker and the action-button group keep their natural widths */
    }

    /* File chips: one horizontally-scrollable row rather than four wrapped rows, so the
       editor below it keeps usable height. */
    .tabs {
      flex-wrap: nowrap;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .tabs::-webkit-scrollbar {
      display: none;
    }
    .tabs .tab,
    .tabs .tab-wrap {
      flex: 0 0 auto; /* keep each chip its natural width — don't squeeze the filenames */
    }

    /* Put the Default/Project label inline at the start of its scrollable chip row, so each
       file group is a single line (label · chips →) instead of a label above the chips. */
    .file-group {
      display: flex;
      align-items: center;
      padding: 2px 0;
    }
    .file-group .file-group-label {
      flex: 0 0 auto;
      padding: 0 0 0 16px;
    }
    .file-group .tabs {
      flex: 1 1 auto;
      min-width: 0;
      padding: 0 16px 0 8px;
    }
    /* Symmetric breathing room around the file-tab strip: match the space below it (to the
       edit area) to the space above it (the header's 8px bottom padding). */
    .editor-area {
      margin-top: 8px;
    }

    /* The editor soft-wraps long lines instead of clipping them off the right edge — the
       textarea and its highlight mirror share these metrics, so they stay aligned. */
    .editor {
      white-space: pre-wrap;
      overflow-wrap: break-word;
    }

    /* Drop the result actions onto their own full-width line (the tab row itself already
       scrolls horizontally — see the base .view-tabs). */
    .head-row {
      flex-wrap: wrap;
    }
    .head-row > .actions {
      flex: 1 1 100%;
    }

    /* The Derivations tab renders every word's trace card at once (300+ for
       latin_to_french). Each card's table is horizontally scrollable (.trace-scroll), and
       on a phone hundreds of live scroll containers each get their own compositing layer —
       which exhausts browser memory and crashes/reloads the tab. content-visibility: auto
       makes the browser skip rendering (layout, paint, and compositing) of any card that's
       off-screen, so only the handful in view ever allocate a scroll layer. The card list
       stays lazily rendered: a card materialises as it scrolls into view and is released
       when it leaves. contain-intrinsic-size gives an off-screen card a placeholder height
       so the scrollbar stays sane; `auto` then remembers each card's real height once it
       has rendered, so scrolling back is stable. Mobile only — desktop renders all 300+
       cards fine and needs no change. */
    .card.derivation {
      content-visibility: auto;
      contain-intrinsic-size: auto 600px;
    }

    /* The Accuracy / Errors / Context tables can be wider than a phone (many columns, long
       IPA examples). If they overflow .results, the horizontal scroll bleeds past iOS
       Safari's leaky overflow-x: hidden and drags the whole page — header and all — sideways.
       Make each such table its own horizontal-scroll box (display: block + overflow-x: auto)
       so it scrolls in place and .results never overflows. There are only a handful of these
       tables, so unlike the 300+ derivation cards this creates no memory pressure. The
       derivation/blame traces are excluded — they already scroll via .trace-scroll. */
    .results .report-summary,
    .results .report-misses:not(.blame-traj) {
      display: block;
      overflow-x: auto;
    }
  }

  /* Docs floating window */
  .docs-overlay {
    position: fixed;
    inset: 0;
    z-index: 100;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4vh 16px;
  }
  .docs-window {
    display: flex;
    flex-direction: column;
    width: min(880px, 100%);
    max-height: 92vh;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 10px;
    box-shadow: var(--shadow);
    overflow: hidden;
  }
  .docs-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    flex: none;
  }
  .docs-tabs {
    display: inline-flex;
    gap: 4px;
  }
  .docs-tabs button {
    font-size: var(--fs-body);
    padding: 4px 12px;
  }
  .docs-close {
    border: none;
    background: transparent;
    color: var(--muted);
    font-size: 20px;
    line-height: 1;
    padding: 2px 8px;
  }
  .docs-close:hover:not(:disabled) {
    color: var(--text-h);
    border: none;
  }
  .docs-body {
    overflow: auto;
    padding: 4px 26px 28px;
    font-family: var(--sans);
    color: var(--text);
    font-size: var(--fs-body);
  }

  /* Rendered markdown (dynamic {@html}, so :global). Its own heading scale: h2/h4 land on
     the shared tokens; h1 (22px) and h3 (15px) are documented docs-only steps between them. */
  .docs-body :global(h1) {
    font-size: 22px;
    color: var(--text-h);
    margin: 18px 0 10px;
  }
  .docs-body :global(h2) {
    font-size: var(--fs-emphasis);
    color: var(--text-h);
    margin: 22px 0 8px;
    padding-bottom: 4px;
    border-bottom: 1px solid var(--border);
  }
  .docs-body :global(h3) {
    font-size: 15px;
    color: var(--text-h);
    margin: 16px 0 6px;
  }
  .docs-body :global(h4) {
    font-size: var(--fs-body);
    color: var(--text-h);
    margin: 14px 0 4px;
  }
  .docs-body :global(p),
  .docs-body :global(li) {
    line-height: 1.6;
  }
  .docs-body :global(ul),
  .docs-body :global(ol) {
    padding-left: 22px;
  }
  .docs-body :global(a) {
    color: var(--accent);
  }
  .docs-body :global(code) {
    font-family: var(--ipa), var(--mono);
    font-size: 0.92em;
    background: var(--code-bg);
    padding: 1px 4px;
    border-radius: 4px;
  }
  .docs-body :global(pre) {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
    overflow-x: auto;
  }
  .docs-body :global(pre code) {
    background: none;
    padding: 0;
  }
  .docs-body :global(table) {
    display: block;
    width: max-content;
    max-width: 100%;
    overflow-x: auto;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 0.95em;
  }
  .docs-body :global(th),
  .docs-body :global(td) {
    border: 1px solid var(--border);
    padding: 4px 9px;
    text-align: left;
  }
  .docs-body :global(th) {
    background: var(--panel);
    color: var(--text-h);
  }
  .docs-body :global(blockquote) {
    margin: 8px 0;
    padding: 2px 12px;
    border-left: 3px solid var(--border);
    color: var(--muted);
  }
  .docs-body :global(hr) {
    border: none;
    border-top: 1px solid var(--border);
    margin: 18px 0;
  }
</style>
