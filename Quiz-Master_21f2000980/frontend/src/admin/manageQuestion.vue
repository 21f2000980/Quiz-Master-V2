<template>
    <adminNavbar/>
    <div class="container">
      <!-- Add Question Form -->

      <div class="question-form">
        <h2 class="title">Add a New Question</h2>
        <div class="input-area">
          <input v-model="newQuestion.question_statement" type="text" class="input" placeholder="Enter Question" />
          <input v-model="newQuestion.option_1" type="text" class="input" placeholder="Option 1" />
          <input v-model="newQuestion.option_2" type="text" class="input" placeholder="Option 2" />
          <input v-model="newQuestion.option_3" type="text" class="input" placeholder="Option 3" />
          <input v-model="newQuestion.option_4" type="text" class="input" placeholder="Option 4" />
          <select v-model="newQuestion.correct_option" class="input">
            <option value="">Select Correct Option</option>
            <option value="1">Option 1</option>
            <option value="2">Option 2</option>
            <option value="3">Option 3</option>
            <option value="4">Option 4</option>
          </select>
        </div>
        <button @click="handleAddQuestion" class="add-btn">Add Question</button>
      </div>
  
      <!-- Questions List -->
      <div class="question-list">
        <h2 class="title">Questions</h2>
        <div v-if="questions.length">
          <div v-for="question in questions" :key="question.id" class="question-card">
            <h3 class="question-text">{{ question.question_statement }}</h3>
            <ul class="options-list">
              <li :class="{ correct: question.correct_option == 1 }">{{ question.option_1 }}</li>
              <li :class="{ correct: question.correct_option == 2 }">{{ question.option_2 }}</li>
              <li :class="{ correct: question.correct_option == 3 }">{{ question.option_3 }}</li>
              <li :class="{ correct: question.correct_option == 4 }">{{ question.option_4 }}</li>
            </ul>
            <button @click="deleteQuestion(question.id)" class="delete-btn">Delete</button>
          </div>
        </div>
        <p v-else>No questions available.</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions , mapState } from "vuex";
  import adminNavbar from "../components/adminNavbar.vue"

  
  export default {
    components: { adminNavbar },
    
    data() {
      return {
        newQuestion: {
          question_statement: "",
          option_1: "",
          option_2: "",
          option_3: "",
          option_4: "",
          correct_option: "",
          quiz_id: this.$route.params.quizId, // Fetching quiz_id from route
        },
      };
    },
    computed: {
      ...mapState(["questions"]),
    },
    methods: {
      ...mapActions(["fetchQuestion", "addQuestion", "deleteQuestion"]),
  
      async handleAddQuestion() {
        if (!this.newQuestion.question_statement || !this.newQuestion.correct_option) {
          alert("Please fill in the question and select a correct option.");
          return;
        }
  
        try {
          await this.addQuestion(this.newQuestion);
          this.newQuestion = { question_statement: "", option_1: "", option_2: "", option_3: "", option_4: "", correct_option: "", quiz_id: this.$route.params.quizId };
        } catch (error) {
          console.error("Error adding question:", error);
        }
      },
    },
    created() {
        this.fetchQuestion(this.$route.params.quizId);
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
  }
  
  .title {
    font-size: 22px;
    margin-bottom: 10px;
  }
  
  .input-area {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .add-btn, .delete-btn {
    padding: 10px;
    margin-top: 10px;
    background: #28a745;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .add-btn:hover {
    background: #218838;
  }
  
  .delete-btn {
    background: #dc3545;
  }
  
  .delete-btn:hover {
    background: #c82333;
  }
  
  .question-list {
    margin-top: 20px;
  }
  
  .question-card {
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
  }
  
  .question-text {
    font-weight: bold;
  }
  
  .options-list {
    list-style: none;
    padding: 0;
  }
  
  .options-list li {
    padding: 5px;
  }
  
  .correct {
    color: green;
    font-weight: bold;
  }
  </style>
  