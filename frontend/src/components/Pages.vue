<template>
  <div>
    <div class="flex flex-wrap">
      <h1 v-if="apiData" class="">
        {{ apiData.title }}
      </h1>
      <div
        v-if="apiData"
        v-html="compiledMarkdown(apiData.content)"
        class=""
      ></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import marked from "marked";

export default {
  props: {
    link: String
  },
  data() {
    return {
      apiData: null
    };
  },
  watch: { 
    link: function() {
      this.getContent()
    }
  },
  methods: {
    compiledMarkdown: function(content) {
      return marked(content);
    },
    getContent: function() {
      var url = "/api/pages/" + this.link + "?format=json";
      console.log("Page API URL: " + url)
      axios
        .get(url)
        .then(response => (this.apiData = response.data))
        .catch(error => console.log(error));
    }
  },
  mounted() {
    this.getContent()
  }
};
</script>

<style scoped>
h1 {
  @apply text-3xl;
}
h2 {
  @apply text-xl;
}
h3 {
  @apply text-lg;
}
</style>
