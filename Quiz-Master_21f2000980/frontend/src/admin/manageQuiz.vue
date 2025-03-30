<template>
    <adminNavbar/>
    <div class="container">
      <!-- Add Quiz Form -->
      <div class="quizform">
        <h2 class="title">Create a New Quiz</h2>
        <div class="inputArea">
          <input v-model="newQuiz.date_of_quiz" type="date" class="input" placeholder="Date of Quiz" />
          <input v-model="newQuiz.time_duration" type="text" class="input" placeholder="Time Duration (HH:MM)" />
          <input v-model="newQuiz.remarks" type="text" class="input" placeholder="Remarks" />
        </div>
        <button @click="handleAddQuiz" class="handlequizbtn">
          Add Quiz
        </button>
      </div>
  
      <!-- Quizzes List -->
      <div class="Qlist">
        <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-card">
          <h3 class="quizzestitle">Quiz on {{ quiz.date_of_quiz }}</h3>
          <p><strong>Duration:</strong> {{ quiz.time_duration }}</p>
          <p><strong>Remarks:</strong> {{ quiz.remarks }}</p>
  
          <div class="managesection">
            <button @click="manageQuestions(quiz.id)" class="qmanage">
              Manage Questions
            </button>
            <button @click="deleteQuiz(quiz.id)" class="q\deletequiz">
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
</template>
  
  <script>
  import { mapActions, mapState } from "vuex";
  import adminNavbar from "../components/adminNavbar.vue";
  
  export default {
    components: { adminNavbar },
    data() {
        return {
            newQuiz: {
            date_of_quiz: "",
            time_duration: "",
            remarks: "",
        },
    };
    },
    computed: {
      ...mapState(["quizzes"]), // Map quizzes from Vuex store
    },
    methods: {
      ...mapActions(["fetchQuizzes", "addQuiz", "deleteQuiz"]),
  
      // Handle adding a quiz
      async handleAddQuiz() {
        if (!this.newQuiz.date_of_quiz || !this.newQuiz.time_duration) {
          alert("Please fill in all required fields.");
          return;
        }
            chapter_id: this.$route.params.chapterId, // Add chapter_id from route params
            await this.addQuiz({
              date_of_quiz: this.newQuiz.date_of_quiz,
              time_duration: this.newQuiz.time_duration,
              remarks: this.newQuiz.remarks,
              chapter_id: this.$route.params.chapterId,
            });
            this.fetchQuizzes(this.$route.params.chapterId);
            this.newQuiz = { date_of_quiz: "", time_duration: "", remarks: "" };
      },

      async deleteQuiz(id) {
        if (confirm("Do You Want To Delete this Quiz?")) {
            this.$store.dispatch("deleteQuiz",id);
            this.fetchQuizzes(this.$route.params.chapterId);
        }
      },
  
    //   Navigate to manage questions page
      manageQuestions(quizId) {
        this.$router.push(`${this.$route.path}/${quizId}`);
      },
    },
    mounted() {
      this.fetchQuizzes(this.$route.params.chapterId);
    },
  };
  </script>


  <style scoped>
/* Container */
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

/* Add Quiz Form */
.quizform {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.inputArea {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  outline: none;
}

.handlequizbtn {
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  transition: background 0.3s;
}

.handlequizbtn:hover {
  background-color: #0056b3;
}

/* Quizzes List */
.Qlist {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.quiz-card {
  background-color: #fff;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  text-align: left;
  transition: transform 0.2s;
}

.quiz-card:hover {
  transform: scale(1.02);
}

.quizzestitle {
  font-size: 1.3rem;
  font-weight: bold;
  color: #222;
  margin-bottom: 8px;
}

p {
  color: #555;
  font-size: 1rem;
}

/* Buttons */
.managesection {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.qmanage,
.q\deletequiz {
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.3s;
}

.qmanage {
  background-color: #28a745;
  color: white;
}

.qmanage:hover {
  background-color: #218838;
}

.q\deletequiz {
  background-color: #dc3545;
  color: white;
}

.q\deletequiz:hover {
  background-color: #c82333;
}
</style>