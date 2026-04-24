#!/usr/bin/env bash
set -euo pipefail

if [ "${1:-}" = "" ]; then
  echo "Usage: $0 <year>"
  echo "Example: $0 2024"
  exit 1
fi

year="$1"

if ! [[ "$year" =~ ^[0-9]{4}$ ]]; then
  echo "Error: year must be a 4-digit number, got '$year'."
  exit 1
fi

target_dir="data/comext_raw_${year}"
mkdir -p "$target_dir"

total_months=12
current_month=0

for m in 01 02 03 04 05 06 07 08 09 10 11 12; do
  current_month=$((current_month + 1))
  url="https://ec.europa.eu/eurostat/api/dissemination/files?file=comext%2FCOMEXT_DATA%2FPRODUCTS%2Ffull_v2_${year}${m}.7z"
  echo "[${current_month}/${total_months}] Downloading ${year}${m}..."
  wget -c -P "$target_dir" "$url"
done