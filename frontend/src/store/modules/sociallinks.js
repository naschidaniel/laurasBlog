import { api } from "@/api/api";

export default {
  state: {
    loadingStatusSocialLinks: false,
    socialLinks: ""
  },
  mutations: {
    SET_LOADING_STATUS_SOCIAL_LINKS(state, loadingStatusSocialLinks) {
      state.loadingStatusSocialLinks = loadingStatusSocialLinks;
    },
    SET_SOCIAL_LINKS(state, socialLinks) {
      state.socialLinks = socialLinks;
    }
  },
  actions: {
    fetchSocialLinks({ commit }) {
      async function setSocialLinks() {
        commit("SET_LOADING_STATUS_SOCIAL_LINKS", true);
        let apiLink = "/api/socialmedialinks/?format=json";
        let res = await api(apiLink);
        commit("SET_SOCIAL_LINKS", res);
      }
      setSocialLinks();
      commit("SET_LOADING_STATUS_SOCIAL_LINKS", false);
    }
  },
  getters: {
    getSocialLinkByPlatform: state => Platform => {
      if (state.socialLinks == "") {
        return "";
      } else {
        return state.socialLinks.find(
          socialLinks => socialLinks.socialMediaPlatform === String(Platform)
        );
      }
    },
    getLoadingStatusSocialLinks: state => {
      return state.loadingStatusSocialLinks;
    }
  }
};
