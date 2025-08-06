<template>
  <div class="savvycal-booking-integration">
    <!-- Primary Booking Section -->
    <section class="booking-hero bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800 text-white relative overflow-hidden">
      <div class="absolute inset-0 bg-black opacity-10"></div>
      <div class="container mx-auto px-6 py-16 relative z-10">
        <div class="max-w-4xl mx-auto text-center">
          <h2 class="text-4xl md:text-5xl font-bold mb-6 leading-tight">
            Ready to Transform Your Business?
          </h2>
          <p class="text-xl md:text-2xl mb-8 opacity-90">
            Book your strategy session and start seeing results within 30 days
          </p>
          <div class="inline-flex items-center bg-white/20 backdrop-blur-sm rounded-full px-6 py-3 mb-8">
            <svg class="w-5 h-5 text-yellow-300 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
            </svg>
            <span class="text-sm font-semibold">{{ availableSlots }} Strategy Sessions Available This Month</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Booking Options Grid -->
    <section class="booking-options py-16 bg-gray-50">
      <div class="container mx-auto px-6">
        <div class="max-w-6xl mx-auto">
          <div class="grid md:grid-cols-3 gap-8">
            
            <!-- Chat with Greg -->
            <div class="booking-card group">
              <div class="bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform group-hover:-translate-y-2 border border-gray-100">
                <div class="p-8 text-center">
                  <div class="w-20 h-20 bg-gradient-to-br from-green-400 to-green-600 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-3.582 8-8 8a8.001 8.001 0 01-7.93-6.7c-.02-.12-.016-.25.04-.37.124-.27.395-.43.684-.43h.08c.312 0 .59.187.712.475A6 6 0 1012 6V4a2 2 0 012-2h2a2 2 0 012 2v2a6 6 0 110 12z"/>
                    </svg>
                  </div>
                  <h3 class="text-2xl font-bold mb-3 text-gray-900">Chat with Greg</h3>
                  <div class="mb-4">
                    <span class="text-3xl font-bold text-green-600">FREE</span>
                    <p class="text-gray-500 text-sm">30 minutes</p>
                  </div>
                  <p class="text-gray-600 mb-8 leading-relaxed">
                    Quick conversation to understand your team challenges and see if we're a good fit.
                  </p>
                  <button 
                    @click="openSavvyCal('discovery')" 
                    class="w-full bg-gradient-to-r from-green-500 to-green-600 text-white py-4 px-6 rounded-xl font-semibold hover:from-green-600 hover:to-green-700 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                    Book Free Chat
                  </button>
                </div>
              </div>
            </div>

            <!-- Strategy Session -->
            <div class="booking-card group relative">
              <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 z-10">
                <span class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-2 rounded-full text-sm font-bold shadow-lg">
                  MOST POPULAR
                </span>
              </div>
              <div class="bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 transform group-hover:-translate-y-2 border-2 border-blue-200">
                <div class="p-8 text-center">
                  <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-blue-700 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
                    </svg>
                  </div>
                  <h3 class="text-2xl font-bold mb-3 text-gray-900">Strategy Session</h3>
                  <div class="mb-4">
                    <span class="text-3xl font-bold text-blue-600">$150</span>
                    <p class="text-gray-500 text-sm">60 minutes</p>
                  </div>
                  <p class="text-gray-600 mb-8 leading-relaxed">
                    Deep dive analysis of your challenges with a custom 30-day action plan to get results fast.
                  </p>
                  <button 
                    @click="openSavvyCal('strategy')" 
                    class="w-full bg-gradient-to-r from-blue-500 to-blue-700 text-white py-4 px-6 rounded-xl font-semibold hover:from-blue-600 hover:to-blue-800 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                    Book Strategy Session
                  </button>
                </div>
              </div>
            </div>

            <!-- Team Workshop -->
            <div class="booking-card group">
              <div class="bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform group-hover:-translate-y-2 border border-gray-100">
                <div class="p-8 text-center">
                  <div class="w-20 h-20 bg-gradient-to-br from-purple-500 to-purple-700 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                    <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                    </svg>
                  </div>
                  <h3 class="text-2xl font-bold mb-3 text-gray-900">Team Workshop</h3>
                  <div class="mb-4">
                    <span class="text-3xl font-bold text-purple-600">FREE</span>
                    <p class="text-gray-500 text-sm">30 minutes</p>
                  </div>
                  <p class="text-gray-600 mb-8 leading-relaxed">
                    Planning session to design a custom workshop that transforms your entire team.
                  </p>
                  <button 
                    @click="openSavvyCal('workshop')" 
                    class="w-full bg-gradient-to-r from-purple-500 to-purple-700 text-white py-4 px-6 rounded-xl font-semibold hover:from-purple-600 hover:to-purple-800 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                    Plan Workshop
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Social Proof & Stats -->
    <section class="social-proof py-16 bg-white">
      <div class="container mx-auto px-6">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-12">
            <h3 class="text-3xl font-bold text-gray-900 mb-4">
              Join 200+ Leaders Who've Transformed Their Teams
            </h3>
            <p class="text-xl text-gray-600">
              Proven strategies that deliver measurable results in 30 days
            </p>
          </div>
          
          <!-- Stats Grid -->
          <div class="grid md:grid-cols-4 gap-8 mb-16">
            <div class="stat-item text-center">
              <div class="text-4xl font-bold text-blue-600 mb-2">40%</div>
              <p class="text-gray-600">Average Turnover Reduction</p>
            </div>
            <div class="stat-item text-center">
              <div class="text-4xl font-bold text-green-600 mb-2">30</div>
              <p class="text-gray-600">Days to See Results</p>
            </div>
            <div class="stat-item text-center">
              <div class="text-4xl font-bold text-purple-600 mb-2">200+</div>
              <p class="text-gray-600">Companies Transformed</p>
            </div>
            <div class="stat-item text-center">
              <div class="text-4xl font-bold text-orange-600 mb-2">$180K</div>
              <p class="text-gray-600">Average Cost Savings</p>
            </div>
          </div>

          <!-- Testimonial -->
          <div class="bg-gray-50 rounded-2xl p-8 border-l-4 border-blue-500">
            <div class="flex flex-col md:flex-row items-center">
              <div class="md:flex-1 mb-6 md:mb-0">
                <blockquote class="text-xl italic text-gray-700 mb-4">
                  "We went from 35% annual turnover to 12% in just 6 months. The ROI was incredible - we saved $180K in recruitment costs alone. Greg's approach actually works."
                </blockquote>
                <div class="flex items-center">
                  <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center mr-4">
                    <span class="text-white font-bold text-lg">SC</span>
                  </div>
                  <div>
                    <p class="font-bold text-gray-900">Sarah Chen</p>
                    <p class="text-gray-600">VP Operations, TechFlow Solutions</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Inline Calendar Embed -->
    <section class="inline-booking py-16 bg-gray-50">
      <div class="container mx-auto px-6">
        <div class="max-w-4xl mx-auto">
          <div class="text-center mb-8">
            <h3 class="text-3xl font-bold text-gray-900 mb-4">
              Book Your Strategy Session Now
            </h3>
            <p class="text-lg text-gray-600">
              Select a time that works for you - payment collected securely after booking
            </p>
          </div>
          
          <div class="bg-white rounded-2xl shadow-xl p-6">
            <div 
              :data-savvycal-embed="mainBookingLink"
              data-embed-type="inline"
              data-theme="modern"
              class="savvycal-embed"
              style="min-width:320px;height:600px;">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Final CTA -->
    <section class="final-cta py-16 bg-gradient-to-r from-gray-900 to-gray-800 text-white">
      <div class="container mx-auto px-6 text-center">
        <h3 class="text-3xl font-bold mb-4">
          Still Have Questions?
        </h3>
        <p class="text-xl mb-8 opacity-90">
          Start with a free chat - no pressure, just solutions
        </p>
        <button 
          @click="openSavvyCal('discovery')" 
          class="bg-white text-gray-900 py-4 px-8 rounded-xl font-bold text-lg hover:bg-gray-100 transition-colors shadow-lg">
          Chat with Greg - FREE
        </button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SavvyCalBooking',
  data() {
    return {
      // Your actual SavvyCal links
      savvyCalLinks: {
        main: 'greg-AlwaysFreeMinds/strategy',
        discovery: 'greg-AlwaysFreeMinds/chat-with-greg',
        strategy: 'greg-AlwaysFreeMinds/strategy', 
        workshop: 'greg-AlwaysFreeMinds/workshop'
      },
      availableSlots: 8,
      isLoaded: false
    }
  },
  computed: {
    mainBookingLink() {
      return this.savvyCalLinks.main;
    }
  },
  mounted() {
    this.loadSavvyCalScript();
  },
  methods: {
    loadSavvyCalScript() {
      // Load SavvyCal embed script
      if (!document.querySelector('script[src*="savvycal"]')) {
        const script = document.createElement('script');
        script.src = 'https://embed.savvycal.com/v1/embed.js';
        script.async = true;
        script.onload = () => {
          this.isLoaded = true;
          this.initializeSavvyCal();
        };
        document.head.appendChild(script);
      } else {
        this.isLoaded = true;
        this.initializeSavvyCal();
      }
    },
    
    initializeSavvyCal() {
      // Initialize SavvyCal after script loads
      if (window.SavvyCal) {
        window.SavvyCal.init();
      }
    },
    
    openSavvyCal(type) {
      const link = this.savvyCalLinks[type];
      
      if (this.isLoaded && window.SavvyCal) {
        // Use SavvyCal popup method
        window.SavvyCal.popup(link);
      } else {
        // Fallback to direct link
        window.open(`https://savvycal.com/${link}`, '_blank', 'width=800,height=700');
      }
      
      // Track conversion
      this.trackBookingClick(type);
      
      // Visual feedback
      if (type === 'strategy' && this.availableSlots > 0) {
        this.availableSlots--;
      }
    },
    
    trackBookingClick(type) {
      // Google Analytics 4 tracking
      if (typeof gtag !== 'undefined') {
        gtag('event', 'booking_click', {
          event_category: 'savvycal',
          event_label: type,
          value: this.getBookingValue(type)
        });
      }
      
      // Facebook Pixel tracking
      if (typeof fbq !== 'undefined') {
        fbq('track', 'Schedule', {
          content_name: `${type}_booking`,
          value: this.getBookingValue(type),
          currency: 'USD'
        });
      }
      
      // Console log for debugging
      console.log(`SavvyCal booking clicked: ${type}`, {
        link: `https://savvycal.com/${this.savvyCalLinks[type]}`,
        value: this.getBookingValue(type)
      });
    },
    
    getBookingValue(type) {
      const values = {
        discovery: 0,
        strategy: 150,
        workshop: 0
      };
      return values[type] || 0;
    }
  }
}
</script>

<style scoped>
.savvycal-booking-integration {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.booking-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.booking-hero {
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
}

.stat-item {
  transition: transform 0.3s ease;
}

.stat-item:hover {
  transform: translateY(-4px);
}

.savvycal-embed {
  border-radius: 12px;
  overflow: hidden;
}

/* SavvyCal specific styling */
[data-savvycal-embed] {
  border-radius: 12px;
  overflow: hidden;
}

/* Loading state for SavvyCal embed */
[data-savvycal-embed]:empty::before {
  content: "Loading calendar...";
  display: flex;
  align-items: center;
  justify-content: center;
  height: 600px;
  color: #6B7280;
  font-size: 1.125rem;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .booking-options .grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .social-proof .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
  
  .savvycal-embed {
    height: 500px;
  }
  
  .booking-hero h2 {
    font-size: 2.25rem;
  }
  
  .booking-hero p {
    font-size: 1.125rem;
  }
}

@media (max-width: 480px) {
  .social-proof .grid {
    grid-template-columns: 1fr;
  }
  
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}

/* Animation for smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Focus states for accessibility */
button:focus {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}
</style>