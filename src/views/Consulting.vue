<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white py-20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">Transform Your Organization with Proven Second-Chance Strategies</h1>
        <p class="text-xl md:text-2xl mb-8 text-gray-200 max-w-3xl mx-auto leading-relaxed">
          Reduce turnover by 40%, build diverse teams, and unlock untapped talent with insights from someone who's lived the transformation.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <button 
            @click="scrollToBooking" 
            class="inline-flex items-center justify-center bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            Book Strategy Call - $150
          </button>
          <button 
            @click="scrollToWorkshops" 
            class="inline-flex items-center justify-center border-2 border-white text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-white hover:text-primary-900 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            Corporate Training
          </button>
        </div>
        
        <!-- Available slots indicator -->
        <div class="mt-6 inline-flex items-center bg-white/20 backdrop-blur-sm rounded-full px-6 py-3">
          <svg class="w-5 h-5 text-yellow-300 mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          <span class="text-sm font-semibold">{{ availableSlots }} Strategy Sessions Available This Month</span>
        </div>
      </div>
    </section>

    <!-- Social Proof -->
    <section class="py-12 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
          <p class="text-gray-600 text-lg">Trusted by organizations committed to meaningful change</p>
        </div>
        <div class="grid md:grid-cols-3 gap-8 text-center">
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="text-3xl font-bold text-primary-600 mb-2">40%</div>
            <div class="text-gray-600">Reduction in employee turnover</div>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="text-3xl font-bold text-primary-600 mb-2">4X</div>
            <div class="text-gray-600">Improvement in team diversity</div>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-md">
            <div class="text-3xl font-bold text-primary-600 mb-2">90%</div>
            <div class="text-gray-600">Client satisfaction rate</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services -->
    <section id="services" class="py-20 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">How I Help Organizations Succeed</h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Real strategies from real experience. I don't just teach theory—I share what actually works.
          </p>
        </div>

        <div class="grid lg:grid-cols-3 gap-8">
          <!-- Individual Consulting -->
          <div class="bg-gradient-to-br from-gray-50 to-gray-100 p-8 rounded-xl">
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-4">Strategy Consulting</h3>
            <div class="text-3xl font-bold text-primary-600 mb-4">$150/hour</div>
            <p class="text-gray-600 mb-6">
              One-on-one guidance for implementing second-chance hiring, building inclusive teams, and creating transformation-focused programs.
            </p>
            <ul class="text-sm text-gray-600 space-y-2 mb-8">
              <li>• Second-chance hiring strategy</li>
              <li>• Bias reduction techniques</li>
              <li>• Team integration planning</li>
              <li>• Policy development guidance</li>
              <li>• ROI measurement frameworks</li>
            </ul>
            <button 
              @click="openSavvyCal('strategy')" 
              class="block w-full bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors duration-200 text-center"
            >
              Book Session
            </button>
          </div>

          <!-- Corporate Training -->
          <div class="bg-gradient-to-br from-primary-50 to-primary-100 p-8 rounded-xl border-2 border-primary-200 relative">
            <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-medium">
              Most Popular
            </div>
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-4">Corporate Training</h3>
            <div class="text-3xl font-bold text-primary-600 mb-4">$2,500/day</div>
            <p class="text-gray-600 mb-6">
              Interactive workshops that transform how your team thinks about hiring, retention, and building inclusive cultures.
            </p>
            <ul class="text-sm text-gray-600 space-y-2 mb-8">
              <li>• Half or full-day workshops</li>
              <li>• Custom curriculum for your industry</li>
              <li>• Interactive exercises and role-playing</li>
              <li>• Follow-up implementation guide</li>
              <li>• 30-day email support included</li>
            </ul>
            <button 
              @click="openSavvyCal('workshop')" 
              class="block w-full bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors duration-200 text-center"
            >
              Request Proposal
            </button>
          </div>

          <!-- Speaking Engagements -->
          <div class="bg-gradient-to-br from-gray-50 to-gray-100 p-8 rounded-xl">
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-4">Speaking</h3>
            <div class="text-3xl font-bold text-primary-600 mb-4">$3,500+</div>
            <p class="text-gray-600 mb-6">
              Powerful keynotes and panels that inspire, educate, and drive action around second chances and transformation.
            </p>
            <ul class="text-sm text-gray-600 space-y-2 mb-8">
              <li>• Conference keynotes</li>
              <li>• University presentations</li>
              <li>• Panel discussions</li>
              <li>• Nonprofit galas and events</li>
              <li>• Virtual and in-person options</li>
            </ul>
            <button 
              @click="scrollToContact" 
              class="block w-full bg-primary-600 text-white py-3 rounded-lg font-semibold hover:bg-primary-700 transition-colors duration-200 text-center"
            >
              Book Speaking
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Problem/Solution -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">The Challenge Most Organizations Face</h2>
            <div class="space-y-4 text-gray-600">
              <p class="flex items-start">
                <span class="text-red-500 mr-3 mt-1">✗</span>
                High turnover rates costing $15,000+ per replacement
              </p>
              <p class="flex items-start">
                <span class="text-red-500 mr-3 mt-1">✗</span>
                Struggling to find reliable, motivated employees
              </p>
              <p class="flex items-start">
                <span class="text-red-500 mr-3 mt-1">✗</span>
                Missing out on a talented, loyal workforce
              </p>
              <p class="flex items-start">
                <span class="text-red-500 mr-3 mt-1">✗</span>
                Unconscious bias limiting diversity efforts
              </p>
            </div>
          </div>
          <div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">What Changes When You Work With Me</h3>
            <div class="space-y-4 text-gray-600">
              <p class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                Access to motivated employees with proven resilience
              </p>
              <p class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                Reduced turnover through better hiring and integration
              </p>
              <p class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                Enhanced company reputation and community impact
              </p>
              <p class="flex items-start">
                <span class="text-green-500 mr-3 mt-1">✓</span>
                Teams that understand the value of second chances
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Enhanced Booking Section with SavvyCal Integration -->
    <section id="book-consultation" ref="bookingSection" class="py-20 bg-white">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Main Booking Hero -->
        <div class="bg-gradient-to-br from-primary-600 to-primary-800 rounded-2xl p-8 md:p-12 text-white text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Transform Your Hiring Strategy?</h2>
          <p class="text-xl text-gray-200 mb-8 max-w-2xl mx-auto">
            Book a 60-minute strategy session where we'll identify opportunities, address challenges, and create an action plan tailored to your organization.
          </p>
          
          <div class="bg-white/10 backdrop-blur-sm rounded-lg p-6 mb-8 max-w-md mx-auto">
            <div class="text-2xl font-bold mb-2">Strategy Session - $150</div>
            <div class="text-gray-200 text-sm">
              • 60-minute focused consultation<br>
              • Custom action plan<br>
              • Follow-up resources<br>
              • 7-day email support
            </div>
          </div>

          <button 
            @click="openSavvyCal('strategy')" 
            class="bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105 mb-8"
          >
            Book Your Strategy Session Now
          </button>
        </div>

        <!-- Quick Booking Options -->
        <div class="grid md:grid-cols-3 gap-8 mb-16">
          <!-- Free Chat -->
          <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
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
            <p class="text-gray-600 mb-6 text-center">
              Quick conversation to understand your challenges and see if we're a good fit.
            </p>
            <button 
              @click="openSavvyCal('discovery')" 
              class="w-full bg-green-500 text-white py-3 px-6 rounded-lg font-semibold hover:bg-green-600 transition-colors duration-200"
            >
              Book Free Chat
            </button>
          </div>

          <!-- Strategy Session -->
          <div class="bg-white p-8 rounded-xl shadow-xl border-2 border-primary-200 hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 relative">
            <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-medium">
              Most Popular
            </div>
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
            <p class="text-gray-600 mb-6 text-center">
              Deep dive analysis with a custom 30-day action plan to get results fast.
            </p>
            <button 
              @click="openSavvyCal('strategy')" 
              class="w-full bg-primary-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-primary-700 transition-colors duration-200"
            >
              Book Strategy Session
            </button>
          </div>

          <!-- Workshop Planning -->
          <div class="bg-white p-8 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
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
            <p class="text-gray-600 mb-6 text-center">
              Planning session to design a custom workshop for your team.
            </p>
            <button 
              @click="openSavvyCal('workshop')" 
              class="w-full bg-purple-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-purple-700 transition-colors duration-200"
            >
              Plan Workshop
            </button>
          </div>
        </div>

        <!-- Inline Calendar Embed -->
        <div class="max-w-4xl mx-auto">
          <div class="text-center mb-8">
            <h3 class="text-2xl font-bold text-gray-900 mb-4">
              Select Your Preferred Time
            </h3>
            <p class="text-lg text-gray-600">
              Choose a time that works for you - payment collected securely after booking
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

    <!-- Corporate Training Details -->
    <section id="workshops" ref="workshopsSection" class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">Corporate Training Programs</h2>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Custom workshops designed to transform your team's approach to hiring, inclusion, and second chances.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-12">
          <div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">Popular Workshop Topics</h3>
            <div class="space-y-4">
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <h4 class="font-semibold text-gray-900">Second-Chance Hiring Excellence</h4>
                <p class="text-gray-600 text-sm">Build effective programs that reduce turnover and increase loyalty</p>
              </div>
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <h4 class="font-semibold text-gray-900">Unconscious Bias in Hiring</h4>
                <p class="text-gray-600 text-sm">Identify and eliminate barriers to inclusive recruitment</p>
              </div>
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <h4 class="font-semibold text-gray-900">Managing Diverse Teams</h4>
                <p class="text-gray-600 text-sm">Create environments where everyone can thrive</p>
              </div>
              <div class="bg-white p-4 rounded-lg shadow-sm">
                <h4 class="font-semibold text-gray-900">Building Resilient Organizations</h4>
                <p class="text-gray-600 text-sm">Develop cultures that support growth and transformation</p>
              </div>
            </div>
          </div>

          <div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">Investment & Packages</h3>
            <div class="bg-white p-6 rounded-lg shadow-md mb-6">
              <h4 class="text-xl font-semibold text-gray-900 mb-3">Half-Day Workshop</h4>
              <div class="text-2xl font-bold text-primary-600 mb-3">$1,500</div>
              <ul class="text-gray-600 space-y-1 text-sm">
                <li>• 3-4 hours of interactive training</li>
                <li>• Up to 25 participants</li>
                <li>• Custom materials and handouts</li>
                <li>• Action planning session</li>
              </ul>
            </div>

            <div class="bg-white p-6 rounded-lg shadow-md mb-6">
              <h4 class="text-xl font-semibold text-gray-900 mb-3">Full-Day Intensive</h4>
              <div class="text-2xl font-bold text-primary-600 mb-3">$2,500</div>
              <ul class="text-gray-600 space-y-1 text-sm">
                <li>• 6-7 hours comprehensive training</li>
                <li>• Up to 30 participants</li>
                <li>• Role-playing and case studies</li>
                <li>• Implementation roadmap</li>
                <li>• 30-day follow-up support</li>
              </ul>
            </div>

            <div class="bg-primary-50 p-6 rounded-lg border border-primary-200">
              <h4 class="text-lg font-semibold text-gray-900 mb-3">Ready to Get Started?</h4>
              <p class="text-gray-600 mb-4 text-sm">
                Contact me to discuss your organization's specific needs and create a custom proposal.
              </p>
              <button 
                @click="openSavvyCal('workshop')" 
                class="inline-block bg-primary-600 text-white px-6 py-2 rounded-lg font-semibold hover:bg-primary-700 transition-colors duration-200"
              >
                Schedule Planning Call
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Form -->
    <section id="contact-form" ref="contactSection" class="py-20 bg-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Let's Discuss Your Needs</h2>
          <p class="text-lg text-gray-600">
            Ready to explore how second-chance hiring can transform your organization? Let's talk.
          </p>
        </div>

        <div class="grid md:grid-cols-2 gap-12">
          <div>
            <form class="space-y-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Name *</label>
                <input type="text" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Email *</label>
                <input type="email" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Organization</label>
                <input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Service Interest</label>
                <select class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent">
                  <option>Strategy Consulting</option>
                  <option>Corporate Training</option>