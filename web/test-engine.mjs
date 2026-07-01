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
  const csv = py.runPython(`read_file("output.csv")`).toString();
  if (!md.startsWith("# Output")) throw new Error("output.md missing its header: " + md.slice(0, 80));
  if (!csv.startsWith("ipa,gloss,")) throw new Error("output.csv missing its header row: " + csv.slice(0, 80));
  log(`5. reports written: output.md (${md.length} chars), output.csv (${csv.split("\n").length} rows)`);

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

  log("SMOKE TEST PASSED");
} catch (e) {
  const m = (e && e.message) ? e.message : String(e);
  console.log("FAILED:\n" + m.split("\n").slice(-25).join("\n"));
  process.exit(1);
}
