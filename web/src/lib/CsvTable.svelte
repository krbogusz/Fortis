<script>
  // A CSV table view. Read-only by default; pass an `onchange` callback to make it editable.
  //  - Click a cell to select it; arrow keys / Tab move the selection.
  //  - Enter or F2 (or just start typing) edits the selected cell; Enter/Tab commit and move,
  //    Escape cancels.
  //  - The `⋮` handle on each row/column opens a menu (add before/after, remove) or is dragged
  //    to reorder — a line marks exactly where it will land, and the moving row/column dims.
  // RFC4180 quoting: a quoted field may contain commas, newlines, and doubled `""`.
  // `wideColumns` is a list of header names that get a roomier default width (a higher cap and
  // a minimum), for content-heavy columns like the rule table's `changes`/`matched`.
  // `italicColumn` names a header whose non-empty cells italicize the whole data row —
  // used to flag sporadic (word-scoped) rules in the rule-firings table.
  let { content = "", onchange = null, wideColumns = [], italicColumn = null } = $props();
  const editable = $derived(typeof onchange === "function");

  function parseCsv(text) {
    const rows = [];
    let row = [],
      field = "",
      inQuotes = false;
    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (inQuotes) {
        if (c === '"' && text[i + 1] === '"') {
          field += '"';
          i++;
        } else if (c === '"') {
          inQuotes = false;
        } else {
          field += c;
        }
      } else if (c === '"') {
        inQuotes = true;
      } else if (c === ",") {
        row.push(field);
        field = "";
      } else if (c === "\n" || c === "\r") {
        if (c === "\r" && text[i + 1] === "\n") i++;
        row.push(field);
        rows.push(row);
        row = [];
        field = "";
      } else {
        field += c;
      }
    }
    if (field !== "" || row.length) {
      row.push(field);
      rows.push(row);
    }
    return rows;
  }

  function toCsv(rows) {
    const esc = (f) =>
      /[",\n\r]/.test(f) ? '"' + String(f).replace(/"/g, '""') + '"' : String(f);
    return rows.map((r) => r.map(esc).join(",")).join("\n") + "\n";
  }

  let rows = $state([]);
  let colOverrides = $state({}); // colIndex → user-dragged width (px); overrides the measured cap
  let sel = $state(null); // {r, c} — the selected cell (r = 0 is the header row)
  let editing = $state(false); // whether the selected cell is in text-edit mode
  let menu = $state(null); // {kind:"row"|"col", index, x, y} — the open ⋮ menu
  let drag = $state(null); // {kind, from} — an in-flight reorder
  let dropIndex = $state(null); // {kind, index} — the insertion position (0..n) under the cursor
  let tableEl = $state(null); // the <table>, for moving DOM focus onto the selected cell
  let wrapEl = $state(null); // the scroll container, for virtualization
  let scrollTop = $state(0);
  let scrollLeft = $state(0);
  let viewportH = $state(600);
  let viewportW = $state(800); // nonzero so the first paint isn't a collapsed column window
  let rowH = $state(24); // measured body-row height (rows are uniform, single-line)
  const OVERSCAN = 10; // extra rows rendered above/below the viewport
  const COL_OVERSCAN = 6; // extra columns rendered left/right of the viewport
  let reverting = false; // an Escape in progress — discard the edit on blur
  let editOrig = ""; // the cell value when editing began, for Escape to restore
  let lastEmitted = " uninitialised";
  $effect.pre(() => {
    if (content !== lastEmitted) {
      rows = content.trim() ? parseCsv(content.trim()) : [];
      lastEmitted = content;
      colOverrides = {}; // new content ⇒ drop per-column width overrides (indices may remap)
      sel = null;
      editing = false;
    }
  });

  const header = $derived(rows[0] ?? []);
  const italicColIndex = $derived(italicColumn ? header.indexOf(italicColumn) : -1);
  const cols = $derived(header.length);
  const isSel = (r, c) => sel && sel.r === r && sel.c === c;

  // ---- virtualization: render only the body rows in (or near) the viewport --------------
  const bodyCount = $derived(Math.max(0, rows.length - 1));
  const vStart = $derived(Math.max(0, Math.floor(scrollTop / rowH) - OVERSCAN));
  const vEnd = $derived(
    Math.min(bodyCount, vStart + Math.ceil(viewportH / rowH) + OVERSCAN * 2),
  );
  const topPad = $derived(vStart * rowH);
  const botPad = $derived(Math.max(0, (bodyCount - vEnd) * rowH));
  // Visible body rows carrying their absolute index (1-based into `rows`).
  const visibleRows = $derived(
    rows.slice(vStart + 1, vEnd + 1).map((row, i) => ({ r: vStart + 1 + i, row })),
  );

  function onScroll() {
    if (!wrapEl) return;
    scrollTop = wrapEl.scrollTop;
    scrollLeft = wrapEl.scrollLeft;
    viewportH = wrapEl.clientHeight;
    viewportW = wrapEl.clientWidth;
  }
  // Measure a real row height once the table is on screen, and re-measure on content change.
  $effect(() => {
    rows.length; // re-run when the lexicon changes
    if (!wrapEl) return;
    viewportH = wrapEl.clientHeight;
    viewportW = wrapEl.clientWidth;
    const tr = wrapEl.querySelector("tbody tr:not(.vpad)");
    if (tr?.offsetHeight) rowH = tr.offsetHeight;
  });
  // ---- stable column widths ------------------------------------------------------------
  // Virtualization renders a shifting subset of rows, so `table-layout: auto` would re-fit
  // every column to whatever happens to be on screen — widths jitter as you scroll. Instead
  // we measure each column's widest cell across the WHOLE table once (cheap: canvas text
  // metrics, no DOM render) and pin it with a <colgroup> + table-layout: fixed.
  const CTRL_W = 26; // the ⋮ handle column (editable only)
  const CELL_PAD = 16; // 7px l/r padding + 1px l/r border + a hair of slack
  const HANDLE_W = 26; // editable header padding-right: room for the ⋮ handle + edge resize grip
  const MAX_COL_W = 320; // cap a column's measured width; over-long cells ellipsize (drag to widen)
  const WIDE_MAX_COL_W = 460; // a roomier cap for wideColumns (content-heavy columns)
  const WIDE_MIN_COL_W = 220; // and a comfortable minimum default for them
  const MIN_COL_W = 44; // floor when dragging a column narrower
  // Fonts mirror the CSS below: headers are the sans face at --fs-body; the first (key) column
  // is the IPA face at --fs-content, semibold; every other body column is the IPA face at
  // --fs-body. Keep the px sizes in sync with --fs-body (14) / --fs-content (16) — canvas can't
  // read CSS variables.
  const KEY_FONT = "600 16px 'Charis SIL', serif";
  const BODY_FONT = "14px 'Charis SIL', serif";
  const HEAD_FONT = "600 14px system-ui, 'Segoe UI', Roboto, sans-serif";
  let fontsReady = $state(false);
  $effect(() => {
    if (typeof document !== "undefined" && document.fonts) {
      document.fonts.ready.then(() => (fontsReady = true)); // re-measure once webfonts land
    }
  });
  let _canvas = null;
  function textWidth(text, font) {
    if (typeof document === "undefined") return String(text).length * 9;
    _canvas ??= document.createElement("canvas");
    const ctx = _canvas.getContext("2d");
    ctx.font = font;
    return ctx.measureText(String(text)).width;
  }
  // Each column's natural width, measured across the whole table and clamped to MAX_COL_W so a
  // long cell (a descriptive rule name, a many-word `matched` list) can't stretch it off-screen.
  const measuredWidths = $derived.by(() => {
    void fontsReady; // recompute after the IPA/webfonts finish loading
    const widths = [];
    for (let c = 0; c < cols; c++) {
      const bodyFont = c === 0 ? KEY_FONT : BODY_FONT;
      // The IPA face renders combining marks (tie-bars t͡s, stacked diacritics) that canvas
      // metrics under-count; extra slack keeps fixed layout from clipping them off.
      const slack = 12;
      const headW = textWidth(header[c] ?? "", HEAD_FONT) + (editable ? HANDLE_W : 0);
      let bodyW = 0;
      for (let r = 1; r < rows.length; r++) {
        const v = rows[r][c];
        if (v) bodyW = Math.max(bodyW, textWidth(v, bodyFont));
      }
      const wide = wideColumns.includes(header[c]);
      const cap = wide ? WIDE_MAX_COL_W : MAX_COL_W;
      const floor = wide ? WIDE_MIN_COL_W : 0;
      const natural = Math.ceil(Math.max(headW, bodyW)) + CELL_PAD + slack;
      widths.push(Math.max(floor, Math.min(cap, natural)));
    }
    return widths;
  });
  // A user's drag-resize (colOverrides) wins over the measured cap; content change resets them.
  const colWidths = $derived(measuredWidths.map((w, c) => colOverrides[c] ?? w));

  // Drag a header cell's right-edge grip to resize that column (read-only tables — editable ones
  // use the ⋮ handle to reorder instead). The drag sets an override that beats the measured cap.
  function startColResize(event, c) {
    event.preventDefault();
    event.stopPropagation();
    const startX = event.clientX;
    const startW = colWidths[c];
    const onMove = (e) => {
      const w = Math.max(MIN_COL_W, Math.round(startW + e.clientX - startX));
      colOverrides = { ...colOverrides, [c]: w };
    };
    const onUp = () => {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
    };
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  }
  // The exact table width = sum of the column widths. A fixed-layout table with width:auto
  // instead FILLS its container and hands the leftover space to a column, so that column's
  // width shifts whenever the available width does (e.g. a scrollbar appearing) — the width
  // "fluctuation on scroll". Pinning the table to the column sum leaves no slack to distribute.
  const tableWidth = $derived(
    (editable ? CTRL_W : 0) + colWidths.reduce((sum, w) => sum + w, 0),
  );

  // ---- column virtualization (read-only wide tables) -----------------------------------
  // The result-pane derivation table can carry hundreds of rule columns; rendering every
  // <td> for each visible row is what makes it lag. Mirroring the row window above, we render
  // only the columns near the horizontal viewport, with left/right spacer cells holding the
  // off-screen width. Only for read-only tables — editable inventory tables are column-bounded
  // (a handful of columns), so they keep every column and column drag-reorder/selection, which
  // index by the true column number, stay exact.
  // Cumulative left edge of each data column: colX[c]..colX[c+1] is column c; colX[cols] is
  // the full data width (the editable ⋮ ctrl column is never virtualized, so it is excluded).
  const colX = $derived.by(() => {
    const xs = [0];
    for (let c = 0; c < cols; c++) xs.push(xs[c] + (colWidths[c] ?? 0));
    return xs;
  });
  const colWindow = $derived.by(() => {
    if (editable || cols <= 1) return { start: 1, end: cols, leftPad: 0, rightPad: 0 };
    const x = colX;
    const left = scrollLeft;
    const right = scrollLeft + viewportW;
    let start = 1;
    while (start < cols && x[start + 1] <= left) start++; // first col reaching past the left edge
    start = Math.max(1, start - COL_OVERSCAN);
    let end = start;
    while (end < cols && x[end] < right) end++; // one past the last col starting before the right edge
    end = Math.min(cols, end + COL_OVERSCAN);
    return { start, end, leftPad: x[start] - x[1], rightPad: x[cols] - x[end] };
  });
  // The per-row column layout: the sticky column 0, an optional left spacer, the visible data
  // columns, an optional right spacer. Editable tables get every column and no spacers.
  const rowCols = $derived.by(() => {
    const w = colWindow;
    const items = [{ kind: "cell", c: 0 }];
    if (w.leftPad > 0) items.push({ kind: "pad", id: "L", w: w.leftPad });
    for (let c = w.start; c < w.end; c++) items.push({ kind: "cell", c });
    if (w.rightPad > 0) items.push({ kind: "pad", id: "R", w: w.rightPad });
    return items;
  });
  const colspan = $derived(rowCols.length + (editable ? 1 : 0));

  // Scroll a body row into view (so keyboard navigation off-screen still renders + focuses).
  function ensureVisible(r) {
    if (!wrapEl || r < 1) return;
    const top = (r - 1) * rowH;
    let st = wrapEl.scrollTop;
    if (top < st + rowH) st = Math.max(0, top - rowH);
    else if (top + rowH > st + wrapEl.clientHeight - rowH)
      st = top - wrapEl.clientHeight + rowH * 3;
    st = Math.max(0, st);
    wrapEl.scrollTop = st;
    scrollTop = st;
  }

  function commit() {
    const csv = toCsv(rows);
    lastEmitted = csv;
    onchange(csv);
  }

  // ---- selection + editing -------------------------------------------------------------
  function select(r, c) {
    if (!editable) return;
    sel = { r, c };
    editing = false;
  }
  function startEdit(r, c) {
    if (!editable) return;
    sel = { r, c };
    editOrig = rows[r][c] ?? "";
    editing = true;
  }
  function setCell(r, c, value) {
    rows[r][c] = value;
    commit();
  }
  function moveSel(dr, dc) {
    if (!sel) return;
    const r = Math.min(rows.length - 1, Math.max(0, sel.r + dr));
    const c = Math.min(cols - 1, Math.max(0, sel.c + dc));
    sel = { r, c };
    editing = false;
    ensureVisible(r); // bring it into the virtualized window before the focus effect runs
  }
  function cellKey(event, r, c) {
    if (editing) return; // while editing, keys belong to the <input> (caret nav, typing) — see inputKey
    const k = event.key;
    if (k === "ArrowUp") moveSel(-1, 0);
    else if (k === "ArrowDown") moveSel(1, 0);
    else if (k === "ArrowLeft") moveSel(0, -1);
    else if (k === "ArrowRight") moveSel(0, 1);
    else if (k === "Tab") moveSel(0, event.shiftKey ? -1 : 1);
    else if (k === "Enter" || k === "F2") startEdit(r, c); // edit is entered only here + double-click
    else if (k === "Backspace" || k === "Delete") setCell(r, c, "");
    else return;
    event.preventDefault();
  }
  function inputKey(event) {
    if (event.key === "Enter") {
      event.preventDefault();
      event.target.blur();
      moveSel(1, 0);
    } else if (event.key === "Tab") {
      event.preventDefault();
      const d = event.shiftKey ? -1 : 1;
      event.target.blur();
      moveSel(0, d);
    } else if (event.key === "Escape") {
      event.preventDefault();
      reverting = true;
      event.target.blur();
    }
  }
  function inputBlur(event, r, c) {
    if (reverting) {
      rows[r][c] = editOrig;
      reverting = false;
    } else {
      setCell(r, c, event.target.value);
    }
    editing = false;
  }
  function focusCell(node) {
    node.focus();
    const n = node.value.length; // caret at the end for in-place editing, never select-all
    node.setSelectionRange(n, n);
  }
  $effect(() => {
    if (!sel || editing || !tableEl) return;
    tableEl.querySelector(`[data-cell="${sel.r}-${sel.c}"]`)?.focus();
  });

  // ---- clipboard on the selected cell (not while editing) ------------------------------
  // Handled as native copy/cut/paste events (no clipboard permission prompt, unlike
  // navigator.clipboard). Only when this table's selected cell holds focus, so a copy meant
  // for the read-only tables, the text editor, or another table is never hijacked.
  const cellHasFocus = () =>
    editable && sel && !editing && !!tableEl && tableEl.contains(document.activeElement);
  function onCopy(event) {
    if (!cellHasFocus()) return;
    event.preventDefault();
    event.clipboardData.setData("text/plain", rows[sel.r][sel.c] ?? "");
  }
  function onCut(event) {
    if (!cellHasFocus()) return;
    event.preventDefault();
    event.clipboardData.setData("text/plain", rows[sel.r][sel.c] ?? "");
    setCell(sel.r, sel.c, ""); // commits the cleared cell
  }
  function onPaste(event) {
    if (!cellHasFocus()) return;
    event.preventDefault();
    const text = event.clipboardData.getData("text/plain").replace(/\r?\n$/, ""); // drop 1 trailing NL
    setCell(sel.r, sel.c, text); // commits the pasted value
  }

  // ---- row / column structure ----------------------------------------------------------
  function emptyRow() {
    return Array(cols || 1).fill("");
  }
  function addRow(index) {
    rows.splice(index, 0, emptyRow());
    commit();
  }
  function removeRow(index) {
    rows.splice(index, 1);
    sel = null;
    commit();
  }
  // Move the row at `from` so it lands at insertion position `index` (0..rows.length).
  function moveRow(from, index) {
    if (from < 1 || index < 1 || index === from || index === from + 1) return;
    const item = rows[from];
    const rest = rows.filter((_, i) => i !== from);
    rest.splice(index > from ? index - 1 : index, 0, item);
    rows = rest;
    commit();
  }
  function addCol(index) {
    for (const row of rows) row.splice(index, 0, "");
    commit();
  }
  function removeCol(index) {
    for (const row of rows) row.splice(index, 1);
    sel = null;
    commit();
  }
  function moveCol(from, index) {
    if (index === from || index === from + 1) return;
    const at = index > from ? index - 1 : index;
    for (const row of rows) {
      const [cell] = row.splice(from, 1);
      row.splice(at, 0, cell);
    }
    commit();
  }

  // ---- the ⋮ menu ----------------------------------------------------------------------
  function openMenu(kind, index, event) {
    event.stopPropagation();
    menu = { kind, index, x: event.clientX, y: event.clientY };
  }
  function closeMenu() {
    menu = null;
  }
  function act(fn, index) {
    fn(index);
    closeMenu();
  }

  // ---- drag reorder --------------------------------------------------------------------
  // Native DnD, but the drop *position* (an insertion index, before/after the cell under the
  // cursor) is what we track and show as a line — so it reads like Numbers, not a vague
  // "dropped on a row" guess.
  function startDrag(kind, from, event) {
    drag = { kind, from };
    event.dataTransfer.effectAllowed = "move";
    event.dataTransfer.setData("text/plain", `${kind}:${from}`);
  }
  function endDrag() {
    drag = null;
    dropIndex = null;
  }
  function overRow(event, r) {
    if (drag?.kind !== "row") return;
    event.preventDefault();
    const rect = event.currentTarget.getBoundingClientRect();
    const index = event.clientY > rect.top + rect.height / 2 ? r + 1 : r;
    if (dropIndex?.index !== index) dropIndex = { kind: "row", index };
  }
  function overCol(event, c) {
    if (drag?.kind !== "col") return;
    event.preventDefault();
    const rect = event.currentTarget.getBoundingClientRect();
    const index = event.clientX > rect.left + rect.width / 2 ? c + 1 : c;
    if (dropIndex?.index !== index) dropIndex = { kind: "col", index };
  }
  function dropRow(event) {
    if (drag?.kind !== "row" || !dropIndex) return;
    event.preventDefault();
    moveRow(drag.from, dropIndex.index);
    endDrag();
  }
  function dropCol(event) {
    if (drag?.kind !== "col" || !dropIndex) return;
    event.preventDefault();
    moveCol(drag.from, dropIndex.index);
    endDrag();
  }
  const insTop = (r) => dropIndex?.kind === "row" && dropIndex.index === r;
  const insBottom = (r) =>
    dropIndex?.kind === "row" && dropIndex.index === rows.length && r === rows.length - 1;
  const insLeft = (c) => dropIndex?.kind === "col" && dropIndex.index === c;
  const insRight = (c) => dropIndex?.kind === "col" && dropIndex.index === cols && c === cols - 1;
  const dragRow = (r) => drag?.kind === "row" && drag.from === r;
  const dragCol = (c) => drag?.kind === "col" && drag.from === c;
</script>

<svelte:window onclick={closeMenu} />

<div class="csv-wrap" bind:this={wrapEl} onscroll={onScroll}>
  {#if header.length}
    <table class="csv" class:editable bind:this={tableEl} style="width: {tableWidth}px">
      <colgroup>
        {#if editable}<col style="width: {CTRL_W}px" />{/if}
        {#each rowCols as it (it.kind === "pad" ? "pad-" + it.id : it.c)}
          {#if it.kind === "pad"}<col style="width: {it.w}px" />{:else}<col
              style="width: {colWidths[it.c]}px"
            />{/if}
        {/each}
      </colgroup>
      <thead>
        <tr>
          {#if editable}<th class="ctrl" aria-hidden="true"></th>{/if}
          {#each rowCols as it (it.kind === "pad" ? "pad-" + it.id : it.c)}
            {#if it.kind === "pad"}
              <th class="cpad" aria-hidden="true"></th>
            {:else}
              {@const c = it.c}
              <th
                class:sym-head={c === 0}
                class:selected={isSel(0, c)}
                class:ins-left={insLeft(c)}
                class:ins-right={insRight(c)}
                class:col-dragging={dragCol(c)}
                data-cell={`0-${c}`}
                tabindex={isSel(0, c) && !editing ? 0 : -1}
                ondragover={(e) => overCol(e, c)}
                ondrop={dropCol}
                onclick={(e) => {
                  if (!editable) return; // read-only: never steal the text selection
                  if (editing && isSel(0, c)) return; // editing here — let the input keep its caret
                  select(0, c);
                  e.currentTarget.focus();
                }}
                ondblclick={() => startEdit(0, c)}
                onkeydown={(e) => cellKey(e, 0, c)}
              >
                {#if editing && isSel(0, c)}
                  <input
                    use:focusCell
                    value={rows[0][c] ?? ""}
                    onblur={(e) => inputBlur(e, 0, c)}
                    onkeydown={inputKey}
                  />
                {:else}
                  <span class="label">{header[c]}</span>
                {/if}
                {#if editable}
                  <button
                    class="handle"
                    title="Column options — click for menu, drag to move"
                    aria-label="Column options"
                    draggable="true"
                    ondragstart={(e) => startDrag("col", c, e)}
                    ondragend={endDrag}
                    onclick={(e) => openMenu("col", c, e)}>⋮</button
                  >
                {/if}
                <span
                  class="col-resizer"
                  aria-hidden="true"
                  title="Drag to resize this column"
                  onpointerdown={(e) => startColResize(e, c)}
                ></span>
              </th>
            {/if}
          {/each}
        </tr>
      </thead>
      <tbody>
        {#if topPad > 0}
          <tr class="vpad" aria-hidden="true">
            <td colspan={colspan} style="height: {topPad}px"></td>
          </tr>
        {/if}
        {#each visibleRows as { r, row } (r)}
          <tr
            class:ins-top={insTop(r)}
            class:ins-bottom={insBottom(r)}
            class:row-dragging={dragRow(r)}
            class:sporadic-row={italicColIndex >= 0 && (row[italicColIndex] ?? "") !== ""}
            ondragover={(e) => overRow(e, r)}
            ondrop={dropRow}
          >
            {#if editable}
              <td class="ctrl">
                <button
                  class="handle"
                  title="Row options — click for menu, drag to move"
                  aria-label="Row options"
                  draggable="true"
                  ondragstart={(e) => startDrag("row", r, e)}
                  ondragend={endDrag}
                  onclick={(e) => openMenu("row", r, e)}>⋮</button
                >
              </td>
            {/if}
            {#each rowCols as it (it.kind === "pad" ? "pad-" + it.id : it.c)}
              {#if it.kind === "pad"}
                <td class="cpad" aria-hidden="true"></td>
              {:else}
                {@const c = it.c}
                <td
                  class:sym={c === 0}
                  class:selected={isSel(r, c)}
                  class:ins-left={insLeft(c)}
                  class:ins-right={insRight(c)}
                  class:col-dragging={dragCol(c)}
                  title={!editable ? (row[c] ?? "") : null}
                  data-cell={`${r}-${c}`}
                  tabindex={isSel(r, c) && !editing ? 0 : -1}
                  ondragover={(e) => overCol(e, c)}
                  ondrop={dropCol}
                  onclick={(e) => {
                    if (!editable) return; // read-only: never steal the text selection or focus-scroll
                    if (editing && isSel(r, c)) return; // editing here — let the input keep its caret
                    select(r, c);
                    e.currentTarget.focus(); // keystrokes reach cellKey even if the focus effect lags
                  }}
                  ondblclick={() => startEdit(r, c)}
                  onkeydown={(e) => cellKey(e, r, c)}
                >
                  {#if editing && isSel(r, c)}
                    <input
                      use:focusCell
                      value={row[c] ?? ""}
                      onblur={(e) => inputBlur(e, r, c)}
                      onkeydown={inputKey}
                    />
                  {:else}{row[c] ?? ""}{/if}
                </td>
              {/if}
            {/each}
          </tr>
        {/each}
        {#if botPad > 0}
          <tr class="vpad" aria-hidden="true">
            <td colspan={colspan} style="height: {botPad}px"></td>
          </tr>
        {/if}
      </tbody>
    </table>
    {#if editable}
      <button class="add-row" onclick={() => addRow(rows.length)}>+ Add row</button>
    {/if}
  {:else}
    <p class="empty">Empty file.</p>
  {/if}
</div>

{#if menu}
  <!-- Fixed so it escapes the table's overflow clipping; closed by the window click above. -->
  <div class="ctx-menu" style="left: {menu.x}px; top: {menu.y}px" role="menu">
    {#if menu.kind === "row"}
      <button role="menuitem" onclick={() => act(addRow, menu.index)}>Add row above</button>
      <button role="menuitem" onclick={() => act(addRow, menu.index + 1)}>Add row below</button>
      <button role="menuitem" class="danger" onclick={() => act(removeRow, menu.index)}
        >Remove row</button
      >
    {:else}
      <button role="menuitem" onclick={() => act(addCol, menu.index)}>Add column left</button>
      <button role="menuitem" onclick={() => act(addCol, menu.index + 1)}>Add column right</button>
      <button role="menuitem" class="danger" onclick={() => act(removeCol, menu.index)}
        >Remove column</button
      >
    {/if}
  </div>
{/if}

<style>
  .csv-wrap {
    flex: 1;
    overflow: auto;
    margin: 0 16px 16px;
  }
  /* The grid matches the .report-summary analysis tables: the IPA/body face, roomier cells,
     and a muted, panel-backed header — over the grid's fixed layout, column resizing, and
     row virtualization. */
  table.csv {
    border-collapse: collapse;
    font-family: var(--ipa);
    font-size: var(--fs-body);
    font-variant-numeric: tabular-nums;
    /* Fixed layout + measured <colgroup> widths: columns stay put as virtualization swaps
       the rendered rows (auto layout would re-fit them to the visible subset and jitter). */
    table-layout: fixed;
  }
  .csv td,
  .csv th {
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .csv th,
  .csv td {
    border: 1px solid var(--border);
    padding: 4px 9px;
    text-align: left;
    white-space: nowrap;
    position: relative;
  }
  /* Sporadic (word-scoped) rules are italicized across the whole row. */
  .csv tr.sporadic-row td {
    font-style: italic;
  }
  /* Read-only column resize: an invisible grip over each header cell's right edge. */
  .col-resizer {
    position: absolute;
    top: 0;
    right: 0;
    width: 7px;
    height: 100%;
    cursor: col-resize;
    user-select: none;
    touch-action: none;
  }
  .col-resizer:hover {
    background: var(--accent-border);
  }
  table.editable th,
  table.editable td {
    cursor: cell;
  }
  table.editable th {
    padding-right: 26px; /* room for the ⋮ handle plus the edge resize grip */
  }
  table.editable td.ctrl,
  table.editable th.ctrl {
    cursor: default;
  }
  /* Selection ring drawn inward, input filling the cell exactly — no size change on select. */
  .csv td:focus,
  .csv th:focus {
    outline: none;
  }
  .csv td.selected,
  .csv th.selected {
    box-shadow: inset 0 0 0 2px var(--accent, #4a90d9);
  }
  .csv input {
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    border: none;
    outline: none;
    font: inherit;
    line-height: inherit;
    text-align: left;
    background: transparent;
    color: var(--text-h);
  }
  /* The ⋮ drag/menu handle. */
  .handle {
    border: none;
    background: none;
    color: var(--muted);
    cursor: grab;
    font-size: 15px;
    line-height: 1;
    padding: 0 3px;
    border-radius: 4px;
    user-select: none;
  }
  th .handle {
    position: absolute;
    right: 10px; /* left of the edge resize grip (.col-resizer sits at right: 0) */
    top: 50%;
    transform: translateY(-50%);
  }
  .handle:hover {
    color: var(--text-h);
    background: var(--border);
  }
  .handle:active {
    cursor: grabbing;
  }
  /* Drag reorder: a thick accent line at the exact insertion boundary, and the moving
     row/column dimmed — the "where will it land" cue, Numbers-style. */
  .csv tr.ins-top td {
    box-shadow: inset 0 3px 0 var(--accent, #4a90d9);
  }
  .csv tr.ins-bottom td {
    box-shadow: inset 0 -3px 0 var(--accent, #4a90d9);
  }
  .csv th.ins-left,
  .csv td.ins-left {
    box-shadow: inset 3px 0 0 var(--accent, #4a90d9);
  }
  .csv th.ins-right,
  .csv td.ins-right {
    box-shadow: inset -3px 0 0 var(--accent, #4a90d9);
  }
  .csv tr.row-dragging td,
  .csv th.col-dragging,
  .csv td.col-dragging {
    opacity: 0.4;
  }
  /* Sticky header row and sticky first (symbol) column. */
  .csv thead th {
    position: sticky;
    top: 0;
    z-index: 2;
    background: var(--panel);
    color: var(--muted);
    font-weight: 600;
    font-family: var(--sans);
  }
  .csv td.sym,
  .csv th.sym-head {
    position: sticky;
    left: 0;
    z-index: 1;
    background: var(--panel);
  }
  /* Top-left corner: the "word" header pins both directions, so it must sit above
     the sticky header row (z2) and the sticky first column (z1). */
  .csv thead th.sym-head {
    z-index: 3;
  }
  .csv td.sym {
    font-family: var(--ipa);
    font-size: var(--fs-content);
    font-weight: 600;
    color: var(--text-h);
  }
  .csv td.ctrl,
  .csv th.ctrl {
    width: 1%;
    padding: 0 2px;
  }
  /* Virtualization spacers: hold the scroll height for off-screen rows (vpad) and the
     scroll width for off-screen columns (cpad). Inert — no border, padding, or interaction. */
  .csv tr.vpad td,
  .csv th.cpad,
  .csv td.cpad {
    padding: 0;
    border: 0;
  }
  .add-row {
    margin: 8px 12px 12px;
    padding: 5px 12px;
    border: 1px dashed var(--border);
    border-radius: 6px;
    background: none;
    color: var(--text-h);
    cursor: pointer;
    font-family: var(--sans);
    font-size: 14px;
  }
  .add-row:hover {
    background: var(--border);
  }
  .ctx-menu {
    position: fixed;
    z-index: 50;
    display: flex;
    flex-direction: column;
    min-width: 150px;
    padding: 4px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.28);
    font-family: var(--sans);
    font-size: 14px;
  }
  .ctx-menu button {
    text-align: left;
    padding: 6px 10px;
    border: none;
    border-radius: 5px;
    background: none;
    color: var(--text-h);
    cursor: pointer;
  }
  .ctx-menu button:hover {
    background: var(--border);
  }
  .ctx-menu button.danger:hover {
    background: #d9534f;
    color: #fff;
  }
  .empty {
    color: var(--muted);
    padding: 14px;
  }
</style>
