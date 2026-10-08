// Browser-side bridge to the Fortis engine: the Rust crate in ../rust/web, compiled to
// WebAssembly and run in a Web Worker (src/lib/engine.worker.js).
//
// The project files stay here on the main thread, so reading and editing them is synchronous.
// Two maps mirror the CLI's project/fallback model: `defaults` is the pristine shipped
// projects/default, and `overlay` is what the user has customized (initially empty, so
// everything falls back to the default, like load_project() with no project directory).
// Editing or loading a file always writes into the overlay. The worker gets a copy of the
// overlay with the first engine call after a change. The reports each call writes land in
// `reports`, keyed "reports/<name>" like the CLI's <project>/reports/.

export const FILES = [
  "features.toml",
  "letters.csv",
  "diacritics.toml",
  "diacritics.csv",
  "sonorities.toml",
  "sonorities.csv",
  "syllable_parts.toml",
  "tiers.toml",
  "words.toml",
  "words.csv",
  "rules.toml",
  "rules.csv",
  "settings.toml",
];

// Generated reports, read-only — written by each run into `reports`.
export const OUTPUT_FILES = [
  "reports/derivations.csv",
  "reports/derivation_matrix.csv",
  "reports/rule_firings.csv",
];

// Each dual-format pair: a project uses the .toml or the .csv, never both.
const DUAL_FORMAT = [
  ["words.toml", "words.csv"],
  ["rules.toml", "rules.csv"],
  ["diacritics.toml", "diacritics.csv"],
  ["sonorities.toml", "sonorities.csv"],
];

const defaults = new Map();
const overlay = new Map();
const reports = new Map();
let overlayVersion = 0; // bumped on every overlay change
let sentVersion = -1; // the overlay version the worker holds

let worker = null;
let nextId = 0;
const pending = new Map(); // call id → {resolve, reject}
let manifest = null; // projects/index.json

// Resolve against document.baseURI so the assets load under a GitHub Pages project subpath
// (vite base "./" emits no <base> tag, so this is the page URL).
const asset = (path) => new URL(path, document.baseURI).href;

async function fetchText(path) {
  const res = await fetch(asset(path));
  if (!res.ok) throw new Error(`Could not fetch ${path} (${res.status})`);
  return res.text();
}

function call(method, ...args) {
  const message = { id: ++nextId, method, args };
  if (sentVersion !== overlayVersion) {
    message.overlay = Object.fromEntries(overlay);
    sentVersion = overlayVersion;
  }
  return new Promise((resolve, reject) => {
    pending.set(message.id, { resolve, reject });
    worker.postMessage(message);
  });
}

function onReply({ data }) {
  const caller = pending.get(data.id);
  pending.delete(data.id);
  if (data.error !== undefined) {
    caller.reject(new Error(data.error));
    return;
  }
  for (const [name, text] of Object.entries(data.reports ?? {})) {
    if (text === null) reports.delete("reports/" + name); // a stale report from an earlier run
    else reports.set("reports/" + name, text);
  }
  caller.resolve(data.result);
}

/**
 * Load the default project and start the engine worker.
 * @param {(msg: string) => void} [onStatus] progress callback
 */
export async function initEngine(onStatus = () => {}) {
  if (worker) return;
  onStatus("Loading the default project…");
  manifest = JSON.parse(await fetchText("projects/index.json"));
  for (const name of manifest.default ?? []) defaults.set(name, await fetchText(`projects/default/${name}`));

  onStatus("Starting the engine…");
  worker = new Worker(asset("engine/worker.js"), { type: "module" });
  worker.onmessage = onReply;
  worker.onerror = (e) => {
    for (const caller of pending.values()) caller.reject(new Error(e.message || "The engine worker failed"));
    pending.clear();
  };
  await call("init", Object.fromEntries(defaults));
  onStatus("Ready");
}

/** The editable project filenames (the inventories plus settings.toml). */
export function listFiles() {
  return [...FILES];
}

/** The generated (read-only) report filenames, written after each run. */
export function listOutputFiles() {
  return [...OUTPUT_FILES];
}

/** A project file (the overlay's, else the default's) or a report; "" if there is none. */
export function readFile(name) {
  if (name.startsWith("reports/")) return reports.get(name) ?? "";
  return overlay.get(name) ?? defaults.get(name) ?? "";
}

/** Write a file into the overlay (marks it as a project file). */
export function writeFile(name, text) {
  overlay.set(name, text);
  overlayVersion++;
}

/** Remove a file from the overlay, reverting it to the shipped default. */
export function removeFile(name) {
  if (overlay.delete(name)) overlayVersion++;
}

/** Clear the whole overlay and the reports — every file reverts to the shipped default. */
export function resetOverlay() {
  overlay.clear();
  reports.clear();
  overlayVersion++;
}

/**
 * The source of each project file: "project" (in the overlay), "default" (only in the shipped
 * default), or "absent". For each dual-format pair the file the loader does not use is forced
 * absent, so the .toml and .csv never both show a tab: the loader takes the overlay's .toml,
 * else the overlay's .csv, else the default's .toml.
 * @returns {Record<string, "project"|"default"|"absent">}
 */
export function fileStatus() {
  const source = (name) => (overlay.has(name) ? "project" : defaults.has(name) ? "default" : "absent");
  const out = Object.fromEntries(FILES.map((name) => [name, source(name)]));
  for (const pair of DUAL_FORMAT) {
    const keep = pair.find((name) => overlay.has(name)) ?? pair[0];
    for (const name of pair) if (name !== keep) out[name] = "absent";
  }
  return out;
}

/**
 * List the bundled example projects from the static manifest.
 * @returns {Promise<Array<{dir: string, label: string, files: string[]}>>}
 *   empty array if the manifest has none.
 */
export async function listExampleProjects() {
  return Array.isArray(manifest?.projects) ? manifest.projects : [];
}

/**
 * Load a bundled example project into the overlay: clears the overlay, then
 * fetches each of its inventory files and writes it in. Files the project does
 * not supply fall back to the shipped default, exactly like the CLI loader.
 * @param {{dir: string, files: string[]}} entry a manifest entry
 */
export async function loadExampleProject(entry) {
  resetOverlay(); // loading a project REPLACES the current one, not merges into it
  for (const name of entry.files) writeFile(name, await fetchText(`projects/${entry.dir}/${name}`));
}

/**
 * Derive a single word (by id, IPA or gloss), independent of the batched full run.
 * @returns {Promise<{found: boolean, ipa: string, gloss: string, derivations: Array,
 *   accuracy: object|null, errors: object|null, errorContext: object|null,
 *   blame: object|null}|{error: string[]}>}
 */
export function runSingle(word) {
  return call("run_single", word);
}

/**
 * Diagnostics: the inventory segments a feature bundle matches (the engine's own denotation),
 * read from the current overlay so it reflects unsaved feature-system edits.
 * @param {string} bundle a feature bundle, e.g. "+front, +sonorant, -syllabic"
 * @returns {Promise<{matched: string[], total: number}|{error: string}>}
 */
export function queryClasses(bundle) {
  return call("query_classes", bundle);
}

/**
 * Diagnostics: the feature geometry as a tree — the segmental hierarchy under ROOT plus the
 * suprasegmental tier features — read from the current overlay so it reflects unsaved edits.
 * @returns {Promise<{root: object, tiers: object[]}|{error: string}>} nodes are
 *   {name, kind, values: string|null, children: node[]}
 */
export function featureTree() {
  return call("feature_tree");
}

// Batched run API — the caller drives a run in slices and paints a progress bar between them.

/**
 * Begin a run: load the project and derive every word.
 * @returns {Promise<{words: number, rules: number}|{error: string[]}>}
 */
export function prepareRun() {
  return call("prepare_run");
}

/**
 * Render a slice of the run's derivations.
 * @returns {Promise<Array>} the derivation cards for words [start, start+count).
 */
export function deriveBatch(start, count) {
  return call("derive_batch", start, count);
}

/**
 * Set up the post-derivation analysis so the caller can drive it step by step (and paint a
 * progress bar between steps). The results come back from the final {@link analysisStep} call.
 * @returns {Promise<{steps: string[], result: object|null}>} the step labels (empty when
 *   superseded), and a ready result only when there was nothing to run.
 */
export function finalizeRun() {
  return call("finalize_run");
}

/**
 * Run the next analysis step (call in a loop over {@link finalizeRun}'s steps).
 * @returns {Promise<{done: number, total: number, result: object|null}>} the full analysis
 *   summary (accuracy, errors, errorContext, blame, warnings, unfiredRules, unsatisfiable,
 *   dependencies, analysisMs) on the final step, otherwise null.
 */
export function analysisStep() {
  return call("analysis_step");
}
