import { actions } from "./blogActions";

export default {
  state: {
    lodStatBlogCategories: "notLoadingBlogCategories",
    blogCategories: "",
    blogCategory: "",
    lodStatBlogPosts: "notLoading",
    blogPosts: ""
  },
  mutations: {
    SET_BLOG_CATEGORIES(state, blogCategories) {
      state.blogCategories = blogCategories;
    },
    SET_BLOG_CATEGORY(state, id) {
      state.blogCategory = id;
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
    getBlogCategoriesById: state => id => {
      if (state.blogCategories === "") {
        return "";
      } else {
        return state.blogCategories.find(
          blogCategories => blogCategories.id === id
        );
      }
    },
    getBlogCategory: state => {
      return state.blogCategory;
    },
    filterBlogPostsByCategory: state => category => {
      if (state.blogPosts === "") {
        return "";
      } else {
        if (category !== "") {
          return state.blogPosts.filter(blogPosts => blogPosts.category === category);
        } else {
          return state.blogPosts;
        }
      }
    }
  }
};
