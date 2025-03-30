<template>
    <NavbarPage/>
    <div class="score-container">
      <h1>Your Quiz Scores</h1>
  
      <table v-if="scores.length" class="score-table">
        <thead>
          <tr>
            <th>Quiz ID</th>
            <th>Chapter Name</th>
            <th>Score</th>
            <th>Date</th>
            
          </tr>
        </thead>
        <tbody>
          <tr v-for="score in scores" :key="score.quiz_id">
            <td>{{ score.quiz_id }}</td>
            <td>{{ score.chapter_name }}</td>
            <td>{{ score.total_scored }}</td>
            <td>{{ score.date }}</td>
          </tr>
        </tbody>
      </table>
  
      <p v-else>No scores available</p>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import NavbarPage from "../components/NavbarPage.vue" ;


  export default {
    components: { NavbarPage },
    computed: {
      ...mapState(["scores"])
    },
    methods: {
      ...mapActions(["fetchScores"])
    },
    mounted() {
      this.fetchScores();
    }
  };
  </script>
  
  <style scoped>
  .score-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    text-align: center;
  }
  
  .score-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .score-table th, .score-table td {
    border: 1px solid #ddd;
    padding: 10px;
  }
  
  .score-table th {
    background-color: #007BFF;
    color: white;
  }
  
  .score-table tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  </style>
  