<script>
  // Read-only table view of a CSV (RFC4180 quoting: quoted fields may contain
  // commas, newlines, and doubled `""` for a literal quote).
  let { content = "" } = $props();

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

  const rows = $derived(content.trim() ? parseCsv(content.trim()) : []);
  const header = $derived(rows[0] ?? []);
  const body = $derived(rows.slice(1));
</script>

<div class="csv-wrap">
  {#if header.length}
    <table class="csv">
      <thead>
        <tr>
          {#each header as h}<th>{h}</th>{/each}
        </tr>
      </thead>
      <tbody>
        {#each body as row}
          <tr>
            {#each header as _, i}
              <td class:sym={i === 0}>{row[i] ?? ""}</td>
            {/each}
          </tr>
        {/each}
      </tbody>
    </table>
  {:else}
    <p class="empty">Empty file.</p>
  {/if}
</div>

<style>
  .csv-wrap {
    flex: 1;
    overflow: auto;
    margin: 0 16px 16px;
    border: 1px solid var(--border);
    border-radius: 6px;
    background: var(--code-bg);
  }
  table.csv {
    border-collapse: collapse;
    font-family: var(--mono);
    font-size: 16px;
  }
  .csv th,
  .csv td {
    border: 1px solid var(--border);
    padding: 2px 7px;
    text-align: center;
    white-space: nowrap;
  }
  /* Sticky header row and sticky first (symbol) column. */
  .csv thead th {
    position: sticky;
    top: 0;
    z-index: 2;
    background: var(--panel);
    color: var(--text-h);
    font-weight: 600;
    font-family: var(--sans);
  }
  .csv td.sym,
  .csv th:first-child {
    position: sticky;
    left: 0;
    z-index: 1;
    background: var(--panel);
  }
  .csv thead th:first-child {
    z-index: 3;
  }
  .csv td.sym {
    font-family: var(--ipa);
    font-size: 16px;
    font-weight: 600;
    color: var(--text-h);
  }
  .empty {
    color: var(--muted);
    padding: 14px;
  }
</style>
