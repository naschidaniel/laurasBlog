import { actions } from "./blogActions";

export default {
  state: {
    lodStatBlogCategories: "notLoadingBlogCategories",
    blogCategories: "",
    lodStatBlogPosts: "notLoading",
    blogPosts: []
  },
  mutations: {
    SET_BLOG_CATEGORIES(state, blogCategories) {
      state.blogCategories = blogCategories;
    },
    SET_LOAD_STAT_BLOG_CATEGORIES(state, status) {
      state.lodStatBlogCategories = status;
    },
    SET_BLOG_POSTS(state, blogPosts) {
      state.blogPosts = blogPosts;
    },
    SET_LOAD_STAT_BLOG_POSTS(state, status) {
      state.lodStatBlogPosts = status;
    }
  },
  actions,
  getters: {
    allBlogCateogries: state => {
      return state.blogCategories;
    },
    getLoadingStatus: state => {
      return state.loadingStatus;
    },
    getBlogById: state => id => {
      if (state.blogPosts === "") {
        return "";
      } else {
        return state.blogPosts.find(blogPosts => blogPosts.id === Number(id));
      }
    },
    getblogCategoriesById: state => id => {
      if (state.blogCategories === "") {
        return "";
      } else {
        return state.blogCategories.find(
          blogCategories => blogCategories.id === id
        );
      }
    },
    allBlogPosts: state => {
      return state.blogPosts;
    }
  }
};
