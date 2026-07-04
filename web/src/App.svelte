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
    listExampleProjects,
    loadExampleProject,
  } from "./lib/engine.js";
  import CsvTable from "./lib/CsvTable.svelte";
  import { marked } from "marked";
  import userGuideMd from "../../docs/user_guide.md?raw";
  import defaultSystemMd from "../../docs/default_system.md?raw";

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
  let result = $state(null); // { derivations } | { error }
  let grading = $state(null); // grading summary from the last run, or null when there's no target
  let tableCsv = $state(""); // derivation_table.csv content, for the right-pane Table view
  let resultView = $state("derivations"); // right-pane view: "derivations" | "table" | "grading"

  // A project with more than this many words OR rules is too costly to re-run on
  // every edit; it waits for the "Run project" button instead of auto-running.
  const AUTO_RUN_WORDS = 500;
  const AUTO_RUN_RULES = 100;
  let needsRun = $state(false); // a large project is awaiting a manual run
  let pendingSize = $state(null); // { words, rules } of the project awaiting a run

  let fileInput; // single-file <input>
  let projectInput; // multi-file (folder) <input>
  let examples = $state([]); // bundled example projects from the static manifest
  let imported = $state([]); // imported (local-folder) projects: { id, label, files }
  let picked = $state(""); // id of the selected project ("" = the built-in default)

  let docsOpen = $state(false); // the Docs floating window
  let docsTab = $state("guide"); // active docs tab: "guide" | "system"
  const docsHtml = $derived(
    marked.parse(docsTab === "guide" ? userGuideMd : defaultSystemMd),
  );

  let debounceTimer = null;

  const defaultFiles = $derived(files.filter((f) => fileSource[f] !== "project"));
  const projectFiles = $derived(files.filter((f) => fileSource[f] === "project"));

  // Everything the project switcher lists: the built-in default, the bundled
  // examples, and any locally-imported folders (added by loadProject).
  const projects = $derived([
    { id: "", label: "Default" },
    ...examples.map((e) => ({ id: e.dir, label: e.label || e.dir, kind: "example", entry: e })),
    ...imported.map((p) => ({ id: p.id, label: p.label, kind: "imported", files: p.files })),
  ]);

  let theme = $state(localStorage.getItem("theme") ?? "system"); // "light" | "dark" | "system"
  $effect(() => {
    if (theme === "system") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = theme;
    localStorage.setItem("theme", theme);
  });

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

  // Yield to the browser so a state change (the progress bar) actually paints
  // before the next synchronous Pyodide batch blocks the main thread again.
  const paint = () => new Promise((r) => setTimeout(r, 0));

  async function rerun(force = false) {
    if (!ready) return;
    const myToken = ++runToken; // claim this run; a newer run bumps the token and supersedes us
    busy = true;
    progress = 0;
    progressText = "";
    result = null; // clear the previous results so the pane doesn't show stale output under the bar
    grading = null; // and the previous grading summary
    tableCsv = ""; // and the previous derivation table
    openDefs = {}; // reset per-card definition toggles (indices map to new words after a run)
    await paint(); // paint the (updated) left pane + cleared right pane before the first batch blocks
    if (myToken !== runToken) return; // superseded while painting — a newer run owns the session now
    try {
      const prep = prepareRun();
      if (prep.error) {
        result = { error: prep.error };
        return;
      }
      if (!force && (prep.words > AUTO_RUN_WORDS || prep.rules > AUTO_RUN_RULES)) {
        pendingSize = { words: prep.words, rules: prep.rules };
        needsRun = true; // too large to auto-run — wait for the Run project button
        return;
      }
      needsRun = false;
      const total = prep.words;
      const acc = [];
      // Drive the run in slices, painting the bar between them. Batch size is
      // adapted from the measured cost of the previous batch to keep each one a
      // short, roughly fixed slice of wall-clock time (so the bar stays smooth
      // and the thread never freezes for long, whatever the machine's speed).
      let batch = 4;
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
      const fin = finalizeRun();
      grading = fin?.grading ?? null;
      if (!grading && resultView === "grading") resultView = "derivations"; // no target ⇒ leave the (now hidden) tab
      tableCsv = readFile("derivation_table.csv"); // for the Table view
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
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => rerun(), 400); // auto-run only if under the size limit
  }

  function runProject() {
    rerun(true); // force a run regardless of size (the Run project button)
  }

  async function removeFileTab(name, ev) {
    ev.stopPropagation();
    removeFile(name);
    refreshStatus();
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

  // The report file each right-pane view is generated from.
  const RESULT_FILE = {
    derivations: "output.md",
    table: "derivation_table.csv",
    grading: "distances.md",
  };

  function saveResult() {
    const name = RESULT_FILE[resultView];
    if (name) download(name, readFile(name));
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
      selectFile(active);
      await rerun(); // bumps runToken and takes over the busy flag from here
    } catch (e) {
      if (myToken === runToken) {
        alert(`Could not load ${proj.label}: ${e?.message ?? e}`);
        picked = "";
        resetOverlay();
        refreshStatus();
        selectFile(active);
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
      <button class="docs-btn" onclick={() => (docsOpen = true)}>Docs</button>
    </div>
    <div class="state">
      {#if initError}
        <span class="err-dot"></span> {status}
      {:else if !ready}
        <span class="spinner"></span> {status}
      {:else}
        <span class="ok-dot"></span> Engine ready
      {/if}
      <div class="theme-toggle">
        <button class:active={theme === "light"} onclick={() => (theme = "light")}
          >Light</button
        >
        <button class:active={theme === "dark"} onclick={() => (theme = "dark")}
          >Dark</button
        >
        <button class:active={theme === "system"} onclick={() => (theme = "system")}
          >System</button
        >
      </div>
    </div>
  </header>

  {#if initError}
    <div class="fatal">
      <h2>Could not load the engine</h2>
      <pre>{initError}</pre>
    </div>
  {/if}

  <main class="panels" class:disabled={!ready}>
    <!-- LEFT: inventories -->
    <section class="panel left">
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
          <button disabled={!ready} onclick={() => fileInput.click()}
            >Load file</button
          >
          <button disabled={!ready} onclick={() => projectInput.click()}
            >Load project</button
          >
          <button disabled={!ready} onclick={saveActiveFile}>Save</button>
        </div>
      </div>

      {#if defaultFiles.length}
        <div class="file-group-label">Default</div>
        <div class="tabs">
          {#each defaultFiles as f}
            <button
              class="tab"
              class:active={f === active}
              disabled={!ready}
              onclick={() => selectFile(f)}>{f}</button
            >
          {/each}
        </div>
      {/if}

      {#if projectFiles.length}
        <div class="file-group-label">Project</div>
        <div class="tabs">
          {#each projectFiles as f}
            <span class="tab-wrap">
              <button
                class="tab"
                class:active={f === active}
                disabled={!ready}
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
      {/if}

      {#if active === "letters.csv"}
        <CsvTable {content} />
      {:else}
        <textarea
          class="editor ipa"
          spellcheck="false"
          disabled={!ready}
          bind:value={content}
          oninput={onEdit}
        ></textarea>
      {/if}

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

    <div class="divider"></div>

    <!-- RIGHT: results -->
    <section class="panel right">
      <div class="panel-head results-head">
        <div class="head-row">
          <h2>Results</h2>
          <div class="actions">
            {#if result?.derivations}
              <div class="view-tabs">
                <button
                  class:active={resultView === "derivations"}
                  onclick={() => (resultView = "derivations")}>Derivations</button
                >
                <button
                  class:active={resultView === "table"}
                  onclick={() => (resultView = "table")}>Table</button
                >
                {#if grading}
                  <button
                    class:active={resultView === "grading"}
                    onclick={() => (resultView = "grading")}>Grading</button
                  >
                {/if}
              </div>
              <button
                class="save-result"
                disabled={!ready}
                title="Download this view's report file"
                onclick={saveResult}>Save</button
              >
            {/if}
          </div>
        </div>
      </div>

      {#if busy}
        <div class="results ipa">
          <div class="run-prompt">
            <span class="progress big" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow={Math.round(progress * 100)}>
              <span class="progress-fill" style="width:{Math.round(progress * 100)}%"></span>
            </span>
            <p class="muted progress-text">{progressText || "running…"}</p>
          </div>
        </div>
      {:else if needsRun}
        <div class="results ipa">
          <div class="run-prompt">
            <button class="run-project" disabled={!ready || busy} onclick={runProject}
              >Run project</button
            >
            {#if pendingSize}
              <p class="muted">
                {pendingSize.words} words × {pendingSize.rules} rules — too large to run on
                every edit. Click to run.
              </p>
            {/if}
          </div>
        </div>
      {:else if resultView === "table" && tableCsv}
        <CsvTable content={tableCsv} />
      {:else}
      <div class="results ipa">
        {#if resultView === "grading" && grading}
          <table class="grade-summary">
            <thead>
              <tr>
                <th>stage</th><th>graded</th><th>exact</th><th>≤1</th>
                <th>mean d</th><th>mean fd</th>
              </tr>
            </thead>
            <tbody>
              {#each grading.stages as s}
                <tr class:final={s.label === "final"}>
                  <td class="tgt">{s.label}</td>
                  <td>{s.graded}</td>
                  <td>{s.exact}</td>
                  <td>{s.withinOne}</td>
                  <td>{s.meanPhone.toFixed(3)}</td>
                  <td>{s.meanFeature.toFixed(3)}</td>
                </tr>
              {/each}
            </tbody>
          </table>

          {#if grading.hasStages}
            <p class="caveat">
              Intermediate stages compare the derived snapshot at rule-time T against
              the target at stage-time T. If those timescales aren’t calibrated, the
              stage rows read low for an alignment reason, not a phonological one —
              only <strong>final</strong> is independent of that.
            </p>
          {/if}

          {#each grading.stages as s}
            <details class="grade-detail" open={s.label === "final"}>
              <summary>
                <span class="tgt">{s.label}</span>
                <span class="muted">{s.graded - s.exact} of {s.graded} differ</span>
              </summary>
              {#if s.misses.length}
                <table class="grade-misses">
                  <thead>
                    <tr><th>gloss</th><th>derived</th><th>target</th><th>d</th><th>fd</th></tr>
                  </thead>
                  <tbody>
                    {#each s.misses as m}
                      <tr>
                        <td>{m.gloss}</td>
                        <td class="form">{m.derived}</td>
                        <td class="form">{m.target}</td>
                        <td>{m.d}</td>
                        <td>{m.fd ?? "—"}</td>
                      </tr>
                    {/each}
                  </tbody>
                </table>
              {:else}
                <p class="muted">All {s.graded} graded words exact.</p>
              {/if}
            </details>
          {/each}
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
                {#if d.steps.some((s) => s.definition)}
                  <button
                    class="def-toggle"
                    class:active={openDefs[i]}
                    title="Show the rule definitions for this word"
                    onclick={() => (openDefs[i] = !openDefs[i])}>Definition</button
                  >
                {/if}
              </header>
              <div class="steps">
                {#each d.steps as s}
                  {#if s.timeHeader != null}
                    <div class="time-header">{s.timeHeader}</div>
                  {/if}
                  {#if s.heading}
                    <div class="rule-heading">
                      {s.heading}{#if s.definition && openDefs[i]}<span class="def">{s.definition}</span>{/if}
                    </div>
                  {/if}
                  <div class="step">
                    <span class="form">{s.before}</span>
                    <span class="arrow">→</span>
                    <span class="form">{s.after}</span>
                    {#if s.change}<span class="change">({s.change})</span>{/if}
                  </div>
                {/each}
              </div>
              <div class="surface">
                <span class="form">{d.surface}</span>
              </div>
            </article>
          {/each}
        {/if}
      </div>
      {/if}
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
        </div>
        <button class="docs-close" title="Close (Esc)" onclick={() => (docsOpen = false)}
          >×</button
        >
      </div>
      <div class="docs-body">{@html docsHtml}</div>
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
  .theme-toggle {
    display: flex;
    margin-left: 4px;
  }
  .theme-toggle button {
    font-size: var(--fs-label);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 3px 8px;
    border-radius: 0;
    margin-left: -1px;
  }
  .theme-toggle button:first-child {
    border-top-left-radius: 6px;
    border-bottom-left-radius: 6px;
    margin-left: 0;
  }
  .theme-toggle button:last-child {
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
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
    flex: 1 1 50%;
  }
  .right {
    flex: 1 1 50%;
  }
  .divider {
    width: 1px;
    background: var(--border);
    flex: none;
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
    font-size: 16px;
    line-height: 1.55;
    resize: none;
    tab-size: 4;
    white-space: pre;
    overflow: auto;
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
  .run-project {
    font-size: var(--fs-header);
    padding: 8px 22px;
    color: var(--accent);
    background: var(--accent-bg);
    border-color: var(--accent-border);
  }
  .run-prompt .muted {
    max-width: 30ch;
  }

  .view-tabs {
    display: inline-flex;
    gap: 4px;
  }
  .view-tabs button {
    font-size: var(--fs-body);
    padding: 4px 10px;
  }
  .save-result {
    margin-left: 8px;
  }

  .grade-summary,
  .grade-misses {
    border-collapse: collapse;
    width: 100%;
    font-size: var(--fs-body);
    font-variant-numeric: tabular-nums;
  }
  .grade-summary {
    margin-bottom: 14px;
  }
  .grade-summary th,
  .grade-summary td,
  .grade-misses th,
  .grade-misses td {
    border: 1px solid var(--border);
    padding: 4px 9px;
    text-align: right;
  }
  .grade-summary td.tgt,
  .grade-misses th,
  .grade-misses td:first-child {
    text-align: left;
  }
  .grade-summary thead th,
  .grade-misses thead th {
    color: var(--muted);
    font-weight: 600;
    text-align: right;
    background: var(--panel);
  }
  .grade-summary tr.final td {
    font-weight: 700;
    color: var(--text-h);
    border-top-width: 2px;
  }
  .grade-misses td.form {
    color: var(--text-h);
  }

  .caveat {
    font-size: var(--fs-body);
    color: var(--muted);
    border-left: 3px solid var(--border);
    padding: 6px 12px;
    margin: 0 0 16px;
  }

  .grade-detail {
    margin-bottom: 10px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
  }
  .grade-detail summary {
    cursor: pointer;
    display: flex;
    gap: 10px;
    align-items: baseline;
    padding: 4px 0;
    font-weight: 600;
    color: var(--text-h);
  }
  .grade-detail summary .muted {
    font-weight: 400;
  }
  .grade-detail .grade-misses {
    margin-top: 6px;
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
    padding-bottom: 8px;
    border-bottom: 1px solid var(--muted);
  }
  .word-ipa {
    font-size: var(--fs-emphasis);
    font-weight: 700;
    color: var(--text-h);
  }
  .gloss {
    font-size: var(--fs-body);
    color: var(--muted);
    font-style: italic;
  }
  .def-toggle {
    margin-left: auto;
    align-self: center;
    font-family: var(--sans); /* UI chrome, not the IPA font inherited from .results.ipa */
    font-size: var(--fs-label);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 3px 8px;
  }

  .steps {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  .rule-heading {
    margin: 10px 0 2px;
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
  }
  .time-header {
    margin: 18px 0 3px;
    padding-bottom: 3px;
    border-bottom: 1px solid var(--border);
    font-size: var(--fs-header);
    font-weight: 600;
    color: var(--text-h);
  }
  .rule-heading .def {
    display: block;
    margin-top: 2px;
    font-family: var(--mono);
    font-size: var(--fs-body);
    font-weight: 400;
    color: var(--muted);
  }
  .step {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 8px;
    padding-left: 16px;
    font-size: var(--fs-emphasis);
    color: var(--text-h);
  }
  .arrow {
    color: var(--muted);
  }
  .change {
    color: var(--muted);
  }

  .surface {
    display: flex;
    align-items: baseline;
    gap: 8px;
    margin-top: 12px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
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
  .err-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
  }
  .ok-dot {
    background: #2faa5b;
  }
  .err-dot {
    background: var(--error);
  }

  @media (max-width: 800px) {
    .panels {
      flex-direction: column;
    }
    .divider {
      width: auto;
      height: 1px;
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

  /* Rendered markdown (dynamic {@html}, so :global) */
  .docs-body :global(h1) {
    font-size: 22px;
    color: var(--text-h);
    margin: 18px 0 10px;
  }
  .docs-body :global(h2) {
    font-size: 18px;
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
    font-size: 14px;
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
