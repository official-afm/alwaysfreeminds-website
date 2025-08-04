<template>
  <div>
    <!-- Hero Section -->
    <section class="relative bg-gradient-to-br from-primary-900 via-primary-800 to-primary-600 text-white">
      <div class="absolute inset-0 bg-black opacity-20"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 lg:py-32">
        <div class="text-center max-w-4xl mx-auto">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 leading-tight">
            Minds of 
            <span class="text-yellow-300">Resilience</span> & 
            <span class="text-yellow-300">Freedom</span>
          </h1>
          <p class="text-xl md:text-2xl mb-8 text-gray-200 max-w-3xl mx-auto leading-relaxed">
            Your mind is always free. Real stories from real people who've discovered mental freedom, 
            even in the toughest situations.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <router-link 
              to="/blog" 
              class="inline-flex items-center justify-center bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
            >
              Read Stories
            </router-link>
            <button
              @click="openConvertKit"
              class="inline-flex items-center justify-center border-2 border-white text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-white hover:text-primary-900 transition-all duration-200 shadow-lg hover:shadow-xl"
            >
              Get Mental Freedom Guide
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Content -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16 max-w-3xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">
            Transforming Lives Through Mental Freedom
          </h2>
          <p class="text-xl text-gray-600 leading-relaxed">
            Every setback is a setup for a comeback. Here's how we're helping people discover 
            the freedom that already exists within their minds.
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-12">
          <!-- Feature 1 -->
          <div class="text-center p-8 bg-gray-50 rounded-xl hover:bg-gray-100 transition-all duration-200 hover:shadow-lg">
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Mental Freedom</h3>
            <p class="text-gray-600 leading-relaxed">
              Discover how your mind can be free regardless of your external circumstances or past experiences.
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="text-center p-8 bg-gray-50 rounded-xl hover:bg-gray-100 transition-all duration-200 hover:shadow-lg">
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Real Stories</h3>
            <p class="text-gray-600 leading-relaxed">
              Authentic experiences from people who've walked the path of transformation and emerged stronger.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="text-center p-8 bg-gray-50 rounded-xl hover:bg-gray-100 transition-all duration-200 hover:shadow-lg">
            <div class="w-16 h-16 bg-primary-100 rounded-xl flex items-center justify-center mx-auto mb-6">
              <svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-4">Practical Guidance</h3>
            <p class="text-gray-600 leading-relaxed">
              Actionable strategies and hard-won wisdom that you can apply to your own journey of mental freedom.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Recent Blog Posts -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16 max-w-3xl mx-auto">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6">Latest Stories</h2>
          <p class="text-xl text-gray-600">Fresh perspectives and insights from the journey to mental freedom</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 lg:gap-12">
          <article v-for="post in featuredPosts" :key="post.id" class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-all duration-300 transform hover:scale-105">
            <img :src="post.image" :alt="post.title" class="w-full h-48 object-cover">
            <div class="p-6">
              <div class="text-sm text-primary-600 font-medium mb-2">{{ post.category }}</div>
              <h3 class="text-xl font-semibold text-gray-900 mb-3 leading-tight">{{ post.title }}</h3>
              <p class="text-gray-600 mb-4 leading-relaxed">{{ post.excerpt }}</p>
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-500">{{ post.date }}</span>
                <router-link to="/blog" class="text-primary-600 font-medium hover:text-primary-700 transition-colors duration-200">
                  Read More →
                </router-link>
              </div>
            </div>
          </article>
        </div>

        <div class="text-center mt-12">
          <router-link 
            to="/blog" 
            class="inline-flex items-center justify-center bg-primary-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-primary-700 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            View All Stories
          </router-link>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-primary-800 text-white py-20">
      <div class="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Discover Your Mental Freedom?</h2>
        <p class="text-xl text-gray-200 mb-10 leading-relaxed max-w-3xl mx-auto">
          Whether you're looking for inspiration, practical guidance, or someone who understands your journey, 
          you're in the right place. Your mind is always free - let us show you how.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <router-link 
            to="/consulting" 
            class="inline-flex items-center justify-center bg-yellow-400 text-gray-900 px-8 py-4 rounded-lg text-lg font-semibold hover:bg-yellow-300 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            Work With Me
          </router-link>
          <button
            @click="openConvertKit"
            class="inline-flex items-center justify-center border-2 border-white text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-white hover:text-primary-900 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            Get Free Guide
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Home',
  setup() {
    const featuredPosts = ref([
      {
        id: 1,
        title: "Finding Mental Freedom Behind Bars",
        excerpt: "How I discovered that my mind could be free even when my body wasn't, and how you can too.",
        category: "Mental Freedom",
        date: "Jan 15, 2024",
        image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=300&fit=crop"
      },
      {
        id: 2,
        title: "The Power of Choosing Your Response",
        excerpt: "Why the space between stimulus and response is where your freedom lives - and how to expand it.",
        category: "Personal Growth",
        date: "Jan 10, 2024",
        image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=300&fit=crop"
      },
      {
        id: 3,
        title: "Building Resilience in Tough Times",
        excerpt: "Practical strategies for maintaining mental strength when everything around you feels out of control.",
        category: "Resilience",
        date: "Jan 5, 2024",
        image: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=400&h=300&fit=crop"
      }
    ])

    const openConvertKit = () => {
      // Trigger ConvertKit form
      if (typeof window !== 'undefined' && window.ml) {
        window.ml('show', 'd89cc074cd')
      }
    }

    return {
      featuredPosts,
      openConvertKit
    }
  }
}
</script>
