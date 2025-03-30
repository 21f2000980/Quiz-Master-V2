<template>
    <div>
      <NavbarPage/>
      <div class="chapter-page">
        <div class="chapter-title"><h2>Chapters</h2></div>
        <div class="chapter-list">
          <div v-for="chapter in chapters" :key="chapter.id" class="chapter-card">
            <h3>{{ chapter.name }}</h3>
            <p>{{ chapter.description }}</p>
            <button class="take-quiz" @click="takeQuiz(chapter.id,chapter.name)">Take Quiz</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from "vuex";
  import NavbarPage from '../components/NavbarPage.vue';

  
  export default {
    components: { NavbarPage },
    computed: {
    ...mapState(["chapters"])
  },
    methods: {
    ...mapActions(["fetchChapters"]),
    takeQuiz(chapterId,chapterName) {
      this.$router.push({
        path: `/quiz/${chapterId}`,
        query: {name:chapterName }
      }
    );
    },
  },
  mounted() {
    const subjectId = this.$route.params.subjectId;
    this.fetchChapters(subjectId);
  },
};
  </script>
  
  <style scoped>
  .chapter-page {
    max-width: ;
    margin: 40px auto;
    padding: 20px;
    background: #951593;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.chapter-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.chapter-card {
    background: #f8f9fa;;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    width: 250px;
    text-align: center;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.chapter-card:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
}

.chapter-title {
    font-size: 20px;
    font-weight: bold;
    color: #007bff;
    margin-bottom: 10px;
}

.subject-description {
    font-size: 14px;
    color: #666;
    margin-bottom: 12px;
}

.take-quiz {
    background: #aed114;
    color: rgb(146, 68, 20);
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.2s ease-in-out;
}

.take-quiz:hover {
    background: #0056b3;
}
  </style>
  