<template>
  <div>
    harr: {{ blogID }}
    {{ getBlogById(blogID) }}
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    blogID: Number
  },
  computed: mapGetters(["getBlogById"])
};
</script>
