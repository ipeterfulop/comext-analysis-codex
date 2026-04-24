---
theme: neversink
title: COMEXT Energy Trade in the EU
info: |
  Eurostat COMEXT ext_go_detail energy-trade analysis.
  Deck assembled from four explicit Codex subagent outputs.
mdc: true
transition: slide-left
---

---
id: "cover"
layout: "two-column"
agent_notes:
  - "Opening slide of the deck."
  - "Ground the title and subtitle in Eurostat COMEXT ext_go_detail."
---
<div class="grid grid-cols-2 gap-16 h-full items-center">
  <div>
    <h1 class="text-5xl font-bold leading-tight">COMEXT Energy Trade in the EU</h1>
    <p class="text-xl opacity-80 mt-4">Eurostat COMEXT ext_go_detail, energy-focused SITC 32/33/34/35 coverage, 2021–2025</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="i-mdi-chart-line text-[22rem]" style="opacity: 0.05"></div>
  </div>
</div>


---
id: "describe-the-data"
layout: "centered"
agent_notes:
  - "Tone: light but direct, setting the stage rather than deep-diving."
  - "Source of truth: docs/comext_investigation.md."
---
# COMEXT dataset scope

Eurostat `ext_go_detail` from the official dissemination API, covering monthly international trade detail for 2021–2025. Downloading and unzipping were AI-assisted and executed in parallel through one subagent per year before the energy-only filtering and deck assembly.


---
id: "population-context"
layout: "centered"
agent_notes:
  - "This slide fulfills the per-capita requirement from Section 2.1."
  - "Place it immediately after the dataset-description slide."
---
# Population context

Country populations are shown up front so the trade totals in later slides can be interpreted with per-capita context rather than raw scale alone.

| Code | Country | Population (2024) |
| --- | --- | ---: |
| AT | Austria | 9,177,982 |
| BE | Belgium | 11,858,610 |
| BG | Bulgaria | 6,441,421 |
| CY | Cyprus | 1,358,282 |
| CZ | Czechia | 10,905,028 |
| DE | Germany | 83,516,593 |
| DK | Denmark | 5,976,992 |
| EE | Estonia | 1,372,341 |
| ES | Spain | 48,848,840 |
| FI | Finland | 5,619,911 |
| FR | France | 68,551,653 |
| GR | Greece | — |
| HR | Croatia | 3,866,200 |
| HU | Hungary | 9,562,065 |
| IE | Ireland | 5,395,790 |
| IT | Italy | 58,952,704 |
| LT | Lithuania | 2,888,278 |
| LU | Luxembourg | 677,012 |
| LV | Latvia | 1,866,124 |
| MT | Malta | 568,847 |
| NL | Netherlands | 17,993,485 |
| PL | Poland | 36,559,233 |
| PT | Portugal | 10,694,681 |
| RO | Romania | 19,051,804 |
| SE | Sweden | 10,569,709 |
| SI | Slovenia | 2,127,400 |
| SK | Slovakia | 5,422,069 |


---
id: "data-quality-aspects"
layout: "centered"
agent_notes:
  - "Keep it an at-a-glance summary; do not profile every column."
  - "Tone: light but direct."
  - "Source of truth for the column list: docs/comext_investigation.md."
---
# Data quality snapshot

SITC-scoped trade rows across the prepared 2021–2025 monthly files, summarized after filtering to energy and hydrocarbons.

| Aspect | Value |
| --- | --- |
| Total rows | 1,617,089 |
| Columns | 18 (`REPORTER`, `PARTNER`, `PRODUCT_SITC`, `FLOW`, `PERIOD`, `VALUE_EUR`, `QUANTITY_KG`, ...) |
| Year coverage | 2021 – 2025 |
| Distinct reporters | 27 |
| Distinct products (`PRODUCT_SITC`) | 44 |
| Missing `VALUE_EUR` | 0.00% |
| Missing `QUANTITY_KG` | 0.00% |


---
id: "describe-the-analysis"
layout: "centered"
agent_notes:
  - "Roadmap slide only; do not render chapter contents here."
---
# Analysis roadmap

The rest of the deck moves through three chapters: imports, exports, and a Hungary deep-dive that tracks yearly import and export trends against the EU-27 average.
---
id: "chapter-imports"
layout: "centered-section-divider"
agent_notes:
  - "Centered section-divider slide for the chapter intro."
---
# Chapter 1 — Imports

This chapter ranks the top EU importers in each SITC energy category and calls out the highest and lowest non-zero importer in the same scope.
---
id: "imports-32"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '32%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Imports — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 36822338579.0}, {"code": "NL", "name": "Netherlands", "value": 31155185388.0}, {"code": "PL", "name": "Poland", "value": 12858743207.0}, {"code": "FR", "name": "France", "value": 9765978129.0}, {"code": "IT", "name": "Italy", "value": 9284202838.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest import</div>
    <div class="text-2xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">€36,822,338,579</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest import</div>
  <div class="text-2xl font-semibold mt-1">MT · Malta</div>
  <div class="opacity-80 mt-1">€3,740,495</div>
</div>
</div>
---
id: "imports-33"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '33%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Imports — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 458897949220.0}, {"code": "DE", "name": "Germany", "value": 356083093489.0}, {"code": "FR", "name": "France", "value": 264641729152.0}, {"code": "BE", "name": "Belgium", "value": 255665213774.0}, {"code": "ES", "name": "Spain", "value": 224028891100.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest import</div>
    <div class="text-2xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">€458,897,949,220</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest import</div>
  <div class="text-2xl font-semibold mt-1">MT · Malta</div>
  <div class="opacity-80 mt-1">€5,933,366,737</div>
</div>
</div>
---
id: "imports-34"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '34%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Imports — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 181038194170.0}, {"code": "IT", "name": "Italy", "value": 168018998273.0}, {"code": "FR", "name": "France", "value": 144002259907.0}, {"code": "BE", "name": "Belgium", "value": 138042294967.0}, {"code": "NL", "name": "Netherlands", "value": 80777618825.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest import</div>
    <div class="text-2xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">€181,038,194,170</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest import</div>
  <div class="text-2xl font-semibold mt-1">LU · Luxembourg</div>
  <div class="opacity-80 mt-1">€39,460,040</div>
</div>
</div>
---
id: "imports-35"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '35%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Imports — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 38172904447.0}, {"code": "IT", "name": "Italy", "value": 37195907331.0}, {"code": "FR", "name": "France", "value": 23850883899.0}, {"code": "HU", "name": "Hungary", "value": 20813492499.0}, {"code": "AT", "name": "Austria", "value": 11885836827.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest import</div>
    <div class="text-2xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">€38,172,904,447</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest import</div>
  <div class="text-2xl font-semibold mt-1">MT · Malta</div>
  <div class="opacity-80 mt-1">€598,366,465</div>
</div>
</div>
---
id: "chapter-exports"
layout: "centered-section-divider"
agent_notes:
  - "Centered section-divider slide for the chapter intro."
---
# Chapter 2 — Exports

This chapter ranks the top EU exporters in each SITC energy category and calls out the highest and lowest non-zero exporter in the same scope.
---
id: "exports-32"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '32%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Exports — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 26801396764.0}, {"code": "PL", "name": "Poland", "value": 16148791618.0}, {"code": "DE", "name": "Germany", "value": 4193826877.0}, {"code": "CZ", "name": "Czechia", "value": 2847873028.0}, {"code": "BE", "name": "Belgium", "value": 2754284679.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest export</div>
    <div class="text-2xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">€26,801,396,764</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest export</div>
  <div class="text-2xl font-semibold mt-1">MT · Malta</div>
  <div class="opacity-80 mt-1">€3,226</div>
</div>
</div>
---
id: "exports-33"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '33%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Exports — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 447756320684.0}, {"code": "BE", "name": "Belgium", "value": 209341289530.0}, {"code": "DE", "name": "Germany", "value": 128571414407.0}, {"code": "ES", "name": "Spain", "value": 119232715145.0}, {"code": "IT", "name": "Italy", "value": 104967581083.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest export</div>
    <div class="text-2xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">€447,756,320,684</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest export</div>
  <div class="text-2xl font-semibold mt-1">LU · Luxembourg</div>
  <div class="opacity-80 mt-1">€32,622,896</div>
</div>
</div>
---
id: "exports-34"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '34%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Exports — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "BE", "name": "Belgium", "value": 96150207408.0}, {"code": "FR", "name": "France", "value": 33666025300.0}, {"code": "DE", "name": "Germany", "value": 22099766028.0}, {"code": "HU", "name": "Hungary", "value": 8038153204.0}, {"code": "NL", "name": "Netherlands", "value": 7513309971.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest export</div>
    <div class="text-2xl font-semibold mt-1">BE · Belgium</div>
    <div class="opacity-80 mt-1">€96,150,207,408</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest export</div>
  <div class="text-2xl font-semibold mt-1">CY · Cyprus</div>
  <div class="opacity-80 mt-1">€125</div>
</div>
</div>
---
id: "exports-35"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '35%'"
  - "The chart component uses the default Chart.js color handling without any external colorscheme plugin."
---
# Exports — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 41086930356.0}, {"code": "FR", "name": "France", "value": 33544824653.0}, {"code": "ES", "name": "Spain", "value": 16206633461.0}, {"code": "AT", "name": "Austria", "value": 15208614527.0}, {"code": "CZ", "name": "Czechia", "value": 13577711310.0}]' label="VALUE_EUR" />

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
    <div class="text-xs uppercase tracking-[0.18em] opacity-60">Highest export</div>
    <div class="text-2xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">€41,086,930,356</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.18em] opacity-60">Lowest export</div>
  <div class="text-2xl font-semibold mt-1">MT · Malta</div>
  <div class="opacity-80 mt-1">€8,614,478</div>
</div>
</div>
---
id: "chapter-hungary"
layout: "centered-section-divider"
agent_notes:
  - "Centered section-divider slide for the chapter intro."
---
# Chapter 3 — Hungary

This chapter tracks Hungary’s yearly imports and exports in each SITC energy category and compares them with EU-27 averages.
---
id: "hungary-32"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses fixed colors from brewer.Paired12 directly to preserve import/export semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [208916550.0, 325566829.0, 136583601.0, 67939996.0, 32067736.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [133712108.0, 72045196.0, 42048690.0, 51330555.0, 8092636.0], "color": "#33a02c", "dashed": false}, {"label": "EU-27 avg imports", "values": [721639891.3333334, 1999483936.2592592, 1114942884.074074, 746473437.2222222, 564445036.2592592], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [311385750.8518519, 753989514.7692307, 557681739.7692307, 393210995.84, 317770679.8076923], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved -84.7% from the first available year to the last, while exports moved -93.9% from the first available year to the last.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
- Most visible high points: import peak in 2022; export peak in 2021.
---
id: "hungary-33"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses fixed colors from brewer.Paired12 directly to preserve import/export semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [4269951986.0, 5835960397.0, 5311133454.0, 4926279494.0, 4423920005.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1338652588.0, 1904998626.0, 2109506471.0, 2187915309.0, 2238690881.0], "color": "#33a02c", "dashed": false}, {"label": "EU-27 avg imports", "values": [13981108764.925926, 23646371156.25926, 19510069004.88889, 18842285187.037037, 15835906069.0], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [7494086709.518518, 13192983317.037037, 11507746600.296297, 10893631381.592592, 9458694388.333334], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +3.6% from the first available year to the last, while exports moved +67.2% from the first available year to the last.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
- Most visible high points: import peak in 2022; export peak in 2025.
---
id: "hungary-34"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses fixed colors from brewer.Paired12 directly to preserve import/export semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [3833269749.0, 11258654431.0, 4419794742.0, 3535652836.0, 3892996388.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1834270923.0, 3096214118.0, 832916422.0, 796386935.0, 1478364806.0], "color": "#33a02c", "dashed": false}, {"label": "EU-27 avg imports", "values": [4334951725.555555, 14504595235.814816, 7287815684.111111, 4953865395.185185, 5345030216.777778], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [909121316.6538461, 3734889521.8, 1714617232.68, 1120179198.2307692, 1183001167.8461537], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +1.6% from the first available year to the last, while exports moved -19.4% from the first available year to the last.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
- Most visible high points: import peak in 2022; export peak in 2022.
---
id: "hungary-35"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses fixed colors from brewer.Paired12 directly to preserve import/export semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [3099536420.0, 7096492332.0, 3770458092.0, 3438594292.0, 3408411363.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1344646475.0, 3148635410.0, 1521298544.0, 1784783298.0, 2277454849.0], "color": "#33a02c", "dashed": false}, {"label": "EU-27 avg imports", "values": [1530781407.9166667, 3805043596.04, 1728976238.48, 1461176629.84, 1586990242.72], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [1386589582.8, 3046206786.6923075, 1646955113.2307692, 1349398610.3846154, 1423929497.3846154], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +10.0% from the first available year to the last, while exports moved +69.4% from the first available year to the last.
- Across the available years, Hungary stayed above the EU-27 average on imports and above it on exports.
- Most visible high points: import peak in 2022; export peak in 2022.
