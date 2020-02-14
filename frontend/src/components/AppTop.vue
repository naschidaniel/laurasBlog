<template>
  <div class="min-w-full mx-auto lg:max-w-6xl">
    <div class="font-title truncate text-center h-18 md:h-44 mt-2 md:mt-8 align-middle px-3">
      <div
        class="text-3xl md:text-5xl ml-3 mr-3 truncate cursor-pointer"
        v-on:click="$store.commit('SET_BLOG_CATEGORY', '')"
      >
        <span class="text-gray-900">Milena</span>
        <span class="text-red-600">&</span>
        <span class="text-gray-900">her dog</span>
      </div>
      <div class="ml-3 mr-3">
        <span
          class="cursor-pointer p-2 text-gray-700 font-semibold rounded hover:bg-gray-100 md:text-l"
          v-on:click="$store.commit('SET_BLOG_CATEGORY', 1)"
        >All ({{ filterBlogPostsByCategory("").length }})</span>
        <span class="p-2" > - </span>
        <span v-for="(bC, i) in allBlogCateogries" :key="bC.id">
          <span
            class="cursor-pointer p-2 text-gray-700 font-semibold rounded hover:bg-gray-100 md:text-l"
            v-on:click="$store.commit('SET_BLOG_CATEGORY', bC.id)"
          >{{ bC.category }} ({{ filterBlogPostsByCategory(bC.id).length }})</span>
          <span v-if="i != allBlogCateogries.length - 1" class="p-2">-</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters(["allBlogCateogries", "filterBlogPostsByCategory"]),
  created() {
    this.$store.dispatch("fetchBlogCategories");
  }
};
</script>
