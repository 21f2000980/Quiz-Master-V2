<template>
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/dashboard" class="nav-item"> Home </router-link>
        <router-link to="/Score" class="nav-item"> Score </router-link>
        <button class="nav-item" @click="handlelogout">Logout</button>
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
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.nav-container {
  display: flex;
  gap: 15px;
}
.nav-item {
  color: red;
  text-decoration: none;
  font-size: 18px;
  cursor: pointer;
}
.logout {
  background: red;
  border: none;
  padding: 5px 10px;
  color: white;
  cursor: pointer;
}
</style>