<template>
  <div class="mt-6 mb-8 flex flex-wrap">
    <h1 class=" text-3xl md:text-5xl text-red-600 font-blogCard">
      {{ getBlogById(blogID).title }}
    </h1>
    <img
      :src="getBlogById(blogID).mainImage_url"
      :alt="getBlogById(blogID).mainImageAlt"
      class="rounded shadow-2xl mt-6"
    />
    <div
      v-html="getBlogById(blogID).content"
      class="content mt-5 text-gray-700"
    ></div>
    <div class=" mx-auto mt-5 font-semibold text-lg md:text-2xl">
      <router-link
        :to="{ name: 'blogpost', params: { blogID: blogPostNavigation.back } }"
        v-if="blogPostNavigation.back != ''"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
      >
        zurück
      </router-link>
      <router-link
        to="/"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
        >Blog
      </router-link>
      <router-link
        :to="{ name: 'blogpost', params: { blogID: blogPostNavigation.next } }"
        v-if="blogPostNavigation.next != ''"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
      >
        vor
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { findIndex as _findIndex } from "lodash";

export default {
  props: {
    blogID: String
  },
  computed: {
    ...mapGetters([
      "getBlogById",
      "filterBlogPostsByCategory",
      "getBlogCategory"
    ]),
    blogPostNavigation: function navi() {
      const blogPosts = this.filterBlogPostsByCategory(this.getBlogCategory);
      let navigation = { back: "", current: "", next: "nextIndex" };
      if (blogPosts.length !== 0) {
        let currentIndex = _findIndex(blogPosts, ["id", Number(this.blogID)]);
        let back = "";
        let next = "";

        if (currentIndex !== blogPosts.length - 1) {
          back = blogPosts[currentIndex + 1].id;
        }

        if (currentIndex !== 0) {
          next = blogPosts[currentIndex - 1].id;
        }

        navigation = {
          back: back,
          current: blogPosts[currentIndex].id,
          next: next
        };
      }
      return navigation;
    }
  },
  created() {
    this.$store.dispatch("fetchBlogPosts");
  }
};
</script>

<style scoped src="./markdown.css"></style>
