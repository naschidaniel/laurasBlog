<template>
  <div class="mt-6 mb-8 flex flex-wrap">
    <h1 class="">
      {{ getBlogById(blogID).title }}
    </h1>
    <img
      :src="getBlogById(blogID).mainImage_url"
      class="rounded shadow-2xl"
    />
    <div v-html="getBlogById(blogID).content" class="content mt-5"></div>
    <div class=" mx-auto mt-5 font-semibold text-xs md:text-l">
      <router-link
        :to="{ name: 'blogpost', params: { blogID: blogPostNavigation.back } }"
        v-if="blogPostNavigation.back != ''"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
      >
        vorheriger Beitrag
      </router-link>
      <span v-if="blogPostNavigation.back != ''">-</span>
      <router-link
        to="/"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
        >zurück zur Übersicht
      </router-link>
      <span v-if="blogPostNavigation.next != ''">-</span>
      <router-link
        :to="{ name: 'blogpost', params: { blogID: blogPostNavigation.next } }"
        v-if="blogPostNavigation.next != ''"
        class="cursor-pointer p-1 md:p-2 text-gray-700 rounded m-2 bg-gray-100 hover:bg-gray-400"
      >
        nächster Beitrag
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { findIndex as _findIndex } from "lodash";

// import { indexOf as _indexOf } from "lodash";
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
    blogPostNavigation: function next() {
      const blogPosts = this.filterBlogPostsByCategory(this.getBlogCategory);
      let navigation = { back: "", current: "", next: "nextIndex" };
      if (blogPosts.length !== 0) {
        let currentIndex = _findIndex(blogPosts, ["id", Number(this.blogID)]);
        let back = "";
        let next = "";
        console.log(currentIndex);
        if (currentIndex !== 0) {
          back = blogPosts[currentIndex - 1].id;
        }

        console.log(blogPosts.length);
        if (currentIndex !== blogPosts.length - 1) {
          next = blogPosts[currentIndex + 1].id;
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
