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

// Generated reports, read-only — written by run_derivations() into the overlay's
// reports/ subfolder (mirroring the CLI's <project>/reports/) after each run.
export const OUTPUT_FILES = ["reports/derivations.csv", "reports/derivation_table.csv"];

// Python helper loaded into the interpreter after the engine is importable.
// Rendering mirrors ../src/fortis/main.py:_trace_lines.
//
// Two directories mirror the CLI's project/fallback model: DEFAULT is the
// pristine shipped project/default (read-only, from the bundle); OVERLAY is
// what the user has customized (initially empty ⇒ everything falls back to
// DEFAULT, exactly like load_project() with no project_dir). Editing or
// loading a file always writes into OVERLAY, never DEFAULT.
const HELPER = `
import json, re, time, shutil
from pathlib import Path
from src.fortis.loaders.project import load_project
from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.rendering import render_syllabified, describe_change
from src.fortis.application.tiers import lower_tiers
from src.fortis.analysis.accuracy import accuracy_by_stage, measure_accuracy, distance_to_target, ingest_targets
from src.fortis.analysis.diagnosis import confusions, diagnose_stages, render_errors_csv, render_error_context_csv
from src.fortis.analysis.blame import blame_all, render_blame
from src.fortis.analysis.filtering import filter_by_pattern, filter_attested
from src.fortis.analysis.synthesis import render_scoped
from src.fortis.analysis.reporting import render_accuracy_csv, render_distance_to_target_csv
from src.fortis.analysis.warnings import syllabification_warnings, render_warnings
from src.fortis.main import _build_derivations_csv, _build_csv_report, _build_filtered_report
_SUB = re.compile(r"#\\d+$")
DEFAULT = "/work/projects/default"
OVERLAY = "/work/overlay"
Path(OVERLAY).mkdir(parents=True, exist_ok=True)
def _pick(name):
    p = Path(OVERLAY)/name
    return p if p.exists() else Path(DEFAULT)/name
def read_file(name):
    p = _pick(name)
    return p.read_text(encoding="utf-8") if p.exists() else ""
def write_file(name, text): (Path(OVERLAY)/name).write_text(text, encoding="utf-8")
def remove_file(name):
    p = Path(OVERLAY)/name
    if p.exists(): p.unlink()
def reset_overlay():
    for p in Path(OVERLAY).iterdir():
        if p.is_dir(): shutil.rmtree(p, ignore_errors=True)  # e.g. the reports/ subfolder
        else: p.unlink()
def _reports_dir():
    # The reports/ subfolder of the overlay, mirroring the CLI's <project>/reports/.
    d = Path(OVERLAY)/"reports"
    d.mkdir(parents=True, exist_ok=True)
    return d
def _active_of(toml_name, csv_name):
    # The file load_project() actually uses for a toml/csv pair: overlay TOML, else overlay
    # CSV, else the shipped default's TOML (mirrors pick_words/pick_rules in load_project).
    for f in (toml_name, csv_name):
        if (Path(OVERLAY)/f).exists(): return f
    return toml_name
def file_status(names):
    # "project" (in the overlay), "default" (only in the shipped default), or "absent"
    # (in neither). For each dual-format pair (words, rules) the non-effective file is forced
    # absent so the .toml and .csv never both show a tab — the UI hides absent files.
    def _src(name):
        if (Path(OVERLAY)/name).exists(): return "project"
        if (Path(DEFAULT)/name).exists(): return "default"
        return "absent"
    out = {name: _src(name) for name in names}
    for toml_name, csv_name in (
        ("words.toml", "words.csv"), ("rules.toml", "rules.csv"),
        ("diacritics.toml", "diacritics.csv"), ("sonorities.toml", "sonorities.csv"),
    ):
        keep = _active_of(toml_name, csv_name)
        for f in (toml_name, csv_name):
            if f in out and f != keep:
                out[f] = "absent"
    return json.dumps(out)
# A run is split so the UI can paint a progress bar between word batches:
# prepare_run() parses the project once; derive_batch(start,count) renders a
# slice (accumulating raw derivations for the reports); finalize_run() writes
# the reports. _SESSION carries state across these calls (Python globals persist
# across runPython). run_derivations() composes them for one-shot callers.
_SESSION = {}
# The last completed run (project + derivations + rules), so the interactive Filter tab
# can run over it without re-deriving. Set at finalize; cleared when a new run starts.
_LAST = {}

def _card(d, project):
    # One word's rendered derivation trace (the Derivations-tab card shape).
    R = lambda f,b: render_syllabified(lower_tiers(f), b, project)
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
    # A leading "input" pseudo-step: how the raw lexicon IPA is syllabified/normalised on import
    # (raw string -> the form the first rule sees, or the surface if nothing fired).
    syllabified_input = steps[0]["before"] if steps else R(d.surface, d.surface_boundaries)
    steps.insert(0, {"timeHeader":None,"heading":"Input","definition":None,"time":None,
                     "name":"Input","before":d.word.ipa,"after":syllabified_input,"change":""})
    return {"ipa":d.word.ipa,"gloss":d.word.gloss,"surface":R(d.surface,d.surface_boundaries),"steps":steps}

def _derive_one(project, rules, ipa, word):
    d = derive(word, string_to_sequence(ipa, project), rules, project.letters,
               project.features, project.sonorities, project.syllable_parts, project.tiers)
    return d, _card(d, project)

def prepare_run():
    res = load_project(Path(OVERLAY))
    if res.is_err(): return json.dumps({"error": res.unwrap_err()})
    project = res.unwrap()
    try: rules = resolve_rule_letters(project.rules, project)
    except ValueError as e: return json.dumps({"error":[str(e)]})
    _SESSION.clear()
    _LAST.clear()  # a new run invalidates the Filter cache
    _SESSION.update(project=project, rules=rules, words=list(project.words.items()), acc=[])
    n_rules = sum(len(rules_at_time) for rules_at_time in project.rules.values())
    return json.dumps({"words": len(_SESSION["words"]), "rules": n_rules})

def derive_batch(start, count):
    if "project" not in _SESSION: return json.dumps([])  # session superseded/cleared — caller aborts
    project, rules = _SESSION["project"], _SESSION["rules"]
    out = []
    for ipa, word in _SESSION["words"][start:start+count]:
        d, rendered = _derive_one(project, rules, ipa, word)
        _SESSION["acc"].append(d)
        out.append(rendered)
    return json.dumps(out)

def _accuracy_summary(acc, project):
    # None when the lexicon carries no attested forms; otherwise a per-target
    # (each stage + final) summary with the words that differ, for the UI to render.
    if not any(d.word.final is not None or d.word.stages for d in acc):
        return None
    stages = accuracy_by_stage(acc, project)
    final = next((s for s in stages if s.time is None), None)
    weighted = None  # a token-weighted final headline, only when frequencies vary
    if final is not None and final.report.frequencies_vary:
        r = final.report
        weighted = {"accuracy": round(r.weighted_accuracy, 4),
                    "meanPhone": round(r.weighted_mean_distance, 3),
                    "meanFeature": round(r.weighted_mean_feature_distance, 3),
                    "weight": r.weight}
    return {
        "hasStages": any(s.time is not None for s in stages),
        "weighted": weighted,
        "stages": [{
            "label": s.label,
            "assessed": s.report.assessed,
            "exact": s.report.exact,
            "withinOne": s.report.within_one,
            "meanPhone": round(s.report.mean_distance, 3),
            "meanFeature": round(s.report.mean_feature_distance, 3),
            "misses": [{"gloss": g.gloss or g.ipa, "derived": g.derived, "target": g.target,
                        "d": g.distance, "fd": g.feature_distance}
                       for g in sorted(s.report.distances, key=lambda g: (g.gloss or g.ipa).lower())
                       if not g.exact],
        } for s in stages],
    }

def _confusions_json(cs):
    return [{"expected": c.expected, "got": c.got, "count": c.count,
             "kind": c.kind, "examples": list(c.examples)} for c in cs]

def _autopsy_json(aus, top):
    return [{"segment": a.phone, "errors": a.errors, "total": a.total,
             "supportFloor": a.support_floor,
             "predictors": [{"predictor": x.predictor, "phi": round(x.phi, 2),
                             "fscore": round(x.fscore, 2),
                             "errHere": x.err_here, "okHere": x.ok_here,
                             "errAway": x.err_away, "okAway": x.ok_away}
                            for x in a.associations if x.phi > 0][:top]}
            for a in aus]

def _errors_summary(stages):
    # The Errors analysis: which segments came out wrong at each stage (and the final).
    # None when every assessed word is exact at every stage.
    if not any(s.confusions for s in stages):
        return None
    return {"stages": [{"label": s.label, "time": s.time,
                        "confusions": _confusions_json(s.confusions)}
                       for s in stages if s.confusions]}

def _error_context_summary(stages, project):
    # The Error-context analysis: per stage, per erroring segment, the environment
    # predictors positively associated with the error. None when nothing is associated.
    top = project.settings.diagnosis.report_top
    staged = []
    for s in stages:
        segments = [seg for seg in _autopsy_json(s.autopsy, top) if seg["predictors"]]
        if segments:
            staged.append({"label": s.label, "time": s.time, "segments": segments})
    return {"stages": staged} if staged else None

def _blame_summary(blames):
    # None when every assessed word is exact; else per wrong word its residuals (with
    # the culprit rule), stage divergence, and distance trajectory.
    if not blames:
        return None
    return {"words": [{
        "word": b.gloss or b.ipa, "surface": b.surface, "target": b.target, "distance": b.distance,
        "residuals": [{"expected": r.expected, "got": r.got, "culprit": r.culprit,
                       "time": r.culprit_time, "attributed": r.attributed, "kind": r.kind}
                      for r in b.residuals],
        "stage": ({"time": b.stage_divergence.time, "attested": b.stage_divergence.attested,
                   "derived": b.stage_divergence.derived} if b.stage_divergence else None),
        "trajectory": [{"label": p.label, "time": p.time, "form": p.form, "target": p.target,
                        "distance": p.distance, "fd": p.feature_distance, "regressed": p.regressed}
                       for p in b.trajectory],
    } for b in blames]}

def _write_or_clear(path, text):
    if text is not None:
        path.write_text(text, encoding="utf-8")
    elif path.exists():
        path.unlink()  # remove a stale report from a run that produced one

def finalize_run():
    if "project" not in _SESSION:  # superseded
        return json.dumps({"accuracy": None, "errors": None, "errorContext": None, "blame": None, "warnings": []})
    project, rules, acc = _SESSION["project"], _SESSION["rules"], _SESSION["acc"]
    O = _reports_dir()  # every report mirrors the CLI's <project>/reports/ subfolder
    (O/"derivations.csv").write_text(_build_derivations_csv(acc, project), encoding="utf-8")
    (O/"derivation_table.csv").write_text(_build_csv_report(acc, rules, project), encoding="utf-8")

    _t0 = time.perf_counter()
    ingest_targets(acc, project)  # segment attested forms once before any analysis reads them
    accuracy = _accuracy_summary(acc, project)
    # Machine-readable distance tables (only when the lexicon carries attested forms);
    # cleared otherwise so a run without targets leaves no stale CSV.
    stages = accuracy_by_stage(acc, project) if accuracy is not None else None
    _write_or_clear(O/"accuracy.csv", render_accuracy_csv(stages) if stages is not None else None)
    _write_or_clear(O/"distance_to_target.csv", render_distance_to_target_csv(stages) if stages is not None else None)
    _t_accuracy = time.perf_counter()
    # Errors + Error context, per attested stage (and the final); complete CSVs, capped JSON.
    stage_diag = diagnose_stages(acc, project) if accuracy is not None else None
    _write_or_clear(O/"errors.csv", render_errors_csv(stage_diag) if stage_diag is not None else None)
    _write_or_clear(O/"error_context.csv", render_error_context_csv(stage_diag) if stage_diag is not None else None)
    errors = _errors_summary(stage_diag) if stage_diag is not None else None
    error_context = _error_context_summary(stage_diag, project) if stage_diag is not None else None
    blames = blame_all(acc, project)
    blame = _blame_summary(blames)
    _write_or_clear(O/"blame.md", render_blame(blames, "the current project") if blame else None)

    warns = syllabification_warnings(acc, project)
    _write_or_clear(O/"warnings.md", render_warnings(warns, "the current project") if warns else None)
    warnings = [{"word": w.ipa, "gloss": w.gloss, "form": w.form,
                 "clusters": list(w.clusters), "syllabified": w.syllabified} for w in warns]
    _t_end = time.perf_counter()
    _LAST.update(project=project, rules=rules, derivations=list(acc))  # for the Filter tab
    _SESSION.clear()
    return json.dumps({"accuracy": accuracy, "errors": errors, "errorContext": error_context,
                       "blame": blame, "warnings": warnings,
                       "accuracyMs": round((_t_accuracy - _t0) * 1000), "analysisMs": round((_t_end - _t_accuracy) * 1000)})

def run_filter(pattern):
    # Interactive filter over the last completed run — matches the pattern against every
    # form each word takes, writes filtered_output.md/filtered_table.csv, and returns the
    # matched words (trace card + where-matched + measurement) for the Filter tab.
    if "project" not in _LAST:
        return json.dumps({"error": ["Run the project first, then filter."]})
    project, rules, derivations = _LAST["project"], _LAST["rules"], _LAST["derivations"]
    res = filter_by_pattern(derivations, pattern, project)
    if res.is_err():
        return json.dumps({"error": res.unwrap_err()})
    result = res.unwrap()
    matched_derivs = [m.derivation for m in result.matched]
    O = _reports_dir()
    O.joinpath("filtered_output.md").write_text(
        _build_filtered_report(result, project, "the current project"), encoding="utf-8")
    O.joinpath("filtered_table.csv").write_text(
        _build_csv_report(matched_derivs, rules, project), encoding="utf-8")

    report = measure_accuracy(matched_derivs, project)
    accuracy = None
    confusions_json = []
    if report.assessed:
        accuracy = {"exact": report.exact, "assessed": report.assessed,
                   "accuracy": round(report.accuracy, 4), "meanPhone": round(report.mean_distance, 3)}
        confusions_json = _confusions_json(confusions(report.distances))
    words = []
    for m in result.matched:
        g = distance_to_target(m.derivation, project)
        words.append({"card": _card(m.derivation, project),
                      "locations": [loc.label for loc in m.locations],
                      "measurement": ({"target": g.target, "distance": g.distance, "exact": g.exact} if g else None)})
    return json.dumps({"pattern": pattern, "matched": len(result.matched),
                       "considered": result.considered, "accuracy": accuracy,
                       "confusions": confusions_json, "words": words})

def run_scope(pattern):
    # Restrict the accuracy analyses to the words whose attested forms match the pattern:
    # write scoped_output.md, and return the subset accuracy headline + errors.
    if "project" not in _LAST:
        return json.dumps({"error": ["Run the project first, then scope."]})
    project, derivations = _LAST["project"], _LAST["derivations"]
    res = filter_attested(derivations, pattern, project)
    if res.is_err():
        return json.dumps({"error": res.unwrap_err()})
    result = res.unwrap()
    subset = list(result.matched)
    where = "the current project · scope '" + pattern + "': " + str(len(subset)) + "/" + str(result.considered) + " words"
    _reports_dir().joinpath("scoped_output.md").write_text(render_scoped(subset, project, where), encoding="utf-8")
    report = measure_accuracy(subset, project)
    accuracy = None
    errors = None
    if report.assessed:
        accuracy = {"exact": report.exact, "assessed": report.assessed,
                   "accuracy": round(report.accuracy, 4), "meanPhone": round(report.mean_distance, 3)}
        errors = _errors_summary(diagnose_stages(subset, project))
    return json.dumps({"pattern": pattern, "matched": len(subset), "considered": result.considered,
                       "accuracy": accuracy, "errors": errors})

def run_derivations():
    prep = json.loads(prepare_run())
    if "error" in prep: return json.dumps(prep)
    out = []
    for i in range(0, prep["words"], 64):
        out.extend(json.loads(derive_batch(i, 64)))
    fin = json.loads(finalize_run())
    return json.dumps({"derivations": out, "accuracy": fin.get("accuracy"),
                       "errors": fin.get("errors"), "errorContext": fin.get("errorContext"),
                       "blame": fin.get("blame"), "warnings": fin.get("warnings"),
                       "accuracyMs": fin.get("accuracyMs"), "analysisMs": fin.get("analysisMs")})
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

/** The 9 editable project filenames (8 inventories + settings.toml). */
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

/** @returns {Record<string, "default"|"project">} source of each of the 9 project files. */
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
 * Finish a run: write the reports from the accumulated derivations and measure them.
 * @returns {{accuracy: object|null, errors: object|null, errorContext: object|null, blame: object|null, warnings: Array<object>}}
 *   the accuracy summary, the errors (per-stage confusions), the error context
 *   (per-stage per-segment autopsy), the per-word blame, and any
 *   syllabification-fallback warnings — the first four are null when the lexicon carries
 *   no attested forms or every word is exact.
 */
export function finalizeRun() {
  const fn = py.globals.get("finalize_run");
  try {
    return JSON.parse(fn());
  } finally {
    fn.destroy();
  }
}

/**
 * Filter the last completed run: match PATTERN against every form each word takes and
 * return the matched words (trace card + where-matched + measurement). Also writes
 * filtered_output.md / filtered_table.csv into the overlay.
 * @param {string} pattern a Fortis sequence pattern
 * @returns {{pattern: string, matched: number, considered: number, accuracy: object|null,
 *   confusions: Array, words: Array}|{error: string[]}}
 */
export function runFilter(pattern) {
  const fn = py.globals.get("run_filter");
  try {
    return JSON.parse(fn(pattern));
  } finally {
    fn.destroy();
  }
}

/**
 * Scope the accuracy analyses to words whose attested forms match PATTERN: writes
 * scoped_output.md and returns the subset's accuracy headline + errors.
 * @param {string} pattern a Fortis sequence pattern
 * @returns {{pattern: string, matched: number, considered: number, accuracy: object|null,
 *   errors: object|null}|{error: string[]}}
 */
export function runScope(pattern) {
  const fn = py.globals.get("run_scope");
  try {
    return JSON.parse(fn(pattern));
  } finally {
    fn.destroy();
  }
}
