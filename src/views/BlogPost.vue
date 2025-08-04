<template>
  <div>
    <!-- Hero Section -->
    <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        <p class="mt-2 text-gray-600">Loading story...</p>
      </div>

      <div v-else-if="!post" class="text-center py-12">
        <h1 class="text-2xl font-bold text-gray-900 mb-4">Story Not Found</h1>
        <p class="text-gray-600 mb-6">The story you're looking for doesn't exist or has been moved.</p>
        <router-link to="/blog" class="text-primary-600 font-medium hover:text-primary-700">
          ← Back to All Stories
        </router-link>
      </div>

      <div v-else>
        <!-- Breadcrumb -->
        <nav class="mb-8">
          <ol class="flex items-center space-x-2 text-sm text-gray-500">
            <li><router-link to="/" class="hover:text-primary-600">Home</router-link></li>
            <li>/</li>
            <li><router-link to="/blog" class="hover:text-primary-600">Blog</router-link></li>
            <li>/</li>
            <li class="text-gray-900">{{ post.title }}</li>
          </ol>
        </nav>

        <!-- Article Header -->
        <header class="mb-8">
          <div class="mb-4">
            <span class="inline-block bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm font-medium">
              {{ post.category }}
            </span>
          </div>
          <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight">
            {{ post.title }}
          </h1>
          <p class="text-xl text-gray-600 mb-6">{{ post.excerpt }}</p>
          
          <!-- Author and Date -->
          <div class="flex items-center space-x-4 pb-6 border-b border-gray-200">
            <img 
              src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=64&h=64&fit=crop&crop=face" 
              alt="Author" 
              class="w-12 h-12 rounded-full"
            >
            <div>
              <div class="font-semibold text-gray-900">{{ post.author }}</div>
              <div class="text-sm text-gray-500">
                {{ formatDate(post.publishedAt) }} • {{ readingTime }} min read
              </div>
            </div>
          </div>
        </header>

        <!-- Featured Image -->
        <div v-if="post.image" class="mb-8">
          <img 
            :src="post.image" 
            :alt="post.title" 
            class="w-full h-64 md:h-96 object-cover rounded-lg shadow-lg"
          >
        </div>

        <!-- Article Content -->
        <div class="prose prose-lg max-w-none mb-12">
          <div v-html="post.content"></div>
        </div>

        <!-- Share Buttons -->
        <div class="border-t border-b border-gray-200 py-6 mb-8">
          <div class="flex items-center justify-between">
            <span class="text-sm font-medium text-gray-700">Share this story:</span>
            <div class="flex space-x-4">
              <button 
                @click="shareOnTwitter"
                class="text-gray-400 hover:text-blue-500 transition-colors duration-200"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/>
                </svg>
              </button>
              <button 
                @click="shareOnLinkedIn"
                class="text-gray-400 hover:text-blue-600 transition-colors duration-200"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
              </button>
              <button 
                @click="shareOnFacebook"
                class="text-gray-400 hover:text-blue-700 transition-colors duration-200"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                </svg>
              </button>
              <button 
                @click="copyLink"
                class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
                :class="{ 'text-green-500': linkCopied }"
              >
                <svg v-if="!linkCopied" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Author Bio -->
        <div class="bg-gray-50 rounded-lg p-6 mb-12">
          <div class="flex items-start space-x-4">
            <img 
              src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&h=80&fit=crop&crop=face" 
              alt="Author" 
              class="w-16 h-16 rounded-full"
            >
            <div>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ post.author }}</h3>
              <p class="text-gray-600 mb-4">
                Gregory spent four years in the Florida Department of Corrections and now uses his experience 
                to help others navigate transformation and reentry. He's a certified Linux professional, 
                web developer, and advocate for second chances.
              </p>
              <div class="flex space-x-4">
                <router-link to="/about" class="text-primary-600 font-medium hover:text-primary-700">
                  Learn More →
                </router-link>
                <router-link to="/contact" class="text-primary-600 font-medium hover:text-primary-700">
                  Work Together →
                </router-link>
              </div>
            </div>
          </div>
        </div>

        <!-- Related Posts -->
        <div v-if="relatedPosts.length > 0" class="mb-12">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Related Stories</h2>
          <div class="grid md:grid-cols-2 gap-6">
            <article 
              v-for="relatedPost in relatedPosts" 
              :key="relatedPost.id"
              class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-200"
            >
              <router-link :to="`/blog/${relatedPost.slug}`">
                <img :src="relatedPost.image" :alt="relatedPost.title" class="w-full h-32 object-cover">
              </router-link>
              <div class="p-4">
                <div class="text-sm text-primary-600 font-medium mb-1">{{ relatedPost.category }}</div>
                <h3 class="text-lg font-semibold text-gray-900 mb-2">
                  <router-link :to="`/blog/${relatedPost.slug}`" class="hover:text-primary-600 transition-colors duration-200">
                    {{ relatedPost.title }}
                  </router-link>
                </h3>
                <p class="text-gray-600 text-sm">{{ relatedPost.excerpt.substring(0, 100) }}...</p>
              </div>
            </article>
          </div>
        </div>

        <!-- Newsletter CTA -->
        <div class="bg-primary-50 rounded-lg p-8 text-center">
          <h3 class="text-2xl font-bold text-gray-900 mb-4">Want More Stories Like This?</h3>
          <p class="text-gray-600 mb-6">
            Get weekly insights and stories of transformation delivered to your inbox.
          </p>
          <form @submit.prevent="subscribeNewsletter" class="max-w-md mx-auto">
            <div class="flex">
              <input 
                v-model="newsletterEmail"
                type="email" 
                required
                placeholder="Enter your email" 
                class="flex-1 px-4 py-2 border border-gray-300 rounded-l-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              >
              <button 
                type="submit" 
                class="px-6 py-2 bg-primary-600 text-white rounded-r-lg font-semibold hover:bg-primary-700 transition-colors duration-200"
              >
                Subscribe
              </button>
            </div>
          </form>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'

export default {
  name: 'BlogPost',
  setup() {
    const route = useRoute()
    const loading = ref(true)
    const post = ref(null)
    const relatedPosts = ref([])
    const newsletterEmail = ref('')
    const linkCopied = ref(false)

    // Mock blog post data - replace with API call
    const mockPost = {
      id: 1,
      title: "Finding Purpose After Prison",
      slug: "finding-purpose-after-prison",
      excerpt: "How I discovered my calling and built a meaningful life after serving four years in the Florida Department of Corrections.",
      content: `
        <p>Four years. That's how long I spent behind bars in the Florida Department of Corrections. When I walked out, I thought the hardest part was over. I was wrong.</p>
        
        <p>The real challenge wasn't surviving inside—it was figuring out how to build a meaningful life on the outside. How do you rebuild when society sees you as broken? How do you find purpose when every door seems closed?</p>
        
        <h2>The Reality of Reentry</h2>
        
        <p>Let me be honest about what reentry really looks like. It's not the Hollywood version where the reformed ex-convict gets a second chance and everything works out. It's checking a box on every job application that immediately puts you in the "no" pile. It's seeing people's expressions change when they learn about your past.</p>
        
        <p>But here's what I learned: the same qualities that help you survive inside—resilience, resourcefulness, the ability to find strength in impossible situations—those are exactly what you need to build something meaningful outside.</p>
        
        <h2>Finding My Voice</h2>
        
        <p>My technical background became my bridge back to the world. Linux certification, web development, the skills I had before—they were still there, waiting to be rebuilt and expanded. But more importantly, I realized I had something else: a story that could help others.</p>
        
        <p>That's when BuyMindInsights was born. Not just as a business, but as a mission to show that transformation is real, that second chances work, and that society benefits when we invest in redemption instead of just punishment.</p>
        
        <h2>The Power of Purpose</h2>
        
        <p>Purpose isn't something you find—it's something you create. For me, it came from understanding that my experience, as painful as it was, gave me something valuable to offer. Every person who emails me saying a blog post helped them, every organization that asks me to speak about second-chance hiring, every small step toward changing how society sees people like me—that's purpose.</p>
        
        <p>Your purpose might be different. Maybe it's being the father your kids deserve. Maybe it's starting a business that employs other people who need second chances. Maybe it's simply showing up every day and proving that people can change.</p>
        
        <h2>What I Want You to Know</h2>
        
        <p>If you're reading this from inside, know that this time can be preparation, not just punishment. Use it to learn, to grow, to plan. The person you become inside will determine the life you build outside.</p>
        
        <p>If you're on the outside, struggling with reentry, know that you're not alone. The challenges are real, but so is the possibility of transformation. Focus on progress, not perfection. Every small step forward matters.</p>
        
        <p>And if you're someone who's never been inside but wants to understand, know that the people coming home from prison are your neighbors, your potential employees, your community members. They're not broken—they're human beings who made mistakes and are working to build better lives.</p>
        
        <p>Purpose isn't about erasing the past. It's about using everything you've learned—including the hardest lessons—to create something meaningful going forward. That's not just possible. It's powerful.</p>
      `,
      category: "Personal Growth",
      author: "Gregory Barber",
      publishedAt: "2024-01-15",
      image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&h=600&fit=crop"
    }

    const mockRelatedPosts = [
      {
        id: 2,
        title: "The Power of Second Chances",
        slug: "power-of-second-chances",
        excerpt: "Why society needs to embrace redemption and how individuals can advocate for meaningful criminal justice reform.",
        category: "Social Justice",
        image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=300&fit=crop"
      },
      {
        id: 3,
        title: "Building Your Support Network",
        slug: "building-support-network",
        excerpt: "Practical steps to find and nurture relationships that will sustain your growth and transformation journey.",
        category: "Community",
        image: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=400&h=300&fit=crop"
      }
    ]

    const readingTime = computed(() => {
      if (!post.value) return 0
      const wordsPerMinute = 200
      const wordCount = post.value.content.replace(/<[^>]*>/g, '').split(/\s+/).length
      return Math.ceil(wordCount / wordsPerMinute)
    })

    const formatDate = (dateString) => {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    }

    const shareOnTwitter = () => {
      const url = encodeURIComponent(window.location.href)
      const text = encodeURIComponent(post.value.title)
      window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, '_blank')
    }

    const shareOnLinkedIn = () => {
      const url = encodeURIComponent(window.location.href)
      window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank')
    }

    const shareOnFacebook = () => {
      const url = encodeURIComponent(window.location.href)
      window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank')
    }

    const copyLink = async () => {
      try {
        await navigator.clipboard.writeText(window.location.href)
        linkCopied.value = true
        setTimeout(() => {
          linkCopied.value = false
        }, 2000)
      } catch (err) {
        console.error('Failed to copy link:', err)
      }
    }

    const subscribeNewsletter = () => {
      // Implement newsletter subscription logic
      console.log('Newsletter subscription:', newsletterEmail.value)
      newsletterEmail.value = ''
      // Show success message
    }

    onMounted(() => {
      // Simulate loading
      setTimeout(() => {
        // In real app, fetch post by route.params.slug
        if (route.params.slug === 'finding-purpose-after-prison') {
          post.value = mockPost
          relatedPosts.value = mockRelatedPosts
        }
        loading.value = false
      }, 500)
    })

    return {
      loading,
      post,
      relatedPosts,
      newsletterEmail,
      linkCopied,
      readingTime,
      formatDate,
      shareOnTwitter,
      shareOnLinkedIn,
      shareOnFacebook,
      copyLink,
      subscribeNewsletter
    }
  }
}
</script>