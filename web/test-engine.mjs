// Node smoke test for the *browser* engine-load path.
// It loads Pyodide from the copied public/pyodide/ assets (the exact files the
// browser serves), unpacks public/engine.tgz, imports src.fortis, loads the
// same helper as src/lib/engine.js, and runs a real derivation.
import { readFileSync } from "fs";
import { pathToFileURL } from "url";
import { resolve } from "path";

const log = (...a) => console.log(...a);

try {
  // Load Pyodide from the served assets, not the bare npm entry point.
  const pyUrl = pathToFileURL(resolve("public/pyodide/pyodide.mjs")).href;
  const { loadPyodide } = await import(pyUrl);
  const py = await loadPyodide({ indexURL: resolve("public/pyodide") + "/" });
  log("1. pyodide loaded from public/pyodide/");

  const tgz = readFileSync("public/engine.tgz");
  py.unpackArchive(new Uint8Array(tgz), "gztar", { extractDir: "/work" });
  log("2. unpacked:", py.runPython(`import os; sorted(os.listdir("/work"))`).toString());

  py.runPython(`import sys; sys.path.insert(0, "/work")`);
  py.runPython(`import src.fortis`);
  log("3. imported src.fortis");

  // Load the production helper, then call run_derivations() like the app does.
  const HELPER = readFileSync("src/lib/engine.js", "utf8")
    .split("const HELPER = `")[1]
    .split("`;")[0]
    .replace(/\\\\/g, "\\"); // un-escape the JS template-string backslashes
  py.runPython(HELPER);
  const json = py.runPython("run_derivations()");
  const data = JSON.parse(json);
  if (data.error) throw new Error("engine returned error: " + JSON.stringify(data.error));
  const first = data.derivations[0];
  log(`4. run_derivations(): ${data.derivations.length} word(s)`);
  log(`   ${first.ipa}  ->  ${first.surface}  (${first.steps.length} steps)`);

  // The reports are written into the virtual FS alongside the inventory files.
  const derivations = py.runPython(`read_file("reports/derivations.csv")`).toString();
  const csv = py.runPython(`read_file("reports/derivation_matrix.csv")`).toString();
  const ruleFirings = py.runPython(`read_file("reports/rule_firings.csv")`).toString();
  if (!derivations.startsWith("word,rule,t,before,after,change"))
    throw new Error("derivations.csv missing its header row: " + derivations.slice(0, 80));
  if (!csv.startsWith("ipa,gloss,")) throw new Error("derivation_matrix.csv missing its header row: " + csv.slice(0, 80));
  if (!ruleFirings.startsWith("rule,t,count,matched,changes"))
    throw new Error("rule_firings.csv missing its header row: " + ruleFirings.slice(0, 80));
  log(`5. reports written: derivations.csv (${derivations.split("\n").length} rows), derivation_matrix.csv (${csv.split("\n").length} rows), rule_firings.csv (${ruleFirings.split("\n").length} rows)`);

  // Overlay model: empty overlay ⇒ all-default; write ⇒ project; remove ⇒ back to default.
  const FILES = [
    "features.toml", "letters.csv", "diacritics.toml", "sonorities.toml",
    "syllable_parts.toml", "tiers.toml", "words.toml", "rules.toml",
  ];
  const statusPy = (names) => JSON.parse(py.runPython(`file_status(${JSON.stringify(names)})`).toString());

  const before = statusPy(FILES);
  if (Object.values(before).some((v) => v !== "default"))
    throw new Error("expected an all-default status on a fresh overlay: " + JSON.stringify(before));
  log("6. fresh overlay: all files default");

  py.runPython(`write_file("words.toml", read_file("words.toml"))`); // no-op content change, still promotes it
  const afterWrite = statusPy(FILES);
  if (afterWrite["words.toml"] !== "project") throw new Error("write_file did not promote words.toml to project");
  if (FILES.filter((f) => f !== "words.toml").some((f) => afterWrite[f] !== "default"))
    throw new Error("write_file affected files other than words.toml: " + JSON.stringify(afterWrite));
  log("7. write_file(words.toml): promoted to project, everything else still default");

  // Lexicon format resolution: only the effective words file shows. The default project
  // carries words.toml, so words.csv is "absent" (hidden). Writing words.csv makes it the
  // active lexicon and forces words.toml absent — the two never both show a tab.
  const lex = statusPy(["words.toml", "words.csv"]);
  if (lex["words.csv"] !== "absent")
    throw new Error("expected words.csv absent when the project uses words.toml: " + JSON.stringify(lex));
  py.runPython(`remove_file("words.toml"); write_file("words.csv", "word,gloss,final\\nka,c,ka\\n")`);
  const lex2 = statusPy(["words.toml", "words.csv"]);
  if (lex2["words.csv"] !== "project" || lex2["words.toml"] !== "absent")
    throw new Error("expected words.csv active, words.toml absent: " + JSON.stringify(lex2));
  py.runPython(`remove_file("words.csv"); write_file("words.toml", read_file("words.toml"))`); // restore
  log("8b. lexicon resolution: words.toml/words.csv never both visible");

  // Same dual-format resolution for rules: the default project ships rules.toml, so rules.csv
  // is "absent" (hidden). Writing rules.csv makes it active and forces rules.toml absent.
  const rul = statusPy(["rules.toml", "rules.csv"]);
  if (rul["rules.csv"] !== "absent")
    throw new Error("expected rules.csv absent when the project uses rules.toml: " + JSON.stringify(rul));
  py.runPython(`remove_file("rules.toml"); write_file("rules.csv", "id,time,definition\\nr,0,a -> b\\n")`);
  const rul2 = statusPy(["rules.toml", "rules.csv"]);
  if (rul2["rules.csv"] !== "project" || rul2["rules.toml"] !== "absent")
    throw new Error("expected rules.csv active, rules.toml absent: " + JSON.stringify(rul2));
  py.runPython(`remove_file("rules.csv"); write_file("rules.toml", read_file("rules.toml"))`); // restore
  log("8c. rules resolution: rules.toml/rules.csv never both visible");

  // Diacritics and sonorities are dual-format too: their .csv is hidden while the project
  // uses the shipped .toml, and never both show a tab.
  for (const base of ["diacritics", "sonorities"]) {
    const st = statusPy([`${base}.toml`, `${base}.csv`]);
    if (st[`${base}.csv`] !== "absent")
      throw new Error(`expected ${base}.csv absent when the project uses ${base}.toml: ` + JSON.stringify(st));
  }
  log("8d. diacritics/sonorities resolution: .toml/.csv never both visible");

  const rerun = JSON.parse(py.runPython("run_derivations()").toString());
  if (rerun.error) throw new Error("run_derivations() failed with a project file present: " + JSON.stringify(rerun.error));
  log("8. run_derivations() still succeeds with one project file (per-file fallback for the rest)");

  py.runPython(`remove_file("words.toml")`);
  const afterRemove = statusPy(FILES);
  if (afterRemove["words.toml"] !== "default") throw new Error("remove_file did not revert words.toml to default");
  log("9. remove_file(words.toml): reverted to default");

  py.runPython(`write_file("words.toml", "")`);
  py.runPython(`write_file("rules.toml", "")`);
  py.runPython(`reset_overlay()`);
  const afterReset = statusPy(FILES);
  if (Object.values(afterReset).some((v) => v !== "default"))
    throw new Error("reset_overlay() left project files behind: " + JSON.stringify(afterReset));
  log("10. reset_overlay(): all files back to default");

  // 11. The non-empty warnings path: onset = coda = [-syll] cannot split a 3-consonant
  //     cluster, so 'astra' falls back to sonority. Exercises finalize_run's populated
  //     branch (render_warnings + the structured list) through the real Pyodide round-trip.
  py.globals.set(
    "_sp",
    '[0]\nnucleus = { definition = "+syll" }\nonset = { definition = "[-syll]" }\ncoda = { definition = "[-syll]" }\n',
  );
  py.globals.set("_wd", '"astra" = "three"\n"apta" = "ok"\n');
  py.runPython(`write_file("syllable_parts.toml", _sp); write_file("words.toml", _wd)`);
  const warned = JSON.parse(py.runPython("run_derivations()").toString());
  if (warned.error) throw new Error("warnings run failed: " + JSON.stringify(warned.error));
  const ws = warned.warnings || [];
  const astra = ws.find((w) => w.syllabified === "as.tra");
  if (!astra || !astra.clusters.includes("str") || astra.form !== "astra" || astra.word !== "astra")
    throw new Error("expected a populated 'astra' warning, got: " + JSON.stringify(ws));
  const warnMd = py.runPython(`read_file("reports/warnings.md")`).toString();
  if (!warnMd.includes("as.tra")) throw new Error("warnings.md not written: " + warnMd.slice(0, 80));
  log(`11. warnings path: ${ws.length} warning(s) through Pyodide, warnings.md written`);
  py.runPython(`reset_overlay()`);

  // 12. Errors + Error context + blame populated: a word with a deliberately-wrong `final`
  //     makes one assessed miss, so finalize_run's errors (per-stage confusions), error
  //     context (per-stage autopsy), and blame branches all fill through the real Pyodide path.
  py.globals.set("_wd2", '"apa" = { gloss = "wrong", final = "xxx" }\n"ata" = { gloss = "ok", final = "ata" }\n');
  py.runPython(`write_file("words.toml", _wd2)`);
  const diag = JSON.parse(py.runPython("run_derivations()").toString());
  if (diag.error) throw new Error("errors run failed: " + JSON.stringify(diag.error));
  if (!diag.errors || !Array.isArray(diag.errors.stages) || !diag.errors.stages.length)
    throw new Error("expected populated errors, got: " + JSON.stringify(diag.errors));
  if (!diag.errors.stages.some((s) => s.label === "final" && s.confusions.length))
    throw new Error("errors missing the final stage confusions");
  if (typeof diag.accuracyMs !== "number" || typeof diag.analysisMs !== "number")
    throw new Error("run missing accuracy/analysis timing: " + JSON.stringify({a: diag.accuracyMs, n: diag.analysisMs}));
  if (!diag.blame || !diag.blame.words.length)
    throw new Error("expected a populated blame, got: " + JSON.stringify(diag.blame));
  const blamedWord = diag.blame.words[0];
  if (!blamedWord.residuals.length || !blamedWord.trajectory.length)
    throw new Error("blame word missing residuals/trajectory: " + JSON.stringify(blamedWord));
  const step = blamedWord.trajectory[0];
  if (!("target" in step) || !("fd" in step) || !("distance" in step))
    throw new Error("trajectory point missing target/d/fd: " + JSON.stringify(step));
  const errorsCsv = py.runPython(`read_file("reports/errors.csv")`).toString();
  const ctxCsv = py.runPython(`read_file("reports/error_context.csv")`).toString();
  const blameCsv = py.runPython(`read_file("reports/blame.csv")`).toString();
  if (!errorsCsv.startsWith("stage,expected,got,count,kind,examples"))
    throw new Error("errors.csv missing its header: " + errorsCsv.slice(0, 80));
  if (!ctxCsv.startsWith("stage,segment,environment,assoc. (φ),F₁,err/ok · with,err/ok · without"))
    throw new Error("error_context.csv missing its header: " + ctxCsv.slice(0, 90));
  if (!blameCsv.startsWith("gloss,step,t,form,target,d,fd"))
    throw new Error("blame.csv missing its header: " + blameCsv.slice(0, 80));
  // The accuracy CSVs are written for a lexicon with attested forms.
  const overallCsv = py.runPython(`read_file("reports/accuracy.csv")`).toString();
  const dttCsv = py.runPython(`read_file("reports/distance_to_target.csv")`).toString();
  if (!overallCsv.startsWith("stage,assessed,exact,within 1,mean phone dist,mean feature dist"))
    throw new Error("accuracy.csv missing its header: " + overallCsv.slice(0, 80));
  if (!dttCsv.startsWith("stage,gloss,derived,target,d,fd"))
    throw new Error("distance_to_target.csv missing its header: " + dttCsv.slice(0, 80));
  log(`12. errors + error context + blame (${diag.blame.words.length} word(s)) + accuracy CSVs through Pyodide`);
  py.runPython(`reset_overlay()`);

  // 13. Interactive filter over the last run: match a vowel pattern against every form,
  //     return matched words (trace + where-matched) and write filtered_output.md.
  const run13 = JSON.parse(py.runPython("run_derivations()").toString());
  if (run13.error) throw new Error("filter setup run failed: " + JSON.stringify(run13.error));
  const filt = JSON.parse(py.runPython(`run_filter("[+syllabic]")`).toString());
  if (filt.error) throw new Error("run_filter errored: " + JSON.stringify(filt.error));
  if (!filt.words.length) throw new Error("expected matched words for a vowel pattern");
  const fw = filt.words[0];
  if (!fw.card || !Array.isArray(fw.locations) || !fw.locations.length)
    throw new Error("filter word missing card/locations: " + JSON.stringify(fw));
  const filteredMd = py.runPython(`read_file("reports/filtered_output.md")`).toString();
  if (!filteredMd.startsWith("# Filtered")) throw new Error("filtered_output.md not written");
  const badFilter = JSON.parse(py.runPython(`run_filter("[bad")`).toString());
  if (!badFilter.error) throw new Error("expected run_filter to error on a bad pattern");
  log(`13. run_filter: matched ${filt.matched}/${filt.considered}, filtered_output.md written; bad pattern → error`);

  // 14. Interactive scope: restrict the accuracy analyses to words whose attested forms match,
  //     write scoped_output.md, return the subset's accuracy headline + errors.
  const scoped = JSON.parse(py.runPython(`run_scope("[+syllabic]")`).toString());
  if (scoped.error) throw new Error("run_scope errored: " + JSON.stringify(scoped.error));
  if (typeof scoped.matched !== "number" || typeof scoped.considered !== "number")
    throw new Error("run_scope missing matched/considered: " + JSON.stringify(scoped));
  const scopedMd = py.runPython(`read_file("reports/scoped_output.md")`).toString();
  if (!scopedMd.startsWith("# Scoped")) throw new Error("scoped_output.md not written");
  if (!JSON.parse(py.runPython(`run_scope("[bad")`).toString()).error)
    throw new Error("expected run_scope to error on a bad pattern");
  log(`14. run_scope: ${scoped.matched}/${scoped.considered} words, scoped_output.md written; bad pattern → error`);
  py.runPython(`reset_overlay()`);

  log("SMOKE TEST PASSED");
} catch (e) {
  const m = (e && e.message) ? e.message : String(e);
  console.log("FAILED:\n" + m.split("\n").slice(-25).join("\n"));
  process.exit(1);
}
