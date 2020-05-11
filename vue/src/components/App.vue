<template>
  <div id="app" class="z-2">
    <div
      class="flex justify-center w-screen h-screen absolute z-20 opacity-75"
      :class="setLoadingWindow(setSpinner())"
    >
      <ring-loader
        :loading="setSpinner()"
        color="#db3d3d"
        class="m-auto opacity-100"
      ></ring-loader>
    </div>

    <div @click="appClickHandler(getAppClick, getNavbarOpen)">
      <div class="antialiased flex flex-col min-h-screen">
        <navbar />
        <alerts class="mt-2" />
        <app-top />
        <main class="mx-auto flex-grow w-full px-3 lg:max-w-6xl">
          <router-view />
        </main>
        <app-Footer />
      </div>
    </div>
  </div>
</template>

<script>
import Alerts from "./Alerts.vue";
import AppTop from "./AppTop.vue";
import AppFooter from "./AppFooter.vue";
import Navbar from "./Navbar.vue";
import RingLoader from "vue-spinner/src/RingLoader.vue";
import "es6-promise/auto";
import { mapGetters } from "vuex";

export default {
  name: "app",
  computed: mapGetters([
    "getAppClick",
    "getNavbarOpen",
    "getLoadingStatusBlogPosts",
    "getLoadingStatusBlogQuotes",
    "getLoadingStatusPage",
    "getLoadingStatusSocialLinks",
  ]),
  methods: {
    appClickHandler(appClick, isOpen) {
      if (appClick === true && isOpen === true) {
        this.$store.commit("SET_APP_CLICK", false);
        this.$store.commit("SET_NAVBAR_OPEN", false);
      } else {
        this.$store.commit("SET_APP_CLICK", false);
      }
    },
    setSpinner() {
      if (
        this.getLoadingStatusBlogPosts ||
        this.getLoadingStatusBlogQuotes ||
        this.getLoadingStatusPage ||
        this.getLoadingStatusSocialLinks
      ) {
        return true;
      } else {
        return false;
      }
    },
    setLoadingWindow(setSpinner) {
      return {
        block: setSpinner,
        hidden: !setSpinner,
      };
    },
  },
  components: {
    Alerts,
    AppTop,
    AppFooter,
    Navbar,
    RingLoader,
  },
};
</script>
