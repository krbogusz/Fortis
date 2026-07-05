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
  const md = py.runPython(`read_file("output.md")`).toString();
  const csv = py.runPython(`read_file("derivation_table.csv")`).toString();
  if (!md.startsWith("# Output")) throw new Error("output.md missing its header: " + md.slice(0, 80));
  if (!csv.startsWith("ipa,gloss,")) throw new Error("derivation_table.csv missing its header row: " + csv.slice(0, 80));
  log(`5. reports written: output.md (${md.length} chars), derivation_table.csv (${csv.split("\n").length} rows)`);

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
  if (!astra || !astra.clusters.includes("str") || !astra.stage)
    throw new Error("expected a populated 'astra' warning, got: " + JSON.stringify(ws));
  const warnMd = py.runPython(`read_file("warnings.md")`).toString();
  if (!warnMd.includes("as.tra")) throw new Error("warnings.md not written: " + warnMd.slice(0, 80));
  log(`11. warnings path: ${ws.length} warning(s) through Pyodide, warnings.md written`);
  py.runPython(`reset_overlay()`);

  // 12. Diagnosis + blame populated: a word with a deliberately-wrong `final` makes one
  //     graded miss, so finalize_run's diagnosis (confusions + autopsy) and blame branches
  //     both fill and round-trip through the real Pyodide path.
  py.globals.set("_wd2", '"apa" = { gloss = "wrong", final = "xxx" }\n"ata" = { gloss = "ok", final = "ata" }\n');
  py.runPython(`write_file("words.toml", _wd2)`);
  const diag = JSON.parse(py.runPython("run_derivations()").toString());
  if (diag.error) throw new Error("diagnosis run failed: " + JSON.stringify(diag.error));
  if (!diag.diagnosis || !diag.diagnosis.confusions.length)
    throw new Error("expected a populated diagnosis, got: " + JSON.stringify(diag.diagnosis));
  if (!diag.timeline || !Array.isArray(diag.timeline.byTime) || !Array.isArray(diag.timeline.stages))
    throw new Error("timeline missing byTime/stages: " + JSON.stringify(diag.timeline));
  if (!diag.timeline.stages.some((s) => s.label === "final"))
    throw new Error("per-stage timeline missing the final stage");
  if (!diag.blame || !diag.blame.words.length)
    throw new Error("expected a populated blame, got: " + JSON.stringify(diag.blame));
  const blamedWord = diag.blame.words[0];
  if (!blamedWord.residuals.length || !blamedWord.trajectory.length)
    throw new Error("blame word missing residuals/trajectory: " + JSON.stringify(blamedWord));
  const step = blamedWord.trajectory[0];
  if (!("target" in step) || !("fd" in step) || !("distance" in step))
    throw new Error("trajectory point missing target/d/fd: " + JSON.stringify(step));
  const diagMd = py.runPython(`read_file("diagnosis.md")`).toString();
  const timelineMd = py.runPython(`read_file("timeline.md")`).toString();
  const blameMd = py.runPython(`read_file("blame.md")`).toString();
  if (!diagMd.startsWith("# Diagnosis")) throw new Error("diagnosis.md not written: " + diagMd.slice(0, 80));
  if (!timelineMd.startsWith("# Timeline")) throw new Error("timeline.md not written: " + timelineMd.slice(0, 80));
  if (!blameMd.startsWith("# Blame")) throw new Error("blame.md not written: " + blameMd.slice(0, 80));
  log(`12. diagnosis + timeline + blame (${diag.blame.words.length} word(s)) through Pyodide, reports written`);
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
  const filteredMd = py.runPython(`read_file("filtered_output.md")`).toString();
  if (!filteredMd.startsWith("# Filtered")) throw new Error("filtered_output.md not written");
  const badFilter = JSON.parse(py.runPython(`run_filter("[bad")`).toString());
  if (!badFilter.error) throw new Error("expected run_filter to error on a bad pattern");
  log(`13. run_filter: matched ${filt.matched}/${filt.considered}, filtered_output.md written; bad pattern → error`);
  py.runPython(`reset_overlay()`);

  log("SMOKE TEST PASSED");
} catch (e) {
  const m = (e && e.message) ? e.message : String(e);
  console.log("FAILED:\n" + m.split("\n").slice(-25).join("\n"));
  process.exit(1);
}
