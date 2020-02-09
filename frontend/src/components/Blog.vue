<template>
  <div>
    <div class="flex flex-wrap">
      <div
        v-for="bp in allBlogPosts"
        :key="bp.title"
        class="w-full px-2 mt-3"
      >
        <div class="shadow-md overflow-hidden">
          <div
            class="bg-cover bg-center"
            style="background-image: url('https://images.unsplash.com/photo-1556740738-b6a63e27c4df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80')"
          >
            <router-link :to="{ name: 'blogpost', params: { blogID: bp.id } }">
              <div
                class="flex content-center flex-wrap font-blogCard bg-center h-64 md:h-128"
              >
                <div class="w-4/5 bg-gray-200 mx-auto text-center  opacity-75 z-30">
                  <span
                    v-for="c in getblogCategoriesById(bp.category).breadcrumps"
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
                    Untertitel
                  </span>
                </div>
              </div>
            </router-link>
          </div>
          <div class="pt-3 py-2 px-2">
            <div class="pt-3 text-gray-900">
              <p class="h-28 break-words overflow-hidden whitespace-normal text-lg">
                {{ bp.content | substring }}
                <span v-if="bp.truncate">
                  <router-link
                    :to="{ name: 'blogpost', params: { blogID: bp.id } }"
                  >
                    ...
                  </router-link>
                </span>
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
