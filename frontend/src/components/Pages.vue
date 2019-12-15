<template>
  <div>
    <h1 v-if="apiData.title">
      {{ apiData.title }}
    </h1>
    <div
      v-if="apiData.content"
      v-html="compileMarkdown(apiData.content)"
      class="content"
    ></div>
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
      this.getContent();
    }
  },
  methods: {
    compileMarkdown: function(string) {
      return marked(string);
    },

    getContent: function() {
      var url = "/api/pages/" + this.link + "?format=json";
      console.log("Page API URL: " + url);
      axios
        .get(url)
        .then(response => (this.apiData = response.data))
        .catch(error => console.log(error));
    }
  },
  mounted() {
    this.getContent();
  }
};
</script>

<style scoped>
.content >>> h2 {
  @apply text-2xl text-lauraOrange;
}

.content >>> h3 {
  @apply text-xl text-lauraOrange;
}

.content >>> ul {
  @apply list-inside;
}
.content >>> li {
  @apply list-disc;
}
</style>
