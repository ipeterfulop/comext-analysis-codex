#!/usr/bin/env python3
"""Merge per-month aggregates and emit the analysis bundle for the Slidev deck."""

from __future__ import annotations

import argparse
import glob
import json
import math
from collections import defaultdict
from pathlib import Path


AGG_CODES = {
    "EU27_2020",
    "EU28",
    "EU27",
    "EU",
    "EXT_EU27_2020",
    "EXT_EU28",
    "EXT_EU27",
    "EU27_2020_EXTRA",
    "EU27_2020_INTRA",
    "EU28_EXTRA",
    "EU28_INTRA",
    "EA",
    "EA19",
    "EA20",
    "EFTA",
    "WORLD",
    "TOTAL",
    "EXTRA_EU",
    "INTRA_EU",
    "XX",
}

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

SITC = {
    "32": "Coal, coke and briquettes",
    "33": "Petroleum, petroleum products and related materials",
    "34": "Gas, natural and manufactured",
    "35": "Electric current",
}

YEARS = [2021, 2022, 2023, 2024, 2025]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agg-dir", default="/tmp/comext_agg")
    parser.add_argument("--stats-dir", default="/tmp/comext_stats")
    parser.add_argument("--population-json")
    parser.add_argument("out", nargs="?", default="/tmp/comext_slide_data.json")
    return parser.parse_args()


def load_stats(stats_dir: str) -> dict:
    merged = {
        "filtered_rows": 0,
        "missing_value": 0,
        "missing_quantity": 0,
        "column_count": 0,
        "column_names": [],
        "reporters": set(),
        "products": set(),
    }

    for path in sorted(glob.glob(f"{stats_dir}/*.tsv")):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                key, value = line.rstrip("\n").split("\t", 1)
                if key in {"filtered_rows", "missing_value", "missing_quantity", "column_count"}:
                    merged[key] += int(value or 0)
                elif key == "column_names" and value:
                    if not merged["column_names"]:
                        merged["column_names"] = value.split(",")
                elif key == "reporters" and value:
                    merged["reporters"].update(part for part in value.split(",") if part)
                elif key == "products" and value:
                    merged["products"].update(part for part in value.split(",") if part)

    if merged["column_count"] and glob.glob(f"{stats_dir}/*.tsv"):
        merged["column_count"] = int(merged["column_count"] / len(glob.glob(f'{stats_dir}/*.tsv')))

    return merged


def load_populations(path: str | None) -> dict:
    if not path:
        return {}
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def metric_item(
    code: str,
    value: float,
    populations: dict | None = None,
    energy_totals: dict | None = None,
) -> dict:
    population = populations.get(code) if populations else None
    energy_total = energy_totals.get(code, {}).get("val", 0.0) if energy_totals else 0.0
    return {
        "code": code,
        "name": COUNTRY_NAMES.get(code, code),
        "value": value,
        "per_capita": (value / population) if population else None,
        "category_share_pct": ((value / energy_total) * 100) if energy_total else None,
    }


def ranking_payload(totals: dict, populations: dict | None = None, energy_totals: dict | None = None) -> dict:
    items = [(reporter, values["val"]) for reporter, values in totals.items()]
    positive = [item for item in items if item[1] > 0]
    positive.sort(key=lambda item: item[1], reverse=True)
    top5 = positive[:5]
    highest = positive[0] if positive else None
    lowest = min(positive, key=lambda item: item[1]) if positive else None
    per_capita = [
        metric_item(code, value, populations, energy_totals)
        for code, value in positive
        if populations and populations.get(code)
    ]
    per_capita.sort(key=lambda item: item["per_capita"] or 0, reverse=True)
    return {
        "top5": [metric_item(code, value, populations, energy_totals) for code, value in top5],
        "per_capita_top5": per_capita[:5],
        "highest": {
            "code": highest[0],
            "name": COUNTRY_NAMES.get(highest[0], highest[0]),
            "value": highest[1],
        }
        if highest
        else None,
        "lowest": {
            "code": lowest[0],
            "name": COUNTRY_NAMES.get(lowest[0], lowest[0]),
            "value": lowest[1],
        }
        if lowest
        else None,
        "count_nonzero": len(positive),
    }


def change_payload(yearly: dict, populations: dict, start_year: int, end_year: int) -> dict:
    rows = []
    for code in COUNTRY_NAMES:
        start = yearly.get((code, start_year), {}).get("val", 0.0)
        end = yearly.get((code, end_year), {}).get("val", 0.0)
        if start <= 0 and end <= 0:
            continue
        pct = ((end - start) / start) * 100 if start > 0 else None
        population = populations.get(code)
        rows.append(
            {
                "code": code,
                "name": COUNTRY_NAMES.get(code, code),
                "start_value": start,
                "end_value": end,
                "absolute_change": end - start,
                "pct_change": pct,
                "end_per_capita": (end / population) if population else None,
            }
        )

    increases = sorted(rows, key=lambda item: item["absolute_change"], reverse=True)
    decreases = sorted(rows, key=lambda item: item["absolute_change"])
    return {
        "largest_increase": increases[0] if increases else None,
        "largest_decrease": decreases[0] if decreases else None,
    }


def share_change_payload(yearly: dict, start_year: int, end_year: int) -> dict:
    start_total = sum(values["val"] for (code, year), values in yearly.items() if year == start_year and code in COUNTRY_NAMES)
    end_total = sum(values["val"] for (code, year), values in yearly.items() if year == end_year and code in COUNTRY_NAMES)
    rows = []
    if start_total <= 0 or end_total <= 0:
        return {"largest_gain": None, "largest_loss": None}

    for code in COUNTRY_NAMES:
        start = yearly.get((code, start_year), {}).get("val", 0.0)
        end = yearly.get((code, end_year), {}).get("val", 0.0)
        start_share = (start / start_total) * 100
        end_share = (end / end_total) * 100
        rows.append(
            {
                "code": code,
                "name": COUNTRY_NAMES.get(code, code),
                "start_share_pct": start_share,
                "end_share_pct": end_share,
                "delta_pp": end_share - start_share,
            }
        )

    rows.sort(key=lambda item: item["delta_pp"], reverse=True)
    return {
        "largest_gain": rows[0] if rows else None,
        "largest_loss": rows[-1] if rows else None,
    }


def stability_payload(yearly: dict, ranking: dict) -> dict | None:
    candidates = [item["code"] for item in ranking["top5"]]
    rows = []
    for code in candidates:
        values = [yearly.get((code, year), {}).get("val", 0.0) for year in YEARS]
        mean = sum(values) / len(values)
        if mean <= 0:
            continue
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        rows.append(
            {
                "code": code,
                "name": COUNTRY_NAMES.get(code, code),
                "coefficient_of_variation": math.sqrt(variance) / mean,
                "mean_value": mean,
            }
        )
    rows.sort(key=lambda item: item["coefficient_of_variation"])
    return rows[0] if rows else None


def net_supplier_payload(import_totals: dict, export_totals: dict) -> dict | None:
    rows = []
    for code in COUNTRY_NAMES:
        imports = import_totals.get(code, {}).get("val", 0.0)
        exports = export_totals.get(code, {}).get("val", 0.0)
        rows.append(
            {
                "code": code,
                "name": COUNTRY_NAMES.get(code, code),
                "net_value": exports - imports,
                "imports": imports,
                "exports": exports,
            }
        )
    positives = [row for row in rows if row["net_value"] > 0]
    positives.sort(key=lambda item: item["net_value"], reverse=True)
    return positives[0] if positives else None


def main() -> None:
    args = parse_args()
    populations = load_populations(args.population_json)

    data = defaultdict(lambda: {"val": 0.0, "qty": 0.0, "rows": 0})
    filtered_rows = 0
    for path in sorted(glob.glob(f"{args.agg_dir}/*.tsv")):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                reporter, flow, cat, year, value, qty, rows = line.rstrip("\n").split("\t")
                key = (reporter, flow, cat, int(year))
                data[key]["val"] += float(value)
                data[key]["qty"] += float(qty)
                data[key]["rows"] += int(rows)
                filtered_rows += int(rows)

    stats = load_stats(args.stats_dir)

    def by_country_total(flow: str, cat: str) -> dict:
        acc = defaultdict(lambda: {"val": 0.0, "qty": 0.0})
        for (reporter, current_flow, current_cat, _year), values in data.items():
            if current_flow != flow or current_cat != cat:
                continue
            if reporter in AGG_CODES or reporter not in COUNTRY_NAMES:
                continue
            acc[reporter]["val"] += values["val"]
            acc[reporter]["qty"] += values["qty"]
        return acc

    def by_country_total_all_energy(flow: str) -> dict:
        acc = defaultdict(lambda: {"val": 0.0, "qty": 0.0})
        for (reporter, current_flow, _cat, _year), values in data.items():
            if current_flow != flow:
                continue
            if reporter in AGG_CODES or reporter not in COUNTRY_NAMES:
                continue
            acc[reporter]["val"] += values["val"]
            acc[reporter]["qty"] += values["qty"]
        return acc

    def by_country_year(flow: str, cat: str) -> dict:
        acc = defaultdict(lambda: {"val": 0.0, "qty": 0.0})
        for (reporter, current_flow, current_cat, year), values in data.items():
            if current_flow != flow or current_cat != cat:
                continue
            if reporter in AGG_CODES or reporter not in COUNTRY_NAMES:
                continue
            acc[(reporter, year)]["val"] += values["val"]
            acc[(reporter, year)]["qty"] += values["qty"]
        return acc

    analyzed_countries = sorted(
        reporter
        for reporter in stats["reporters"]
        if reporter in COUNTRY_NAMES and reporter not in AGG_CODES
    )

    bundle = {
        "meta": {
            "dataset": "ext_go_detail",
            "source": "Eurostat COMEXT",
            "years": YEARS,
            "sitc_categories": SITC,
            "country_names": COUNTRY_NAMES,
            "analyzed_countries": analyzed_countries,
            "populations": populations,
            "filtered_detail_rows": filtered_rows,
            "data_quality": {
                "filtered_rows": stats["filtered_rows"],
                "column_count": stats["column_count"],
                "column_names": stats["column_names"],
                "distinct_reporters": len(
                    [r for r in stats["reporters"] if r in COUNTRY_NAMES and r not in AGG_CODES]
                ),
                "distinct_products": len(stats["products"]),
                "missing_value_pct": (
                    (stats["missing_value"] / stats["filtered_rows"]) * 100
                    if stats["filtered_rows"]
                    else 0.0
                ),
                "missing_quantity_pct": (
                    (stats["missing_quantity"] / stats["filtered_rows"]) * 100
                    if stats["filtered_rows"]
                    else 0.0
                ),
            },
        },
        "imports": {},
        "exports": {},
        "hungary": {},
    }

    total_imports = by_country_total_all_energy("1")
    total_exports = by_country_total_all_energy("2")

    for cat in SITC:
        import_totals = by_country_total("1", cat)
        export_totals = by_country_total("2", cat)
        import_year = by_country_year("1", cat)
        export_year = by_country_year("2", cat)

        import_ranking = ranking_payload(import_totals, populations, total_imports)
        export_ranking = ranking_payload(export_totals, populations, total_exports)
        bundle["imports"][cat] = {
            **import_ranking,
            "change_2021_2025": change_payload(import_year, populations, YEARS[0], YEARS[-1]),
        }
        bundle["exports"][cat] = {
            **export_ranking,
            "share_change_2021_2025": share_change_payload(export_year, YEARS[0], YEARS[-1]),
            "stable_exporter": stability_payload(export_year, export_ranking),
            "net_supplier": net_supplier_payload(import_totals, export_totals),
        }

        hu_imports = {
            year: (import_year[("HU", year)]["val"] if ("HU", year) in import_year else None)
            for year in YEARS
        }
        hu_exports = {
            year: (export_year[("HU", year)]["val"] if ("HU", year) in export_year else None)
            for year in YEARS
        }

        def eu_avg(by_year: dict) -> dict:
            averages = {}
            for year in YEARS:
                values = [entry["val"] for (reporter, current_year), entry in by_year.items() if current_year == year]
                averages[year] = (sum(values) / len(values)) if values else 0.0
            return averages

        eu_avg_imports = eu_avg(import_year)
        eu_avg_exports = eu_avg(export_year)

        bundle["hungary"][cat] = {
            "years": YEARS,
            "hu_imports": [hu_imports[year] for year in YEARS],
            "hu_exports": [hu_exports[year] for year in YEARS],
            "hu_balance": [
                (
                    (hu_exports[year] or 0.0) - (hu_imports[year] or 0.0)
                    if hu_imports[year] is not None or hu_exports[year] is not None
                    else None
                )
                for year in YEARS
            ],
            "eu_avg_imports": [eu_avg_imports[year] for year in YEARS],
            "eu_avg_exports": [eu_avg_exports[year] for year in YEARS],
        }

    population_hu = populations.get("HU")
    bundle["hungary"]["summary"] = []
    for cat in SITC:
        payload = bundle["hungary"][cat]
        import_2025 = payload["hu_imports"][-1]
        export_2025 = payload["hu_exports"][-1]
        balance_2025 = payload["hu_balance"][-1]
        eu_import_2025 = payload["eu_avg_imports"][-1]
        bundle["hungary"]["summary"].append(
            {
                "sitc": cat,
                "label": SITC[cat],
                "import_2025": import_2025,
                "export_2025": export_2025,
                "balance_2025": balance_2025,
                "import_per_capita_2025": (import_2025 / population_hu) if import_2025 is not None and population_hu else None,
                "import_vs_eu_avg_2025_pct": (
                    ((import_2025 - eu_import_2025) / eu_import_2025) * 100
                    if import_2025 is not None and eu_import_2025
                    else None
                ),
            }
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(bundle, handle, indent=2)

    print(f"Wrote {out_path}")
    print(f"Filtered detail rows: {filtered_rows:,}")


if __name__ == "__main__":
    main()
