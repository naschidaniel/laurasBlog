<template>
  <div>
    <div class="flex flex-wrap">
      <div v-for="p in post" :key="p.title" class="w-full px-2 mt-3 md:w-1/2 lg:w-1/2 ">
        <div class="border border-lauraOrange rounded-lg shadow-md overflow-hidden">
          <img class="flex1" src="https://images.unsplash.com/photo-1556740738-b6a63e27c4df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80" alt="Woman paying for a purchase">
          <div class="pt-3 py-2 px-2">
            <h3 class="text-xl text-lauraOrange">{{ p.title }}</h3>
            <div class="pt-3 text-gray-900">
              <p class="h-20 break-words overflow-hidden whitespace-normal" >
                {{ p.content | substring}}
              <span v-if="p.truncate">
                ...
              </span>
              </p>
            </div>
            <div class="pt-3 pb-3 font-semibold">
              Kategorien:
                Stricken, Hude, Rudi
                <span class="sm:invisible md:visible"> | </span>
              <br class="md:hidden"> 
              www.naschi.info 
            </div>
          </div>
        </div>
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
        post: null,
      }
    },
    filters: {
      substring: function(string) {
        return string.substring(0, 200)
      }
    },
    mounted() {
      axios
        .get('/api/post/?format=json')
        .then(response => {
          var data = null
          data = response.data
          for ( var index=0; index<data.length; index++ ){
            if ( data[index].content.length >= '200' ) {
              data[index]['truncate'] = true
            }
          }

          console.log(data)
          return (this.post = data)
        })
    },
  };

</script>
