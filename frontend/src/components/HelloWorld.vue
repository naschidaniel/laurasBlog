<template>
  <div class="hello">
    <h1>{{ msg }}</h1>

      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
       <li
               v-for="name in rudi"
               :key="name"
       >{{ name }}
       </li>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data (){
    return {
          rudi: ['foo', 'bar', 'baz']
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
