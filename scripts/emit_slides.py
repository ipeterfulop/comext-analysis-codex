#!/usr/bin/env python3
import json, sys, os

DIR = sys.argv[1]
b = json.load(open(os.path.join(DIR, "data.json")))
SITC = b["meta"]["sitc_categories"]

CAT_ICON = {"32":"mdi-fire","33":"mdi-oil","34":"mdi-fire-circle","35":"mdi-flash"}
ICON_CHOICE = "mdi-chart-areaspline"

out = []
def add(s): out.append(s)

add("""---
theme: neversink
title: COMEXT Energy Trade — 2021–2025
info: |
  Eurostat COMEXT (ext_go_detail) energy & hydrocarbons analysis.
  Dataset filtered to SITC 32/33/34/35.
transition: slide-left
mdc: true
---

<div class="grid grid-cols-2 gap-16 h-full items-center">
  <div>
    <h1 class="text-5xl font-bold leading-tight">COMEXT Energy & Hydrocarbons</h1>
    <p class="text-xl opacity-80 mt-4">EU international trade in goods — SITC 32 / 33 / 34 / 35, monthly data from January 2021 to December 2025</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="i-mdi-chart-areaspline text-[22rem]" style="opacity: 0.05"></div>
  </div>
</div>

---
layout: default
---

# Goals and style

<div class="relative h-full">
  <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
    <div class="i-mdi-target-arrow text-[20rem]" style="opacity: 0.05"></div>
  </div>
  <ul class="text-xl space-y-3 relative">
    <li>Light, informal knowledge-sharing session</li>
    <li>More show &amp; tell than deep dive</li>
    <li>Real experiences and working solutions</li>
    <li>Practical ideas for day-to-day work in the Budapest data teams</li>
    <li>Open to contributions from anyone in the Budapest data teams</li>
    <li>A prepared topic is always ready if no one volunteers</li>
  </ul>
</div>

---
layout: center
---

# The dataset

<p class="text-xl opacity-80 max-w-3xl mx-auto text-center">
Eurostat <code>ext_go_detail</code> (COMEXT) — 60 monthly <code>.7z</code> archives covering 2021–2025,
obtained via the official dissemination API. Download and unpacking were <b>AI-assisted</b> and executed
<b>in parallel using one subagent per year</b>.
</p>

---
layout: center
---

# Data at a glance

<div class="text-lg opacity-80 max-w-4xl mx-auto space-y-3 text-center">
  <p>~<b>293.8 M</b> raw detail rows across 60 monthly files · 18 columns per row.</p>
  <p>After filtering to SITC energy categories (<code>32, 33, 34, 35</code>): <b>1,617,089</b> rows retained.</p>
</div>

<div class="grid grid-cols-2 gap-6 mt-6 max-w-5xl mx-auto text-sm">
  <div class="border rounded p-4">
    <h3 class="font-semibold mb-2">Key columns</h3>
    <ul class="space-y-1">
      <li><code>REPORTER</code>, <code>PARTNER</code> — 2-letter country codes</li>
      <li><code>PRODUCT_SITC</code> — 3–5 digits (first 2 = category)</li>
      <li><code>FLOW</code> — 1 = imports, 2 = exports</li>
      <li><code>PERIOD</code> — YYYYMM (string)</li>
      <li><code>VALUE_EUR</code>, <code>QUANTITY_KG</code> — numeric</li>
    </ul>
  </div>
  <div class="border rounded p-4">
    <h3 class="font-semibold mb-2">Quality notes</h3>
    <ul class="space-y-1">
      <li>Value/quantity missing encoded as 0 — dropped when ranking lowest.</li>
      <li>Aggregate reporter codes (<code>EU27_2020</code>, etc.) excluded from per-country rankings.</li>
      <li>Rows per year fairly uniform: 57–59 M.</li>
      <li>Obfuscated codes (e.g. <code>39XXXXXX</code>) present in PRODUCT_NC but SITC prefix still usable.</li>
    </ul>
  </div>
</div>

---
layout: center
---

# Roadmap

<p class="text-xl opacity-80 max-w-3xl mx-auto text-center">
Three chapters follow: <b>imports</b>, <b>exports</b>, and a <b>Hungary deep-dive</b> with year-over-year trends.
</p>

---
layout: section
---

# Chapter 1 — Imports

Top 5 EU reporter countries per SITC energy category, with highest and lowest importer callouts.
""")

def fmt_eur(v):
    return "€" + f"{int(v):,}"

def ranking_slide(chapter, flow_label, cat, data, color):
    label = SITC[cat]
    top5_json = json.dumps(data["top5"])
    highest = data["highest"]
    lowest = data["lowest"]
    lowest_block = (
        f'<div><div class="text-xs opacity-60">LOWEST {flow_label.upper()}ER (non-zero)</div>'
        f'<div class="text-2xl font-bold">{lowest["code"]} · {lowest["name"]}</div>'
        f'<div class="opacity-80">{fmt_eur(lowest["value"])}</div></div>'
        if lowest else
        '<div><div class="text-xs opacity-60">LOWEST</div><div class="text-xl">insufficient data</div></div>'
    )
    highest_block = (
        f'<div><div class="text-xs opacity-60">HIGHEST {flow_label.upper()}ER</div>'
        f'<div class="text-2xl font-bold">{highest["code"]} · {highest["name"]}</div>'
        f'<div class="opacity-80">{fmt_eur(highest["value"])}</div></div>'
        if highest else '<div>—</div>'
    )
    note = "" if data["count_nonzero"] >= 5 else f" · only {data['count_nonzero']} reporters with data"
    add(f"""
---
layout: default
---

# {flow_label.title()}s — SITC {cat} · {label}

<div class="text-sm opacity-70 -mt-2 mb-2">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR{note}</div>

<BarRanking :items='{top5_json}' color="{color}" label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  {highest_block}
  {lowest_block}
</div>
""")

# Chapter 1 — imports
COLOR_IMP = "#2563eb"
for cat in ["32","33","34","35"]:
    ranking_slide("imports", "import", cat, b["imports"][cat], COLOR_IMP)

add("""
---
layout: section
---

# Chapter 2 — Exports

Top 5 EU reporter countries per SITC energy category, with highest and lowest exporter callouts.
""")

COLOR_EXP = "#dc2626"
for cat in ["32","33","34","35"]:
    ranking_slide("exports", "export", cat, b["exports"][cat], COLOR_EXP)

add("""
---
layout: section
---

# Chapter 3 — Hungary

Hungary's yearly imports and exports per SITC energy category, benchmarked against the EU-27 average.
""")

def hu_commentary(cat, h):
    years=h['years']; hi=h['hu_imports']; he=h['hu_exports']; ei=h['eu_avg_imports']; ee=h['eu_avg_exports']
    def change(v):
        if v[0]==0: return "n/a"
        c=(v[-1]-v[0])/v[0]*100
        return f"{c:+.0f}%"
    imp_vs = "above" if sum(hi)/len(hi) > sum(ei)/len(ei) else "below"
    exp_vs = "above" if sum(he)/len(he) > sum(ee)/len(ee) else "below"
    peak_imp_yr = years[hi.index(max(hi))] if max(hi)>0 else None
    lines = [
        f"Imports change 2021→2025: <b>{change(hi)}</b>; exports change: <b>{change(he)}</b>.",
        f"Hungary sits <b>{imp_vs}</b> the EU-27 average on imports and <b>{exp_vs}</b> on exports (period mean).",
    ]
    if peak_imp_yr:
        lines.append(f"Import peak year for SITC {cat}: <b>{peak_imp_yr}</b>.")
    return lines

for cat in ["32","33","34","35"]:
    h = b["hungary"][cat]
    label = SITC[cat]
    series = [
        {"label":"HU imports","values":h["hu_imports"],"color":"#2563eb","dashed":False,"gapOnZero":True},
        {"label":"HU exports","values":h["hu_exports"],"color":"#dc2626","dashed":False,"gapOnZero":True},
        {"label":"EU-27 avg imports","values":h["eu_avg_imports"],"color":"#2563eb","dashed":True},
        {"label":"EU-27 avg exports","values":h["eu_avg_exports"],"color":"#dc2626","dashed":True},
    ]
    commentary = hu_commentary(cat, h)
    all_zero = all(v == 0 for v in h["hu_imports"]) and all(v == 0 for v in h["hu_exports"])
    chart_or_msg = (
        f"<p class='text-lg opacity-70'>No Hungarian trade recorded in SITC {cat} for 2021–2025.</p>"
        if all_zero else
        f"<TrendLines :years='{json.dumps(h['years'])}' :series='{json.dumps(series)}' />"
    )
    comm_html = "\n".join(f"  <li>{c}</li>" for c in commentary)
    add(f"""
---
layout: default
---

# Hungary — SITC {cat} · {label}

<div class="text-sm opacity-70 -mt-2 mb-2">Imports vs. exports, 2021–2025, with EU-27 average</div>

{chart_or_msg}

<ul class="mt-4 text-sm space-y-1">
{comm_html}
</ul>
""")

with open(os.path.join(DIR, "slides.md"), "w") as fh:
    fh.write("\n".join(out))
print("slides.md written:", sum(1 for _ in open(os.path.join(DIR, "slides.md"))), "lines")
