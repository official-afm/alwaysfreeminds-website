<template>
  <div class="consulting-page">
    <!-- Global Effects Component -->
    <GlobalEffects />
    
    <!-- Parallax Hero Section -->
    <section class="parallax-hero bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white relative overflow-hidden">
      <!-- Animated background elements -->
      <div class="absolute inset-0">
        <div class="blob absolute top-20 left-10 w-64 h-64 bg-blue-500 opacity-20"></div>
        <div class="blob absolute bottom-20 right-10 w-48 h-48 bg-yellow-400 opacity-15" style="animation-delay: -2s;"></div>
        <div class="blob absolute top-1/2 left-1/2 w-32 h-32 bg-purple-500 opacity-25" style="animation-delay: -4s;"></div>
      </div>
      
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <h1 class="text-4xl md:text-5xl font-bold mb-6 fade-in-up gradient-text">
          Transform Your Organization with Proven Second-Chance Strategies
        </h1>
        <p class="text-xl md:text-2xl mb-8 text-gray-200 max-w-3xl mx-auto leading-relaxed fade-in-up" style="animation-delay: 0.2s;">
          Reduce turnover by 40%, build diverse teams, and unlock untapped talent with insights from someone who's lived the transformation.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center fade-in-up" style="animation-delay: 0.4s;">
          <button 
            @click="scrollToBooking" 
            class="btn-enhanced inline-flex items-center justify-center bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg"
          >
            Let's Have a Conversation
          </button>
        </div>
      </div>
    </section>

    <!-- Animated Sections Wrapper -->
    <AnimatedSections :section-count="6">
      <!-- Social Proof -->
      <template #section-0="{ isVisible }">
        <section class="py-12 bg-gray-50" :class="{ 'animate': isVisible }">
          <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-8">
              <p class="text-gray-600 text-lg stagger-animation">Trusted by organizations committed to meaningful change</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8 text-center">
              <div class="bg-white p-6 rounded-lg shadow-md card-hover stagger-animation">
                <div class="text-3xl font-bold text-primary-600 mb-2">40%</div>
                <div class="text-gray-600">Reduction in employee turnover</div>
              </div>
              <div class="bg-white p-6 rounded-lg shadow-md card-hover stagger-animation">
                <div class="text-3xl font-bold text-primary-600 mb-2">4X</div>
                <div class="text-gray-600">Improvement in team diversity</div>
              </div>
              <div class="bg-white p-6 rounded-lg shadow-md card-hover stagger-animation">
                <div class="text-3xl font-bold text-primary-600 mb-2">90%</div>
                <div class="text-gray-600">Client satisfaction rate</div>
              </div>
            </div>
          </div>
        </section>
      </template>

      <!-- Problem/Solution -->
      <template #section-1="{ isVisible }">
        <section class="py-20 bg-white" :class="{ 'animate': isVisible }">
          <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
              <div class="stagger-animation">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">The Challenge Most Organizations Face</h2>
                <div class="space-y-4 text-gray-600">
                  <p class="flex items-start stagger-animation">
                    <span class="text-red-500 mr-3 mt-1">✗</span>
                    High turnover rates costing $15,000+ per replacement
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-red-500 mr-3 mt-1">✗</span>
                    Struggling to find reliable, motivated employees
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-red-500 mr-3 mt-1">✗</span>
                    Missing out on a talented, loyal workforce
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-red-500 mr-3 mt-1">✗</span>
                    Unconscious bias limiting diversity efforts
                  </p>
                </div>
              </div>
              <div class="stagger-animation">
                <h3 class="text-2xl font-semibold text-gray-900 mb-6">What Changes When You Embrace Second Chances</h3>
                <div class="space-y-4 text-gray-600">
                  <p class="flex items-start stagger-animation">
                    <span class="text-green-500 mr-3 mt-1">✓</span>
                    Access to motivated employees with proven resilience
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-green-500 mr-3 mt-1">✓</span>
                    Reduced turnover through better hiring and integration
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-green-500 mr-3 mt-1">✓</span>
                    Enhanced company reputation and community impact
                  </p>
                  <p class="flex items-start stagger-animation">
                    <span class="text-green-500 mr-3 mt-1">✓</span>
                    Teams that understand the value of transformation
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </template>

      <!-- Simple Booking Component -->
      <template #section-2="{ isVisible }">
        <div ref="bookingSection" :class="{ 'animate': isVisible }">
          <SimpleBooking />
        </div>
      </template>

      <!-- About Section -->
      <template #section-3="{ isVisible }">
        <section class="py-20 bg-white" :class="{ 'animate': isVisible }">
          <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 gap-12 items-center">
              <div class="stagger-animation">
                <h2 class="text-3xl font-bold text-gray-900 mb-6">Why This Matters</h2>
                <p class="text-lg text-gray-700 mb-6 leading-relaxed">
                  I've spent years learning what actually works when it comes to giving people second chances and building inclusive teams. Not theory—real experience from someone who's been there.
                </p>
                <p class="text-lg text-gray-700 mb-6 leading-relaxed">
                  Every conversation is different. Sometimes I can help directly, sometimes I can connect you with the right resources, and sometimes just talking through the challenges helps clarify the path forward.
                </p>
                <div class="space-y-4">
                  <div class="flex items-center stagger-animation">
                    <div class="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                      <span class="text-blue-600 text-sm">✓</span>
                    </div>
                    <p class="text-gray-700">Real experience, not just theory</p>
                  </div>
                  <div class="flex items-center stagger-animation">
                    <div class="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                      <span class="text-blue-600 text-sm">✓</span>
                    </div>
                    <p class="text-gray-700">Practical insights you can actually use</p>
                  </div>
                  <div class="flex items-center stagger-animation">
                    <div class="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                      <span class="text-blue-600 text-sm">✓</span>
                    </div>
                    <p class="text-gray-700">No agenda except being helpful</p>
                  </div>
                </div>
              </div>
              <div class="text-center stagger-animation">
                <div class="w-64 h-64 bg-gray-200 rounded-full mx-auto mb-6 flex items-center justify-center float-animation">
                  <span class="text-4xl font-bold text-gray-500">Greg</span>
                </div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">Greg Barber</h3>
                <p class="text-gray-600">Always Free Minds</p>
              </div>
            </div>
          </div>
        </section>
      </template>
    </AnimatedSections>

    <!-- Sticky Footer -->
    <footer class="sticky-footer text-white py-8">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h3 class="text-xl font-bold mb-2">Always Free Minds</h3>
          <p class="text-gray-300 mb-4">Transforming organizations through second chances</p>
          <div class="flex justify-center space-x-6">
            <a href="mailto:gregory@alwaysfreeminds.com" class="text-gray-300 hover:text-yellow-400 transition-colors">
              Email
            </a>
            <a href="#" class="text-gray-300 hover:text-yellow-400 transition-colors">
              LinkedIn
            </a>
            <a href="#" class="text-gray-300 hover:text-yellow-400 transition-colors">
              Twitter
            </a>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import SimpleBooking from '@/components/booking/SimpleBooking.vue'
import GlobalEffects from '@/components/effects/GlobalEffects.vue'
import AnimatedSections from '@/components/effects/AnimatedSections.vue'

export default {
  name: 'ConsultingPage',
  components: {
    SimpleBooking,
    GlobalEffects,
    AnimatedSections
  },
  mounted() {
    // Trigger stagger animations on load
    this.$nextTick(() => {
      const elements = document.querySelectorAll('.stagger-animation');
      elements.forEach((el, index) =>
      setTimeout(() => el.classList.add('animate'), index * 100)
     );
   });
 },
 methods: {
   scrollToBooking() {
     this.$refs.bookingSection.scrollIntoView({ 
       behavior: 'smooth',
       block: 'start'
     });
   }
 }
}
</script>

<style scoped>
.consulting-page {
 position: relative;
 overflow-x: hidden;
}

.stagger-animation.animate {
 opacity: 1;
 transform: translateY(0);
}
</style>
