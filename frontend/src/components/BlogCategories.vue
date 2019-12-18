<template>
  <div class="pt-4 px-4 pb-2">
    <h3 class="uppercase">Kategorien</h3>
    {{ getblogCategoryById(1) }}
    <ul>
      <li v-for="bC in allBlogCateogries" :key="bC.category" class="pt-3">
        <span v-if="bC.breadcrumps.length == 1">{{ bC.breadcrumps[0] }}</span>
        <ul v-else>
          <li>
            <ul>
              <li class=" px-6">{{ bC.breadcrumps[1] }}</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  computed: mapGetters(["allBlogCateogries", "getLoadingStatus", "getblogCategoryById"]),
  mounted() {
    this.$store.dispatch("fetchBlogCategories");
  }
};
</script>
