import { createRouter, createWebHistory } from "vue-router";
import { HomeView, AboutView, ProfileView, LoginView } from "../views";

const routes = [
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/profile",
    name: "profile",
    component : ProfileView,
  },
  {
    path: "/",
    name: "Login",
    component : LoginView,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
