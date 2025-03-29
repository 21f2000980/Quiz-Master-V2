<template>
    <nav class="navbar">
      <router-link to="/admin/manage-subjects">Manage Subjects</router-link>
      <router-link to="/admin/manage-chapters">Manage Chapters</router-link>
      <router-link to="/admin/manage-quizzes">Manage Quizzes</router-link>
      <router-link to="/admin/manage-questions">Manage Questions</router-link>
      <router-link to="/admin/user-analytics">User Analytics</router-link>
      <button @click="logout">Logout</button>
    </nav>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/login");
      }
    }
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    gap: 15px;
    background: #2c3e50;
    padding: 10px;
  }
  .navbar a {
    color: white;
    text-decoration: none;
  }
  button {
    background: red;
    color: white;
    border: none;
    padding: 5px 10px;
  }
  </style>