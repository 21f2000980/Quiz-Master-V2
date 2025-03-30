<template>
  <nav class="admin-navbar">
    <h1 class="dashboard-title">Admin Dashboard</h1>
    <div class="nav-links">
      <router-link to="/admin" class="nav-item">Home</router-link>
      <!-- <router-link to="/admin/ViewUser" class="nav-item">Users</router-link> -->
      <router-link to="/admin/userscore" class="nav-item">User Results</router-link>
      <router-link to="/admin/chart" class="nav-item">Charts</router-link>
    </div>
    <button @click="logout" class="logout-btn">Logout</button>
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
.admin-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #2c3e50;
  padding: 15px 30px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.dashboard-title {
  color: white;
  font-size: 22px;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-item {
  color: white;
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s;
}

.nav-item:hover {
  color: #f39c12;
}

.logout-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

.logout-btn:hover {
  background: #c0392b;
}
</style>