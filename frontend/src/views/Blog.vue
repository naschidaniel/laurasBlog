<template>
  <div>
    <Blog-top />
    <Blog />
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
