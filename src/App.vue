<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <!-- Navigation -->
    <Navbar />
    
    <!-- Main Content -->
    <main class="flex-1">
      <router-view />
    </main>
    
    <!-- Footer -->
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  }
}
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

/* Custom fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

body {
  font-family: 'Inter', sans-serif;
  line-height: 1.6;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  @apply bg-gray-100;
}

::-webkit-scrollbar-thumb {
  @apply bg-gray-400 rounded-full;
}

::-webkit-scrollbar-thumb:hover {
  @apply bg-gray-500;
}

/* Ensure proper text alignment and spacing */
.prose {
  text-align: left;
  max-width: none;
}

.prose p {
  margin-bottom: 1.25rem;
  text-align: left;
}

.prose h1, .prose h2, .prose h3, .prose h4, .prose h5, .prose h6 {
  text-align: left;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

/* Center content containers properly */
.container-center {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

/* Fix any text alignment issues */
.text-balance {
  text-wrap: balance;
}

/* Ensure buttons and CTAs are properly centered */
.btn-center {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

/* Responsive text alignment */
@media (max-width: 768px) {
  .mobile-center {
    text-align: center;
  }
}
</style>