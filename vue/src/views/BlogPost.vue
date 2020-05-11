<template>
  <BlogPost v-bind:blogID="String(this.blogID)" />
</template>

<script>
// @ is an alias to /src
import BlogPost from "@/components/BlogPost.vue";

export default {
  name: "blogpost",
  props: ["blogID"],
  components: {
    BlogPost,
  },
};
</script>
