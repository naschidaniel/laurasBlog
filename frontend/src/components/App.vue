<template>
  <div id="app">
    <div @click="appClickHandler(getAppClick, getIsOpen)">
      <div class="antialiased flex flex-col min-h-screen">
        <navbar />
        <app-top />
        <main class=" mx-auto flex-grow w-full px-3 lg:max-w-6xl">
          <router-view />
        </main>
        <app-Footer />
      </div>
    </div>
  </div>
</template>

<script>
import AppTop from "./AppTop.vue";
import AppFooter from "./AppFooter.vue";
import Navbar from "./Navbar.vue";
import "es6-promise/auto";
import { mapGetters } from "vuex";

export default {
  name: "app",
  computed: mapGetters(["getAppClick", "getIsOpen"]),
  methods: {
    appClickHandler(appClick, isOpen) {
      if (appClick === true && isOpen === true) {
        this.$store.commit("SET_APP_CLICK", false);
        this.$store.commit("SET_IS_OPEN", false);
      } else {
        this.$store.commit("SET_APP_CLICK", false);
      }
    }
  },
  components: {
    Navbar,
    AppTop,
    AppFooter
  }
};
</script>
