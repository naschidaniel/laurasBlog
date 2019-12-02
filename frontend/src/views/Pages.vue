<template>
  <div>
    <div>Page {{ $route.params.page }}</div>
    <Pages />
  </div>
    
</template>

<script>
// @ is an alias to /src
import Pages from "@/components/Pages.vue";

export default {
  name: "pages",
  components: {
    Pages
  }
};
</script>
