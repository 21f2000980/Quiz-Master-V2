<template>
    <adminNavbar />
    <div class="analytics-container">
      <h1>Admin Dashboard - Analytics</h1>
  
      <!-- Summary Cards -->
      <div class="summary-cards">
        <div class="card">
          <h3>Total Users</h3>
          <p>{{ summaryData.total_users }}</p>
        </div>
        <div class="card">
          <h3>Total Subjects</h3>
          <p>{{ summaryData.total_subjects }}</p>
        </div>
        <div class="card">
          <h3>Total Chapters</h3>
          <p>{{ summaryData.total_chapters }}</p>
        </div>
        <div class="card">
          <h3>Total Quizzes</h3>
          <p>{{ summaryData.total_quizzes }}</p>
        </div>
      </div>
  
      <!-- Chart for Average Marks per Subject -->
      <div class="chart-container">
        <canvas ref="barChart"></canvas>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import AdminNavbar from "../components/AdminNavbar.vue";
  import Chart from "chart.js/auto";
  
  export default {
  components: { AdminNavbar },
  computed: {
    ...mapState(["summaryData", "chartData"]), // Use Vuex state
  },
  methods: {
    ...mapActions(["fetchSummaryData", "fetchChartData"]),
    async loadData() {
      await this.fetchSummaryData();
      await this.fetchChartData();
      console.log("chartData after fetching:", this.chartData); // Debugging
      this.renderChart();
    },
    renderChart() {
    if (!this.chartData || !this.chartData.labels || !this.chartData.datasets) {
      console.error("chartData is not structured correctly:", this.chartData);
      return;
    }

    if (this.$refs.barChart) {
      new Chart(this.$refs.barChart, {
        type: "bar",
        data: {
          labels: this.chartData.labels,  // Use `labels` directly
          datasets: this.chartData.datasets, // Use `datasets` directly
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: "Average Marks per Subject",
            },
          },
        },
      });
    }
  },
  },
  mounted() {
    this.loadData();
  },
};
  </script>
  
  <style scoped>
  .analytics-container {
    max-width: 900px;
    margin: auto;
    text-align: center;
    padding: 20px;
  }
  .summary-cards {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  .card {
    background: #007bff;
    color: white;
    padding: 15px;
    border-radius: 8px;
    width: 180px;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  }
  .chart-container {
    margin-top: 30px;
    padding: 20px;
  }
  </style>
  
  