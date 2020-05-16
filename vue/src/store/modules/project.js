import { api } from "@/api/api";

export default {
  getters: {
    appProject() {
      process.env.NODE_ENV === "development" ? console.log("The environment variable PROJECT is set: " + process.env.VUE_APP_PROJECT) : false;
      return process.env.VUE_APP_PROJECT;
    },
  },
};
