export const mutations = {
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
  },
  SET_LOAD_STAT_PAGE(state, page) {
    state.page = page;
  },
  SET_PAGE(state, page) {
    state.page = page;
  }
};
