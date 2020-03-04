<template>
  <div class="mt-10">
    {{ blogQuoteID }}
    <div class="w-full px-2 mb-8 shadow-lg rounded">
      <div class="p-3">
        <img class="h-20 w-20 rounded-full mx-auto" :src="getBlogQuoteById(blogQuoteID).mainImage_url">
        <h2>
          {{ getBlogQuoteById(blogQuoteID).title }}
        </h2>
        <p class="text-lg">
          {{ getBlogQuoteById(blogQuoteID).content }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  props: {
    blogQuoteID: Number
  },
  computed: mapGetters([
    "getBlogQuoteById"
  ])
};
</script>