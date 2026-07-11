// Generates public/engine.tgz from ../src + ../projects/default (nested, so the
// bundle mirrors the repo layout and config.paths.default resolves correctly),
// and copies the verified Pyodide runtime assets into public/pyodide/.
// Wired as npm predev / prebuild.
import { execSync } from "node:child_process";
import {
  mkdirSync,
  copyFileSync,
  existsSync,
  writeFileSync,
  rmSync,
  readdirSync,
  statSync,
} from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const web = resolve(here, "..");

// The editable inventory filenames (must match FILES in src/lib/engine.js). A project
// carries its lexicon as either words.toml or words.csv; each example ships whichever it
// has (the `provided` filter below drops the absent one).
const INVENTORY = [
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
];

// The web app's picker offers every project in ../projects except `default` (which is
// the fallback base, bundled inside engine.tgz). Just drop a project folder into
// projects/ and it shows up here — no edit needed. The picker label is the folder name.
// Each project ships only the inventory files it overrides; the rest fall back to
// projects/default in-browser (per-file, exactly like the CLI's load_project).

// 1. Engine bundle (exact command from the task spec).
mkdirSync(resolve(web, "public"), { recursive: true });
execSync(
  "COPYFILE_DISABLE=1 tar czf public/engine.tgz --exclude='__pycache__' --exclude='._*' --exclude='reports' -C .. src projects/default",
  { cwd: web, stdio: "inherit", shell: "/bin/bash" }
);
console.log("built public/engine.tgz");

// 2. Copy Pyodide runtime assets (version-locked to the installed package).
const pyDir = resolve(web, "public", "pyodide");
mkdirSync(pyDir, { recursive: true });
const src = resolve(web, "node_modules", "pyodide");
for (const f of [
  "pyodide.mjs",
  "pyodide.asm.mjs",
  "pyodide.asm.wasm",
  "pyodide-lock.json",
  "python_stdlib.zip",
]) {
  copyFileSync(resolve(src, f), resolve(pyDir, f));
}
console.log("copied pyodide assets to public/pyodide/");

// 3. Example projects served as static assets + a manifest. The picker fetches
//    these on demand (they're not in engine.tgz, so the first-load download
//    stays lean). Rebuilt fresh each time so they never go stale vs the repo.
const projectsSrc = resolve(web, "..", "projects");
const projectsDir = resolve(web, "public", "projects");
rmSync(projectsDir, { recursive: true, force: true });
mkdirSync(projectsDir, { recursive: true });

// Discover projects: every subdirectory of ../projects except `default`, that carries at
// least one inventory file (so stray/support folders are skipped). Sorted for determinism.
const discovered = readdirSync(projectsSrc)
  .filter((dir) => dir !== "default")
  .filter((dir) => statSync(resolve(projectsSrc, dir)).isDirectory())
  .filter((dir) => INVENTORY.some((f) => existsSync(resolve(projectsSrc, dir, f))))
  .sort();

const manifest = [];
for (const dir of discovered) {
  const label = dir;
  const projectSrc = resolve(projectsSrc, dir);
  const outDir = resolve(projectsDir, dir);
  mkdirSync(outDir, { recursive: true });
  const provided = INVENTORY.filter((f) => existsSync(resolve(projectSrc, f)));
  for (const f of provided) copyFileSync(resolve(projectSrc, f), resolve(outDir, f));
  manifest.push({ dir, label, files: provided });
  console.log(`bundled project '${dir}' as "${label}" (${provided.length} files: ${provided.join(", ")})`);
}
writeFileSync(resolve(projectsDir, "index.json"), JSON.stringify({ projects: manifest }, null, 2));
console.log(`wrote public/projects/index.json (${manifest.length} project(s))`);
