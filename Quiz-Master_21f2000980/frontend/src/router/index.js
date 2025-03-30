import { createRouter, createWebHistory } from "vue-router" ;

import HomePage from "../components/HomePage.vue";
import LoginPage from "../components/LoginPage.vue";
import RegisterPage from "../components/RegisterPage.vue";
import UserDashboard from "../views/UserDashboard.vue";
import ChapterPage from "../views/ChapterPage.vue"
import QuizPage from "../views/QuizPage.vue"
import AttemptQuiz from "../views/AttemptQuiz.vue"
import ScorePage from "../views/ScorePage.vue"


import adminDashboard from "../admin/adminDashboard.vue"
import manageChapter from "../admin/manageChapter.vue"
import manageQuiz from "../admin/manageQuiz.vue"
import manageQuestion from "../admin/manageQuestion.vue"
import ViewUser from "../admin/ViewUser.vue"
import adminChart from "../admin/adminChart.vue"


import store from "../store"



const routes = [

  //  routes for authorization 


    {path: "/", component: HomePage},
    {path: "/login",component: LoginPage},
    {path: "/register",component: RegisterPage},

    //  routes for user dashboard 


    {path: "/dashboard",component: UserDashboard,
        meta: {requiresAuth: true}
    },
  { path: "/chapters/:subjectId", component: ChapterPage },
  { path: "/quiz/:chapterId", component: QuizPage },
  { path: "/question/:quizId", component: AttemptQuiz },
  { path: "/score", component: ScorePage },

  //  routes for admin pages
   
  { path: "/admin", component: adminDashboard },
  { path: "/admin/userscore", component: ViewUser},
  { path: "/admin/:subjectId", component: manageChapter },
  { path: "/admin/:subjectId/:chapterId", component: manageQuiz},
  { path: "/admin/:subjectId/:chapterId/:quizId", component: manageQuestion},
  { path: "/admin/chart", component: adminChart},
  

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});


// Navigation Guard for Protected Routes
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
      next("/login");
    } else {
      next();
    }
  });

export default router;
