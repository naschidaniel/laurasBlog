import { actions } from "./blogActions";

export default {
  state: {
    loadingStatusBlogCategories: "notLoadingBlogCategories",
    blogCategories: "",
    blogCategory: "",
    loadingStatusBlogPosts: false,
    blogPosts: "",
    loadingStatusBlogQuotes: false,
    blogQuotes: "",
  },
  mutations: {
    SET_BLOG_CATEGORIES(state, blogCategories) {
      state.blogCategories = blogCategories;
    },
    SET_BLOG_CATEGORY(state, id) {
      state.blogCategory = id;
    },
    SET_LOADING_STATUS_BLOG_CATEGORIES(state, status) {
      state.loadingStatusBlogCategories = status;
    },
    SET_BLOG_POSTS(state, blogPosts) {
      state.blogPosts = blogPosts;
    },
    SET_LOADING_STATUS_BLOG_POSTS(state, status) {
      state.loadingStatusBlogPosts = status;
    },
    SET_BLOG_QUOTES(state, blogQuotes) {
      state.blogQuotes = blogQuotes;
    },
    SET_LOADING_STATUS_BLOG_QUOTES(state, status) {
      state.loadingStatusBlogQuotes = status;
    },
  },
  actions,
  getters: {
    allBlogCateogries: (state) => {
      return state.blogCategories;
    },
    getLoadingStatusBlogPosts: (state) => {
      return state.loadingStatusBlogPosts;
    },
    getLoadingStatusBlogQuotes: (state) => {
      return state.loadingStatusBlogQuotes;
    },
    getBlogById: (state) => (id) => {
      if (state.blogPosts === "") {
        return "";
      } else {
        return state.blogPosts.find((blogPosts) => blogPosts.id === Number(id));
      }
    },
    getBlogCategoriesById: (state) => (id) => {
      if (state.blogCategories === "") {
        return "";
      } else {
        return state.blogCategories.find(
          (blogCategories) => blogCategories.id === id
        );
      }
    },
    getBlogCategory: (state) => {
      return state.blogCategory;
    },
    getBlogQuoteById: (state) => (id) => {
      if (state.blogQuotes === "") {
        return "";
      } else {
        return state.blogQuotes.find((blogQuotes) => blogQuotes.id === id);
      }
    },
    getBlogQuotesLen: (state) => {
      return state.blogQuotes.length;
    },
    filterBlogPostsByCategory: (state) => (category) => {
      if (state.blogPosts === "") {
        return "";
      } else {
        if (category !== "") {
          return state.blogPosts.filter(
            (blogPosts) => blogPosts.category === category
          );
        } else {
          return state.blogPosts;
        }
      }
    },
  },
};
