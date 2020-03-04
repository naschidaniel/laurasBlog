import {
  delay as _delay,
  forEach as _forEach,
  orderBy as _orderBy
} from "lodash";

import marked from "marked";
import { api } from "@/api/api";

export const actions = {
  fetchBlogCategories({ state, commit }) {
    async function setBlogCategories() {
      commit("SET_LOAD_STAT_BLOG_CATEGORIES", "loading");
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

      let orderData = _orderBy(res, function(o) {
        return o.breadcrumps.join(" ");
      });
      commit("SET_BLOG_CATEGORIES", orderData);
      commit("SET_LOAD_STAT_BLOG_CATEGORIES", "notLoading");
    }

    if (state.blogCategories.length === 0) {
      setBlogCategories();
    }
  },
  fetchBlogPosts({ state, dispatch, commit }) {
    commit("SET_LOAD_STAT_BLOG_POSTS", "loading");
    async function setBlogPosts() {
      let res = await api("/api/blogposts/?format=json");
      _forEach(res, function(post) {
        if (post.content.length >= 200) {
          post["truncate"] = true;
        }
        post["content"] = marked(post.content);
      });
      commit("SET_BLOG_POSTS", res);
      commit("SET_LOAD_STAT_BLOG_POSTS", "notLoading");
    }

    if (state.blogCategories.length === 0) {
      setBlogPosts();
    }

    _delay(function() {
      if (
        state.lodStatBlogCategories === "notLoading" &&
        state.blogCategories.length === 0
      ) {
        dispatch("fetchBlogCategories");
      }
    }, 10);
  },
  fetchBlogQuotes({ state, dispatch, commit }) {
    commit("SET_LOAD_STAT_BLOG_QUOTES", "loading");
    async function setBlogQuotes() {
      let res = await api("/api/blogquotes/?format=json");
      _forEach(res, function(post) {
        post["content"] = marked(post.content);
      });
      commit("SET_BLOG_QUOTES", res);
      commit("SET_LOAD_STAT_BLOG_QUOTES", "notLoading");
    }

    if (state.blogCategories.length === 0) {
      setBlogQuotes();
    }

    _delay(function() {
      if (
        state.lodStatBlogCategories === "notLoading" &&
        state.blogCategories.length === 0
      ) {
        dispatch("fetchBlogCategories");
      }
    }, 20);
  }
};
