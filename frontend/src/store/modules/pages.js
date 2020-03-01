import marked from "marked";
import { api } from "@/api/api";

export default {
  state: {
    loadStatusPage: "",
    page: ""
  },
  mutations: {
    SET_LOAD_STATUS_PAGE(state, loadStatusPage) {
      state.loadStatusPage = loadStatusPage;
    },
    SET_PAGE(state, page) {
      state.page = page;
    }
  },
  actions: {
    fetchPages({ commit }, link) {
      commit("SET_LOAD_STATUS_PAGE", "loading");
      async function setPages() {
        let apiLink = "/api/pages/" + link + "/?format=json";
        let res = await api(apiLink);
        res["content"] = marked(res.content);
        commit("SET_PAGE", res);
      }
      setPages();
      commit("SET_LOAD_STATUS_PAGE", "notloading");
    }
  },
  getters: {
    getPage: state => {
      return state.page;
    }
  }
};
