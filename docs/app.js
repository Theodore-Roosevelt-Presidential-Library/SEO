/* TRPL Search & AI Visibility dashboard. Reads JSON from ./data and renders tabs. */
(() => {
  "use strict";

  const FILES = {
    status: "data/status.json", meta: "data/meta.json",
    gscSummary: "data/gsc/summary.json", daily: "data/gsc/daily.json", queries: "data/gsc/queries.json",
    pages: "data/gsc/pages.json", devices: "data/gsc/devices.json",
    opp: "data/opportunities.json",
    ranks: "data/ranks/latest.json", rankHist: "data/ranks/history.json",
    ai: "data/ai/latest.json", aiHist: "data/ai/history.json",
    audit: "data/audit/summary.json", auditPages: "data/audit/pages.json", auditHist: "data/audit/history.json",
    tips: "data/tips.json", tracking: "data/tracking.json",
    ux: "data/ux/latest.json", uxHist: "data/ux/history.json", checkout: "data/checkout/latest.json", links: "data/links.json",
  };
  const D = {};
  const charts = [];

  // ---------- helpers ----------
  function el(tag, attrs, ...kids) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v == null || v === false) continue;
      if (k === "class") n.className = v;
      else if (k.startsWith("on")) n.addEventListener(k.slice(2), v);
      else n.setAttribute(k, v === true ? "" : v);
    }
    for (const k of kids.flat()) if (k != null && k !== false) n.append(k.nodeType ? k : String(k));
    return n;
  }
  const nf = new Intl.NumberFormat("en-US");
  const num = (v) => (v == null ? "–" : nf.format(Math.round(v)));
  const pct = (v, d = 1) => (v == null ? "–" : (v * 100).toFixed(d) + "%");
  const pos = (v) => (v == null ? "–" : Number(v).toFixed(1));
  const shortUrl = (u) => (u || "").replace(/^https?:\/\/(www\.)?trlibrary\.com/, "") || "/";
  const link = (u, text) => el("a", { href: u, target: "_blank", rel: "noopener" }, text || shortUrl(u));
  const date = (iso) => (iso ? new Date(iso).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" }) : "–");
  const cssVar = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();

  function delta(cur, prev, { invert = false, asPct = true } = {}) {
    if (cur == null || prev == null || prev === 0) return el("span", { class: "muted" }, "no prior data");
    const ch = asPct ? (cur - prev) / prev : cur - prev;
    const good = invert ? ch < 0 : ch > 0;
    const txt = asPct ? `${ch > 0 ? "+" : ""}${(ch * 100).toFixed(1)}%` : `${ch > 0 ? "+" : ""}${ch.toFixed(1)}`;
    return el("span", { class: `delta ${Math.abs(ch) < 1e-9 ? "" : good ? "up" : "down"}` }, `${txt} vs prior 28 days`);
  }

  function kpi(label, value, sub) {
    return el("div", { class: "card kpi" }, el("div", { class: "label" }, label), el("div", { class: "value" }, value), el("div", { class: "sub" }, sub || ""));
  }

  function empty(msg, hint) {
    return el("div", { class: "empty" }, el("p", {}, msg), hint ? el("p", { class: "small" }, hint) : null);
  }

  function lineChart(series, labels, { yReverse = false, pctAxis = false } = {}) {
    const box = el("div", { class: "chart-box" });
    const canvas = el("canvas", { role: "img", "aria-label": series.map((s) => s.label).join(", ") + " over time" });
    box.append(canvas);
    requestAnimationFrame(() => {
      if (!window.Chart) return;
      const colors = ["--chart-1", "--chart-2", "--chart-3", "--chart-4", "--chart-5"].map(cssVar);
      const ink2 = cssVar("--ink-2"), line = cssVar("--line");
      charts.push(new Chart(canvas, {
        type: "line",
        data: {
          labels,
          datasets: series.map((s, i) => ({
            label: s.label, data: s.data, yAxisID: s.axis || "y", borderColor: colors[i % 5], backgroundColor: colors[i % 5],
            borderWidth: 2, pointRadius: labels.length > 40 ? 0 : 3, tension: 0.25, spanGaps: true,
          })),
        },
        options: {
          maintainAspectRatio: false, animation: { duration: 300 }, interaction: { mode: "index", intersect: false },
          plugins: { legend: { labels: { color: ink2, boxWidth: 12 } } },
          scales: {
            x: { ticks: { color: ink2, maxTicksLimit: 8 }, grid: { color: line } },
            y: { reverse: yReverse, ticks: { color: ink2, callback: pctAxis ? (v) => Math.round(v * 100) + "%" : undefined }, grid: { color: line }, min: pctAxis ? 0 : undefined, max: pctAxis ? 1 : undefined },
            ...(series.some((s) => s.axis === "y2") ? { y2: { position: "right", ticks: { color: ink2 }, grid: { display: false } } } : {}),
          },
        },
      }));
    });
    return box;
  }

  // Sortable, searchable table
  function table(columns, rows, { search = true, limit = 50, sort, filters } = {}) {
    let q = "", shown = limit, sortKey = sort ? sort[0] : null, sortDir = sort ? sort[1] : -1;
    const extra = {};
    const wrap = el("div");
    const tbody = el("tbody");
    const more = el("button", { onclick: () => { shown += limit * 2; draw(); } }, "Show more");
    const count = el("span", { class: "muted small" });
    const tools = el("div", { class: "table-tools" });
    if (search) tools.append(el("input", { type: "search", placeholder: "Filter…", "aria-label": "Filter rows", oninput: (e) => { q = e.target.value.toLowerCase(); shown = limit; draw(); } }));
    for (const f of filters || []) {
      const s = el("select", { "aria-label": f.label, onchange: (e) => { extra[f.key] = e.target.value; shown = limit; draw(); } },
        el("option", { value: "" }, `All ${f.label}`), ...f.options.map((o) => el("option", { value: o }, o)));
      tools.append(s);
    }
    tools.append(count);
    const ths = columns.map((c) => {
      const th = el("th", { class: c.num ? "num" : "", scope: "col", tabindex: 0 }, c.label);
      const go = () => { if (sortKey === c.key) sortDir *= -1; else { sortKey = c.key; sortDir = c.num ? -1 : 1; } draw(); };
      th.addEventListener("click", go); th.addEventListener("keydown", (e) => e.key === "Enter" && go());
      return th;
    });
    function draw() {
      let r = rows.filter((row) => (!q || JSON.stringify(row).toLowerCase().includes(q)) &&
        Object.entries(extra).every(([k, v]) => !v || (Array.isArray(row[k]) ? row[k].includes(v) : String(row[k]) === v)));
      if (sortKey) {
        const col = columns.find((c) => c.key === sortKey);
        const val = col && col.sortVal ? col.sortVal : (x) => x[sortKey];
        r = [...r].sort((a, b) => { const A = val(a), B = val(b); if (A == null) return 1; if (B == null) return -1; return (A > B ? 1 : A < B ? -1 : 0) * sortDir; });
      }
      ths.forEach((th, i) => th.setAttribute("aria-sort", columns[i].key === sortKey ? (sortDir > 0 ? "ascending" : "descending") : "none"));
      tbody.replaceChildren(...r.slice(0, shown).map((row) => el("tr", {}, ...columns.map((c) => {
        const v = c.render ? c.render(row) : c.fmt ? c.fmt(row[c.key]) : row[c.key];
        return el("td", { class: (c.num ? "num " : "") + (c.cls || "") }, v ?? "–");
      }))));
      count.textContent = `${num(r.length)} rows`;
      more.hidden = r.length <= shown;
    }
    wrap.append(tools, el("div", { class: "table-wrap" }, el("table", {}, el("thead", {}, el("tr", {}, ...ths)), tbody)), more);
    draw();
    return wrap;
  }

  // What the system added/retired on its own (seo/curate.py)
  function trackingLog() {
    const t = D.tracking;
    if (!t || !(t.log || []).length) return [];
    const active = (t.keywords || []).filter((k) => k.status === "active").length;
    const activeQ = (t.prompts || []).filter((p) => p.status === "active").length;
    return [
      el("h2", {}, "What the system changed"),
      el("p", { class: "lead" }, `Each week the system adds promising searches and AI questions from Search Console, and retires ones that have been won or have faded. It's tracking ${active} discovered keywords and ${activeQ} discovered questions now, within the caps in config/tracking.yml. To keep one for good, copy it into keywords.yml or ai_prompts.yml. To block one, add it to the exclude list.`),
      el("div", { class: "card" }, table([
        { key: "date", label: "Date" },
        { key: "action", label: "Change", render: (e) => el("span", { class: `pill ${e.action === "added" ? "ok" : e.action === "graduated" ? "" : "skipped"}` }, e.action) },
        { key: "kind", label: "Type" }, { key: "item", label: "Keyword / question" }, { key: "reason", label: "Why" },
      ], t.log, { limit: 20, sort: ["date", -1] })),
    ];
  }

  // ---------- views ----------
  const VIEWS = {
    overview() {
      const out = [];
      const s = D.gscSummary;
      if (s) {
        const c = s.current_totals, p = s.previous_totals;
        out.push(el("p", { class: "lead" }, `Google Search, ${date(s.period.start)} – ${date(s.period.end)}.`));
        out.push(el("div", { class: "grid kpis" },
          kpi("Clicks from Google", num(c.clicks), delta(c.clicks, p.clicks)),
          kpi("Impressions", num(c.impressions), delta(c.impressions, p.impressions)),
          kpi("Click-through rate", pct(c.ctr), delta(c.ctr, p.ctr)),
          kpi("Average position", pos(c.position), delta(c.position, p.position, { invert: true, asPct: false })),
          kpi("Non-branded clicks", num(s.nonbranded_clicks), `${pct(s.nonbranded_clicks / Math.max(1, s.nonbranded_clicks + s.branded_clicks), 0)} of clicks with a known search: people who didn't search our name${s.unattributed_clicks ? `. Google hides the search for another ${num(s.unattributed_clicks)}.` : ""}`),
        ));
      } else {
        out.push(empty("Search Console isn't connected yet.", "See the Setup tab."));
      }
      const row2 = el("div", { class: "grid kpis", style: "margin-top:1rem" });
      if (D.audit) row2.append(kpi("Site health", `${D.audit.score}/100`, `${num(D.audit.crawled)} pages crawled ${date(D.audit.updated)}`), kpi("AI readiness", `${D.audit.ai_score}/100`, "Structure signals AI tools rely on"));
      if (D.ai && D.ai.results) {
        const ok = D.ai.results.filter((r) => !r.error);
        row2.append(kpi("Mentioned in AI answers", pct(ok.filter((r) => r.mentioned).length / Math.max(1, ok.length), 0), `${ok.length} answers across ${Object.keys(D.ai.providers).length} assistants`),
          kpi("AI answers citing trlibrary.com", pct(ok.filter((r) => r.cited_us).length / Math.max(1, ok.length), 0), "Linked as a source"));
      }
      if (row2.children.length) out.push(row2);

      if (D.daily && D.daily.length) {
        const last = D.daily.slice(-90);
        out.push(el("h2", {}, "Last 90 days"));
        out.push(el("div", { class: "card" }, lineChart([
          { label: "Clicks", data: last.map((r) => r.clicks) },
          { label: "Impressions", data: last.map((r) => r.impressions), axis: "y2" },
        ], last.map((r) => r.date.slice(5)))));
      }
      if (D.opp) {
        const top = (D.opp.striking_distance || []).slice(0, 6);
        if (top.length) {
          out.push(el("h2", {}, "Biggest quick wins"));
          out.push(el("p", { class: "lead" }, "Searches where trlibrary.com already ranks on page one or two. Moving these into the top three is the fastest route to more visitors."));
          out.push(el("div", { class: "card" }, table([
            { key: "query", label: "Search" }, { key: "page", label: "Our page", render: (r) => link(r.page), cls: "url" },
            { key: "position", label: "Position", num: true, fmt: pos }, { key: "impressions", label: "Impressions", num: true, fmt: num },
            { key: "est_extra_clicks", label: "Extra clicks / 28d (est.)", num: true, fmt: num },
          ], top, { search: false, limit: 6 })));
        }
      }
      if (D.tips && D.tips.ai_brief && D.tips.ai_brief.headline) {
        out.push(el("h2", {}, "AI visibility this week"), el("div", { class: "card" }, el("p", {}, D.tips.ai_brief.headline), el("a", { href: "#tips" }, "Read the recommendations →")));
      }
      return out;
    },

    search() {
      if (!D.queries) return [empty("Search Console isn't connected yet.", "See the Setup tab.")];
      let mode = "queries";
      const holder = el("div");
      const btnQ = el("button", { class: "on", onclick: () => set("queries") }, "Searches");
      const btnP = el("button", { onclick: () => set("pages") }, "Pages");
      function set(m) {
        mode = m; btnQ.className = m === "queries" ? "on" : ""; btnP.className = m === "pages" ? "on" : "";
        holder.replaceChildren(m === "queries" ? table([
          { key: "query", label: "Search" },
          { key: "branded", label: "Type", render: (r) => el("span", { class: "pill" }, r.branded ? "Branded" : "Discovery"), sortVal: (r) => r.branded },
          { key: "clicks", label: "Clicks", num: true, fmt: num }, { key: "prev_clicks", label: "Prior", num: true, fmt: num },
          { key: "impressions", label: "Impressions", num: true, fmt: num }, { key: "ctr", label: "CTR", num: true, fmt: (v) => pct(v) },
          { key: "position", label: "Position", num: true, fmt: pos },
        ], D.queries, { sort: ["clicks", -1] }) : table([
          { key: "page", label: "Page", render: (r) => link(r.page), cls: "url", sortVal: (r) => r.page },
          { key: "clicks", label: "Clicks", num: true, fmt: num }, { key: "prev_clicks", label: "Prior", num: true, fmt: num },
          { key: "impressions", label: "Impressions", num: true, fmt: num }, { key: "ctr", label: "CTR", num: true, fmt: (v) => pct(v) },
          { key: "position", label: "Position", num: true, fmt: pos },
        ], D.pages || [], { sort: ["clicks", -1] }));
      }
      set(mode);
      const s = D.gscSummary;
      return [
        el("p", { class: "lead" }, `Last 28 days${s ? ` (${date(s.period.start)} – ${date(s.period.end)})` : ""}. Google hides very rare searches for privacy, so these won't add up to the totals.`),
        el("div", { class: "table-tools" }, btnQ, btnP), el("div", { class: "card" }, holder),
      ];
    },

    opportunities() {
      const o = D.opp;
      if (!o) return [empty("No opportunities yet.", "These appear once Search Console data is flowing.")];
      const sec = (title, lead, node) => [el("h2", {}, title), el("p", { class: "lead" }, lead), el("div", { class: "card" }, node)];
      return [
        el("p", { class: "lead" }, o.note),
        ...sec("Striking distance", "Ranking 4–20 with real demand. Strengthen the page for the exact search: use the words in the title and an H2, answer the question directly, and link to it from related pages.", table([
          { key: "query", label: "Search" }, { key: "page", label: "Page", render: (r) => link(r.page), cls: "url" },
          { key: "position", label: "Pos.", num: true, fmt: pos }, { key: "impressions", label: "Impr.", num: true, fmt: num },
          { key: "clicks", label: "Clicks", num: true, fmt: num }, { key: "est_extra_clicks", label: "Upside", num: true, fmt: num },
        ], o.striking_distance, { sort: ["est_extra_clicks", -1], limit: 25 })),
        ...sec("Ranking well, few clicks", "These pages sit high in results but people skip them. Usually a title or meta description problem.", table([
          { key: "page", label: "Page", render: (r) => link(r.page), cls: "url" }, { key: "position", label: "Pos.", num: true, fmt: pos },
          { key: "ctr", label: "CTR", num: true, fmt: (v) => pct(v) }, { key: "expected_ctr", label: "Typical", num: true, fmt: (v) => pct(v) },
          { key: "est_extra_clicks", label: "Upside", num: true, fmt: num },
        ], o.low_ctr, { sort: ["est_extra_clicks", -1], limit: 15 })),
        ...sec("Search words missing from the title", "Popular searches whose main words don't appear in the ranking page's title.", table([
          { key: "query", label: "Search" }, { key: "title", label: "Current title" },
          { key: "missing_words", label: "Missing", render: (r) => r.missing_words.join(", ") },
          { key: "impressions", label: "Impr.", num: true, fmt: num }, { key: "page", label: "Page", render: (r) => link(r.page), cls: "url" },
        ], o.missing_in_title, { sort: ["impressions", -1], limit: 15 })),
        ...sec("Losing clicks", "Down 30% or more vs the previous 28 days (seasonality is normal for a seasonal attraction, so compare with last year before acting).", table([
          { key: "kind", label: "Type" }, { key: "item", label: "Search / page", render: (r) => (r.kind === "page" ? link(r.item) : r.item), cls: "url" },
          { key: "clicks", label: "Clicks", num: true, fmt: num }, { key: "prev_clicks", label: "Prior", num: true, fmt: num },
          { key: "change", label: "Change", num: true, fmt: (v) => pct(v, 0) },
        ], o.declining, { sort: ["change", 1], limit: 15 })),
        ...sec("Pages competing with each other", "Two or more of our pages split the same search. Pick one page to own it and link the others to it.", table([
          { key: "query", label: "Search" }, { key: "impressions", label: "Impr.", num: true, fmt: num },
          { key: "pages", label: "Pages", render: (r) => el("ul", { class: "clean" }, ...r.pages.map((p) => el("li", {}, link(p.page), ` · pos ${pos(p.position)}`))) },
        ], o.cannibalization, { sort: ["impressions", -1], limit: 15 })),
      ];
    },

    rankings() {
      const r = D.ranks;
      if (!r) return [empty("No ranking data yet.", "Runs weekly. Edit config/keywords.yml to change the tracked searches.")];
      const live = r.source.includes("dataforseo");
      const groups = [...new Set(r.keywords.map((k) => k.group))];
      const cols = [
        { key: "keyword", label: "Search", render: (k) => (k.auto ? el("span", {}, k.keyword, " ", el("span", { class: "pill", title: "Added automatically. See 'What the system changed' below." }, "auto")) : k.keyword) },
        { key: "group", label: "Group" },
        { key: "volume", label: "Monthly searches", num: true, fmt: num },
        { key: "gsc", label: "Search Console pos.", num: true, render: (k) => pos(k.gsc && k.gsc.position), sortVal: (k) => k.gsc && k.gsc.position },
      ];
      if (live) cols.push(
        { key: "serp", label: "Google rank", num: true, render: (k) => (k.serp ? (k.serp.rank ?? ">" + 30) : "–"), sortVal: (k) => (k.serp && k.serp.rank) || 99 },
        { key: "aio", label: "AI Overview", render: (k) => (!k.serp ? "–" : !k.serp.ai_overview ? "None" : k.serp.ai_overview_cites_us ? el("span", { class: "pill ok" }, "Cites us") : el("span", { class: "pill high" }, "Not cited")), sortVal: (k) => (k.serp ? (k.serp.ai_overview ? (k.serp.ai_overview_cites_us ? 2 : 1) : 0) : -1) },
        { key: "above", label: "Ranking above us", render: (k) => (!k.serp ? "–" : k.serp.top.filter((t) => !k.serp.rank || t.rank < k.serp.rank).slice(0, 3).map((t) => t.domain).join(", ") || "—") },
      );
      const out = [
        el("p", { class: "lead" }, live ? `Live Google results (US, desktop) checked ${date(r.updated)}, alongside Search Console's 28-day average position.`
          : "Showing Search Console's 28-day average position. Add DataForSEO keys to see live Google results, AI Overviews and who ranks above us."),
        el("div", { class: "card" }, table(cols, r.keywords, { sort: ["volume", -1], limit: 100, filters: [{ key: "group", label: "groups", options: groups }] })),
      ];
      const h = D.rankHist || [];
      if (h.length > 1 && live) {
        const kws = r.keywords.filter((k) => k.serp && k.serp.rank).sort((a, b) => (b.volume || 0) - (a.volume || 0)).slice(0, 5).map((k) => k.keyword);
        out.push(el("h2", {}, "Rank over time"), el("div", { class: "card" }, lineChart(kws.map((k) => ({ label: k, data: h.map((x) => (x.serp || {})[k] ?? null) })), h.map((x) => x.date), { yReverse: true })));
      }
      out.push(...trackingLog());
      return out;
    },

    ai() {
      const a = D.ai;
      if (!a) return [empty("AI visibility tracking isn't running yet.", "Add at least one AI API key (see Setup). Questions live in config/ai_prompts.yml.")];
      const provs = Object.keys(a.providers);
      const out = [el("p", { class: "lead" }, `Each week the same travel and history questions go to ${provs.map((p) => a.providers[p].label).join(", ")} with web search on. Last run ${date(a.updated)}.`)];
      out.push(el("div", { class: "grid kpis" }, ...provs.map((p) => kpi(a.providers[p].label, pct(a.providers[p].mention_rate, 0), `mention us · ${pct(a.providers[p].cite_rate, 0)} cite trlibrary.com`))));

      const h = D.aiHist || [];
      if (h.length > 1) {
        out.push(el("h2", {}, "Mention rate over time"), el("div", { class: "card" }, lineChart(
          provs.map((p) => ({ label: a.providers[p].label, data: h.map((x) => (x.providers[p] || {}).mention_rate ?? null) })), h.map((x) => x.date), { pctAxis: true })));
      }

      out.push(el("h2", {}, "Question by question"));
      const detail = el("div", { class: "card", hidden: true });
      const groups = [...new Set(a.prompts.map((p) => p.group))];
      const tb = el("tbody");
      for (const g of groups) {
        tb.append(el("tr", {}, el("th", { colspan: provs.length + 1, scope: "colgroup" }, g)));
        for (const p of a.prompts.filter((x) => x.group === g)) {
          tb.append(el("tr", {}, el("td", {}, p.text, p.auto ? el("span", {}, " ", el("span", { class: "pill", title: "Added automatically from a Google search" }, "auto")) : null), ...provs.map((pv) => {
            const r = a.results.find((x) => x.prompt_id === p.id && x.provider === pv);
            if (!r) return el("td", { class: "cell" }, "–");
            const cls = r.error ? "err" : r.cited_us ? "cite" : r.mentioned ? "yes" : "no";
            const label = r.error ? "!" : r.mentioned ? (r.position || "✓") : "✕";
            return el("td", { class: "cell", tabindex: 0, title: "Show answer", onclick: () => show(p, r), onkeydown: (e) => e.key === "Enter" && show(p, r) }, el("span", { class: `dot ${cls}` }, label));
          })));
        }
      }
      function show(p, r) {
        detail.hidden = false;
        detail.replaceChildren(...[
          el("h3", {}, `${a.providers[r.provider].label}: “${p.text}”`),
          r.error ? el("p", { class: "warn-box" }, r.error) : null,
          el("p", {}, r.mentioned ? `Mentioned${r.position ? `, #${r.position} among tracked attractions` : ""}${r.cited_us ? ", and trlibrary.com is cited." : ", but trlibrary.com isn't cited."}` : "The Library isn't mentioned."),
          r.peers && r.peers.length ? el("p", { class: "small muted" }, "Also mentioned: " + r.peers.join(", ")) : null,
          r.citations && r.citations.length ? el("details", {}, el("summary", {}, `Sources cited (${r.citations.length})`), el("ul", { class: "clean small" }, ...r.citations.map((c) => el("li", {}, link(c, c))))) : null,
          el("details", { open: true }, el("summary", {}, "Full answer"), el("div", { class: "answer" }, r.text || "")),
        ].filter(Boolean));
        detail.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      out.push(el("div", { class: "legend" },
        el("span", {}, el("span", { class: "dot cite" }, "1"), " mentioned and cites trlibrary.com"),
        el("span", {}, el("span", { class: "dot yes" }, "2"), " mentioned (number = order among attractions)"),
        el("span", {}, el("span", { class: "dot no" }, "✕"), " not mentioned")));
      out.push(el("div", { class: "card table-wrap" }, el("table", { class: "matrix" },
        el("thead", {}, el("tr", {}, el("th", {}, "Question"), ...provs.map((p) => el("th", { class: "num" }, a.providers[p].label)))), tb)), detail);

      if (a.top_cited_domains && a.top_cited_domains.length) {
        const max = a.top_cited_domains[0][1];
        out.push(el("h2", {}, "Sources AI assistants lean on"), el("p", { class: "lead" }, "Being accurate and present on these sites is how the Library gets into more answers."),
          el("div", { class: "card" }, table([
            { key: "d", label: "Site" }, { key: "n", label: "Citations", num: true },
            { key: "bar", label: "", render: (r) => el("div", { class: "bar", style: "min-width:120px" }, el("span", { style: `width:${(100 * r.n) / max}%` })) },
          ], a.top_cited_domains.map(([d, n]) => ({ d, n })), { search: false, limit: 25, sort: ["n", -1] })));
      }
      out.push(...trackingLog());
      return out;
    },

    audit() {
      const s = D.audit;
      if (!s) return [empty("The site audit hasn't run yet.", "It runs weekly, or start it from the Actions tab on GitHub.")];
      const out = [el("p", { class: "lead" }, `Crawled ${num(s.crawled)} of ${num(s.sitemap_urls)} sitemap URLs on ${date(s.updated)}.`)];
      out.push(el("div", { class: "grid kpis" },
        kpi("Health score", `${s.score}/100`, "Average across pages"),
        kpi("AI readiness", `${s.ai_score}/100`, "Structured data, clear headings, real answers"),
        kpi("llms.txt", s.llms_txt ? "Yes" : "No", "A plain-text guide for AI tools at /llms.txt"),
        kpi("Errors", num((s.status_codes && Object.entries(s.status_codes).filter(([c]) => +c >= 400).reduce((a, [, n]) => a + n, 0)) || 0), "Pages returning 4xx/5xx"),
      ));
      if (D.auditHist && D.auditHist.length > 1) out.push(el("div", { class: "card", style: "margin-top:1rem" }, lineChart([
        { label: "Health", data: D.auditHist.map((x) => x.score) }, { label: "AI readiness", data: D.auditHist.map((x) => x.ai_score) }], D.auditHist.map((x) => x.date))));

      const bots = (s.robots && s.robots.bots) || {};
      out.push(el("div", { class: "grid two", style: "margin-top:1rem" },
        el("div", { class: "card" }, el("h3", {}, "Issues found"), table([
          { key: "severity", label: "Severity", render: (r) => el("span", { class: `pill ${r.severity}` }, r.severity), sortVal: (r) => ({ high: 3, medium: 2, low: 1 })[r.severity] },
          { key: "label", label: "Issue" }, { key: "pages", label: "Pages", num: true, fmt: num },
        ], s.issues, { search: false, limit: 30, sort: ["severity", -1] })),
        el("div", { class: "card" }, el("h3", {}, "Crawler access (robots.txt)"),
          el("p", { class: "small muted" }, "AI assistants can only recommend what their crawlers are allowed to read."),
          el("table", {}, el("tbody", {}, ...Object.entries(bots).map(([b, ok]) => el("tr", {}, el("td", {}, b), el("td", {}, el("span", { class: `pill ${ok ? "ok" : "error"}` }, ok ? "Allowed" : "Blocked")))))),
          el("h3", { style: "margin-top:1rem" }, "Structured data in use"),
          el("p", { class: "small" }, Object.entries(s.structured_data_types || {}).map(([t, n]) => `${t} (${n})`).join(", ") || "None found")),
      ));

      if (D.auditPages) {
        const codes = [...new Set(D.auditPages.flatMap((p) => p.issues))].sort();
        const sections = [...new Set(D.auditPages.map((p) => shortUrl(p.url).split("/")[1] || "home"))].sort();
        D.auditPages.forEach((p) => { p._section = shortUrl(p.url).split("/")[1] || "home"; });
        out.push(el("h2", {}, "Every page"), el("div", { class: "card" }, table([
          { key: "url", label: "Page", render: (p) => link(p.url), cls: "url" },
          { key: "score", label: "Score", num: true }, { key: "status", label: "Status", num: true },
          { key: "title", label: "Title", render: (p) => (p.title ? `${p.title} (${p.title.length})` : "–") },
          { key: "issues", label: "Issues", render: (p) => p.issues.join(", ") || "—", sortVal: (p) => p.issues.length },
          { key: "words", label: "Words", num: true, fmt: num },
        ], D.auditPages, { sort: ["score", 1], limit: 50, filters: [{ key: "issues", label: "issues", options: codes }, { key: "_section", label: "sections", options: sections }] })));
      }
      return out;
    },

    ux() {
      const u = D.ux;
      if (!u) return [empty("The visitor-experience check hasn't run yet.", "It runs weekly. Add a PAGESPEED_API_KEY for speed and accessibility scores; any AI key turns on the task checks.")];
      const s = u.summary || {};
      const scoreTxt = (v) => (v == null ? "–" : `${v}/100`);
      const out = [el("p", { class: "lead" }, `${s.pages} pages under ${u.section}, checked ${date(u.updated)} on a phone-sized screen. ${u.sources.pagespeed === "all pages" ? "" : "PageSpeed covered " + u.sources.pagespeed + ". "}`)];
      out.push(el("div", { class: "grid kpis" },
        kpi("Can visitors find answers?", scoreTxt(s.findability), u.checked_by ? `Key pages read by ${u.checked_by} as a first-time visitor` : "Add any AI key to turn on"),
        kpi("Mobile speed", scoreTxt(s.performance), s.origin_field ? `Real visitors: ${s.origin_field.toLowerCase()} overall` : "Google PageSpeed, mobile"),
        kpi("Accessibility", scoreTxt(s.accessibility), "Google Lighthouse checks"),
        kpi("Reading level", s.grade_level == null ? "–" : `Grade ${s.grade_level}`, s.hard_to_read == null ? "Aim for grade 8" : `${s.hard_to_read} pages above grade 10; aim for 8`),
        kpi("Facts that disagree", num(s.conflicts), "Hours, prices or visit length differ between pages"),
      ));
      if ((u.conflicts || []).length) {
        out.push(el("h2", {}, "Pages that contradict each other"), el("p", { class: "lead" }, "Visitors and AI assistants both lose trust when pages disagree. Fix these first."),
          el("div", { class: "card" }, table([{ key: "fact", label: "Fact" }, { key: "pages", label: "Pages", render: (c) => (c.pages || []).join(", ") }, { key: "detail", label: "What disagrees" }], u.conflicts, { search: false })));
      }
      const keyed = u.pages.filter((p) => p.task_check);
      if (keyed.length) {
        const ids = Object.keys(u.tasks);
        const sym = { top: ["✓", "yes", "Answered near the top"], buried: ["↓", "err", "Answered, but buried"], linked: ["→", "cite", "Linked from here"], missing: ["✕", "no", "Missing"], not_relevant: ["·", "no", "Not expected here"] };
        const tb = el("tbody", {}, ...keyed.map((p) => el("tr", {},
          el("td", {}, link(p.url, p.path), p.task_check.biggest_fix ? el("div", { class: "small muted" }, p.task_check.biggest_fix) : null),
          el("td", { class: "num" }, p.task_check.findability ?? "–"),
          ...ids.map((id) => { const t = p.task_check.tasks[id] || { status: "missing" }; const [g, c, lbl] = sym[t.status] || sym.missing;
            return el("td", { class: "cell", title: `${lbl}${t.note ? ": " + t.note : ""}` }, el("span", { class: `dot ${c}` }, g)); }))));
        out.push(el("h2", {}, "Can a first-time visitor find what they need?"),
          el("div", { class: "legend" }, ...Object.values(sym).slice(0, 4).map(([g, c, l]) => el("span", {}, el("span", { class: `dot ${c}` }, g), " ", l))),
          el("div", { class: "card table-wrap" }, el("table", { class: "matrix" },
            el("thead", {}, el("tr", {}, el("th", {}, "Page"), el("th", { class: "num" }, "Score"), ...ids.map((id) => el("th", { class: "num", title: u.tasks[id] }, id.replace("_", " "))))), tb)),
          el("p", { class: "small muted" }, "Hover a dot for the reviewer's note."));
      }
      const fmtS = (v) => (v == null ? "–" : `${v}s`);
      out.push(el("h2", {}, "Every /visit page"), el("div", { class: "card" }, table([
        { key: "path", label: "Page", render: (p) => link(p.url, p.path), cls: "url" },
        { key: "perf", label: "Speed", num: true, render: (p) => (p.pagespeed || {}).performance ?? "–", sortVal: (p) => (p.pagespeed || {}).performance },
        { key: "a11y", label: "Access.", num: true, render: (p) => (p.pagespeed || {}).accessibility ?? "–", sortVal: (p) => (p.pagespeed || {}).accessibility },
        { key: "lcp", label: "Load (LCP)", num: true, render: (p) => fmtS((p.pagespeed || {}).lcp_s), sortVal: (p) => (p.pagespeed || {}).lcp_s },
        { key: "grade", label: "Grade", num: true, render: (p) => (p.readability || {}).grade_level ?? "–", sortVal: (p) => (p.readability || {}).grade_level },
        { key: "tl", label: "Words to ticket link", num: true, render: (p) => { const w = (p.readability || {}).words_before_ticket_link; return w == null ? "none" : w; }, sortVal: (p) => { const w = (p.readability || {}).words_before_ticket_link; return w == null ? 99999 : w; } },
        { key: "eng", label: "Engaged", num: true, render: (p) => (p.ga4 ? pct(p.ga4.engagement_rate, 0) : "–"), sortVal: (p) => (p.ga4 || {}).engagement_rate },
        { key: "time", label: "Avg time", num: true, render: (p) => (p.ga4 ? fmtS(p.ga4.avg_engagement_s) : "–"), sortVal: (p) => (p.ga4 || {}).avg_engagement_s },
        { key: "rage", label: "Rage / dead clicks", num: true, render: (p) => (p.clarity ? `${p.clarity.rage_clicks ?? "–"}% / ${p.clarity.dead_clicks ?? "–"}%` : "–"), sortVal: (p) => ((p.clarity || {}).rage_clicks || 0) + ((p.clarity || {}).dead_clicks || 0) },
        { key: "fails", label: "Accessibility problems", render: (p) => ((p.pagespeed || {}).a11y_failures || []).join("; ") || "–" },
      ], u.pages, { sort: ["path", 1], limit: 100 })),
      el("p", { class: "small muted" }, "Speed and accessibility are Google Lighthouse scores on a phone (0–100). Grade is the US school reading level. \"Words to ticket link\" counts how much a visitor reads before the first ticket link in the page body. \"Engaged\" and \"Avg time\" come from GA4 (28 days); rage and dead clicks are the share of Clarity sessions with them (last 3 days)."));
      if ((u.errors || []).length) out.push(el("details", {}, el("summary", {}, `${u.errors.length} problems during the run`), el("ul", { class: "clean small" }, ...u.errors.map((e) => el("li", {}, e)))));
      return out;
    },

    checkout() {
      const c = D.checkout;
      if (!c) return [empty("Checkout tracking isn't running yet.", "Add the repo variable GA4_PROPERTY_ID and give the Google service account Viewer access in GA4 (see Setup).")];
      const fmt = (v) => (v == null ? "–" : typeof v === "string" ? v : pct(v, 0));
      const cur = c.current, prev = c.previous;
      const out = [el("p", { class: "lead" }, `How many people who reach the ticket store (${c.store}) complete each step, ${c.period}. ${c.note}`)];
      const pp = (a, b) => (typeof a === "number" && typeof b === "number" ? el("span", { class: `delta ${a >= b ? "up" : "down"}` }, `${a >= b ? "+" : ""}${((a - b) * 100).toFixed(1)} pts vs prior 28 days`) : el("span", { class: "muted" }, "no comparison"));
      out.push(el("div", { class: "grid kpis" },
        kpi("Checkout completion", fmt(cur.checkout_completion), pp(cur.checkout_completion, prev.checkout_completion)),
        kpi("Store visitors who buy", fmt(cur.store_conversion), pp(cur.store_conversion, prev.store_conversion)),
        kpi("Ticket page → store", fmt(c.ticket_page_to_store), "trlibrary.com/tickets visitors who open the store (approximate)"),
      ));
      if ((cur.missing_steps || []).length) out.push(el("p", { class: "warn-box small", style: "margin-top:1rem" }, `Not reported to GA4 by the ticket store: ${cur.missing_steps.map((s) => c.labels[s] || s).join(", ")}. Ask ACME to turn on GA4 ecommerce events for those steps to see where people drop off.`));
      const steps = ["store_visit", ...cur.tracked_steps];
      const max = 1;
      out.push(el("h2", {}, "Where people drop off"), el("div", { class: "card" }, el("table", {}, el("tbody", {},
        ...steps.map((st, i) => {
          const r = st === "store_visit" ? 1 : cur.of_store_visitors[st];
          const step = i ? cur.step_to_step[`${steps[i - 1]}->${st}`] : null;
          return el("tr", {}, el("td", {}, c.labels[st] || st),
            el("td", { style: "width:45%" }, el("div", { class: "bar" }, el("span", { style: `width:${typeof r === "number" ? (100 * r) / max : 0}%` }))),
            el("td", { class: "num" }, fmt(r)), el("td", { class: "num small muted" }, i ? `${fmt(step)} of previous step` : "everyone"));
        })))));
      const devs = Object.keys(c.by_device || {});
      if (devs.length) out.push(el("h2", {}, "By device"), el("div", { class: "card" }, table([
        { key: "d", label: "Device" }, { key: "cc", label: "Checkout completion", num: true, render: (r) => fmt(r.cc) }, { key: "sc", label: "Store visitors who buy", num: true, render: (r) => fmt(r.sc) },
      ], devs.map((dv) => ({ d: dv, cc: c.by_device[dv].checkout_completion, sc: c.by_device[dv].store_conversion })), { search: false })));
      const fr = c.store_friction;
      if (fr) {
        const o = fr.overall || {}, p1 = (v) => (v == null ? "–" : `${v}%`);
        out.push(el("h2", {}, "Where people struggle in the store"),
          el("p", { class: "lead" }, `From Microsoft Clarity on the ticket store, ${fr.period}: the share of sessions with each frustration signal. Dead clicks are clicks on things that aren't links or buttons; quick backs are people leaving a page within seconds.`),
          el("div", { class: "grid kpis" },
            kpi("Dead clicks", p1(o.dead_clicks), "sessions with at least one"), kpi("Rage clicks", p1(o.rage_clicks), "repeated frustrated clicking"),
            kpi("Quick backs", p1(o.quick_backs), "left a page almost immediately"), kpi("Scroll depth", p1(o.scroll_depth), "average")),
          el("div", { class: "card", style: "margin-top:1rem" }, table([
            { key: "page", label: "Store page" }, { key: "dead_clicks", label: "Dead clicks", num: true, fmt: p1 },
            { key: "rage_clicks", label: "Rage clicks", num: true, fmt: p1 }, { key: "quick_backs", label: "Quick backs", num: true, fmt: p1 },
            { key: "scroll_depth", label: "Scroll depth", num: true, fmt: p1 },
          ], Object.entries(fr.pages || {}).map(([page, v]) => ({ page, ...v })), { search: false, sort: ["dead_clicks", -1], limit: 15 })),
          el("p", { class: "small muted" }, "Watch the matching session recordings in Clarity to see what people were trying to click."));
      } else if (c.store_friction_error) {
        out.push(el("p", { class: "warn-box small", style: "margin-top:1rem" }, `Clarity: ${c.store_friction_error}`));
      }
      const wk = (c.weekly || []).filter((w) => typeof w.checkout_completion === "number");
      if (wk.length > 1) out.push(el("h2", {}, "Weekly trend"), el("div", { class: "card" }, lineChart([
        { label: "Checkout completion", data: wk.map((w) => w.checkout_completion) }, { label: "Store visitors who buy", data: wk.map((w) => (typeof w.store_conversion === "number" ? w.store_conversion : null)) }],
        wk.map((w) => `Wk ${String(w.week).slice(4)}`), { pctAxis: true })));
      return out;
    },

    links() {
      const L = D.links;
      if (!L) return [empty("The internal-links check hasn't run yet.", "It runs weekly; no keys needed.")];
      const s = L.summary || {};
      const short = (p) => (p || "").replace(/^https?:\/\/(www\.)?trlibrary\.com/, "") || "/";
      const pageLink = (p) => link("https://www.trlibrary.com" + p, p);
      const out = [el("p", { class: "lead" }, `Every page of trlibrary.com, read ${date(L.updated)}. Internal links help readers go deeper and tell Google which pages matter; broken ones lose both.`)];
      out.push(el("div", { class: "grid kpis" },
        kpi("Broken links on our site", num(s.broken_internal), `${num(s.broken_internal_instances)} links on our pages point to these; ${num(s.redirects_high_confidence)} sure fixes`),
        kpi("Links to add", num(s.suggestions), "Pages mention a topic we have a page for, but don't link it"),
        kpi("Pages nothing links to", num(s.orphans), "No links from other pages' content"),
        kpi("Same topic, two pages", num(s.duplicate_topics), "Pick one to be the main page"),
        kpi("Broken outside links", num(s.external_broken), s.linkchecker_scan ? `From the LinkChecker, scanned ${s.linkchecker_scan}` : "LinkChecker results unavailable"),
      ));
      // 1. broken internal -> redirects
      const conf = (c) => el("span", { class: `pill ${c === "high" ? "ok" : c === "medium" ? "medium" : "low"}` }, c);
      out.push(el("h2", {}, "Fix broken links with 301 redirects"),
        el("p", { class: "lead" }, "Each broken address below gets a proposed redirect. Add the high-confidence ones in Drupal (Configuration → Search and metadata → URL redirects), and check medium and low ones before adding. Fixing the link on the page itself is even better when there are only one or two."),
        el("p", {}, el("a", { href: "data/redirects.csv", download: "trlibrary-redirects.csv" }, "Download all as CSV"), el("span", { class: "small muted" }, " (source, destination, language, status code — the Redirect module's import format)")),
        el("div", { class: "card" }, table([
          { key: "broken", label: "Broken address", cls: "url", render: (b) => el("span", {}, b.broken, " ", el("span", { class: "pill" }, String(b.status))) },
          { key: "redirect_to", label: "Redirect to", cls: "url", render: (b) => (b.redirect_to.startsWith("http") ? link(b.redirect_to, b.redirect_to) : pageLink(b.redirect_to)) },
          { key: "confidence", label: "Confidence", render: (b) => conf(b.confidence), sortVal: (b) => ({ high: 3, medium: 2, low: 1 })[b.confidence] },
          { key: "why", label: "Why", render: (b) => el("span", { class: "small" }, b.why) },
          { key: "source_count", label: "Linked from", num: true, render: (b) => el("details", {}, el("summary", {}, `${b.source_count} page${b.source_count === 1 ? "" : "s"}`), el("ul", { class: "clean small" }, ...b.sources.map((x) => el("li", {}, pageLink(x.page), x.link_text ? ` (“${x.link_text}”)` : "")))), sortVal: (b) => b.source_count },
        ], L.broken_internal || [], { sort: ["confidence", -1], limit: 30 })));
      // 2. suggested links
      const secs = [...new Set((L.suggestions || []).map((x) => "/" + x.source.split("/")[1]))].sort();
      (L.suggestions || []).forEach((x) => { x._section = "/" + x.source.split("/")[1]; });
      out.push(el("h2", {}, "Links to add"),
        el("p", { class: "lead" }, "The bracketed words name a topic that has its own page. Link them. Highest-value first: links to pages Google already shows, especially ones ranking 4–20, and pages with few links in."),
        el("div", { class: "card" }, table([
          { key: "source", label: "On this page", cls: "url", render: (x) => pageLink(x.source) },
          { key: "snippet", label: "Link these words", render: (x) => { const m = x.snippet.split(/\[\[|\]\]/); return el("span", { class: "small" }, m[0], el("mark", {}, m[1] || ""), m[2] || ""); } },
          { key: "target", label: "To this page", cls: "url", render: (x) => el("span", {}, pageLink(x.target), el("div", { class: "small muted" }, x.target_title)) },
          { key: "target_inlinks", label: "Links in now", num: true },
          { key: "score", label: "Value", num: true, fmt: (v) => v.toFixed(1) },
        ], L.suggestions || [], { sort: ["score", -1], limit: 25, filters: [{ key: "_section", label: "sections", options: secs }] })));
      // 3. orphans
      out.push(el("h2", {}, "Pages nothing links to"), el("p", { class: "lead" }, "Only menus or search lead here. Sorted by how often Google shows them, so the top ones are the biggest missed opportunity."),
        el("div", { class: "card" }, table([
          { key: "page", label: "Page", cls: "url", render: (r) => el("span", {}, pageLink(r.page), el("div", { class: "small muted" }, r.title)) },
          { key: "impressions", label: "Google impressions (28d)", num: true, fmt: num }, { key: "position", label: "Avg position", num: true, fmt: pos },
          { key: "unlinked_mentions", label: "Mentioned without link", num: true },
        ], L.orphans || [], { sort: ["impressions", -1], limit: 20 })));
      // 4. duplicates
      if ((L.duplicate_topics || []).length) out.push(el("h2", {}, "Same topic, two pages"), el("p", { class: "lead" }, "These pages compete with each other in Google and split links. Choose a main page, link the others to it, or merge and redirect."),
        el("div", { class: "card" }, table([
          { key: "name", label: "Topic" },
          { key: "pages", label: "Pages (Google impressions, 28d)", render: (d) => el("ul", { class: "clean small" }, ...d.pages.map((p, i) => el("li", {}, pageLink(p), ` (${num(d.impressions[i])})`))) },
        ], L.duplicate_topics, { search: false, limit: 20 })));
      // 5. related pairs
      if ((L.related_unlinked || []).length) out.push(el("h2", {}, `Related ${L.focus_sections.join(", ")} pages with no link either way`),
        el("div", { class: "card" }, table([
          { key: "a", label: "Page", cls: "url", render: (r) => el("span", {}, pageLink(r.a), el("div", { class: "small muted" }, r.a_title)) },
          { key: "b", label: "Related page", cls: "url", render: (r) => el("span", {}, pageLink(r.b), el("div", { class: "small muted" }, r.b_title)) },
          { key: "similarity", label: "Overlap", num: true, fmt: (v) => pct(v, 0) },
          { key: "shared_words", label: "Shared words", render: (r) => r.shared_words.join(", ") },
        ], L.related_unlinked, { sort: ["similarity", -1], limit: 20 })));
      // 6. external
      const ext = L.external || {};
      if (ext.error) out.push(el("p", { class: "warn-box" }, ext.error));
      else if ((ext.external || []).length) {
        const ours = ext.external.filter((r) => !r.from_video_pages), vids = ext.external.filter((r) => r.from_video_pages);
        const extTable = (rows) => table([
          { key: "url", label: "Outside link", cls: "url", render: (r) => link(r.url, r.url) },
          { key: "status", label: "Status", render: (r) => el("span", { class: `pill ${r.kind === "broken" ? "high" : "low"}` }, r.status ? String(r.status) : r.error ? "error" : r.kind) },
          { key: "sources", label: "On pages", render: (r) => el("span", { class: "small" }, ...r.sources.slice(0, 4).flatMap((p, i) => [i ? ", " : "", pageLink(p)])), sortVal: (r) => r.sources.length },
        ], rows, { limit: 20 });
        out.push(el("h2", {}, "Broken links to other websites"),
          el("p", { class: "lead" }, `From the LinkChecker (links.labs.trlibrary.com), last scan ${ext.generated_at}. Update or remove these in the page content; redirects can't fix links to other sites. 403s are often the other site blocking automated checks, so test those in a browser first.`),
          el("div", { class: "card" }, extTable(ours)));
        if (vids.length) out.push(el("details", {}, el("summary", {}, `${vids.length} more on /video/ pages (from YouTube descriptions, lower priority)`), el("div", { class: "card" }, extTable(vids))));
      }
      if ((L.links_through_redirects || []).length) out.push(el("details", {}, el("summary", {}, `${L.links_through_redirects.length} links that work but go through a redirect (update when convenient)`),
        el("div", { class: "card" }, table([{ key: "link", label: "Link", cls: "url" }, { key: "goes_to", label: "Ends up at", cls: "url", render: (r) => pageLink(r.goes_to) }, { key: "sources", label: "On pages", render: (r) => r.sources.slice(0, 3).join(", ") }], L.links_through_redirects, { limit: 20 }))));
      return out;
    },

    tips() {
      const t = D.tips;
      if (!t) return [empty("No recommendations yet.", "Add any AI key (Gemini, Claude, ChatGPT or Perplexity). Recommendations are written weekly.")];
      const out = [el("p", { class: "warn-box" }, `Drafts written by ${t.provider_label || "AI"} (${t.model}) on ${date(t.updated)}.${(t.fallbacks || []).length ? ` Skipped this week: ${t.fallbacks.join(", ")}.` : ""} Review before using: check every historical claim and never publish a TR quote that hasn't been verified.`)];
      const b = t.ai_brief;
      if (b) {
        out.push(el("h2", {}, "Getting recommended by AI assistants"), el("div", { class: "card tip" },
          el("p", {}, el("strong", {}, b.headline || "")),
          b.how_described ? el("p", {}, el("strong", {}, "How we're described: "), b.how_described) : null,
          (b.actions || []).length ? el("div", {}, el("h3", {}, "Actions"), el("ol", {}, ...b.actions.map((x) => el("li", {}, el("strong", {}, x.action), ` (${x.effort} effort; ${x.where}) `, el("span", { class: "muted" }, x.why))))) : null,
          (b.gaps || []).length ? el("details", {}, el("summary", {}, "Where we're missing"), el("ul", { class: "clean" }, ...b.gaps.map((g) => el("li", {}, el("strong", {}, g.theme), ": ", g.who_shows_up_instead)))) : null,
          (b.inaccuracies || []).length ? el("details", { open: true }, el("summary", {}, "Inaccurate claims to correct"), el("ul", { class: "clean" }, ...b.inaccuracies.map((g) => el("li", {}, `${g.engine}: “${g.claim}” → fix on ${g.correction_source}`)))) : null,
        ));
      }
      if ((t.pages || []).length) out.push(el("h2", {}, "Page recommendations"));
      for (const p of t.pages || []) {
        const sug = (label, o) => (o && o.suggested ? el("div", {}, el("div", { class: "small muted" }, `${label} (${o.suggested.length} characters)`), el("div", { class: "suggest" }, o.suggested), el("div", { class: "small muted" }, o.why)) : null);
        const list = (title, arr, f) => ((arr || []).length ? el("div", {}, el("h3", { style: "margin-top:.75rem" }, title), el("ul", { class: "clean" }, ...arr.map(f))) : null);
        out.push(el("div", { class: "card tip" },
          el("h3", {}, link(p.page)), p.written_by ? el("p", { class: "small muted" }, `Written by ${p.written_by}`) : null, el("p", {}, p.summary || ""),
          (p.checks || []).length ? el("p", { class: "warn-box small" }, p.checks.join(" · ")) : null,
          sug("Suggested title", p.title), sug("Suggested meta description", p.meta_description),
          list("Content to add", p.content_additions, (c) => el("li", {}, c.for_query ? el("strong", {}, `“${c.for_query}”: `) : null, c.suggestion, c.draft ? el("div", { class: "suggest small" }, c.draft) : null)),
          list("AI readiness", p.ai_readiness, (c) => el("li", {}, c.suggestion, el("span", { class: "muted" }, ` (${c.why})`))),
          list("Technical", p.technical, (c) => el("li", {}, c.suggestion, el("span", { class: "muted" }, ` (${c.why})`))),
          list("Verify before publishing", p.needs_verification, (c) => el("li", {}, c)),
        ));
      }
      if ((t.errors || []).length) out.push(el("details", {}, el("summary", {}, `${t.errors.length} pages failed`), el("ul", { class: "clean small" }, ...t.errors.map((e) => el("li", {}, e)))));
      return out;
    },

    setup() {
      const names = { gsc: "Search Console", audit: "Site audit", ranks: "Rank tracking", ai_visibility: "AI visibility", opportunities: "Opportunities", curate: "Keyword & question discovery", ux: "Visitor experience (/visit)", links: "Internal links & redirects", checkout: "Ticket checkout (GA4)", tips: "AI recommendations", digest: "AI-readable digest (llms.txt)" };
      const secrets = { gsc: "Variables GCP_WIF_PROVIDER + GCP_SERVICE_ACCOUNT (or secret GSC_SERVICE_ACCOUNT_JSON)", audit: "none needed", ranks: "DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD", ai_visibility: "OPENAI_API_KEY, GEMINI_API_KEY, PERPLEXITY_API_KEY, ANTHROPIC_API_KEY (any)", opportunities: "none needed", curate: "none (an AI key improves the filtering); rules in config/tracking.yml", ux: "PAGESPEED_API_KEY (needed); any AI key for task checks; optional GA4_PROPERTY_ID variable and CLARITY_API_TOKEN (the website's Clarity project)", links: "none needed (reads the LinkChecker's results.json for outside links)", checkout: "Variable GA4_PROPERTY_ID + Google sign-in (service account as GA4 Viewer); optional CLARITY_STORE_API_TOKEN for store frustration signals", digest: "none needed", tips: "Any one of GEMINI_API_KEY, ANTHROPIC_API_KEY, OPENAI_API_KEY, PERPLEXITY_API_KEY (order set in config/site.yml)" };
      const st = D.status || {};
      return [
        el("p", { class: "lead" }, "Each source turns on when its key is added as a GitHub Actions secret on the SEO repo. Instructions are in the repo README."),
        el("div", { class: "card table-wrap" }, el("table", {}, el("thead", {}, el("tr", {}, el("th", {}, "Source"), el("th", {}, "State"), el("th", {}, "Last run"), el("th", {}, "Details"), el("th", {}, "Secrets"))),
          el("tbody", {}, ...Object.keys(names).map((k) => {
            const s = st[k] || { state: "skipped", message: "Hasn't run yet" };
            return el("tr", {}, el("td", {}, names[k]), el("td", {}, el("span", { class: `pill ${s.state}` }, s.state === "skipped" ? "off" : s.state)), el("td", {}, date(s.updated)), el("td", { class: "small" }, s.message), el("td", { class: "small muted" }, secrets[k]));
          })))),
      ];
    },
  };

  // ---------- routing ----------
  function render() {
    const id = (location.hash || "#overview").slice(1);
    const view = VIEWS[id] ? id : "overview";
    charts.splice(0).forEach((c) => c.destroy());
    document.querySelectorAll("#tabs a").forEach((a) => {
      const on = a.getAttribute("href") === "#" + view;
      a.classList.toggle("active", on);
      if (on) a.scrollIntoView({ block: "nearest", inline: "nearest" });
    });
    const main = document.getElementById("view");
    try { main.replaceChildren(...VIEWS[view]().filter(Boolean)); } catch (e) { console.error(e); main.replaceChildren(empty("Something went wrong drawing this tab.", String(e))); }
  }

  async function load() {
    await Promise.all(Object.entries(FILES).map(async ([k, f]) => {
      try { const r = await fetch(f, { cache: "no-cache" }); D[k] = r.ok ? await r.json() : null; } catch { D[k] = null; }
    }));
    const stamps = Object.values(D.status || {}).map((s) => s.updated).filter(Boolean).sort();
    document.getElementById("updated").textContent = stamps.length ? `Updated ${date(stamps[stamps.length - 1])}` : "No data yet";
    window.addEventListener("hashchange", () => { render(); document.getElementById("view").focus({ preventScroll: true }); });
    render();
  }
  load();
})();
