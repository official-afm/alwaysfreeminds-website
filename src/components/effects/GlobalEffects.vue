<template>
 <div class="global-effects">
   <nav :class="['sticky-nav', { 'scrolled': isScrolled }]" class="fixed top-0 w-full z-50 transition-all duration-300">
     <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
       <div class="flex justify-between items-center py-4">
         <div class="flex items-center">
           <router-link to="/" class="text-2xl font-bold text-white hover:text-yellow-400 transition-colors">Always Free Minds</router-link>
         </div>
         <div class="hidden md:flex space-x-8">
           <router-link to="/" class="nav-link">Home</router-link>
           <router-link to="/about" class="nav-link">About</router-link>
           <router-link to="/consulting" class="nav-link">Consulting</router-link>
           <router-link to="/speaking" class="nav-link">Speaking</router-link>
           <router-link to="/contact" class="nav-link">Contact</router-link>
         </div>
         <div class="md:hidden">
           <button @click="toggleMobileMenu" class="text-white hover:text-yellow-400">
             <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
             </svg>
           </button>
         </div>
       </div>
       <div v-show="mobileMenuOpen" class="md:hidden pb-4">
         <div class="flex flex-col space-y-4">
           <router-link to="/" class="nav-link-mobile">Home</router-link>
           <router-link to="/about" class="nav-link-mobile">About</router-link>
           <router-link to="/consulting" class="nav-link-mobile">Consulting</router-link>
           <router-link to="/speaking" class="nav-link-mobile">Speaking</router-link>
           <router-link to="/contact" class="nav-link-mobile">Contact</router-link>
         </div>
       </div>
     </div>
   </nav>
   <div class="scroll-progress fixed top-0 left-0 h-1 bg-gradient-to-r from-yellow-400 to-blue-500 z-50 transition-all duration-300" :style="{ width: scrollProgress + '%' }"></div>
   <transition name="fab">
     <button v-show="showScrollTop" @click="scrollToTop" class="fixed bottom-8 right-8 z-40 bg-primary-600 hover:bg-primary-700 text-white p-4 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-110">
       <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
       </svg>
     </button>
   </transition>
 </div>
</template>
<script>
export default {
 name: 'GlobalEffects',
 data() { return { isScrolled: false, scrollProgress: 0, showScrollTop: false, mobileMenuOpen: false }; },
 mounted() { window.addEventListener('scroll', this.handleScroll); },
 beforeUnmount() { window.removeEventListener('scroll', this.handleScroll); },
 methods: {
   handleScroll() {
     const scrollTop = window.pageYOffset;
     const docHeight = document.documentElement.scrollHeight - window.innerHeight;
     this.isScrolled = scrollTop > 50;
     this.scrollProgress = (scrollTop / docHeight) * 100;
     this.showScrollTop = scrollTop > 300;
   },
   scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }); },
   toggleMobileMenu() { this.mobileMenuOpen = !this.mobileMenuOpen; }
 }
}
</script>
<style scoped>
.sticky-nav { background: rgba(17, 24, 39, 0.8); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
.sticky-nav.scrolled { background: rgba(17, 24, 39, 0.95); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); }
.nav-link { @apply text-white hover:text-yellow-400 transition-colors duration-200 font-medium; }
.nav-link-mobile { @apply text-white hover:text-yellow-400 transition-colors duration-200 font-medium py-2; }
.fab-enter-active, .fab-leave-active { transition: all 0.3s ease; }
.fab-enter-from, .fab-leave-to { opacity: 0; transform: scale(0.8) translateY(20px); }
</style>
