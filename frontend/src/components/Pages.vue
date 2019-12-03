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
  methods: {
    compiledMarkdown: function(content) {
      return marked(content);
    }
  },
  mounted() {
    var url = "/api/pages/" + this.link + "?format=json";
    axios.get(url)
      .then(response => this.apiData = response.data)
      .catch(error => console.log(error));
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