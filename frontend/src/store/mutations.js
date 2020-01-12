export const mutations = {
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
};
