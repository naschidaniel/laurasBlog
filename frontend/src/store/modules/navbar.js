import { delay as _delay } from "lodash";

export default {
  state: {
    appClick: false,
    isOpen: false
  },
  mutations: {
    SET_APP_CLICK(state, appClick) {
      state.appClick = appClick;
    },
    SET_IS_OPEN(state, isOpen) {
      state.isOpen = isOpen;
    }
  },
  actions: {
    setAppClick({ commit }, appClick) {
      _delay(function() {
        commit("SET_APP_CLICK", appClick);
      }, 10);
    },
    setIsOpen({ commit }, isOpen) {
      commit("SET_IS_OPEN", isOpen);
    }
  },
  getters: {
    getAppClick: state => {
      return state.appClick;
    },
    getIsOpen: state => {
      return state.isOpen;
    }
  }
};
