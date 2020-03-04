import { actions } from "./blogActions";

export default {
  state: {
    lodStatBlogCategories: "notLoadingBlogCategories",
    blogCategories: "",
    blogCategory: "",
    lodStatBlogPosts: "notLoading",
    blogPosts: "",
    lodStatBlogQuotes: "notLoading",
    blogQuotes: ""
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
    },
    SET_BLOG_QUOTES(state, blogQuotes) {
      state.blogQuotes = blogQuotes;
    },
    SET_LOAD_STAT_BLOG_QUOTES(state, status) {
      state.lodStatBlogQuotes = status;
    }
  },
  actions,
  getters: {
    allBlogCateogries: state => {
      return state.blogCategories;
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
          return state.blogPosts.filter(
            blogPosts => blogPosts.category === category
          );
        } else {
          return state.blogPosts;
        }
      }
    },
    filterBlogQuotesByCategory: state => category => {
      if (state.blogQuotes === "") {
        return "";
      } else {
        if (category !== "") {
          return state.blogQuotes.filter(
            blogQuotes => blogQuotes.category === category
          );
        } else {
          return state.blogQuotes;
        }
      }
    }
  }
};
