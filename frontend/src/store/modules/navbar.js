import { delay as _delay } from "lodash";

export default {
  state: {
    appClick: false,
    navbarOpen: false
  },
  mutations: {
    SET_APP_CLICK(state, appClick) {
      state.appClick = appClick;
    },
    SET_NAVBAR_OPEN(state, navbarOpen) {
      state.navbarOpen = navbarOpen;
    }
  },
  actions: {
    setAppClick({ commit }, appClick) {
      _delay(function() {
        commit("SET_APP_CLICK", appClick);
      }, 5);
    },
    setNavbarOpen({ commit }, navbarOpen) {
      commit("SET_NAVBAR_OPEN", navbarOpen);
    }
  },
  getters: {
    getAppClick: state => {
      return state.appClick;
    },
    getNavbarOpen: state => {
      return state.navbarOpen;
    }
  }
};
