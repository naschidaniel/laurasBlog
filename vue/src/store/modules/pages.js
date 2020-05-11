import marked from "marked";
import { api } from "@/api/api";

export default {
  state: {
    loadingStatusPage: false,
    page: "",
  },
  mutations: {
    SET_LOADING_STATUS_PAGE(state, loadingStatusPage) {
      state.loadingStatusPage = loadingStatusPage;
    },
    SET_PAGE(state, page) {
      state.page = page;
    },
  },
  actions: {
    fetchPages({ commit }, link) {
      async function setPages() {
        commit("SET_LOADING_STATUS_PAGE", true);
        let apiLink = "/api/pages/" + link + "/?format=json";
        let res = await api(apiLink);
        res["content"] = marked(res.content);
        commit("SET_PAGE", res);
      }
      setPages();
      commit("SET_LOADING_STATUS_PAGE", false);
    },
  },
  getters: {
    getPage: (state) => {
      return state.page;
    },
    getLoadingStatusPage: (state) => {
      return state.loadingStatusPage;
    },
  },
};
