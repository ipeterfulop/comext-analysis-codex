<script setup>
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
