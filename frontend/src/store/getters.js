export const getters = {
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
      return state.blogCategories.find(blogCategories => blogCategories.id === id);
    }
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
