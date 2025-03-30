<template>
    <div>
        <NavbarPage />
        <div class="user-dashboard">
            <h2 class="dashboard-title">Subjects</h2>
            <div class="subject-list">
                <div v-for="subject in subjects" :key="subject.id" class="subject-card">
                    <h3 class="subject-title">{{ subject.name }}</h3>
                    <p class="subject-description">{{ subject.description }}</p>
                    <button class="view-button" @click="viewChapters(subject.id)">View Chapters</button>
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
    ...mapState(["subjects"])
  },
  methods: {
    ...mapActions(["fetchSubjects"]),
    viewChapters(subjectId) {
        console.log("Clicked subjectId:", subjectId); // Debugging
        this.$store.dispatch("fetchChapters", subjectId);
        this.$router.push(`/chapters/${subjectId}`);
    }
  },
  mounted(){
    this.fetchSubjects();
  },
};
</script>

<style scoped>
.Userdashboard {
    max-width: 900px;
    margin: 40px auto;
    padding: 20px;
    background: #951593;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
.dashboard-title {
    text-align: center;
    color: #ce181b;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 20px;
}

.subject-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.subject-card {
    background: #f8f9fa;;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    width: 250px;
    text-align: center;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.subject-card:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
}

.subject-title {
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

.view-button {
    background: #aed114;
    color: rgb(146, 68, 20);
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.2s ease-in-out;
}

.view-button:hover {
    background: #0056b3;
}
</style>