<template>
  <div id="app">
    <div class="antialiased">
      <top></top>
      <div class="flex bg-white border-gray-200 border-b shadow-sm sticky top-0 inset-x-0 z-100 h-16 items-center">
        <div class=" w-full max-w-screen-xl relative mx-auto">
          <navbar></navbar>
        </div>
      </div>
      <div class=" lg:max-w-6xl mx-auto min-h-screen">
        <blog></blog>
        <BlogCategories></BlogCategories>
      </div>
      <div>
        <pages></pages>
      </div>
      <footer class=" border-t px-2 pt-2 pb-2 text-center w-full">
        <p>
          <a href="#" class="">Impressum</a> | <a href="#" class="">Datenschutz</a> | <a href="#">laura@milena-and-her-dog.com</a>
        </p>
      </footer>
    </div>
    <router-view />
  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Top from './components/Top.vue'
  import Blog from './components/Blog.vue'
  import BlogCategories from './components/BlogCategories.vue'
  import Pages from './components/Pages.vue'

  export default {
    name: 'app',
    components: {
      Navbar,
      Blog,
      BlogCategories,
      Pages,
      Top
    }
  }
</script>