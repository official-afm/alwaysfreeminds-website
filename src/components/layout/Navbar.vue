<template>
  <nav class="bg-white shadow-lg sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex-shrink-0 flex items-center group">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-700 rounded-xl flex items-center justify-center transform group-hover:scale-105 transition-transform duration-200">
                <span class="text-white font-bold text-sm">AFM</span>
              </div>
              <span class="text-xl font-bold text-gray-900 group-hover:text-primary-600 transition-colors duration-200">AlwaysFreeMinds</span>
            </div>
          </router-link>
        </div>

        <div class="hidden md:flex items-center space-x-1">
          <router-link 
            v-for="item in navigation" 
            :key="item.name"
            :to="item.href" 
            class="text-gray-600 hover:text-primary-600 px-4 py-2 text-sm font-medium transition-all duration-200 rounded-lg hover:bg-primary-50"
            :class="{ 'text-primary-600 bg-primary-50': $route.path === item.href }"
          >
            {{ item.name }}
          </router-link>
          
          <router-link 
            to="/contact" 
            class="ml-4 bg-primary-600 text-white px-6 py-2.5 rounded-lg text-sm font-medium hover:bg-primary-700 transition-all duration-200 shadow-md hover:shadow-lg transform hover:scale-105"
          >
            Get Started
          </router-link>
        </div>

        <div class="md:hidden flex items-center">
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="text-gray-400 hover:text-gray-500 focus:outline-none focus:text-gray-500 p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <div v-if="mobileMenuOpen" class="md:hidden border-t border-gray-200">
      <div class="px-2 pt-2 pb-3 space-y-1 bg-white">
        <router-link 
          v-for="item in navigation" 
          :key="item.name"
          :to="item.href" 
          @click="mobileMenuOpen = false"
          class="block px-3 py-2 text-base font-medium text-gray-600 hover:text-primary-600 hover:bg-primary-50 rounded-lg transition-colors duration-200"
          :class="{ 'text-primary-600 bg-primary-50': $route.path === item.href }"
        >
          {{ item.name }}
        </router-link>
        <router-link 
          to="/contact" 
          @click="mobileMenuOpen = false"
          class="block px-3 py-2 text-base font-medium bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors duration-200 text-center mt-4"
        >
          Get Started
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Navbar',
  setup() {
    const mobileMenuOpen = ref(false)
    
    const navigation = [
      { name: 'Home', href: '/' },
      { name: 'Blog', href: '/blog' },
      { name: 'Books', href: '/books' },
      { name: 'Consulting', href: '/consulting' },
      { name: 'About', href: '/about' },
    ]

    return {
      mobileMenuOpen,
      navigation
    }
  }
}
</script>
