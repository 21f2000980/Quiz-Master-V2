<!-- eslint-disable -->
<template>
    <div class = "login-container">
      <div class="login_box">
        <h1> Login</h1>
        <form @submit.prevent="handleLogin">
            
            <label> Email ID </label>
            <input type="email" v-model="email" required />

            <label> Password </label>
            <input type="password" v-model="password" required />

            <button type="Submit"> Login </button>

        </form>
        <p class="register-link">
        Not registered yet? <router-link to="/register">Register here</router-link>
      </p>
    </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      email: "",  // ✅ Ensure this is initialized
      password: "" // ✅ Ensure this is initialized
    };
  },
  methods: {
    ...mapActions(["login"]),

    async handleLogin() {
      console.log("Email:", this.email, "Password:", this.password); // ✅ Debugging

      if (!this.email || !this.password) {
        alert("Please enter both email and password.");
        return;
      }

      try {
        await this.login({ email: this.email, password: this.password });
        console.log("Stored Role:", localStorage.getItem("role")); // Debugging

        const role = localStorage.getItem("role");

        if (role === "admin") {
            this.$router.push("/admin"); // Redirect admin
        } else {
            this.$router.push("/dashboard"); // Redirect regular user
        }
      } catch (error) {
        console.error("Login failed:", error);
        alert("Login failed! Check credentials.");
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f4f4f4;
  font-family: Arial, sans-serif;
}

.login-box {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 300px;
}

.login-box h2 {
  margin-bottom: 20px;
  font-size: 24px;
  color: #333;
}

input {
  width: 100%;
  padding: 10px;
  margin: 8px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

button {
  width: 100%;
  background: #007bff;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

button:hover {
  background: #0056b3;
}

.register-link {
  margin-top: 15px;
  font-size: 14px;
}

.register-link a {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.register-link a:hover {
  text-decoration: underline;
}

</style>