<template>
  <div>
    <h1>
      {{ getBlogById(blogID).title }}
    </h1>
    <div v-html="getBlogById(blogID).content" class="content"></div>
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
    this.$store.dispatch("fetchBlogPosts");
  }
};
</script>

<style scoped src="./markdown.css"></style>
