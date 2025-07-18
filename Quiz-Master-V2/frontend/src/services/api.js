import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api", // Change URL if needed
  headers: {
    "Content-Type": "application/json",
  },
});

const token = localStorage.getItem("token");
if (token) {
  api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

export default api;
