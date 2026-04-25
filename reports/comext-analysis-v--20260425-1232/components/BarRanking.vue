<script setup>
import { onMounted, ref, watch } from 'vue'
import { Chart, BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend, Colors } from 'chart.js'

Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend, Colors)

const chartJsDefaultColors = [
  '#36A2EB',
  '#FF6384',
  '#FFCE56',
  '#4BC0C0',
  '#9966FF',
  '#FF9F40',
  '#C9CBCF',
]

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
    backgroundColor: data.map((_, index) => chartJsDefaultColors[index % chartJsDefaultColors.length]),
    borderColor: data.map((_, index) => chartJsDefaultColors[index % chartJsDefaultColors.length]),
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
