<!-- eslint-disable -->
<template>
  <div class="register">
    <h1> Register </h1>
    <form @submit.prevent="handleRegister">
      <label>Name</label>
      <input type="text" v-model="name" required />

      <label>Email ID</label>
      <input type="email" v-model="email" required />

      <label>Password</label>
      <input type="password" v-model="password" required />

      <label>Qualification</label>
      <input type="text" v-model="qualification" required />

      <label>Date Of Birth</label>
      <input type="date" v-model="dob" required />

      <button type="submit">Register</button>
    </form>
    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "RegisterPage",
  data() {
    return {
      name: "",
      email: "",
      password: "",
      qualification: "",
      dob: "",
      successMessage: "",
      errorMessage: "",
    };
  },
  methods: {
    ...mapActions(["register"]), // Map Vuex action
    async handleRegister() {
      try {
        await this.register({
          name: this.name,
          email: this.email,
          password: this.password,
          qualification: this.qualification,
          dob: this.dob,
        });
        // Show success message
        this.successMessage = "Registration successful! Redirecting to login...";
        this.errorMessage = "";

        // Redirect to login after 2 seconds
        setTimeout(() => {
          this.$router.push("/login");
        }, 2000);
      } catch (error) {
        this.successMessage = "";
        this.errorMessage = error.response?.data?.message || "Registration failed.";
      }
    },
  },
};
</script>

<style scoped>
.register {
  text-align: center;
  margin-top: 50px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

input {
  margin: 5px;
  padding: 8px;
  font-size: 16px;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>