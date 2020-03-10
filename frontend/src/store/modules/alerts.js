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
<<<<<<< HEAD
=======

>>>>>>> f647a84ffc3c959a0ac723192e80e4ac22e18910
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
