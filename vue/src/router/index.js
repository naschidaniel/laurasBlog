import Vue from "vue";
import VueRouter from "vue-router";
import Blog from "../views/Blog.vue";
import BlogPost from "../views/BlogPost.vue";
import Pages from "../views/Pages.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "blog",
    component: Blog,
  },
  {
    path: "/blog/:blogID",
    name: "blogpost",
    props: true,
    component: BlogPost,
  },
  {
    path: "/pages/:link",
    name: "page",
    props: true,
    component: Pages,
  },
];

const scrollBehavior = (to, from, savedPosition) => {
  if (savedPosition) {
    return savedPosition;
  } else {
    return { x: 0, y: 0 };
  }
};

const router = new VueRouter({
  mode: "history",
  base: "/",
  routes,
  scrollBehavior,
});

export default router;
