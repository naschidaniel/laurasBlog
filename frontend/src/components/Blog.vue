<template>
  <div class="mt-2">
    <div class="flex flex-wrap">
      <div
        v-for="(bp, index) in filterBlogPostsByCategory(getBlogCategory)"
        :key="bp.id"
        class="w-full px-2 mt-3 mb-8"
      >
        <div class="shadow-md rounded overflow-hidden">
          <div
            class="bg-cover bg-center"
            :style="{ backgroundImage: 'url(' + bp.mainImage_url + ')' }"
            :title="bp.mainImageAlt"
          >
            <router-link :to="{ name: 'blogpost', params: { blogID: bp.id } }">
              <div
                class="flex content-center flex-wrap font-blogCard bg-center h-64 md:h-128"
              >
                <div
                  class="w-4/5 bg-gray-200 mx-auto text-center opacity-75 z-30"
                >
                  <span
                    v-for="c in getBlogCategoriesById(bp.category).breadcrumps"
                    :key="c"
                    class="text-l md:text-2xl text-red-600 uppercase"
                    >{{ c }}
                  </span>
                  <br />
                  <h3
                    class="text-2XL md:text-4xl text-gray-900 leading-none text-content"
                  >
                    {{ bp.title }}
                  </h3>
                  <span class="text-l md:text-2xl">
                    {{ bp.subtitle }}
                  </span>
                </div>
              </div>
            </router-link>
          </div>
          <div class="p-2 text-gray-700">
            <p
              class="h-28 break-words overflow-hidden whitespace-normal text-xl text-justify p-3"
            >
              {{ bp.abstract }}
            </p>
          </div>
        </div>
        <div
          v-if="
            [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29].includes(index + 1) &&
              getBlogQuotesLen > index
          "
        >
          <blog-quote :blogQuoteID="index + 1"></blog-quote>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import BlogQuote from "./BlogQuote.vue";

export default {
  name: "blogPosts",
  props: {
    blogCategoryID: String
  },
  components: {
    BlogQuote
  },
  computed: mapGetters([
    "getBlogCategoriesById",
    "getBlogCategory",
    "filterBlogPostsByCategory",
    "getBlogQuotesLen"
  ]),
  created() {
    this.$store.dispatch("fetchBlogPosts");
    this.$store.dispatch("fetchBlogQuotes");
  }
};
</script>
