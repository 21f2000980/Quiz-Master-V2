<template>
    <adminNavbar />
    <div class="score-container">
      <h1>User Quiz Scores</h1>
  
      <!-- Search Box -->
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Search by User, Subject, or Chapter"
        class="search-input"
      />
  
      <!-- Show table only if there are scores -->
      <table v-if="filteredScores.length" class="score-table">
        <thead>
          <tr>
            <th>Quiz ID</th>
            <th>User Name</th>
            <th>Subject</th>
            <th>Chapter</th>
            <th>Score</th>
            <th>Date</th>
            
          </tr>
        </thead>
        <tbody>
          <tr v-for="score in filteredScores" :key="score.quiz_id">
            <td>{{ score.quiz_id }}</td>
            <td>{{ score.full_name }}</td>
            <td>{{ score.subject_name }}</td>
            <td>{{ score.chapter_name }}</td>
            <td>{{ score.total_scored }}</td>
            <td>{{ score.date }}</td>
            
          </tr>
        </tbody>
      </table>
  
      <p v-else class="no-scores">No scores available</p>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import AdminNavbar from "../components/AdminNavbar.vue";
  import axios from "axios";
  
  export default {
    components: { AdminNavbar },
    data() {
      return {
        searchQuery: "", // Search input
      };
    },
    computed: {
      ...mapState(["adview"]),
      scores() {
        return this.adview || []; // Ensure it's an array
      },
      filteredScores() {
        if (!this.searchQuery) {
          return this.scores;
        }
        const query = this.searchQuery.toLowerCase();
        return this.scores.filter(
          (score) =>
            score.full_name.toLowerCase().includes(query) ||
            score.subject_name.toLowerCase().includes(query) ||
            score.chapter_name.toLowerCase().includes(query)
        );
      },
    },
    methods: {
      ...mapActions(["fetchadminuserview"]),
      async deleteScore(quizId) {
        if (!confirm("Are you sure you want to delete this score?")) return;
        try {
          await axios.delete(`http://localhost:5000/api/admin/score/${quizId}`);
          this.fetchadminuserview(); // Refresh scores after deletion
        } catch (error) {
          console.error("Error deleting score:", error);
        }
      },
    },
    mounted() {
      this.fetchadminuserview();
    },
  };
  </script>
  
  <style scoped>
  .score-container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
    text-align: center;
  }
  
  /* Search Bar */
  .search-input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
  }
  
  /* Score Table */
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
  
  /* Alternate Row Colors */
  .score-table tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  
  /* Delete Button */
  .delete-btn {
    background-color: red;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .delete-btn:hover {
    background-color: darkred;
  }
  
  /* No Scores Message */
  .no-scores {
    color: red;
    font-size: 18px;
  }
  </style>
  