<template>
  <div class="min-w-full lg:max-w-6xl">
    <div class="font-title truncate text-center h-18 md:h-44 mt-2">
      <div
        class="flex flex-wrap justify-center ml-3 mr-3 font-semibold text-m md:text-lg w-full"
      >
        <span
          v-for="(bC, i) in allBlogCateogries"
          :key="bC.id"
          class="m-1 md:m-2"
        >
          <span
            v-if="i == 0"
            class="cursor-pointer p-1 mr-3 md:p-2 text-gray-700 rounded bg-gray-100 hover:bg-gray-400"
            v-on:click="$store.commit('SET_BLOG_CATEGORY', '')"
            v-bind:class="selectCategory('')"
            >All ({{ filterBlogPostsByCategory("").length }})</span
          >
          <span
            class="cursor-pointer m-2 p-1 md:p-2 text-gray-700 rounded bg-gray-100 hover:bg-gray-400"
            v-on:click="$store.commit('SET_BLOG_CATEGORY', bC.id)"
            v-bind:class="selectCategory(bC.id)"
            v-if="filterBlogPostsByCategory(bC.id).length != 0"
            >{{ bC.category }} ({{
              filterBlogPostsByCategory(bC.id).length
            }})</span
          >
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters([
    "allBlogCateogries",
    "getBlogCategory",
    "filterBlogPostsByCategory",
  ]),
  created() {
    this.$store.dispatch("fetchBlogCategories");
  },
  methods: {
    selectCategory(category) {
      return {
        "bg-gray-400": category === this.getBlogCategory,
        "bg-gray-100": category !== this.getBlogCategory,
        "hover:bg-gray-400": category !== this.getBlogCategory,
      };
    },
  },
};
</script>
