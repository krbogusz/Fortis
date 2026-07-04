// Generates public/engine.tgz from ../src + ../projects/default (nested, so the
// bundle mirrors the repo layout and config.paths.default resolves correctly),
// and copies the verified Pyodide runtime assets into public/pyodide/.
// Wired as npm predev / prebuild.
import { execSync } from "node:child_process";
import { mkdirSync, copyFileSync, existsSync, writeFileSync, rmSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const web = resolve(here, "..");

// The 8 editable inventory filenames (must match FILES in src/lib/engine.js).
const INVENTORY = [
  "features.toml",
  "letters.csv",
  "diacritics.toml",
  "sonorities.toml",
  "syllable_parts.toml",
  "tiers.toml",
  "words.toml",
  "rules.toml",
];

// Example projects offered in the web app's picker. Each ships only the
// inventory files it actually overrides; the rest fall back to projects/default
// in-browser (per-file, exactly like the CLI's load_project). Add a row here to
// expose another project — no other file needs to change.
const EXAMPLE_PROJECTS = [
  { dir: "latin_to_french", label: "Latin → French" },
];

// 1. Engine bundle (exact command from the task spec).
mkdirSync(resolve(web, "public"), { recursive: true });
execSync(
  "COPYFILE_DISABLE=1 tar czf public/engine.tgz --exclude='__pycache__' --exclude='._*' -C .. src projects/default",
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
const projectsDir = resolve(web, "public", "projects");
rmSync(projectsDir, { recursive: true, force: true });
mkdirSync(projectsDir, { recursive: true });
const manifest = [];
for (const { dir, label } of EXAMPLE_PROJECTS) {
  const projectSrc = resolve(web, "..", "projects", dir);
  const outDir = resolve(projectsDir, dir);
  mkdirSync(outDir, { recursive: true });
  const provided = INVENTORY.filter((f) => existsSync(resolve(projectSrc, f)));
  for (const f of provided) copyFileSync(resolve(projectSrc, f), resolve(outDir, f));
  manifest.push({ dir, label, files: provided });
  console.log(`bundled example project '${dir}' (${provided.length} files: ${provided.join(", ")})`);
}
writeFileSync(resolve(projectsDir, "index.json"), JSON.stringify({ projects: manifest }, null, 2));
console.log(`wrote public/projects/index.json (${manifest.length} project(s))`);
