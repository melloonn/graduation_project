<template>
  <canvas id="myChart"></canvas>
</template>

<script>
import { onMounted, ref, watch } from "vue";
import { Chart, registerables } from "chart.js";

// 註冊所有必要的組件
Chart.register(...registerables);

export default {
  props: {
    companyId: String,
    reportType: String,
    dataField: String,
    chartData: Array,
  },
  setup(props) {
    const chart = ref(null);

    const renderChart = () => {
      const ctx = document.getElementById("myChart").getContext("2d");

      // 使用 chartData 的資料生成圖表
      const labels = props.chartData.map((item) => item.year_month);
      const dataValues = props.chartData.map((item) => item[props.dataField]);

      if (chart.value) {
        chart.value.destroy(); // 銷毀舊的圖表實例
      }

      chart.value = new Chart(ctx, {
        type: "line",
        data: {
          labels: labels,
          datasets: [
            {
              label: props.dataField + props.companyId,
              data: dataValues,
              borderColor: "rgba(75, 192, 192, 1)",
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderWidth: 3,
              fill: true,
              pointRadius: 4,
              pointHoverRadius: 6,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            x: {
              type: "category",
              title: {
                display: true,
                text: "年月",
              },
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "數值 (元)",
              },
              ticks: {
                callback: (value) => value.toLocaleString(),
              },
            },
          },
          plugins: {
            tooltip: {
              enabled: true,
              callbacks: {
                label: (tooltipItem) =>
                  `${
                    tooltipItem.dataset.label
                  }: ${tooltipItem.raw.toLocaleString()}`,
              },
            },
            legend: {
              display: true,
              position: "top",
              labels: {
                color: "#333", // 圖例顏色
                font: {
                  size: 14, // 圖例字體大小
                  weight: 700,
                },
              },
            },
          },
          interaction: {
            mode: "nearest",
            intersect: true,
          },
        },
      });
    };

    // 監聽 chartData 的變化以重新渲染圖表
    watch(
      () => props.chartData,
      (newData) => {
        if (newData) {
          renderChart();
        }
      }
    );

    // 在組件掛載時渲染圖表
    onMounted(() => {
      renderChart();
    });

    return {};
  },
};
</script>

<style scoped>
canvas {
  max-width: 550px;
  max-height: 350px;
}
</style>
