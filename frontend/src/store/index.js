import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loadingStatus: "notLoading",
    blogCategory: null,
    sort_by: "breadcrups",
    sort_ascending: true,
    items: null
  },
  mutations: {
    SET_BLOG_CATEGORY(state, blogCategory) {
      state.blogCategory = blogCategory;
    },
    SET_LOADING_STATUS(state, status) {
      state.loadingStatus = status;
    }
  },
  actions: {
    fetchBlogCategories({ commit }) {
      commit("SET_LOADING_STATUS", "loading");
      axios.get("/api/blogcategories/?format=json").then(response => {
        var data = response.data;
        typeof data;
        for (var index = 0; index < response.data.length; index++) {
          var breadcrumps = [data[index].category];
          var breadcrumpsID = [data[index].id];
          var k = data[index].parent;

          while (k != null) {
            if (k.parent != null) {
              breadcrumps.push(k.category);
              breadcrumpsID.push(k.id);
            } else {
              const parent = data[index].parent;
              var DataParent = data.filter(data => data.id === parent);
              breadcrumps.push(DataParent[0].category);
              breadcrumpsID.push(DataParent[0].id);
            }
            k = k.parent;
          }
          data[index]["breadcrumps"] = breadcrumps.reverse();
          data[index]["breadcrumpsID"] = breadcrumpsID.reverse();
        }

        commit("SET_LOADING_STATUS", "notLoading");
        commit("SET_BLOG_CATEGORY", data);
      });
    }
  },
  getters: {
    allBlogCateogries: state => {
      return state.blogCategory;
    },
    getLoadingStatus: state => {
      return state.loadingStatus;
    },
    getblogCategoryById: state => id => {
      var rudi = state.blogCategory.find(blogCategory => blogCategory.parent === id);
      console.log(rudi);
      return rudi;
    }
  }
});

export default store;
