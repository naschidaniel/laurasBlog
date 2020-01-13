import _ from "lodash";
import marked from "marked";

import { api } from "../../api/api";

export const actions = {
  fetchBlogCategories({ commit }) {
    async function setBlogCategories() {
      commit("SET_LOADING_STATUS", "loading");
      let res = await api("/api/blogcategories/?format=json");

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

      let orderData = _.orderBy(res, function(o) {
        return o.breadcrumps.join(" ");
      });
      commit("SET_LOADING_STATUS", "notLoading");
      commit("SET_BLOG_CATEGORY", orderData);
    }
    setBlogCategories();
  },
  fetchBlogPosts({ commit }) {
    commit("SET_LOADING_STATUS", "loading");
    async function setBlogPosts() {
      let res = await api("/api/blogposts/?format=json");
      _.forEach(res, function(value) {
        if (value.content.length >= 200) {
          value["truncate"] = true;
        }
      });
      commit("SET_BLOG_POSTS", res);
      commit("SET_LOADING_STATUS", "notLoading");
    }
    setBlogPosts();
  },
  fetchPages({ commit }, link) {
    commit("SET_LOADING_STATUS", "loading");
    async function setPages() {
      let apiLink = "/api/pages/" + link + "/?format=json";
      let res = await api(apiLink);
      res["content"] = marked(res.content);
      commit("SET_PAGE", res);
    }
    setPages();
    commit("SET_LOADING_STATUS", "notloading");
  }
};
