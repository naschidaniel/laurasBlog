<template>
  <div id="app" class="container mx-auto py-10">
    <Blog></Blog>

    <navbar></navbar>

    <img alt="Vue logo" src="./assets/logo.png" class="center">
    <HelloWorld msg="Welcome to Your Vue.js App"/>

  </div>
</template>

<script>
  import HelloWorld from './components/HelloWorld.vue'
  import Navbar from './components/Navbar'
  import Blog from './components/Blog'

  export default {
    name: 'app',
    components: {
      HelloWorld,
      Navbar,
      Blog
    }
  }


</script>