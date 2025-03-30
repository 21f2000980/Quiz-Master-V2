<template>
    <nav class="navbar">
      <h1 class="dashboard-title">User Dashboard</h1>
      <div class="nav-container">
        <router-link to="/dashboard" class="nav-item">Home</router-link>
        <router-link to="/Score" class="nav-item">Score</router-link>
        <button class="nav-item logout" @click="handlelogout">Logout</button>
      </div>
    </nav>
  </template>

<script>
import { mapActions } from 'vuex';

export default {
    methods: {
      
        ...mapActions( ["logout"]),

        handlelogout() {
        console.log("Logging out...");
        this.logout();
        this.$router.push("/login");
        },
    },
};
</script>

<style scoped>
.navbar {
  background-color: #007bff;
  padding: 15px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.dashboard-title {
  color: white;
  font-size: 22px;
  font-weight: bold;
  flex-grow: 1;
  text-align: center;
}

.nav-container {
  display: flex;
  gap: 20px;
}

.nav-item {
  color: white;
  text-decoration: none;
  font-size: 18px;
  padding: 8px 12px;
  border-radius: 5px;
  transition: background 0.3s ease-in-out;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.2);
}

.logout {
  background: #dc3545;
  border: none;
  padding: 8px 15px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease-in-out;
}

.logout:hover {
  background: #a71d2a;
}
</style>