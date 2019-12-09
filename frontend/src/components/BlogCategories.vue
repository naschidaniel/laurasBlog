<template>
  <div class="pt-4 px-4 pb-2">
    <h3 class="uppercase">Kategorien</h3>
    <ul>
      <li v-for="bC in blogCategories" :key="bC.category" class="pt-3">
        <span v-if="bC.breadcrumps.length == 1">{{ bC.breadcrumps[0] }}</span>
        <ul v-else>
          <li>
            <ul>
              <li class=" px-6">{{ bC.breadcrumps[1] }}</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Navbar",
  data() {
    return {
      blogCategories: null
    };
  },
  filters: {
    substring: function(string) {
      return string.substring(0, 200);
    }
  },
  mounted() {
    axios.get("/api/blogcategories/?format=json").then(response => {
      var data = response.data;
      console.log(data);
      for (var index = 0; index < response.data.length; index++) {
        var breadcrumps = [data[index].category];
        var breadcrumpsID = [data[index].id];
        var k = data[index].parent;

        while (k != null) {
          if (k.parent != null) {
            breadcrumps.push(k.category);
            breadcrumpsID.push(k.id);
          } else {
            var selectParent = data[index].parent - 1;
            breadcrumps.push(data[selectParent].category);
            breadcrumpsID.push(data[selectParent].id);
          }
          k = k.parent;
        }
        data[index]["breadcrumps"] = breadcrumps.reverse();
        data[index]["breadcrumpsID"] = breadcrumpsID.reverse();
      }
      return (this.blogCategories = data);
    });
  }
};
</script>
