<template>
  <div>
    <h1 class="text-3xl md:text-5xl text-red-600 font-content">
      {{ getPage.title }}
    </h1>
    <div
      v-html="getPage.content"
      class="content font-content text-gray-700"
    ></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    link: String
  },
  watch: {
    link: function() {
      this.$store.dispatch("fetchPages", this.link);
    }
  },
  computed: mapGetters(["getPage"]),
  created() {
    this.$store.dispatch("fetchPages", this.link);
  }
};
</script>

<style scoped src="./markdown.css"></style>
