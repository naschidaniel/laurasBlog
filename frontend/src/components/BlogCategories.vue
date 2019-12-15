<template>
  <div class="pt-4 px-4 pb-2">
    <h3 class="uppercase">Kategorien</h3>
    <ul>
      <li v-for="bC in blogCategories" :key="bC.category" class="pt-3">
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
export default {
  name: "blogCategory",
  computed: {
    loadingStatus () {
      return this.$store.getters.getLoadingStatus
    },
    blogCategories () {
      return this.$store.getters.allBlogCateogries
    }
  },
  mounted() {
    this.$store.dispatch('fetchBlogCategories')
  }
};
</script>
