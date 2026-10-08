// The engine worker: runs the Rust engine (WebAssembly) off the main thread, so the page stays
// responsive during a run. scripts/build-engine.mjs copies this file to public/engine/worker.js,
// beside the wasm-pack output, so its imports resolve without a bundler.
//
// Each message is {id, method, args, overlay?}; the reply is {id, result, reports} or
// {id, error}. An `overlay` (name → text) replaces the user's project files before the call.
import init, { Fortis } from "./fortis_web.js";

const ready = init().then(() => new Fortis());

let analysisStart = 0;

self.onmessage = async ({ data }) => {
  const { id, method, args = [], overlay } = data;
  try {
    const fortis = await ready;
    if (overlay) {
      fortis.clear_project();
      for (const [name, text] of Object.entries(overlay)) fortis.put("project/" + name, text);
    }
    if (method === "init") {
      // args[0]: the shipped default project, name → text
      for (const [name, text] of Object.entries(args[0])) fortis.put("default/" + name, text);
      postMessage({ id, result: null });
      return;
    }
    if (method === "finalize_run") analysisStart = performance.now();
    const result = JSON.parse(fortis[method](...args));
    let reports = null;
    if (result && !Array.isArray(result) && "reports" in result) {
      reports = result.reports;
      delete result.reports;
    }
    // The analysis summary carries its wall-clock time, measured here around the steps.
    if ((method === "finalize_run" || method === "analysis_step") && result.result)
      result.result.analysisMs = Math.round(performance.now() - analysisStart);
    postMessage({ id, result, reports });
  } catch (e) {
    postMessage({ id, error: e?.message ?? String(e) });
  }
};
