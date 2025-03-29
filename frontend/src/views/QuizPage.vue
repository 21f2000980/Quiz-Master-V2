<template>
    <div class="quiz-container">
      <!-- Navbar -->
      <NavbarPage />
  
      <!-- Heading -->
      <h1>Available Quizzes for {{ chapterName }}</h1>
  
      <!-- Quiz List -->
      <div v-if="quizzes.length" class="quiz-list">
        <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-card">
          <div class="quiz-info">
            <h2>Quiz ID: {{ quiz.id }}</h2>
            <p><strong>Date:</strong> {{ quiz.date_of_quiz }}</p>
            <p><strong>Duration:</strong> {{ quiz.time_duration }} mins</p>
            <p><strong>Remark:</strong> {{ quiz.remark }}</p>
          </div>
          <button @click="attemptQuiz(quiz.id)" class="attempt-btn">
            Attempt Quiz
          </button>
        </div>
      </div>
  
      <!-- No Quizzes Available -->
      <p v-else class="no-quiz">No quizzes available</p>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import NavbarPage from "../components/NavbarPage.vue";
  
  export default {
    components: { NavbarPage },
    data() {
    return {
      chapterName: "", // Store chapter name
    };
  },
    computed: {
      ...mapState(["quizzes"]),
    },
    methods: {
      ...mapActions(["fetchQuizzes"]),
      attemptQuiz(quizId) {
        this.$router.push(`/question/${quizId}`);
      },
    },
    mounted() {
         // Get chapter name from query parameter
      this.chapterName = this.$route.query.name ;
      const chapterId = this.$route.params.chapterId;
      this.fetchQuizzes(chapterId);
    },
  };
  </script>
  
  <style scoped>
  /* Heading */
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
    color: #2c3e50;
  }
  
  /* Quiz List */
  .quiz-list {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  /* Quiz Card */
  .quiz-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    transition: transform 0.2s ease-in-out;
  }
  
  .quiz-card:hover {
    transform: scale(1.02);
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  /* Quiz Info */
  .quiz-info {
    text-align: left;
  }
  
  .quiz-info h2 {
    margin: 0;
    color: #34495e;
  }
  
  .quiz-info p {
    margin: 5px 0;
    color: #555;
  }
  
  /* Attempt Button */
  .attempt-btn {
    background: #3498db;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
    transition: background 0.3s ease-in-out;
  }
  
  .attempt-btn:hover {
    background: #2980b9;
  }
  
  /* No Quizzes Available */
  .no-quiz {
    color: #7f8c8d;
    font-style: italic;
    margin-top: 20px;
  }
  </style>
  