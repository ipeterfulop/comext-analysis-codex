#!/usr/bin/env python3
"""Initialize a fresh Slidev report folder for the COMEXT deck."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


PACKAGE_JSON = {
    "name": "comext-analysis-deck",
    "private": True,
    "type": "module",
    "scripts": {
        "dev": "slidev --port 3030",
        "build": "slidev build",
        "export": "slidev export",
    },
    "dependencies": {
        "@iconify-json/mdi": "^1.2.3",
        "@slidev/cli": "^52.14.2",
        "chart.js": "^4.4.1",
        "slidev-theme-neversink": "^0.4.1",
        "vue": "^3.4.0",
    },
}

BAR_RANKING = """<script setup>
import { onMounted, ref, watch } from 'vue'
import { Chart, BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js'

Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend)

const props = defineProps({
  items: { type: Array, default: () => [] },
  label: { type: String, default: 'VALUE_EUR' },
})

const canvas = ref(null)
let chart

function eurFmt(value) {
  return '€' + Number(value || 0).toLocaleString('en-US', { maximumFractionDigits: 0 })
}

function render() {
  if (!canvas.value)
    return

  if (chart)
    chart.destroy()

  const labels = props.items.map(item => `${item.code} · ${item.name}`)
  const data = props.items.map(item => item.value)
  const dataset = {
    label: props.label,
    data,
    borderWidth: 1,
  }

  chart = new Chart(canvas.value, {
    type: 'bar',
    data: { labels, datasets: [dataset] },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: context => eurFmt(context.raw),
          },
        },
      },
      scales: {
        x: {
          ticks: {
            callback: value => eurFmt(value),
          },
        },
      },
    },
  })
}

onMounted(render)
watch(() => props.items, render, { deep: true })
</script>

<template>
  <div class="w-full" style="height: 340px">
    <canvas ref="canvas"></canvas>
  </div>
</template>
"""

TREND_LINES = """<script setup>
import { onMounted, ref, watch } from 'vue'
import { Chart, LineController, LineElement, PointElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js'

Chart.register(LineController, LineElement, PointElement, CategoryScale, LinearScale, Tooltip, Legend)

const props = defineProps({
  years: { type: Array, default: () => [] },
  series: { type: Array, default: () => [] },
})

const canvas = ref(null)
let chart

function eurFmt(value) {
  return '€' + Number(value || 0).toLocaleString('en-US', { maximumFractionDigits: 0 })
}

function render() {
  if (!canvas.value)
    return

  if (chart)
    chart.destroy()

  const datasets = props.series.map((series, index) => ({
    label: series.label,
    data: series.values.map(value => value == null ? null : value),
    borderColor: series.color,
    backgroundColor: series.color,
    borderDash: series.dashed ? [8, 5] : [],
    borderWidth: 3,
    pointRadius: 3,
    pointHoverRadius: 5,
    tension: 0.2,
    spanGaps: false,
    order: index + 1,
  }))

  chart = new Chart(canvas.value, {
    type: 'line',
    data: {
      labels: props.years,
      datasets,
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom' },
        tooltip: {
          callbacks: {
            label: context => `${context.dataset.label}: ${context.raw == null ? '—' : eurFmt(context.raw)}`,
          },
        },
      },
      scales: {
        y: {
          ticks: {
            callback: value => eurFmt(value),
          },
        },
      },
    },
  })
}

onMounted(render)
watch(() => props.series, render, { deep: true })
</script>

<template>
  <div class="w-full" style="height: 360px">
    <canvas ref="canvas"></canvas>
  </div>
</template>
"""

TWO_COLUMN_LAYOUT = """<template>
  <div class="h-full w-full">
    <slot />
  </div>
</template>
"""

CENTERED_LAYOUT = """<template>
  <div class="h-full flex items-center justify-center">
    <div class="w-full max-w-5xl px-12 mx-auto">
      <slot />
    </div>
  </div>
</template>
"""

CENTERED_SECTION_DIVIDER_LAYOUT = """<template>
  <div class="h-full flex items-center justify-center">
    <div class="w-full max-w-4xl px-12 mx-auto text-center">
      <slot />
    </div>
  </div>
</template>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("report_dir")
    parser.add_argument("--bundle-json")
    return parser.parse_args()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    args = parse_args()
    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    write_text(report_dir / "package.json", json.dumps(PACKAGE_JSON, indent=2) + "\n")
    write_text(report_dir / "components" / "BarRanking.vue", BAR_RANKING)
    write_text(report_dir / "components" / "TrendLines.vue", TREND_LINES)
    write_text(report_dir / "layouts" / "two-column.vue", TWO_COLUMN_LAYOUT)
    write_text(report_dir / "layouts" / "centered.vue", CENTERED_LAYOUT)
    write_text(report_dir / "layouts" / "centered-section-divider.vue", CENTERED_SECTION_DIVIDER_LAYOUT)

    if args.bundle_json:
      shutil.copyfile(args.bundle_json, report_dir / "data.json")

    print(f"Initialized {report_dir}")


if __name__ == "__main__":
    main()
