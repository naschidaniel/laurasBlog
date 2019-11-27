<template>
  <div class="antialiased">
    <div class=" w-full lg:max-w-6xl mx-auto">
      <div class="font-title text-lg md:text-3xl text-gray-600 truncate text-center h-8 md:h-20 mt-2 md:mt-8 align-middle px-3">
        <span class="mr-3">
          Outdoor
        </span>
        <span class="ml-3 mr-3">
          Indoor
        </span>
        <span class="ml-3 mr-3">
          Dogstuff
        </span>
        <span class="ml-3">
          Knitting
        </span>
      </div>
    </div>
    <div class="flex bg-white border-gray-200 border-b shadow-sm sticky top-0 inset-x-0 z-100 h-16 items-center">
      <div class=" w-full max-w-screen-xl relative mx-auto">
        <navbar></navbar>
      </div>
    </div>
    <div class=" lg:max-w-6xl mx-auto min-h-screen">
      <blog></blog>
      <BlogCategories></BlogCategories>
    </div>
    <footer class=" border-t px-2 pt-2 pb-2 text-center w-full">
      <p>
        <a href="#" class="">Impressum</a> | <a href="#" class="">Datenschutz</a> | <a href="#">laura@milena-and-her-dog.com</a>
      </p>
    </footer>
  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Blog from './components/Blog.vue'
  import BlogCategories from './components/BlogCategories.vue'

  export default {
    name: 'app',
    components: {
      Navbar,
      Blog,
      BlogCategories
    }
  }


</script>