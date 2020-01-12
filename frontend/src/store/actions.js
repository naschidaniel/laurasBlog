import axios from "axios";
import _ from "lodash";

import { getBlogPosts } from "../../api/blogPosts";
import { getBlogCategories } from "../../api/blogCategories";

export const actions = {
  fetchBlogCategories({ commit }) {
    async function setBlogCategories() {
      commit("SET_LOADING_STATUS", "loading");
      let res = await getBlogCategories();

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
      let res = await getBlogPosts();
      _.forEach(res, function(value) {
        if (value.content.length >= 200) {
          value["truncate"] = true;
        }
      });
      commit("SET_LOADING_STATUS", "notLoading");
      commit("SET_BLOG_POSTS", res);
    }
    setBlogPosts();
  },
  fetchPage({ commit }, link) {
    commit("SET_LOADING_STATUS", "loading");
    commit("SET_LINK", link);
    console.log("Page API URL: " + link);
    axios.get("api/pages/" + link + "?format=json").then(response => {
      var data = response.data;
      commit("SET_PAGE", data);
    });
  },
  fetchLink({ commit }, link) {
    commit("SET_LINK", link);
    console.log("LINK SET " + link);
  }
};
