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
