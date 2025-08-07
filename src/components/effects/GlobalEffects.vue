<template>
  <div class="global-effects">
    <!-- Sticky Navigation -->
    <nav 
      :class="['sticky-nav', { 'scrolled': isScrolled }]"
      class="fixed top-0 w-full z-50 transition-all duration-300"
    >
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <!-- Logo -->
          <div class="flex items-center">
            <router-link to="/" class="text-2xl font-bold text-white hover:text-yellow-400 transition-colors">
              Always Free Minds
            </router-link>
          </div>
          
          <!-- Navigation Links -->
          <div class="hidden md:flex space-x-8">
            <router-link to="/" class="nav-link">Home</router-link>
            <router-link to="/about" class="nav-link">About</router-link>
            <router-link to="/consulting" class="nav-link">Consulting</router-link>
            <router-link to="/speaking" class="nav-link">Speaking</router-link>
            <router-link to="/contact" class="nav-link">Contact</router-link>
          </div>
          
          <!-- Mobile Menu Button -->
          <div class="md:hidden">
            <button @click="toggleMobileMenu" class="text-white hover:text-yellow-400">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Mobile Menu -->
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

    <!-- Scroll Progress Bar -->
    <div 
      class="scroll-progress fixed top-0 left-0 h-1 bg-gradient-to-r from-yellow-400 to-blue-500 z-50 transition-all duration-300"
      :style="{ width: scrollProgress + '%' }"
    ></div>

    <!-- Floating Action Button -->
    <transition name="fab">
      <button 
        v-show="showScrollTop"
        @click="scrollToTop"
        class="fixed bottom-8 right-8 z-40 bg-primary-600 hover:bg-primary-700 text-white p-4 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-110"
      >
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
        </svg>
      </button>
    </transition>

    <!-- Parallax Background Elements -->
    <div class="parallax-container">
      <div 
        class="parallax-element parallax-slow"
        :style="{ transform: `translateY(${parallaxSlow}px)` }"
      >
        <div class="absolute top-20 left-10 w-64 h-64 bg-blue-500 opacity-10 rounded-full blur-3xl"></div>
      </div>
      <div 
        class="parallax-element parallax-medium"
        :style="{ transform: `translateY(${parallaxMedium}px)` }"
      >
        <div class="absolute top-96 right-20 w-48 h-48 bg-yellow-400 opacity-15 rounded-full blur-2xl"></div>
      </div>
      <div 
        class="parallax-element parallax-fast"
        :style="{ transform: `translateY(${parallaxFast}px)` }"
      >
        <div class="absolute top-1/2 left-1/3 w-32 h-32 bg-purple-500 opacity-20 rounded-full blur-xl"></div>
      </div>
    </div>

    <!-- Cursor Trail Effect -->
    <div 
      v-for="(dot, index) in cursorTrail" 
      :key="index"
      class="cursor-dot"
      :style="{ 
        left: dot.x + 'px', 
        top: dot.y + 'px',
        opacity: dot.opacity 
      }"
    ></div>
  </div>
</template>

<script>
export default {
  name: 'GlobalEffects',
  data() {
    return {
      isScrolled: false,
      scrollProgress: 0,
      showScrollTop: false,
      mobileMenuOpen: false,
      parallaxSlow: 0,
      parallaxMedium: 0,
      parallaxFast: 0,
      cursorTrail: [],
      mouseX: 0,
      mouseY: 0
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
    window.addEventListener('mousemove', this.handleMouseMove);
    this.updateParallax();
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
    window.removeEventListener('mousemove', this.handleMouseMove);
  },
  methods: {
    handleScroll() {
      const scrollTop = window.pageYOffset;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      
      // Update scroll states
      this.isScrolled = scrollTop > 50;
      this.scrollProgress = (scrollTop / docHeight) * 100;
      this.showScrollTop = scrollTop > 300;
      
      // Update parallax
      this.updateParallax();
    },
    
    updateParallax() {
      const scrollTop = window.pageYOffset;
      this.parallaxSlow = scrollTop * 0.2;
      this.parallaxMedium = scrollTop * 0.5;
      this.parallaxFast = scrollTop * 0.8;
    },
    
    handleMouseMove(e) {
      this.mouseX = e.clientX;
      this.mouseY = e.clientY;
      
      // Add cursor trail dot
      this.cursorTrail.push({
        x: e.clientX,
        y: e.clientY,
        opacity: 1
      });
      
      // Limit trail length and fade dots
      if (this.cursorTrail.length > 15) {
        this.cursorTrail.shift();
      }
      
      this.cursorTrail.forEach((dot, index) => {
        dot.opacity = (index + 1) / this.cursorTrail.length * 0.5;
      });
    },
    
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    },
    
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    }
  }
}
</script>

<style scoped>
.sticky-nav {
  background: rgba(17, 24, 39, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sticky-nav.scrolled {
  background: rgba(17, 24, 39, 0.95);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.nav-link {
  @apply text-white hover:text-yellow-400 transition-colors duration-200 font-medium;
}

.nav-link-mobile {
  @apply text-white hover:text-yellow-400 transition-colors duration-200 font-medium py-2;
}

.parallax-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  pointer-events: none;
  z-index: -1;
}

.parallax-element {
  position: absolute;
  width: 100%;
  height: 100%;
}

.cursor-dot {
  position: fixed;
  width: 4px;
  height: 4px;
  background: linear-gradient(45deg, #3B82F6, #F59E0B);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transition: opacity 0.3s ease;
}

.fab-enter-active, .fab-leave-active {
  transition: all 0.3s ease;
}

.fab-enter-from, .fab-leave-to {
  opacity: 0;
  transform: scale(0.8) translateY(20px);
}

@media (max-width: 768px) {
  .cursor-dot {
    display: none;
  }
}
</style>
