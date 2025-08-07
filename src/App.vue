<template>
 <div id="app" class="app-container">
   <transition name="page-fade">
     <div v-if="isLoading" class="loading-overlay">
       <div class="loading-spinner">
         <div class="spinner"></div>
         <p class="mt-4 text-white">Loading...</p>
       </div>
     </div>
   </transition>
   <transition name="page-transition" mode="out-in">
     <router-view />
   </transition>
 </div>
</template>
<script>
export default {
 name: 'App',
 data() { return { isLoading: true }; },
 mounted() { setTimeout(() => { this.isLoading = false; }, 1000); }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; line-height: 1.6; color: #333; overflow-x: hidden; }
.app-container { min-height: 100vh; position: relative; }
.loading-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, #1f2937, #374151); display: flex; align-items: center; justify-content: center; z-index: 9999; }
.loading-spinner { text-align: center; }
.spinner { width: 50px; height: 50px; border: 3px solid rgba(255, 255, 255, 0.1); border-radius: 50%; border-top-color: #F59E0B; animation: spin 1s
ease-in-out infinite; margin: 0 auto; }
@keyframes spin { to { transform: rotate(360deg); } }
.page-transition-enter-active, .page-transition-leave-active { transition: all 0.4s ease; }
.page-transition-enter-from { opacity: 0; transform: translateY(20px); }
.page-transition-leave-to { opacity: 0; transform: translateY(-20px); }
.page-fade-enter-active, .page-fade-leave-active { transition: opacity 0.5s ease; }
.page-fade-enter-from, .page-fade-leave-to { opacity: 0; }
:root { --primary-50: #eff6ff; --primary-100: #dbeafe; --primary-200: #bfdbfe; --primary-300: #93c5fd; --primary-400: #60a5fa; --primary-500: #3b82f6; --primary-600: #2563eb; --primary-700: #1d4ed8; --primary-800: #1e40af; --primary-900: #1e3a8a; }
</style>
