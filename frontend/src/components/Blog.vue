<template>
  <div class="bg-gray-100">
    Blog:
    <div v-for="p in post" :key="p.title" class="bg-gray-700">
      <pre>
        <h3 class="ml-1 ">{{ p.title }}</h3>
        <p>{{ p.content }}</p>
      </pre>
    </div>
  </div>
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
