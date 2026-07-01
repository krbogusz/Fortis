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

// Python helper loaded into the interpreter after the engine is importable.
// Rendering mirrors ../src/fortis/main.py:_print_derivation.
const HELPER = `
import json, re
from pathlib import Path
from src.fortis.loaders.project import load_project
from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.rendering import render_syllabified, describe_change
from src.fortis.application.tiers import lower_tiers
from src.fortis.application.diagram import render_autosegmental, render_change, render_geometry_tree
_SUB = re.compile(r"#\\d+$")
INV = "/work/default"
def read_file(name): return (Path(INV)/name).read_text(encoding="utf-8")
def write_file(name, text): (Path(INV)/name).write_text(text, encoding="utf-8")
def run_derivations():
    res = load_project(Path(INV))
    if res.is_err(): return json.dumps({"error": res.unwrap_err()})
    project = res.unwrap()
    try: rules = resolve_rule_letters(project.rules, project)
    except ValueError as e: return json.dumps({"error":[str(e)]})
    out, R = [], lambda f,b: render_syllabified(lower_tiers(f), b, project)
    for ipa, word in project.words.items():
        d = derive(word, string_to_sequence(ipa, project), rules, project.letters,
                   project.features, project.sonorities, project.syllable_parts, project.tiers)
        steps, prev, prev_time = [], None, object()  # prev_time sentinel ⇒ first time emits a header
        has_tiers = any(t.autosegs for t in d.input.tiers.values())
        frames = []
        for s in d.steps:
            base = _SUB.sub("", s.rule.id)
            heading = (s.rule.name or base) if base!=prev else None
            time_header = s.rule.time if (s.rule.time is not None and s.rule.time != prev_time) else None
            prev, prev_time = base, s.rule.time
            steps.append({"timeHeader":time_header,"heading":heading,"definition":s.rule.raw_definition,
                          "time":s.rule.time,"name":s.rule.name or base,
                          "before":R(s.before,s.before_boundaries),"after":R(s.after,s.after_boundaries),
                          "change":describe_change(lower_tiers(s.before),lower_tiers(s.after),project)})
            lbl = (str(s.rule.time)+": " if s.rule.time is not None else "")+(s.rule.name or base)
            for sublabel, diagram in render_change(s.before, s.after, s.rule, project):  # tier + spreads
                frames.append({"label": lbl + (" · " + sublabel if sublabel else ""), "diagram":diagram})
        # The change diagrams already show before→after, so separate Input/Surface melody snapshots
        # are redundant. Keep an Input melody only for a tier word with no change (else it'd be blank).
        if not frames and has_tiers:
            frames.append({"label":"Input","diagram":render_autosegmental(d.input,project)})
        autoseg = bool(frames)  # any autosegmental content: a change diagram or the lone-melody snapshot
        input_geometry = [render_geometry_tree(seg.bundle, project) for seg in d.input.segments]
        output_geometry = [render_geometry_tree(seg.bundle, project) for seg in d.surface.segments]
        out.append({"ipa":ipa,"gloss":word.gloss,"surface":R(d.surface,d.surface_boundaries),
                    "steps":steps,"frames":frames,"autosegmental":autoseg,
                    "inputGeometry":input_geometry,"outputGeometry":output_geometry})
    return json.dumps({"derivations": out})
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

/** Read an inventory file from the Pyodide virtual filesystem. */
export function readFile(name) {
  const fn = py.globals.get("read_file");
  try {
    return fn(name);
  } finally {
    fn.destroy();
  }
}

/** Write an inventory file into the Pyodide virtual filesystem. */
export function writeFile(name, text) {
  const fn = py.globals.get("write_file");
  try {
    fn(name, text);
  } finally {
    fn.destroy();
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
