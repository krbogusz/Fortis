// Browser-side bridge to the Fortis phonology engine running in Pyodide.
//
// We load Pyodide via a *runtime* dynamic import of the served file so Vite
// never tries to bundle pyodide.mjs (which references Node built-ins on its
// Node code path). The assets live in public/pyodide/ (copied by
// scripts/build-engine.mjs) and are addressed through import.meta.env.BASE_URL
// so everything works under a GitHub Pages subpath.

// Resolve against document.baseURI so paths are correct under a GH-Pages
// project subpath (vite base "./" emits no <base> tag, so this is the page URL).
const PYODIDE_URL = new URL("pyodide/pyodide.mjs", document.baseURI).href;
const PYODIDE_INDEX = new URL("pyodide/", document.baseURI).href;
const ENGINE_TGZ = new URL("engine.tgz", document.baseURI).href;
// Example projects live beside the app as static assets (built by
// scripts/build-engine.mjs). Resolve against document.baseURI so they load
// under a GitHub Pages project subpath, exactly like the assets above.
const EXAMPLES_INDEX = new URL("projects/index.json", document.baseURI).href;

export const FILES = [
  "features.toml",
  "letters.csv",
  "diacritics.toml",
  "sonorities.toml",
  "syllable_parts.toml",
  "tiers.toml",
  "words.toml",
  "rules.toml",
];

// Generated reports, read-only — written by run_derivations() after each run.
export const OUTPUT_FILES = ["output.md", "derivation_table.csv"];

// Python helper loaded into the interpreter after the engine is importable.
// Rendering mirrors ../src/fortis/main.py:_print_derivation.
//
// Two directories mirror the CLI's project/fallback model: DEFAULT is the
// pristine shipped project/default (read-only, from the bundle); OVERLAY is
// what the user has customized (initially empty ⇒ everything falls back to
// DEFAULT, exactly like load_project() with no project_dir). Editing or
// loading a file always writes into OVERLAY, never DEFAULT.
const HELPER = `
import json, re
from pathlib import Path
from src.fortis.loaders.project import load_project
from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.rendering import render_syllabified, describe_change
from src.fortis.application.tiers import lower_tiers
from src.fortis.analysis.grading import grade_stages
from src.fortis.main import _build_report, _build_csv_report
_SUB = re.compile(r"#\\d+$")
DEFAULT = "/work/projects/default"
OVERLAY = "/work/overlay"
Path(OVERLAY).mkdir(parents=True, exist_ok=True)
def _pick(name):
    p = Path(OVERLAY)/name
    return p if p.exists() else Path(DEFAULT)/name
def read_file(name): return _pick(name).read_text(encoding="utf-8")
def write_file(name, text): (Path(OVERLAY)/name).write_text(text, encoding="utf-8")
def remove_file(name):
    p = Path(OVERLAY)/name
    if p.exists(): p.unlink()
def reset_overlay():
    for p in Path(OVERLAY).iterdir():
        if p.is_file(): p.unlink()
def file_status(names):
    return json.dumps({name: ("project" if (Path(OVERLAY)/name).exists() else "default") for name in names})
# A run is split so the UI can paint a progress bar between word batches:
# prepare_run() parses the project once; derive_batch(start,count) renders a
# slice (accumulating raw derivations for the reports); finalize_run() writes
# the reports. _SESSION carries state across these calls (Python globals persist
# across runPython). run_derivations() composes them for one-shot callers.
_SESSION = {}

def _derive_one(project, rules, ipa, word):
    R = lambda f,b: render_syllabified(lower_tiers(f), b, project)
    d = derive(word, string_to_sequence(ipa, project), rules, project.letters,
               project.features, project.sonorities, project.syllable_parts, project.tiers)
    steps, prev, prev_time = [], None, object()  # prev_time sentinel ⇒ first time emits a header
    for s in d.steps:
        base = _SUB.sub("", s.rule.id)
        heading = (s.rule.name or base) if base!=prev else None
        time_header = s.rule.time if (s.rule.time is not None and s.rule.time != prev_time) else None
        prev, prev_time = base, s.rule.time
        steps.append({"timeHeader":time_header,"heading":heading,"definition":s.rule.raw_definition,
                      "time":s.rule.time,"name":s.rule.name or base,
                      "before":R(s.before,s.before_boundaries),"after":R(s.after,s.after_boundaries),
                      "change":describe_change(lower_tiers(s.before),lower_tiers(s.after),project)})
    return d, {"ipa":ipa,"gloss":word.gloss,"surface":R(d.surface,d.surface_boundaries),"steps":steps}

def prepare_run():
    res = load_project(Path(OVERLAY))
    if res.is_err(): return json.dumps({"error": res.unwrap_err()})
    project = res.unwrap()
    try: rules = resolve_rule_letters(project.rules, project)
    except ValueError as e: return json.dumps({"error":[str(e)]})
    _SESSION.clear()
    _SESSION.update(project=project, rules=rules, words=list(project.words.items()), acc=[])
    return json.dumps({"words": len(_SESSION["words"])})

def derive_batch(start, count):
    if "project" not in _SESSION: return json.dumps([])  # session superseded/cleared — caller aborts
    project, rules = _SESSION["project"], _SESSION["rules"]
    out = []
    for ipa, word in _SESSION["words"][start:start+count]:
        d, rendered = _derive_one(project, rules, ipa, word)
        _SESSION["acc"].append(d)
        out.append(rendered)
    return json.dumps(out)

def _grade_summary(acc, project):
    # None when the lexicon carries no attested forms; otherwise a per-target
    # (each stage + final) summary with the words that differ, for the UI to render.
    if not any(d.word.final is not None or d.word.stages for d in acc):
        return None
    stages = grade_stages(acc, project)
    return {
        "hasStages": any(s.time is not None for s in stages),
        "stages": [{
            "label": s.label,
            "graded": s.report.graded,
            "exact": s.report.exact,
            "withinOne": s.report.within_one,
            "meanPhone": round(s.report.mean_distance, 3),
            "meanFeature": round(s.report.mean_feature_distance, 3),
            "misses": [{"gloss": g.gloss or g.ipa, "derived": g.derived, "target": g.target,
                        "d": g.distance, "fd": g.feature_distance}
                       for g in sorted(s.report.grades, key=lambda g: (g.gloss or g.ipa).lower())
                       if not g.exact],
        } for s in stages],
    }

def finalize_run():
    if "project" not in _SESSION: return json.dumps({"grading": None})  # superseded run
    project, rules, acc = _SESSION["project"], _SESSION["rules"], _SESSION["acc"]
    (Path(OVERLAY)/"output.md").write_text(_build_report(acc, project, None), encoding="utf-8")
    (Path(OVERLAY)/"derivation_table.csv").write_text(_build_csv_report(acc, rules, project), encoding="utf-8")
    grading = _grade_summary(acc, project)
    _SESSION.clear()
    return json.dumps({"grading": grading})

def run_derivations():
    prep = json.loads(prepare_run())
    if "error" in prep: return json.dumps(prep)
    out = []
    for i in range(0, prep["words"], 64):
        out.extend(json.loads(derive_batch(i, 64)))
    fin = json.loads(finalize_run())
    return json.dumps({"derivations": out, "grading": fin.get("grading")})
`;

let py = null; // the Pyodide interpreter, set once initialised

/**
 * Load Pyodide, unpack the engine bundle, and load the Python helper.
 * @param {(msg: string) => void} [onStatus] progress callback
 */
export async function initEngine(onStatus = () => {}) {
  if (py) return;
  onStatus("Loading Python runtime (Pyodide)…");
  const { loadPyodide } = await import(/* @vite-ignore */ PYODIDE_URL);
  const interp = await loadPyodide({ indexURL: PYODIDE_INDEX });

  onStatus("Fetching phonology engine…");
  const res = await fetch(ENGINE_TGZ);
  if (!res.ok) throw new Error(`Could not fetch engine.tgz (${res.status})`);
  const buf = new Uint8Array(await res.arrayBuffer());

  onStatus("Unpacking engine…");
  interp.unpackArchive(buf, "gztar", { extractDir: "/work" });
  interp.runPython('import sys; sys.path.insert(0, "/work")');

  onStatus("Importing engine…");
  interp.runPython("import src.fortis");
  interp.runPython(HELPER);

  py = interp;
  onStatus("Ready");
}

/** The 8 editable inventory filenames. */
export function listFiles() {
  return [...FILES];
}

/** The generated (read-only) report filenames, written after each run_derivations(). */
export function listOutputFiles() {
  return [...OUTPUT_FILES];
}

/** Read an inventory file from the Pyodide virtual filesystem. */
export function readFile(name) {
  const fn = py.globals.get("read_file");
  try {
    return fn(name);
  } finally {
    fn.destroy();
  }
}

/** Write an inventory file into the overlay (marks it as a project file). */
export function writeFile(name, text) {
  const fn = py.globals.get("write_file");
  try {
    fn(name, text);
  } finally {
    fn.destroy();
  }
}

/** Remove a file from the overlay, reverting it to the shipped default. */
export function removeFile(name) {
  const fn = py.globals.get("remove_file");
  try {
    fn(name);
  } finally {
    fn.destroy();
  }
}

/** Clear the whole overlay — every file reverts to the shipped default. */
export function resetOverlay() {
  const fn = py.globals.get("reset_overlay");
  try {
    fn();
  } finally {
    fn.destroy();
  }
}

/** @returns {Record<string, "default"|"project">} source of each of the 8 inventory files. */
export function fileStatus() {
  const fn = py.globals.get("file_status");
  try {
    return JSON.parse(fn(FILES));
  } finally {
    fn.destroy();
  }
}

/**
 * List the bundled example projects from the static manifest.
 * @returns {Promise<Array<{dir: string, label: string, files: string[]}>>}
 *   empty array if the manifest is absent (e.g. no examples were bundled).
 */
export async function listExampleProjects() {
  try {
    const res = await fetch(EXAMPLES_INDEX);
    if (!res.ok) return [];
    const data = await res.json();
    return Array.isArray(data?.projects) ? data.projects : [];
  } catch {
    return [];
  }
}

/**
 * Load a bundled example project into the overlay: clears the overlay, then
 * fetches each of its inventory files and writes it in. Files the project does
 * not supply fall back to the shipped default, exactly like the CLI loader.
 * @param {{dir: string, files: string[]}} entry a manifest entry
 */
export async function loadExampleProject(entry) {
  resetOverlay(); // loading a project REPLACES the current one, not merges into it
  for (const name of entry.files) {
    const url = new URL(`projects/${entry.dir}/${name}`, document.baseURI).href;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Could not fetch ${entry.dir}/${name} (${res.status})`);
    writeFile(name, await res.text());
  }
}

/**
 * Run all derivations.
 * @returns {{derivations: Array}|{error: string[]}}
 */
export function runDerivations() {
  const fn = py.globals.get("run_derivations");
  try {
    return JSON.parse(fn());
  } finally {
    fn.destroy();
  }
}

// Batched run API — lets the caller drive derivations in slices and paint a
// progress bar between them (a single runDerivations() call would block the main
// thread for the whole run, so the bar could never update).

/**
 * Begin a run: parse the project and count its words.
 * @returns {{words: number}|{error: string[]}}
 */
export function prepareRun() {
  const fn = py.globals.get("prepare_run");
  try {
    return JSON.parse(fn());
  } finally {
    fn.destroy();
  }
}

/**
 * Derive a slice of words, accumulating them for the reports.
 * @returns {Array} the rendered derivations for words [start, start+count).
 */
export function deriveBatch(start, count) {
  const fn = py.globals.get("derive_batch");
  try {
    return JSON.parse(fn(start, count));
  } finally {
    fn.destroy();
  }
}

/**
 * Finish a run: write the reports from the accumulated derivations and grade them.
 * @returns {{grading: object|null}} the grading summary, or null when the lexicon
 *   carries no attested forms (nothing to grade against).
 */
export function finalizeRun() {
  const fn = py.globals.get("finalize_run");
  try {
    return JSON.parse(fn());
  } finally {
    fn.destroy();
  }
}
