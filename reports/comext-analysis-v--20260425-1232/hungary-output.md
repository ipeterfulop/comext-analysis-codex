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
