#!/usr/bin/env python3
"""Render one report section for the COMEXT Slidev deck."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PAIRED12 = [
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
    "#ffff99",
    "#b15928",
]

SITC_ORDER = ["32", "33", "34", "35"]
COUNTRY_NAMES = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "GR": "Greece",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MT": "Malta",
    "NL": "Netherlands",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle_json")
    parser.add_argument("section", choices=["requirements", "imports", "exports", "hungary"])
    parser.add_argument("output")
    parser.add_argument("--population-year", default="2024")
    return parser.parse_args()


def format_eur(value: float | int | None) -> str:
    if value is None:
        return "—"
    return f"€{int(round(value)):,}"


def format_eur_person(value: float | int | None) -> str:
    if value is None:
        return "—"
    return f"€{value:,.0f}/person"


def format_pct(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:+.1f}%"


def format_pp(value: float | int | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:+.1f} pp"


def format_population(value: int | float | None) -> str:
    if value is None:
        return "—"
    return f"{int(round(value)):,}"


def yaml_escape(value: str) -> str:
    return value.replace('"', '\\"')


def frontmatter(**fields: object) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - \"{yaml_escape(str(item))}\"")
        else:
            lines.append(f'{key}: "{yaml_escape(str(value))}"')
    lines.append("---")
    return "\n".join(lines)


def slide(fields: dict, body: str) -> str:
    body = body.strip("\n")
    return frontmatter(**fields) + "\n" + body + "\n"


def build_population_table(bundle: dict, population_year: str) -> str:
    populations = bundle["meta"].get("populations", {})
    rows = [
        f"| {code} | {COUNTRY_NAMES.get(code, code)} | {format_population(populations.get(code))} |"
        for code in bundle["meta"]["analyzed_countries"]
    ]
    return "\n".join(
        [
            "| Code | Country | Population (" + population_year + ") |",
            "| --- | --- | ---: |",
            *rows,
        ]
    )


def requirements_section(bundle: dict, population_year: str) -> str:
    meta = bundle["meta"]
    quality = meta["data_quality"]
    years = meta["years"]
    title = "COMEXT Energy Trade in the EU"
    subtitle = (
        f"Eurostat COMEXT ext_go_detail, energy-focused SITC 32/33/34/35 coverage, "
        f"{years[0]}–{years[-1]}"
    )
    population_table = build_population_table(bundle, population_year)
    body = [
        "---",
        "theme: neversink",
        f"title: {title}",
        "info: |",
        "  Eurostat COMEXT ext_go_detail energy-trade analysis.",
        "  Deck assembled from four explicit Codex subagent outputs.",
        "mdc: true",
        "transition: slide-left",
        "---",
        "",
        slide(
            {
                "id": "cover",
                "layout": "two-column",
                "agent_notes": [
                    "Opening slide of the deck.",
                    "Ground the title and subtitle in Eurostat COMEXT ext_go_detail.",
                ],
            },
            f"""
<div class="grid grid-cols-2 gap-16 h-full items-center">
  <div>
    <h1 class="text-5xl font-bold leading-tight">{title}</h1>
    <p class="text-xl opacity-80 mt-4">{subtitle}</p>
  </div>
  <div class="flex items-center justify-center">
    <div class="i-mdi-chart-line text-[22rem]" style="opacity: 0.05"></div>
  </div>
</div>
""",
        ),
        "",
        slide(
            {
                "id": "describe-the-data",
                "layout": "centered",
                "agent_notes": [
                    "Tone: light but direct, setting the stage rather than deep-diving.",
                    "Source of truth: docs/comext_investigation.md.",
                ],
            },
            """
# COMEXT dataset scope

Eurostat `ext_go_detail` from the official dissemination API, covering monthly international trade detail for 2021–2025. Downloading and unzipping were AI-assisted and executed in parallel through one subagent per year before the energy-only filtering and deck assembly.
""",
        ),
        "",
        slide(
            {
                "id": "population-context",
                "layout": "centered",
                "agent_notes": [
                    "This slide fulfills the per-capita requirement from Section 2.1.",
                    "Place it immediately after the dataset-description slide.",
                ],
            },
            f"""
# Population context

Country populations are shown up front so the trade totals in later slides can be interpreted with per-capita context rather than raw scale alone.

{population_table}
""",
        ),
        "",
        slide(
            {
                "id": "data-quality-aspects",
                "layout": "centered",
                "agent_notes": [
                    "Keep it an at-a-glance summary; do not profile every column.",
                    "Tone: light but direct.",
                    "Source of truth for the column list: docs/comext_investigation.md.",
                ],
            },
            f"""
# Data quality snapshot

SITC-scoped trade rows across the prepared 2021–2025 monthly files, summarized after filtering to energy and hydrocarbons.

| Aspect | Value |
| --- | --- |
| Total rows | {quality["filtered_rows"]:,} |
| Columns | {quality["column_count"]} (`REPORTER`, `PARTNER`, `PRODUCT_SITC`, `FLOW`, `PERIOD`, `VALUE_EUR`, `QUANTITY_KG`, ...) |
| Year coverage | {years[0]} – {years[-1]} |
| Distinct reporters | {quality["distinct_reporters"]} |
| Distinct products (`PRODUCT_SITC`) | {quality["distinct_products"]} |
| Missing `VALUE_EUR` | {quality["missing_value_pct"]:.2f}% |
| Missing `QUANTITY_KG` | {quality["missing_quantity_pct"]:.2f}% |
""",
        ),
        "",
        slide(
            {
                "id": "describe-the-analysis",
                "layout": "centered",
                "agent_notes": [
                    "Roadmap slide only; do not render chapter contents here.",
                ],
            },
            """
# Analysis roadmap

The rest of the deck moves through three chapters: imports, exports, and a Hungary deep-dive that tracks yearly import and export trends against the EU-27 average.
""",
        ),
    ]
    return "\n".join(body).strip() + "\n"


def chapter_intro(chapter_id: str, title: str, subtitle: str) -> str:
    return slide(
        {
            "id": chapter_id,
            "layout": "centered-section-divider",
            "agent_notes": ["Centered section-divider slide for the chapter intro."],
        },
        f"""
# {title}

{subtitle}
""",
    )


def ranking_slide(bundle: dict, section: str, flow_label: str, sitc: str) -> str:
    sitc_label = bundle["meta"]["sitc_categories"][sitc]
    data = bundle[section][sitc]
    note = (
        f"Top {min(5, data['count_nonzero'])} EU reporter countries, 2021–2025, by total VALUE_EUR"
        if data["count_nonzero"] < 5
        else "Top 5 EU reporter countries, 2021–2025, by total VALUE_EUR"
    )
    highest = data["highest"]
    lowest = data["lowest"]

    if section == "imports":
        per_capita = data["per_capita_top5"][0] if data["per_capita_top5"] else None
        change = data["change_2021_2025"]
        increase = change["largest_increase"]
        decrease = change["largest_decrease"]
        top_share = data["top5"][0].get("category_share_pct") if data["top5"] else None
        top_share_text = f"{top_share:.1f}%" if top_share is not None else "n/a"
        insight_html = f"""
<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Per-capita exposure</div>
    <div class="text-xl font-semibold mt-1">{per_capita["code"] if per_capita else "n/a"} · {per_capita["name"] if per_capita else "n/a"}</div>
    <div class="opacity-80 mt-1">{format_eur_person(per_capita["per_capita"] if per_capita else None)}</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">2021 to 2025 movement</div>
    <div class="text-xl font-semibold mt-1">Up: {increase["code"] if increase else "n/a"} / Down: {decrease["code"] if decrease else "n/a"}</div>
    <div class="opacity-80 mt-1">{format_eur(increase["absolute_change"] if increase else None)} · {format_pct(increase["pct_change"] if increase else None)}</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Category concentration</div>
    <div class="text-xl font-semibold mt-1">{highest["code"]} · {highest["name"]}</div>
    <div class="opacity-80 mt-1">{top_share_text} of its energy imports</div>
  </div>
</div>
""".strip()
    else:
        share = data["share_change_2021_2025"]
        gain = share["largest_gain"]
        stable = data["stable_exporter"]
        supplier = data["net_supplier"]
        stable_cv = f"{stable['coefficient_of_variation'] * 100:.1f}%" if stable else "n/a"
        insight_html = f"""
<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">EU share shift</div>
    <div class="text-xl font-semibold mt-1">{gain["code"] if gain else "n/a"} · {gain["name"] if gain else "n/a"}</div>
    <div class="opacity-80 mt-1">{format_pp(gain["delta_pp"] if gain else None)} from 2021 to 2025</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Stable exporter</div>
    <div class="text-xl font-semibold mt-1">{stable["code"] if stable else "n/a"} · {stable["name"] if stable else "n/a"}</div>
    <div class="opacity-80 mt-1">CV {stable_cv} across yearly exports</div>
  </div>
  <div class="rounded-lg border border-neutral-300 px-4 py-3">
    <div class="text-xs uppercase tracking-[0.16em] opacity-60">Net supplier signal</div>
    <div class="text-xl font-semibold mt-1">{supplier["code"] if supplier else "none"} · {supplier["name"] if supplier else "net import market"}</div>
    <div class="opacity-80 mt-1">{format_eur(supplier["net_value"] if supplier else None)} export surplus</div>
  </div>
</div>
""".strip()

    chart_items = json.dumps(data["top5"])
    return slide(
        {
            "id": f"{section}-{sitc}",
            "layout": "default",
            "agent_notes": [
                (
                    f"Data comes from extracted monthly CSV-formatted .dat files under "
                    f"data/comext_raw_2021..2025/, filtered to PRODUCT_SITC LIKE '{sitc}%'"
                ),
                "The chart component applies the Chart.js default color palette directly and uses no external colorscheme plugin.",
            ],
        },
        f"""
# {flow_label.title()}s — SITC {sitc} · {sitc_label}

<div class="text-sm opacity-70 -mt-2 mb-3">{note}</div>

<BarRanking :items='{chart_items}' label="VALUE_EUR" />

{insight_html}
""",
    )


def imports_section(bundle: dict) -> str:
    parts = [
        chapter_intro(
            "chapter-imports",
            "Chapter 1 — Imports",
            "This chapter reads energy imports through absolute scale, per-capita exposure, category concentration, and 2021-to-2025 movement.",
        )
    ]
    for sitc in SITC_ORDER:
        parts.append(ranking_slide(bundle, "imports", "import", sitc))
    return "\n".join(part.strip() for part in parts) + "\n"


def exports_section(bundle: dict) -> str:
    parts = [
        chapter_intro(
            "chapter-exports",
            "Chapter 2 — Exports",
            "This chapter reads energy exports through scale, EU share shifts, trend stability, and net supplier signals.",
        )
    ]
    for sitc in SITC_ORDER:
        parts.append(ranking_slide(bundle, "exports", "export", sitc))
    return "\n".join(part.strip() for part in parts) + "\n"


def change_text(values: list[float | None]) -> str:
    present = [(idx, value) for idx, value in enumerate(values) if value is not None]
    if len(present) < 2:
        return "not enough data for a start-to-end comparison"
    first = present[0][1]
    last = present[-1][1]
    if not first:
        return "starts from zero, so percentage change is not meaningful"
    return f"{((last - first) / first) * 100:+.1f}% from the first available year to the last"


def peak_year(years: list[int], values: list[float | None]) -> int | None:
    present = [(year, value) for year, value in zip(years, values) if value is not None]
    if not present:
        return None
    return max(present, key=lambda item: item[1])[0]


def mean_present(values: list[float | None]) -> float | None:
    present = [value for value in values if value is not None]
    if not present:
        return None
    return sum(present) / len(present)


def hungary_commentary(payload: dict) -> list[str]:
    years = payload["years"]
    hu_imports = payload["hu_imports"]
    hu_exports = payload["hu_exports"]
    eu_imports = payload["eu_avg_imports"]
    eu_exports = payload["eu_avg_exports"]

    import_mean = mean_present(hu_imports)
    export_mean = mean_present(hu_exports)
    eu_import_mean = mean_present(eu_imports)
    eu_export_mean = mean_present(eu_exports)

    import_position = (
        "above" if import_mean is not None and eu_import_mean is not None and import_mean > eu_import_mean else "below"
    )
    export_position = (
        "above" if export_mean is not None and eu_export_mean is not None and export_mean > eu_export_mean else "below"
    )

    bullets = [
        f"Hungary imports moved {change_text(hu_imports)}, while exports moved {change_text(hu_exports)}.",
        f"The 2025 trade balance is {format_eur(payload['hu_balance'][-1])}, where negative values indicate net import exposure.",
        f"Across the available years, Hungary stayed {import_position} the EU-27 average on imports and {export_position} it on exports.",
    ]

    peaks = []
    import_peak = peak_year(years, hu_imports)
    export_peak = peak_year(years, hu_exports)
    if import_peak is not None:
        peaks.append(f"import peak in {import_peak}")
    if export_peak is not None:
        peaks.append(f"export peak in {export_peak}")
    if peaks:
        bullets.append("Most visible high points: " + "; ".join(peaks) + ".")
    return bullets[:3]


def hungary_slide(bundle: dict, sitc: str) -> str:
    sitc_label = bundle["meta"]["sitc_categories"][sitc]
    payload = bundle["hungary"][sitc]
    hu_imports = payload["hu_imports"]
    hu_exports = payload["hu_exports"]
    no_hu_trade = all(value is None for value in hu_imports) and all(value is None for value in hu_exports)

    if no_hu_trade:
        chart_block = f"<p class='text-lg opacity-75'>No Hungarian trade was recorded for SITC {sitc} in the prepared 2021–2025 files.</p>"
    else:
        chart_block = (
            "<TrendLines :years='"
            + json.dumps(payload["years"])
            + "' :series='"
            + json.dumps(
                [
                    {
                        "label": "HU imports",
                        "values": hu_imports,
                        "color": PAIRED12[1],
                        "dashed": False,
                    },
                    {
                        "label": "HU exports",
                        "values": hu_exports,
                        "color": PAIRED12[3],
                        "dashed": False,
                    },
                    {
                        "label": "HU balance",
                        "values": payload["hu_balance"],
                        "color": PAIRED12[5],
                        "dashed": False,
                    },
                    {
                        "label": "EU-27 avg imports",
                        "values": payload["eu_avg_imports"],
                        "color": PAIRED12[0],
                        "dashed": True,
                    },
                    {
                        "label": "EU-27 avg exports",
                        "values": payload["eu_avg_exports"],
                        "color": PAIRED12[2],
                        "dashed": True,
                    },
                ]
            )
            + "' />"
        )

    bullets = "\n".join(f"- {item}" for item in hungary_commentary(payload))
    return slide(
        {
            "id": f"hungary-{sitc}",
            "layout": "default",
            "agent_notes": [
                "Hungary lines are solid and EU-average lines are dashed.",
                "The line chart uses explicit Chart.js colors to preserve import/export/balance semantics.",
                "Missing Hungarian years render as gaps because absent yearly aggregates are stored as null in the analysis bundle.",
            ],
        },
        f"""
# Hungary — SITC {sitc} · {sitc_label}

<div class="text-sm opacity-70 -mt-2 mb-3">Imports vs. exports, 2021–2025, with EU-27 average</div>

{chart_block}

{bullets}
""",
    )


def hungary_summary_slide(bundle: dict) -> str:
    rows = []
    summary = bundle["hungary"]["summary"]
    vulnerability = max(
        [row for row in summary if row["import_per_capita_2025"] is not None],
        key=lambda row: row["import_per_capita_2025"],
        default=None,
    )
    for row in summary:
        rows.append(
            "| "
            + " | ".join(
                [
                    f"SITC {row['sitc']}",
                    row["label"],
                    format_eur(row["import_2025"]),
                    format_eur(row["export_2025"]),
                    format_eur(row["balance_2025"]),
                    format_eur_person(row["import_per_capita_2025"]),
                    format_pct(row["import_vs_eu_avg_2025_pct"]),
                ]
            )
            + " |"
        )

    vulnerability_text = (
        f"Highest 2025 per-capita import exposure: SITC {vulnerability['sitc']} · {vulnerability['label']} "
        f"at {format_eur_person(vulnerability['import_per_capita_2025'])}."
        if vulnerability
        else "No Hungary per-capita import exposure could be computed."
    )

    return slide(
        {
            "id": "hungary-scorecard",
            "layout": "default",
            "agent_notes": [
                "Hungary scorecard summarizes 2025 imports, exports, balance, per-capita exposure, and EU-average position.",
            ],
        },
        f"""
# Hungary risk scorecard

<div class="text-sm opacity-70 -mt-2 mb-3">2025 category snapshot before the SITC trend slides</div>

| Category | Label | Imports | Exports | Balance | Import exposure | vs EU avg imports |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
{chr(10).join(rows)}

<div class="mt-5 rounded-lg border border-neutral-300 px-5 py-4">
  <div class="text-xs uppercase tracking-[0.16em] opacity-60">Primary vulnerability signal</div>
  <div class="text-xl font-semibold mt-1">{vulnerability_text}</div>
</div>
""",
    )


def hungary_section(bundle: dict) -> str:
    parts = [
        chapter_intro(
            "chapter-hungary",
            "Chapter 3 — Hungary",
            "This chapter starts with Hungary’s energy-trade risk scorecard, then tracks each SITC category against EU-27 benchmarks.",
        )
    ]
    parts.append(hungary_summary_slide(bundle))
    for sitc in SITC_ORDER:
        parts.append(hungary_slide(bundle, sitc))
    return "\n".join(part.strip() for part in parts) + "\n"


def main() -> None:
    args = parse_args()
    bundle = json.loads(Path(args.bundle_json).read_text(encoding="utf-8"))

    if args.section == "requirements":
        content = requirements_section(bundle, args.population_year)
    elif args.section == "imports":
        content = imports_section(bundle)
    elif args.section == "exports":
        content = exports_section(bundle)
    else:
        content = hungary_section(bundle)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
