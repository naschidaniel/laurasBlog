<template>
  <div class=" mb-4 mt-4">
    <div class="flex flex-wrap">
      <div
        v-for="bp in filterBlogPostsByCategory(getBlogCategory)"
        :key="bp.id"
        class="w-full px-2 mt-3 mb-8"
      >
        <div class="shadow-md overflow-hidden">
          <div
            class="bg-cover bg-center"
            v-bind:style="{ backgroundImage: 'url(' + bp.mainImage_url + ')' }"
          >
            <router-link :to="{ name: 'blogpost', params: { blogID: bp.id } }">
              <div
                class="flex content-center flex-wrap font-blogCard bg-center h-64 md:h-128"
              >
                <div
                  class="w-4/5 bg-gray-200 mx-auto text-center  opacity-75 z-30"
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
                    {{ bp.subTitle }}
                  </span>
                </div>
              </div>
            </router-link>
          </div>
          <div class="pt-3 py-2 px-2">
            <div class="pt-3 text-gray-900">
              <p
                class="h-28 break-words overflow-hidden whitespace-normal text-lg"
              >
                {{ bp.abstract }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogPosts",
  props: {
    blogCategoryID: String
  },
  computed: mapGetters([
    "getBlogCategoriesById",
    "getBlogCategory",
    "filterBlogPostsByCategory"
  ]),
  created() {
    this.$store.dispatch("fetchBlogPosts");
  }
};
</script>
