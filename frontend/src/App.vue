<template>
  <div id="app">
    <div class="antialiased flex flex-col min-h-screen">
      <app-top />
      <navbar></navbar>
        <main class=" mx-auto flex-grow w-full px-3 lg:max-w-6xl">
         <router-view/>
        </main>
      <BlogCategories class="mx-auto w-full px-3 lg:max-w-6xl"></BlogCategories>
      <app-Footer />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import AppTop from "./components/AppTop.vue";
import BlogCategories from "./components/BlogCategories.vue";
import AppFooter from "./components/AppFooter.vue";

export default {
  name: "app",
  components: {
    Navbar,
    BlogCategories,
    AppTop,
    AppFooter
  }
};
</script>
