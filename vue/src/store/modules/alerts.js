export default {
  state: {
    NetworkError: false,
    NetworkErrorWindow: false
  },
  mutations: {
    SET_NETWORK_ERROR(state, NetworkError) {
      state.NetworkError = NetworkError;
    },
    SET_NETWORK_ERROR_WINDOW(state, NetworkErrorWindow) {
      state.NetworkErrorWindow = NetworkErrorWindow;
    }
  },
  actions: {
    setAlertError({ commit }, what, error) {
      if (what === "None") {
        commit("SET_NETWORK_ERROR_WINDOW", false);
        commit("SET_NETWORK_ERROR", false);
      } else if (what === "StatusError") {
        console.log("Api Status: " + error);
        commit("SET_NETWORK_ERROR_WINDOW", true);
        commit("SET_NETWORK_ERROR", true);
      } else {
        commit("SET_NETWORK_ERROR_WINDOW", true);
        commit("SET_NETWORK_ERROR", true);
        console.log("Error: " + error);
      }
    },
    setAlertErrorWindow({ commit }, value) {
      commit("SET_NETWORK_ERROR_WINDOW", value);
    }
  },
  getters: {
    getNetworkError: state => {
      return state.NetworkError;
    },
    getNetworkErrorWindow: state => {
      return state.NetworkErrorWindow;
    }
  }
};
