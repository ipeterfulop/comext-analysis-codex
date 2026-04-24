#!/usr/bin/env bash
# Aggregate one monthly COMEXT CSV file to per-(REPORTER,FLOW,SITC_CAT,YEAR) sums.
# Filter: PRODUCT_SITC starts with 32|33|34|35.
# Output:
#   - /tmp/comext_agg/<stem>.tsv
#   - /tmp/comext_stats/<stem>.tsv
# Columns out: REPORTER, FLOW, SITC_CAT, YEAR, SUM_VALUE_EUR, SUM_QUANTITY_KG, ROWS
set -euo pipefail
f="$1"
base=$(basename "$f")
stem="${base%.*}"
agg_dir="${COMEXT_AGG_DIR:-/tmp/comext_agg}"
stats_dir="${COMEXT_STATS_DIR:-/tmp/comext_stats}"
out="${agg_dir}/${stem}.tsv"
stats="${stats_dir}/${stem}.tsv"

mkdir -p "$agg_dir" "$stats_dir"

awk -F, -v stats_out="$stats" '
NR==1 {
  col_count = NF
  for (i = 1; i <= NF; i++) {
    header = header (i == 1 ? "" : ",") $i
  }
  next
}
{
  sitc = $5
  cat = substr(sitc,1,2)
  if (cat != "32" && cat != "33" && cat != "34" && cat != "35") next
  rep = $1
  flow = $11
  period = $14
  year = substr(period,1,4)
  v = $15 + 0
  q = $17 + 0
  key = rep "\t" flow "\t" cat "\t" year
  val[key] += v
  qty[key] += q
  cnt[key] += 1

  filtered_rows += 1
  reporters[rep] = 1
  products[sitc] = 1

  if ($15 == "" || $15 == ":" || $15 == "NA") missing_value += 1
  if ($17 == "" || $17 == ":" || $17 == "NA") missing_quantity += 1
}
END {
  for (k in val) {
    printf "%s\t%.0f\t%.0f\t%d\n", k, val[k], qty[k], cnt[k]
  }

  reporter_list = ""
  for (r in reporters) {
    reporter_list = reporter_list (reporter_list == "" ? "" : ",") r
  }

  product_list = ""
  for (p in products) {
    product_list = product_list (product_list == "" ? "" : ",") p
  }

  print "filtered_rows\t" filtered_rows > stats_out
  print "missing_value\t" missing_value > stats_out
  print "missing_quantity\t" missing_quantity > stats_out
  print "column_count\t" col_count > stats_out
  print "column_names\t" header > stats_out
  print "reporters\t" reporter_list > stats_out
  print "products\t" product_list > stats_out
}' "$f" > "$out"

echo "done $stem: $(wc -l < "$out") groups"
