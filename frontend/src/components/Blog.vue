<template>
  <div>
    <div class="flex flex-wrap">
      <div
        v-for="bp in allBlogPosts"
        :key="bp.title"
        class="w-full px-2 mt-3 md:w-1/2 "
      >
        <div
          class="border border-lauraOrange rounded-lg shadow-md overflow-hidden"
        >
          <img
            class="flex1"
            src="https://images.unsplash.com/photo-1556740738-b6a63e27c4df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80"
            alt="Woman paying for a purchase"
          />
          <div class="pt-3 py-2 px-2">
            <h3 class="text-xl text-lauraOrange">
              <router-link
          :to="{ name: 'blogpost', params: { blogID: bp.id } }"
        >
          {{ bp.title }}
        </router-link>
              </h3>
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
              <span
                v-for="c in getblogCategoryById(bp.category).breadcrumps"
                :key="c"
                >{{ c }}
              </span>
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
  computed: mapGetters(["allBlogPosts", "getblogCategoryById"]),
  filters: {
    substring: function(string) {
      return string.substring(0, 200);
    }
  },
  mounted() {
    this.$store.dispatch("fetchBlogPosts", "fetchBlogCategories");
  }
};
</script>
