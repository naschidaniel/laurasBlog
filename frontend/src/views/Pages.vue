<template>
  <div>
    <Pages v-bind:link="this.link" />
  </div>
</template>

<script>
// @ is an alias to /src
import Pages from "@/components/Pages.vue";

export default {
  name: "pages",
  props: ["link"],
  components: {
    Pages
  }
};
</script>
