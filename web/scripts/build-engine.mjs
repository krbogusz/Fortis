// Builds the Rust engine (../crates/fortis-web) to WebAssembly with wasm-pack and copies it, with its
// worker script, into public/engine/. Also copies the shipped default project and the example
// projects into public/projects/.
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
import { homedir } from "node:os";
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
// the fallback base). Just drop a project folder into projects/ and it shows up here — no
// edit needed. The picker label is the folder name. Each project ships only the inventory
// files it overrides; the rest fall back to projects/default in-browser (per-file, exactly
// like the CLI's load_project).

// 1. The engine. wasm-pack fetches the wasm-bindgen CLI that matches the crate's version.
const crate = resolve(web, "..", "crates", "fortis-web");
const env = { ...process.env, PATH: `${resolve(homedir(), ".cargo", "bin")}:${process.env.PATH}` };
execSync("wasm-pack build --release --target web --no-pack --out-dir pkg", { cwd: crate, stdio: "inherit", env });
const engineDir = resolve(web, "public", "engine");
rmSync(engineDir, { recursive: true, force: true });
mkdirSync(engineDir, { recursive: true });
for (const f of ["fortis_web.js", "fortis_web_bg.wasm"]) copyFileSync(resolve(crate, "pkg", f), resolve(engineDir, f));
copyFileSync(resolve(web, "src", "lib", "engine.worker.js"), resolve(engineDir, "worker.js"));
console.log("built the engine into public/engine/");

// 2. The default project and the example projects, served as static assets + a manifest.
//    The engine loads the default at start; the picker fetches an example on demand.
//    Rebuilt fresh each time so they never go stale vs the repo.
const projectsSrc = resolve(web, "..", "projects");
const projectsDir = resolve(web, "public", "projects");
rmSync(projectsDir, { recursive: true, force: true });
mkdirSync(projectsDir, { recursive: true });

const defaultSrc = resolve(projectsSrc, "default");
const defaultFiles = [...INVENTORY, "settings.toml"].filter((f) => existsSync(resolve(defaultSrc, f)));
mkdirSync(resolve(projectsDir, "default"), { recursive: true });
for (const f of defaultFiles) copyFileSync(resolve(defaultSrc, f), resolve(projectsDir, "default", f));
console.log(`bundled the default project (${defaultFiles.length} files)`);

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
writeFileSync(resolve(projectsDir, "index.json"), JSON.stringify({ default: defaultFiles, projects: manifest }, null, 2));
console.log(`wrote public/projects/index.json (${manifest.length} project(s))`);
