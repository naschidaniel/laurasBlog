import { api } from "@/api/api";

export default {
  getters: {
    appProject() {
      return process.env.VUE_APP_PROJECT;
    },
  },
};
