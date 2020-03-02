<template>
  <div>
    <h1>
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
img {md:w-1/3} 
img {md:mr-2} 
img {md:ml-2} 

.content >>> h1 {
@apply text-4xl text-red-600 mt-16;
}

.content >>> h2 {
@apply text-3xl text-red-600 mt-12;
}

.content >>> h3 {
@apply text-2xl text-red-600 mt-8;
}

.content >>> h4 {
@apply text-xl text-red-600 mt-4;
}

.content >>> ul {
@apply list-inside;
}

.content >>> li {
@apply list-disc;
}

.content >>> p {
@apply flex flex-wrap max-w-full justify-center p-2 mb-3 text-2xl text-justify;
}

.content >>> img {
@apply rounded shadow-2xl;
}
</style>


