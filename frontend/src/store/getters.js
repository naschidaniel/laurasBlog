export const getters = {
  allBlogCateogries: state => {
    return state.blogCategory;
  },
  getLoadingStatus: state => {
    return state.loadingStatus;
  },
  getblogCategoryById: state => id => {
    return state.blogCategory.find(blogCategory => blogCategory.id === id);
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
};
