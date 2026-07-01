<script>
  import { onMount } from "svelte";
  import {
    initEngine,
    listFiles,
    listOutputFiles,
    readFile,
    writeFile,
    removeFile,
    resetOverlay,
    fileStatus,
    runDerivations,
  } from "./lib/engine.js";
  import CsvTable from "./lib/CsvTable.svelte";

  let ready = $state(false);
  let status = $state("Starting…");
  let initError = $state(null);

  let files = $state([]); // editable inventory filenames
  let outputFiles = $state([]); // generated report filenames (read-only)
  let fileSource = $state({}); // filename -> "default" | "project"
  let projectName = $state("default"); // title of the left panel
  let active = $state(null); // filename, from either files or outputFiles
  let content = $state(""); // viewer content for the active file
  let busy = $state(false); // a derivation run is in flight
  let reportsReady = $state(false); // true once run_derivations() has written the reports at least once

  let mode = $state("historical"); // "historical" | "autosegmental"
  let showDef = $state(false); // off by default: hide rule definitions to keep results uncluttered
  let result = $state(null); // { derivations } | { error }
  let csvMode = $state("table"); // csv view (letters.csv / output.csv): "table" | "raw"

  let fileInput; // single-file <input>
  let projectInput; // multi-file (folder) <input>

  let debounceTimer = null;

  const isOutput = (name) => outputFiles.includes(name);
  const defaultFiles = $derived(files.filter((f) => fileSource[f] !== "project"));
  const projectFiles = $derived(files.filter((f) => fileSource[f] === "project"));

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
      outputFiles = listOutputFiles();
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

  async function rerun() {
    if (!ready) return;
    busy = true;
    // Yield so the spinner paints before the (synchronous) Pyodide call.
    await new Promise((r) => setTimeout(r, 0));
    try {
      result = runDerivations();
      reportsReady = !result.error; // run_derivations() only writes the reports on success
      if (isOutput(active)) content = readFile(active); // keep an open report tab in sync
    } catch (e) {
      result = { error: [e?.message ?? String(e)] };
    } finally {
      busy = false;
    }
  }

  function onEdit() {
    writeFile(active, content);
    refreshStatus();
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(rerun, 400);
  }

  async function removeFileTab(name, ev) {
    ev.stopPropagation();
    removeFile(name);
    refreshStatus();
    if (active === name) content = readFile(name); // now shows the default content
    await rerun();
  }

  function saveActiveFile() {
    const blob = new Blob([content], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = active;
    a.click();
    URL.revokeObjectURL(url);
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

  async function loadProject(ev) {
    const incoming = Array.from(ev.target.files ?? []);
    resetOverlay(); // loading a project REPLACES the current one, not merges into it
    let written = 0;
    const skipped = [];
    for (const file of incoming) {
      const target = matchFile(file.name);
      if (!target) {
        skipped.push(file.name);
        continue;
      }
      writeFile(target, await file.text());
      written += 1;
    }
    const folder = incoming[0]?.webkitRelativePath?.split("/")[0];
    projectName = written && folder ? folder : "default";
    refreshStatus();
    // Refresh the editor with whatever the active file now is.
    selectFile(active);
    await rerun();
    let msg = `Loaded ${written} inventory file(s).`;
    if (skipped.length)
      msg += `\nIgnored (not inventory files): ${skipped.join(", ")}`;
    if (!written) msg = "No matching inventory files found in the selection.";
    alert(msg);
    ev.target.value = "";
  }
</script>

<div class="app">
  <header class="bar">
    <div class="brand">
      <strong>Fortis</strong>
      <span class="tag">phonology engine</span>
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
        <h2>{projectName}</h2>
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

      <div class="file-group-label">Reports</div>
      <div class="tabs">
        {#each outputFiles as f}
          <button
            class="tab report-tab"
            class:active={f === active}
            disabled={!ready || !reportsReady}
            title="Generated report — read only"
            onclick={() => selectFile(f)}>{f}</button
          >
        {/each}
      </div>

      {#if active === "letters.csv" || active === "output.csv"}
        <div class="view-bar">
          <span class="view-lbl">View</span>
          <button
            class:active={csvMode === "table"}
            disabled={!ready}
            onclick={() => (csvMode = "table")}>Table</button
          >
          <button
            class:active={csvMode === "raw"}
            disabled={!ready}
            onclick={() => (csvMode = "raw")}>Raw</button
          >
        </div>
      {/if}

      {#if (active === "letters.csv" || active === "output.csv") && csvMode === "table"}
        <CsvTable {content} />
      {:else if isOutput(active)}
        <textarea class="editor ipa" spellcheck="false" readonly value={content}
        ></textarea>
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
            <button
              class:active={showDef}
              disabled={!ready}
              onclick={() => (showDef = !showDef)}>Definition</button
            >
            <button
              class:active={mode === "historical"}
              disabled={!ready}
              onclick={() => (mode = "historical")}>Historical</button
            >
            <button
              class:active={mode === "autosegmental"}
              disabled={!ready}
              onclick={() => (mode = "autosegmental")}>Autosegmental</button
            >
            {#if busy}<span class="running"
                ><span class="spinner small"></span> running…</span
              >{/if}
          </div>
        </div>
        {#if mode === "autosegmental"}
          <p class="legend">
            Each rule as an association change: <code>│</code> kept ·
            <code>╎</code> added (spread / dock) · <code>╪</code> delinked
          </p>
        {/if}
      </div>

      <div class="results ipa">
        {#if !result}
          <p class="muted">No results yet.</p>
        {:else if result.error}
          <div class="card error">
            <h3>Error</h3>
            {#each result.error as line}
              <pre>{line}</pre>
            {/each}
          </div>
        {:else if result.derivations.length === 0}
          <p class="muted">No words in the project.</p>
        {:else if mode === "autosegmental"}
          {#each result.derivations as d}
            <details class="card auto-card" open={d.autosegmental}>
              <summary>
                <span class="word-ipa">{d.ipa}</span>
                {#if d.gloss}<span class="gloss">‘{d.gloss}’</span>{/if}
                {#if !d.autosegmental}<span class="flat-note">no autosegmental process</span>{/if}
              </summary>
              <div class="frames">
                {#if d.inputGeometry?.length}
                  <details class="geometry">
                    <summary>Input geometry — one tree per segment</summary>
                    <div class="frames">
                      {#each d.inputGeometry as tree}
                        <pre class="diagram">{tree}</pre>
                      {/each}
                    </div>
                  </details>
                {/if}
                {#each d.frames as f}
                  <div class="frame">
                    <span class="frame-lbl">{f.label}</span>
                    <pre class="diagram">{f.diagram}</pre>
                  </div>
                {/each}
                {#if d.outputGeometry?.length}
                  <details class="geometry">
                    <summary>Output geometry — one tree per segment</summary>
                    <div class="frames">
                      {#each d.outputGeometry as tree}
                        <pre class="diagram">{tree}</pre>
                      {/each}
                    </div>
                  </details>
                {/if}
              </div>
            </details>
          {/each}
        {:else}
          {#each result.derivations as d}
            <article class="card derivation">
              <header class="word-head">
                <span class="word-ipa">{d.ipa}</span>
                {#if d.gloss}<span class="gloss">‘{d.gloss}’</span>{/if}
              </header>
              <div class="steps">
                {#each d.steps as s}
                  {#if s.timeHeader != null}
                    <div class="time-header">{s.timeHeader}</div>
                  {/if}
                  {#if s.heading}
                    <div class="rule-heading">
                      {s.heading}{#if s.definition && showDef}<span class="def">{s.definition}</span>{/if}
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
    </section>
  </main>
</div>

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
  .report-tab {
    font-style: italic;
    color: var(--muted);
  }
  .report-tab.active {
    font-style: normal;
    color: inherit;
  }

  .view-bar {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 0 16px 8px;
    flex: none;
  }
  .view-lbl {
    font-size: var(--fs-label);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--muted);
  }
  .view-bar button {
    font-size: var(--fs-body);
    padding: 3px 10px;
  }

  .editor {
    flex: 1;
    margin: 0 16px 16px;
    padding: 12px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--code-bg);
    color: var(--text-h);
    font-size: var(--fs-body);
    line-height: 1.55;
    resize: none;
    tab-size: 4;
    white-space: pre;
    overflow: auto;
  }

  .running {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: var(--fs-body);
    color: var(--muted);
  }

  .results {
    flex: 1;
    overflow: auto;
    padding: 4px 16px 24px;
  }
  .muted {
    color: var(--muted);
  }

  .card {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 14px;
    background: var(--panel);
    box-shadow: var(--shadow);
  }
  .auto-card > summary {
    display: flex;
    align-items: baseline;
    gap: 10px;
    cursor: pointer;
    list-style: none;
  }
  .auto-card > summary::-webkit-details-marker {
    display: none;
  }
  .auto-card > summary::before {
    content: "▾";
    color: var(--muted);
    font-size: 11px;
  }
  .auto-card:not([open]) > summary::before {
    content: "▸";
  }
  .auto-card[open] > summary {
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--muted);
  }
  .flat-note {
    color: var(--muted);
    font-style: italic;
    font-size: var(--fs-body);
  }
  .frames {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .geometry {
    margin-top: 12px;
  }
  .geometry summary {
    cursor: pointer;
    font-family: var(--sans);
    font-size: var(--fs-body);
    color: var(--muted);
  }
  .geometry .frames {
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 10px;
  }
  .frame {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .frame-lbl {
    font-family: var(--sans);
    font-size: var(--fs-body);
    font-weight: 600;
    color: var(--accent);
  }
  .legend {
    font-size: var(--fs-body);
    color: var(--muted);
    margin: 0;
  }
  .legend code {
    font-family: var(--mono);
    font-size: var(--fs-body);
    color: var(--text-h);
    padding: 0 2px;
  }
  /* Diagrams must be monospace for the box-drawing association lines to align. */
  .diagram {
    margin: 0;
    padding: 10px 14px;
    font-family: "DejaVu Sans Mono", "Noto Sans Mono", "JuliaMono", ui-monospace,
      monospace;
    font-size: var(--fs-body);
    line-height: 1.35;
    white-space: pre;
    color: var(--text-h);
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: auto;
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
  .spinner.small {
    width: 10px;
    height: 10px;
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
</style>
