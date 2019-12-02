<template>
  <div id="app">
    <div class="antialiased flex flex-col min-h-screen">
      <top></top>
      <navbar></navbar>
      <main class=" mx-auto flex-grow lg:max-w-6xl">
        <router-view />
        <BlogCategories></BlogCategories>
      </main>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Top from "./components/Top.vue";
import BlogCategories from "./components/BlogCategories.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "app",
  components: {
    Navbar,
    BlogCategories,
    Top,
    Footer
  }
};
</script>
