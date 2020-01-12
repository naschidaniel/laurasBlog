import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import _ from "lodash";

import { getBlogPosts } from "../../api/blogPosts";
import { getBlogCategories } from "../../api/blogCategories";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loadingStatus: "notLoading",
    blogCategory: [],
    blogPosts: [],
    link: "",
    page: []
  },
  mutations: {
    SET_BLOG_CATEGORY(state, blogCategory) {
      state.blogCategory = blogCategory;
    },
    SET_LOADING_STATUS(state, status) {
      state.loadingStatus = status;
    },
    SET_BLOG_POSTS(state, blogPosts) {
      state.blogPosts = blogPosts;
    },
    SET_PAGE(state, page) {
      state.page = page;
    },
    SET_LINK(state, link) {
      state.link = link;
    }
  },

  actions: {
    fetchBlogCategories({ commit }) {
      async function setBlogCategories() {
        commit("SET_LOADING_STATUS", "loading");
        let res = await getBlogCategories();

        for (let index = 0; index < res.length; index++) {
          let breadcrumps = [res[index].category];
          let breadcrumpsID = [res[index].id];
          let k = res[index].parent;
          while (k != null) {
            if (k.parent != null) {
              breadcrumps.push(k.category);
              breadcrumpsID.push(k.id);
            } else {
              const parent = res[index].parent;
              let DataParent = res.filter(res => res.id === parent);
              breadcrumps.push(DataParent[0].category);
              breadcrumpsID.push(DataParent[0].id);
            }
            k = k.parent;
          }
          res[index]["breadcrumps"] = breadcrumps.reverse();
          res[index]["breadcrumpsID"] = breadcrumpsID.reverse();
        }

        _.orderBy(res, function(o) {
          return o.breadcrumps.join(" ");
        });
        commit("SET_LOADING_STATUS", "notLoading");
        commit("SET_BLOG_CATEGORY", res);
      }
      setBlogCategories();
    },
    fetchBlogPosts({ commit }) {
      commit("SET_LOADING_STATUS", "loading");
      async function setBlogPosts() {
        let res = await getBlogPosts();
        _.forEach(res, function(value) {
          if (value.content.length >= 200) {
            value["truncate"] = true;
          }
        });
        commit("SET_LOADING_STATUS", "notLoading");
        commit("SET_BLOG_POSTS", res);
      }
      setBlogPosts();
    },
    fetchPage({ commit }, link) {
      commit("SET_LOADING_STATUS", "loading");
      commit("SET_LINK", link);
      console.log("Page API URL: " + link);
      axios.get("api/pages/" + link + "?format=json").then(response => {
        var data = response.data;
        commit("SET_PAGE", data);
      });
    },
    fetchLink({ commit }, link) {
      commit("SET_LINK", link);
      console.log("LINK SET " + link);
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
      return state.blogCategory.find(
        blogCategory => blogCategory.parent === id
      );
    },
    allBlogPosts: state => {
      return state.blogPosts;
    },
    getPage: state => {
      return state.page;
    },
    getLink: state => {
      return state.link;
    }
  }
});
export default store;
