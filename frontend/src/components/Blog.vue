<template>
  <div class="relative pb-5/6">
    Blog:
    <div v-for="p in post" :key="p.title" class="relative px-4 mt-1">
        <div class="bg-white p-6 rounded-lg shadow-lg">
          <pre>
            <h3 class="ml-1 ">{{ p.title }}</h3>
            <p>{{ p.content }}</p>
          </pre>
        </div>
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
