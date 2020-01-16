import Vue from "vue";
import Vuex from "vuex";

import blog from "./modules/blog";
import pages from "./modules/pages";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    blog,
    pages
  }
});
export default store;
