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
export const OUTPUT_FILES = [
  "reports/derivations.csv",
  "reports/derivation_matrix.csv",
  "reports/rule_firings.csv",
];

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
from src.fortis.loaders.project import load_project, unfired_scoped_rules
from src.fortis.application.deriving import derive, resolve_rule_letters
from src.fortis.application.segmentation import string_to_sequence
from src.fortis.application.rendering import render_syllabified, describe_change
from src.fortis.application.diagram import render_change
from src.fortis.application.tiers import lower_tiers
from src.fortis.analysis.accuracy import accuracy_by_stage, measure_accuracy, distance_to_target, ingest_targets
from src.fortis.analysis.diagnosis import confusions, diagnose_stages, render_errors_csv, render_error_context_csv
from src.fortis.analysis.blame import blame_all, render_blame_csv
from src.fortis.analysis.reporting import render_accuracy_csv, render_distance_to_target_csv
from src.fortis.analysis.warnings import syllabification_warnings, render_warnings
from src.fortis.analysis.diagnostics import match_set, unsatisfiable_rules
from src.fortis.main import _build_derivations_csv, _build_matrix_csv, _build_rule_firings_csv
from src.fortis.analysis.dependencies import build_dependency_graph, dependency_layout, render_dependency_html
from src.fortis.models.inventories import Attestation, Word
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
                      "time":s.rule.time,"name":s.rule.name or base,"sporadic":bool(s.rule.words),
                      "before":R(s.before,s.before_boundaries),"after":R(s.after,s.after_boundaries),
                      "change":describe_change(lower_tiers(s.before),lower_tiers(s.after),project),
                      # [[sublabel, monospace diagram], …] for the rules using autosegmental
                      # mechanisms (~n spread / dock / delink); empty for all others. Drives the
                      # per-card AUTOSEGMENTAL toggle + its appearing rows.
                      "autosegmental":render_change(s.before,s.after,s.rule,project)})
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
    _SESSION.update(project=project, rules=rules, words=list(project.words.items()), acc=[])
    n_rules = sum(len(rules_at_time) for rules_at_time in project.rules.values())
    return json.dumps({"words": len(_SESSION["words"]), "rules": n_rules})

def derive_batch(start, count):
    if "project" not in _SESSION: return json.dumps([])  # session superseded/cleared — caller aborts
    project, rules = _SESSION["project"], _SESSION["rules"]
    out = []
    for _id, word in _SESSION["words"][start:start+count]:
        d, rendered = _derive_one(project, rules, word.seed.ipa, word)
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
    # Token-weighted numbers, only when frequencies vary (weighting is a no-op otherwise):
    # per-stage columns for the summary table, plus the total weight for the footnote.
    weighted = None
    if final is not None and final.report.frequencies_vary:
        weighted = {"weight": final.report.weight}
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
            "wtExact": round(s.report.weighted_accuracy, 4) if weighted else None,
            "wtPhone": round(s.report.weighted_mean_distance, 3) if weighted else None,
            "wtFeature": round(s.report.weighted_mean_feature_distance, 3) if weighted else None,
            "misses": [{"gloss": g.gloss or g.ipa, "derived": g.derived, "target": g.target,
                        "d": g.distance, "fd": g.feature_distance,
                        "matchesAt": g.matches_at, "closestAt": g.closest_at}
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
    # None when there are no assessed words; else per word its residuals (with the culprit
    # rule; empty for an exact word), stage divergence, and distance trajectory.
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

_EMPTY_ANALYSIS = {"accuracy": None, "errors": None, "errorContext": None, "blame": None,
                   "warnings": [], "unfiredRules": [], "unsatisfiable": [], "dependencies": None,
                   "analysisMs": 0}

def finalize_run():
    # Set up the post-derivation analysis so JS can drive it step by step (progress bar),
    # yielding to the browser between steps. Returns the step labels; the results accumulate
    # in _SESSION and come back from the final analysis_step().
    if "project" not in _SESSION:  # superseded before we started
        return json.dumps({"steps": [], "result": dict(_EMPTY_ANALYSIS)})
    _SESSION["_out"] = dict(_EMPTY_ANALYSIS)
    _SESSION["_step"] = 0
    _SESSION["_t0"] = time.perf_counter()
    _SESSION["_labels"] = ["derivations", "matrix", "rule firings", "feeding graph",
                           "accuracy", "errors", "blame", "warnings"]
    return json.dumps({"steps": _SESSION["_labels"], "result": None})

def analysis_step():
    # Run the next analysis step. JS calls this in a loop, painting the bar between calls.
    # Returns {done,total,result}; result is the full analysis JSON only on the last step.
    labels = _SESSION.get("_labels")
    if labels is None:  # superseded mid-analysis (a newer run cleared the session)
        return json.dumps({"done": 0, "total": 0, "result": dict(_EMPTY_ANALYSIS)})
    project, rules, acc = _SESSION["project"], _SESSION["rules"], _SESSION["acc"]
    O = _reports_dir()  # every report mirrors the CLI's <project>/reports/ subfolder
    out = _SESSION["_out"]
    k = _SESSION["_step"]
    if k == 0:
        (O/"derivations.csv").write_text(_build_derivations_csv(acc, project), encoding="utf-8")
    elif k == 1:
        (O/"derivation_matrix.csv").write_text(_build_matrix_csv(acc, rules, project), encoding="utf-8")
    elif k == 2:
        (O/"rule_firings.csv").write_text(_build_rule_firings_csv(acc, rules, project), encoding="utf-8")
    elif k == 3:
        _g = build_dependency_graph(acc, rules, project)  # the feeding graph (Tree tab)
        (O/"rule_dependencies.html").write_text(render_dependency_html(_g), encoding="utf-8")
        out["dependencies"] = dependency_layout(_g)
    elif k == 4:
        ingest_targets(acc, project)  # segment attested forms once before any analysis reads them
        out["accuracy"] = _accuracy_summary(acc, project)
        _stages = accuracy_by_stage(acc, project) if out["accuracy"] is not None else None
        _write_or_clear(O/"accuracy.csv", render_accuracy_csv(_stages) if _stages is not None else None)
        _write_or_clear(O/"distance_to_target.csv", render_distance_to_target_csv(_stages) if _stages is not None else None)
    elif k == 5:
        _diag = diagnose_stages(acc, project) if out["accuracy"] is not None else None
        _write_or_clear(O/"errors.csv", render_errors_csv(_diag) if _diag is not None else None)
        _write_or_clear(O/"error_context.csv", render_error_context_csv(_diag) if _diag is not None else None)
        out["errors"] = _errors_summary(_diag) if _diag is not None else None
        out["errorContext"] = _error_context_summary(_diag, project) if _diag is not None else None
    elif k == 6:
        _blames = blame_all(acc, project, include_exact=True)  # the Blame tab lists every assessed word
        out["blame"] = _blame_summary(_blames)
        _write_or_clear(O/"blame.csv", render_blame_csv(_blames) if out["blame"] else None)
    elif k == 7:
        _warns = syllabification_warnings(acc, project)
        _write_or_clear(O/"warnings.md", render_warnings(_warns, "the current project") if _warns else None)
        out["warnings"] = [{"word": w.ipa, "gloss": w.gloss, "form": w.form,
                            "clusters": list(w.clusters), "syllabified": w.syllabified} for w in _warns]
        out["unfiredRules"] = [{"rule": r, "word": w} for r, w in unfired_scoped_rules(rules, project.words)]
        out["unsatisfiable"] = [{"rule": u.rule, "role": u.role, "label": u.label, "reason": u.reason}
                                for u in unsatisfiable_rules(project)]
    _SESSION["_step"] = k + 1
    if _SESSION["_step"] >= len(labels):
        out["analysisMs"] = round((time.perf_counter() - _SESSION["_t0"]) * 1000)
        result = dict(out)
        _SESSION.clear()
        return json.dumps({"done": len(labels), "total": len(labels), "result": result})
    return json.dumps({"done": _SESSION["_step"], "total": len(labels), "result": None})

def _find_word(project, word_str):
    # Locate word_str by id, gloss or seed IPA; else a bare seed-only Word (no target).
    for word_id, w in project.words.items():
        if word_str in (word_id, w.gloss, w.seed.ipa):
            return w.seed.ipa, w, True
    return word_str, Word(id=word_str, forms={0: Attestation(ipa=word_str)}), False

def run_single(word_str):
    # Derive one word (independent of the batched full-run session): find it in the lexicon
    # by IPA key or gloss so it carries any attested/target forms, else derive it bare. Writes
    # the single_*.csv reports and returns the same shapes the full run does, for one word.
    res = load_project(Path(OVERLAY))
    if res.is_err(): return json.dumps({"error": res.unwrap_err()})
    project = res.unwrap()
    try: rules = resolve_rule_letters(project.rules, project)
    except ValueError as e: return json.dumps({"error":[str(e)]})
    word_str = (word_str or "").strip()
    if not word_str: return json.dumps({"error":["Enter a word to derive."]})
    ipa, word, found = _find_word(project, word_str)
    d, card = _derive_one(project, rules, ipa, word)
    acc = [d]
    O = _reports_dir()
    (O/"single_derivations.csv").write_text(_build_derivations_csv(acc, project), encoding="utf-8")
    ingest_targets(acc, project)  # segment the attested form (if any) before the analyses read it
    accuracy = _accuracy_summary(acc, project)
    stages = accuracy_by_stage(acc, project) if accuracy is not None else None
    _write_or_clear(O/"single_accuracy.csv", render_accuracy_csv(stages) if stages is not None else None)
    _write_or_clear(O/"single_distance_to_target.csv", render_distance_to_target_csv(stages) if stages is not None else None)
    stage_diag = diagnose_stages(acc, project) if accuracy is not None else None
    _write_or_clear(O/"single_errors.csv", render_errors_csv(stage_diag) if stage_diag is not None else None)
    _write_or_clear(O/"single_error_context.csv", render_error_context_csv(stage_diag) if stage_diag is not None else None)
    errors = _errors_summary(stage_diag) if stage_diag is not None else None
    error_context = _error_context_summary(stage_diag, project) if stage_diag is not None else None
    blames = blame_all(acc, project, include_exact=True)
    blame = _blame_summary(blames)
    _write_or_clear(O/"single_blame.csv", render_blame_csv(blames) if blame else None)
    return json.dumps({"found": found, "ipa": ipa, "gloss": word.gloss,
                       "derivations": [card], "accuracy": accuracy, "errors": errors,
                       "errorContext": error_context, "blame": blame})

def query_classes(bundle_str):
    # Diagnostics: which inventory segments a feature bundle matches, read fresh from the overlay
    # so the answer reflects the current (unsaved) feature system. Errors surface verbatim.
    res = load_project(Path(OVERLAY))
    if res.is_err():
        err = res.unwrap_err()
        return json.dumps({"error": "\\n".join(err) if isinstance(err, list) else str(err)})
    r = match_set(bundle_str or "", res.unwrap())
    if r.is_err(): return json.dumps({"error": r.unwrap_err()})
    ms = r.unwrap()
    return json.dumps({"matched": ms.matched, "total": ms.total})

def feature_tree():
    # Diagnostics: the feature geometry as a tree — the segmental hierarchy under ROOT plus the
    # suprasegmental tier features — read fresh from the overlay so it reflects the current
    # (unsaved) feature system.
    res = load_project(Path(OVERLAY))
    if res.is_err():
        err = res.unwrap_err()
        return json.dumps({"error": "\\n".join(err) if isinstance(err, list) else str(err)})
    features = res.unwrap().features
    def node(name):
        f = features[name]
        values = None
        if f.kind == "scalar":  # the scalar's levels, lowest first (binary/unary need no legend)
            values = ", ".join(f"{k} {v}" for k, v in sorted(f.values.items()))
        return {"name": name, "kind": str(f.kind), "values": values,
                "children": [node(c) for c in (f.children or ())]}
    tiers = [node(name) for name, f in features.items()
             if not features.is_segmental(name) and f.parent is None]
    return json.dumps({"root": node("root"), "tiers": tiers})

def run_derivations():
    # All-in-one convenience (the smoke test; the app drives the batched API itself):
    # derive every word, then drive the step-wise analysis to completion.
    prep = json.loads(prepare_run())
    if "error" in prep: return json.dumps(prep)
    out = []
    for i in range(0, prep["words"], 64):
        out.extend(json.loads(derive_batch(i, 64)))
    fin = json.loads(finalize_run())
    result = fin.get("result")
    while result is None:
        result = json.loads(analysis_step()).get("result")
    return json.dumps({"derivations": out, "accuracy": result.get("accuracy"),
                       "errors": result.get("errors"), "errorContext": result.get("errorContext"),
                       "blame": result.get("blame"), "warnings": result.get("warnings"),
                       "unfiredRules": result.get("unfiredRules"), "unsatisfiable": result.get("unsatisfiable"),
                       "dependencies": result.get("dependencies"), "analysisMs": result.get("analysisMs")})
`;

let py = null; // the Pyodide interpreter, set once initialised

/**
 * Load Pyodide, unpack the engine bundle, and load the Python helper.
 * @param {(msg: string) => void} [onStatus] progress callback
 */
export async function initEngine(onStatus = () => {}) {
  if (py) return;
  onStatus("Loading Pyodide…");
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

/**
 * Derive a single word (by IPA key or gloss), independent of the batched full run.
 * @returns {{found: boolean, ipa: string, gloss: string, derivations: Array,
 *   accuracy: object|null, errors: object|null, errorContext: object|null,
 *   blame: object|null}|{error: string[]}}
 */
export function runSingle(word) {
  const fn = py.globals.get("run_single");
  try {
    return JSON.parse(fn(word));
  } finally {
    fn.destroy();
  }
}

/**
 * Diagnostics: the inventory segments a feature bundle matches (the engine's own denotation),
 * read from the current overlay so it reflects unsaved feature-system edits.
 * @param {string} bundle a feature bundle, e.g. "+front, +sonorant, -syllabic"
 * @returns {{matched: string[], total: number}|{error: string}}
 */
export function queryClasses(bundle) {
  const fn = py.globals.get("query_classes");
  try {
    return JSON.parse(fn(bundle));
  } finally {
    fn.destroy();
  }
}

/**
 * Diagnostics: the feature geometry as a tree — the segmental hierarchy under ROOT plus the
 * suprasegmental tier features — read from the current overlay so it reflects unsaved edits.
 * @returns {{root: object, tiers: object[]}|{error: string}} nodes are
 *   {name, kind, values: string|null, children: node[]}
 */
export function featureTree() {
  const fn = py.globals.get("feature_tree");
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
 * Set up the post-derivation analysis so the caller can drive it step by step (and paint a
 * progress bar between steps). The results accumulate in the session and come back from the
 * final {@link analysisStep} call.
 * @returns {{steps: string[], result: object|null}} the step labels (empty when superseded),
 *   and a ready result only when there was nothing to run.
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
 * Run the next analysis step (call in a loop over {@link finalizeRun}'s steps).
 * @returns {{done: number, total: number, result: object|null}} the full analysis summary
 *   (accuracy, errors, errorContext, blame, warnings, unfiredRules, dependencies, analysisMs)
 *   on the final step, otherwise null.
 */
export function analysisStep() {
  const fn = py.globals.get("analysis_step");
  try {
    return JSON.parse(fn());
  } finally {
    fn.destroy();
  }
}

