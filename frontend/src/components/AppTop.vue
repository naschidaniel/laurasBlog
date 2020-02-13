<template>
  <div class="min-w-full mx-auto lg:max-w-6xl">
    <div
      class="font-title truncate text-center h-18 md:h-44 mt-2 md:mt-8 align-middle px-3"
    >
      <div
        class="text-3xl md:text-5xl ml-3 mr-3 truncate cursor-pointer"
        v-on:click="$store.commit('SET_BLOG_CATEGORY', '')"
      >
        <span class="text-gray-900">Milena </span>
        <span class="text-red-600"> & </span>
        <span class="text-gray-900"> her dog</span>
      </div>
      <div class="ml-3 mr-3">
        <span v-for="(bC, i) in allBlogCateogries" :key="bC.id">
          <span
            class="px-2 cursor-pointer"
            v-on:click="$store.commit('SET_BLOG_CATEGORY', bC.id)"
          >
            {{ bC.category }}
          </span>
          <span v-if="i != allBlogCateogries.length - 1"> - </span>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters(["allBlogCateogries"]),
  created() {
    this.$store.dispatch("fetchBlogCategories");
  }
};
</script>
