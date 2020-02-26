<template>
  <div id="app">
    <div class="antialiased flex flex-col min-h-screen">
      <navbar />
      <app-top />
      <main class=" mx-auto flex-grow w-full px-3 lg:max-w-6xl">
        <router-view />
      </main>
      <app-Footer />
    </div>
  </div>
</template>

<script>
import AppTop from "./AppTop.vue";
import AppFooter from "./AppFooter.vue";
import Navbar from "./Navbar.vue";
import "es6-promise/auto";

export default {
  name: "app",
  components: {
    Navbar,
    AppTop,
    AppFooter
  }
};
</script>
