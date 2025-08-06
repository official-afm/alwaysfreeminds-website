<template>
  <div class="enhanced-savvycal-booking">
    <!-- Corporate Booking Section -->
    <div v-if="viewType === 'corporate'" class="corporate-bookings">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">Corporate Services</h2>
        <p class="text-lg text-gray-600">Transform your organization with proven strategies</p>
      </div>
      
      <div class="grid md:grid-cols-3 gap-8 mb-16">
        <!-- Corporate Discovery Call -->
        <div class="booking-card bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0V6a2 2 0 112 2H6a2 2 0 112-2V6"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-3 text-center">Corporate Discovery</h3>
          <div class="text-center mb-4">
            <span class="text-2xl font-bold text-blue-600">FREE</span>
            <p class="text-gray-500 text-sm">30 minutes</p>
          </div>
          <p class="text-gray-600 mb-6 text-center">Initial consultation to understand your corporate challenges and explore solutions.</p>
          <button @click="openSavvyCal('discovery-call')" class="w-full bg-blue-500 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-600 transition-colors">
            Book Discovery Call
          </button>
        </div>

        <!-- Corporate Strategy -->
        <div class="booking-card bg-white p-8 rounded-xl shadow-xl border-2 border-primary-200 hover:shadow-2xl transition-all duration-300 relative">
          <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-medium">Most Popular</div>
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-3 text-center">Strategy Session</h3>
          <div class="text-center mb-4">
            <span class="text-2xl font-bold text-primary-600">$150</span>
            <p class="text-gray-500 text-sm">60 minutes</p>
          </div>
          <p class="text-gray-600 mb-6 text-center">Deep dive analysis with custom action plan for your organization.</p>
          <button @click="openSavvyCal('strategy')" class="w-full bg-primary-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-primary-700 transition-colors">
            Book Strategy Session
          </button>
        </div>

        <!-- Corporate Workshop -->
        <div class="booking-card bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 715.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 919.288 0M15 7a3 3 0 11-6 0 3 3 0 616 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-3 text-center">Workshop Planning</h3>
          <div class="text-center mb-4">
            <span class="text-2xl font-bold text-purple-600">FREE</span>
            <p class="text-gray-500 text-sm">30 min planning</p>
            <p class="text-sm text-gray-600 mt-1">Workshop: $1,500-2,500</p>
          </div>
          <p class="text-gray-600 mb-6 text-center">Plan custom workshops for your team starting at $1,500.</p>
          <button @click="openSavvyCal('workshop')" class="w-full bg-purple-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-purple-700 transition-colors">
            Plan Workshop
          </button>
        </div>
      </div>
    </div>

    <!-- All Booking Types View -->
    <div v-if="viewType === 'all'" class="all-bookings">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">All Booking Options</h2>
        <p class="text-lg text-gray-600">Choose the service that best fits your needs</p>
      </div>
      
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Corporate Discovery -->
        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Corporate Discovery</h4>
          <p class="text-sm text-gray-600 mb-4">30 min • FREE</p>
          <button @click="openSavvyCal('discovery-call')" class="w-full bg-blue-500 text-white py-2 px-4 rounded-lg font-semibold hover:bg-blue-600 transition-colors text-sm">
            Book Discovery
          </button>
        </div>

        <!-- Strategy Session -->
        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border-2 border-primary-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Strategy Session</h4>
          <p class="text-sm text-gray-600 mb-4">60 min • $150</p>
          <button @click="openSavvyCal('strategy')" class="w-full bg-primary-600 text-white py-2 px-4 rounded-lg font-semibold hover:bg-primary-700 transition-colors text-sm">
            Book Strategy
          </button>
        </div>

        <!-- Workshop Planning -->
        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Workshop Planning</h4>
          <p class="text-sm text-gray-600 mb-4">30 min • FREE</p>
          <button @click="openSavvyCal('workshop')" class="w-full bg-purple-600 text-white py-2 px-4 rounded-lg font-semibold hover:bg-purple-700 transition-colors text-sm">
            Plan Workshop
          </button>
        </div>

        <!-- All other booking options -->
        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Non-Profit Chat</h4>
          <p class="text-sm text-gray-600 mb-4">30 min • FREE</p>
          <button @click="openSavvyCal('chat-with-greg')" class="w-full bg-green-500 text-white py-2 px-4 rounded-lg font-semibold hover:bg-green-600 transition-colors text-sm">
            Book Chat
          </button>
        </div>

        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Podcast Interview</h4>
          <p class="text-sm text-gray-600 mb-4">Flexible • FREE</p>
          <button @click="openSavvyCal('podcast')" class="w-full bg-red-500 text-white py-2 px-4 rounded-lg font-semibold hover:bg-red-600 transition-colors text-sm">
            Book Interview
          </button>
        </div>

        <div class="booking-card bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
          <h4 class="text-lg font-bold text-gray-900 mb-2">Book Development</h4>
          <p class="text-sm text-gray-600 mb-4">30 min • FREE</p>
          <button @click="openSavvyCal('your-book-developement')" class="w-full bg-yellow-500 text-white py-2 px-4 rounded-lg font-semibold hover:bg-yellow-600 transition-colors text-sm">
            Discuss Book
          </button>
        </div>
      </div>
    </div>

    <!-- Inline Calendar Embed -->
    <div v-if="showInlineCalendar" class="max-w-4xl mx-auto mt-16">
      <div class="text-center mb-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-4">Select Your Preferred Time</h3>
        <p class="text-lg text-gray-600">Choose a time that works for you</p>
      </div>
      
      <div class="bg-white rounded-2xl shadow-xl p-6">
        <div 
          :data-savvycal-embed="currentBookingLink"
          data-embed-type="inline"
          data-theme="modern"
          style="min-width:320px;height:600px;">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EnhancedSavvyCalBooking',
  props: {
    viewType: {
      type: String,
      default: 'corporate',
      validator: value => ['corporate', 'nonprofit', 'media', 'interview', 'all'].includes(value)
    },
    showInlineCalendar: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      // Complete SavvyCal link mapping
      savvyCalLinks: {
        'discovery-call': 'greg-AlwaysFreeMinds/discovery-call',
        'interview': 'greg-AlwaysFreeMinds/interview',
        'join-our-team': 'greg-AlwaysFreeMinds/join-our-team',
        'chat-with-greg': 'greg-AlwaysFreeMinds/chat-with-greg',
        'podcast': 'greg-AlwaysFreeMinds/podcast',
        'prison-non-profit': 'greg-AlwaysFreeMinds/prison-non-profit',
        'religous-non-profit': 'greg-AlwaysFreeMinds/religous-non-profit',
        'strategy': 'greg-AlwaysFreeMinds/strategy',
        'workshop': 'greg-AlwaysFreeMinds/workshop',
        'your-book-developement': 'greg-AlwaysFreeMinds/your-book-developement'
      },
      
      // SavvyCal API Configuration (CLIENT-SAFE ONLY)
      apiConfig: {
        publicKey: 'pt_01K1YSYX41PRJGQ25M6GNG8ZN1', // ✅ Safe to expose
        baseUrl: 'https://api.savvycal.com/v1'
        // SECRET KEY REMOVED FOR SECURITY
      },
      
      currentBookingLink: '',
      isLoaded: false
    }
  },
  computed: {
    defaultBookingLink() {
      switch(this.viewType) {
        case 'corporate': return this.savvyCalLinks.strategy;
        case 'nonprofit': return this.savvyCalLinks['chat-with-greg'];
        case 'media': return this.savvyCalLinks.podcast;
        case 'interview': return this.savvyCalLinks.interview;
        default: return this.savvyCalLinks.strategy;
      }
    }
  },
  mounted() {
    this.currentBookingLink = this.defaultBookingLink;
    this.loadSavvyCalScript();
    this.trackPageView();
  },
  methods: {
    loadSavvyCalScript() {
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
      if (window.SavvyCal) {
        window.SavvyCal.init();
      }
    },
    
    async openSavvyCal(bookingType) {
      const link = this.savvyCalLinks[bookingType];
      
      // Track booking attempt
      this.trackBookingClick(bookingType);
      
      // Update current booking link for inline calendar
      this.currentBookingLink = link;
      
      // Open SavvyCal popup or fallback to new window
      if (this.isLoaded && window.SavvyCal) {
        try {
          window.SavvyCal.popup(link);
        } catch (error) {
          console.error('SavvyCal popup failed:', error);
          this.fallbackBooking(link);
        }
      } else {
        this.fallbackBooking(link);
      }
      
      // Track booking metrics (client-safe)
      this.updateBookingMetrics(bookingType);
    },
    
    fallbackBooking(link) {
      window.open(`https://savvycal.com/${link}`, '_blank', 'width=800,height=700,scrollbars=yes,resizable=yes');
    },
    
    async updateBookingMetrics(bookingType) {
      try {
        // Client-safe booking tracking (no secret key needed)
        console.log(`Booking attempt tracked: ${bookingType}`);
        console.log(`Public API available:`, {
          publicKey: this.apiConfig.publicKey,
          timestamp: new Date().toISOString()
        });
        
        // For advanced API features requiring secret key,
        // you would need a backend proxy endpoint
        
      } catch (error) {
        console.error('Failed to track booking metrics:', error);
      }
    },
    
    /* eslint-disable no-undef */
    trackPageView() {
      // Google Analytics 4 tracking
      if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "page_view", {
          page_title: `SavvyCal Booking - ${this.viewType}`,
          page_location: window.location.href,
          booking_type: this.viewType
        });
      }
      
      // Facebook Pixel tracking
      if (typeof window !== "undefined" && window.fbq) {
        window.fbq("track", "ViewContent", {
          content_name: `${this.viewType}_booking_page`,
          content_category: "booking"
        });
      }
      
      console.log(`Page view tracked: ${this.viewType} booking page`);
    },
    
    /* eslint-disable no-undef */
    trackBookingClick(bookingType) {
      // Google Analytics 4 tracking
      if (typeof window !== "undefined" && window.gtag) {
        window.gtag("event", "booking_click", {
          event_category: "savvycal",
          event_label: bookingType,
          booking_view_type: this.viewType,
          value: this.getBookingValue(bookingType)
        });
      }
      
      // Facebook Pixel tracking
      if (typeof window !== "undefined" && window.fbq) {
        window.fbq("track", "Schedule", {
          content_name: `${bookingType}_booking`,
          value: this.getBookingValue(bookingType),
          currency: "USD"
        });
      }
      
      console.log(`Booking clicked: ${bookingType} from ${this.viewType} view`);
    },
    
    getBookingValue(bookingType) {
      const values = {
        'strategy': 150,
        'workshop': 1500,
        'discovery-call': 0,
        'interview': 0,
        'join-our-team': 0,
        'chat-with-greg': 0,
        'podcast': 0,
        'prison-non-profit': 0,
        'religous-non-profit': 0,
        'your-book-developement': 0
      };
      return values[bookingType] || 0;
    }
  }
}
</script>

<style scoped>
.booking-card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.booking-card:hover {
  transform: translateY(-4px);
}

.enhanced-savvycal-booking {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

[data-savvycal-embed]:empty::before {
  content: "Loading calendar...";
  display: flex;
  align-items: center;
  justify-content: center;
  height: 600px;
  color: #6B7280;
  font-size: 1.125rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.corporate-bookings .booking-card {
  border-left: 4px solid #3B82F6;
}

.all-bookings .booking-card {
  border-left: 4px solid #6B7280;
}

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

button:focus {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}
</style>
