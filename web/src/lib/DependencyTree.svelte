<script>
  // The rule feeding graph (from analysis.dependencies.dependency_layout). x = time blocks,
  // sub-columns by same-time feeding depth; y stacks; hover a node to trace its feeding.
  let { data = null } = $props();

  let hovered = $state(null); // hovered node index, or null
  let tipX = $state(0);
  let tipY = $state(0);

  const nodes = $derived(data?.nodes ?? []);
  const edges = $derived(data?.edges ?? []);
  const bands = $derived(data?.bands ?? []);
  const byIndex = $derived(new Map(nodes.map((n) => [n.i, n])));
  const hoveredNode = $derived(hovered == null ? null : byIndex.get(hovered));

  // edge = {from: dependent, to: dependency}; from depends on to.
  const dependsOn = $derived(new Set(hoveredNode?.deps ?? [])); // nodes the hovered one needs
  const dependents = $derived.by(() => {
    const set = new Set();
    if (hovered != null) for (const e of edges) if (e.to === hovered) set.add(e.from);
    return set;
  });

  function path(e) {
    const dep = byIndex.get(e.to);
    const src = byIndex.get(e.from);
    const mx = (dep.x + src.x) / 2 + (dep.x === src.x ? 60 : 0); // bulge same-column edges
    return `M${src.x},${src.y} C${mx},${src.y} ${mx},${dep.y} ${dep.x},${dep.y}`;
  }
  function edgeClass(e) {
    if (hovered == null) return "edge";
    if (e.from === hovered) return "edge dep"; // hovered depends on e.to
    if (e.to === hovered) return "edge dependent"; // e.from depends on hovered
    return "edge dim";
  }
  function nodeClass(n) {
    if (hovered == null) return n.deps.length ? "node" : "node root";
    if (n.i === hovered) return "node focus";
    if (dependsOn.has(n.i)) return "node dep";
    if (dependents.has(n.i)) return "node dependent";
    return "node dim";
  }
  function enter(n, ev) {
    hovered = n.i;
    move(ev);
  }
  function move(ev) {
    tipX = Math.min(ev.clientX + 14, window.innerWidth - 348);
    tipY = ev.clientY + 14;
  }
</script>

{#if data}
  <div class="tree-outer">
    <div class="tree-meta">
      <span class="mgrp">{data.rules} rules · {data.edgeCount} feeding edges · {data.roots} unconnected roots</span>
      <span class="msep">·</span>
      <span class="mgrp">x = time, +1 column per same-time dependency</span>
      <span class="msep">·</span>
      <span class="mgrp">hover a node: <span class="k-dep">blue</span> = fed by · <span class="k-dependent">orange</span> = feeds</span>
    </div>
    <div class="tree-wrap">
      <svg width={data.width} height={data.height} onmouseleave={() => (hovered = null)} role="img" aria-label="rule dependence tree">
      {#each bands as b, i (i)}
        <rect x={b.x0} y="40" width={b.x1 - b.x0} height={data.height - 40} class={i % 2 ? "band odd" : "band"} />
        <text x={(b.x0 + b.x1) / 2} y="26" class="bandlbl">{b.label}</text>
      {/each}
      {#each edges as e, i (i)}
        <path class={edgeClass(e)} d={path(e)} />
      {/each}
      {#each nodes as n (n.i)}
        <circle class={nodeClass(n)} cx={n.x} cy={n.y} r="4.5"
          onmouseenter={(ev) => enter(n, ev)} onmousemove={move}
          onmouseleave={() => (hovered = null)} role="img" />
      {/each}
    </svg>
    {#if hoveredNode}
      <div class="tip" style="left:{tipX}px;top:{tipY}px">
        <div class="nm">{hoveredNode.name}</div>
        <div class="meta">
          t={hoveredNode.t ?? "untimed"} · depth {hoveredNode.depth}{hoveredNode.deps.length ? "" : " (root)"}
          · <code>{hoveredNode.id}</code>
        </div>
        <div class="needs">needs: {hoveredNode.requires.join(" ") || "—"}</div>
        <div class="makes">makes: {hoveredNode.produces.join(" ") || "—"}</div>
        <div class="fed">fed by ({hoveredNode.deps.length}):</div>
        <div class="ids">{hoveredNode.deps.map((i) => byIndex.get(i).id).join(", ") || "—"}</div>
        <div class="feeds">feeds ({dependents.size}):</div>
        <div class="ids">{[...dependents].map((i) => byIndex.get(i).id).join(", ") || "—"}</div>
      </div>
    {/if}
    </div>
  </div>
{/if}

<style>
  .tree-outer {
    display: flex;
    flex-direction: column;
    flex: 1 1 0;
    min-height: 0;
    background: var(--bg);
  }
  .tree-wrap {
    flex: 1 1 auto;
    min-height: 0;
    overflow: auto;
    background: var(--bg);
    position: relative;
  }
  .tree-meta {
    flex: none;
    padding: 6px 12px;
    font: var(--fs-body) / 1.4 var(--sans);
    color: var(--muted);
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    z-index: 3;
    white-space: normal;
    overflow-wrap: break-word;
  }
  .tree-meta .mgrp {
    white-space: nowrap;
  }
  .tree-meta .msep {
    margin: 0 0.5ch;
    opacity: 0.6;
  }
  .k-dep {
    color: var(--tree-dep);
    font-weight: 600;
  }
  .k-dependent {
    color: var(--warn-fg);
    font-weight: 600;
  }
  svg {
    display: block;
    font-family: var(--sans);
  }
  .band {
    fill: var(--panel);
  }
  .band.odd {
    fill: var(--code-bg);
  }
  .bandlbl {
    fill: var(--muted);
    font-size: 11px;
    text-anchor: middle;
  }
  .edge {
    fill: none;
    stroke: var(--border);
    stroke-width: 1;
    opacity: 0.55;
  }
  .edge.dim {
    opacity: 0.06;
  }
  .edge.dep {
    stroke: var(--tree-dep);
    opacity: 0.95;
    stroke-width: 1.6;
  }
  .edge.dependent {
    stroke: var(--warn-fg);
    opacity: 0.95;
    stroke-width: 1.6;
  }
  .node {
    fill: var(--muted);
    stroke: var(--bg);
    stroke-width: 1;
    cursor: pointer;
  }
  .node.root {
    stroke: var(--text-h);
    stroke-width: 1.5;
  }
  .node.focus {
    fill: var(--text-h);
  }
  .node.dep {
    fill: var(--tree-dep);
  }
  .node.dependent {
    fill: var(--warn-fg);
  }
  .node.dim {
    opacity: 0.16;
  }
  .tip {
    position: fixed;
    pointer-events: none;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 10px;
    max-width: 330px;
    font: 12px / 1.4 var(--sans);
    box-shadow: var(--shadow);
    z-index: 20;
  }
  .tip .nm {
    color: var(--text-h);
    font-weight: 600;
    margin-bottom: 3px;
  }
  .tip .meta {
    color: var(--muted);
  }
  .tip code {
    color: var(--text);
  }
  .tip .needs,
  .tip .makes {
    font-family: var(--ipa);
    margin-top: 2px;
    color: var(--text);
  }
  .tip .fed {
    color: var(--tree-dep);
    margin-top: 4px;
  }
  .tip .feeds {
    color: var(--warn-fg);
  }
  .tip .ids {
    color: var(--muted);
    font-size: 11px;
    word-break: break-word;
  }
</style>
