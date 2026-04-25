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

This chapter reads energy imports through absolute scale, per-capita exposure, category concentration, and 2021-to-2025 movement.
---
id: "imports-32"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '32%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Imports — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 36822338579.0, "per_capita": 440.89847605493196, "category_share_pct": 6.015576566408573}, {"code": "NL", "name": "Netherlands", "value": 31155185388.0, "per_capita": 1731.4703287328718, "category_share_pct": 5.405444978765854}, {"code": "PL", "name": "Poland", "value": 12858743207.0, "per_capita": 351.723549752808, "category_share_pct": 9.56823651650669}, {"code": "FR", "name": "France", "value": 9765978129.0, "per_capita": 142.4615994161366, "category_share_pct": 2.208194124575334}, {"code": "IT", "name": "Italy", "value": 9284202838.0, "per_capita": 157.48561487527357, "category_share_pct": 2.176525040812332}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Per-capita exposure</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">€1,731/person</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">2021 to 2025 movement</div>
    <div class="text-xl font-semibold mt-1">Up: BE / Down: DE</div>
    <div class="opacity-80 mt-1">€349,107,218 · +44.9%</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Category concentration</div>
    <div class="text-xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">6.0% of its energy imports</div>
  </div>
</div>
---
id: "imports-33"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '33%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Imports — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 458897949220.0, "per_capita": 25503.56138457892, "category_share_pct": 79.61909340243008}, {"code": "DE", "name": "Germany", "value": 356083093489.0, "per_capita": 4263.620924874174, "category_share_pct": 58.17243541691626}, {"code": "FR", "name": "France", "value": 264641729152.0, "per_capita": 3860.4718860973344, "category_share_pct": 59.8383801101899}, {"code": "BE", "name": "Belgium", "value": 255665213774.0, "per_capita": 21559.458804531052, "category_share_pct": 62.09673554221635}, {"code": "ES", "name": "Spain", "value": 224028891100.0, "per_capita": 4586.166039971471, "category_share_pct": 71.73257644538853}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Per-capita exposure</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">€25,504/person</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">2021 to 2025 movement</div>
    <div class="text-xl font-semibold mt-1">Up: NL / Down: GR</div>
    <div class="opacity-80 mt-1">€9,783,279,389 · +13.7%</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Category concentration</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">79.6% of its energy imports</div>
  </div>
</div>
---
id: "imports-34"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '34%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Imports — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 181038194170.0, "per_capita": 2167.6913253633325, "category_share_pct": 29.575772764608395}, {"code": "IT", "name": "Italy", "value": 168018998273.0, "per_capita": 2850.0643205950314, "category_share_pct": 39.38922527377341}, {"code": "FR", "name": "France", "value": 144002259907.0, "per_capita": 2100.638768068802, "category_share_pct": 32.560480891100255}, {"code": "BE", "name": "Belgium", "value": 138042294967.0, "per_capita": 11640.680903326782, "category_share_pct": 33.52812749795433}, {"code": "NL", "name": "Netherlands", "value": 80777618825.0, "per_capita": 4489.27035674301, "category_share_pct": 14.014969535133565}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Per-capita exposure</div>
    <div class="text-xl font-semibold mt-1">BE · Belgium</div>
    <div class="opacity-80 mt-1">€11,641/person</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">2021 to 2025 movement</div>
    <div class="text-xl font-semibold mt-1">Up: FR / Down: AT</div>
    <div class="opacity-80 mt-1">€18,237,510,770 · +1175.5%</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Category concentration</div>
    <div class="text-xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">29.6% of its energy imports</div>
  </div>
</div>
---
id: "imports-35"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '35%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Imports — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 38172904447.0, "per_capita": 457.0697040646761, "category_share_pct": 6.2362152520667795}, {"code": "IT", "name": "Italy", "value": 37195907331.0, "per_capita": 630.9448898391497, "category_share_pct": 8.71995422054958}, {"code": "FR", "name": "France", "value": 23850883899.0, "per_capita": 347.92572979968844, "category_share_pct": 5.392944874134504}, {"code": "HU", "name": "Hungary", "value": 20813492499.0, "per_capita": 2176.6733962799876, "category_share_pct": 28.397971382761515}, {"code": "AT", "name": "Austria", "value": 11885836827.0, "per_capita": 1295.0381496716816, "category_share_pct": 13.846592183459395}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Per-capita exposure</div>
    <div class="text-xl font-semibold mt-1">SI · Slovenia</div>
    <div class="opacity-80 mt-1">€2,930/person</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">2021 to 2025 movement</div>
    <div class="text-xl font-semibold mt-1">Up: DE / Down: FR</div>
    <div class="opacity-80 mt-1">€2,778,446,344 · +58.0%</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Category concentration</div>
    <div class="text-xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">6.2% of its energy imports</div>
  </div>
</div>
---
id: "chapter-exports"
layout: "centered-section-divider"
agent_notes:
  - "Centered section-divider slide for the chapter intro."
---
# Chapter 2 — Exports

This chapter reads energy exports through scale, EU share shifts, trend stability, and net supplier signals.
---
id: "exports-32"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '32%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Exports — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 26801396764.0, "per_capita": 1489.5056051676481, "category_share_pct": 5.516214750356097}, {"code": "PL", "name": "Poland", "value": 16148791618.0, "per_capita": 441.71582095280826, "category_share_pct": 33.49527681821007}, {"code": "DE", "name": "Germany", "value": 4193826877.0, "per_capita": 50.21549283026907, "category_share_pct": 2.1402324094929703}, {"code": "CZ", "name": "Czechia", "value": 2847873028.0, "per_capita": 261.1522893843097, "category_share_pct": 11.045258330273871}, {"code": "BE", "name": "Belgium", "value": 2754284679.0, "per_capita": 232.2603305952384, "category_share_pct": 0.8592069359157071}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">EU share shift</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">+2.2 pp from 2021 to 2025</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Stable exporter</div>
    <div class="text-xl font-semibold mt-1">DE · Germany</div>
    <div class="opacity-80 mt-1">CV 18.4% across yearly exports</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Net supplier signal</div>
    <div class="text-xl font-semibold mt-1">PL · Poland</div>
    <div class="opacity-80 mt-1">€3,290,048,411 export surplus</div>
  </div>
</div>
---
id: "exports-33"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '33%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Exports — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "NL", "name": "Netherlands", "value": 447756320684.0, "per_capita": 24884.357904208107, "category_share_pct": 92.15639179074}, {"code": "BE", "name": "Belgium", "value": 209341289530.0, "per_capita": 17653.105172528652, "category_share_pct": 65.30461041631281}, {"code": "DE", "name": "Germany", "value": 128571414407.0, "per_capita": 1539.4714964845368, "category_share_pct": 65.6137499517038}, {"code": "ES", "name": "Spain", "value": 119232715145.0, "per_capita": 2440.850491946175, "category_share_pct": 82.59738779516347}, {"code": "IT", "name": "Italy", "value": 104967581083.0, "per_capita": 1780.5388720252763, "category_share_pct": 91.0263916079252}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">EU share shift</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">+1.4 pp from 2021 to 2025</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Stable exporter</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">CV 18.7% across yearly exports</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Net supplier signal</div>
    <div class="text-xl font-semibold mt-1">none · net import market</div>
    <div class="opacity-80 mt-1">— export surplus</div>
  </div>
</div>
---
id: "exports-34"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '34%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Exports — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "BE", "name": "Belgium", "value": 96150207408.0, "per_capita": 8108.050387692992, "category_share_pct": 29.994330551438033}, {"code": "FR", "name": "France", "value": 33666025300.0, "per_capita": 491.1045004268533, "category_share_pct": 26.128524108781683}, {"code": "DE", "name": "Germany", "value": 22099766028.0, "per_capita": 264.6152726560577, "category_share_pct": 11.278156414785487}, {"code": "HU", "name": "Hungary", "value": 8038153204.0, "per_capita": 840.6294251294046, "category_share_pct": 28.50210348677252}, {"code": "NL", "name": "Netherlands", "value": 7513309971.0, "per_capita": 417.5572420239881, "category_share_pct": 1.546375797163574}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">EU share shift</div>
    <div class="text-xl font-semibold mt-1">FR · France</div>
    <div class="opacity-80 mt-1">+11.8 pp from 2021 to 2025</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Stable exporter</div>
    <div class="text-xl font-semibold mt-1">NL · Netherlands</div>
    <div class="opacity-80 mt-1">CV 7.9% across yearly exports</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Net supplier signal</div>
    <div class="text-xl font-semibold mt-1">DK · Denmark</div>
    <div class="opacity-80 mt-1">€1,698,225 export surplus</div>
  </div>
</div>
---
id: "exports-35"
layout: "default"
agent_notes:
  - "Data comes from extracted monthly CSV-formatted .dat files under data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '35%'"
  - "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin."
---
# Exports — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR</div>

<BarRanking :items='[{"code": "DE", "name": "Germany", "value": 41086930356.0, "per_capita": 491.9612843402269, "category_share_pct": 20.967861224017746}, {"code": "FR", "name": "France", "value": 33544824653.0, "per_capita": 489.33648110571454, "category_share_pct": 26.034459127872296}, {"code": "ES", "name": "Spain", "value": 16206633461.0, "per_capita": 331.77110164744954, "category_share_pct": 11.226999126912226}, {"code": "AT", "name": "Austria", "value": 15208614527.0, "per_capita": 1657.0760900380933, "category_share_pct": 50.94750997718334}, {"code": "CZ", "name": "Czechia", "value": 13577711310.0, "per_capita": 1245.0872487443407, "category_share_pct": 52.660117736411685}]' label="VALUE_EUR" />

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">EU share shift</div>
    <div class="text-xl font-semibold mt-1">RO · Romania</div>
    <div class="opacity-80 mt-1">+2.6 pp from 2021 to 2025</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Stable exporter</div>
    <div class="text-xl font-semibold mt-1">FR · France</div>
    <div class="opacity-80 mt-1">CV 14.4% across yearly exports</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Net supplier signal</div>
    <div class="text-xl font-semibold mt-1">FR · France</div>
    <div class="opacity-80 mt-1">€9,693,940,754 export surplus</div>
  </div>
</div>
---
id: "chapter-hungary"
layout: "centered-section-divider"
agent_notes:
  - "Centered section-divider slide for the chapter intro."
---
# Chapter 3 — Hungary

This chapter starts with Hungary’s energy-trade risk scorecard, then tracks each SITC category against EU-27 benchmarks.
---
id: "hungary-scorecard"
layout: "default"
agent_notes:
  - "Hungary scorecard summarizes 2025 imports, exports, balance, per-capita exposure, and EU-average position."
---
# Hungary risk scorecard

<div class="text-sm opacity-70 -mt-2 mb-3">2025 category snapshot before the SITC trend slides</div>

| Category | Label | Imports | Exports | Balance | Import exposure | vs EU avg imports |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| SITC 32 | Coal, coke and briquettes | €32,067,736 | €8,092,636 | €-23,975,100 | €3/person | -94.3% |
| SITC 33 | Petroleum, petroleum products and related materials | €4,423,920,005 | €2,238,690,881 | €-2,185,229,124 | €463/person | -72.1% |
| SITC 34 | Gas, natural and manufactured | €3,892,996,388 | €1,478,364,806 | €-2,414,631,582 | €407/person | -27.2% |
| SITC 35 | Electric current | €3,408,411,363 | €2,277,454,849 | €-1,130,956,514 | €356/person | +114.8% |

<div class="mt-5 rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.16em] opacity-60">Primary vulnerability signal</div>
  <div class="text-xl font-semibold mt-1">Highest 2025 per-capita import exposure: SITC 33 · Petroleum, petroleum products and related materials at €463/person.</div>
</div>
---
id: "hungary-32"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses explicit Chart.js colors to preserve import/export/balance semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 32 · Coal, coke and briquettes

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [208916550.0, 325566829.0, 136583601.0, 67939996.0, 32067736.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [133712108.0, 72045196.0, 42048690.0, 51330555.0, 8092636.0], "color": "#33a02c", "dashed": false}, {"label": "HU balance", "values": [-75204442.0, -253521633.0, -94534911.0, -16609441.0, -23975100.0], "color": "#e31a1c", "dashed": false}, {"label": "EU-27 avg imports", "values": [721639891.3333334, 1999483936.2592592, 1114942884.074074, 746473437.2222222, 564445036.2592592], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [311385750.8518519, 753989514.7692307, 557681739.7692307, 393210995.84, 317770679.8076923], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved -84.7% from the first available year to the last, while exports moved -93.9% from the first available year to the last.
- The 2025 trade balance is €-23,975,100, where negative values indicate net import exposure.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
---
id: "hungary-33"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses explicit Chart.js colors to preserve import/export/balance semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 33 · Petroleum, petroleum products and related materials

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [4269951986.0, 5835960397.0, 5311133454.0, 4926279494.0, 4423920005.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1338652588.0, 1904998626.0, 2109506471.0, 2187915309.0, 2238690881.0], "color": "#33a02c", "dashed": false}, {"label": "HU balance", "values": [-2931299398.0, -3930961771.0, -3201626983.0, -2738364185.0, -2185229124.0], "color": "#e31a1c", "dashed": false}, {"label": "EU-27 avg imports", "values": [13981108764.925926, 23646371156.25926, 19510069004.88889, 18842285187.037037, 15835906069.0], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [7494086709.518518, 13192983317.037037, 11507746600.296297, 10893631381.592592, 9458694388.333334], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +3.6% from the first available year to the last, while exports moved +67.2% from the first available year to the last.
- The 2025 trade balance is €-2,185,229,124, where negative values indicate net import exposure.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
---
id: "hungary-34"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses explicit Chart.js colors to preserve import/export/balance semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 34 · Gas, natural and manufactured

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [3833269749.0, 11258654431.0, 4419794742.0, 3535652836.0, 3892996388.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1834270923.0, 3096214118.0, 832916422.0, 796386935.0, 1478364806.0], "color": "#33a02c", "dashed": false}, {"label": "HU balance", "values": [-1998998826.0, -8162440313.0, -3586878320.0, -2739265901.0, -2414631582.0], "color": "#e31a1c", "dashed": false}, {"label": "EU-27 avg imports", "values": [4334951725.555555, 14504595235.814816, 7287815684.111111, 4953865395.185185, 5345030216.777778], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [909121316.6538461, 3734889521.8, 1714617232.68, 1120179198.2307692, 1183001167.8461537], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +1.6% from the first available year to the last, while exports moved -19.4% from the first available year to the last.
- The 2025 trade balance is €-2,414,631,582, where negative values indicate net import exposure.
- Across the available years, Hungary stayed below the EU-27 average on imports and below it on exports.
---
id: "hungary-35"
layout: "default"
agent_notes:
  - "Hungary lines are solid and EU-average lines are dashed."
  - "The line chart uses explicit Chart.js colors to preserve import/export/balance semantics."
  - "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle."
---
# Hungary — SITC 35 · Electric current

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

<TrendLines :years='[2021, 2022, 2023, 2024, 2025]' :series='[{"label": "HU imports", "values": [3099536420.0, 7096492332.0, 3770458092.0, 3438594292.0, 3408411363.0], "color": "#1f78b4", "dashed": false}, {"label": "HU exports", "values": [1344646475.0, 3148635410.0, 1521298544.0, 1784783298.0, 2277454849.0], "color": "#33a02c", "dashed": false}, {"label": "HU balance", "values": [-1754889945.0, -3947856922.0, -2249159548.0, -1653810994.0, -1130956514.0], "color": "#e31a1c", "dashed": false}, {"label": "EU-27 avg imports", "values": [1530781407.9166667, 3805043596.04, 1728976238.48, 1461176629.84, 1586990242.72], "color": "#a6cee3", "dashed": true}, {"label": "EU-27 avg exports", "values": [1386589582.8, 3046206786.6923075, 1646955113.2307692, 1349398610.3846154, 1423929497.3846154], "color": "#b2df8a", "dashed": true}]' />

- Hungary imports moved +10.0% from the first available year to the last, while exports moved +69.4% from the first available year to the last.
- The 2025 trade balance is €-1,130,956,514, where negative values indicate net import exposure.
- Across the available years, Hungary stayed above the EU-27 average on imports and above it on exports.
