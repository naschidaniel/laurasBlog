<template>
  <div class="pt-4 px-4 pb-2">
    <h3 class="uppercase">Kategorien</h3>
    <ul v-for="bC in allBlogCateogries" :key="bC.id">
      <li class=" px-6">
        <span v-for="n in bC.breadcrumps.length" :key="n">-</span>
        {{ bC.category }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters(["allBlogCateogries", "getLoadingStatus"]),
  created() {
    this.$store.dispatch("fetchBlogCategories");
  }
};
</script>
