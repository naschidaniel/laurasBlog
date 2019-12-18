<template>
  <div>
    <h1>
      {{ getPage.title }}
    </h1>
    <div
      v-html="getPage.content"
      class="content"
    ></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    link: String
  },
  computed: mapGetters(["getPage"]),
  watch: {
    link: function() {
      this.$store.dispatch("fetchPage", this.link);
    }
  },
  mounted() {
    console.log("link " +  this.link)
    this.$store.dispatch("fetchPage");
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
