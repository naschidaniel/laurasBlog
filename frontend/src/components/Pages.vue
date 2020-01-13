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
      this.$store.dispatch("fetchPage", this.link)
    }
  },
  computed: mapGetters(["getPage"]),
  created() {
    this.$store.dispatch("fetchPage", this.link)
  }
};
</script>

<style scoped>
.content >>> h2 {
  @apply text-2xl text-lauraOrange;
}

.content >>> h3 {
  @apply text-xl text-lauraOrange;
}

.content >>> ul {
  @apply list-inside;
}
.content >>> li {
  @apply list-disc;
}
</style>
