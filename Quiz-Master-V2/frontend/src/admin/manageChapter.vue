<template>
    <adminNavbar/>
    <div class="container">
      <h1>View Chapters</h1>
      <button @click="toggleAddForm" class="add-btn">+ Add Chapter</button>
  
      <div v-if="showAddChapter" class="form-container">
        <input v-model="newChapter.name" placeholder="Chapter Name" class="input-field" />
        <textarea v-model="newChapter.description" placeholder="Description" class="input-field"></textarea>
        <div class="btn-group">
          <button @click="handleAddChapter" class="save-btn">Save</button>
          <button @click="toggleAddForm" class="cancel-btn">Cancel</button>
        </div>
      </div>
  
      <div class="chapters">
        <div v-for="chapter in chapters" :key="chapter.id" class="chapter-card">
          <h3>{{ chapter.name }}</h3>
          <p>{{ chapter.description }}</p>
          <div class="btn-group">
            <button @click="viewQuizzes(chapter.id)" class="view-btn">View Quizzes</button>
            <button @click="handleDeleteChapter(chapter.id)" class="delete-btn">Delete</button>
          </div>
        </div>
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
        newChapter: { name: "", description: "" },
        showAddChapter: false,
      };
    },
    computed: {
      ...mapState(["chapters"]),
    },
    methods: {
      ...mapActions(["fetchChapters", "addChapter", "deleteChapter"]),
  
      toggleAddForm() {
        this.showAddChapter = !this.showAddChapter;
      },
  
      async handleAddChapter() {
        if (!this.newChapter.name.trim()) return alert("Chapter name required");
        await this.addChapter({
          ...this.newChapter ,subject_id: this.$route.params.subjectId
    
        });
        this.fetchChapters(this.$route.params.subjectId);
        this.newChapter = { name: "", description: "" };
        this.showAddChapter = false;
      },
  
      async handleDeleteChapter(id) {
        if (confirm("Delete this chapter?")) {
             this.$store.dispatch("deleteChapter",id);
            //  this.fetchChapters(this.$route.params.subjectId);
        }
      },
  
      viewQuizzes(chapterId) {
        this.$router.push(`${this.$route.path}/${chapterId}`);
      },
    },
    created() {
      this.fetchChapters(this.$route.params.subjectId);
    },
  };
  </script>
  
  <style scoped>
  .container {
    width: 40%;
    margin: auto;
    text-align: center;
    padding-top: 20px;
  }
  
  .add-btn {
    background: #007bff;
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .form-container {
    background: #fff;
    padding: 15px;
    margin-top: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .input-field {
    width: 90%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .btn-group {
    display: flex;
    justify-content: space-between;
  }
  
  .save-btn, .cancel-btn, .view-btn, .delete-btn {
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .save-btn { background: #28a745; color: white; }
  .cancel-btn { background: #dc3545; color: white; }
  .view-btn { background: #007bff; color: white; }
  .delete-btn { background: #dc3545; color: white; }
  
  .chapters {
    margin-top: 20px;
  }
  
  .chapter-card {
    background: #f9f9f9;
    padding: 12px;
    margin-bottom: 10px;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  </style>
  