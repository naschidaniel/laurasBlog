<template>
  <div>
    <div class="flex flex-wrap">
      <div v-for="p in pages" :key="p.titel" class="">
        <h1 class="">
          {{ p.titel }}
        </h1>
        <div v-html="compiledMarkdown(p.content)"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import marked from "marked";

export default {
  name: "Pages",
  data() {
    return {
      pages: null
    };
  },
  methods: {
    compiledMarkdown: function(content) {
      return marked(content, { sanitize: true });
    }
  },
  mounted() {
    axios.get("/api/pages/?format=json").then(response => {
      return (this.pages = response.data);
    });
  }
};
</script>
