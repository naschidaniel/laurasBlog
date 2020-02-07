<template>
  <div
    class="bg-white border-b border-gray-200 shadow-sm sticky top-0 h-16 md:h-18 items-center z-50"
  >
    <header
      class="h-12 w-full mx-auto sm:flex sm:justify-between sm:items-center sm:px-4 sm:py-3 md:rounded-lg mt-2 lg:max-w-6xl"
    >
      <div class="flex items-center justify-between px-4 py-3 sm:p-0 md:text-2xl">
        <div>
          Logo
        </div>
        <div class="sm:hidden">
          <button
            @click="isOpen = !isOpen"
            type="button"
            class="block text-gray-700 hover:text-gray-900 focus:text-gray-900 focus:outline-none"
          >
            <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
              <path
                v-if="isOpen"
                fill-rule="evenodd"
                d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"
              ></path>
              <path
                v-if="!isOpen"
                fill-rule="evenodd"
                d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
      <nav
        :class="isOpen ? 'block' : 'hidden'"
        class="px-2 pt-2 pb-4 sm:flex sm:p-0 bg-white rounded-b"
      >
        <router-link
          to="/"
          class="block px-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 md:text-2xl"
        >
          Blog
        </router-link>
        <router-link
          :to="{ name: 'page', params: { link: 'about' } }"
          class="mt-1 block px-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 sm:mt-0 sm:ml-2 md:text-2xl"
        >
          About
        </router-link>
        <router-link
          :to="{ name: 'page', params: { link: 'kontakt' } }"
          class="mt-1 block px-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 sm:mt-0 sm:ml-2 md:text-2xl"
        >
          Kontakt
        </router-link>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      isOpen: false
    };
  }
};
</script>
