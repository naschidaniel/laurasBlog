<template>
  <div>
    <h1>
      {{ getPage.title }}
    </h1>
    <div v-html="getPage.content" class="content"></div>
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
