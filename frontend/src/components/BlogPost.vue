<template>
  <div>
    {{ getBlogById(blogID) }}
    BlogID: {{ blogID }}
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    blogID: String
  },
  computed: mapGetters(["getBlogById"]),
  mounted() {
    this.$store.dispatch("fetchBlogPosts", "fetchBlogCategories");
  }
};
</script>
