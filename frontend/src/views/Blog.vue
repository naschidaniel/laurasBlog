<template>
  <div>
    <Blog-top class=" mt-2"></Blog-top>
    <Blog class=" mt-5"></Blog>
  </div>
</template>

<script>
// @ is an alias to /src
import Blog from "@/components/Blog.vue";
import BlogTop from "@/components/BlogTop.vue";

export default {
  name: "blog",
  components: {
    Blog,
    BlogTop
  }
};
</script>
