export const getters = {
  allBlogCateogries: state => {
    return state.blogCategory;
  },
  getLoadingStatus: state => {
    return state.loadingStatus;
  },
  getBlogById: state => id => {
    if (state.blogPosts === "") {
      console.log("state.blogPosts = ", state.blogPosts);
      return "";
    } else {
      return state.blogPosts.find(blogPosts => blogPosts.id === id);
    }
  },
  getblogCategoryById: state => id => {
    if (state.blogCategory === "") {
      console.log("state.blogCategory = ", state.blogCategory);
      return "";
    } else {
      return state.blogCategory.find(blogCategory => blogCategory.id === id);
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
