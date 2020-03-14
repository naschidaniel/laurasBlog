<template>
  <div
    class="bg-white border-b border-gray-400 shadow-lg sticky top-0 h-20 md:h-24 items-center z-40"
  >
    <header
      class="h-12 md:h-20 w-full mx-auto sm:flex sm:justify-between sm:items-center sm:px-4 sm:py-3 md:rounded-lg mt-2 lg:max-w-6xl"
    >
      <div
        class="flex items-center justify-between px-4 py-3 sm:p-2 md:text-2xl"
      >
        <router-link
          to="/"
          class="text-2xl md:text-4xl truncate cursor-pointer md:hidden"
        >
          <span class="text-gray-700">Milena</span>
          <span class="text-red-600"> & </span>
          <span class="text-gray-700">her dog</span>
        </router-link>
        <div class="sm:hidden">
          <button
            @click="clickHandler(getNavbarOpen, getAppClick)"
            type="button"
            class="block text-gray-700 hover:text-gray-900 focus:text-gray-900 focus:outline-none"
          >
            <svg class="h-8 w-8 fill-current" viewBox="0 0 24 24">
              <path
                v-if="getNavbarOpen"
                fill-rule="evenodd"
                d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"
              ></path>
              <path
                v-if="!getNavbarOpen"
                fill-rule="evenodd"
                d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
      <nav>
        <transition name="slide-fade">
          <div
            v-if="getNavbarOpen"
            class="px-2 pt-2 pb-4 bg-white border-b border-gray-400"
          >
            <router-link
              :to="{ name: 'blog' }"
              class="block p-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 text-xl hover:bg-gray-400"
              :class="selectBlogNavigation(['blog', 'blogpost'])"
            >
              Blog
            </router-link>
            <router-link
              :to="{ name: 'page', params: { link: 'about' } }"
              class="mt-1 block px-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 sm:ml-2 text-xl hover:bg-gray-400"
              :class="selectPageNavigation('about')"
            >
              About
            </router-link>
            <router-link
              :to="{ name: 'page', params: { link: 'kontakt' } }"
              class="mt-1 block px-2 py-1 text-gray-700 font-semibold rounded hover:bg-gray-100 text-xl hover:bg-gray-400"
              :class="selectPageNavigation('kontakt')"
            >
              Kontakt
            </router-link>
          </div>
        </transition>
        <div
          class="hidden sm:block mt-2 md:mt-0 text-gray-700 font-semibold text-xl md:text-3xl"
        >
          <router-link
            :to="{ name: 'blog' }"
            class="hover:bg-gray-100 hover:bg-gray-400 rounded p-2"
            v-bind:class="selectBlogNavigation(['blog', 'blogpost'])"
          >
            Blog
          </router-link>
          <router-link
            :to="{ name: 'page', params: { link: 'about' } }"
            class="hover:bg-gray-100 hover:bg-gray-400 rounded p-2 mx-2"
            v-bind:class="selectPageNavigation('about')"
          >
            About
          </router-link>
          <router-link
            :to="{ name: 'page', params: { link: 'kontakt' } }"
            class="hover:bg-gray-100 hover:bg-gray-400 rounded p-2"
            v-bind:class="selectPageNavigation('kontakt')"
          >
            Kontakt
          </router-link>
        </div>
      </nav>
    </header>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  computed: mapGetters(["getNavbarOpen", "getAppClick"]),
  methods: {
    clickHandler(isOpen, appClick) {
      this.$store.dispatch("setNavbarOpen", !isOpen);
      this.$store.dispatch("setAppClick", !appClick);
    },
    selectBlogNavigation(name) {
      return {
        "bg-gray-400": name.includes(this.$route.name)
      };
    },
    selectPageNavigation(link) {
      return {
        "bg-gray-400": link === this.$route.params.link
      };
    }
  }
};
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 0.2s;
}
.slide-fade-leave-active {
  transition: all 0.3s;
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
