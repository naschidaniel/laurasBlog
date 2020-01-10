<template>
  <div class="pt-4 px-4 pb-2">
    <h3 class="uppercase">Kategorien</h3>
    <!-- {{ getblogCategoryById(1) }} -->
    {{ allBlogCateogries }}
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters([
    "allBlogCateogries",
    "getLoadingStatus",
    "getblogCategoryById"
  ]),
  mounted() {
    this.$store.dispatch("fetchBlogCategories");
  }
};
</script>
