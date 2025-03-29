<template>
    <div class="attempt-quiz-container">
      <NavbarPage />
      
      <h1>Attempt Quiz</h1>
  
      <div v-if="questions.length" class="question-list">
        <div v-for="(question, index) in questions" :key="question.id" class="question-card">
          <h3>Q{{ index + 1 }}: {{ question.question_statement }}</h3>
          
          <div class="options">
            <label v-for="optionKey in ['option_1', 'option_2', 'option_3', 'option_4']" :key="optionKey">
              <input 
                type="radio" 
                :name="'question-' + question.id" 
                :value="optionKey" 
                v-model="selectedAnswers[question.id]"
              />
              {{ question[optionKey] }}
            </label>
          </div>
        </div>
      </div>
  
      <button @click="submitQuiz" class="submit-btn">Submit Quiz</button>
    </div>
  </template>
  
  <script>
import { mapState, mapActions } from "vuex";
import NavbarPage from "../components/NavbarPage.vue";

export default {
  components: { NavbarPage },
  data() {
    return {
      selectedAnswers: {} // Store user's selected answers
    };
  },
  computed: {
    ...mapState(["questions"])
  },
  methods: {
    ...mapActions(["fetchQuestion", "submitScore"]),

    async submitQuiz() {
      let score = 0;

      this.questions.forEach(question => {
        if (this.selectedAnswers[question.id] === `option_${question.correct_option}`) {
          score++;
        }
      });

      // Get user_id from localStorage (or Vuex if available)
      const userId = localStorage.getItem("user_id");

      if (!userId) {
        console.error("User ID not found");
        return;
      }

      // Prepare score data
      const scoreData = {
        user_id: parseInt(userId), // Ensure it's an integer
        quiz_id: this.$route.params.quizId,
        total_scored: score
      };

      try {
        // Submit Score
        await this.submitScore(scoreData);

        // Navigate to score page
        this.$router.push({
          path: `/score`
        });
      } catch (error) {
        console.error("Error submitting score", error);
      }
    }
  },
  mounted() {
    this.fetchQuestion(this.$route.params.quizId);
  }
};
</script>
  
  <style scoped>
  /* .attempt-quiz-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    text-align: center;
  } */
  
  .question-card {
    background: #f9f9f9;
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
  }
  
  .options {
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  
  .submit-btn {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
    margin-top: 20px;
  }
  
  .submit-btn:hover {
    background-color: #218838;
  }
  </style>
  
  