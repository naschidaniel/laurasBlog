<template>
  <div>
    Links:
    <span>
            <ul>
                <li
                    v-for="ling in links"
                    :key="ling.site">
                    {{ ling.site }}
                </li>
            </ul>
        </span>
  </div>
</template>

<script>

  export default {
    name: 'Navbar',
    data() {
      return {
        links: [
          {
            site: 'about me',
            url: 'about'
          },
          {
            site: 'blog',
            url: 'blog'
          }
        ],
      }
    },
  }
</script>