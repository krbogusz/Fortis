"""Rule dependency graph — which rules feed which, from what actually fired.

Read empirically off the derivations, not the rule text (so back-references, agreement,
and letter results all resolve to real segments). For each firing we look at its changed
region: the segment(s) it *consumed* (the ``before`` region it rewrote) and the segment(s)
it *produced* (the ``after`` region left in their place). Within one word's firing order, a
firing **depends on** the most recent earlier firing that produced a segment it consumed —
e.g. ``n → ŋ`` produces ``ŋ``, then ``ŋ → ɲ`` consumes that ``ŋ``, so the second rule is fed
by the first. Edges are aggregated to the rule level over every word. A rule fed by nothing
is an unconnected **root**.

:func:`build_dependency_graph` returns the nodes and edges (it needs the derivations);
:func:`render_dependency_html` renders a self-contained, horizontally-scrolling SVG view
(time on the x-axis in period bands, feeding depth on the y-axis, hover to trace a rule's
dependencies).
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass

from src.fortis.application.rendering import describe_change
from src.fortis.application.tiers import lower_tiers
from src.fortis.models.bundles import FeatureBundle
from src.fortis.models.derivation import Derivation
from src.fortis.models.project import Project
from src.fortis.models.rules import RuleInventory

_SUBRULE_SUFFIX = re.compile(r"#\d+$")  # a list-definition sub-rule's id suffix


@dataclass(frozen=True)
class RuleNode:
    """One rule in the graph, with its feature dependencies resolved.

    ``requires``/``produces`` are the segments (IPA strings) this rule consumed and
    produced across all its firings; ``deps`` are the indices of the earlier rules that
    feed this one; ``depth`` is its longest feeding chain to a root (0 for a root).
    """

    index: int
    id: str
    name: str
    time: int | None
    requires: tuple[str, ...]
    produces: tuple[str, ...]
    deps: tuple[int, ...]
    depth: int


@dataclass(frozen=True)
class DependencyEdge:
    """``source`` (the later, dependent rule) is fed by ``target`` (earlier), via ``via``."""

    source: int
    target: int
    via: tuple[str, ...]


@dataclass(frozen=True)
class DependencyGraph:
    """The full graph: rules as nodes, feeding relations as edges."""

    nodes: tuple[RuleNode, ...]
    edges: tuple[DependencyEdge, ...]


def _change(
    before: list[FeatureBundle], after: list[FeatureBundle], project: Project
) -> tuple[set[str], set[str]]:
    """One firing's ``(consumed, produced)`` segments over its changed region.

    Common leading/trailing segments are trimmed so only the differing region counts.
    Reads the same per-segment deltas the rule-firings ``changes`` column reports
    (:func:`describe_change`): each ``X→Y`` delta consumes segment ``X`` and produces ``Y``
    (``∅`` on either side for a deletion/insertion). So ``n̪ → ŋ`` consumes ``n̪`` and
    produces ``ŋ``, and shortening every long vowel in a word touches only those vowels —
    describe_change diffs position by position, not just the outer edges.
    """
    consumed: set[str] = set()
    produced: set[str] = set()
    for delta in describe_change(before, after, project).split(", "):
        left, _, right = delta.partition("→")
        if left and left != "∅":
            consumed.add(left)
        if right and right != "∅":
            produced.add(right)
    return consumed, produced


def build_dependency_graph(
    derivations: list[Derivation], rules: RuleInventory, project: Project
) -> DependencyGraph:
    """Feeding graph read off the actual firings in *derivations*.

    One node per rule (sub-rules of a list definition merged), in time order — from
    *rules* so a rule that never fired still appears (as an isolated node). Within each
    word's firing order, a firing links to the most recent earlier firing that produced a
    value it required; those links are aggregated to the rule level across every word.
    """
    # One node per distinct base id, in (time, file) order.
    index: dict[str, int] = {}
    meta: list[tuple[str, str, int | None]] = []
    for t in sorted(rules.keys(), key=lambda t: (t is None, t)):
        for rule in rules[t]:
            base = _SUBRULE_SUFFIX.sub("", rule.id)
            if base not in index:
                index[base] = len(meta)
                meta.append((base, rule.name or base, rule.time))

    node_requires: dict[str, set[str]] = defaultdict(set)
    node_produces: dict[str, set[str]] = defaultdict(set)
    edge_via: dict[tuple[int, int], set[str]] = defaultdict(set)  # (dependent, dependency) -> features
    for derivation in derivations:
        producer: dict[str, str] = {}  # feature-value -> base id that last produced it, this word
        for step in derivation.steps:
            base = _SUBRULE_SUFFIX.sub("", step.rule.id)
            if base not in index:
                continue
            required, produced = _change(
                lower_tiers(step.before), lower_tiers(step.after), project
            )
            node_requires[base] |= required
            node_produces[base] |= produced
            for value in required:
                source = producer.get(value)
                if source is not None and source != base and index[source] < index[base]:
                    edge_via[(index[base], index[source])].add(value)
            for value in produced:
                producer[value] = base

    deps: dict[int, set[int]] = defaultdict(set)
    edges: list[DependencyEdge] = []
    for (dependent, dependency), via in edge_via.items():
        deps[dependent].add(dependency)
        edges.append(DependencyEdge(dependent, dependency, tuple(sorted(via))))
    depth = [0] * len(meta)
    for i in range(len(meta)):  # deps[i] all have index < i, so depth is well-defined in order
        depth[i] = 1 + max((depth[d] for d in deps[i]), default=-1)
    nodes = tuple(
        RuleNode(
            index=i,
            id=base,
            name=name,
            time=time,
            requires=tuple(sorted(node_requires[base])),
            produces=tuple(sorted(node_produces[base])),
            deps=tuple(sorted(deps[i])),
            depth=depth[i],
        )
        for i, (base, name, time) in enumerate(meta)
    )
    return DependencyGraph(nodes, tuple(edges))


def dependency_layout(graph: DependencyGraph) -> dict:
    """The graph laid out for rendering — nodes with x/y, edges, time bands, and size.

    Each time is a block on the x-axis; within a block, rules advance one sub-column per
    step of *same-time* feeding: a root (or a rule fed only by earlier times) sits in the
    block's first column; a rule fed by a same-time rule sits one column to its right. y
    stacks the rules that share a (time, column). JSON-serialisable, so both the standalone
    HTML (:func:`render_dependency_html`) and the webapp render from it.
    """
    sub_w, row_h, pad_x, pad_y, gap = 150, 16, 60, 80, 34
    nodes = graph.nodes
    time_of = {n.index: n.time for n in nodes}

    # Sub-column within a time = depth of the same-time feeding chain (0 for a root or a
    # rule fed only by earlier times). deps have smaller indices, so this resolves in order.
    column: dict[int, int] = {}
    for n in nodes:
        same_time = [d for d in n.deps if time_of[d] == n.time]
        column[n.index] = 0 if not same_time else 1 + max(column[d] for d in same_time)

    times = sorted({n.time for n in nodes}, key=lambda t: (t is None, t))
    max_col = {t: 0 for t in times}
    for n in nodes:
        max_col[n.time] = max(max_col[n.time], column[n.index])
    base_x: dict[int | None, float] = {}  # left edge (first column centre) of each time block
    cursor = float(pad_x)
    for t in times:
        base_x[t] = cursor
        cursor += (max_col[t] + 1) * sub_w + gap

    positions: dict[int, tuple[float, float]] = {}
    stack: dict[tuple[int | None, int], int] = {}  # (time, column) -> next row
    for n in nodes:
        col = column[n.index]
        row = stack.get((n.time, col), 0)
        positions[n.index] = (base_x[n.time] + col * sub_w, pad_y + row * row_h)
        stack[(n.time, col)] = row + 1

    return {
        "nodes": [
            {"i": n.index, "id": n.id, "name": n.name,
             "t": n.time if n.time is not None else None, "depth": n.depth,
             "x": positions[n.index][0], "y": positions[n.index][1],
             "requires": list(n.requires), "produces": list(n.produces), "deps": list(n.deps)}
            for n in nodes
        ],
        "edges": [{"from": e.source, "to": e.target} for e in graph.edges],
        "bands": [
            {"x0": base_x[t] - sub_w / 2, "x1": base_x[t] + max_col[t] * sub_w + sub_w / 2,
             "label": "untimed" if t is None else str(t)}
            for t in times
        ],
        "width": int(cursor + pad_x),
        "height": pad_y + max(stack.values(), default=1) * row_h + 40,
        "rules": len(nodes),
        "edgeCount": len(graph.edges),
        "roots": sum(1 for n in nodes if not n.deps),
    }


def render_dependency_html(graph: DependencyGraph) -> str:
    """A self-contained HTML page of the graph (the standalone/CLI report)."""
    layout = dependency_layout(graph)
    return (
        _HTML_TEMPLATE
        .replace("__WIDTH__", str(layout["width"]))
        .replace("__HEIGHT__", str(layout["height"]))
        .replace("__HEIGHT_MINUS__", str(layout["height"] - 40))
        .replace("__NRULES__", str(layout["rules"]))
        .replace("__NEDGES__", str(layout["edgeCount"]))
        .replace("__NROOTS__", str(layout["roots"]))
        .replace("__BANDS__", json.dumps(layout["bands"]))
        .replace("__DATA__", json.dumps({"nodes": layout["nodes"], "edges": layout["edges"]}))
    )


_HTML_TEMPLATE = """<!doctype html><html><head><meta charset="utf-8">
<title>Rule dependence tree</title>
<style>
 :root{--bg:#fff;--panel:#faf9fb;--code-bg:#f4f3ec;--border:#e2e0e6;--text:#4b4753;
   --text-h:#08060d;--muted:#8a8594;--dep:#2f6fbf;--dependent:#a67a10;--shadow:rgba(0,0,0,.08) 0 4px 12px -4px}
 @media (prefers-color-scheme:dark){:root{--bg:#14151a;--panel:#1a1b21;--code-bg:#1f2028;--border:#2c2e38;
   --text:#c2c6cf;--text-h:#f3f4f6;--muted:#8b8f99;--dep:#6ea8ff;--dependent:#e0b84d;--shadow:rgba(0,0,0,.4) 0 4px 12px -4px}}
 html,body{margin:0;background:var(--bg);color:var(--text);font:13px/1.4 system-ui,sans-serif}
 header{padding:10px 16px;border-bottom:1px solid var(--border);position:sticky;top:0;left:0;background:var(--bg);z-index:5}
 header b{color:var(--text-h)}
 .hint{color:var(--muted)}
 .k-dep{color:var(--dep);font-weight:600} .k-dependent{color:var(--dependent);font-weight:600}
 #wrap{overflow:auto;height:calc(100vh - 52px)}
 svg{display:block;font:11px system-ui,sans-serif}
 .band{fill:var(--panel)} .band.odd{fill:var(--code-bg)}
 .bandlbl{fill:var(--muted);font-size:11px}
 .edge{fill:none;stroke:var(--border);stroke-width:1;opacity:.55}
 .edge.dim{opacity:.06}
 .edge.dep{stroke:var(--dep);opacity:.95;stroke-width:1.6}
 .edge.dependent{stroke:var(--dependent);opacity:.95;stroke-width:1.6}
 .node{fill:var(--muted);stroke:var(--bg);stroke-width:1;cursor:pointer}
 .node.root{stroke:var(--text-h);stroke-width:1.5}
 .node.focus{fill:var(--text-h)}
 .node.dep{fill:var(--dep)} .node.dependent{fill:var(--dependent)}
 .node.dim{opacity:.16}
 #tip{position:fixed;pointer-events:none;background:var(--panel);border:1px solid var(--border);border-radius:6px;
   padding:8px 10px;max-width:330px;font:12px system-ui,sans-serif;display:none;z-index:10;box-shadow:var(--shadow)}
 #tip .nm{color:var(--text-h);font-weight:600;margin-bottom:3px}
 #tip code{color:var(--text)} #tip .req,#tip .prod{color:var(--text);margin-top:2px}
 #tip .fed{color:var(--dep);margin-top:4px} #tip .feeds{color:var(--dependent)}
 #tip .ids{color:var(--muted);font-size:11px;word-break:break-word}
</style></head><body>
<header><b>Rule dependence tree</b>
 &nbsp;<span class="hint">__NRULES__ rules · __NEDGES__ feeding edges · __NROOTS__ unconnected roots
 &nbsp;·&nbsp; x = time, +1 sub-column per same-time dependency &rarr; · hover a node:
 <span class="k-dep">blue</span> = fed by · <span class="k-dependent">orange</span> = feeds</span></header>
<div id="wrap"><svg id="svg" width="__WIDTH__" height="__HEIGHT__"></svg></div>
<div id="tip"></div>
<script>
const D=__DATA__, bands=__BANDS__;
const H=__HEIGHT_MINUS__;
const svg=document.getElementById('svg'), tip=document.getElementById('tip');
const NS='http://www.w3.org/2000/svg';
const el=(n,a)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);return e;};
const baseCls=n=>D.nodes[n].deps.length?'node':'node root';
bands.forEach((b,i)=>{
  svg.appendChild(el('rect',{class:i%2?'band odd':'band',x:b.x0,y:40,width:b.x1-b.x0,height:H}));
  const t=el('text',{class:'bandlbl',x:(b.x0+b.x1)/2,y:26,'text-anchor':'middle'});
  t.textContent=b.label; svg.appendChild(t);
});
const node=i=>D.nodes[i];
const edgeEls=[];
D.edges.forEach(e=>{const a=node(e.from),b=node(e.to);  // e.from depends on e.to
  const mx=(a.x+b.x)/2+(a.x===b.x?60:0);  // bulge same-column edges sideways
  const p=el('path',{class:'edge',d:`M${b.x},${b.y} C${mx},${b.y} ${mx},${a.y} ${a.x},${a.y}`});
  svg.appendChild(p); edgeEls.push({el:p,from:e.from,to:e.to});
});
const nodeEls=[];
D.nodes.forEach(n=>{
  const c=el('circle',{class:baseCls(n.i),cx:n.x,cy:n.y,r:4.5,'data-i':n.i});
  svg.appendChild(c); nodeEls.push(c);
  c.addEventListener('mouseenter',()=>hover(n));
  c.addEventListener('mousemove',ev=>{tip.style.left=Math.min(ev.clientX+14,innerWidth-348)+'px';tip.style.top=(ev.clientY+14)+'px';});
  c.addEventListener('mouseleave',clear);
});
function hover(n){
  const deps=new Set(n.deps), dependents=new Set();
  D.edges.forEach(e=>{if(e.to===n.i)dependents.add(e.from);});
  edgeEls.forEach(({el,from,to})=>{
    el.setAttribute('class', from===n.i?'edge dep':to===n.i?'edge dependent':'edge dim');
  });
  nodeEls.forEach(c=>{const i=+c.getAttribute('data-i');
    c.setAttribute('class', i===n.i?'node focus':deps.has(i)?'node dep':dependents.has(i)?'node dependent':baseCls(i)+' dim');
  });
  const fedBy=n.deps.map(i=>D.nodes[i].id), feeds=[...dependents].map(i=>D.nodes[i].id);
  tip.style.display='block';
  tip.innerHTML=`<div class="nm">${n.name}</div>`+
    `<div class="hint">t=${n.t===null?'untimed':n.t} · depth ${n.depth}${n.deps.length?'':' (root)'} · <code>${n.id}</code></div>`+
    `<div class="req">needs: ${n.requires.join(' ')||'—'}</div>`+
    `<div class="prod">makes: ${n.produces.join(' ')||'—'}</div>`+
    `<div class="fed">fed by (${fedBy.length}):</div><div class="ids">${fedBy.join(', ')||'—'}</div>`+
    `<div class="feeds">feeds (${feeds.length}):</div><div class="ids">${feeds.join(', ')||'—'}</div>`;
}
function clear(){tip.style.display='none';
  edgeEls.forEach(({el})=>el.setAttribute('class','edge'));
  nodeEls.forEach(c=>c.setAttribute('class', baseCls(+c.getAttribute('data-i'))));}
</script></body></html>"""
