<template>
  <article>
    Blog:
    <div v-for="p in post" :key="p.title">
      <pre>
        <h3>{{ p.title }}</h3>
        <p>{{ p.content }}</p>
      </pre>
    </div>
    <br>
    data:
    {{ post }}
  </article>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Navbar',
    data() {
      return {
        post: null
      }
    },
    mounted() {
      axios
        .get('/api/post/?format=json')
        .then(response => (this.post = response.data))
    }
  };

</script>
