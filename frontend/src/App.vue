<template>
  <div id="app">
    <div class="antialiased">
      <top></top>
      <div
        class="flex bg-white border-gray-200 border-b shadow-sm sticky top-0 inset-x-0 z-100 h-16 items-center"
      >
        <navbar></navbar>
      </div>
      <div class=" lg:max-w-6xl mx-auto min-h-screen">
        <router-view />
        <BlogCategories></BlogCategories>
      </div>
    </div>
    <Footer></Footer>
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
