<template>
  <div class="antialiased text-gray-90">
    <div class="bg-gray-800 min-h-screen">
      <navbar></navbar>
      <Blog></Blog>
    </div>

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->

  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Blog from './components/Blog.vue'

  export default {
    name: 'app',
    components: {
      Navbar,
      Blog
    }
  }


</script>