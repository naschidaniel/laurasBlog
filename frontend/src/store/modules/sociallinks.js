import { api } from "@/api/api";

export default {
  state: {
    loadStatusSocialLinks: "",
    socialLinks: ""
  },
  mutations: {
    SET_LOAD_STATUS_SOCIAL_LINKS(state, loadStatusSocialLinks) {
      state.loadStatusSocialLinks = loadStatusSocialLinks;
    },
    SET_SOCIAL_LINKS(state, socialLinks) {
      state.socialLinks = socialLinks;
    }
  },
  actions: {
    fetchSocialLinks({ commit }) {
      commit("SET_LOAD_STATUS_SOCIAL_LINKS", "loading");
      async function setSocialLinks() {
        let apiLink = "/api/socialmedialinks/?format=json";
        let res = await api(apiLink);
        commit("SET_SOCIAL_LINKS", res);
      }
      setSocialLinks();
      commit("SET_LOAD_STATUS_SOCIAL_LINKS", "notloading");
    }
  },
  getters: {
    getSocialLinkByPlatform: state => Platform => {
      if (state.socialLinks === "") {
        return "";
      } else {
        return state.socialLinks.find(
          socialLinks => socialLinks.socialMediaPlatform === String(Platform)
        );
      }
    }
  }
};
