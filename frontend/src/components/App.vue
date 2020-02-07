<template>
  <div id="app">
    <div class="antialiased flex flex-col min-h-screen">
      <navbar></navbar>
      <app-top />
      <main class=" mx-auto flex-grow w-full px-3 lg:max-w-6xl">
        <router-view />
      </main>
      <!-- <BlogCategories class="mx-auto w-full px-3 lg:max-w-6xl"></BlogCategories> -->
      <app-Footer />
    </div>
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";
import AppTop from "./AppTop.vue";
import AppFooter from "./AppFooter.vue";
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
