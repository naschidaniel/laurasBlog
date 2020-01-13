<template>
  <div>
    {{ getBlogById(blogID) }}
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    blogID: String
  },
  computed: mapGetters(["getBlogById"]),
  created() {
    this.$store.dispatch("fetchBlogPosts", "fetchBlogCategories");
  }
};
</script>
