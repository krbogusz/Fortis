//! The Fortis engine for the web app, driven from a Web Worker through wasm-bindgen. It runs in
//! one thread: the crate's rayon calls fall back to the calling thread on this target.
//!
//! Project files live in memory under two roots: `default/` holds the shipped project and
//! `project/` holds the user's files, so each file falls back to the default as in the CLI.
//! Every call returns JSON text in the shapes the Svelte app renders. A call that writes
//! reports returns them under `reports`, as name → text, or null for a report to delete.

use std::path::{Path, PathBuf};

use fortis::analysis::accuracy::{StageAccuracy, accuracy_by_stage, ingest_targets};
use fortis::analysis::blame::{Blame, blame_all, render_blame_csv};
use fortis::analysis::dependencies::{base_id, build_dependency_graph, dependency_layout, render_dependency_html};
use fortis::analysis::diagnosis::{StageDiagnosis, diagnose_stages, render_error_context_csv, render_errors_csv};
use fortis::analysis::diagnostics::{match_set, unsatisfiable_rules};
use fortis::analysis::reporting::{render_accuracy_csv, render_distance_to_target_csv};
use fortis::analysis::warnings::{render_warnings, syllabification_warnings};
use fortis::diagram::render_change;
use fortis::engine::deriving::Engine;
use fortis::engine::rendering::Renderer;
use fortis::engine::segmentation::string_to_sequence;
use fortis::engine::tiers::lower_tiers;
use fortis::loaders::files::Memory;
use fortis::loaders::{load_project_from, unfired_scoped_rules};
use fortis::models::*;
use fortis::py::{self, Json};
use fortis::reports;
use wasm_bindgen::prelude::*;

const STEPS: [&str; 8] = ["derivations", "matrix", "rule firings", "feeding graph", "accuracy", "errors", "blame", "warnings"];

fn obj(fields: Vec<(&str, Json)>) -> Json {
    Json::Obj(fields.into_iter().map(|(k, v)| (k.to_string(), v)).collect())
}

fn s(text: impl Into<String>) -> Json {
    Json::Str(text.into())
}

fn opt_s(text: Option<&str>) -> Json {
    text.map_or(Json::Null, s)
}

fn opt_i(n: Option<i64>) -> Json {
    n.map_or(Json::Null, Json::Int)
}

/// `round(x, digits)` as Python gives it.
fn round(x: f64, digits: usize) -> Json {
    Json::Float(py::fixed(x, digits).parse().unwrap())
}

fn strs(items: &[String]) -> Json {
    Json::List(items.iter().map(|x| s(x.as_str())).collect())
}

fn error_list(messages: Vec<String>) -> String {
    obj(vec![("error", strs(&messages))]).dumps()
}

fn has_target(word: &Word) -> bool {
    word.final_ipa().is_some() || !word.stages().is_empty()
}

/// Reports written by one call: name → text, or `None` to delete a stale one.
#[derive(Default)]
struct Reports(Vec<(String, Json)>);

impl Reports {
    fn write(&mut self, name: &str, text: Option<String>) {
        self.0.push((name.to_string(), text.map_or(Json::Null, Json::Str)));
    }
}

// ---- JSON shapes ------------------------------------------------------------------------------

/// One word's derivation trace: the Derivations-tab card.
fn card(d: &Derivation, project: &Project, r: &Renderer) -> Json {
    let render = |form: &Form, boundaries: &Boundaries| r.syllabified(&lower_tiers(form), boundaries, true);
    let mut steps = Vec::new();
    let mut previous: Option<&str> = None;
    let mut previous_time: Option<Option<i64>> = None;
    for step in &d.steps {
        let rule = &step.rule;
        let base = base_id(&rule.id);
        let name = rule.name.clone().unwrap_or_else(|| base.to_string());
        let heading = if previous == Some(base) { Json::Null } else { s(name.clone()) };
        let time_header = match rule.time {
            Some(t) if previous_time != Some(Some(t)) => Json::Int(t),
            _ => Json::Null,
        };
        previous = Some(base);
        previous_time = Some(rule.time);
        let autosegmental = render_change(&step.before, &step.after, rule, project, r)
            .into_iter()
            .map(|(label, diagram)| Json::List(vec![s(label), s(diagram)]))
            .collect();
        steps.push(obj(vec![
            ("timeHeader", time_header),
            ("heading", heading),
            ("definition", s(rule.raw_definition.as_str())),
            ("time", opt_i(rule.time)),
            ("name", s(name)),
            ("sporadic", Json::Bool(!rule.words.is_empty())),
            ("before", s(render(&step.before, &step.before_boundaries))),
            ("after", s(render(&step.after, &step.after_boundaries))),
            ("change", s(r.describe_change(&lower_tiers(&step.before), &lower_tiers(&step.after)))),
            ("autosegmental", Json::List(autosegmental)),
        ]));
    }
    let surface = render(&d.surface, &d.surface_boundaries);
    // The Input pseudo-step: the raw lexicon IPA and the form the first rule sees.
    let input = d.steps.first().map_or_else(|| surface.clone(), |step| render(&step.before, &step.before_boundaries));
    steps.insert(
        0,
        obj(vec![
            ("timeHeader", Json::Null),
            ("heading", s("Input")),
            ("definition", Json::Null),
            ("time", Json::Null),
            ("name", s("Input")),
            ("before", s(d.word.ipa())),
            ("after", s(input)),
            ("change", s("")),
        ]),
    );
    obj(vec![
        ("ipa", s(d.word.ipa())),
        ("gloss", s(d.word.gloss.as_str())),
        ("surface", s(surface)),
        ("steps", Json::List(steps)),
    ])
}

fn accuracy_json(stages: &[StageAccuracy]) -> Json {
    let weighted = stages
        .iter()
        .find(|st| st.time.is_none())
        .filter(|st| st.report.frequencies_vary())
        .map(|st| obj(vec![("weight", Json::Int(st.report.weight()))]));
    let wt = |x: f64, digits: usize| if weighted.is_some() { round(x, digits) } else { Json::Null };
    let stage_json = |st: &StageAccuracy| {
        let report = &st.report;
        let mut misses: Vec<_> = report.distances.iter().filter(|g| !g.exact()).collect();
        let name = |g: &&fortis::analysis::accuracy::DistanceToTarget| if g.gloss.is_empty() { g.ipa.clone() } else { g.gloss.clone() };
        misses.sort_by_cached_key(|g| name(g).to_lowercase());
        let misses = misses
            .iter()
            .map(|g| {
                obj(vec![
                    ("gloss", s(name(g))),
                    ("derived", s(g.derived.as_str())),
                    ("target", s(g.target.as_str())),
                    ("d", Json::Int(g.distance)),
                    ("fd", opt_i(g.feature_distance)),
                    ("matchesAt", s(g.matches_at.as_str())),
                    ("closestAt", s(g.closest_at.as_str())),
                ])
            })
            .collect();
        obj(vec![
            ("label", s(st.label.as_str())),
            ("assessed", Json::Int(report.assessed() as i64)),
            ("exact", Json::Int(report.exact() as i64)),
            ("withinOne", Json::Int(report.within_one() as i64)),
            ("meanPhone", round(report.mean_distance(), 3)),
            ("meanFeature", round(report.mean_feature_distance(), 3)),
            ("wtExact", wt(report.weighted_accuracy(), 4)),
            ("wtPhone", wt(report.weighted_mean_distance(), 3)),
            ("wtFeature", wt(report.weighted_mean_feature_distance(), 3)),
            ("misses", Json::List(misses)),
        ])
    };
    let stage_list = stages.iter().map(stage_json).collect();
    obj(vec![
        ("hasStages", Json::Bool(stages.iter().any(|st| st.time.is_some()))),
        ("weighted", weighted.unwrap_or(Json::Null)),
        ("stages", Json::List(stage_list)),
    ])
}

/// Which segments came out wrong at each stage; `null` when every assessed word is exact.
fn errors_json(diagnosis: &[StageDiagnosis]) -> Json {
    if diagnosis.iter().all(|st| st.confusions.is_empty()) {
        return Json::Null;
    }
    let stages = diagnosis
        .iter()
        .filter(|st| !st.confusions.is_empty())
        .map(|st| {
            let confusions = st
                .confusions
                .iter()
                .map(|c| {
                    obj(vec![
                        ("expected", opt_s(c.expected.as_deref())),
                        ("got", opt_s(c.got.as_deref())),
                        ("count", Json::Int(c.count as i64)),
                        ("kind", s(c.kind())),
                        ("examples", strs(&c.examples)),
                    ])
                })
                .collect();
            obj(vec![("label", s(st.label.as_str())), ("time", opt_i(st.time)), ("confusions", Json::List(confusions))])
        })
        .collect();
    obj(vec![("stages", Json::List(stages))])
}

/// The environments positively associated with each wrong segment; `null` when there are none.
fn error_context_json(diagnosis: &[StageDiagnosis], top: usize) -> Json {
    let mut staged = Vec::new();
    for st in diagnosis {
        let segments: Vec<Json> = st
            .autopsy
            .iter()
            .filter_map(|a| {
                let predictors: Vec<Json> = a
                    .associations
                    .iter()
                    .filter(|x| x.phi > 0.0)
                    .take(top)
                    .map(|x| {
                        obj(vec![
                            ("predictor", s(x.predictor.as_str())),
                            ("phi", round(x.phi, 2)),
                            ("fscore", round(x.fscore, 2)),
                            ("errHere", Json::Int(x.err_here)),
                            ("okHere", Json::Int(x.ok_here)),
                            ("errAway", Json::Int(x.err_away)),
                            ("okAway", Json::Int(x.ok_away)),
                        ])
                    })
                    .collect();
                (!predictors.is_empty()).then(|| {
                    obj(vec![
                        ("segment", s(a.phone.as_str())),
                        ("errors", Json::Int(a.errors)),
                        ("total", Json::Int(a.total)),
                        ("supportFloor", Json::Int(a.support_floor)),
                        ("predictors", Json::List(predictors)),
                    ])
                })
            })
            .collect();
        if !segments.is_empty() {
            staged.push(obj(vec![("label", s(st.label.as_str())), ("time", opt_i(st.time)), ("segments", Json::List(segments))]));
        }
    }
    if staged.is_empty() { Json::Null } else { obj(vec![("stages", Json::List(staged))]) }
}

/// Every assessed word's residuals, stage divergence and trajectory; `null` with no targets.
fn blame_json(blames: &[Blame]) -> Json {
    if blames.is_empty() {
        return Json::Null;
    }
    let words = blames
        .iter()
        .map(|b| {
            let residuals = b
                .residuals
                .iter()
                .map(|x| {
                    obj(vec![
                        ("expected", opt_s(x.expected.as_deref())),
                        ("got", opt_s(x.got.as_deref())),
                        ("culprit", opt_s(x.culprit.as_ref().map(|(rule, _)| rule.as_str()))),
                        ("time", opt_i(x.culprit.as_ref().and_then(|(_, time)| *time))),
                        ("attributed", Json::Bool(true)),
                        ("kind", s(x.kind())),
                    ])
                })
                .collect();
            let stage = b.stage_divergence.as_ref().map_or(Json::Null, |sd| {
                obj(vec![("time", Json::Int(sd.time)), ("attested", s(sd.attested.as_str())), ("derived", s(sd.derived.as_str()))])
            });
            let trajectory = b
                .trajectory
                .iter()
                .map(|p| {
                    obj(vec![
                        ("label", s(p.label.as_str())),
                        ("time", opt_i(p.time)),
                        ("form", s(p.form.as_str())),
                        ("target", s(p.target.as_str())),
                        ("distance", Json::Int(p.distance)),
                        ("fd", Json::Int(p.feature_distance)),
                        ("regressed", Json::Bool(p.regressed)),
                    ])
                })
                .collect();
            obj(vec![
                ("word", s(if b.gloss.is_empty() { b.ipa.as_str() } else { b.gloss.as_str() })),
                ("surface", s(b.surface.as_str())),
                ("target", s(b.target.as_str())),
                ("distance", Json::Int(b.distance)),
                ("residuals", Json::List(residuals)),
                ("stage", stage),
                ("trajectory", Json::List(trajectory)),
            ])
        })
        .collect();
    obj(vec![("words", Json::List(words))])
}

fn feature_node(id: FeatId, features: &FeatureInventory) -> Json {
    let feature = features.get(id);
    let values = if feature.kind == FeatureKind::Scalar {
        let mut levels = feature.values.clone();
        levels.sort();
        s(levels.iter().map(|(code, label)| format!("{code} {label}")).collect::<Vec<_>>().join(", "))
    } else {
        Json::Null
    };
    let children =
        feature.children.iter().flatten().filter_map(|name| features.id(name)).map(|c| feature_node(c, features)).collect();
    obj(vec![
        ("name", s(feature.name.as_str())),
        ("kind", s(feature.kind.name())),
        ("values", values),
        ("children", Json::List(children)),
    ])
}

// ---- The session ------------------------------------------------------------------------------

/// A full run in progress: derived at once, then rendered in batches and analysed in steps, so
/// the page can show progress between calls.
struct Run {
    project: Project,
    rules: RuleInventory,
    derivations: Vec<Derivation>,
    step: usize,
    stages: Option<Vec<StageAccuracy>>,
    out: Vec<(String, Json)>,
}

fn empty_analysis() -> Vec<(String, Json)> {
    ["accuracy", "errors", "errorContext", "blame", "warnings", "unfiredRules", "unsatisfiable", "dependencies"]
        .into_iter()
        .map(|key| {
            let empty = if matches!(key, "warnings" | "unfiredRules" | "unsatisfiable") { Json::List(Vec::new()) } else { Json::Null };
            (key.to_string(), empty)
        })
        .collect()
}

fn set(out: &mut [(String, Json)], key: &str, value: Json) {
    out.iter_mut().find(|(k, _)| k == key).unwrap().1 = value;
}

#[wasm_bindgen]
#[derive(Default)]
pub struct Fortis {
    files: Memory,
    run: Option<Run>,
}

#[wasm_bindgen]
impl Fortis {
    #[wasm_bindgen(constructor)]
    pub fn new() -> Fortis {
        Fortis::default()
    }

    /// Store one file: `default/<name>` for the shipped project, `project/<name>` for the user's.
    pub fn put(&mut self, path: &str, text: String) {
        self.files.0.insert(PathBuf::from(path), text);
    }

    /// Drop every user file, so each one falls back to the default.
    pub fn clear_project(&mut self) {
        self.files.0.retain(|path, _| !path.starts_with("project"));
    }

    fn load(&self) -> Result<Project, Vec<String>> {
        load_project_from(&self.files, Path::new("default"), Some(Path::new("project")), None, None)
    }

    /// Load the project and derive every word. Returns `{words, rules}` or `{error}`.
    pub fn prepare_run(&mut self) -> String {
        self.run = None;
        let project = match self.load() {
            Ok(p) => p,
            Err(e) => return error_list(e),
        };
        let (rules, derivations) = {
            let engine = match Engine::new(&project) {
                Ok(e) => e,
                Err(e) => return error_list(vec![e]),
            };
            match engine.derive_all() {
                Ok(d) => (engine.rules.clone(), d),
                Err(e) => return error_list(vec![e]),
            }
        };
        let rule_count: usize = project.rules.by_time.values().map(Vec::len).sum();
        let words = derivations.len();
        self.run = Some(Run { project, rules, derivations, step: 0, stages: None, out: empty_analysis() });
        obj(vec![("words", Json::Int(words as i64)), ("rules", Json::Int(rule_count as i64))]).dumps()
    }

    /// The cards for words `[start, start + count)` of the current run.
    pub fn derive_batch(&self, start: usize, count: usize) -> String {
        let Some(run) = &self.run else { return "[]".into() };
        let end = (start + count).min(run.derivations.len());
        let r = Renderer::new(&run.project);
        let cards: Vec<Json> = run.derivations[start.min(end)..end].iter().map(|d| card(d, &run.project, &r)).collect();
        Json::List(cards).dumps()
    }

    /// Start the analysis. Returns the step labels; the results come from the last step.
    pub fn finalize_run(&mut self) -> String {
        let Some(run) = &mut self.run else {
            return obj(vec![("steps", Json::List(Vec::new())), ("result", Json::Obj(empty_analysis()))]).dumps();
        };
        run.step = 0;
        run.out = empty_analysis();
        let steps = STEPS.iter().map(|x| s(*x)).collect();
        obj(vec![("steps", Json::List(steps)), ("result", Json::Null)]).dumps()
    }

    /// Run the next analysis step. Returns `{done, total, result, reports}`, with the whole
    /// analysis as `result` on the last step.
    pub fn analysis_step(&mut self) -> String {
        let Some(run) = &mut self.run else {
            let result = Json::Obj(empty_analysis());
            return obj(vec![("done", Json::Int(0)), ("total", Json::Int(0)), ("result", result), ("reports", obj(vec![]))]).dumps();
        };
        let mut written = Reports::default();
        let Run { project, rules, derivations, step, stages, out } = run;
        let project: &Project = project;
        let r = Renderer::new(project);
        match *step {
            0 => written.write("derivations.csv", Some(reports::derivations_csv(derivations, &r))),
            1 => written.write("derivation_matrix.csv", Some(reports::matrix_csv(derivations, rules, &r))),
            2 => written.write("rule_firings.csv", Some(reports::rule_firings_csv(derivations, rules, &r))),
            3 => {
                let graph = build_dependency_graph(derivations, rules, &r);
                written.write("rule_dependencies.html", Some(render_dependency_html(&graph)));
                set(out, "dependencies", dependency_layout(&graph));
            }
            4 => {
                ingest_targets(derivations, project);
                *stages = derivations.iter().any(|d| has_target(&d.word)).then(|| accuracy_by_stage(derivations, project, &r));
                set(out, "accuracy", stages.as_deref().map_or(Json::Null, accuracy_json));
                written.write("accuracy.csv", stages.as_deref().map(render_accuracy_csv));
                written.write("distance_to_target.csv", stages.as_deref().map(render_distance_to_target_csv));
            }
            5 => {
                let diagnosis = stages.as_deref().map(|st| diagnose_stages(st, project));
                written.write("errors.csv", diagnosis.as_deref().map(render_errors_csv));
                written.write("error_context.csv", diagnosis.as_deref().map(render_error_context_csv));
                let top = project.settings.diagnosis.report_top.max(0) as usize;
                set(out, "errors", diagnosis.as_deref().map_or(Json::Null, errors_json));
                set(out, "errorContext", diagnosis.as_deref().map_or(Json::Null, |d| error_context_json(d, top)));
            }
            6 => {
                let blames = blame_all(derivations, project, &r);
                written.write("blame.csv", (!blames.is_empty()).then(|| render_blame_csv(&blames)));
                set(out, "blame", blame_json(&blames));
            }
            _ => {
                let warnings = syllabification_warnings(derivations, project, &r);
                let text = (!warnings.is_empty()).then(|| render_warnings(&warnings, "the current project", &[]));
                written.write("warnings.md", text);
                let list = warnings
                    .iter()
                    .map(|w| {
                        obj(vec![
                            ("word", s(w.ipa.as_str())),
                            ("gloss", s(w.gloss.as_str())),
                            ("form", s(w.form.as_str())),
                            ("clusters", strs(&w.clusters)),
                            ("syllabified", s(w.syllabified.as_str())),
                        ])
                    })
                    .collect();
                set(out, "warnings", Json::List(list));
                let unfired = unfired_scoped_rules(rules, &project.words)
                    .into_iter()
                    .map(|(rule, word)| obj(vec![("rule", s(rule)), ("word", s(word))]))
                    .collect();
                set(out, "unfiredRules", Json::List(unfired));
                let unsatisfiable = unsatisfiable_rules(project)
                    .into_iter()
                    .map(|u| obj(vec![("rule", s(u.rule)), ("role", s(u.role)), ("label", s(u.label)), ("reason", s(u.reason))]))
                    .collect();
                set(out, "unsatisfiable", Json::List(unsatisfiable));
            }
        }
        *step += 1;
        let done = *step;
        let result = if done >= STEPS.len() { Json::Obj(std::mem::take(out)) } else { Json::Null };
        if done >= STEPS.len() {
            self.run = None;
        }
        obj(vec![
            ("done", Json::Int(done as i64)),
            ("total", Json::Int(STEPS.len() as i64)),
            ("result", result),
            ("reports", Json::Obj(written.0)),
        ])
        .dumps()
    }

    /// Derive one word, found by id, gloss or seed IPA, else derived bare without a target.
    pub fn run_single(&self, word: &str) -> String {
        let project = match self.load() {
            Ok(p) => p,
            Err(e) => return error_list(e),
        };
        let engine = match Engine::new(&project) {
            Ok(e) => e,
            Err(e) => return error_list(vec![e]),
        };
        let word_str = py::strip(word);
        if word_str.is_empty() {
            return error_list(vec!["Enter a word to derive.".into()]);
        }
        let found = project.words.values().find(|w| [w.id.as_str(), w.gloss.as_str(), w.ipa()].contains(&word_str));
        let word = match found {
            Some(w) => w.clone(),
            None => Word {
                id: word_str.to_string(),
                forms: vec![(Some(0), Attestation { ipa: word_str.to_string(), ..Default::default() })],
                frequency: 1,
                ..Default::default()
            },
        };
        let form = match string_to_sequence(word.ipa(), &project) {
            Ok(f) => f,
            Err(e) => return error_list(vec![e]),
        };
        let mut derivations = vec![engine.derive(&word, form)];
        let r = Renderer::new(&project);
        let card = card(&derivations[0], &project, &r);
        let mut written = Reports::default();
        written.write("single_derivations.csv", Some(reports::derivations_csv(&derivations, &r)));
        ingest_targets(&mut derivations, &project);
        let stages = has_target(&word).then(|| accuracy_by_stage(&derivations, &project, &r));
        written.write("single_accuracy.csv", stages.as_deref().map(render_accuracy_csv));
        written.write("single_distance_to_target.csv", stages.as_deref().map(render_distance_to_target_csv));
        let diagnosis = stages.as_deref().map(|st| diagnose_stages(st, &project));
        written.write("single_errors.csv", diagnosis.as_deref().map(render_errors_csv));
        written.write("single_error_context.csv", diagnosis.as_deref().map(render_error_context_csv));
        let top = project.settings.diagnosis.report_top.max(0) as usize;
        let blames = blame_all(&derivations, &project, &r);
        written.write("single_blame.csv", (!blames.is_empty()).then(|| render_blame_csv(&blames)));
        obj(vec![
            ("found", Json::Bool(found.is_some())),
            ("ipa", s(word.ipa())),
            ("gloss", s(word.gloss.as_str())),
            ("derivations", Json::List(vec![card])),
            ("accuracy", stages.as_deref().map_or(Json::Null, accuracy_json)),
            ("errors", diagnosis.as_deref().map_or(Json::Null, errors_json)),
            ("errorContext", diagnosis.as_deref().map_or(Json::Null, |d| error_context_json(d, top))),
            ("blame", blame_json(&blames)),
            ("reports", Json::Obj(written.0)),
        ])
        .dumps()
    }

    /// The letters a feature bundle matches: `{matched, total}` or `{error}`.
    pub fn query_classes(&self, bundle: &str) -> String {
        let project = match self.load() {
            Ok(p) => p,
            Err(e) => return obj(vec![("error", s(e.join("\n")))]).dumps(),
        };
        match match_set(bundle, &project) {
            Ok((matched, total)) => obj(vec![("matched", strs(&matched)), ("total", Json::Int(total as i64))]).dumps(),
            Err(e) => obj(vec![("error", s(e))]).dumps(),
        }
    }

    /// The feature geometry: `{root, tiers}`, each node `{name, kind, values, children}`.
    pub fn feature_tree(&self) -> String {
        let project = match self.load() {
            Ok(p) => p,
            Err(e) => return obj(vec![("error", s(e.join("\n")))]).dumps(),
        };
        let features = &project.features;
        let root = features.id("root").map_or(Json::Null, |id| feature_node(id, features));
        let tiers = features
            .iter()
            .filter(|(id, f)| !features.is_segmental(*id) && f.parent.is_none())
            .map(|(id, _)| feature_node(id, features))
            .collect();
        obj(vec![("root", root), ("tiers", Json::List(tiers))]).dumps()
    }
}
