<template>
    <div class="container">
      <!-- Admin Navbar -->
      <adminNavbar />
  
      <div class="content">
        <h2>Manage Subjects</h2>
  
        <!-- Search Input -->
        <div class="search-container">
          <input v-model="querysearch" type="text" placeholder="Search subject..." />
          <button @click="handleSearch">Search</button>
        </div>
  
        <!-- Add Subject Button -->
        <button class="toggle-btn" @click="toggleAddForm">+ Add Subject</button>
  
        <!-- Add Subject Form (Hidden Initially) -->
        <div v-if="addvisibility" class="add-subject-box">
          <input v-model="Subject_name" type="text" placeholder="Enter subject name" />
          <input v-model="Subject_desc" type="text" placeholder="Enter subject description" />
          <button @click="handleAddSubject">Save</button>
        </div>
  
        <!-- Subjects List -->
        <ul v-if="filteredSubjects.length > 0" class="subject-list">
          <li v-for="subject in filteredSubjects" :key="subject.id" class="subject-item">
            <div class="subject-details">
              <p class="subject-name">{{ subject.name }}</p>
              <p class="subject-desc">{{ subject.description }}</p>
            </div>
            <div class="btn-group">
              <button class="view-btn" @click="viewChapters(subject.id)">View Chapters</button>
              <button class="delete-btn" @click="handleDeleteSubject(subject.id)">Delete</button>
            </div>
          </li>
        </ul>
  
        <!-- No Subjects Message -->
        <p v-else class="no-subjects">No subjects available.</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import adminNavbar from "../components/adminNavbar.vue";
  
  export default {
    components: { adminNavbar },
    data() {
      return {
        Subject_name: "",
        Subject_desc: "",
        addvisibility: false, // Controls visibility of add form
        querysearch: "",
      };
    },
    computed: {
        ...mapState(["subjects"]),
         filteredSubjects() {
              if (!this.querysearch.trim()) {
         return this.subjects;
      }
         return this.subjects.filter((subject) =>
         subject.name.toLowerCase().includes(this.querysearch.toLowerCase())
      );
    },
    },
    methods: {
      ...mapActions(["fetchSubjects", "addSubject", "deleteSubject"]),

      // Toggle Add Subject Form
      toggleAddForm() {
      this.addvisibility = !this.addvisibility;
        },
  
      async handleAddSubject() {
        if (!this.Subject_name.trim() || !this.Subject_desc.trim()) {
          alert("Both fields are required!");
          return;
        }
        await this.addSubject({ name: this.Subject_name, description: this.Subject_desc });
        this.fetchSubjects();
        this.Subject_name = "";
        this.Subject_desc = "";
      },
  
      async handleDeleteSubject(id) {
        if (confirm("Are you sure you want to delete this subject?")) {
            this.$store.dispatch("deleteSubject", id);
        }
      },
  
      viewChapters(id) {
        this.$router.push(`/admin/${id}`);
      },
    },
    created() {
      this.fetchSubjects();
    },
  };
  </script>
  
  <style scoped>
  .container {
  width: 95%;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background: #f9f9f9;
  min-height: 100vh;
}

/* Content */
.content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  margin: auto;
}

/* Heading */
h2 {
  text-align: center;
  color: #333;
}

/* Search Bar */
.search-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-container input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-container button {
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.search-container button:hover {
  background: #0056b3;
}

/* Toggle Add Subject Button */
.toggle-btn {
  display: block;
  margin: auto;
  padding: 10px;
  background: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.toggle-btn:hover {
  background: #218838;
}

/* Add Subject Box */
.add-subject-box {
  margin-top: 10px;
  padding: 15px;
  background: #f1f1f1;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.add-subject-box input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

.add-subject-box button {
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-subject-box button:hover {
  background: #0056b3;
}

/* Subject List */
.subject-list {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  padding: 0;
  justify-content: space-between;
}

/* Subject Card */
.subject-item {
  flex: 1 1 calc(33.333% - 15px); /* 3 cards per row */
  min-width: 250px;
  background: #ffffff;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.subject-item:hover {
  transform: scale(1.02);
}

/* Subject Details */
.subject-details {
  flex: 1;
}

.subject-name {
  font-weight: bold;
  font-size: 16px;
}

.subject-desc {
  font-size: 14px;
  color: #666;
  margin-top: 5px;
}

/* Buttons */
.btn-group {
  display: flex;
  gap: 10px;
}

.delete-btn,
.view-btn {
  background: #007bff;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
}

.delete-btn:hover {
  background: #cc0000;
}

.view-btn:hover {
  background: #0056b3;
}

/* No Subjects Message */
.no-subjects {
  text-align: center;
  color: #666;
  font-size: 16px;
  margin-top: 20px;
}
  </style>