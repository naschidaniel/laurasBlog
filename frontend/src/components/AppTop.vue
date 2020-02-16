<template>
  <div class="min-w-full mx-auto lg:max-w-6xl">
    <div
      class="font-title truncate text-center h-18 md:h-44 mt-2 md:mt-4 align-middle px-3"
    >
      <router-link
        to="/"
        class="text-3xl md:text-5xl ml-3 mr-3 truncate cursor-pointer"
      >
        <span class="text-gray-900">Milena</span>
        <span class="text-red-600">&</span>
        <span class="text-gray-900">her dog</span>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "appTop"
};
</script>
