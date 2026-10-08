// Node smoke test for the browser engine path. It runs the real src/lib/engine.js against the
// built public/ assets: the worker script (public/engine/worker.js), the WASM engine beside it,
// and the default project. Node has no Web Worker, so a small shim runs the worker module in
// this process and passes the messages, and fetch reads files under public/.
import { readFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { resolve } from "node:path";

const log = (...a) => console.log(...a);
const PUBLIC = pathToFileURL(resolve("public") + "/").href;

globalThis.document = { baseURI: PUBLIC };
globalThis.fetch = async (url) => {
  try {
    const body = readFileSync(fileURLToPath(String(url)));
    const type = String(url).endsWith(".wasm") ? "application/wasm" : "text/plain";
    return new Response(body, { headers: { "Content-Type": type } });
  } catch {
    return new Response(null, { status: 404 });
  }
};
// The worker script assigns self.onmessage and calls postMessage; replies go to the page side.
let page = null;
globalThis.self = globalThis;
globalThis.postMessage = (data) => setTimeout(() => page.onmessage({ data: structuredClone(data) }));
globalThis.Worker = class {
  constructor(url) {
    page = this;
    this.loaded = import(url);
  }
  postMessage(data) {
    this.loaded.then(() => setTimeout(() => self.onmessage({ data: structuredClone(data) })));
  }
};

const engine = await import("./src/lib/engine.js");

// The app's batched run, end to end: prepare, render every card, then each analysis step.
async function runAll() {
  const prep = await engine.prepareRun();
  if (prep.error) return prep;
  const derivations = [];
  for (let i = 0; i < prep.words; i += 64) derivations.push(...(await engine.deriveBatch(i, 64)));
  const plan = await engine.finalizeRun();
  let result = plan.result;
  while (!result) result = (await engine.analysisStep()).result;
  return { derivations, ...result };
}

try {
  await engine.initEngine();
  log("1. engine loaded: worker, WASM, and the default project");

  const data = await runAll();
  if (data.error) throw new Error("engine returned error: " + JSON.stringify(data.error));
  const first = data.derivations[0];
  log(`2. full run: ${data.derivations.length} word(s)`);
  log(`   ${first.ipa}  ->  ${first.surface}  (${first.steps.length} steps)`);

  // The reports land in the reports/ map, read back like the inventory files.
  const derivations = engine.readFile("reports/derivations.csv");
  const csv = engine.readFile("reports/derivation_matrix.csv");
  const ruleFirings = engine.readFile("reports/rule_firings.csv");
  if (!derivations.startsWith("word,rule,t,before,after,change"))
    throw new Error("derivations.csv missing its header row: " + derivations.slice(0, 80));
  if (!csv.startsWith("ipa,gloss,")) throw new Error("derivation_matrix.csv missing its header row: " + csv.slice(0, 80));
  if (!ruleFirings.startsWith("rule,t,sporadic,count,changes,matched"))
    throw new Error("rule_firings.csv missing its header row: " + ruleFirings.slice(0, 80));
  log(`3. reports written: derivations.csv (${derivations.split("\n").length} rows), derivation_matrix.csv (${csv.split("\n").length} rows), rule_firings.csv (${ruleFirings.split("\n").length} rows)`);

  // Overlay model: empty overlay ⇒ all-default; write ⇒ project; remove ⇒ back to default.
  const FILES = [
    "features.toml", "letters.csv", "diacritics.toml", "sonorities.toml",
    "syllable_parts.toml", "tiers.toml", "words.toml", "rules.toml",
  ];
  const statusOf = (names) => {
    const all = engine.fileStatus();
    return Object.fromEntries(names.map((n) => [n, all[n]]));
  };

  const before = statusOf(FILES);
  if (Object.values(before).some((v) => v !== "default"))
    throw new Error("expected an all-default status on a fresh overlay: " + JSON.stringify(before));
  log("4. fresh overlay: all files default");

  engine.writeFile("words.toml", engine.readFile("words.toml")); // no-op content change, still promotes it
  const afterWrite = statusOf(FILES);
  if (afterWrite["words.toml"] !== "project") throw new Error("writeFile did not promote words.toml to project");
  if (FILES.filter((f) => f !== "words.toml").some((f) => afterWrite[f] !== "default"))
    throw new Error("writeFile affected files other than words.toml: " + JSON.stringify(afterWrite));
  log("5. writeFile(words.toml): promoted to project, everything else still default");

  // Dual-format resolution: only the effective file of each pair shows. The default project
  // carries the .toml, so the .csv is "absent" (hidden). Writing the .csv makes it the active
  // file and forces the .toml absent — the two never both show a tab.
  for (const [base, sample] of [["words", "word,gloss,final\nka,c,ka\n"], ["rules", "id,time,definition\nr,0,a -> b\n"]]) {
    const st = statusOf([`${base}.toml`, `${base}.csv`]);
    if (st[`${base}.csv`] !== "absent")
      throw new Error(`expected ${base}.csv absent when the project uses ${base}.toml: ` + JSON.stringify(st));
    const kept = engine.readFile(`${base}.toml`);
    engine.removeFile(`${base}.toml`);
    engine.writeFile(`${base}.csv`, sample);
    const st2 = statusOf([`${base}.toml`, `${base}.csv`]);
    if (st2[`${base}.csv`] !== "project" || st2[`${base}.toml`] !== "absent")
      throw new Error(`expected ${base}.csv active, ${base}.toml absent: ` + JSON.stringify(st2));
    engine.removeFile(`${base}.csv`);
    engine.writeFile(`${base}.toml`, kept); // restore
  }
  for (const base of ["diacritics", "sonorities"]) {
    const st = statusOf([`${base}.toml`, `${base}.csv`]);
    if (st[`${base}.csv`] !== "absent")
      throw new Error(`expected ${base}.csv absent when the project uses ${base}.toml: ` + JSON.stringify(st));
  }
  log("6. dual-format resolution: .toml/.csv never both visible");

  const rerun = await runAll();
  if (rerun.error) throw new Error("the run failed with a project file present: " + JSON.stringify(rerun.error));
  log("7. a run still succeeds with project files present (per-file fallback for the rest)");

  engine.removeFile("words.toml");
  engine.removeFile("rules.toml");
  if (statusOf(FILES)["words.toml"] !== "default") throw new Error("removeFile did not revert words.toml to default");
  log("8. removeFile(words.toml): reverted to default");

  engine.writeFile("words.toml", "");
  engine.writeFile("rules.toml", "");
  engine.resetOverlay();
  if (Object.values(statusOf(FILES)).some((v) => v !== "default"))
    throw new Error("resetOverlay() left project files behind: " + JSON.stringify(statusOf(FILES)));
  log("9. resetOverlay(): all files back to default");

  // 10. The non-empty warnings path: onset = coda = [-syll] cannot split a 3-consonant
  //     cluster, so 'astra' falls back to sonority.
  engine.writeFile(
    "syllable_parts.toml",
    '[0]\nnucleus = { definition = "+syll" }\nonset = { definition = "[-syll]" }\ncoda = { definition = "[-syll]" }\n',
  );
  engine.writeFile("words.toml", '"astra" = "three"\n"apta" = "ok"\n');
  const warned = await runAll();
  if (warned.error) throw new Error("warnings run failed: " + JSON.stringify(warned.error));
  const astra = (warned.warnings || []).find((w) => w.syllabified === "as.tra");
  if (!astra || !astra.clusters.includes("str") || astra.form !== "astra" || astra.word !== "astra")
    throw new Error("expected a populated 'astra' warning, got: " + JSON.stringify(warned.warnings));
  if (!engine.readFile("reports/warnings.md").includes("as.tra"))
    throw new Error("warnings.md not written: " + engine.readFile("reports/warnings.md").slice(0, 80));
  log(`10. warnings path: ${warned.warnings.length} warning(s), warnings.md written`);
  engine.resetOverlay();

  // 11. Errors + error context + blame populated: a word with a deliberately-wrong `final`.
  const wrongWords = '[[words]]\nid = "apa"\ngloss = "wrong"\nforms = [{ time = 0, ipa = "apa" }, { time = "final", ipa = "xxx" }]\n\n[[words]]\nid = "ata"\ngloss = "ok"\nforms = [{ time = 0, ipa = "ata" }, { time = "final", ipa = "ata" }]\n';
  engine.writeFile("words.toml", wrongWords);
  const diag = await runAll();
  if (diag.error) throw new Error("errors run failed: " + JSON.stringify(diag.error));
  if (!diag.errors?.stages?.some((s) => s.label === "final" && s.confusions.length))
    throw new Error("expected the final stage's confusions, got: " + JSON.stringify(diag.errors));
  if (typeof diag.analysisMs !== "number") throw new Error("run missing analysis timing");
  const blamed = diag.blame?.words?.[0];
  if (!blamed?.residuals.length || !blamed.trajectory.length)
    throw new Error("blame word missing residuals/trajectory: " + JSON.stringify(diag.blame));
  const point = blamed.trajectory[0];
  if (!("target" in point) || !("fd" in point) || !("distance" in point))
    throw new Error("trajectory point missing target/d/fd: " + JSON.stringify(point));
  const headers = {
    "errors.csv": "stage,expected,got,count,kind,examples",
    "error_context.csv": "stage,segment,environment,assoc. (φ),F₁,err/ok · with,err/ok · without",
    "blame.csv": "gloss,step,regression,t,form,target,d,fd",
    "accuracy.csv": "stage,assessed,exact,within 1,mean phone dist,mean feature dist",
    "distance_to_target.csv": "stage,gloss,derived,target,d,fd",
  };
  for (const [name, header] of Object.entries(headers)) {
    const text = engine.readFile("reports/" + name);
    if (!text.startsWith(header)) throw new Error(`${name} missing its header: ` + text.slice(0, 90));
  }
  log(`11. errors + error context + blame (${diag.blame.words.length} word(s)) + accuracy CSVs`);

  // 12. Single-word mode: found by id with a wrong `final`, found by gloss, and absent (card
  //     only, and the stale target report is cleared).
  const single = await engine.runSingle("apa");
  if (single.error) throw new Error("runSingle failed: " + JSON.stringify(single.error));
  if (!single.found || single.ipa !== "apa") throw new Error("runSingle did not find 'apa': " + JSON.stringify(single));
  if (single.derivations.length !== 1) throw new Error("runSingle should return exactly one derivation card");
  if (!single.accuracy || !single.errors || !single.blame)
    throw new Error("runSingle(found, wrong target) should populate accuracy/errors/blame");
  const byGloss = await engine.runSingle("ok");
  if (!byGloss.found || byGloss.ipa !== "ata") throw new Error("runSingle by gloss 'ok' should resolve to 'ata'");
  if (!engine.readFile("reports/single_derivations.csv").startsWith("word,rule,t,before,after,change"))
    throw new Error("single_derivations.csv missing its header");
  if (!engine.readFile("reports/single_accuracy.csv").startsWith("stage,assessed,exact"))
    throw new Error("single_accuracy.csv missing its header");
  const missing = await engine.runSingle("zzz");
  if (missing.found || missing.derivations.length !== 1 || missing.accuracy !== null)
    throw new Error("runSingle(absent) should give one card and null accuracy: " + JSON.stringify(missing).slice(0, 200));
  if (engine.readFile("reports/single_accuracy.csv") !== "")
    throw new Error("single_accuracy.csv should be cleared after a no-target single run");
  log("12. single-word mode: found (accuracy+errors+blame), by gloss, and absent (card only, stale report cleared)");
  engine.resetOverlay();

  // 13. Diagnostics: a class query, a rejected alpha variable, and the feature tree.
  const classes = await engine.queryClasses("+syllabic");
  if (!classes.matched?.includes("a") || !(classes.total > 0)) throw new Error("class query: " + JSON.stringify(classes));
  const rejected = await engine.queryClasses("αfront");
  if (!rejected.error) throw new Error("an alpha variable should be rejected outside a rule");
  const tree = await engine.featureTree();
  if (tree.root?.name !== "root" || !tree.root.children.length) throw new Error("feature tree: " + JSON.stringify(tree).slice(0, 200));
  log(`13. diagnostics: [+syllabic] matches ${classes.matched.length} of ${classes.total}, α rejected, tree of ${tree.root.children.length} top nodes`);

  log("SMOKE TEST PASSED");
  process.exit(0);
} catch (e) {
  const m = e && e.message ? e.message : String(e);
  console.log("FAILED:\n" + m.split("\n").slice(-25).join("\n"));
  process.exit(1);
}
