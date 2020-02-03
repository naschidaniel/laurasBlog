<template>
  <div>
    <div class="flex flex-wrap">
      <div
        v-for="bp in allBlogPosts"
        :key="bp.title"
        class="w-full px-2 mt-3 md:w-1/2 "
      >
        <div class="shadow-md overflow-hidden">
          <div
            class="bg-cover bg-center"
            style="background-image: url('https://images.unsplash.com/photo-1556740738-b6a63e27c4df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80')"
          >
            <router-link :to="{ name: 'blogpost', params: { blogID: bp.id } }">
              <div
                class="flex content-center flex-wrap font-blogTitle bg-center h-64"
              >
                <div class=" bg-gray-200 text-center w-1/2">
                  <span
                    v-for="c in getblogCategoriesById(bp.category).breadcrumps"
                    :key="c"
                    class="text-l text-red-600 uppercase"
                    >{{ c }}
                  </span>
                  <br />
                  <h3 class="text-2XL text-gray-900">
                    {{ bp.title }}
                  </h3>
                  <span class="text-l">
                    Biwaktour
                  </span>
                </div>
              </div>
            </router-link>
          </div>
          <div class="pt-3 py-2 px-2">
            <div class="pt-3 text-gray-900">
              <p class="h-20 break-words overflow-hidden whitespace-normal">
                {{ bp.content | substring }}
                <span v-if="bp.truncate">
                  ...
                </span>
              </p>
            </div>
            <div class="pt-3 pb-3 font-semibold">
              Kategorien:
              <span class="invisible md:visible"> | </span>
              <br class="md:hidden" />
              www.naschi.info
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
  computed: mapGetters(["allBlogPosts", "getblogCategoriesById"]),
  filters: {
    substring: function(string) {
      return string.substring(0, 200);
    }
  },
  created() {
    this.$store.dispatch("fetchBlogPosts");
  }
};
</script>

<style scoped src="./markdown.css"></style>
