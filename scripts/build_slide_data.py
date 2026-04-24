#!/usr/bin/env python3
"""Merge per-month aggregates and emit the analysis bundle for the Slidev deck."""

from __future__ import annotations

import argparse
import glob
import json
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


def ranking_payload(totals: dict) -> dict:
    items = [(reporter, values["val"]) for reporter, values in totals.items()]
    positive = [item for item in items if item[1] > 0]
    positive.sort(key=lambda item: item[1], reverse=True)
    top5 = positive[:5]
    highest = positive[0] if positive else None
    lowest = min(positive, key=lambda item: item[1]) if positive else None
    return {
        "top5": [
            {"code": code, "name": COUNTRY_NAMES.get(code, code), "value": value}
            for code, value in top5
        ],
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

    for cat in SITC:
        bundle["imports"][cat] = ranking_payload(by_country_total("1", cat))
        bundle["exports"][cat] = ranking_payload(by_country_total("2", cat))

        import_year = by_country_year("1", cat)
        export_year = by_country_year("2", cat)

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
            "eu_avg_imports": [eu_avg_imports[year] for year in YEARS],
            "eu_avg_exports": [eu_avg_exports[year] for year in YEARS],
        }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(bundle, handle, indent=2)

    print(f"Wrote {out_path}")
    print(f"Filtered detail rows: {filtered_rows:,}")


if __name__ == "__main__":
    main()
