import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loadingStatus: "notLoading",
    blogCategory: null
  },
  mutations: {
    SET_LOADING_STATUS(state, status) {
      state.loadingStatus = status;
    },
    SET_BLOG_CATEGORY(state, blogCategory) {
      state.blogCategory = blogCategory;
    }
  },
  actions: {
    fetchBlogCategories(entrys) {
      entrys.commit("SET_LOADING_STATUS", "loading");
      axios.get("/api/blogcategories/?format=json").then(response => {
        var data = response.data;
        for (var index = 0; index < response.data.length; index++) {
          var breadcrumps = [data[index].category];
          var breadcrumpsID = [data[index].id];
          var k = data[index].parent;

          while (k != null) {
            if (k.parent != null) {
              breadcrumps.push(k.category);
              breadcrumpsID.push(k.id);
            } else {
              var selectParent = data[index].parent - 1;
              breadcrumps.push(data[selectParent].category);
              breadcrumpsID.push(data[selectParent].id);
            }
            k = k.parent;
          }
          data[index]["breadcrumps"] = breadcrumps.reverse();
          data[index]["breadcrumpsID"] = breadcrumpsID.reverse();
        }
        entrys.commit("SET_LOADING_STATUS", "notLoading");
        entrys.commit("SET_BLOG_CATEGORY", data);
      });
    }
  },
  getters: {
    allBlogCateogries: state => {
      return state.blogCategory
    },
    getLoadingStatus: state => {
      return state.loadingStatus
    }
  }
});

export default store;
