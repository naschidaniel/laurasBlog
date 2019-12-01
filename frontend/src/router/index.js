import Vue from "vue";
import VueRouter from "vue-router";
import Blog from "../views/Blog.vue";
import About from "../views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "blog",
    component: Blog
  },
  {
    path: "/about",
    name: "about",
    component: About
  }
];

const router = new VueRouter({
  mode: "history",
  base: "/",
  routes
});

export default router;
