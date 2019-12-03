<template>
  <div>
    <Pages v-bind:link="$route.params.link" />
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
