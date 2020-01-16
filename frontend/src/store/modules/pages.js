import marked from "marked";
import { api } from "@/api/api";

export default {
  state: {
    lodStatPage: [],
    page: []
  },
  mutations: {
    SET_LOAD_STAT_PAGES(state, page) {
      state.page = page;
    },
    SET_PAGE(state, page) {
      state.page = page;
    }
  },
  actions: {
    fetchPages({ commit }, link) {
      commit("SET_LOAD_STAT_PAGES", "loading");
      async function setPages() {
        let apiLink = "/api/pages/" + link + "/?format=json";
        let res = await api(apiLink);
        res["content"] = marked(res.content);
        commit("SET_PAGE", res);
      }
      setPages();
      commit("SET_LOAD_STAT_PAGES", "notloading");
    }
  },
  getters: {
    getPage: state => {
      return state.page;
    }
  }
};
