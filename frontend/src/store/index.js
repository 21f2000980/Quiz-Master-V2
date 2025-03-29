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
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      localStorage.setItem("user_id", user.id);
    },
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    },
    SET_Subjects(state,subjects){
      state.subjects = subjects;
    },
    SET_Chapters(state,chapters){
      state.chapters = chapters;
    },
    SET_Quizzes(state,quizzes){
      state.quizzes = quizzes;
    },
    SET_Question(state,questions){
      state.questions = questions;
    },
    SET_Scores(state,scores){
      state.scores = scores;
    },

    LOGOUT(state) {
      console.log("LOGOUT mutation triggered"); // Debugging

      state.user = null;
      state.access_token = null;
      localStorage.removeItem("token");  // Clear token
      localStorage.removeItem("user_id"); // Also clear user_id
    },
  },
  actions: {
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
  async fetchSubjects({ commit } ){
    try{
      const { data } = await axios.get("/subjects");
      console.log("Fetched subjects:", data); // Debugging
      commit("SET_Subjects",data);
    } catch (error) {
      console.error("error handling subject",error)
    }
  },
  async fetchChapters({ commit }, subjectId ){
    try{
      const { data } = await axios.get(`/subjects/${subjectId}`);
      console.log("Fetched subjects:", data.chapters);
      commit("SET_Chapters",data.chapters);
    } catch (error) {
      console.error("error handling chapters",error)
    }
  },
  async fetchQuizzes({ commit }, chapterId){
    try {
      const { data } = await axios.get(`/quiz/${chapterId}`)

      console.log("Fetch Quizes:", data);
      commit("SET_Quizzes", data);
    }
    catch (error) {
      console.error("error handling quizzes",error)
    }

  },
  async fetchQuestion({ commit }, quizId){
    try {
      const { data } = await axios.get(`/QuizQues/${quizId}`)

      console.log("Fetch Question:", data);
      commit("SET_Question", data);
    }
    catch (error) {
      console.error("error handling quizzes",error)
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
    getQuizzes: (state) => state.quizzes
  },
});
