/* eslint-disable no-undef */
import { createStore } from "vuex";
import api from "../services/api";
import axios from 'axios';


export default createStore({
  state: {
    user: "",
    token: localStorage.getItem("token") || "",
    subjects:[],
    chapters:[],
    quizzes:[],
    questions:[],
    scores: [],
    adview:[],
    summaryData:[],
    chartData:[],
  },


  mutations: {
    SET_USER(state, user) {
      state.user = user;
      localStorage.setItem("user_id", user.id);
      localStorage.setItem("role", user.role);
    },


    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    },


    SET_Subjects(state,subjects){
      state.subjects = subjects;
    },


    ADD_SUBJECT(state, subject) {
      state.subjects.push(subject);
    },


    DELETE_SUBJECT(state, subjectId) {
      state.subjects = state.subjects.filter(s => s.id !== subjectId);
    },


    SET_Chapters(state,chapters){
      state.chapters = chapters;
    },


    ADD_Chapters(state,chapter){
      state.chapters.push(chapter);
    },


    DELETE_Chapters(state,chaptersId){
      state.chapters = state.chapters.filter(ch => ch.id !== chapterId);
    },


    SET_Quizzes(state,quizzes){
      state.quizzes = quizzes;
    },


    ADD_Quiz(state,quiz){
      state.quizzes=quiz;
    },


    DELETE_Quiz(state,quiz_id){
      state.quizzes = state.quizzes.filter(q => q.id !== quiz_id)
    },


    SET_QUESTIONS(state, questions) {
      state.questions = questions;
    },


    ADD_QUESTION(state, question) {
      state.questions.push(question);
    },


    DELETE_QUESTION(state, questionId) {
      state.questions = state.questions.filter((q) => q.id !== questionId);
    },
   

    SET_user_view(state,view){
      state.adview = view;
    },


    SET_SUMMARY(state, data) {
      state.summaryData = data;
    },


    SET_CHART_DATA(state, data) {
      state.chartData = {
        labels: data.map((item) => item.subject_name),
        datasets: [
          {
            label: "Average Marks",
            data: data.map((item) => item.average_marks),
            backgroundColor: "#007bff",
          },
        ],
      };
    },



    SET_Scores(state,scores){
      state.scores = scores;
    },




    LOGOUT(state) {
      console.log("LOGOUT mutation triggered"); // Debugging

      state.user = null;
      state.access_token = null;
      localStorage.removeItem("token");  // Clear token
      localStorage.removeItem("user_id");
      localStorage.removeItem("role"); // Also clear user_id
    },



  },

  actions: {
   // Action for registration

    async register(_, userData) {
      try {
        const { data } = await api.post("/register", userData);
        console.log("User registered successfully:", data);
        commit("SET_USER", data.user);
        commit("SET_TOKEN", data.access_token);

        return data; // Return data for redirection in component
        
      } catch (error) {
        console.error("Registration failed:", error.response?.data || error.message);
      }
    },


    // >> Action for Login 


    async login({ commit }, credentials) {
      try {
        const response = await api.post("/login", credentials);
        console.log("Login response:", response.data);
        if (!response.data.access_token) {
          throw new Error("Token missing in response");
        }
        console.log("Login response:", response.data.user.id);
        commit("SET_TOKEN", response.data.access_token);
        commit("SET_USER", response.data.user);
      } catch (error) {
        console.error("Login failed:", error.response?.data || error.message);
      }
    
  },


  //  Action for doing crud on Subject



  async fetchSubjects({ commit } ){
    try{
      const { data } = await axios.get("/subjects");
      console.log("Fetched subjects:", data); // Debugging
      commit("SET_Subjects",data);
    } catch (error) {
      console.error("error handling subject",error)
    }
  },

    async addSubject({ commit }, subject) {
      const response = await api.post("/subjects",subject);
      commit("ADD_SUBJECT", response.data);
    },
    
    async deleteSubject({ commit }, subjectId) {
      await api.delete(`/subjects/${subjectId}`); // Pass ID in URL
      commit("DELETE_SUBJECT", subjectId);
    },
  
  
//  Action for crud on chapters

  async fetchChapters({ commit }, subjectId ){
    try{
      const { data } = await axios.get(`/subjects/${subjectId}`);
      console.log("Fetched subjects:", data.chapters);
      commit("SET_Chapters",data.chapters);
    } catch (error) {
      console.error("error handling chapters",error)
    }
  },

  async addChapter({ commit }, chapterdata ){
    try{
      const { data } = await axios.post(`/chapters`, chapterdata
  );
      console.log("Fetched :", data);
      commit("ADD_Chapters",data);
    } catch (error) {
      console.error("error handling chapters",error)
    }
  },

  async deleteChapter({ commit }, chapter_id ){
      await axios.delete(`/chapters/${chapter_id}`);
      commit("DELETE_Chapters", chapter_id);
  },



//  action for crud on quizzes

  async fetchQuizzes({ commit }, chapter_id){
    try {
      const { data } = await axios.get(`/quiz/${chapter_id}`)

      console.log("Fetch Quizes:", data);
      commit("SET_Quizzes", data);
    }
    catch (error) {
      console.error("error handling quizzes",error)
    }

  },

  async addQuiz( { commit }, Quizdata ){
    const { data } = await axios.post(`/quizzes`,Quizdata)
    commit("ADD_Quiz",data);
  },


  async deleteQuiz( { commit }, quiz_id ){
    const { data } = await axios.delete(`/quizzes/${quiz_id}`)
    commit("DELETE_Quiz",quiz_id);
  },



  // async adminfetchQuestions({ commit }) {
  //   try {
  //     const response = await axios.get("/questions");
  //     commit("SET_QUESTIONS", response.data);
  //   } catch (error) {
  //     console.error("Error fetching questions:", error);
  //   }
  // },
  async addQuestion({ commit }, questionData) {
    try {
      const response = await axios.post("/questions", questionData);
      commit("ADD_QUESTION", { ...questionData, id: response.data.id });
    } catch (error) {
      console.error("Error adding question:", error);
    }
  },
  async deleteQuestion({ commit }, questionId) {
    try {
      await axios.delete(`/questions/${questionId}`);
      commit("DELETE_QUESTION", questionId);
    } catch (error) {
      console.error("Error deleting question:", error);
    }
  },








  async fetchQuestion({ commit }, quizId){
    try {
      const { data } = await axios.get(`/QuizQues/${quizId}`)

      console.log("Fetch Question:", data);
      commit("SET_QUESTIONS", data);
    }
    catch (error) {
      console.error("error handling quizzes",error)
    }

  },

  async fetchadminuserview( {commit }){
    const { data } = await axios.get(`/adminscores`)
    commit("SET_user_view", data );
  },




  async fetchSummaryData({ commit }) {
    try {
      const response = await axios.get("/summary");
      commit("SET_SUMMARY", response.data);
    } catch (error) {
      console.error("Error fetching summary:", error);
    }
  },

  async fetchChartData({ commit }) {
    try {
      const response = await axios.get("/avgmarks");
      commit("SET_CHART_DATA", response.data);
    } catch (error) {
      console.error("Error fetching chart data:", error);
    }
  },



    
  async submitScore({ commit }, scoreData) {
      try {
        await axios.post('/scores', scoreData);
        console.log("Score submitted successfully!");
      } catch (error) {
        console.error("Error submitting score", error);
      }
    },



    async fetchScores({ commit }, userId) {
      try {
        const userId = localStorage.getItem("user_id");
        const { data } = await axios.get(`/scores/${userId}`);
        console.log("score data",data)
        commit("SET_Scores", data);
      } catch (error) {
        console.error("Error fetching scores", error);
      }
    },



   logout({ commit }) {
      console.log("Logout action dispatched");  // Debugging
      commit("LOGOUT");
    },
  },




  getters: {
    isAuthenticated: (state) => !!state.token,
    userRole: (state) => (state.user ? state.user.role : null),
    getSubjects: (state) => state.subjects,
    getChapters: (state) => state.chapters,
  },
});
