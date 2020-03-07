<template>
  <div>
    <h1 class="content">
      {{ getPage.title }}
    </h1>
    <div v-html="getPage.content" class="content text-gray-700"></div>
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

<style scoped>
img {md:w-1/3;}
img {md:mr-2;}
img {md:ml-2;}
.content >>> h1 {
  @apply text-3xl text-red-600 mt-8;
}
.content >>> h2 {
  @apply text-xl text-red-600 mt-6;
}
.content >>> h3 {
  @apply text-lg text-red-600 mt-4;
}
.content >>> h4 {
  @apply text-base text-red-600 mt-3;
}
.content >>> ul {
  @apply list-inside;
}
.content >>> li {
  @apply list-disc;
}
.content >>> p {
  @apply flex flex-wrap max-w-full justify-center p-2 mb-3 text-base text-justify;
}
.content >>> img {
  @apply rounded shadow-2xl m-3;
}
</style>
