<template>
  <div class="simple-booking">
    <!-- Clean, helpful hero section -->
    <section class="bg-gradient-to-br from-primary-600 via-primary-700 to-primary-800 text-white py-20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Let's Have a Conversation</h2>
        <p class="text-xl text-gray-200 mb-8 max-w-2xl mx-auto leading-relaxed">
          I'm here to listen and share what I've learned. Whether you're facing team challenges, exploring second-chance hiring, or just want to connect - let's talk.
        </p>
        
        <div class="bg-white/10 backdrop-blur-sm rounded-lg p-8 mb-8 max-w-md mx-auto">
          <div class="text-2xl font-bold mb-2">Discovery Call</div>
          <div class="text-gray-200 text-sm mb-6">
            • 15 minutes<br>
            • Completely free<br>
            • No sales pitch<br>
            • Just a helpful conversation
          </div>
          <button 
            @click="openDiscoveryCall" 
            class="w-full bg-yellow-400 text-gray-900 py-4 px-6 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            Book a Quick Chat
          </button>
        </div>

        <p class="text-sm text-gray-300 opacity-75">
          After we talk, I can share resources or suggest next steps that might help
        </p>
      </div>
    </section>

    <!-- What to expect -->
    <section class="py-16 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h3 class="text-2xl font-bold text-gray-900 mb-4">What to Expect</h3>
          <p class="text-lg text-gray-600">A genuine conversation, no agenda</p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-3.582 8-8 8a8.001 8.001 0 01-7.93-6.7c-.02-.12-.016-.25.04-.37.124-.27.395-.43.684-.43h.08c.312 0 .59.187.712.475A6 6 0 1012 6V4a2 2 0 012-2h2a2 2 0 012 2v2a6 6 0 110 12z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Just Listen</h4>
            <p class="text-gray-600">Tell me what's on your mind. I'm here to understand your situation.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Share Insights</h4>
            <p class="text-gray-600">I'll share relevant experiences and perspectives that might help.</p>
          </div>
          
          <div class="text-center">
            <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h4 class="text-lg font-semibold text-gray-900 mb-2">Offer Resources</h4>
            <p class="text-gray-600">If it makes sense, I'll suggest helpful next steps or resources.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Inline calendar -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Pick a Time That Works</h3>
          <p class="text-lg text-gray-600">15 minutes, your schedule</p>
        </div>
        
        <div class="bg-white rounded-2xl shadow-xl p-6">
          <div 
            data-savvycal-embed="greg-AlwaysFreeMinds/discovery-call"
            data-embed-type="inline"
            data-theme="modern"
            style="min-width:320px;height:600px;">
          </div>
        </div>
      </div>
    </section>

    <!-- Reassurance -->
    <section class="py-12 bg-white">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="bg-gray-50 rounded-lg p-8">
          <h4 class="text-lg font-semibold text-gray-900 mb-4">No Pressure, Just Connection</h4>
          <p class="text-gray-600 leading-relaxed">
            This is simply a conversation between two people. No sales pitch, no agenda. 
            Just someone who's walked a difficult path and is happy to share what they've learned. 
            After we talk, you'll know if there are ways I can help, and I'll know how I can best support your goals.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SimpleBooking',
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
          if (window.SavvyCal) {
            window.SavvyCal.init();
          }
        };
        document.head.appendChild(script);
      }
    },
    
    openDiscoveryCall() {
      const link = 'greg-AlwaysFreeMinds/discovery-call';
      
      if (window.SavvyCal) {
        try {
          window.SavvyCal.popup(link);
        } catch (error) {
          window.open(`https://savvycal.com/${link}`, '_blank', 'width=800,height=700');
        }
      } else {
        window.open(`https://savvycal.com/${link}`, '_blank', 'width=800,height=700');
      }
      
      console.log('Discovery call booking clicked');
    }
  }
}
</script>

<style scoped>
.simple-booking {
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

@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>
