<template>
  <footer class=" border-t px-2 pt-2 pb-2 text-center w-full">
    <p>
      <router-link
        :to="{ name: 'page', params: { link: 'impressum' } }"
        class=""
      >
        Impressum
      </router-link>
      |
      <a href="#">laura@milena-and-her-dog.com</a>
    </p>
  </footer>
</template>
