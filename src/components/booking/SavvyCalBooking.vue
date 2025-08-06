<template>
  <div class="savvycal-booking">
    <!-- Quick Booking Cards -->
    <div class="grid md:grid-cols-3 gap-8 mb-16">
      <!-- Chat with Greg -->
      <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
        <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-3.582 8-8 8a8.001 8.001 0 01-7.93-6.7c-.02-.12-.016-.25.04-.37.124-.27.395-.43.684-.43h.08c.312 0 .59.187.712.475A6 6 0 1012 6V4a2 2 0 012-2h2a2 2 0 012 2v2a6 6 0 110 12z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3 text-center">Chat with Greg</h3>
        <div class="text-center mb-4">
          <span class="text-2xl font-bold text-green-600">FREE</span>
          <p class="text-gray-500 text-sm">30 minutes</p>
        </div>
        <p class="text-gray-600 mb-6 text-center">Quick conversation to understand your challenges and see if we're a good fit.</p>
        <button @click="openSavvyCal('discovery')" class="w-full bg-green-500 text-white py-3 px-6 rounded-lg font-semibold hover:bg-green-600 transition-colors">
          Book Free Chat
        </button>
      </div>

      <!-- Strategy Session -->
      <div class="bg-white p-8 rounded-xl shadow-xl border-2 border-primary-200 hover:shadow-2xl transition-all duration-300 relative">
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
        <p class="text-gray-600 mb-6 text-center">Deep dive analysis with a custom 30-day action plan to get results fast.</p>
        <button @click="openSavvyCal('strategy')" class="w-full bg-primary-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-primary-700 transition-colors">
          Book Strategy Session
        </button>
      </div>

      <!-- Workshop Planning -->
      <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300">
        <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
          </svg>
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-3 text-center">Workshop Planning</h3>
        <div class="text-center mb-4">
          <span class="text-2xl font-bold text-purple-600">FREE</span>
          <p class="text-gray-500 text-sm">30 minutes</p>
        </div>
        <p class="text-gray-600 mb-6 text-center">Planning session to design a custom workshop for your team.</p>
        <button @click="openSavvyCal('workshop')" class="w-full bg-purple-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-purple-700 transition-colors">
          Plan Workshop
        </button>
      </div>
    </div>

    <!-- Inline Calendar -->
    <div class="max-w-4xl mx-auto">
      <div class="text-center mb-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-4">Select Your Preferred Time</h3>
        <p class="text-lg text-gray-600">Choose a time that works for you</p>
      </div>
      <div class="bg-white rounded-2xl shadow-xl p-6">
        <div :data-savvycal-embed="mainBookingLink" data-embed-type="inline" data-theme="modern" style="min-width:320px;height:600px;"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SavvyCalBooking',
  data() {
    return {
      savvyCalLinks: {
        main: 'greg-AlwaysFreeMinds/strategy',
        discovery: 'greg-AlwaysFreeMinds/chat-with-greg',
        strategy: 'greg-AlwaysFreeMinds/strategy', 
        workshop: 'greg-AlwaysFreeMinds/workshop'
      },
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
      if (!document.querySelector('script[src*="savvycal"]')) {
        const script = document.createElement('script');
        script.src = 'https://embed.savvycal.com/v1/embed.js';
        script.async = true;
        script.onload = () => {
          this.isLoaded = true;
          if (window.SavvyCal) window.SavvyCal.init();
        };
        document.head.appendChild(script);
      } else {
        this.isLoaded = true;
        if (window.SavvyCal) window.SavvyCal.init();
      }
    },
    openSavvyCal(type) {
      const link = this.savvyCalLinks[type];
      if (this.isLoaded && window.SavvyCal) {
        window.SavvyCal.popup(link);
      } else {
        window.open(`https://savvycal.com/${link}`, '_blank', 'width=800,height=700');
      }
      console.log(`SavvyCal booking clicked: ${type}`);
    }
  }
}
</script>
