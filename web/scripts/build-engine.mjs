// Generates public/engine.tgz from ../src + ../projects/default,
// and copies the verified Pyodide runtime assets into public/pyodide/.
// Wired as npm predev / prebuild.
import { execSync } from "node:child_process";
import { mkdirSync, copyFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const web = resolve(here, "..");

// 1. Engine bundle (exact command from the task spec).
mkdirSync(resolve(web, "public"), { recursive: true });
execSync(
  "COPYFILE_DISABLE=1 tar czf public/engine.tgz --exclude='__pycache__' --exclude='._*' -C .. src -C projects default",
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
